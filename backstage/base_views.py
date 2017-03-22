from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin

from account.models import Privilege

def index(request):
    return render(request, 'backstage/index.jinja2')


class BaseBackstageMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.privilege in (Privilege.ADMIN, Privilege.ROOT)


@method_decorator(login_required(), name='dispatch')
class BaseCreateView(BaseBackstageMixin, CreateView):

    def post_create(self, instance):
        """
        Do something here
        """
        pass

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_by = self.request.user
        self.post_create(instance)
        instance.save()
        messages.success(self.request, "%s was successfully added." % self.form_class.Meta.model.__name__)
        return HttpResponseRedirect(self.get_redirect_url(instance))

    def get_redirect_url(self, instance):
        raise NotImplementedError("Method get_redirect_url should be implemented")


@method_decorator(login_required(), name='dispatch')
class BaseUpdateView(BaseBackstageMixin, UpdateView):

    def post_update(self, instance):
        """
        Do something here
        """
        pass

    def form_valid(self, form):
        instance = form.save(commit=False)
        self.post_update(instance)
        instance.save()
        messages.success(self.request, "Your changes have been saved.")
        return HttpResponseRedirect(self.get_redirect_url(instance))

    def get_redirect_url(self, instance):
        return self.request.path