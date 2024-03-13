class Singleton:
    _instance = None

    def __init__(self):
        if self._instance is not None:
            raise ValueError("Singleton instance already exists.")
        self._instance = self

    """
    O decorador @classmethod é usado para definir um método de classe em Python. Métodos de classe são métodos que operam na classe em si, em vez de em instâncias específicas da classe.

    No caso do método instance, estamos usando @classmethod porque ele precisa acessar e modificar a variável de classe _instance, que é compartilhada por todas as instâncias da classe Singleton. Não estamos acessando nem modificando atributos de instância específicos, mas sim manipulando o estado da própria classe. Portanto, faz sentido usar um método de classe para isso.
    
    Se não usássemos @classmethod, teríamos que passar a classe Singleton como um argumento para o método instance, o que não seria tão natural. O decorador @classmethod torna o código mais claro e Pythonic, indicando explicitamente que estamos trabalhando com um método que opera na classe em si.
    """
    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


instance1 = Singleton.instance()
instance2 = Singleton.instance()

print(instance1 is instance2)
