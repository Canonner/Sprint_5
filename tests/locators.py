from selenium.webdriver.common.by import By

class Locators:
    # названия констант с локаторами читаются как НАДПИСЬ_КНОПКА_МЕСТО
    # локаторы для test_registration
    ACCOUNT_BUTTON_HEADER = (By.XPATH, ".//a[@href='/account']")  # кнопка "Личный кабинет" в шапке
    SIGN_IN_BUTTON_AUTH = (By.XPATH, ".//button[text()='Войти']")  # кнопка "Войти" в форме авторизации
    REGISTER_URL_AUTH = (By.XPATH, ".//a[@href='/register']")  # ссылка "Зарегистрироваться" в форме авторизации
    REGISTER_BUTTON_REG = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # кнопка "Зарегистрироваться" в форме регистрации
    NAME_INPUT_FIELD_REG = (By.XPATH, ".//h2[text()='Регистрация']/..//label[text() = 'Имя']/../input")  # поле ввода "Имя" в форме регистрации
    EMAIL_INPUT_FIELD_REG = (By.XPATH, ".//h2[text()='Регистрация']/..//label[text() = 'Email']/../input")  # поле ввода "Email" в форме регистрации
    PASSWORD_INPUT_FIELD_REG = (By.XPATH, ".//h2[text()='Регистрация']/..//label[text() = 'Пароль']/../input")  # поле ввода "Пароль" в форме регистрации
    EMAIL_INPUT_FIELD_AUTH = (By.XPATH, ".//h2[text()='Вход']/..//label[text() = 'Email']/../input")  # поле ввода "Email" в форме авторизации
    PASSWORD_INPUT_FIELD_AUTH = (By.XPATH, ".//h2[text()='Вход']/..//label[text() = 'Пароль']/../input")  # поле ввода "Пароль" в форме авторизации
    PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")  # кнопка "Оформить заказ" на главной
    INCORRECT_PASSWORD_ERROR_REG = (By.XPATH, ".//p[text()='Некорректный пароль']")  # текст ошибки в форме регистрации

    # локаторы для test_sign_in
    SIGN_IN_ACCOUNT_BUTTON_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт" на главной странице
    SIGN_IN_BUTTON_REG = (By.XPATH, ".//h2[text()='Регистрация']/..//a[text()='Войти']")  # кнопка "Войти" в форме регистрации
    FORGOT_PASSWORD_BUTTON_AUTH = (By.XPATH, ".//a[text()='Восстановить пароль']")  # кнопка "Восстановить пароль" в форме авторизации
    SIGN_IN_BUTTON_FORGOT_PASSWORD = (By.XPATH, ".//h2[text()='Восстановление пароля']/..//a[text()='Войти']")  # кнопка "Войти" в форме восстановленения пароля

    # локаторы для test_access_profile
    PROFILE_URL_ACCOUNT = (By.XPATH, ".//a[text()='Профиль']")  # ссылка "Профиль" в личном кабинете
    FEED_BUTTON_HEADER = (By.XPATH, ".//a[@href='/feed']")  # кнопка "Лента заказов" в шапке
    FEED_HEADER = (By.XPATH, ".//h1[text()='Лента заказов']")  # заголовок "Лента заказов" в ленте заказов

    # локаторы для test_from_profile_to_constructor
    CONSTRUCTOR_BUTTON_HEADER = (By.XPATH, ".// p[text() = 'Конструктор']")  # кнопка "Конструктор" в шапке
    LOGO_HEADER = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")  # логотип "Stellar Burgers" в шапке
    COMPILE_BURGER_HEADER = (By.XPATH, ".//h1[text()='Соберите бургер']")  # заголовок "Соберите бургер" конструкторе

    # локаторы для test_exit_from_account
    EXIT_BUTTON_ACCOUNT = (By.XPATH, ".//button[text()='Выход']")  # кнопка "Выход" в личном кабинете

    # локаторы для test_constructor_sections
    BUNS_SPAN = (By.XPATH, ".//span[text()='Булки']")  # закладка "Булки" в конструкторе
    BUNS_HEADER = (By.XPATH, ".//h2[text()='Булки']")  # заголовок секции "Булки" в конструкторе
    SAUCES_SPAN = (By.XPATH, ".//span[text()='Соусы']")  # закладка "Соусы" в конструкторе
    SAUCES_HEADER = (By.XPATH, ".//h2[text()='Соусы']")  # заголовок секции "Соусы" в конструкторе
    FILLINGS_SPAN = (By.XPATH, ".//span[text()='Начинки']")  # закладка "Начинки" в конструкторе
    FILLINGS_HEADER = (By.XPATH, ".//h2[text()='Начинки']")  # заголовок секции "Начинки" в конструкторе