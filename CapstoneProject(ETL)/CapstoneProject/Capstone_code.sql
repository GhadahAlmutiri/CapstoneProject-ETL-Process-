CREATE OR REPLACE DATABASE TPCDS;
CREATE OR REPLACE SCHEMA RAW;

CREATE OR REPLACE table TPCDS.RAW.inventory (
inv_date_sk int NOT NULL,
inv_item_sk int NOT NULL,
inv_quantity_on_hand int,
inv_warehouse_sk int NOT NULL
);
