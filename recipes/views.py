from django.shortcuts import render, reverse, HttpResponseRedirect

from recipes.models import Author, Recipe
from recipes.forms import AddRecipeForm, AddAuthorForm

# Create your views here.
def index(req):
    recipes = Recipe.objects.all()
    return render(req, 'index.html', {'recipes': recipes})

def author(req, author_id):
    author = Author.objects.get(id=author_id)
    recipes = Recipe.objects.filter(author=author)
    return render(req, 'author.html', {
        'author': author,
        'recipes': recipes,
    })

def authors(req):
    authors = Author.objects.all()
    return render(req, 'authors.html', {
        'authors': authors
    })

def recipe(req, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(req, 'recipe.html', {
        'recipe': recipe
    })

def add_recipe(req):
    html = 'generic_form.html'

    if req.method == "POST":
        form = AddRecipeForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions'],
                author=data['author']
            )
            return HttpResponseRedirect(reverse("homepage"))
        
    form = AddRecipeForm()

    return render(req, html, {'form': form })

def add_author(req):
    html = 'generic_form.html'

    if req.method == "POST":
        form = AddAuthorForm(req.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = AddAuthorForm()

    return render(req, html, {'form': form })