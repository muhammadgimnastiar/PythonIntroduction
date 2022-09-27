print("hello world")
print(type("hello colab"))

print("")
print(type(10))
print(type(10.0))
print("")


list1=['kimia','fisika',1993,2017]
list2=[1,2,3,4,5]
list3=["a","b","c","d","e"]
print(type(list1))
print(type(list2))
print(type(list3))
print("")
print ("list1[2]: ", list1[2])
print ("list2[1:5]: ", list2[1:5])
print("")

list1[2] = "biologi"
print ("Nilai baru ada pada index 2 : ", list1[2])
print("")

tup1 = ('fisika', 'kimia', 1993, 2017)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
print(type(tup1))
print(type(tup2))
print(type(tup3))
print("")
print ("tup1[0]: ", tup1[0])
print ("tup3[1:4]: ", tup3[1:4])
print("")
a = range(0,10)
print(a) 
print(list(a))
print(type(a))
print("")


dict1 = {'Nama': 'Seneca', 'Umur': 15, 'Kelas': '10'} 

for i in dict1:
 print(i)
print(type(dict1))
print("dict1['Nama']: ",
dict1['Nama']) 
print("dict1['Umur']: ",
dict1['Umur'])
print("")
dict1['Hobby'] = "Merenung"
dict1['Umur'] = 20;
print(dict1)

print("")
print(type(True))
print(type(False))
print("")



a = 5
print(a)
print(type(a)) 
a = "Ganti Variable" 
print(a)
print(type(a)) 
print("")

print(5+7)
print("")

print("Hallo" + " dunia")
print("")

print([1,2,3,4] + [5,6,7,8])
print("")

a = 5
b = 10
print(a+b)
print("")

print("Contoh casting int ke string")
x = 1 
print(type(x))
x = str(x)
print(type(x)) 
print("")

a = "hello"
b = 10
print(a + " Colab, kamu berumur " + str(b) + " tahun")
print("")

print("contoh casting list menjadi tuple")
ini_list = [1,1,2,3,4,5]
print(type(ini_list))
ini_tuple = tuple(ini_list)
print(type(ini_tuple))
print("")

a = 33
b = 200
if b > a:
 print("b is greater than a")
print("")

a = 33
b = 33
if b > a:
 print("b is greater than a")
elif a == b:
 print("a and b are equal")
print("")

a = 200
b = 33
if b > a:
 print("b is greater than a")
elif a == b:
 print("a and b are equal")
else:
 print("a is greater than b")
print("")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
 print(x)
print("")
for x in "banana":
 print(x)
print("")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
 print(x)
 if x == "banana":
  break
print("")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
 if x == "banana":
  continue
 print(x)
print("")
for x in range(6):
 print(x)
print("")
i = 1
while i < 6:
 print(i)
 i += 1
print("")

def my_function():
 print("Hello from a function")
my_function()
print("")

def my_function(fname):
 print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
print("")

def my_function(fname, lname):
 print(fname + " " + lname)
my_function("Emil", "Refsnes")
print("")