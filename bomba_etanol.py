from bomba_combustivel import BombaCombustivel

class BombaEtanol(BombaCombustivel):
    def __init__(self, quantidade_litros):
        super().__init__(4.50, quantidade_litros)  # Preço do etanol como exemplo