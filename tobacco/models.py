from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import Media


class Country(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('Country name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class Manufacturer(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=100)

    class Meta:
        verbose_name = _("manufacturer")
        verbose_name_plural = _("manufacturers")

    def __str__(self):
        return self.name


class Taste(models.Model):
    title = models.CharField(verbose_name=_("title"), max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Taste")
        verbose_name_plural = _("Tastes")


class Type(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Type")
        verbose_name_plural = _("Types")


class Product(models.Model):
    class Strength(models.TextChoices):
        STRONG = 'strong', _('strong')
        MEDIUM = 'medium', _('medium')
        WEAK = 'weak', _('weak')

    title = models.CharField(verbose_name=_("title"), max_length=120)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name=_("manufacturer"),
                                     related_name='product_manufacturer')
    leaf = models.CharField(verbose_name=_("leaf"), max_length=250)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='product_country',
                                verbose_name='product_country')

    composition = models.CharField(verbose_name=_("composition"), max_length=250)

    strength = models.CharField(verbose_name=_("strength"), max_length=120, choices=Strength.choices)

    taste = models.ForeignKey(Taste, verbose_name=_('Product taste'), related_name='product_taste',
                              on_delete=models.CASCADE)
    type = models.ForeignKey(Type, verbose_name=_('Product type'), related_name='product_type', on_delete=models.CASCADE)

    photo = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name=_('photo'), related_name='product_photo')
    description = models.TextField(verbose_name=_('Description'))
    tag = models.ManyToManyField('ProductTag', verbose_name=_('tag'), blank=True)
    prep_method = models.ManyToManyField('PrepMethod', verbose_name=_('tag'), blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Tobacco product')
        verbose_name_plural = _('Tobacco products')


class ProductTag(models.Model):
    title = models.CharField(verbose_name=_("title"), max_length=120)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("product tag")
        verbose_name_plural = _("product tags")


class PrepMethod(models.Model):
    title = models.CharField(_("title"), max_length=400)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Preparation method")
        verbose_name_plural = _("Preparation methods")