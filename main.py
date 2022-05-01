import requests
from bs4 import BeautifulSoup

def get_url(url):
    response = requests.get(url)
    return response.text

def get_titles(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find_all('h2', class_="by")
    return title

def get_alt_title(html):
    soup = BeautifulSoup(html, 'lxml')
    alt_title = soup.find_all('h3', class_="ho")
    return alt_title

def split_title(titles):
    title_list = []
    for title in titles:
        for a in title:
            title_list.append(a)
    return title_list

def write_txt(title_list, alt_title_list):
    sayac = 0
    title_len = len(title_list)
    f = open("titles_subject.txt","w")
    f.write("Medium's Last Posted\n")
    while sayac < title_len:
        if sayac < 6:
            f.write(title_list[sayac] + "\n")
            sayac = int(sayac) + int(1)
        else:
            if(sayac % 2 == 0):
                f.write(title_list[sayac] + "\n")
                sayac = int(sayac) + int(1)
            else:
                f.write(" >>" + alt_title_list[sayac - 7] + "\n")
                sayac = int(sayac) + int(1)

    f.close

def main():
    url = "https://medium.com/"
    titles = get_titles(get_url(url))
    alt_titles = get_alt_title(get_url(url))

    title_list = split_title(titles)

    alt_title_list = split_title(alt_titles)

    write_txt(title_list, alt_title_list)

if __name__ == "__main__":
    main()