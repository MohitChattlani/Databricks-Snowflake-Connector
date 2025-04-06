# Databricks notebook source
silver_df=spark.table("silver_lyr.business_ops")

# COMMAND ----------

sfOptions = {
  "sfURL"       : "abc12345.us-east-1.snowflakecomputing.com",
  "sfUser"      : "MOHIT_USER",
  "sfPassword"  : "yourStrongPassword",
  "sfDatabase"  : "SALES_DB",
  "sfSchema"    : "PUBLIC",
  "sfWarehouse" : "COMPUTE_WH"
}


# COMMAND ----------

silver_df.write \
  .format("snowflake") \
  .options(**sfOptions) \
  .option("dbtable", "business_ops") \
  .mode("overwrite") \
  .save()   