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
        return"Human('%s', %s, %s, %s,'%s', '%s')" % (self.имя, self.возраст, self.вec, self.рост, self.телосложение, self.талант)
first_human=Human('Маслов А.С.', 33, 60, 170, 'худой', 'играет на скрипке')
second_human=Human('Воронова А.В.', 35, 50, 165, 'стройное', 'занимается художественной гимнастикой')


class Child(Human):
    def __init__(self, имя, возраст, вес, рост, телосложение, талант):
        super().__init__(имя, возраст, вес, рост, телосложение, талант)
        self.характер='капризный'
    def __repr__(self):
        return"Child('%s')" % (self.характер)
child_1=Child('Игорь', 7, 25, 120, 'стройное', 'катается на велосипеде')


class Family():
    def __init__(self, имя, возраст, вес, рост, телосложение, талант ):
        super().__init__(имя, возраст, вес, рост, телосложение, талант)
    def __init__(self, отец, мать, сын):
        self.отец=отец
        self.мать=мать
        self.сын=сын
        self.семья=(отец, мать, сын)
    def __repr__(self):
        return("%s","%s","%s") % (self.отец, self.мать, self.сын)

first_human=Human('Маслов А.С.', 33, 60, 170, 'худой', 'играет на скрипке')       
second_human=Human('Воронова А.В.', 35, 50, 165, 'стройное', 'занимается художественной гимнастикой')
child_1=Child('Игорь', 7, 25, 120, 'стройное', 'катается на велосипеде')
my_family=Family("'Маслов А.С.', 33, 60, 170, 'худой', 'играет на скрипке'",
                "'Воронова А.В.', 35, 50, 165, 'стройное', 'занимается художественной гимнастикой'",
                "'Игорь', 7, 25, 120, 'стройное', 'катается на велосипеде'")

print(my_family.семья)



