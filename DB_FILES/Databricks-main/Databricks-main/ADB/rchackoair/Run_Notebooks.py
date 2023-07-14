# Databricks notebook source
dbutils.widgets.text("Layer_Name","")
Layer_Name=dbutils.widgets.getArgument("Layer_Name")

# COMMAND ----------

Notebook_Path_Json = {
    "Raw": ["/rchackoair/Raw_Sourcing/Raw_Plane"],
    "Cleansed": [
        
            "/rchackoair/Cleansing/Airlines",
            "/rchackoair/Cleansing/Airport",
            "/rchackoair/Cleansing/Cancellation",
            "/rchackoair/Cleansing/Flight",
            "/rchackoair/Cleansing/Plane",
            "/rchackoair/Cleansing/Unique_Carrier",
        
    ],
    "Data_Quality_Cleansed": 
        ["/rchackoair/Data_Quality_Notebook/Cleansing_Data_Quality"]
    ,
    "Mart": 
        [
            "/rchackoair/Mart/Dim_Airlines",
            "/rchackoair/Mart/Dim_Airport",
            "/rchackoair/Mart/Dim_Plane",
            "/rchackoair/Cleansing/Dim_UniqueCarrier",
            "/rchackoair/Mart/Dim_Cancellation",
            "/rchackoair/Mart/Reporting_Flight",
            
        
    ],
    "Data_Quality_Mart":["/rchackoair/Data_Quality_Notebook/Excecute_Mart_Data_Quality"]
}

# COMMAND ----------

for notebook_paths in Notebook_Path_Json[Layer_Name]:
    dbutils.notebook.run(notebook_paths,0)
