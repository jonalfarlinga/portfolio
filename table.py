import os
from azure.data.tables import TableServiceClient

TABLE_CONNECTION_STRING = os.environ.get("TABLE_CONNECTION_STRING")
if not TABLE_CONNECTION_STRING:
    raise ValueError("TABLE_CONNECTION_STRING is not set.")


class CounterTable:
    def increment(self):
        with TableServiceClient.from_connection_string(
            conn_str=TABLE_CONNECTION_STRING
        ) as table_service:
            with table_service.get_table_client("counter") as table_client:

                try:
                    entity = table_client.get_entity("counter", "counter")
                    count = entity["count"] + 1
                    entity["count"] = count
                    table_client.update_entity(entity=entity)
                except Exception as e:
                    print(e)
                    table_client.create_entity(
                        entity={
                            "PartitionKey": "counter",
                            "RowKey": "counter",
                            "count": 1
                        }
                    )
                    count = 1
                finally:
                    return count
