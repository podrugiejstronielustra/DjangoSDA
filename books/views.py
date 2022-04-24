from uuid import uuid4

from django.core.exceptions import BadRequest
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView

from books.models import BookAuthor, Category, Book
import logging

from books.forms import CategoryForm, AuthorForm

logger = logging.getLogger("Ala")

class AuthorListBaseView(View):
    template_name = "authors_list.html"
    queryset = BookAuthor.objects.all()  # type: ignore

    def get(self, request: WSGIRequest, *args, **kwargs):
        logger.debug(f"{request} ---")
        context = {"authors": self.queryset}
        return render(request, template_name=self.template_name, context=context)

class CategoryListTemplateView(TemplateView):
    template_name = "category_list.html"
    extra_context = {"categories": Category.objects.all()} # type: ignore

class BookListView(ListView):
    template_name = "books_list.html"
    model = Book
    paginate_by = 10

class BookDetailsView(DetailView):
    template_view = "book_detail.html"
    model = Book

    def get_object(self, **kwargs):
        return get_object_or_404(Book, id=self.kwargs.get("pk"))

class CategoryCreateFormView(FormView):
    template_name = "category_form.html"
    form_class = CategoryForm
    success_url = reverse_lazy("category_list")

    def form_invalid(self, form):
        logger.critical(f"FORM CRITICAL ERROR, MORE INFO {form}")
        return super().form_invalid(form)

    def form_valid(self, form):
        result = super().form_valid(form)
        logger.info(f"form = {form}")
        logger.info(f"form.cleaned_data = {form.cleaned_data}")  # cleaned means with removed html indicators
        check_entity = Category.objects.create(**form.cleaned_data)
        logger.info(f"check_entity-id={check_entity.id}")
        return result

class AuthorCreateView(CreateView):
    template_name = "author_form.html"
    form_class = AuthorForm
    success_url = reverse_lazy("authors_list")

def get_hello(request: WSGIRequest) -> HttpResponse:
    hello = "hello world"
    return render(request, template_name="hello_world.html", context={"hello_var": hello})

# 12. Utwórz funkcję zwracającą listę stringów. Stringi niech będą losowym UUID dodawanym do listy. Lista niech posiada 10 elementów.
#
#     a) Zwróć listę jako HTTPResponse (musisz na liście zrobić json.dumps)
#     b) zwróć listę jako JsonResponse


def get_uuids_a(request: WSGIRequest) -> HttpResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return render(request, template_name="uuids.html", context={"elements": uuids} )
    #return HttpResponse(f"uuids={uuids}")

def get_uuids_b(request: WSGIRequest) -> JsonResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return JsonResponse({"uuids":uuids})

def get_argument_from_path(request: WSGIRequest, x: int, y: str, z: str) -> HttpResponse:
    return HttpResponse(f"X = {x}, Y = {y}, Z = {z}")


def get_arguments_from_query(request: WSGIRequest) -> HttpResponse:
    a = request.GET.get("a")
    b = request.GET.get("b")
    c = request.GET.get("c")
    print(type(int("a")))
    return HttpResponse(f"a = {a}, b = {b}, c = {c}")

# 15. Przygotuj funkcję drukująca odpowiedni komunikat dla method HTTP takich jak GET, POST, PUT, DELETE

@csrf_exempt
def check_http_query_types(request: WSGIRequest) -> HttpResponse:
    query_type = "Unknown"
#    if request.method == "GET":
#        query_type = "This is GET"
#    elif request.method == "POST":
#        query_type = "This is POST"
#    elif request.method == "This is PUT":
#        query_type = "This is PUT"
#    elif request.method == "This is DELETE":
#        query_type = "This is DELETE"
#    return HttpResponse(query_type)
    return render(request, template_name="methods.html", context={})

# 21. Przygotuj funkcję, która zwróci informację o headerach HTTP
def get_headers(request: WSGIRequest) -> JsonResponse:
    our_headers = request.headers

    return JsonResponse({"headers": dict(our_headers)})

# 22. Rzuć wyjątkiem HTTP

@csrf_exempt
def raise_error_for_fun(request: WSGIRequest) -> HttpResponse:
    if request.method != "GET":
        raise BadRequest("Method not allowed")
    return HttpResponse("Everything is OK")
