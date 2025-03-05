# pip install openai
# pip install pyodbc

from openai import AzureOpenAI
import pyodbc
from azure.cosmos import CosmosClient

# ----------------------------
# Azure OpenAI Service details
# ----------------------------
azure_endpoint_url = "https://aoai-apav-test.openai.azure.us/"  # Replace with your Azure OpenAI endpoint
deployment_name = "gpt-4o"  # Replace with your model deployment name
sas_key = "your_key_here"  # Replace with your actual SAS key

# Authenticate using SAS key
client = AzureOpenAI(
    azure_endpoint=azure_endpoint_url,
    api_version="2024-05-01-preview",
    api_key=sas_key
)

# ----------------------------
# Database connection details
# ----------------------------
server = 'your_server'  # Replace with your server name
database = 'your_database'  # Replace with your database name
username = 'your_username'  # Replace with your username
password = 'your_password'  # Replace with your password

# Establish a database connection
connection = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
)
cursor = connection.cursor()

# Define the SQL query
query = """
SELECT TOP 1 *
FROM your_table
WHERE some_column = 'some_value'
ORDER BY another_column DESC
"""  # Replace with your actual query

cursor.execute(query)
result = cursor.fetchone()
cursor.close()
connection.close()


# ----------------------------
# Define the chat prompt
# ----------------------------
chat_prompt = [ 
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": "You are an AI assistant that helps people find information."
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": f"The result from the database query is: {result}"
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "How do I decide which ontology framework to use?"
            }
        ]
    }
]

# ----------------------------
# Send to Azure OpenAI
# ----------------------------
completion = client.chat.completions.create(  
    model=deployment_name,  
    messages=chat_prompt,
    max_tokens=800, # Maximum number of tokens to generate
    # Streaming is when the model returns a response before it has finished processing the entire request
    # if set to False, the model will only return a response after it has finished processing the entire request.
    # It makes it seem like the model is responding faster because the user starts to see a response
    # Its more about the user experience than anything else.
    stream=False # Set to True to enable streaming, 
) 

# Print the assistant's response
print(completion.choices[0].message.content)


# ----------------------------
# Cosmos DB connection details
# ----------------------------
cosmos_endpoint = "your_cosmos_endpoint"  # Replace with your Cosmos DB endpoint
cosmos_key = "your_cosmos_key"  # Replace with your Cosmos DB key
database_name = "your_cosmos_database"  # Replace with your Cosmos DB database name
container_name = "your_cosmos_container"  # Replace with your Cosmos DB container name

# Create a Cosmos client
cosmos_client = CosmosClient(cosmos_endpoint, cosmos_key)
database = cosmos_client.get_database_client(database_name)
container = database.get_container_client(container_name)

# ----------------------------
# Prepare the data to be saved
# ----------------------------
data_to_save = {
    "id": "unique_id",  # Replace with a unique identifier for the document
    "user_message": "How do I decide which ontology framework to use?",
    "ai_model": deployment_name,
    "query_result": result,
    "assistant_response": completion.choices[0].message.content
}

# ----------------------------
# Save the data to Cosmos DB
# ----------------------------
container.upsert_item(data_to_save)