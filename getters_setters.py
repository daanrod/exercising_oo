class Alarme:
 
    def __init__(self) -> None:
        self.__estado = False

    def get_estado(self) -> bool:
        return self.__estado

    def set_estado(self, valor: bool) -> None:
        if isinstance(valor, bool):
            self.__estado = valor
        else:
            print('Only booleans are accepted!')