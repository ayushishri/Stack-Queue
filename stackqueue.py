class stack:
	def __init__(self):
		self.store=[]
		self.count=0

	def push(self,val):
		self.store+=[val]
		self.count+=1
		return 0

	def pop(self):
		rval=self.store[len(self.store)-1]
		self.store=self.store[:len(self.store)-1]
		self.count-=1
		return rval

	def isEmpty(self):
		if (self.count==0):
			return True
		return False

	def printStack(self):
		print (self.store)
		return 0


class queue:
	def __init__(self):
		self.store=[]
		self.count=0

	def enQ(self,val):
		self.store+=[val]
		self.count+=1
		return 0

	def deQ(self):
		rval=self.store[0]
		self.store=self.store[1:]
		self.count-=1
		return [True,rval]
		
	def isEmpty(self):
		if (self.count==0):
			return True
		return False

	def printQ(self):
		print (self.store)
		return 0
