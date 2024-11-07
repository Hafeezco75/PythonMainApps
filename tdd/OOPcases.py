class Human:
    number_of_eyes = 2

    def __init__(self, name, age):
        self._name = name
        self.age = age

    @property
    def age(self):
        return self.__age


    @age.setter
    def age(self, age):
        if 0 > age < 100:
            raise ValueError("Age must be between 0 and 100")
        self.__age = age

    @classmethod
    def create_human(cls, detail):
        name, age = detail.split()
        age = int(age)
        return cls(name, age)


    def decorate(func):
        def wrapper(*args, **kwargs):
           print("***********")
           print(func(*args, **kwargs))
           print("***********")


        return wrapper


    #try:
    #    result = 10 / 0
     #   print(result)


    @decorate
    def show_name(self):
        return "janet"
