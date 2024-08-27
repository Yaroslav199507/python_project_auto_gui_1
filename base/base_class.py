from datetime import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver


    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Текущий url страницы: " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Проверка по слову успешна")

    """Method scroll"""

    def scroll_down(self, a, b):
        y = a
        x = b
        self.driver.execute_script(f"window.scrollTo({x},{y})")


    """Method Screenshot"""

    def screenshot(self):
        now_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screen = "screen " + now_date + ".png"
        self.driver.save_screenshot(f"C:\\Users\\davyd\\PycharmProjects\\new_main_project\\screen\\{name_screen}")

    """Method assert URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("текущий URL соответствует ожидаемому")