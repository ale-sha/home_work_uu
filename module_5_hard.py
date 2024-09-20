class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname: str = nickname
        self.password: int = password.__hash__()
        self.age: int = age

    def __repr__(self):
        return f'({self.nickname}, {self.password}, {self.age})'


class Video:
    def __init__(self, title: str, duration: int, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0

    def __repr__(self):
        return f'({self.title}, {self.duration}, {self.adult_mode})'


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user: User = None

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print(f"Пользователь {nickname} уже существует")
                break
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.current_user = user
            print(f"Вход {nickname} выполнен")

    def login(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname:
                if nickname == user.nickname and password.__hash__() == user.password:
                    self.current_user = user
                    print("Добро пожаловать")
                    break
                else:
                    print("Не верный логин или пароль")

    def log_out(self):
        print(self.current_user)
        self.current_user = None
        print(self.current_user)

    def add(self, *other: Video):
        for video in other:
            if self.videos.__contains__(video):
                print("Видео с таким названием уже есть")
            else:
                self.videos.append(video)

    def get_videos(self, any_word: str):
        video_with_any_word = []
        for video in self.videos:
            if video.title.lower().__contains__(any_word.lower()):
                video_with_any_word.append(video.title)
        return video_with_any_word

    def watch_video(self, title_video):
        if self.current_user is not None:
            if self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста, покиньте страницу")
            else:
                for video in self.videos:
                    if title_video == video.title:
                        from time import sleep
                        for i in range(1, video.duration):
                            print(i, end=' ')
                            sleep(1)
                        print('Конец видео')
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
