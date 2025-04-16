from pymilvus import MilvusClient

import threading

print(f"THREADS >>>>>>>>>>>>>>>: {threading.active_count()}")
client = MilvusClient("./data/milvus_test.db")


