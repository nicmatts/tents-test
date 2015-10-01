from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^categories/', views.categories, name='categories'),
    # url(r'^book/(\d+)/', views.book_details, name='book_details'),
    # url(r'^add/(\d+)/', views.add_to_cart, name='add_to_cart'),
    # url(r'^remove/(\d+)/', views.remove_from_cart, name='remove_from_cart'),
    # url(r'^cart/', views.cart, name='cart'),
    # url(r'^checkout/', views.checkout, name='checkout'),
    # url(r'^order-error/', views.order_error, name='order_error'),
    # url(r'^complete-order/(\w+)/', views.complete_order, name='complete_order'),
]
