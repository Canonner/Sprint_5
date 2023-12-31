## Финальный проект 5 спринта

Папка tests содержит файлы с тестами, проверяющими функциональность сервиса [Stellar Burgers](https://stellarburgers.nomoreparties.site/) 


### Список тестовых файлов и описание проверок:

#### test_registration.py
  Содержит проверки:
  - успешной регистрации - test_registration_valid_data_successful_registration,
  - выдачи ошибки при вводе некорректного пароля - test_registration_invalid_password_error_received.

#### test_sign_in.py
  Содержит проверки:
  - входа по кнопке «Войти в аккаунт» на главной - test_authorization_via_sign_in_account_button,
  - входа через кнопку «Личный кабинет» - test_authorization_via_account_button,
  - входа через кнопку в форме регистрации - test_authorization_via_sign_in_register_button,
  - входа через кнопку в форме восстановления пароля - test_authorization_via_sign_in_forgot_password_button.

#### test_click_to_profile.py
  Содержит проверку перехода в «Личный кабинет» по клику на кнопку «Личный кабинет»
  - с главной страницы - test_access_to_profile_from_main,
  - из ленты заказов - test_access_to_profile_from_feed.

#### test_from_profile_to_constructor.py
  Содержит проверки перехода из Личного кабинета в Конструктор:
  - по клику на кнопку «Конструктор» - test_click_from_profile_on_constructor,
  - по клику на логотип Stellar Burgers - test_click_from_profile_on_logo_burgers.

#### test_exit_from_account.py
  Содержит проверку выхода при клике по кнопке «Выйти» в личном кабинете - test_exit_from_account.

#### test_constructor_sections.py
  Содержит проверки перехода в соответствующие разделы Конструктора при клике:
  - на закладку «Булки» - test_constructor_section_buns,
  - на закладку «Соусы» - test_constructor_section_sauces,
  - на закладку «Начинки» - test_constructor_section_fillings.


### Фикстуры

Фикстуры, использованные в тестах, находятся в файле conftest.py
  - фикстура driver - инициализирует драйвер браузера, используется во всех без исключения тестах,
  - фикстура sign_in - для входа под тестовым юзером во всех тестах, где нужна авторизация (кроме тестов регистрации, тестов входа и тестов разделов конструктора).


### Локаторы
Локаторы и их описания находятся в файле locators.py.
Локаторы разделены на классы, соответствующие страницам.
Названия констант с локаторами читаются как НАДПИСЬ_КНОПКА_МЕСТО

### Тестовые данные
Тестовые данные находятся в файле data.py в классе CommonData
- данные тестового пользователя, зарегистрированного в системе, для тестов, где нужна авторизация,
- статический метод reg_data - для генерации имени, логина и пароля для тестов регистрации (в рамках дополнительного задания к проекту).


