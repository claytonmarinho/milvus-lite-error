# milvus-lite-error

```
docker --version
Docker version 28.0.4, build b8034c0

system_profiler SPHardwareDataType
Hardware:

    Hardware Overview:

      Model Name: Mac mini
      Model Identifier: Macmini9,1
      Model Number: Z12N000G0LL/A
      Chip: Apple M1
      Total Number of Cores: 8 (4 performance and 4 efficiency)
      Memory: 16 GB
      System Firmware Version: 11881.101.1
      OS Loader Version: 11881.101.1
      Serial Number (system):
      Hardware UUID:
      Provisioning UDID:
      Activation Lock Status: Enabled
```

```
docker compose build milvus
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 13.8s (10/10) FINISHED                                                                   docker:desktop-linux
 => [milvus internal] load build definition from Dockerfile                                                           0.0s
 => => transferring dockerfile: 131B                                                                                  0.0s
 => [milvus internal] load metadata for docker.io/library/python:3.13-slim-bullseye                                   1.5s
 => [milvus internal] load .dockerignore                                                                              0.0s
 => => transferring context: 2B                                                                                       0.0s
 => [milvus 1/4] FROM docker.io/library/python:3.13-slim-bullseye@sha256:0d46ec7010093c2a30ae712c3d6fc9d3938ae8d31dc  0.0s
 => [milvus internal] load build context                                                                              0.0s
 => => transferring context: 200B                                                                                     0.0s
 => CACHED [milvus 2/4] WORKDIR /app                                                                                  0.0s
 => [milvus 3/4] RUN pip install pymilvus==2.5.0                                                                     11.4s
 => [milvus 4/4] COPY main.py .                                                                                       0.0s 
 => [milvus] exporting to image                                                                                       0.8s 
 => => exporting layers                                                                                               0.8s 
 => => writing image sha256:f9a458f2102c62a1d8e6cad8c9e7a8b3a9863c62c50b22e8d9684c7a5a316232                          0.0s 
 => => naming to docker.io/library/milvus-lite-error-milvus                                                           0.0s 
 => [milvus] resolving provenance for metadata file                                                                   0.0s 
[+] Building 1/1
 ✔ milvus  Built                                                                                                      0.0s 
docker compose up milvus

[+] Running 2/2
 ✔ Network milvus-lite-error_default     Created                                                                      0.0s 
 ✔ Container milvus-lite-error-milvus-1  Created                                                                      0.0s 
Attaching to milvus-1
milvus-1  | E20250416 15:31:15.666395    14 server.cpp:47] [SERVER][BlockLock][milvus] Process exit
milvus-1  | Start milvus-lite failed
milvus-1  | THREADS >>>>>>>>>>>>>>>: 1
milvus-1  | Failed to create new connection using: 3abd7763cd934d9b9ee8d1758f44e3af
milvus-1  | Traceback (most recent call last):
milvus-1  |   File "/app/main.py", line 6, in <module>
milvus-1  |     client = MilvusClient("./data/milvus_test.db")
milvus-1  |   File "/usr/local/lib/python3.13/site-packages/pymilvus/milvus_client/milvus_client.py", line 60, in __init__
milvus-1  |     self._using = self._create_connection(
milvus-1  |                   ~~~~~~~~~~~~~~~~~~~~~~~^
milvus-1  |         uri, user, password, db_name, token, timeout=timeout, **kwargs
milvus-1  |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
milvus-1  |     )
milvus-1  |     ^
milvus-1  |   File "/usr/local/lib/python3.13/site-packages/pymilvus/milvus_client/milvus_client.py", line 726, in _create_connection
milvus-1  |     raise ex from ex
milvus-1  |   File "/usr/local/lib/python3.13/site-packages/pymilvus/milvus_client/milvus_client.py", line 723, in _create_connection
milvus-1  |     connections.connect(using, user, password, db_name, token, uri=uri, **kwargs)
milvus-1  |     ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
milvus-1  |   File "/usr/local/lib/python3.13/site-packages/pymilvus/orm/connections.py", line 386, in connect
milvus-1  |     raise ConnectionConfigException(message="Open local milvus failed")
milvus-1  | pymilvus.exceptions.ConnectionConfigException: <ConnectionConfigException: (code=1, message=Open local milvus failed)>
milvus-1 exited with code 1
```
