def hello(*names):
    for name in names :
        print(f"hello {name}")

def sum(*numbers):
    answer=0
    for number in numbers:
        answer+=number
    return answer       

def multiply(*numbers):
    answer=1
    for number in numbers:
        answer*=number
    return answer    

def student_attribute(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

def my_country(country="burundi"):
    print(f"Hello from {country}")

#A function named concatenate_args that takes any number of string arguments in positional arguments format and concatenates them into a single string


def concatenate_args(*args):
    answer=""
    for arg in args:
        answer+=arg
    return answer

 


#A function named concatenate_kwargs that takes any number of string arguments in keyword arguments  format and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += arg
    return result


    
    
 
    

     


