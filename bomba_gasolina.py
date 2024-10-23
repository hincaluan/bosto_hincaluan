from bomba_combustivel import BombaCombustivel
# Classe para Bomba de Gasolina
class BombaGasolina(BombaCombustivel):
    def __init__(self, quantidade_litros):
        super().__init__(5.50, quantidade_litros)  # Preço da gasolina como exemplo

    def abastecer_por_valor_com_aditivo(self, valor):
        preco_aditivo = self.__preco_por_litro * 1.05  # Aumento de 5% para gasolina com aditivo
        litros = valor / preco_aditivo
        if litros <= self.get_quantidade_litros():
            self._BombaCombustivel__quantidade_litros -= litros  # Acesso ao atributo protegido
            return litros
        else:
            raise ValueError("Quantidade de litros insuficiente.")
        
    def abastecer_por_litro_com_aditivo(self, litros):
        if litros > self.quantidade_disponivel:
            return -1
        valor = litros * (self.valor_litro * 1.05)
        self.quantidade_disponivel -= litros
        return valor