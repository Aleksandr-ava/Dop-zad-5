import time


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title  # заголовок, строка
        self.duration = duration  # продолжительность, секунды
        self.time_now = 0  # секунда остановки (изначально 0)
        self.adult_mode = adult_mode  # ограничение по возрасту, bool (False по умолчанию)


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname  # имя пользователя, строка
        self.password = password  # в хэшированном виде, число
        self.age = age  # возраст, число


class UrTube:
    def __init__(self):
        self.current_duration = None
        self.get_video = None
        self.my_str = None
        self.my_search_list = None
        self.search_video = None
        self.video = None
        self.age = 0
        self.nickname = ''
        self.password = ''
        self.login = None
        self.users = []  # список объектов User
        self.videos = []  # список объектов Video
        self.current_user = None  # текущий пользователь, User

    def add(self, *vid):
        self.video = []

        for i in vid:
            self.video = [i.title, i.duration, i.adult_mode]
            self.videos.append(self.video)

    def get_videos(self, search_video):
        self.search_video = search_video.lower()

        self.my_search_list = []
        for i in self.videos:
            my_str = i[0]
            self.my_str = my_str.lower()
            if self.my_str.find(self.search_video) != -1:
                self.my_search_list.append(i[0])
        return self.my_search_list

    def watch_video(self, get_video):
        self.get_video = get_video

        if self.current_user is not None:
            for i in self.videos:
                if i[0] == self.get_video and i[2] is True:
                    self.current_duration = i[1]
                    if self.age > 18:
                        for j in range(1, 11):
                            ur.time_now = j
                            print('۰', end='')
                            print(ur.time_now, sep='', end='')
                            time.sleep(1)
                        print(' Конец видео')
                        time.sleep(1)
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    self.log_out()  # Выход из акаунта
            self.current_user = self.login
        else:
            print('Войдите в акаунт чтобы смотреть видео')

    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        hash1 = hash(password)
        ur.password = "%s" % hash1

        if self.nickname in self.users:
            print(f'Пользователь {self.nickname} уже существует')
        else:
            self.users.append(ur.nickname)
            self.log_in(self.nickname, self.password)
            self.current_user = self.login

    def log_in(self, login, password):
        self.login = login
        self.password = password

    def log_out(self):
        self.current_user = None
        self.nickname = ''
        self.password = ''
        self.age = 0
        return


# Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
#
# # Добавление видео
ur.add(v1, v2)
#
# # Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
