from typing import Union, Literal


class TypeCar:
    type_list = ["esportivo", "popular", "luxuoso"]

    def __new__(cls, type: Union[Literal["esportivo"], Literal["popular"], Literal["luxuoso"]]) -> str:
        if type in cls.type_list:
            return type
