# Databricks notebook source
# MAGIC %run /rchackoair/Utlilities

# COMMAND ----------

list_table_info = [
    ("STREAMING UPDATE", "plane", 100),
    ("STREAMING UPDATE", "flight", 200),
    ("STREAMING UPDATE", "Airport", 100),
    ("STREAMING UPDATE", "cancellation", 100),
    ("STREAMING UPDATE", "unique_carriers", 500),
    ("Write", "airline", 10),
]
for i in list_table_info:
    f_count_check("cleansed_rchackoair", i[0], i[1], i[2])