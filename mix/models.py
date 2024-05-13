from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import Media
from tobacco.models import Product


class Category(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=120)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Mix(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=120)
    category = models.ForeignKey(Category, related_name='category_title', on_delete=models.CASCADE,
                                 verbose_name=_('Category'))
    tag = models.ManyToManyField("MixTag", verbose_name=_("Tag"), blank=True)
    components = models.ManyToManyField("MixComponent", verbose_name=_("Components"))

    description = models.TextField(verbose_name=_('Description'))

    strength = models.IntegerField(verbose_name=_('Strength'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Mix')
        verbose_name_plural = _('Mixes')


class MixTag(models.Model):
    title = models.CharField(_('Title'), max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Mix tag')
        verbose_name_plural = _('Mix tags')


class MixComponent(models.Model):
    title = models.CharField(_('Title'), max_length=150)
    product = models.ForeignKey(Product, related_name='product_component', verbose_name=_('Product component'),
                                on_delete=models.CASCADE)
    image = models.ForeignKey(Media, related_name='image_component', verbose_name=_('Image of component'),
                              on_delete=models.CASCADE)
    percentage = models.PositiveSmallIntegerField(verbose_name=_('Percentage'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Component of a mix')
        verbose_name_plural = _('Components of a mix')