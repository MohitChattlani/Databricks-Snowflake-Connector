# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC Create DATABASE bronze_lyr;

# COMMAND ----------

file_location2="/FileStore/tables/business_ops-2.csv"

# COMMAND ----------

business_ops_df=spark.read.csv(file_location2,header=True)

# COMMAND ----------

business_ops_df.show(2,truncate=False)

# COMMAND ----------

display(business_ops_df)

# COMMAND ----------

business_ops_df.write.saveAsTable("bronze_lyr.business_ops")

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from bronze_lyr.business_ops;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from bronze_lyr.business_ops limit 10;