"""lavenue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import include, path

from organisations.views import AgendaView

urlpatterns = [
	path('admin/', admin.site.urls),
	path('__debug__/', include(debug_toolbar.urls)),
    path('<slug:organisation_slug>/', include([
        path('<slug:meeting_slug>/', include([
            path('agenda/', AgendaView.as_view(), name='meeting-agenda'),
        ])),
    ])),
]
