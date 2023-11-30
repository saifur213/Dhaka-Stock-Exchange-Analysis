from django.urls import path,include
from . import views as l
#from . import views


urlpatterns = [
    path('',l.stream),
    path('youtube-live-stream/',l.startYoutubeStream),
    path('facebook-live-stream/',l.startFacebookStream),
    # path('stop-facebook-live-stream/',l.stopFacebookStream),
    # path('go-live-stream/',l.live_stream),
    
    # path('stor-data',d.storDataPostgres),
    # path('dse-other-info',d.dse_other_info),
    # path('streamlit-dashboard/', d.streamlit_dashboard, name='streamlit_dashboard'),
    # path('api/', include('Api.urls')),
]