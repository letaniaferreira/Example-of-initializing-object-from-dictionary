class Person(object):
    def __init__(self, name, age):

        self.name=name
        self.age=age

    def __repr__(self):

        return "<Person: {} {}".format(self.name, self.age)

dict = {"let": {"age": 41, "name": "Letania"}, "jota":{"age": 36, "name":"Justin"}}


for key in dict:
    person = Person(dict.get(key).get("name"), dict.get(key).get("age"))
    print person.name
    