# Design Pattern 

O que são padrões de projeto

- são soluções elegantes para problemas conhecidos recorrentes no desenvolvimento de software que foram utilizados e testados no passado e continuam relevantes nos dias atuais.
- foram catalogados e popularizados pelo "padrões de projetos soluções reutilizáveis de software orientados a objetos"
- são divididos em 3 categorias: Criacional (creational), que vivam abstrair o processo de como os objetos sao criacao na aplicaçaão; Estrutural (structural), que lidam com a composição de classes e objetos; Corpotamentais (behavioural), que caracterizam como as classes e objetos interagem e distribuiem responsabilidades na aplicação.
- são APENAS SUGESTÕES de software que podem ser aplicadas a qualquer linguagem de programação.

## Benefícios e Problemas 

### O que é bom

- Você não precisa reiventar a rota
- Padrões universais facilitam o entendimento do seu projeto
- Evita refatoração desnecessária
- Ajuda na reutilização de código (conceito DRY - Don't repeat yourself)
- Abstrai na aplicação dos princípios do design orientado a objetos (SOLID)
- Facilitam a criação de testes unitários

### O que é ruim

- Alguns padrões podem ser complexos até que você os compreenda
- Muito código para atingir um objetivo simples
- Podem trazer otimizações prematuras para o seu código (YAGNI - You Ain't Gonna Need It)
- Se usados incorretamente, podem atrapalhar as invés de ajudar

## Categorias 

##### De Criação

- Abstract Factory 
- Factory Method
- Builder
- Prototype
- Singleton

##### Estrutural

- Adapter
- Bridge
- Composite
- Decorator
- Façade
- Flyweight
- Proxy

##### Comportamental

- Interpreter 
- Template Method
- Chain of Responsability
- Iterator
- Command
- Mediator
- Memento
- Observer
- State
- Strategy
- Visitor


## Príncipios do design orientado a objetos (SOLID)

- Single Responsibility Principle (Princípio da responsabilidade única) - Uma classe deve ter apenas um motivo para mudar
- Open/Closed Principle (Princípio do aberto/fechado) - classes ou objetos e métodos devem estar abertos para extensão, mas fechados para modificações.
- Liskov Substitution Principle (Princípio da substituição de Liskov) - classes derivadas devem ser capazes de substituir totalmente classes-bases
- Interface Segregation Principle (Princípio da segregação de interface) - os clientes não devem ser forçados a depender de interfaces que não utilizam
- Dependency inversion Principle (Princípio da inversão de dependência) - módulos de algo nível não devem ser dependentes de módulos de baixo nível; ambos devem depender de abstrações. Detalahes devem depdender das abstrações, não o inverso.