from bs4 import BeautifulSoup
from src.lib.request import *

def search(email):
    base_url = "https://m.facebook.com/"
    page = BeautifulSoup(request("GET", base_url + "login/identify").text, "html.parser")
    form_action = base_url + page.find("form", {"id": "identify_yourself_flow"})["action"]
    lsd = page.find("input", {"name": "lsd"})["value"]
    jazoest = page.find("input", {"name": "jazoest"})["value"]
    search_post(form_action, email, lsd, jazoest)

def search_post(form_action, email, lsd, jazoest):
    email = email + "@yahoo.com"
    page = BeautifulSoup(request("POST", form_action, data={"lsd": lsd, "jazoest": jazoest, "email": email, "did_submit": "Cari"}).text, "html.parser")
    title = page.find("title").text
    if (title == "Temukan Akun Anda"):
        print(f"\n[ * ] Email : {email}\n[ * ] Status : {title} [ NOT FOUND ]")
    else:
        print(f"\n[ * ] Email : {email}\n[ * ] Status : {title} [ FOUND ]")
