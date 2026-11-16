import os
import requests

def run_agent_script():
    
    JOURNAL_NUMBER = 9

    # --- ЭТАП 1. Разведка ---
    print("=== ЭТАП 1: РАЗВЕДКА ===")
    target_name = input("Введите имя цели: ").strip()

    age = None
    gender = None
    female_prob = 0.0

    try:
        # Запрос возраста
        age_resp = requests.get("https://api.agify.io", params={"name": target_name}, timeout=5)
        age_resp.raise_for_status()
        age_data = age_resp.json()
        age = age_data.get("age")

        # Запрос пола
        gender_resp = requests.get("https://api.genderize.io", params={"name": target_name}, timeout=5)
        gender_resp.raise_for_status()
        gender_data = gender_resp.json()
        gender = gender_data.get("gender")
        prob = gender_data.get("probability", 0.0)

        # Рассчитываем вероятность именно женского пола в процентах
        if gender == "female":
            female_prob = round(prob * 100, 1)
        elif gender == "male":
            female_prob = round((1 - prob) * 100, 1)
        else:
            female_prob = 0.0

        print(f"Цель: {target_name.capitalize()}. Вероятный возраст: {age}. Вероятность женского пола: {female_prob}%.\n")

    except requests.exceptions.RequestException as e:
        print(f"[Ошибка Этапа 1] Не удалось получить биометрию цели: {e}\n")

    # --- ЭТАП 2. Маскировка ---
    print("=== ЭТАП 2: МАСКИРОВКА ===")
    
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) СекретныйАгентБот/1.0".encode("utf-8").decode("latin-1")

    headers = {
        "User-Agent": user_agent,
        "Accept-Language": "ru-RU,ru;q=0.9"
    }
    params = {"userId": JOURNAL_NUMBER}

    posts_count = 0

    try:
        posts_resp = requests.get(
            "https://jsonplaceholder.typicode.com/posts",
            params=params,
            headers=headers,
            timeout=5
        )
        posts_resp.raise_for_status()
        posts = posts_resp.json()
        posts_count = len(posts)

        print(f"Получено постов: {posts_count}")
        if posts:
            print(f"Заголовок первого поста: «{posts[0]['title']}»\n")
        else:
            print("Посты для данного userId не найдены.\n")

    except requests.exceptions.RequestException as e:
        print(f"[Ошибка Этапа 2] Сбой при сборе цифровой активности: {e}\n")

    # --- ЭТАП 3. Передача данных ---
    print("=== ЭТАП 3: ПЕРЕДАЧА ДАННЫХ ===")
    dossier = {
        "name": target_name,
        "age": age,
        "gender": gender,
        "posts_count": posts_count
    }

    try:
        post_resp = requests.post("https://httpbin.org/post", json=dossier, timeout=5)
        post_resp.raise_for_status()
        server_answer = post_resp.json()

        print("Сервер принял отчет как JSON. Поле 'json' из ответа:")
        print(server_answer.get("json"), "\n")

    except requests.exceptions.RequestException as e:
        print(f"[Ошибка Этапа 3] Не удалось передать отчет на базу: {e}\n")

    # --- ЭТАП 4. Загрузка улик ---
    print("=== ЭТАП 4: ЗАГРУЗКА УЛИК ===")
    filename = "evidence.jpg"
    img_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/535.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        img_resp = requests.get("https://dummyimage.com/400/300", stream=True, timeout=10)
        img_resp.raise_for_status()

        with open(filename, "wb") as file:
            for chunk in img_resp.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)

        file_size = os.path.getsize(filename)
        print(f"Улика успешно сохранена в '{filename}'. Размер файла: {file_size} байт.\n")

    except requests.exceptions.RequestException as e:
        print(f"[Ошибка Этапа 4] Не удалось скачать фотографию цели: {e}\n")

    # --- ЭТАП 5. Обработка сбоев ---
    print("=== ЭТАП 5: ТЕСТИРОВАНИЕ СБОЕВ СВЯЗИ ===")

    try:
        print("Попытка подключения к секретному узлу (ожидаем 404)...")
        resp_404 = requests.get("https://httpbin.org/status/404", timeout=5)
        resp_404.raise_for_status()  # Принудительно вызываем исключение для кодов 4xx/5xx
    except requests.exceptions.HTTPError as e:
        print(f"[Перехвачен HTTPError] Узел не найден (ошибка клиента/сервера): {e}")
    except requests.exceptions.RequestException as e:
        print(f"[Сетевая ошибка] {e}")

    try:
        print("Попытка подключения к медленному серверу (лимит 3 сек, задержка 6 сек)...")
        resp_delay = requests.get("https://httpbin.org/delay/6", timeout=3)
        resp_delay.raise_for_status()
    except requests.exceptions.Timeout:
        print("[Перехвачен Timeout] Связь с базой нестабильна: сервер не ответил за отведенные 3 секунды!")
    except requests.exceptions.RequestException as e:
        print(f"[Сетевая ошибка] {e}")

if __name__ == "__main__":
    run_agent_script()
