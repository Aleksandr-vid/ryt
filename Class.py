#В терминах ООП описать предметную область.

class Human():
    "Данные человека."
    
    def __init__(self, имя, возраст, вес, рост, телосложение, талант):
        self.имя=имя
        self.возраст=возраст
        self.вес=вес
        self.рост=рост
        self.телосложение=телосложение
        self.талант=талант
        self.полное_описание=(имя, возраст, вес, рост, телосложение, талант)
    def __repr__(self):
        return"Human('%s', %s, %s, %s, '%s', '%s')" % (self.имя, self.возраст, self.вec, self.рост, self.телосложение, self.талант)
first_human=Human('Маслов А.С.', 33, 60, 170, 'худой', 'играет на скрипке')
second_human=Human('Воронова А.В.', 35, 50, 165, 'стройное', 'занимается художественной гимнастикой')
print(first_human.полное_описание, second_human.полное_описание)


 
    
    


    


