
import requests

def instainfo():
    usr = input("user >> ")
    url = "https://instagram.com/"+usr+"/?__a=1"
    r = requests.get(url)
    id = str(r.json()["graphql"]["user"]["id"])
    Full = str(r.json()["graphql"]["user"]["full_name"])
    bio = str(r.json()["graphql"]["user"]["biography"])
    web = str(r.json()["graphql"]["user"]["external_url"])
    followers = str(r.json()["graphql"]["user"]["edge_followed_by"]["count"])
    follow = str(r.json()["graphql"]["user"]["edge_follow"]["count"])
    email = str(r.json()["graphql"]["user"]["business_email"])
    photo = str(r.json()["graphql"]["user"]["profile_pic_url_hd"])
    verified = str(r.json()["graphql"]["user"]["is_verified"])
    private = str(r.json()["graphql"]["user"]["is_private"])
    print("Username >> ",usr)
    print("user id : ",id)
    print("Full Name :",Full)
    print("Bio :",bio)
    print("Website :",web)
    print("followers :",followers)
    print("following :",follow)
    print("Email :",email)
    print("Profile Photo :",photo)
    print("Verified : ",verified)
    print("Account Private :",private)
    print("===== Coded By 6Virus =====")
