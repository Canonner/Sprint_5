import random as r

class CommonData:
    main_url = 'https://stellarburgers.nomoreparties.site/'
    test_user_email = 'test_user_burgers123@ya.ru'
    test_user_password = '123456'
    invalid_password = '12345'


    @staticmethod
    def reg_data():
        name_seq = ['Ев', 'Ге', 'Ний', 'Во', 'Лк', 'Ов']
        name = f'{r.choice(name_seq)}'
        login = f'evgeniivolkov1{r.randint(100, 1000)}@ya.ru'
        pass_seq = ['able', 'baker', 'charlie', 'dog', 'easy', 'fox']
        password = f'{r.choice(pass_seq)}{r.randint(100, 1000)}'
        return {'name': name, 'login': login, 'password': password}


