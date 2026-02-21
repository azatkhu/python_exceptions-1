from ProductCard import ProductCard

class Menu:
    """Класс, описывающий взаимодействие с пользователем."""

    def __init__(self) -> None:
        """Конструктор класса."""

        self.__choice = 0
        self.__list_of_cards = []
        self.__text_products = '''
⬛️⬜️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬛️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬛️⬛️⬜️⬛️⬛️⬛️⬜️⬛️
⬛️⬛️⬛️⬜️⬛️⬛️⬜️⬛️⬛️⬛️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬛️⬛️⬛️⬜️⬛️
⬛️⬛️⬛️⬜️⬛️⬛️⬜️⬛️⬛️⬛️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬛️⬛️⬛️⬜️⬛️
⬛️⬛️⬛️⬜️⬛️⬛️⬜️⬛️⬛️⬛️⬜️⬛️⬜️⬜️⬜️⬛️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬛️
⬛️⬛️⬛️⬜️⬛️⬛️⬜️⬛️⬛️⬛️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬜️⬜️⬜️⬛️⬜️⬛️⬛️⬛️⬛️⬜️⬛️⬜️⬛️⬜️⬛️
⬛️⬛️⬛️⬜️⬛️⬛️⬜️⬛️⬛️⬛️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬛️⬛️⬛️⬛️⬜️⬛️⬜️⬛️⬜️⬛️
⬛️⬛️⬛️⬜️⬛️⬛️⬛️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬛️⬛️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬛️
        '''

    def show_card(self, product: ProductCard = None) -> None:
        """Показывает всю информацию выбранного товара."""

        print('-------------------------------------------------------------------------------------------------------------------')
        print('Название товара: ', product.get_name())
        print('Количество товара: ', product.get_quantity())
        print('Состояние товара: ', product.get_condition())
        print('Поставщик товара: ', product.get_provider())
        print('Производитель товара: ', product.get_manufacturer())
        print('Цена товара(в рублях): ', product.get_price())
        print('Местоположение товара: ', product.get_location())
        print('Описание товара: ', product.get_description())
        print('Страна-производитель товара: ', product.get_сountry_of_manufacture())
        print('Вес товара: ', product.get_weight())
        print('Цвет товара: ', product.get_colour())
        print('-------------------------------------------------------------------------------------------------------------------')
    
    def action_choice(self, product: ProductCard = None, accounting: str = '') -> None:
        """Меню выбора действий для редактирования параметров товара.
        
        Args: 
            product: экземпляр класса ProductCard, параметры которого надо редактировать. 
            accounting: строка, определяющая режим учета. 

        Raises: 
            ValueError: передано число, выходящее за диапазон или передано отрицательное число или введено некорректное значение. 
        """

        inProcess = 1
        
        while inProcess:
            self.show_card(product)

            input('Нажмите ENTER, чтобы продолжить. ')
            print('-------------------------------------------------------------------------------------------------------------------')
            print('Наименование товара --- 1')
            print('Количество товара --- 2')
            print('Состояние товара --- 3')
            print('Поставщик товара --- 4')
            print('Производитель товара --- 5')
            print('Цена товара --- 6')
            print('Местоположение товара --- 7')
            print('Описание товара --- 8')
            print('Страна-производитель товара --- 9')
            print('Вес товара --- 10')
            print('Цвет товара --- 11')
            print('Выход: 0')
            print('-------------------------------------------------------------------------------------------------------------------')

            incorrect_value = 1
            
            while incorrect_value:
                try: 
                    choice = int(input('Выберите параметр: '))
                    
                    if choice not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11):
                        raise ValueError('Нужно ввести число от 0 до 11 включительно. ')

                except ValueError as e:
                    print(f'Введено некорректное значение: {e}')

                else:
                    incorrect_value = 0

            print('-------------------------------------------------------------------------------------------------------------------')

            match choice:
                case 0:
                    inProcess = 0
                case 1:
                    product.set_name(input('Введите название товара: '))
                case 2:
                    process = 1
                    
                    while process:
                        try:
                            product.set_quantity(int(input('Введите количество товара: ')))
                        except ValueError:
                            print('Количество должно быть положительным числом. ')

                        else:
                            process = 0
                case 3:
                    process = 1
                    
                    if accounting != 'new_card':
                        while process:
                            try:
                                answer = int(input('Списать с учета? (1 - да 2 - нет). '))
                                match answer:
                                    case 1:
                                        product.deduction_from_accounting()
                                    case 2:
                                        pass
                                    case _:
                                        raise ValueError('Нужно вписать число 1 или 2. ')

                            except ValueError:
                                print('Нужно вписать число (1 или 2). ')
                                
                            else:
                                process = 0
                    else:
                        print('Вы не можете изменить этот параметр в данный момент. Списать с учета можно после создания карточки товара в разделе изменить данные. ')
                
                case 4: 
                    product.set_provider(input('Введите поставщика товара: '))
                case 5:
                    product.set_manufacturer(input('Введите производителя товара: '))
                case 6:
                    process = 1
                    
                    while process:
                        try:
                            product.set_price(float(input('Введите цену товара: ')))
                        except ValueError:
                            print('Цена должна быть положительным числом. ')

                        else:
                            process = 0
                case 7:
                    product.set_location(input('Введите местоположение товара: '))
                case 8:
                    product.set_description(input('Введите описание товара: '))
                case 9:
                    product.set_сountry_of_manufacture(input('Введите страну-производителя товара: '))
                case 10:
                    process = 1
                    
                    while process:
                        try:
                            product.set_weight(float(input('Введите вес товара: ')))
                        except ValueError:
                            print('Вес должен быть положительным числом. ')

                        else:
                            process = 0
                case 11:
                    product.set_colour(input('Введите цвет товара: '))

    def print_list_of_cards(self) -> None:
        """Вывод наименований товаров из списка."""

        print('-------------------------------------------------------------------------------------------------------------------')
        
        for i in range(len(self.__list_of_cards)):
            print(i+1, self.__list_of_cards[i].get_name())
            
        print('-------------------------------------------------------------------------------------------------------------------')

    def create_card(self) -> None:
        """Создание карточки товара."""

        product = ProductCard()
        self.action_choice(product, 'new_card')
        self.__list_of_cards += [product]
        self.show_card(product)
    
    def edit_card(self, product: ProductCard = None) -> None:
        """Редактирование карточки выбранного товара.
        
        Args:
            product: экземпляр класса ProductCard, параметры которого надо редактировать. 
        """

        self.action_choice(product, 'editing_card')
    
    def check_delete_edit_user_input(self, text: str = '') -> None | int:
        """Обработка пользовательского ввода.

        Args:
            text: строка, определяющая режим работы метода. Принимает 1 из 3 значений: удаления, просмотра, редактирования.

        Returns: 
            choose_editing_card: номер выбранной карточки. Возвращается, если text = 'редактирования'.

        Raises:
            ValueError: передано не целое число.
        """

        process =  1
        
        while process:
            try:
                choose_editing_card = int(input(f'Выберите карточку товара для {text} (exit --- 0): '))
                
                if choose_editing_card > len(self.__list_of_cards) or choose_editing_card < 0:
                    print(f'Число должно быть в диапазоне от 1 до {len(self.__list_of_cards)}. ')

                    continue
                
                elif choose_editing_card == 0:
                    process = 0
            except ValueError:
                print('Введите целое число. ')

            else:
                process = 0

        if text == 'удаления' and len(self.__list_of_cards) != 0:
            self.__list_of_cards.pop(choose_editing_card-1)
            
        elif text == 'просмотра' and len(self.__list_of_cards) != 0:
            self.show_card(self.__list_of_cards[choose_editing_card-1])
            
        elif text == 'редактирования': 
            return choose_editing_card

    def action(self) -> None:
        """Управление программой, реализует основной цикл взаимодействия с пользователем. Предоставляет пользователю главное меню с возможностью выбора действий.
        
        Raises: 
            ValueError: передано не число или передано число не в диапазоне от 1 до 5.and
        """

        programm = 1
        while programm:
            
            print(self.__text_products)
            print('Выберите действие: ')
            print('Создать карточку товара (1) ')
            print('Просмотреть карточки товаров (2) ')
            print('Удалить карточку товара (3) ')
            print('Изменить карточку товара (4) ')
            print('Выход (5) ')

            try:
                choose_action = int(input())
                self.__choice = choose_action
                
                if choose_action < 1 or choose_action > 5:
                    raise ValueError

            except ValueError:
                print('Необходимо ввести число от 1 до 5. ')
                
                continue
            
            match self.__choice:
                case 1: 
                    self.create_card()
                case 2:
                    self.print_list_of_cards()
                    self.check_delete_edit_user_input('просмотра')
                    
                    input('Для продолжения нажмите ENTER')

                    print('-------------------------------------------------------------------------------------------------------------------')

                case 3:
                    self.print_list_of_cards()
                    self.check_delete_edit_user_input('удаления')
                    self.print_list_of_cards()
                case 4:
                    self.print_list_of_cards()
                    choosed_index_of_card_to_edit = self.check_delete_edit_user_input('редактирования')
                    
                    if choosed_index_of_card_to_edit != 0:
                        self.action_choice(self.__list_of_cards[choosed_index_of_card_to_edit-1], 'card')
                case 5:
                    programm = 0 
    