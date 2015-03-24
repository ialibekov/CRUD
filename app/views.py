from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from app.models import Contact
from app.forms import ContactForm


class ContactMixin(object):
    model = Contact


class ContactFormMixin(ContactMixin):
    form_class = ContactForm
    context_object_name = "contact"
    template_name = "app/contact_form.html"


class ContactList(ContactMixin, ListView):
    context_object_name = "contact_list"
    template_name = "app/contact_list.html"


class ViewContact(ContactMixin, DetailView):
    pass


class NewContact(ContactFormMixin, CreateView):
    pass


class EditContact(ContactFormMixin, UpdateView):
    pass


class DeleteContact(ContactMixin, DeleteView):
    template_name = 'app/contact_confirm_delete.html'

    def get_success_url(self):
        return reverse('contact_list')