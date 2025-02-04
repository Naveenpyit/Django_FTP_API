from django.urls import path
from . import views

urlpatterns=[
    path('fetchph-buss/<str:table_name>/',views.get_ph_business,name='ph_business'),

    path('post-grp-prod-det/',views.post_group_product_detail,name='group_product_detail'),
]