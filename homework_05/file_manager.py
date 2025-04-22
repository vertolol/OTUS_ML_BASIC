class BaseMediaFile:
    def __init__(self, name, size, creation_date, owner):
        self.name = name
        self.size = size
        self.creation_date = creation_date
        self.owner = owner

    def save(self):
        """Сохранить файл (реализация зависит от типа хранения)"""
        pass

    def delete(self):
        """Удалить файл"""
        pass

    def get_metadata(self):
        """Получить метаданные файла"""
        return {
            "name": self.name,
            "size": self.size,
            "creation_date": self.creation_date,
            "owner": self.owner
        }


class AudioFile(BaseMediaFile):
    def __init__(self, name, size, creation_date, owner, duration, bitrate):
        super().__init__(name, size, creation_date, owner)
        self.duration = duration
        self.bitrate = bitrate

    def convert(self, format):
        """Конвертировать аудиофайл в другой формат"""
        pass


class VideoFile(BaseMediaFile):
    def __init__(self, name, size, creation_date, owner, duration, resolution):
        super().__init__(name, size, creation_date, owner)
        self.duration = duration
        self.resolution = resolution

    def extract_features(self):
        """Извлечь характеристики видео"""
        pass


class PhotoFile(BaseMediaFile):
    def __init__(self, name, size, creation_date, owner, resolution):
        super().__init__(name, size, creation_date, owner)
        self.resolution = resolution

    def apply_filter(self, filter_name):
        """Применить фильтр к фотографии"""
        pass


class LocalStorage:
    def __init__(self, path):
        self.path = path

    def save(self, media_file):
        """Сохранить медиа-файл на локальном диске"""
        pass

    def delete(self, media_file):
        """Удалить медиа-файл с локального диска"""
        pass


class CloudStorage:
    def __init__(self, cloud_service):
        self.cloud_service = cloud_service

    def upload(self, media_file):
        """Загрузить медиа-файл в облачное хранилище"""
        pass

    def delete(self, media_file):
        """Удалить медиа-файл из облачного хранилища"""
        pass


# Создание медиа-файлов
audio = AudioFile("song.mp3", 5000000, "2023-01-01", "User1", 240, 320)
video = VideoFile("movie.mp4", 1500000000, "2023-01-02", "User2", 120, "1920x1080")
photo = PhotoFile("image.jpg", 3000000, "2023-01-03", "User3", "1920x1080")

# Работа с локальным хранилищем
local_storage = LocalStorage("/path/to/local/storage")
local_storage.save(audio)
local_storage.save(video)

# Работа с облачным хранилищем
cloud_storage = CloudStorage("MyCloudService")
cloud_storage.upload(photo)


"""
Перспективы добавления нового функционала

Добавление новых типов медиа-файлов: Если мы захотим добавить новый тип медиа-файла (например, DocumentFile), 
нам нужно будет создать новый класс, который наследует от BaseMediaFile, 
и реализовать специфические методы. Это не потребует изменения существующих классов, что делает систему расширяемой.

Добавление новых способов хранения: Аналогично, если мы захотим добавить новый способ хранения (например, FTPStorage), 
мы можем создать новый класс, который реализует методы для работы с FTP, не затрагивая существующие классы.
"""
