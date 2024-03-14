# Intenção

Separar a construção de um objeto completo da sua representação de modo que o mesmo processo de construção possa criar diferentes representacoes.

### Visal geral do builder

- O padrao sugere a separacao do codigo que cria e o codigo que uso o objeto
- Trata da criacao de objetos complexos (complexos de verdade)
    - Construtores de varios objetos (composite)
    - Composicao de varios objetos (composite)
    - Algoritmo de criacao do objeto complexo
- Permite a criacao de um objeto em etapas
- Permite method chaining (se vc estiver usando uma programacao fluente)
- O objeto final pode variar de acordo com a necessidade
- É um padrao complexo (Se o objeto e complexo, mas complexo o builder é)

### Estrutura

- Degine a interface de todos os objetos "builder". As etapas de construçãp em comum são definidas aqui.
- Builders concretos implemental a interface de acordo com a sua necessidade. Elas podem produzir produtos de tipos diferentes
- Os produtos finais sao os objetos que o cliente deseja consumir. Eles nao tem uma interface em comum porque podem ser de tipos diferentes.
- A classe "Director" é opcional. Ela pode definir a ordem em que as etapas de construção dos objetos são executadas.

O exemplo é muito simples para o pattern builder, use esse padrao em um objeto verdadeiramente complexo.

### Consequências 

#### Prós
- Separa criacao de utilização
- C cliente não precisa criar objetos diretamente 
- O mesmo código pode construir objetos diferentes.
- Ajuda na aplicação dos principios SRP e OCP (posso criar uma classe que extende de builder para criar outro builder para criar outros objetos complexos) (SOLID)

### Contra

- O codigo final pode ser tornar muito complexo
- 