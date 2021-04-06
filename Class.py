#В терминах ООП описать предметную область.

class Human():
    'Данные человека.'
    
    def __init__(self, имя, возраст, вес, рост, телосложение, талант):
        self.имя=имя
        self.возраст=возраст
        self.вес=вес
        self.рост=рост
        self.телосложение=телосложение
        self.талант=талант
    def get_полное_описание(self):
        описание=f"{self.имя}, {self.возраст} года, {self.вес} кг., {self.рост} см., { self.телосложение}, {self.талант}.\n"
        return описание.title()
    
first_human=Human('Маслов А.С.', 33, 60, 170, 'худой', 'играет на скрипке')
second_human=Human('Воронова А.В.', 35, 50, 165, 'стройное', 'занимается художественной гимнастикой')
print(first_human.get_полное_описание(),second_human.get_полное_описание())


 
    
    


    


