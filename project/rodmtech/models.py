# Import necessary Django modules.

from django.db import models
from django.utils.translation import uggettext_lazy as _

# Import necessary Mezzanine modules.

from mezzanine.pages.models import Page, RichText

# Model for DocPage

class DocPage(Page, RichText):
    """

    A doc tree page
    """

    add_toc = models.BooleanField(_("Add TOC"), default=False,
                                help_text = _("Include a list of child links"))


    class Meta:
        verbose_name        = _("Doc Page")
        verbose_name_plural = _("Doc Pages")
