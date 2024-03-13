# Singleton

### Intenção

Garantir que uma classe tenha somente uma instancia no prohrama e fornecer um ponto de acesso global para a mesma.

"Meio que ele quebra o principio da responsabilidade unica por fazer mais de uma coisa"

### Somente uma instancia?

- Geralmente usado para acesso a recursos compartilhados, como acesso à base de dados, interfaces gráficas, sistema de arquivos, servidores de impressao, logger e mais.
- Também usado para substitutir variaveis globais, como em casos de usos de objetos de configuracoes do sistema como um todo.

### Ponto de acesso global?

- Voce pode permitir acesso global ao singleton em todo sua aplicacao, assim como faziamos (ou fazemos) com variaveis globais.
- Uma vantagem do singleton e que podemos proteger a instancia com encapsulamento, evitando que outro codigo sobrescreva seu valor

### Estrutura

- Atributo privado para a instancia
- Qulquer dados necessario para o singleton
- Construror privado nao permite o uso do new com o singleton. tambem nao ha parametros aqui.
- Getter para instance - aqui decidimos se criamos uma nova instancia ou retornamos a instancia ja criada

### Consequências 

#### Prós

- Acesso controlado à instancia unica
- E facil permitir um numero maior de instancias caso muda de ideia
- Usa lazy instantiotion, o singleton so e criado no momento do uso
- Substitui variaveis globais

#### Contras
- É mais dificil de testar
- Viola o principio da responsabilidade unica 
- Requer tratamento especial em casos de concorrencia
- Erich Gamma descreveu que este seria o unico padrao que ele removeria se fosse refatorar o livro design pattern

