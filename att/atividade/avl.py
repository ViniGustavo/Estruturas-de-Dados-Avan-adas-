from usuario import Usuario  # Importa a classe do arquivo usuario.py

class AVLUsuarios:
    def __init__(self):
        self.raiz = None

    def altura(self, no):
        if not no:
            return 0
        return no.altura

    def fator_balanceamento(self, no):
        if not no:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))
        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))

        return x

    def rotacao_esquerda(self, x):
        y = x.direita
        T2 = y.esquerda

        y.esquerda = x
        x.direita = T2

        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))

        return y

    def inserir(self, raiz, nome, id, email):
        if not raiz:
            return Usuario(nome, id, email)

        if nome < raiz.nome:
            raiz.esquerda = self.inserir(raiz.esquerda, nome, id, email)
        elif nome > raiz.nome:
            raiz.direita = self.inserir(raiz.direita, nome, id, email)
        else:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))

        balanceamento = self.fator_balanceamento(raiz)

        if balanceamento > 1 and nome < raiz.esquerda.nome:
            return self.rotacao_direita(raiz)

        if balanceamento < -1 and nome > raiz.direita.nome:
            return self.rotacao_esquerda(raiz)

        if balanceamento > 1 and nome > raiz.esquerda.nome:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)

        if balanceamento < -1 and nome < raiz.direita.nome:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz

    def remover(self, raiz, nome):
        if not raiz:
            return raiz

        if nome < raiz.nome:
            raiz.esquerda = self.remover(raiz.esquerda, nome)
        elif nome > raiz.nome:
            raiz.direita = self.remover(raiz.direita, nome)
        else:
            if not raiz.esquerda or not raiz.direita:
                temp = raiz.esquerda if raiz.esquerda else raiz.direita
                raiz = temp
            else:
                sucessor = self.get_min(raiz.direita)
                raiz.nome = sucessor.nome
                raiz.id = sucessor.id
                raiz.email = sucessor.email
                raiz.direita = self.remover(raiz.direita, sucessor.nome)

        if not raiz:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))
        balanceamento = self.fator_balanceamento(raiz)

        if balanceamento > 1 and self.fator_balanceamento(raiz.esquerda) >= 0:
            return self.rotacao_direita(raiz)

        if balanceamento > 1 and self.fator_balanceamento(raiz.esquerda) < 0:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)

        if balanceamento < -1 and self.fator_balanceamento(raiz.direita) <= 0:
            return self.rotacao_esquerda(raiz)

        if balanceamento < -1 and self.fator_balanceamento(raiz.direita) > 0:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz

    def get_min(self, no):
        atual = no
        while atual.esquerda:
            atual = atual.esquerda
        return atual

    def buscar(self, raiz, nome):
        if not raiz:
            return None
        if nome == raiz.nome:
            return raiz
        elif nome < raiz.nome:
            return self.buscar(raiz.esquerda, nome)
        else:
            return self.buscar(raiz.direita, nome)

    def listar_em_ordem(self, raiz):
        if raiz:
            self.listar_em_ordem(raiz.esquerda)
            print(f"Nome: {raiz.nome}, ID: {raiz.id}, E-mail: {raiz.email}")
            self.listar_em_ordem(raiz.direita)
