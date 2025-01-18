import os
from django.core.wsgi import get_wsgi_application

print("WSGI module loaded") #Debug statement

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lbhsolutions.settings')

try: 
    application = get_wsgi_application()
    print("WSGI application created") # Debug statement 
except Exception as e: 
    print(f"WSGI application error: {e}") 
    raise e
