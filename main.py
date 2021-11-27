# Вариант В.
#
# 1. «Браузер» и «Компьютер» связаны соотношением один-ко-многим.
#    Выведите список всех компьютеров, у которых название начинается с буквы «А», и их браузеры.
#
# 2. «Браузер» и «Компьютер» связаны соотношением один-ко-многим. Выведите список Браузеров с минимальной памятью
#    компьютеров для каждого браузера, отсортированный по минимальной памяти.
#
# 3. «Браузер» и «Компьютер» связаны соотношением многие-ко-многим.
#    Выведите список всех связанных компьютеров и браузеров,  отсортированный по компьютерам, сортировка по браузерам
#    производная.

from operator import itemgetter


class Browser:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Computer:
    def __init__(self, id, brand, memory_gb, id_browser):
        self.id = id
        self.brand = brand
        self.memory_gb = memory_gb
        self.id_browser = id_browser


class ComputerBrowser:
    def __init__(self, computer_id, id_browser):
        self.computer_id = computer_id
        self.id_browser = id_browser


computers = [
    Computer(1, 'Lenovo', 128, 2),
    Computer(2, 'Acer', 128, 4),
    Computer(3, 'HP', 128, 1),
    Computer(4, 'Dell', 64, 1),
    Computer(5, 'Xiaomi', 256, 2),
    Computer(6, 'Apple', 512, 6),
    Computer(7, 'Asus', 64, 3),
    Computer(8, 'Acer', 256, 5),
    Computer(9, 'Apple', 128, 6),
]

browsers = [
    Browser(1, 'Chrome'),
    Browser(2, 'Yandex'),
    Browser(3, 'Opera'),
    Browser(4, 'Firefox'),
    Browser(5, 'Mozilla'),
    Browser(6, 'Safari'),
]


computers_browsers = [
    ComputerBrowser(1, 2),
    ComputerBrowser(1, 4),
    ComputerBrowser(2, 2),
    ComputerBrowser(2, 4),
    ComputerBrowser(2, 5),
    ComputerBrowser(3, 1),
    ComputerBrowser(3, 3),
    ComputerBrowser(3, 5),
    ComputerBrowser(4, 1),
    ComputerBrowser(5, 2),
    ComputerBrowser(6, 6),
    ComputerBrowser(7, 3),
    ComputerBrowser(8, 5),
    ComputerBrowser(9, 6),
]


def main():
    one_to_many = [(comp.brand, comp.memory_gb, browser.name)
                   for comp in computers
                   for browser in browsers
                   if comp.id_browser == browser.id]

    many_to_many_temp = [(browser.name, comp_browser.computer_id, comp_browser.id_browser)
                         for browser in browsers
                         for comp_browser in computers_browsers
                         if browser.id == comp_browser.id_browser]

    many_to_many = [(comp.brand, browser_name)
                    for browser_name, comp_id, browser_id in many_to_many_temp
                    for comp in computers if comp.id == comp_id]

    print('Дудник Максим ИУ5-53Б')
    print('\n\nЗадание В1')
    res = list(filter(lambda i: str(i[0]).startswith('A'), one_to_many))
    res = [
        (elem[0], elem[2])
        for elem in res
    ]
    print(res)

    print('\n\nЗадание В2')
    sorted_data = sorted(one_to_many, key=itemgetter(1))
    res = []

    for elem in sorted_data:
        flag = False
        for resElem in res:
            if elem[2] == resElem[0]:
                flag = True
        if not flag:
            res.append((elem[2], elem[1]))

    print(res)

    print('\n\nЗадание В3')
    res = sorted(many_to_many, key=itemgetter(0))
    print(res)
    print('\n\n')


if __name__ == '__main__':
    main()
