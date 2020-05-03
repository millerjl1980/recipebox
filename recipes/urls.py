from django.urls import path
from recipes import views


urlpatterns = [
    path('', views.index),
    path('author/<int:author_id>', views.author),
    path('recipe/<int:recipe_id>', views.recipe)
    # path('admin/', admin.site.urls),
]

