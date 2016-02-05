import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
location = lambda *paths: os.path.join(BASE_DIR, *paths)

SONNY_DASHBOARD_TEMPLATE_DIRS = [
    location('sonny_dashboard', 'templates'),
    location('sonny_dashboard', 'templates', 'sonny_dashboard'),
]
