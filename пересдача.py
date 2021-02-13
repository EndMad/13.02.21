#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить программу для решения задачи:
# Создать класс Man (человек), с полями: имя, возраст, пол и вес.
# Определить методы переназначения имени, изменения возраста и изменения веса.
# Создать производный класс Student, имеющий поле года обучения.
# Определить методы переназначения и увеличения года обучения.

class Man:

    def __init__(self):
        self.__name = ' '
        self.__age = 0
        self.__pol = ' '
        self.__weight = 0

    def read(self, name, age, pol, weight):
        self.name(name)
        self.age(age)
        self.pol(pol)
        self.weight(weight)

    def name(self, prompt=None):
        self.__name = input() if prompt is None else input(prompt)

    def age(self, prompt=None):
        self.__age = input() if prompt is None else input(prompt)

    def pol(self, prompt=None):
        self.__pol = int(input()) if prompt is None else input(prompt)

    def weight(self, prompt=None):
        self.__weight = int(input()) if prompt is None else input(prompt)

    def set_name(self, a):
        self.__name = a

    def set_age(self, a):
        self.__age = a

    def set_weight(self, a):
        self.__weight = a

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_weight(self):
        return self.__weight

    def get_pol(self):
        return self.__pol


class Student(Man):
    def __init__(self):
        super(Student, self).__init__()
        self.__year = 0

    def read(self, name, age, pol, weight):
        Man.read(self, name, age, pol, weight)

    def get_info(self):
        return self.get_name(), self.get_age(), self.get_pol(), self.get_weight(), self.get_year()

    def set_year(self, prompt):
        self.__year = input() if prompt is None else input(prompt)

    def get_year(self):
        return self.__year


if __name__ == '__main__':
    man = Student()
    man.read("Введите имя: ",
             "Введите возраст: ",
             "Введите пол: ",
             "Введите вес: ")
    man.set_year("Введите год обучения студента: ")
    year = man.get_year()
    print("Вся информация по студенту вида \n"
          "(Имя, возраст, пол, вес, год обучения) \n"
          "{}".format(man.get_info()))