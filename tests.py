from main import BooksCollector


class TestBooksCollector:
# проверка метода add_new_book
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

#проверка метода set_book_genre
    def test_set_book_genre_check_genre_for_newbook(self):
        new_book = BooksCollector()
        new_book.add_new_book('Ужасы нашего городка')
        new_book.set_book_genre('Ужасы нашего городка', 'Ужасы')
        assert new_book.books_genre['Ужасы нашего городка'] == 'Ужасы'

#проверка метода get_book_genre
    def test_get_book_genre_show_newbook_genre(self):
        new_book = BooksCollector()
        new_book.add_new_book('Ужасы нашего городка')
        new_book.set_book_genre('Ужасы нашего городка', 'Ужасы')
        assert new_book.get_book_genre('Ужасы нашего городка') == 'Ужасы'


#проверка метода get_books_with_specific_genre
    def test_get_books_with_specific_genre_2_horror_books(self):
        new_book = BooksCollector()
        new_book.add_new_book('Ужасы нашего городка')
        new_book.add_new_book('Уж полночь')
        new_book.add_new_book('Мойдодыр')
        new_book.add_new_book('Айболит')
        new_book.set_book_genre('Ужасы нашего городка', 'Ужасы')
        new_book.set_book_genre('Уж полночь', 'Ужасы')
        new_book.set_book_genre('Мойдодыр', 'Мультфильмы')
        new_book.set_book_genre('Лиловый шар', 'Фантастика')
        assert new_book.get_books_with_specific_genre('Ужасы') == ['Ужасы нашего городка', 'Уж полночь']

#проверка метода get_books_genre
    def test_get_books_genre_shows_4_newbooks(self):
        new_book = BooksCollector()
        new_book.add_new_book('Ужасы нашего городка')
        new_book.add_new_book('Уж полночь')
        new_book.add_new_book('Мойдодыр')
        new_book.set_book_genre('Ужасы нашего городка', 'Ужасы')
        new_book.set_book_genre('Уж полночь', 'Ужасы')
        new_book.set_book_genre('Мойдодыр', 'Мультфильмы')
        assert new_book.get_books_genre() == {'Ужасы нашего городка':'Ужасы', 'Уж полночь':'Ужасы', 'Мойдодыр':'Мультфильмы'}

#проверка метода get_books_for_children
    def test_get_books_for_children_1_animation(self):
        new_book = BooksCollector()
        new_book.add_new_book('Ужасы нашего городка')
        new_book.add_new_book('Уж полночь')
        new_book.add_new_book('Мойдодыр')
        new_book.set_book_genre('Ужасы нашего городка', 'Ужасы')
        new_book.set_book_genre('Уж полночь', 'Ужасы')
        new_book.set_book_genre('Мойдодыр', 'Мультфильмы')
        assert new_book.get_books_for_children() == ['Мойдодыр']

#проверка метода add_book_in_favorites
    def test_add_book_in_favorites_add_1_book(self):
        new_book = BooksCollector()
        new_book.add_new_book('Ужасы нашего городка')
        new_book.add_new_book('Уж полночь')
        new_book.add_new_book('Мойдодыр')
        new_book.set_book_genre('Ужасы нашего городка', 'Ужасы')
        new_book.set_book_genre('Уж полночь', 'Ужасы')
        new_book.set_book_genre('Мойдодыр', 'Мультфильмы')
        favorites = new_book.add_book_in_favorites('Уж полночь')
        assert new_book.favorites == ['Уж полночь']

#проверка метода delete_book_from_favorites
    def test_delete_book_from_favorites_empty_list(self):
        new_book = BooksCollector()
        new_book.add_new_book('Ужасы нашего городка')
        new_book.add_new_book('Уж полночь')
        new_book.add_new_book('Мойдодыр')
        new_book.set_book_genre('Ужасы нашего городка', 'Ужасы')
        new_book.set_book_genre('Уж полночь', 'Ужасы')
        new_book.set_book_genre('Мойдодыр', 'Мультфильмы')
        favorites = new_book.add_book_in_favorites('Мойдодыр')
        favorites = new_book.delete_book_from_favorites('Мойдодыр')
        assert new_book.favorites == [ ]

#проверка метода get_list_of_favorites_books
    def test_get_list_of_favorites_books_two_favorites(self):
        new_book = BooksCollector()
        new_book.add_new_book('Ужасы нашего городка')
        new_book.add_new_book('Уж полночь')
        new_book.add_new_book('Мойдодыр')
        new_book.set_book_genre('Ужасы нашего городка', 'Ужасы')
        new_book.set_book_genre('Уж полночь', 'Ужасы')
        new_book.set_book_genre('Мойдодыр', 'Мультфильмы')
        favorites = new_book.add_book_in_favorites('Уж полночь')
        favorites = new_book.add_book_in_favorites('Мойдодыр')
        assert new_book.get_list_of_favorites_books() == ['Уж полночь', 'Мойдодыр']

#негативная проверка добавления в избранное книги, которая там уже есть, метод add_book_in_favorites
    def test_add_book_in_favorites_adding_existing_book(self):
        new_book = BooksCollector()
        new_book.add_new_book('Ужасы нашего городка')
        new_book.add_new_book('Уж полночь')
        new_book.add_new_book('Мойдодыр')
        new_book.set_book_genre('Ужасы нашего городка', 'Ужасы')
        new_book.set_book_genre('Уж полночь', 'Ужасы')
        new_book.set_book_genre('Мойдодыр', 'Мультфильмы')
        favorites = new_book.add_book_in_favorites('Уж полночь')
        favorites = new_book.add_book_in_favorites('Уж полночь')
        assert new_book.get_list_of_favorites_books() == ['Уж полночь']




