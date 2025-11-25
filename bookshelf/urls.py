from django.contrib import admin
from django.urls import path, include
from library.views import index, book_detail, read_book, add_to_library, my_library
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 1. Admin Panel
    path('admin/', admin.site.urls),
    
    # 2. Login/Logout System
    path('accounts/', include('django.contrib.auth.urls')),
    
    # 3. Homepage
    path('', index, name='home'),
    
    # 4. Book Detail Page
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    
    # 5. The Reader Interface
    path('read/<int:book_id>/', read_book, name='read_book'),

    # 6. The "Add to Library" Toggle
    path('library/add/<int:book_id>/', add_to_library, name='add_to_library'),

    #7. Collection
    path('my-library/', my_library, name='my_library'),
]

# Allow serving PDF files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)