-- type of test 1.not_null 2. unique 3. relationships 4.accepted_value

-- CUSTOMER dimension 
--CUSTOMER_id is not null
select count(*) = 0 from TPCDS.ANALYTICS.CUSTOMER_DIM
where C_CUSTOMER_SK is null;
-- CUSTOMER_Name is not null
select count(*) = 0 from TPCDS.ANALYTICS.CUSTOMER_DIM
where C_FIRST_NAME is null;

-- weekly sales inventory
--WAREHOUSE_SK,ITEM_SK,SOLD_WK_SK is unique
select count(*) =0 from
    (select
    WAREHOUSE_SK,ITEM_SK,SOLD_WK_SK
    from TPCDS.ANALYTICS.WEEKLY_SALES_INVENTORY
    group by 1,2,3
    having count(*)> 1);

    
--relationships test 
select count(*) =0 from
    (select
        dim.I_ITEM_SK
    from TPCDS.ANALYTICS.WEEKLY_SALES_INVENTORY fact
    left join  TPCDS.ANALYTICS.ITEM_DIM dim
    on dim.i_item_sk=fact.item_sk
    where dim.i_item_sk is null);
--accepted_value testing
select count(*)=0 from TPCDS.ANALYTICS.WEEKLY_SALES_INVENTORY
where WAREHOUSE_SK NOT IN (1,2,3,4,5,6);

    
--Adhoc testing
select count(*)=0 from 
    (select C_CURRENT_CDEMO_SK,cd.CD_DEMO_SK
    from TPCDS.RAW.CUSTOMER c
    left join TPCDS.RAW.CUSTOMER_DEMOGRAPHICS cd
    on c.C_CURRENT_CDEMO_SK =cd.CD_DEMO_SK
    where C_CURRENT_CDEMO_SK is  null and CD_DEMO_SK is not null);
