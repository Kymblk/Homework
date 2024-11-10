import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def check_password(self, password):
        return self.password == password

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode
    def play(self):
        self.time_now = 0
        print(f'Воспроизведение видео: {self.title}')

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.check_password(password):
                self.current_user = user
                print(f'Добро пожаловать, {nickname}')
                return
        print('Неверный логин или пароль!')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname}, уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        print(f'Пользователь {nickname} зарегистрирован!')
        self.log_in(nickname, password)

    def log_out(self):
        if self.current_user:
            print(f'До свидания, {self.current_user.nickname}!')
            self.current_user = None
        else:
            print('Вы не вошли в систему!')

    def add(self, *videos):
        for video in videos:
            if any(v.title == video.title for v in self.videos):
                print(f'Видео {video.title} уже существует')
            else:
                self.videos.append(video)
                print(f'Видео {video.title} добавлено')

    def get_videos(self, keyword):
        return [video.title for video in self.videos if keyword.lower() in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            print(f'Видео {title} не найдено')
            return

        if video.adult_mode and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
            return

        video.play()
        while video.time_now < video.duration:
            print(f'Проигрывается: {video.time_now+1} сек.')
            time.sleep(1)
            video.time_now += 1
        print('Конец видео')

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