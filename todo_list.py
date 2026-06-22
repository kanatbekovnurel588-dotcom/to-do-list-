todo_list = []


def add_task(task):
    todo_list.append(task)
    print("Добавлено!")


def show_tasks():
    if len(todo_list) == 0:
        print("Список пуст")
    else:
        print("\nЗадачи:")
        count = 1
        for task in todo_list:
            print(f"{count}. {task}")
            count += 1


def delete_task(number):
    if 1 <= number <= len(todo_list):
        deleted = todo_list.pop(number - 1)
        print(f'Удалено: {deleted}')
    else:
        print("Такой задачи нет")


while True:
    print("\n1 - Показать")
    print("2 - Добавить")
    print("3 - Удалить")
    print("4 - Выход")

    choice = input("Выбор: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        task = input("Новая задача: ")
        add_task(task)

    elif choice == "3":
        show_tasks()

        if len(todo_list) > 0:
            num = int(input("Номер задачи: "))
            delete_task(num)

    elif choice == "4":
        print("До свидания!")
        break

    else:
        print("Неправильный ввод")