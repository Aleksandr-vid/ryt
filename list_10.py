#список где не больше 10 элементов

class Top(list):
    def __init__(self, b):
        if len(b)==10:
            raise ValueError('>10')
        else:
            super().__init__(b)

h=Top([1,2,3,4,5,6,7,8,9,10,])+[11]

print(h)



