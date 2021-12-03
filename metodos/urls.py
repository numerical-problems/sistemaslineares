# Use include() to add paths from the catalog application
from django.urls import path
from metodos import views


urlpatterns = [
    path('', views.index, name='index'),
    path('gauss', views.gauss, name='gauss'),
    path('jordan', views.jordan, name='jordan'),
    path('jacobi', views.jacobi, name='jacobi'),
    path('gaussseidel', views.gaussseidel, name='gaussseidel'),
    path('resultgauss', views.resultgauss, name='resultgauss'),
    path('resultjordan', views.resultjordan, name='resultjordan'),
    path('resultjacobi', views.resultjacobi, name='resultjacobi'),
    path('resultgaussseidel', views.resultgaussseidel, name='resultgaussseidel'),
]