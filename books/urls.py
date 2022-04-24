from django.urls import path

from books.views import get_uuids_a, get_uuids_b, get_argument_from_path, get_arguments_from_query, \
    check_http_query_types, get_headers, raise_error_for_fun, AuthorListBaseView, CategoryListTemplateView

urlpatterns = [
    path('uuids-a', get_uuids_a),
    path('uuids-b', get_uuids_b),
    path('path-args/<int:x>/<str:y>/<slug:z>/', get_argument_from_path, name="get_from_path"),
    path('query-args/<int:x>/<str:y>/<slug:z>/', get_arguments_from_query, name="get_from_query"),
    path('query-types', check_http_query_types, name="check_query_types"),
    path('get-headers', get_headers, name="get_headers"),
    path('raise-error', raise_error_for_fun, name="raise_error"),
    path('authors_list', AuthorListBaseView.as_view(), name="authors_list"),
    path('category_list', CategoryListTemplateView.as_view(), name="category_list"),
]