from django.db import models
from django.utils.html import mark_safe

class Category(models.Model):
    name = models.CharField('название категории', max_length=255)
    icon = models.ImageField(upload_to='images/', null=True, blank=True)

    def image_tag(self):
        return mark_safe(f'<img src="{self.icon.url}" width="150" height="150"/>')

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    class Meta:
        verbose_name_plural = 'Categories'


class Level(models.Model):
    name = models.CharField('уровень владения языком', max_length=255)
    code = models.CharField('код уровня владения языком', max_length=2)


class Theme(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    name = models.CharField('название темы', max_length=255)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)

    def image_tag(self):
        return mark_safe(f'<img src="{self.photo.url}" width="150" height="150"/>')

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class Word(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    name = models.CharField('слово', max_length=255)
    translate = models.CharField('перевод', max_length=255)
    transcription = models.CharField('транскрипция', max_length=255)
    example = models.CharField('пример употребления слова', max_length=255)
    sound = models.FileField('произношение слова', upload_to='sounds/', blank=True)

    def audio_tag(self):
        return mark_safe(
            f'<audio controls>'
            f'<source src="{self.sound.url}" type="audio/mpeg">'
            f'</audio>')
