from django.urls import path
from . import views
from . import auth_views

app_name = 'relationship_app'

urlpatterns = [
    # Function-based views
    path('books/', views.book_list, name='book_list'),
    path('books/text/', views.book_list_text, name='book_list_text'),
    
    # Class-based views
    path('libraries/', views.LibraryListView.as_view(), name='library_list'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication URLs
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view, name='logout'),
    path('register/', auth_views.register_view, name='register'),
]

["LogoutView.as_view(template_name=", "LoginView.as_view(template_name="]