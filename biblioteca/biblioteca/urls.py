

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend import views

router = DefaultRouter()
router.register(r'autores', views.AutorViewSet)
router.register(r'livros', views.LivroViewSet) 
router.register(r'emprestimos', views.EmprestimoViewSet)
router.register(r'reservas', views.ReservaViewSet)
router.register(r'multas', views.MultaViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'editoras', views.EditoraViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_biblioteca/', include(router.urls)),
]
