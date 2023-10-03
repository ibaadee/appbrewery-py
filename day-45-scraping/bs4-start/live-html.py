from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

#scrap first and single item in the site
# article_tag = soup.find(name="a", rel="noreferrer")
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").getText()

#scrap multiple items
titles = []
links = []

articles = soup.find_all(class_="titleline")

for article in articles:  
    title = article.getText()
    link = article.find(name="a").get("href")
    titles.append(title)
    links.append(link)

upvotes = [score.getText().split(" ")[0] for score in soup.find_all(name="span", class_="score")]

# print(titles)
# print(links)
# print(upvotes)
# print(soup.find_all(name="a", rel="noreferrer"))

# print the highest upvote article in the list
# highest_upvote = 0
# index = 0
# for upvote in enumerate(upvotes):
#     if int(upvote[1]) > highest_upvote:
#         highest_upvote = int(upvote[1])
#         index = int(upvote[0])

largest_number = max(upvotes)
largest_index = int(upvotes.index(largest_number))

highest_upvote_article = [titles[28], links[28], upvotes[28]]
print(highest_upvote_article)