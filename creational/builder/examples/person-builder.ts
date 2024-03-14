export class PersonBuilder {
    private person = new Person();

    newPerson(): void {
     this.person = new Person()
    }

    setName(name: string): this {
      this.person.name = name;
      return this;
    }

    setAge(age: string): this {
      this.person.age = age;
      return this;
    }


    build(): Person {
      return this.person;
    }
}

const builder = new PersonBuilder();
const person = builder.setName('teste').setAge(2).build();
person.newPerson();
const person = builder.setName('teste2').setAge(2).build();
