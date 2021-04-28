from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view({'get': 'list'})),
    path('sections/', views.sectionsList.as_view()),
    path('sections/create/', views.sectionsCreate.as_view()),
    path('items/', views.itemsList.as_view()),
    path('items/create/', views.itemsCreate.as_view()),
    path('modifiers/', views.modifiersList.as_view()),
    path('modifiers/create/', views.modifiersCreate.as_view()),
]