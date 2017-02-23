import sys
import operator

BIG_NUM = 1000000000000

class Cache:
	def __init__(self,size):
		self.size = size
		self.remaining = size
		self.stored = []
                self.latencies = {}

        def remaining_size(self):
            rsum = 0
            for v in self.stored:
                rsum += sizes[v]
            return self.size - rsum

class Endpoint:
	def __init__(self):
		self.connections = {}
		self.requests = {}
                self.latencies = {}

def test():
	total_saved = 0
	total_requests = 0
	for req in requests:
		Rv = req[0]
		Re = req[1]
		Rn = req[2]

		total_requests += Rn

		for c in endpoints[Re].connections:
			cache = caches[c]
			max_latency = BIG_NUM
			if Rv in cache.stored:
				max_latency = min(endpoints[Re].connections[c],max_latency)
			
		if max_latency < BIG_NUM:
			total_saved += (endpoints[Re].datacenter - max_latency)*Rn

	average_saved = total_saved*1.0/total_requests

	average_saved_mus = average_saved * 1000
	
	print average_saved_mus

def check_correctness():
	for cache in caches:
		total_stored = sum([sizes[Rv] for Rv in cache.stored])
		if total_stored > cache.size:
			print "TOTAL BREAKDOWN!"

def greedy_requests():
	for req in reversed(sorted(requests,key=lambda x: x[2])):
		Rv = req[0]
		Re = req[1]
		candidates = []
		d = endpoints[Re].connections
		for c in sorted(d,key=d.get):
			cache = caches[c]
			if cache.remaining > sizes[Rv]:
				cache.stored.append(Rv)
				cache.remaining -= sizes[Rv]
				break
			
				
def greedy_caches():
    for _ in range(10):
        for c in caches:
            c.sorted = []
            es = c.latencies.keys()
            vids = {}
            for e in es:
                endpoint = endpoints[e]
                for v_id, req_nbr in endpoint.requests.iteritems():
                    s = req_nbr * (endpoint.latencies[v_id] - c.latencies[e]) * 1.0 / sizes[v_id]
                    #s = req_nbr * (endpoint.latencies[v_id] - c.latencies[e])
                    if not (v_id in vids):
                        vids[v_id] = 0
                    vids[v_id] += s
            sorted_vids = sorted(vids.items(), key=operator.itemgetter(1))
            reversed(sorted_vids)
            for (v_id, score) in sorted_vids:
                if sizes[v_id] < c.remaining_size():
                    c.stored.append(v_id)
                    for e in es:
                        endpoints[e].latencies[v_id] = c.latencies[e]
                        


if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = open('me_at_the_zoo.in','r')

data = map(int,f.readline().split())

videos = data[0] #number of videos
points = data[1] #number of endpoints
reqs = data[2] #number of request descriptions
num_caches = data[3] #number of cache servers
capacities = data[4] #capacity of each server

sizes = map(int,f.readline().split()) #Sizes of individual videos

caches = [Cache(capacities) for idx in zip(range(num_caches))]

#For each endpoint: 
endpoints = []
for i in range(0, points):
	L,K = map(int,f.readline().split())#L latency, K number of cache servers	
	#endpts.append([L,K])
	e = Endpoint()
	e.datacenter = L
	for i in range(0,K): #K connections to a cache server from each endpoint
		[c,Lc] = map(int,f.readline().split())
		e.connections[c] = Lc
                caches[c].latencies[i] = Lc
	endpoints.append(e)

requests = []
for j in range(0,reqs):
	Rv,Re,Rn = map(int,f.readline().split())
	#requests.append([Rv,Re,Rn])
	endpoints[Re].requests[Rv] = Rn
	endpoints[Re].latencies[Rv] = endpoints[Re].datacenter 
	requests.append((Rv,Re,Rn,Rn*1.0/sizes[Rv]))

#greedy_memory()
greedy_caches()

#greedy_requests()
check_correctness()
#greedy_requests()
test()
