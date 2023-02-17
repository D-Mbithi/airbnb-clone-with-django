from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(FormView):
    """SignUp view"""

    model = CustomUser()
    template_name = "users/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)
