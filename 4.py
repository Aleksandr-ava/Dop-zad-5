class Database:
    def __init__(self, age):
        self.data = {}
        self.age = age

    def add_user(self, nickname, password, age):
        self.data[nickname] = password
        self.age = age


class User:
    def __init__(self, nickname, password, password_confirm, age):
        self.nickname = nickname
        if password == password_confirm:
            self.password = password
        self.age = age

    def register(self, nickname, password, age):
        if nickname == database.data[nickname]:
            self.nickname = nickname
        else:
            print('Пользователь уже есть!\n')
        self.password = password
        self.age = age


if __name__ == '__main__':
    database = Database(age=0)
    while True:
        choice = int(input('Здравствуй! Выбери действие: \n1 - Вход\n2 - Регистрация\n'))
        if choice == 1:
            login = input('Введите имя: ')
            password = input('Введите пароль: ')
            hash2 = hash(password)
            password = "%s" % hash2
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}')
                    break
                else:
                    print('Неверный пароль.\n')
            else:
                print('Пользователь не найден.\n')
        if choice == 2:
            user = User(input('Введите имя: '), password := input('Ведите пароль: '),
                        password2 := input('Повтарите пароль: '), age=int(input('Введите возраст: ')))
            hash1 = hash(password)
            user.password = "%s" % hash1
            if password != password2:
                print('Неверный повтор пароля!\n')
                continue
            user.register(user.nickname, user.password, user.age)
            database.add_user(user.nickname, user.password, user.age)
