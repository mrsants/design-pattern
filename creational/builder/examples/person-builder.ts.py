class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def new_person(self):
        self.person = Person()

    def set_name(self, name):
        self.person.name = name
        return self

    def set_age(self, age):
        self.person.age = age
        return self

    def build(self):
        return self.person

# Example usage:
builder = PersonBuilder()
person = builder.set_name('teste').set_age(2).build()
builder.new_person()
person2 = builder.set_name('teste2').set_age(2).build()
