from django.views.generic import CreateView, DetailView, UpdateView, FormView
from django.urls import reverse_lazy
from .models import StaffInformation, Department, Book, Staff
from .forms import StaffInformationForm, DepartmentForm, BookForm, StaffForm, StaffInformationUpdateForm


class StaffDetailView(DetailView):
    model = Staff
    template_name='myapp2/staff_detail.html'


class StaffInformationCreateView(CreateView):
    model = StaffInformation
    form_class = StaffInformationForm
    template_name = 'myapp2/staff_information_create.html'
    success_url = reverse_lazy('myapp:home')


class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'myapp2/department_create.html'
    success_url = reverse_lazy('myapp:home')


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'myapp2/book_create.html'
    success_url = reverse_lazy('myapp:home')


class StaffCreateView(CreateView):
    model = Staff
    form_class = StaffForm
    template_name = 'myapp2/staff_create.html'
    success_url = reverse_lazy('myapp:home')

class StaffInformationUpdateView(UpdateView):
    model = StaffInformation
    form_class = StaffInformationUpdateForm
    template_name = 'myapp2/staff_information_update.html'
    success_url = reverse_lazy('myapp:home')
