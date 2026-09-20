import sqlite3

# Подключаемся к базе данных cinema.db
conn = sqlite3.connect("cinema.db")
cursor = conn.cursor()

# Создаем таблицу пользователей
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

# Создаем таблицу фильмов
cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL
)
""")

# Создаем связующую таблицу отзывов
cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER CHECK(rating >= 1 AND rating <= 10),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
)
""")

conn.commit()

# Очищаем таблицы перед заполнением
cursor.execute("DELETE FROM reviews")
cursor.execute("DELETE FROM movies")
cursor.execute("DELETE FROM users")

# Добавляем 5 пользователей
users_data = [
    ("Алихан",),
    ("Айпери",),
    ("Данияр",),
    ("София",),
    ("Бексултан",)
]
cursor.executemany("INSERT INTO users (name) VALUES (?)", users_data)

# Добавляем 5 фильмов
movies_data = [
    ("Начало", "Фантастика"),
    ("Побег из Шоушенка", "Драма"),
    ("Интерстеллар", "Фантастика"),
    ("Темный рыцарь", "Боевик"),
    ("Дюна 2", "Фантастика")
]
cursor.executemany("INSERT INTO movies (title, genre) VALUES (?, ?)", movies_data)

# Добавляем 10 отзывов (user_id, movie_id, rating)
reviews_data = [
    (1, 1, 9),
    (1, 3, 10),
    (2, 1, 8),
    (2, 2, 10),
    (3, 2, 9),
    (3, 4, 10),
    (4, 3, 7),
    (4, 4, 8),
    (5, 1, 10),
    (5, 2, 9)
]
cursor.executemany("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)", reviews_data)

conn.commit()

# 1. Запрос: Имя пользователя + Название фильма + Оценка 
print("=== 1. Имя пользователя + Фильм + Оценка ===")
cursor.execute("""
SELECT users.name, movies.title, reviews.rating
FROM reviews
JOIN users ON reviews.user_id = users.id
JOIN movies ON reviews.movie_id = movies.id
""")
for row in cursor.fetchall():
    print(f"Пользователь: {row[0]} | Фильм: {row[1]} | Оценка: {row[2]}")

# 2. Запрос: ВСЕ фильмы включая те, у которых нет отзывов (LEFT JOIN)
print("\n=== 2. ВСЕ фильмы (даже без отзывов) ===")
cursor.execute("""
SELECT movies.title, reviews.rating
FROM movies
LEFT JOIN reviews ON movies.id = reviews.movie_id
""")
for row in cursor.fetchall():
    rating_str = row[1] if row[1] is not None else "Нет оценок"
    print(f"Фильм: {row[0]} | Оценка: {rating_str}")

# 3. Агрегации: Подсчет средней, максимальной и минимальной оценки
print("\n=== Статистика по оценкам ===")
cursor.execute("""
SELECT 
    AVG(rating),
    MAX(rating),
    MIN(rating)
FROM reviews
""")
stats = cursor.fetchone()

print(f"Средняя оценка всех фильмов: {stats[0]:.2f}")
print(f"Максимальная оценка: {stats[1]}")
print(f"Минимальная оценка: {stats[2]}")

# Закрываем соединение с базой данных
conn.close()