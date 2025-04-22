#Локаторы страницы оформления заказа
place_order_first_name_input = "//input[@placeholder='* Имя']"#Поле для ввода имени
place_order_last_name_input = "//input[@placeholder='* Фамилия']"#Поле для ввода фамилии
place_order_address_input = "//input[@placeholder='* Адрес: куда привезти заказ']"#Поле для ввода адреса
place_order_subway_dropdown = "//input[@placeholder='* Станция метро']"#Выпадающий список станций метро
place_order_stations_list = "//li[@role='menuitem']"#Список станций метро
place_order_phone_number_input = "//input[@placeholder='* Телефон: на него позвонит курьер']"#Поле для ввода номера телефона
place_order_next_button = "//button[contains(text(),'Далее')]"#Кнопка "Далее"

place_order_delivery_date_input = "//input[@placeholder='* Когда привезти самокат']"#Поле для ввода даты доставки самоката
place_order_date_picker_dates = "//div[contains(@class, 'react-datepicker__day react-datepicker__day--')]"#Календарь для выбора даты доставки
place_order_term_date_dropdown = "//div[@class='Dropdown-placeholder']"#Выпадающий список с длительностью аренды
place_order_terms_list = "(//div[@class='Dropdown-option'])"#Список доступных длительностей адренды
place_order_color_checkboxes = "(//input[@type='checkbox'])"#Список опций для выбора цвета
place_order_comment_input = "//input[@placeholder='Комментарий для курьера']"#Поле для ввода комментария курьеру
place_order_order_button = "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"#Кнопка "Заказать"

place_order_confirmation_popup = "//div[@class='Order_Modal__YZ-d3']"#Модальное окно "Хотите оформить заказ?"
place_order_confirmation_popup_yes = "//button[contains(text(),'Да')]"#Кнопка подтверждения оформления заказа в модальном окне

place_order_order_placed_confirmation_popup = "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and text() = 'Заказ оформлен']" #Модальное окно "Заказ оформлен"
