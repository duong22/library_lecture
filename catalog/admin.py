from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Author, Genre, Book, BookInstance, Language
# admin.site.register(User, UserAdmin)

# user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'myuserpassword')

# # Update fields and then save again
# user.first_name = 'John'
# user.last_name = 'Citizen'
# user.save()

admin.site.register(Genre)
admin.site.register(Language)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date_of_birth', 'date_of_death')

    fieldsets = (
        ('General Information', {
            'fields': ('first_name', 'last_name')
        }),
        ('Dates', {
            'fields': (('date_of_birth', 'date_of_death'))
        }),
    )
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.StackedInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )