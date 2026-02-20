class ProductCard:
    """Класс, описсывающий карточку товара."""

    def __init__(self, name: str = None, quantity: int = 0, condition: str = 'Принято на учет', provider: str = None, manufacturer: str = None, price: float = 0.0, location: str = None, сountry_of_manufacture: str = None, description: str = None,  weight: float = 0, colour: str = None) -> None:
        """Конструктор класса.

        Args:
            name: наименование товара.
            quantity: количество товара.
            condition: состояние товара.
            provider: поставщик товара.
            manufacturer: производитель товара.
            price: цена товара.
            location: местоположение товара.
            сountry_of_manufacture: страна-производитель товара.
            description: описание товара.
            weight: вес товара.
            colour: цвет товара.
        """

        self.__name = name
        self.__quantity = quantity
        self.__condition = condition
        self.__provider = provider
        self.__manufacturer = manufacturer
        self.__price = price
        self.__location = location 
        self.__сountry_of_manufacture = сountry_of_manufacture
        self.__description = description
        self.__weight = weight
        self.__colour = colour

    def get_name(self) -> str:
        """Геттер наименования товара.
        
        Returns: 
            __name: наименование товара. 
        """

        return self.__name

    def get_quantity(self) -> int:
        """Геттер количества товара.
        
        Returns: 
            __quantity: количество товара. 
        """
        
        return self.__quantity

    def get_condition(self) -> str:
        """Геттер состояния товара.
        
        Returns: 
            __condition: состояние товара. 
        """

        return self.__condition

    def get_provider(self) -> str:
        """Геттер поставщика товара.
        
        Returns: 
            __provider: поставщик товара. 
        """

        return self.__provider

    def get_manufacturer(self) -> str:
        """Геттер производителя товара.
        
        Returns: 
            __manufacturer: производитель товара. 
        """

        return self.__manufacturer

    def get_price(self) -> float:
        """Геттер цены товара.
        
        Returns: 
            __price: цена товара. 
        """

        return self.__price

    def get_location(self) -> str:
        """Геттер местоположения товара.
        
        Returns: 
            __location: местоположение товара. 
        """

        return self.__location

    def get_сountry_of_manufacture(self) -> str:
        """Геттер страны-производителя товара.
        
        Returns: 
            __сountry_of_manufacture: страна-производитель товара. 
        """

        return self.__сountry_of_manufacture

    def get_description(self) -> str:
        """Геттер описания товара.
        
        Returns: 
            __description: описание товара. 
        """

        return self.__description
    
    def get_weight(self) -> str:
        """Геттер веса товара.
        
        Returns: 
            __weight: вес товара. 
        """

        return self.__weight

    def get_colour(self) -> str:
        """Геттер цвета товара.
        
        Returns: 
            __colour: цвет товара. 
        """

        return self.__colour

    def set_name(self, name: str) -> None:
        """Сеттер наименования товара. 
        
        Args:
            name: наименование товара. 

        Raises:
            TypeError: если передан не строковый тип данных. 
        """

        if type(name) == str or type(name) == int or type(name) == float:
            if name.strip():
                self.__name = name
        else:

            raise TypeError('Наименование должно быть строчным типом данных')

    def set_quantity(self, quantity: int) -> None:
        """Сеттер количества товара. 
        
        Args:
            quantity: количество товара. 

        Raises:
            TypeError: если передан не целочисленный тип данных.
            ValueError: если передано отрицательное число.
        """

        if type(quantity) == int:
            if quantity >= 0:
                self.__quantity = quantity
            else:

                raise ValueError('Количество должно быть положительным числом')

        else:

            raise TypeError('Количество должно быть целым числом')

    def set_condition(self, condition: str) -> None:
        """Сеттер состояния товара. 
        
        Args:
            condition: состояние товара. 

        Raises:
            TypeError: если передан не строковый тип данных. 
        """

        if type(condition) == str:
            self.__condition = condition
        else:

            raise TypeError('Состояние должно быть строковым типом данных ')

    def set_provider(self, provider: str) -> None:
        """Сеттер поставщика товара. 
        
        Args:
            provider: поставщик товара. 

        Raises:
            TypeError: если передан не строковый тип данных. 
        """

        if type(provider) == str:
            self.__provider = provider
        else:

            raise TypeError('Название/имя поставщика должно быть строковым типом данных')

    def set_manufacturer(self, manufacturer: str) -> None:
        """Сеттер производителя товара. 
        
        Args:
            manufacturer: производитель товара. 

        Raises:
            TypeError: если передан не строковый тип данных. 
        """
        
        if type(manufacturer) == str:
            self.__manufacturer = manufacturer
        else:

            raise TypeError('Название/имя производителя должно быть строковым типо данных')

    def set_price(self, price: float) -> None:
        """Сеттер цены товара. 
        
        Args:
            price: цена товара. 

        Raises:
            TypeError: если передан не целочисленный или не число с плавающей точкой.
            ValueError: если передано отрицательное число.
        """

        if type(price) == float or type(price) == int:
            if price >= 0:
                self.__price = price
            else:

                raise ValueError('Цена должна быть положительным числом')

        else:

            raise TypeError('Цена должна быть дробным или целым числом')

    def set_location(self, location: str) -> None:
        """Сеттер местоположения товара. 
        
        Args:
            location: местоположение товара. 

        Raises:
            TypeError: если передан не строковый тип данных. 
        """

        if type(location) == str:
            self.__location = location
        else:

            raise TypeError('Местоположение должно быть строковым типом данных')

    def set_сountry_of_manufacture(self, сountry_of_manufacture: str) -> None:
        """Сеттер страны-производителя товара. 
        
        Args:
            сountry_of_manufacture: страна-производитель товара. 

        Raises:
            TypeError: если передан не строковый тип данных. 
        """

        if type(сountry_of_manufacture) == str:
            self.__сountry_of_manufacture = сountry_of_manufacture
        else:

            raise TypeError('Описание должно быть строковым типом данных')

    def set_description(self, description: str) -> None:
        """Сеттер описания товара. 
        
        Args:
            description: описание товара. 

        Raises:
            TypeError: если передан не строковый тип данных. 
        """

        if type(description) == str:
            self.__description = description
        else:

            raise TypeError('Описание должно быть строковым типом данных')
    
    def set_weight(self, weight: int) -> None:
        """Сеттер веса товара. 
        
        Args:
            weight: вес товара. 

        Raises:
            TypeError: если передан не целочисленный или не число с плавающей точкой.
            ValueError: если передано отрицательное число.
        """

        if type(weight) == float or type(weight) == int:
            if weight >= 0:
                self.__weight = weight
            else:

                raise ValueError('Вес должен быть положительным числом')

        else:

            raise TypeError('Вес должен быть дробным или целым числом')

    def set_colour(self, colour:str) -> None:
        """Сеттер цвета товара. 
        
        Args:
            colour: цвет товара. 

        Raises:
            TypeError: если передан не строковый тип данных. 
        """

        if type(colour) == str:
            self.__colour = colour
        else:

            raise TypeError('Цвет должен быть строковым типом данных')

    def deduction_from_accounting(self) -> None:
        """Списание с учета."""

        if self.__condition in ('Состоит на учете', 'Принято на учет'):
            self.__condition = 'Списано с учета'
        else:

            print('Карта уже списана с учета. ')
