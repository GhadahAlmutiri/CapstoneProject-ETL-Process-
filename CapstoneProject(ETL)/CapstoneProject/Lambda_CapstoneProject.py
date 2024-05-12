import requests
import os
import snowflake.connector as sf
import toml

def load_credentials():
    """
    function for .env variable
    """
    user = os.getenv('user')
    password = os.getenv('password')
    return user, password

def get_snowflake_config():
    """
    function for  .toml file that have snowflake info
    """
    app_config = toml.load('configfile.toml')
    return {
        'account': app_config['sf']['account'],
        'warehouse': app_config['sf']['warehouse'],
        'database': app_config['sf']['database'],
        'schema': app_config['sf']['schema'],
        'role': app_config['sf']['role'],
        'file_format_name': app_config['sf']['file_format_name'],
        'stage_name': app_config['sf']['stage_name'],
        'table': app_config['sf']['table']
    }

def connect_to_snowflake(user, password, snowflake_config):
    """
    function for connect to snowflake
    """
    return sf.connect(user=user, password=password,
                      account=snowflake_config['account'], warehouse=snowflake_config['warehouse'],
                      database=snowflake_config['database'], schema=snowflake_config['schema'], role=snowflake_config['role'])

def lambda_handler(event, context):
    url = 'https://de-materials-tpcds.s3.ca-central-1.amazonaws.com/inventory.csv'
    dest_folder = '/tmp'
    file_name = 'inventory.csv'

    user, password = load_credentials()
    snowflake_config = get_snowflake_config()

    response = requests.get(url)
    response.raise_for_status()
    file_path = os.path.join(dest_folder, file_name)
    with open(file_path, 'wb') as file:
        file.write(response.content)

    with open(file_path, 'r') as file:
        file_content = file.read()
        print(file_content)

    conn = connect_to_snowflake(user, password, snowflake_config)
    cursor = conn.cursor()

    use_warehouse = f"use warehouse {snowflake_config['warehouse']};"
    cursor.execute(use_warehouse)

    use_schema = f"use schema {snowflake_config['schema']};"
    cursor.execute(use_schema)

    create_csv_format = f"create or replace file format {snowflake_config['file_format_name']}  type = 'csv' field_delimiter = ',' ;"
    cursor.execute(create_csv_format)

    create_stg = f"create or replace stage {snowflake_config['stage_name']}  file_format = {snowflake_config['file_format_name']};"
    cursor.execute(create_stg)

    run_put_statement = f"put file://{file_path} @{snowflake_config['stage_name']};"
    cursor.execute(run_put_statement)

    list_stg = f"list @{snowflake_config['stage_name']};"
    cursor.execute(list_stg)

    truncate_table = f"truncate table {snowflake_config['schema']}.{snowflake_config['table']};"
    cursor.execute(truncate_table)

    cp_into_query = f"copy into {snowflake_config['schema']}.{snowflake_config['table']} from @{snowflake_config['stage_name']}/{file_name} file_format = {snowflake_config['file_format_name']} on_error = 'continue';"
    cursor.execute(cp_into_query)

    print("File uploaded successfully into Snowflake!")

    return {
        'statusCode': 200,
        'body': "File uploaded successfully into Snowflake!"
    }
