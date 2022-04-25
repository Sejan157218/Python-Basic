# class Student():
#     def set_name(self,name):
#         self.name=name;

#     def set_result(self,result):
#         self.result=result;

#     def show_name(self):
#          print("Student name is ",self.name);
#     def show_result(self):
#          print("Student name is ",self.result);

# # stu=Student();
# # stu.set_name("sejan");
# # stu.set_result(99);
# # stu.show_name();
# # stu.show_result();

# # simple inheritance class
# class Employee:
#     def __init__(self,name,age,salary):
#         self.name=name;
#         self.age=age;
#         self.salary=salary;

#     def show_employee_details(self):
#         print("Employee name is ",self.name);
#         print("Employee age is ",self.age);
#         print("Employee salary is ",self.salary);


# employee=Employee("sejan",25,20000);
# # employee.show_employee_details();

# # simple inheritance class with super class
# class Employee2(Employee):
#     def show_employee_details2(self):
#         print("I am employee2");

# employee2=Employee2("sajal",26,25000);

# employee2.show_employee_details();


# class Employee3(Employee):
#     def __init__(self, name, age, salary,experience,joining_date):
#         super().__init__(name, age, salary);
#         self.experience=experience;
#         self.joining_date=joining_date;

#     def show_employee_details3(self):
#         print("I am employee3");
#         print("my experience =",self.experience);
#         print("my joining date =",self.joining_date);

# employee3=Employee3("babu",26,25000,"2 yrs",2019);

# employee3.show_employee_details();
# employee3.show_employee_details3();



# multiple inheritance

# class Parent1():
#     def assign_string_one(self,string1):
#         self.string1=string1;
#     def show_string_one(self):
#         return self.string1;


# class Parent2():
#     def assign_string_two(self,string2):
#         self.string2=string2;
#     def show_string_two(self):
#         return self.string1;

# class Child(Parent1,Parent2):
#     def assign_string_three(self,string3):
#         self.string3=string3;
#     def show_string_three(self):
#         return self.string3;


# child=Child();
# child.assign_string_one("one");
# child.assign_string_two("two");
# child.assign_string_three("three");
# print(child.show_string_one());
# print(child.show_string_two());
# print(child.show_string_three());


# multi-level inheritance

class Parent():
    def set_name(self,name):
        self.name=name;
    def show_name(self):
        return self.name;

class Child(Parent):
    def set_age(self,age):
        self.age=age;
    def show_age(self):
        return self.age;

class GrandChild(Child):
    def  set_gender(self,gender):
        self.gender=gender;
    def show_gender(self):
        return self.gender;

granchild=GrandChild();

granchild.set_name("sejan");
granchild.set_age("25");
granchild.set_gender("male");
print(granchild.show_name());
print(granchild.show_age());
print(granchild.show_gender());
