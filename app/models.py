from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import RegexValidator
from localflavor.us.models import PhoneNumberField

valid_name = RegexValidator(regex=r'[\w-]+', message=u"The name should consist of latin letters, numbers, underscore and dash")


class Contact(models.Model):
    first_name = models.CharField(max_length=80, validators=[valid_name])
    last_name = models.CharField(max_length=80, blank=True, validators=[valid_name])
    home_phone = PhoneNumberField(blank=True)
    mobile_phone = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __unicode__(self):
        return u"{0}_{1}".format(self.first_name, self.last_name) if self.last_name != '' else u"{0}".format(self.first_name)

    def save(self, *args, **kwargs):
        self.slug = slugify(unicode(self.full_name()))
        return super(Contact, self).save(*args, **kwargs)

    def full_name(self):
        return u"{0} {1}".format(self.first_name, self.last_name) if self.last_name != '' else u"{0}".format(self.first_name)

    @models.permalink
    def get_absolute_url(self):
        return "contact_detail", [self.slug]

    @models.permalink
    def get_update_url(self):
        return "contact_update", [self.slug]

    @models.permalink
    def get_delete_url(self):
        return "contact_delete", [self.slug]