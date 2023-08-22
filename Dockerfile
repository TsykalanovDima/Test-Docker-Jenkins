# Устанавливаем базовый образ
FROM seleniarm/standalone-chromium:latest

# Устанавливаем переменную окружения LANG
ENV LANG="en_US.UTF-8"

# Выводим информацию о пользователе
RUN id

# Переключаемся на пользователя root для выполнения команд, требующих прав администратора
USER root

# Выводим путь к chromedriver
RUN which chromedriver

# Выводим путь к chromium
RUN which chromium

# Выводим информацию о системе и версии
RUN uname -a ; cat /etc/issue

RUN apt-get update && apt-get install -y --fix-missing python3 python3-dev python3-selenium python3-pip

# Обновляем репозитории и устанавливаем необходимые пакеты
RUN apt-get update && apt-get install -y python3 python3-dev python3-selenium python3-pip

# Устанавливаем путь для поиска исполняемых файлов
ENV PATH="/usr/bin:${PATH}"

# Устанавливаем необходимые библиотеки
RUN apt-get install -y python3-pytest python3-selenium

# Копируем ваш скрипт в контейнер
COPY Test_0.py /app/Test_0.py

# Указываем рабочую директорию
WORKDIR /app

# Запускаем ваш скрипт
CMD ["python3", "Test_0.py"]
