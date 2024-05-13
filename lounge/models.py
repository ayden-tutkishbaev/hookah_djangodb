from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import Media


class Metro(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('Metro name'))
    location = models.CharField(max_length=120, verbose_name=_('Location'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Metro')
        verbose_name_plural = _('Metros')


class Lounge(models.Model):
    location = models.ForeignKey(Metro, verbose_name=_("Location, metro"), on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120, verbose_name=_("Title"))
    price = models.FloatField(verbose_name=_("Price"))
    rating_google = models.FloatField(verbose_name=_('Google rating'))
    rating_yandex = models.FloatField(verbose_name=_('Yandex rating'))
    working_hours = models.CharField(verbose_name=_('Working hours'), max_length=120)
    phone = models.CharField(max_length=100, verbose_name=_('Phone number'))
    description = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Lounge')
        verbose_name_plural = _('Lounges')


class LoungeImage(models.Model):
    lounge = models.ForeignKey(Lounge, on_delete=models.CASCADE, related_name='lounge', verbose_name=_('Lounge'))
    main_image = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='main_image',
                                   verbose_name=_('Main Image'))
    image2 = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='second_image',
                               verbose_name=_('Second Image'), blank=True, null=True)
    image3 = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='third_image',
                               verbose_name=_('Third Image'), blank=True, null=True)
    image4 = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='fourth_image',
                               verbose_name=_('Fourth Image'), blank=True, null=True)

    # def __str__(self):
    #     return self.lounge

    class Meta:
        verbose_name = _('Lounge image')
        verbose_name_plural = _('Lounge images')

