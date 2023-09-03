class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.proximo = None  # Inicializa a referência para o próximo contato

class AgendaHeroes:
    def __init__(self):
        self.tamanho = 26  # Tamanho da tabela hash (uma para cada letra do alfabeto)
        self.tabela = [None] * self.tamanho  # Inicializa a tabela hash vazia

    def _hash(self, nome):
        # Função hash que calcula o índice com base na primeira letra do nome
        if nome:
            primeira_letra = nome[0].upper()
            if 'A' <= primeira_letra <= 'Z':
                return ord(primeira_letra) - ord('A')
        return None  # Retorna None se o nome for inválido ou não começar com uma letra

    def adicionar_contato(self, nome, telefone):
        indice = self._hash(nome)  # Calcula o índice usando a função hash
        if indice is not None:
            novo_contato = Contato(nome, telefone)  # Cria um novo objeto Contato
            if self.tabela[indice] is None:
                self.tabela[indice] = novo_contato
            else:
                atual = self.tabela[indice]
                anterior = None
                while atual:
                    if atual.nome == nome:
                        atual.telefone = telefone  # Atualiza o número de telefone se o contato já existe
                        return
                    anterior = atual
                    atual = atual.proximo
                anterior.proximo = novo_contato  # Adiciona o novo contato à lista ligada

    def buscar_contato(self, nome):
        indice = self._hash(nome)
        if indice is not None:
            atual = self.tabela[indice]
            while atual:
                if atual.nome == nome:
                    return atual.telefone  # Retorna o número de telefone se o contato for encontrado
                atual = atual.proximo
        return None  # Retorna None se o contato não for encontrado

    def listar_contatos_por_letra(self, letra):
        indice = self._hash(letra)
        contatos = []
        if indice is not None:
            atual = self.tabela[indice]
            while atual:
                contatos.append((atual.nome, atual.telefone))  # Adiciona contatos à lista
                atual = atual.proximo
        return contatos

    def remover_contato(self, nome):
        indice = self._hash(nome)
        if indice is not None:
            atual = self.tabela[indice]
            anterior = None
            while atual:
                if atual.nome == nome:
                    if anterior is None:
                        self.tabela[indice] = atual.proximo  # Remove o contato, atualizando as referências
                    else:
                        anterior.proximo = atual.proximo
                    return True
                anterior = atual
                atual = atual.proximo
        return False  # Retorna False se o contato não for encontrado

    def importar_contatos(self, arquivo_csv):
        try:
            with open(arquivo_csv, 'r') as arquivo:
                linhas = arquivo.readlines()
                for linha in linhas:
                    partes = linha.strip().split(',')
                    if len(partes) == 2:
                        nome, telefone = partes
                        self.adicionar_contato(nome, telefone)  # Adiciona contatos do arquivo CSV
        except FileNotFoundError:
            print("O arquivo não foi encontrado.")

    def menu_interativo(self):
        while True:
            print("\nMenu:")
            print("1. Adicionar contato")
            print("2. Buscar contato por nome")
            print("3. Listar contatos por letra")
            print("4. Remover contato")
            print("5. Importar contatos de arquivo CSV")
            print("6. Sair")
            
            escolha = input("Escolha uma opção: ")
            
            if escolha == '1':
                nome = input("Digite o nome do super-herói: ")
                telefone = input("Digite o telefone: ")
                self.adicionar_contato(nome, telefone)
                print("Contato adicionado com sucesso.")
            elif escolha == '2':
                nome = input("Digite o nome do super-herói: ")
                telefone = self.buscar_contato(nome)
                if telefone:
                    print(f"Telefone do super-herói {nome}: {telefone}")
                else:
                    print("Super-herói não encontrado.")
            elif escolha == '3':
                letra = input("Digite a letra inicial: ").upper()
                contatos = self.listar_contatos_por_letra(letra)
                if contatos:
                    print(f"Contatos com a letra {letra}:")
                    for nome, telefone in contatos:
                        print(f"Nome: {nome}, Telefone: {telefone}")
                else:
                    print("Nenhum contato encontrado com a letra especificada.")
            elif escolha == '4':
                nome = input("Digite o nome do super-herói a ser removido: ")
                if self.remover_contato(nome):
                    print(f"Contato {nome} removido com sucesso.")
                else:
                    print("Super-herói não encontrado.")
            elif escolha == '5':
                arquivo_csv = input("Digite o nome do arquivo CSV para importar contatos: ")
                self.importar_contatos(arquivo_csv)
                print("Contatos importados com sucesso.")
            elif escolha == '6':
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    agenda = AgendaHeroes()
    agenda.menu_interativo()