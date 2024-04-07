import requests
from bs4 import BeautifulSoup as Bs

github_user = input('Input Github User: ')
url = 'https://github.com/' + github_user

try:
    r = requests.get(url)
    r.raise_for_status()  # Raise an exception for the HTTP errors
    soup = Bs(r.content, 'html.parser')

    # Generate the user's GitHub profile link
    profile_link = url
    print('Profile Link: ', profile_link)

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

    # Find the social media links based on the user's profile name
    social_links = ['https://twitter.com/' + github_user, 'https://www.linkedin.com/in/' + github_user,
                    'https://www.facebook.com/' + github_user, 'https://www.instagram.com/' + github_user]
    print('Social Links: ', social_links)

    #  Find the user's website
    website = soup.find('a', class_='u-url')
    website = website['href'] if website else 'Not available'
    print('Website: ', website)

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

    #  Find social media links
    social_links = soup.find_all('a', class_='u-url')
    social_links = [link['href'] for link in social_links] if social_links else 'Not available'
    print('Social Links: ', social_links)

    # Find the number of repositories
    repo = soup.find_all('span', class_='Counter')
    repos = repo[0].text if repo else 'Not available'
    print('Number of repositories: ', repos)

    # Find the number of stars
    stars = soup.find_all('span', class_='Counter')
    stars = stars[2].text if stars else 'Not available'
    print('Number of stars: ', stars)


except requests.exceptions.RequestException as e:
    print('Error fetching data:', e)
except Exception as e:
    print('An error occurred:', e)
