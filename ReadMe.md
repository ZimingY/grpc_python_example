a very basic example about using grpc in python.

Define the input and output of server in `server/serverfunc.proto`.

Then run

`python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. serverfunc.proto` in `server/` to generate the `*_pb2.py` and `*pb2_grpc.py`, which are necessary for grpc server. 

`docker compose build`

`docker compose up`


The funcitons are just for concept proof:

tag = 1, input integer `a`, output `a`

tag = 2, input `a`, output `[a,a,a]`

tag = 3, input `a`, output `"a"`


