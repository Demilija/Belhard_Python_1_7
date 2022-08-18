"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:
    surname: str
    name: str
    group: int
    average_score: int

    def __init__(self, surname, name, group, average_score):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __iter__(self):
        return self

    def __eq__(self, other):
        return self.average_score == other

    def __ne__(self, other):
        return self.average_score != other

    def __lt__(self, other):
        return self.average_score < other

    def __gt__(self, other):
        return self.average_score > other

    def __le__(self, other):
        return self.average_score <= other

    def __ge__(self, other):
        return self.average_score >= other


lst = [Student("Добр", "Эмилия", 5, 7), Student("Алексеева", "Мария", 3, 9), Student("Поз", "Петер", 4, 5),
       Student("Ломаш", "Дарья", 3, 3), Student("Козов", "Дмитрий", 1, 6)]

for i in lst:
    if isinstance(i, int):
        lst = lst.sort()
        print(lst)

for i in lst:
    if i.average_score > 5:
        print(i.surname, i.name, i. group, i.average_score)
