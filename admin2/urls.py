from django.contrib import admin
from django.urls import path

from admin2.views import (AdminPanelTemplateView, AdminBookListView, AdminBookCreateView, AdminBookDeleteView,
                          AdminBookUpdateView, UnitListView, UnitCreateView, UnitDeleteView, UnitUpdateView,
                          BookSearchView, UnitSearchView, VocabCreateView, VocabTemplateView,
                          )

urlpatterns = [
    path('panel', AdminPanelTemplateView.as_view() , name='admin-panel'),
    path('panel/book/list', AdminBookListView.as_view() , name='admin-book-list'),
    path('panel/book/search', BookSearchView.as_view(), name='admin-book-search'),

    path('panel/book/create', AdminBookCreateView.as_view() , name='admin-book-create'),
    path('panel/book/delete/<int:pk>', AdminBookDeleteView.as_view() , name='admin-book-delete'),
    path('panel/book/update/<int:pk>', AdminBookUpdateView.as_view() , name='admin-book-update'),
]



urlpatterns += [
    path('panel/unit/list' , UnitListView.as_view() , name = "admin-unit-list"),
    path('panel/unit/search' , UnitSearchView.as_view() , name = "admin-unit-search"),
    path('panel/unit/create' , UnitCreateView.as_view() , name = "admin-unit-create"),
    path('panel/unit/delete/<int:pk>', UnitDeleteView.as_view() , name='admin-unit-delete'),
    path('panel/unit/update/<int:pk>' , UnitUpdateView.as_view() , name = "admin-unit-create"),

]


urlpatterns += [
    path('panel/vocab/list', VocabTemplateView.as_view(), name="admin-vocab-list"),
    path('panel/vocab/create', VocabCreateView.as_view(), name="admin-vocab-create"),
    # path('panel/vocab/delete', VocabDeleteView.as_view(), name="admin-vocab-destroy"),
    # path('panel/vocab/update', VocabUpdateView.as_view(), name="admin-vocab-create"),
    # path('panel/vocab/search', VocabSearchView.as_view(), name="admin-vocab-search")
]
