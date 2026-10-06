from django.contrib import admin
from .models import MealPlan, Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
  list_display = ('name', 'category', 'cooking_time', 'servings')
  search_fields = ('name', 'ingredients')
  list_filter = ('category',)


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
  list_display = ('date', 'meal_type', 'recipe')
  list_filter = ('meal_type', 'date')
  ordering = ('date',)
