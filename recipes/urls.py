from django.urls import path
from recipes import views


urlpatterns = [
    path('', views.index, name='home'),
    path('author/<int:author_id>', views.author),
    path('recipe/<int:recipe_id>', views.recipe, name='recipe'),
    path('recipe_edit/<int:id>', views.recipe_edit, name='recipe_edit'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    # path('admin/', admin.site.urls),
]

