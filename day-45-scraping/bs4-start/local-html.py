## parsing local html

from bs4 import BeautifulSoup

with open("website.html", "r", encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.prettify())
# print(soup.title.string)

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1",  id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.string)