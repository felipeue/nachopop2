from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect


class PermissionAlumno(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy("login"))
        elif not request.user.profile.is_owner:
            return HttpResponseRedirect(reverse_lazy("logout"))
        else:
            return super(PermissionAlumno, self).dispatch(request, *args, **kwargs)