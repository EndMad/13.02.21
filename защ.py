#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Использовать словарь, содержащий следующие ключи: название пункта назначения; номер
# поезда; время отправления. Написать программу, выполняющую следующие действия: ввод
# с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
# быть упорядочены по времени отправления поезда; вывод на экран информации о поездах,
# направляющихся в пункт, название которого введено с клавиатуры; если таких поездов нет,
# выдать на дисплей соответствующее сообщение. фамилия и
# инициалы; номер группы; успеваемость


import sys


def add(flights, destination, number, typ):
    flight = {
        'destination': destination,
        'number': number,
        'typ': typ,
    }

    flights.append(flight)
    if len(flights) > 1:
        flights.sort(key=lambda item: item.get('destination', ' '))


def _list():
    table = []
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 17
    )
    table.append(line)
    table.append(
        '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
            "№",
            "Фамилия и Инициалы",
            "Номер Группы",
            "Успеваемость"
        )
    )
    table.append(line)

    for idx, flight in enumerate(flights, 1):
        table.append(
            '| {:>4} | {:<30} | {:<20} | {:<17} |'.format(
                idx,
                flight.get('destination', ' '),
                flight.get('number', 0),
                flight.get('typ', ' ')
            )
        )
    table.append(line)

    return '\n'.join(table)


def select(type):
    result = []
    for flight in flights:
        if type == flight.get('typ'):
            result.append(flight)

    return result


if __name__ == '__main__':
    flights = []

    while True:
        command = input(">>> ")

        if command == 'exit':
            break

        elif command == 'add':
            destination = input("Фамилия и Инициалы? ")
            number = int(input("Номер Группы? "))
            typ = (input("Успеваемость? "))

            add(flights, destination, number, typ)

        elif command == 'list':
            print(_list())

        elif command.startswith('select '):
            parts = command.split(maxsplit=1)
            selected = select(parts[1])
            count = 1
            if selected:
                for idx, flight in enumerate(selected, 1):
                    print(
                        '{:>4}: Фамилия и Инициалы - {}, Номер Группы- {}'.format(count,
                                                                               flight.get('destination', ''),
                                                                               flight.get('number', '')
                                                                               )
                    )
            else:
                print("!!!Такие Студенты отсутстуют!!! ")

        elif command == 'help':
            print("Список команд:\n")
            print("add - Добавить данные;")
            print("list - Вывести данные;")
            print("list <Успеваемость> - запросить нужную группу;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
