import sqlite3

# Подключение к базе данных
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Создание таблицы books
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
"""
)
conn.commit()


# 1. CREATE — Добавление книги
def create_book(title: str, author: str, price: float, quantity: int):
    cursor.execute(
        """
        INSERT INTO books (title, author, price, quantity)
        VALUES (?, ?, ?, ?)
    """,
        (title, author, price, quantity),
    )
    conn.commit()
    print(f"Книга '{title}' успешно добавлена!")


# 2. READ — Получение списка всех книг
def read_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    print("\n--- Список книг в базе ---")
    if not books:
        print("База данных пуста.")
    else:
        for book in books:
            print(
                f"ID: {book[0]} | Название: {book[1]} | Автор: {book[2]} | Цена: {book[3]} сом | Кол-во: {book[4]}"
            )
    print("--------------------------\n")


# 3. UPDATE — Обновление цены книги по ID
def update_book_price(book_id: int, new_price: float):
    cursor.execute(
        """
        UPDATE books
        SET price = ?
        WHERE id = ?
    """,
        (new_price, book_id),
    )
    conn.commit()
    print(f"Цена книги с ID {book_id} обновлена до {new_price}!")


# 4. DELETE — Удаление книги по ID
def delete_book(book_id: int):
    cursor.execute(
        """
        DELETE FROM books
        WHERE id = ?
    """,
        (book_id,))
    conn.commit()
    print(f"Книга с ID {book_id} удалена!")


# Проверка работы
if __name__ == "__main__":
    # Добавляем книги
    create_book("Мастер и Маргарита", "М. Булгаков", 450.0, 10)
    create_book("1984", "Дж. Оруэлл", 500.0, 5)

    # Читаем базу
    read_books()

    # Обновляем цену у первой книги (ID = 1)
    update_book_price(1, 490.0)

    # Проверяем изменения
    read_books()

    # Удаляем вторую книгу (ID = 2)
    delete_book(2)

    # Итоговый просмотр
    read_books()

    # Закрываем соединение
    conn.close()