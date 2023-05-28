import requests
from bs4 import BeautifulSoup

with open('sample.html', 'r') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())

# print(soup.title, type(soup.title))
# print(soup.title.string, type(soup.title.string))

# print(soup.div) # reutrns first div
# print(soup.find_all("div")) # returns all div
# print(soup.find_all("div")[1]) #returns div as specified by the index
# print(type(soup.find_all("div")[1]))

# for link in soup.find_all("a"):
#     print(link)
#     print(link.get("href"))
#     print(link.get_text())
    
# s = soup.find(id = "link3")
# print(s)
# print(s.get("href"))

# print(soup.select("div.italic"))
# print(soup.select("span#italic"))
# print(soup.span.get("class"))

# print(soup.find(id="italic"))
# print(soup.find(class_="italic"))
# print(soup.find_all(class_="italic"))

# for child in soup.find(class_="container").children:
#     print(child)
    
# for parent in soup.find(class_ = "box").parents:
#     print(parent)


# updating existing tag:
# cont = soup.find(class_="container")
# print(cont)
# cont.name = "span"
# cont['class'] = "myclass class2"
# cont.string = "i am a string"
# print(cont)


# adding new tags
# ulTag = soup.new_tag("ul")

# liTag = soup.new_tag("li")
# liTag.string = "Home"
# ulTag.append(liTag)

# liTag = soup.new_tag("li")
# liTag.string = "About"
# ulTag.append(liTag)

# soup.html.body.insert(0, ulTag)
# with open("modified.html", "w") as f:
#     f.write(str(soup))
    
    
# divTag = soup.new_tag("div")
# divTag.string = "Parent"
# divTag["class"]="Parent"

# divTag1 = soup.new_tag("div")
# divTag1.string = "Child"
# divTag1["class"]="Child"

# divTag.append(divTag1)
# soup.html.body.insert(1, divTag)
# with open("modified.html", "w") as f:
#     f.write(str(soup))


# does tags have some specific attribute or not:
# cont = soup.find(class_="container")
# print(cont.has_attr("class"))
# print(cont.has_attr("id"))
# print(cont.has_attr("contenteditable"))

# function to find the tags which has class attribute but no id attribute
def has_class_but_not_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")

def has_content(tag):
    return tag.has_attr("content")

# results = soup.find_all(has_class_but_not_id) 
# checks every tags one by one according to function and stores it in results
results = soup.find_all(has_content)
for result in results:
    print(result, "\n\n")