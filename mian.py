import requests
from bs4 import BeautifulSoup as Bs

github_user = input('Input Github User: ')
url = 'https://github.com/' + github_user

try:
    r = requests.get(url)
    r.raise_for_status()  # Raise an exception for the HTTP errors
    soup = Bs(r.content, 'html.parser')

    # Find the user's name
    name = soup.find('span', class_='p-name')
    name = name.text if name else 'Not available'
    print('Name: ', name)

    # Number of followers
    followers = soup.find_all('span', class_='Counter')
    followers = followers[1].text if followers else 'Not available'
    print('Followers: ', followers)

    # Find the user's bio
    bio = soup.find('div', class_='p-note')
    bio = bio.text if bio else 'Not available'
    print('Bio: ', bio)

    # Find the user's location
    location = soup.find('span', class_='p-label')
    location = location.text if location else 'Not available'
    print('Location: ', location)

    # Find the user's email
    email = soup.find('a', class_='u-email')
    email = email.text if email else 'Not available'
    print('Email: ', email)

    #  Find the profile image using a more general selector
    profile_image = soup.find('img', class_='avatar')
    profile_image = profile_image['src'] if profile_image else 'Not available'
    print('Profile Image: ', profile_image)

    # Find the number of repositories
    repo = soup.find_all('span', class_='Counter')
    repos = repo[0].text if repo else 'Not available'
    print('Number of repositories: ', repos)

except requests.exceptions.RequestException as e:
    print('Error fetching data:', e)
except Exception as e:
    print('An error occurred:', e)
