from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 4
    max_page_size = 7
    page_size_query_param = 'records'



class LimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3



class CursorPagination(CursorPagination):
    page_size = 3
    ordering = 'name'