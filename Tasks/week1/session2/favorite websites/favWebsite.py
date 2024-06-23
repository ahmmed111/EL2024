import requests
import urllib
import webbrowser

Links_ls={"Facebook"  :"https://www.facebook.com/",
          "Linkedin"  :"https://www.linkedin.com/", 
          "Github"    :"https://github.com/" ,
          "GoogleMaps":"https://maps.google.com/"}

favorite_sites = {
    'Google': 'https://www.google.com',
    'Reddit': 'https://www.reddit.com',
    'GitHub': 'https://www.github.com',
    'YouTube': 'https://www.youtube.com'
}

def fav_website(url):
        webbrowser.register('firefox', None, webbrowser.BackgroundBrowser('/usr/bin/firefox'))
        webbrowser.get('firefox').open(url)

def print_menu():
    print("Favorite Websites Menu:")
    for i , website in enumerate(Links_ls,start=1):
        print(f"{i}. {website}")
    
    while True:
        choice = int(input("Enter the number of the site you want to visit (or 0 to exit): "))
        if choice == 0:
                break
        elif 1<= choice <= len(Links_ls):
             site=list(Links_ls.keys())[choice-1]
             url=Links_ls[site]
             fav_website(url)
        else:
            print("Invalid choice. Please enter a number from the menu.")    

print_menu()