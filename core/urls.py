from django.urls import path
from .views import (
		home_view,
		login_view,
		sign_up_view,
		project_form_view,
		toggle_view,
		logout_view,
        delete_view
)

app_name='core'
urlpatterns=[
	path('', home_view, name='home'),
	path('login/', login_view, name='login'),
	path('signup/', sign_up_view, name='sign_up'),
	path('project/new/', project_form_view, name='project_form'),
	path('project/<int:task_id>/toggle/', toggle_view, name='toggle'),
    path('project/<int:project_id>/edit/', project_form_view, name='edit'),
    path('project/<int:project_id>/delete/', delete_view, name='delete'),
	path('logout/', logout_view, name='logout'),
]
