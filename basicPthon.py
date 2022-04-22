# print("Welcome to Python World")
# firstname=input("inter your first name :")
# lastname=input("inter your last name : ")
# print ("Your full name",firstname,lastname)
# name="sejan"

# name="sajal"
# print(name)
# typeS=type(name)
# print(typeS)

# decimile=3.2;
# print(type(decimile))

# Arithmetic operator
# +,-,*,/,
# num1=10;
# num2=20;
# print(num1+num2);

#Relational Operator : <,>,==,!=
# print(num1>num2);
# print(num1<num2);
# print(num1==num2);
# print(num1!=num2);
# print(num1);

#logical operators : &, |
# log1=True;
# log2=False;
# print(log1 & log1);
# print(log2 & log1);
# print(log2 & log2);
# print(log1 & log2);
# print("Or");
# print(log1 | log1);
# print(log2 | log1);
# print(log2 | log2);
# print(log1 | log2);

# String
# string1='I am sejan';
# string2="I'm sejan";
# string3=''' 
# i am sejan 
# Now I am like yto learn python
# ''';
# print(string1);
# print(string2);
# print(string3);

# string1='I am sejan';
# print(len(string1));
# print(string1[3]);
# print(string1.find('am'));
# print(string1.lower());
# print(string1.upper());
# print(string1.count("sejan"));
# print(string1.replace("sejan","sajal"));
# print(string1.split(" "));


# Data Structures in python
# tuple
# Tup1=(1,2,3);
# tup2=(3,4,6,8,2);
# print(max(tup2));
# print(tup2+Tup1);
# print(Tup1[1]);
# print(Tup1[1:3]);

# list
# list1=[1,2,3,4,5,6,66,4];
# list2=[101.102,103,4,6,22];
# print(max(list1));
# print(list1.append(5));
# print(list1);
# print(list1.pop());
# print(list1+list2);
# print(list2.reverse());
# print(list2.sort());
# print(list2.insert(3,500));
# print(list2);
# print(list2+list1);


# Dictionary
# dic1={"name1":"sejan",
#     "name2":"sajal",
#     "name3":"babu",
# }
# dic2={"num1":"99",
#     "num2":"98",
#     "num3":"97",
# }
# print(dic1.keys());
# print(dic1.values());
# dic1["name4"]="developer";
# print(dic1.update(dic2));
# print(dic1);
# print(dic1.pop("name3"));
# print(dic1);

# set
# set1={"a","a","b","c",1,2,3,3,4,2};
# set2={"d","a","b","c",1,2,3,3,4,2};
# set3={"e","4","b","c",1,2,3,3,4,2};
# print(set1);
# set1.add(5);
# set1.update(set2,set3);
# # print(set1);
# print(set1.union(set2,set3));
# print(set1);
# set1.intersection(set2,set3);
# print(set1.intersection(set2,set3));
# print(set1);
# set1.remove('4');
# print(set1);


# if statement
# a=11;
# b=22;
# c=33;
# if (a>b & a>c):
#     print('a is geterthan b');
# elif (b>c & a>a):
#     print('b is geterthan a')
# else:
#      print('c is geterthan b and a');

# tup1=(1,3,5)
# if 1 in tup1:
#     print('1')

# if tup1[0]==1:
#     print('1==1')


# loops
# i=0;
# n=2;
# while i<=10:
#     print(i);
#     i+=1;

# i=0;
# n=2;
# while i<=10:
#     print(n, "x", i, "=" ,n*i);
#     i+=1;

# l1=['num1',"num2","num3"];
# l2=(1,2,3)

# for i in l1:
#     print(i)
#     for x in l2:
#         print(i,x)
   


# function

# def odd_even(x):
#     if x%2==0:
#         print("odd" ,x);
#     else:
#         print("even",x);

# odd_even(10);


# lamda funtion
lamda_function=lambda x: x+x+x;

print(lamda_function(100))

# lamda with filter
l1=(1,2,3,4,5,6,7,8,9,10)
l2=tuple(filter(lambda x:x%2==0,l1));
print(l2)

l1=(1,2,3,4,5,6,7,8,9,10)
l2=tuple(map(lambda x:x*2,l1));
print(l2)
# lamda with filter
# lamda with filter

