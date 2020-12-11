import requests
from bs4 import BeautifulSoup
import csv


def job():
    url = 'https://github.com/trending/python?since=monthly&spoken_language_code=en'

    page = requests.get(url)

    #create beautiful soup object
    soup = BeautifulSoup(page.text, 'html.parser')

    #repo list
    repo_box = soup.find(class_="explore-pjax-container container-lg p-responsive pt-6")

    #find all instances of a class
    repo_list = repo_box.findAll(class_="Box-row")

    file_name = "github_trending.csv"

    f = csv.writer(open(file_name, 'w', newline=''))

    # write a new row as a header
    f.writerow(["title", "stars", "forks", "contributor"])

    top = 0

    for repo in repo_list:

        if (top == 10) :
            break

        full_repo_name = repo.find('h1').find('a').text.split('/')

        owner_name = full_repo_name[0].strip()

        proj_name = full_repo_name[1].strip()

        stars = repo.find(class_="octicon octicon-star").parent.text.strip()

        forks = repo.find(class_="octicon octicon-repo-forked").parent.text.strip()

        f.writerow([proj_name, stars, forks, owner_name])

        top = top + 1


if __name__ == '__main__':
    job()