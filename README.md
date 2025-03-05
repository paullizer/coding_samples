# Coding Samples Repository

## Overview

This repository contains Python scripts demonstrating how to interact with Azure OpenAI, SQL Server, and Cosmos DB. The examples showcase different approaches to querying data, sending messages to Azure OpenAI, and persisting responses in Cosmos DB.

## Repository Structure

```
📁 coding_samples
├── get_data_from_sql_send_message_to_azure_openai_using_sdk_save_to_cosmos.py
├── get_data_from_sql_send_message_to_azure_openai_using_sdk.py
├── send_message_to_azure_openai_using_rest.py
└── send_message_to_azure_openai_using_sdk.py
```

## Requirements

Before running the scripts, install the required dependencies using:

```sh
pip install openai pyodbc requests azure-cosmos
```

## Scripts

1. `get_data_from_sql_send_message_to_azure_openai_using_sdk_save_to_cosmos.py`

   - Queries data from SQL Server.

   - Sends a query result to Azure OpenAI via SDK.

   - Saves the response to Azure Cosmos DB.

2. `get_data_from_sql_send_message_to_azure_openai_using_sdk.py`

   - Queries data from SQL Server.

   - Sends a query result to Azure OpenAI using the SDK.

3. `send_message_to_azure_openai_using_rest.py`
   - Sends a message to Azure OpenAI using the REST API.

4. `send_message_to_azure_openai_using_sdk.py`
   - Sends a message to Azure OpenAI using the SDK.

## Configuration

### Azure OpenAI Service

Replace placeholders in the scripts with actual values:

```python
azure_endpoint_url = "https://your-azure-openai-endpoint/"
deployment_name = "your-deployment-name"
sas_key = "your-api-key"
```

### SQL Server Connection

Replace database connection details:

```python
server = 'your_server'
database = 'your_database'
username = 'your_username'
password = 'your_password'
```

### Cosmos DB Configuration (If applicable)

Replace Cosmos DB details:

```python
cosmos_endpoint = "your_cosmos_endpoint"
cosmos_key = "your_cosmos_key"
database_name = "your_cosmos_database"
container_name = "your_cosmos_container"
```

## Running the Scripts

Execute any script using:

```sh
python script_name.py
```

## Notes

- Ensure your Azure OpenAI and Cosmos DB services are properly configured.
- SQL Server must be accessible from the script's environment.
- Use secure methods to store credentials instead of hardcoding them in scripts.

## License

This project is licensed under the MIT License.