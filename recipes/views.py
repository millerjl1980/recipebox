from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404

from django.contrib.auth import login, logout, authenticate

from recipes.models import Author, Recipe
from recipes.forms import LoginForm, EditRecipeForm

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

def recipe_edit(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    if request.method == "POST":
        form = EditRecipeForm(request.POST, instance=recipe)
        form.save()
        return HttpResponseRedirect(reverse('recipe', args=(id,)))

    form = EditRecipeForm(instance=recipe)
    return render(request, 'generic_form.html', {'form': form})


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )