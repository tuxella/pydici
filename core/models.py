# coding: utf-8
"""
Database access layer for pydici core module
@author: Sébastien Renard (sebastien.renard@digitalfox.org)
@license: AGPL v3 or newer (http://www.gnu.org/licenses/agpl-3.0.html)
"""

from django.db import models

from django.utils.translation import ugettext_lazy as _


class Subsidiary(models.Model):
    """Internal company / organisation unit"""
    name = models.CharField(_("Name"), max_length=200, unique=True)
    code = models.CharField(_("Code"), max_length=3, unique=True)

    def __unicode__(self): return self.name

    class Meta:
        verbose_name = _("Subsidiary")
        verbose_name_plural = _("Subsidiaries")
