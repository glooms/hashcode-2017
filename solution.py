import numpy as np

class Cache:
	def __init__(self,size):
		self.size = size

class Endpoint:
	pass

f = open('me_at_the_zoo.in','r')

data = map(int,f.readline().split())

videos = data[0] #number of videos
endpoints = data[1] #number of endpoints
requests = data[2] #number of request descriptions
caches = data[3] #number of cache servers
capacities = data[4] #capacity of each server

sizes = map(int,f.readline().split()) #Sizes of individual videos

caches = [Cache(capacities) for idx in zip(range(caches))]

#For each endpoint: 
endpoints = []
for i in range(0,endpoints):
	[L,K] = map(int,f.readline().split())#L latency, K number of cache servers	
	#endpts.append([L,K])
	print K
	e = Endpoint()
	e.datacenter = L
	for i in range(0,K): #K connections to a cache server from each endpoint
		[c,Lc] = map(int,f.readline().split())
		e.connections[c] = Lc
	endpoints.append(e)

requests = []
for j in range(0,requests):
	[Rv,Re,Rn] = map(int,f.readline().split())
	#requests.append([Rv,Re,Rn])
	endpoints[Re].requests[Rv] = Rn






	
