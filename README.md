# AgendaSuper-Herois
Explicação Código:

Esse código Python cria duas classes: Contato e AgendaHeroes para gerenciar uma agenda de super-heróis. Vou explicar o código linha por linha:

A classe Contato é criada para representar um único contato de super-herói. Ela possui três atributos: nome, telefone e proximo. nome e telefone armazenam o nome e o número de telefone do super-herói, enquanto proximo é usado para implementar uma lista ligada para lidar com colisões na tabela hash.

A classe AgendaHeroes é criada para representar a tabela hash da agenda. Ela possui os seguintes métodos e atributos:

__init__(self): O construtor da classe inicializa a agenda com um tamanho de 26 (para cada letra do alfabeto) e cria uma tabela vazia (lista de tamanho 26) para armazenar os contatos.

_hash(self, nome): Este método é uma função de hash que calcula o índice com base na primeira letra do nome do super-herói. Ele converte a primeira letra em maiúscula e subtrai o valor ASCII de 'A' para mapear as letras A a Z aos índices de 0 a 25. Se o nome for inválido ou não começar com uma letra, retorna None.

adicionar_contato(self, nome, telefone): Este método adiciona um novo contato à tabela hash. Primeiro, ele calcula o índice usando _hash, cria um novo objeto Contato com o nome e telefone fornecidos e verifica se o índice está vazio. Se estiver vazio, o novo contato é adicionado. Caso contrário, ele percorre a lista ligada (se houver) até encontrar um contato com o mesmo nome e, nesse caso, atualiza o número de telefone. Se nenhum contato com o mesmo nome for encontrado, o novo contato é adicionado à lista.

buscar_contato(self, nome): Este método busca um contato pelo nome fornecido. Ele calcula o índice usando _hash e percorre a lista ligada (se houver) no índice correspondente para encontrar o contato. Se o contato for encontrado, ele retorna o número de telefone; caso contrário, retorna None.

listar_contatos_por_letra(self, letra): Este método lista todos os contatos cujos nomes começam com a letra fornecida. Ele calcula o índice usando _hash e percorre a lista ligada (se houver) no índice correspondente, adicionando os contatos a uma lista e retornando essa lista.

remover_contato(self, nome): Este método remove um contato pelo nome fornecido. Ele calcula o índice usando _hash e percorre a lista ligada (se houver) no índice correspondente para encontrar o contato a ser removido. Se o contato for encontrado, ele é removido e a função retorna True. Caso contrário, retorna False.

importar_contatos(self, arquivo_csv): Este método permite importar contatos de um arquivo CSV fornecido. Ele lê o arquivo linha por linha, divide cada linha em nome e telefone e chama o método adicionar_contato para adicionar o contato à agenda.

menu_interativo(self): Este método cria um menu interativo para o usuário gerenciar a agenda. Ele permite adicionar, buscar, listar, remover e importar contatos com base nas escolhas do usuário.

Finalmente, a instância da classe AgendaHeroes é criada e o método menu_interativo() é chamado para iniciar o menu interativo de gerenciamento da agenda de super-heróis.
