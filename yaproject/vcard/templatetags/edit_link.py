from django import template
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def admin_link(vcard, user):
    if user.is_authenticated() and user.is_superuser:
        link = reverse('admin:vcard_vcard_change', args=[vcard.pk])
        return mark_safe('<a href="%s"> (admin) </a>' % link)
