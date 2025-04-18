# Databricks notebook source
# MAGIC %sql
# MAGIC Create DATABASE if not exists silver_lyr;

# COMMAND ----------

bronze_df=spark.table("bronze_lyr.business_ops")

# COMMAND ----------

from pyspark.sql.functions import col,cast

# COMMAND ----------

silver_df=bronze_df.withColumn("level",col("level").cast("integer"))\
                    .withColumn("value",col("value").cast("integer"))

# COMMAND ----------

display(silver_df)

# COMMAND ----------

silver_df.write.saveAsTable("silver_lyr.business_ops")

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from silver_lyr.business_ops;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from silver_lyr.business_ops limit 10;