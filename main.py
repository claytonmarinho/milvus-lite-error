import os
from pymilvus import MilvusClient, DataType

import threading

data_dir = "./data-local"

if not os.path.exists(data_dir):
    os.makedirs(data_dir)
    print("Created data-local dir")

print(f"THREADS >>>>>>>>>>>>>>>: {threading.active_count()}")
client = MilvusClient(f"{data_dir}/milvus_test.db")

schema = MilvusClient.create_schema(
        auto_id=False,
        enable_dynamic_field=True,
    )
    # Add fields to schema
schema.add_field(field_name="id", datatype=DataType.VARCHAR, is_primary=True, max_length=50) # SYNONYM_ID
print("✅ Done: Preparing index params...")

print("Done!")