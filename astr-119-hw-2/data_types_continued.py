#string
s="I am a string"
print(type(s)) 			#will say str

#boolean (true/false statements)

yes=True
print(type(yes)) 		#boolean true

no=False
print(type(no)) 		#boolean false

#list -- ordered and changable

alpha_list = ["a", "b", "c"] 	#list initialization
print(type(alpha_list)) 		#will say list
print(type(alpha_list[0])) 		#will say str
alpha_list.append("day") 			#adds "day" to the list end
print(alpha_list) 				#prints list

#tuple -- ordered and unchangable

alpha_tuple=("a", "b", "c") 	#tuple initialization
print(type(alpha_tuple)) 		#will say tuple

try:
	alpha_tuple[2]="d" 			#try to replace index 2 with d
except TypeError:				#will not work and will raise TypeError
	print("we cannot add elements to tuples!") #then, print this
print(alpha_tuple) 				#prints the tuple

