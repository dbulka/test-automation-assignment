import os.path
import json

RESOURCES_DIR = os.path.join(os.path.dirname(__file__), "resources")

site_URL = json.load(open(os.path.join(RESOURCES_DIR, "urls.json")))["site_URL"]
registation_URL = json.load(open(os.path.join(RESOURCES_DIR, "urls.json")))["registation_URL"]
start_main_button = json.load(open(os.path.join(RESOURCES_DIR, "xpaths.json")))["start_main_button"]
second_start_button = json.load(open(os.path.join(RESOURCES_DIR, "xpaths.json")))["start_main_button"]
login_button = json.load(open(os.path.join(RESOURCES_DIR, "xpaths.json")))["login_button"]
name_field = json.load(open(os.path.join(RESOURCES_DIR, "xpaths.json")))["name_field"]
last_name = json.load(open(os.path.join(RESOURCES_DIR, "xpaths.json")))["last_name"]
email = json.load(open(os.path.join(RESOURCES_DIR, "xpaths.json")))["email"]
company = json.load(open(os.path.join(RESOURCES_DIR, "xpaths.json")))["company"]
register = json.load(open(os.path.join(RESOURCES_DIR, "xpaths.json")))["register"]
skip_wizard = json.load(open(os.path.join(RESOURCES_DIR, "xpaths.json")))["skip_wizard"]
settings_drop_down = json.load(open(os.path.join(RESOURCES_DIR, "xpaths.json")))["settings_drop_down"]
setting = json.load(open(os.path.join(RESOURCES_DIR, "xpaths.json")))["settings_drop_down"]
login = json.load(open(os.path.join(RESOURCES_DIR, "xpaths.json")))["login"]
password = json.load(open(os.path.join(RESOURCES_DIR, "xpaths.json")))["password"]
login_page_button = json.load(open(os.path.join(RESOURCES_DIR, "xpaths.json")))["login_page_button"]
user_email = json.load(open(os.path.join(RESOURCES_DIR, "user.json")))["login"]
user_password = json.load(open(os.path.join(RESOURCES_DIR, "user.json")))["password"]