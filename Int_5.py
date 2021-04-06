#сделать int такой что 2+2=5

class Five(int):
    def __add__(self,s):
        return super().__add__(s+1)

r=Five(2)
n=r+2
print(n)

    
