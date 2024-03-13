# Abstract Factory

### Intenção
A intenção do padrão Abstract Factory é fornecer uma interface para a criação de famílias de objetos relacionados ou dependentes, sem a necessidade de especificar suas classes concretas.

### Motivação
Em certos cenários, um sistema pode precisar criar diferentes famílias de objetos, mas é importante evitar o acoplamento entre o código cliente e as classes concretas desses objetos. O padrão Abstract Factory resolve esse problema ao definir interfaces para cada família de objetos e fornecer uma fábrica abstrata que encapsula a criação de objetos concretos.

### Estrutura

- **Abstract Factory**: Define uma interface para a criação de objetos de uma família.
- **Concrete Factory**: Implementa a interface da fábrica abstrata e é responsável por criar os objetos de uma família específica.
- **Abstract Product**: Define a interface dos objetos que serão criados pela fábrica abstrata.
- **Concrete Product**: Implementa a interface do produto definida pela fábrica abstrata.
- **Client**: Utiliza as interfaces declaradas pelas fábricas e produtos abstratos, não dependendo de classes concretas.

### Aplicabilidade

O padrão Abstract Factory é útil quando:

- Um sistema deve ser independente de como seus produtos são criados, compostos ou representados.
- Um sistema deve ser configurado com uma família de produtos que podem ou não trabalhar juntos.
- Uma família de objetos é projetada para ser usada em conjunto e é necessário garantir essa restrição.
- Você quer fornecer uma biblioteca de classes de produtos e deseja revelar apenas interfaces, não suas implementações.

### Prós e Contras

#### Prós
- Os produtos são sempre compatíveis entre si.
- Aplicação clara do princípio Aberto/Fechado (Open/Closed principle); é fácil adicionar novas fábricas e produtos.
- Aplicação clara do Princípio da Responsabilidade Única (Single Responsibility Principle); o código que cria está separado do código que usa os objetos.

#### Contras
- Introduz muitas classes e aumenta a complexidade do código.
