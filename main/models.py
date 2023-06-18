from django.db import models

class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

class Manga(models.Model):
    manga_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=252)
    type = models.CharField(max_length=11)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    scored_by = models.IntegerField()
    status = models.CharField(max_length=20)
    volumes = models.IntegerField(null=True, blank=True)
    chapters = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    members = models.IntegerField()
    favorites = models.IntegerField()
    sfw = models.CharField(max_length=5)
    approved = models.CharField(max_length=5)
    created_at_before = models.CharField(max_length=32)
    updated_at = models.CharField(max_length=25, null=True, blank=True)
    real_start_date = models.CharField(max_length=10, null=True, blank=True)
    real_end_date = models.CharField(max_length=10, null=True, blank=True)
    genres = models.CharField(max_length=113)
    themes = models.CharField(max_length=102)
    demographics = models.CharField(max_length=21)
    authors = models.CharField(max_length=4554)
    serializations = models.CharField(max_length=49)
    synopsis = models.CharField(max_length=4583, null=True, blank=True)
    background = models.CharField(max_length=4454, null=True, blank=True)
    main_picture = models.CharField(max_length=54, null=True, blank=True)
    url = models.CharField(max_length=236)
    title_english = models.CharField(max_length=207, null=True, blank=True)
    title_japanese = models.CharField(max_length=98, null=True, blank=True)
    title_synonyms = models.CharField(max_length=295)
    jikan = models.CharField(max_length=5)

    def __str__(self):
        return self.title