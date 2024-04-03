import requests
from bs4 import BeautifulSoup as Bs

github_user = input('Input Github User: ')
url = 'https://github.com/' + github_user

try:
    r = requests.get(url)
    r.raise_for_status()  # Raise an exception for the HTTP errors
    soup = Bs(r.content, 'html.parser')

    #  Find the profile image using a more general selector
    profile_image = soup.find('img', class_='avatar')['src']

    print('Profile image URL: ', profile_image)

except requests.exceptions.RequestException as e:
    print('Error fetching data:', e)
except Exception as e:
    print('An error occurred:', e)
