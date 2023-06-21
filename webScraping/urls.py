from django.urls import path,include
from . import views as d
#from . import views


urlpatterns = [
    path('',d.dse),
    path('scrap-data',d.dseScraping),
    path('stor-data',d.storDataPostgres),
    path('dse-other-info',d.dse_other_info),
    path('streamlit-dashboard/', d.streamlit_dashboard, name='streamlit_dashboard'),
    path('api/', include('Api.urls')),
]