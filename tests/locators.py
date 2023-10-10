from selenium.webdriver.common.by import By

class MainPageLocators:
    ACCOUNT_BUTTON_HEADER = (By.XPATH, ".//a[@href='/account']")  # кнопка "Личный кабинет" в шапке
    CONSTRUCTOR_BUTTON_HEADER = (By.XPATH, ".// p[text() = 'Конструктор']")  # кнопка "Конструктор" в шапке
    FEED_BUTTON_HEADER = (By.XPATH, ".//a[@href='/feed']")  # кнопка "Лента заказов" в шапке
    LOGO_HEADER = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")  # логотип "Stellar Burgers" в шапке
    SIGN_IN_ACCOUNT_BUTTON_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт" на главной странице
    COMPILE_BURGER_HEADER = (By.XPATH, ".//h1[text()='Соберите бургер']")  # заголовок "Соберите бургер" на главной странице
    PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")  # кнопка "Оформить заказ" на главной
    BUNS_SPAN = (By.XPATH, ".//span[text()='Булки']")  # закладка "Булки" в конструкторе
    BUNS_HEADER = (By.XPATH, ".//h2[text()='Булки']")  # заголовок секции "Булки" в конструкторе
    SAUCES_SPAN = (By.XPATH, ".//span[text()='Соусы']")  # закладка "Соусы" в конструкторе
    SAUCES_HEADER = (By.XPATH, ".//h2[text()='Соусы']")  # заголовок секции "Соусы" в конструкторе
    FILLINGS_SPAN = (By.XPATH, ".//span[text()='Начинки']")  # закладка "Начинки" в конструкторе
    FILLINGS_HEADER = (By.XPATH, ".//h2[text()='Начинки']")  # заголовок секции "Начинки" в конструкторе

class AuthPageLocators:
    SIGN_IN_BUTTON_AUTH = (By.XPATH, ".//button[text()='Войти']")  # кнопка "Войти" в форме авторизации
    REGISTER_URL_AUTH = (By.XPATH, ".//a[@href='/register']")  # ссылка "Зарегистрироваться" в форме авторизации
    EMAIL_INPUT_FIELD_AUTH = (By.XPATH, ".//h2[text()='Вход']/..//label[text() = 'Email']/../input")  # поле ввода "Email" в форме авторизации
    PASSWORD_INPUT_FIELD_AUTH = (By.XPATH, ".//h2[text()='Вход']/..//label[text() = 'Пароль']/../input")  # поле ввода "Пароль" в форме авторизации
    FORGOT_PASSWORD_BUTTON_AUTH = (By.XPATH, ".//a[text()='Восстановить пароль']")  # кнопка "Восстановить пароль" в форме авторизации

class ProfilePageLocators:
    PROFILE_URL_ACCOUNT = (By.XPATH, ".//a[text()='Профиль']")  # ссылка "Профиль" в личном кабинете
    EXIT_BUTTON_ACCOUNT = (By.XPATH, ".//button[text()='Выход']")  # кнопка "Выход" в личном кабинете
    LOGO_HEADER = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")  # логотип "Stellar Burgers" в шапке

class RegisterPageLocators:
    REGISTER_BUTTON_REG = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # кнопка "Зарегистрироваться" в форме регистрации
    NAME_INPUT_FIELD_REG = (By.XPATH, ".//h2[text()='Регистрация']/..//label[text() = 'Имя']/../input")  # поле ввода "Имя" в форме регистрации
    EMAIL_INPUT_FIELD_REG = (By.XPATH, ".//h2[text()='Регистрация']/..//label[text() = 'Email']/../input")  # поле ввода "Email" в форме регистрации
    PASSWORD_INPUT_FIELD_REG = (By.XPATH, ".//h2[text()='Регистрация']/..//label[text() = 'Пароль']/../input")  # поле ввода "Пароль" в форме регистрации
    INCORRECT_PASSWORD_ERROR_REG = (By.XPATH, ".//p[text()='Некорректный пароль']")  # текст ошибки в форме регистрации
    SIGN_IN_BUTTON_REG = (By.XPATH, ".//h2[text()='Регистрация']/..//a[text()='Войти']")  # кнопка "Войти" в форме регистрации


class ForgotPasswordPageLocators:
    SIGN_IN_BUTTON_FORGOT_PASSWORD = (By.XPATH, ".//h2[text()='Восстановление пароля']/..//a[text()='Войти']")  # кнопка "Войти" в форме восстановления пароля

class FeedPageLocators:
    FEED_HEADER = (By.XPATH, ".//h1[text()='Лента заказов']")  # заголовок "Лента заказов" в ленте заказов
