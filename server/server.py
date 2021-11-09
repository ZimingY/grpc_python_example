import grpc
from concurrent import futures
import time
import test
import serverfunc_pb2
import serverfunc_pb2_grpc

class MyServiceServicer(serverfunc_pb2_grpc.MyServiceServicer):

	def Compute(self, request, context):
		if request.tag == 1:
			value = test.copy(request.num)
			return serverfunc_pb2.Output(intout=value)
		elif request.tag == 2: 
			value = test.tolist(request.num)
			return serverfunc_pb2.Output(listout=value)
		elif request.tag == 3:
			value = test.tostr(request.num)
			return serverfunc_pb2.Output(sout=value)


def run():
	server = grpc.server(futures.ThreadPoolExecutor(
							max_workers=2))
	serverfunc_pb2_grpc.add_MyServiceServicer_to_server(
						MyServiceServicer(), server)
	print('starting server. listen on port 50051')
	server.add_insecure_port('[::]:50051')
	server.start()
	try:
		while True:
			time.sleep(600)
	except KeyboardInterrupt:
		server.stop(0)


if __name__ == '__main__':
	run()	