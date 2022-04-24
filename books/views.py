from uuid import uuid4

from django.core.exceptions import BadRequest
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from books.models import BookAuthor, Category


class AuthorListBaseView(View):
    template_name = "authors_list.html"
    queryset = BookAuthor.objects.all()  # type: ignore
    def get(self, request: WSGIRequest, *args, **kwargs):
        context = {"authors": self.queryset}
        return render(request, template_name=self.template_name, context=context)

class CategoryListTemplateView(TemplateView):
    template_name = "category_list.html"
    extra_context = {"categories": Category.objects.all()} # type: ignore



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
