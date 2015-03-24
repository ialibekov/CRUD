from django.conf.urls import patterns, url, include
from app.views import ContactList, ViewContact, NewContact, EditContact, DeleteContact

contact_urls = patterns(
    '',
    url(r'^$', ViewContact.as_view(), name='contact_detail'),
    url(r'^update$', EditContact.as_view(), name='contact_update'),
    url(r'^delete$', DeleteContact.as_view(), name='contact_delete'),
)

urlpatterns = patterns(
    '',
    url(r'^$', ContactList.as_view(), name='contact_list'),
    url(r'^add$', NewContact.as_view(), name='contact_add'),
    url(r'^(?P<slug>[\w-]+)/', include(contact_urls)),
)
