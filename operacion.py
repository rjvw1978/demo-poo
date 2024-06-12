class Operacion:
    def __init__(self, num1, num2):
        self.__num1=num1
        self.__num2=num2

    def get_num1(self):
        return self.__num1
    def set_num1(self, num1):
        self.__num1=num1

    def get_num2(self):
        return self.__num2
    def set_num2(self, num2):
        self.__num2= num2

class Suma(Operacion):
    def suma(self):
        return self.get_num1() + self.get_num2()

class Resta(Operacion):
    def resta(self):
        return self.get_num1() - self.get_num2()


    

    
        