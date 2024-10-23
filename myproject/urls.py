from operator import index
from django.contrib import admin
from django.urls import path
from myapp.views import student_view
from myapp.views import delete_student
# from myapp.views import login
from myapp.views import profile
from myapp.views import update_student
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),   
    path('student_view/',student_view,name="student"),
    path('delete_student/<int:id>/', delete_student, name="delete_student"),
    # path('login',login,name='login'),
    path('update_student/<int:id>/', update_student , name='update_student'),
    path('profile/',profile,name='profile'),
    path('home/',home,name="name")

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)