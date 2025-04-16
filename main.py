from pymilvus import MilvusClient, DataType

import threading

print(f"THREADS >>>>>>>>>>>>>>>: {threading.active_count()}")
client = MilvusClient("./data/milvus_test.db")

schema = MilvusClient.create_schema(
        auto_id=False,
        enable_dynamic_field=True,
    )
    # Add fields to schema
schema.add_field(field_name="id", datatype=DataType.VARCHAR, is_primary=True, max_length=50) # SYNONYM_ID
print("✅ Done: Preparing index params...")

print("Done!")