class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
	def insert(self, data):
		"""
		Insert an element at the end of the list
		"""
		node = Node(data)
		if self.head == None:
			self.head = node
		else:
			temp = self.head
			while temp.next:
				temp = temp.next
			temp.next = node
	def __str__(self):
		s = ''
		temp = self.head
		while temp:
			s = s + str(temp.data) + '\t'
			temp = temp.next
		return s.strip()


if __name__ == '__main__':
	mylist = LinkedList()
	mylist.insert(1)
	mylist.insert(2)
	mylist.insert(3)
	print(mylist)