import zmq, time, pickle, sys

context = zmq.Context()
me = str(sys.argv[1])
s = context.socket(zmq.PUSH) # create a push socket
p1 = "tcp://"+ SRC1 +":"+ PORT1 # address first task source
p2 = "tcp://"+ SRC2 +":"+ PORT2 # address second task source
s.bind(p) # bind socket to address
s.connect(p1) # connect to task source 1
s.connect(p2) # connect to task source 2

while True: # generate 100 workloads
    pass
    #workload = random.randint(1, 100) # compute workload
    #s.send(pickle.dumps((me,workload))) # send workload to worker
    #work = pickle.loads(r.recv()) # receive work from a source
    #time.sleep(work[1]*0.01) # pretend to work