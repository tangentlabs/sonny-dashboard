import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
location = lambda *paths: os.path.join(BASE_DIR, *paths)

TANGENT_IMPORTER_DASHBOARD_TEMPLATE_DIRS = [
    location('tangent_importer_dashboard', 'templates'),
    location('tangent_importer_dashboard', 'templates', 'tangent_importer_dashboard'),
]
