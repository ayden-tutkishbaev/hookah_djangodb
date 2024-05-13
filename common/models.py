from django.db import models

from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User


class Media(models.Model):
    class FileType(models.TextChoices):
        IMAGE = 'image', _("Image")
        VIDEO = 'video', _("Video")
        DOCUMENT = 'document', _("document")
        GIF = 'gif', _("Gif")
        OTHER = 'other', _("Other")

    file = models.FileField(upload_to='only_medias/', verbose_name=_("File"),
                            validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'mp4', 'avi',
                                                                                   'mov', 'gif', 'webp', 'pdf', 'doc',
                                                                                   'docx', 'mpeg'])])
    file_type = models.CharField(max_length=10, verbose_name=_("File Type"),
                                 choices=FileType.choices)

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media")

    def __str__(self):
        element = r"""[\]"""
        return f'Id: {self.id}|Name: {self.file.name.split(element)[-1]}'

    def clean(self):
        if self.file_type not in self.FileType.values:
            raise ValidationError(_("Invalid File Type"))
        elif self.file_type == self.FileType.IMAGE:
            if self.file.name.split('.')[-1] not in ['jpg', 'jpeg', 'png', 'webp']:
                raise ValidationError(_("Invalid Image File"))
        elif self.file_type == self.FileType.VIDEO:
            if self.file.name.split('.')[-1] not in ['mp4', 'avi', 'mov', 'mpeg']:
                raise ValidationError(_("Invalid Video File"))


class CommonSettings(models.Model):
    main_back_page = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name=_('Main Back Page'),
                                       related_name='main_back_page')
    copyright = models.CharField(_('Copyright'), max_length=150)
    second_back_page = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name=_('Second back page'),
                                         related_name='second_back_page')

    def __str__(self):
        return self.copyright

    class Meta:
        verbose_name = _("Common Settings")
        verbose_name_plural = _("Common Settings")


class Comment(models.Model):
    created_at = models.DateTimeField(verbose_name=_('Created_at'), auto_now_add=True)
    author = models.ForeignKey(User, verbose_name=_('Author'), on_delete=models.CASCADE, related_name='comment_author')
    stars = models.IntegerField(_('Stars'))
    text = models.TextField(_('Text'))


class DataHandling(models.Model):
    headline = models.CharField(verbose_name=_('Headline'), max_length=120)
    text = models.TextField(verbose_name=_('Text'))


class Policy(models.Model):
    headline = models.CharField(verbose_name=_('Headline'), max_length=120)
    text = models.TextField(verbose_name=_('Text'))
