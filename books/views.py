from uuid import uuid4

from django.core.exceptions import BadRequest
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# 11. Utwórz pierwszą funkcję widoku drukująca/zwracająca hello world (pamietaj dodać ją do urls.py - moesz ustawić jej name).
from django.views.decorators.csrf import csrf_exempt


def get_hello(request: WSGIRequest) -> HttpResponse:
    return HttpResponse("hello world")


# 12. Utwórz funkcję zwracającą listę stringów. Stringi niech będą losowym UUID ( dodawanym do listy. Lista niech posiada 10 elementów.

#    a) Zwróć listę jako HTTPResponse (musisz na liście zrobić json.dumps)
#    b) zwróć listę jako JsonResponse

def get_uuids_a(request: WSGIRequest) -> HttpResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return HttpResponse (f"uuids={uuids}")

def get_uuids_b(request: WSGIRequest) -> JsonResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return JsonResponse({"uuids":uuids})

#13. Napisz funkcję przyjmującą argumenty w ściezce (path arguments) i wydrukuj je.
# Dwa argumenty pierwszy typu int, drugi typu str, trzeci typu slug .



def get_argument_from_path(request: WSGIRequest, x: int, y: str, z: str) -> HttpResponse:
    return HttpResponse(f"X = {x}, Y = {y}, Z = {z}")

#14. Napisz funkcję przyjmującą argumenty a,b,c jako zapytanie (query arguments <?> [po znaku zapytania]) i wydrukuj je

def get_arguments_from_query(request: WSGIRequest) -> HttpResponse:
    a = request.GET.get("a")
    b = request.GET.get("b")
    c = request.GET.get("c")
    print(type(a))
    return HttpResponse(f"A = {a}, B = {b}, C = {c}")

#15. Przygotuj funkcję drukująca odpowiedni komunikat dla method HTTP takich jak GET, POST, PUT, DELETE
#15. Wykonaj zapytanie typu GET, sprawdź czy wykonana została poprawna metoda drukując jakaś informacje w ifie.
#16. Wykonaj zapytanie typu POST, zrób to samo co poprzednio
#17. Wykonaj zapytanie typu PUT, -||-.
#18. Wykonaj zapytanie typu DELETE, -||-.
#19. Przygotuj funkcję która zwróci informację o headerach HTTP
#20. Rzuć wyjątkiem HTTP
#20. Dodaj routing w urls projektu do urls aplikacji

@csrf_exempt
def check_http_query_type(request: WSGIRequest) -> HttpResponse:
    query_type = "Unknown"
    if request.method=="GET":
        query_type="this is GET"
    elif request.method=="POST":
        query_type="this is POST"
    elif request.method=="PUT":
        query_type="this is PUT"
    elif request.method=="DELETE":
        query_type="this is DELETE"
    return HttpResponse(query_type)

# 21. Przygotuj funkcję która zwróci informację o headerach HTTP

def get_headers(request: WSGIRequest) -> JsonResponse:
    our_headers= request.headers

    return JsonResponse({"headers": dict(our_headers)})

# 22. Rzuć wyjątkiem HTTP

@csrf_exempt
def raise_error_for_fun(request: WSGIRequest) -> HttpResponse:
    if request.method != "GET":
        raise BadRequest("method not allowed")

    return HttpResponse("wszystko GIT")

# 23. Dodaj routing w urls projektu do urls aplikacji

