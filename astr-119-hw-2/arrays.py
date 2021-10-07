x=[0.0, 3.0, 5.0, 2.5, 3.7] 	#define an array
print(type(x)) 					#will say list

#remove element 3 from the array
x.pop(2) 		#elements start from 0
print(x)

#remove the element equal to 2.5
x.remove(2.5)
print(x)

#add an element to the end
x.append(1.2)
print(x)

#make a copy
y=x.copy()
print(y)

#how many elements are 0.0
print(y.count(0.0))

#print the index with value 3.7
print(y.index(3.7))

#sort the list (increasing order)
y.sort()
print(y)

#reverse sort (decreasing order)
y.reverse()
print(y)

#clear all elements
y.clear()
print(y)