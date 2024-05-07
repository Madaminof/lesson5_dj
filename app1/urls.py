from django.urls import path
from .views import Get_Books,Get_Author,Get_Books_Category,Get_Review, add_products, update_products,delete_product,detail


app_name = 'products'
urlpatterns = [
    path('', Get_Books_Category, name='Get_Books_Category'),
    path('Get_Books/<int:pk>/',Get_Books , name='Get_Books'),
    path('Get_Auther/<int:pk>/', Get_Author, name='Get_Author'),
    path('Get_Review/<int:pk>',Get_Review, name='Get_Review'),
    path('product<int:pk>', detail, name='detail'),
    path('add_products', add_products, name='add_products'),
    path('update_products/<int:pk>', update_products, name='update_products'),
    path('delete/<int:pk>', delete_product, name='delete_product'),
]
