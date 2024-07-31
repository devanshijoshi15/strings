#strings
# string = "hello"
# string1 = 'hello'
# string2 = '''hello'''
# str1 = "this is a string. \nwe are creating in python." #next line
# print(str1)
# print(string)
# print(string1)
# print(string2)

# str2 = "hello"
# print(len(str2))

# str3 = "world!"
# print(len(str3))

# final_str = str2+ " "+str3
# print(final_str)
# print(len(final_str))

#slicing
# str = "hello world"
# print(str[1:4])
# print(str[0:11]) #way 1
# print(str[6:len(str)]) #way 2 for accessing till last index
# print(str[6:]) #way 3 to access last index
# print(str[:5]) #[0:4] #to tell we need to go from index 0 to index 5
# print(str[-12: -6])

str = "hey! how are you?"
print(str.endswith("hey")) 
print(str.capitalize())
print(str) #return original str
str = str.capitalize() #returns the new str
print(str)
print(str.replace("o", "a"))
print(str.replace("how", "why"))
print(str.find("o")) #returns index of where it occurred first
print(str.find("A"))#it will return -1, bcoz negative index doesnt exist
print(str.count("o"))

# str1 = "tom from japan from asia"
# print(str1.count("from"))
# print(str1.count("a"))

#print the length
# name = input("enter your name: ")
# print("length of your name is: ", len(name))
# char_to_count = input("enter the letter you want to count: ")
# occurrence= name.count(char_to_count)
# print(f"the character occurs: ", occurrence)

#find occurrence
# word = "hi, @dev@nshi"
# print(word.count("@"))