import requests
import os

# Функция для получения токена
def get_yd_token(filename):
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r', encoding='utf-8') as f:
            token = f.read().strip()
    else:
        token = ''
    return token

class YandexAPI:
    """
    Класс для работы с API Яндекс.Диска: создание папки, загрузка файла,
    а также сохранение метаинформации о загруженных файлах.
    """

    def __init__(self, ydtoken: str) -> None:
        self.__ydtoken = ydtoken

    @property
    def headers(self) -> dict:
        return {'Authorization': f'OAuth {self.__ydtoken}'}

    def create_folder(self, folder_name) -> None:
        """Создание папки на Яндекс диске"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': folder_name}
        try:
            response = requests.put(url, headers=self.headers, params=params)
        except UnicodeEncodeError:
            raise PermissionError("Неверный токен доступа")
        if response.status_code == 401:
            raise PermissionError("Неверный токен доступа")
        return response.status_code

if __name__ == "__main__":
    # Работа с Яндекс Диском: Создание папки
    yd_token = get_yd_token('yd_token.txt')
    ya_disk = YandexAPI(yd_token)
    print(ya_disk.create_folder('new_directory'))