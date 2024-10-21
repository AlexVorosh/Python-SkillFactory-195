import random

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}

for student in students:
    students_marks[student] = {}

    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks

for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Вывести все оценки по ученику
        5. Обновить оценку ученика по предмету
        6. Изменить имя ученика
        7. Удалить ученика
        8. Удалить оценку ученика по предмету
        9. Добавить новый предмет
        10. Вывести средний бал по каждому предмету по ученику
        11. Добавить нового ученика
        12. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Вывести все оценки по ученику')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            print(f'Информация по оценкам для ученика {student} {students_marks[student]}')
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command == 5:
        print('5. Обновить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        print(f'Оценки ученик(а) {student} по предмету {class_} {students_marks[student][class_]}')
        mark = int(input('Введите текущую оценку: '))
        new_mark = int(input('Введите новую оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            if mark in students_marks[student][class_]:
                students_marks[student][class_].remove(mark)
                students_marks[student][class_].append(new_mark)
            print(f'Для ученика {student} по предмету {class_} оценка изменена на {new_mark}')
            print(f'Оценки ученик(а) {student} по предмету {class_} {students_marks[student][class_]}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 6:
        print('6. Измененить имя ученика')
        student = input('Введите имя ученика: ')
        new_student = input('Введите новое имя ученика: ')
        if student in students_marks.keys():
            students_marks[new_student] = students_marks[student]
            del students_marks[student]
            print(f'Имя ученика {student} изменено на имя {new_student}')
        else:
            print('ОШИБКА: Неверное имя ученика')
    elif command == 7:
        print('7. Удалить ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            students.remove(student)
            del students_marks[student]
            print(f'Ученик {student} удален(а) из дневника')
        else:
            print('ОШИБКА: Неверное имя ученика')
    elif command == 8:
        print('8. Удалить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        print(f'Оценки ученик(а) {student} по предмету {class_} {students_marks[student][class_]}')
        mark = int(input('Введите оценку которую нужно удалить: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].remove(mark)
            print(f'Для {student} по предмету {class_} удалена оценка {mark}')
            print(f'Оценки ученик(а) {student} по предмету {class_} {students_marks[student][class_]}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 9:
        print('9. Добавить новый предмет')
        new_class_ = input('Введите название предмета: ')
        if new_class_ not in students_marks[student].keys():
            classes.append(new_class_)
            for student in students_marks:
                students_marks[student][new_class_] = []
            print(f'Предмет {new_class_} добавлен в список')
            print(students_marks[student].keys())
        else:
            print('Предмет уже есть в списке')
    elif command == 10:
        print('10. Вывести средний бал по каждому предмету по ученику')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            for classes, marks in students_marks[student].items():
                marks_sum = sum(marks)
                marks_count = len(marks)
                print(f'{classes} - {marks_sum // marks_count}')
        else:
            print(f'Данного ученика нет в базе')
    elif command == 11:
        print('11. Добавить нового ученика')
        new_student = input('Введите имя нового ученика: ')
        if new_student not in students:
            students.append(new_student)
            students_marks[new_student] = {}
            for class_ in classes:
                marks = []
                students_marks[new_student][class_] = marks
            print(f'Ученик {new_student} добавлен в список')
            print(students_marks)
        else:
            print(f'Ученик {new_student} уже есть в списке')
    elif command == 12:
        print('12. Выход из программы')
        break