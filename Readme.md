# Databricks-Snowflake Connector

This repository contains a series of Databricks notebooks(.py files) designed to demonstrate the process of ingesting data into Databricks, performing transformations, and writing the results to Snowflake.


## Introduction

Efficient data processing often requires integrating multiple platforms. This project showcases how to:

1. **Ingest raw data into Databricks** (Bronze Layer).
2. **Transform the data within Databricks** (Silver Layer).
3. **Load the transformed data into Snowflake** for further analysis.

## Prerequisites

Before using these scripts, ensure you have:

- **Databricks Workspace**: Access to a Databricks environment.
- **Snowflake Account**: With appropriate permissions to create databases, schemas, and tables.
- **Databricks Cluster**: Configured with the Snowflake Spark Connector.
- **Data Source**: Access to the raw data intended for ingestion.

## Workflow Overview

1. **Bronze Layer Ingestion**: Raw data is ingested into Databricks, creating the initial table.
2. **Silver Layer Transformation**: The raw data undergoes cleaning and transformation to prepare it for analysis.
3. **Data Loading to Snowflake**: The transformed data is written from Databricks to a specified table in Snowflake.

## Scripts Overview

- **bronze_layer_ingestion.py**: Handles the ingestion of raw data into Databricks.
- **silver_layer_transformations.py**: Contains functions for data cleaning and transformation.
- **silver_layer_to_snowflake.py**: Manages the connection to Snowflake and writes the transformed data to the specified table.

