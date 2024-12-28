def create_profile(name:str,last_name:str,age:int,city:str='Unknown',hobby:str=None):
    return (name,last_name,age,city,hobby)
print(create_profile('John','Smith',27,'Yaffo','comedy'))
print(create_profile('John','Smith',27,'Yaffo'))
print(create_profile('John','Smith',18))
print(create_profile('John','Smith',22))
print(create_profile('John','Smith',18,hobby='comedy'))
print(create_profile('John','Smith',18))