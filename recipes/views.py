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
    is_fav = False
    recipe = Recipe.objects.get(id=recipe_id)
    if recipe.favorite.filter(id=req.user.id).exists():
        is_fav = True
    return render(req, 'recipe.html', {
        'recipe': recipe,
        'is_fav': is_fav,
    })

def recipe_edit(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    if request.method == "POST":
        form = EditRecipeForm(request.POST, instance=recipe)
        form.save()
        return HttpResponseRedirect(reverse('recipe', args=(id,)))

    form = EditRecipeForm(instance=recipe)
    return render(request, 'generic_form.html', {'form': form})


def recipe_fav(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    if recipe.favorite.filter(id=request.user.id).exists():
        recipe.favorite.remove(request.user)
    else:
        recipe.favorite.add(request.user)
    return HttpResponseRedirect(reverse('recipe', args=(id,)))

def favorite_recipe_list(request):
    user = request.user
    fav_recipies = user.favorite.all()
    return render(request, 'favs_list.html', {'fav_recipies': fav_recipies})

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