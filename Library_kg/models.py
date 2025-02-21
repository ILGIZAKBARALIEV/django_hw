from django.db import models

class BookModel(models.Model):
    Genre_choices = (
        ('Фантастика', 'Фантастика'),
        ('Детектив', 'Детектив'),
        ('Роман', 'Роман'),
        ('Поэзия', 'Поэзия'),
        ('Проза', 'Проза'),
        ('Детская литература', 'Детская литература'),
        ('Ужасы', 'Ужасы'),
        ('Приключения', 'Приключения'),
        ('Фэнтези', 'Фэнтези'),
        ('Научная фантастика', 'Научная фантастика'),
        ('Драма', 'Драма'),
        ('Комедия', 'Комедия'),
    )

    title = models.CharField(max_length=255,verbose_name="Название книги")
    image = models.ImageField(upload_to='book_images',verbose_name="загрузить картинку книги")
    description = models.TextField(verbose_name="Описание книги")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Ценна")
    release_date = models.DateField(verbose_name="Дата выхода")
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=50, choices=Genre_choices, verbose_name="Жанр")
    email = models.EmailField(verbose_name="Почта автора")
    author = models.CharField(max_length=255,verbose_name="Имя автора")
    trailer = models.URLField(verbose_name="Ссылка на видео из ютуб", null=True, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

class Review(models.Model):
    STARS_CHOICE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=STARS_CHOICE)

    def __str__(self):
        return self.book.title

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'