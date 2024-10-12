import time

class User:
  def __init__(self, nickname, password, age):
    self.nickname = nickname
    self.password = password
    self.age = age

class Video:
  def __init__(self, title, duration, adult_mode=False):
    self.title = title
    self.duration = duration
    self.time_now = 0
    self.adult_mode = adult_mode

class UrTube:
  def __init__(self):
    self.users = []
    self.videos = []
    self.current_user = None

  def log_in(self, nickname, password):
    for user in self.users:
      if user.nickname == nickname and user.password == password:
        self.current_user = user
        print(f"Пользователь {nickname} успешно авторизован!")
        return
    print("Неверный логин или пароль")

  def register(self, nickname, password, age):
    for user in self.users:
      if user.nickname == nickname:
        print(f"Пользователь {nickname} уже существует")
        return
    self.users.append(User(nickname, password, age))
    self.log_in(nickname, password)
    print(f"Пользователь {nickname} успешно зарегистрирован!")

  def log_out(self):
    self.current_user = None
    print("Выход из аккаунта")

  def add(self, *videos):
    for video in videos:
      if video.title not in [v.title for v in self.videos]:
        self.videos.append(video)
        print(f"Видео {video.title} добавлено")

  def get_videos(self, search_word):
    search_word = search_word.lower()
    return [video.title for video in self.videos if search_word in video.title.lower()]

  def watch_video(self, title):
    if self.current_user is None:
      print("Войдите в аккаунт, чтобы смотреть видео")
      return

    for video in self.videos:
      if video.title == title:
        if video.adult_mode and self.current_user.age < 18:
          print("Вам нет 18 лет, пожалуйста покиньте страницу")
          return
        print(f"Просмотр видео: {video.title}")
        for i in range(1, video.duration + 1):
          print(i, end=' ')
          time.sleep(1)
        print("Конец видео")
        video.time_now = 0
        return

    print(f"Видео {title} не найдено")

# Код для проверки
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
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')