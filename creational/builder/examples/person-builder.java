
public class PersonBuilder {
    private Person person;

    public PersonBuilder() {
        this.person = new Person();
    }

    public void newPerson() {
        this.person = new Person();
    }

    public PersonBuilder setName(String name) {
        this.person.setName(name);
        return this;
    }

    public PersonBuilder setAge(int age) {
        this.person.setAge(age);
        return this;
    }

    public Person build() {
        return this.person;
    }
}
