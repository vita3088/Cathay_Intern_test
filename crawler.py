import urllib.request as req
import bs4

print("iThome News Link Example: https://www.ithome.com.tw/news/152373")
url = input("Please input a iThome news link: ") # ex: https://www.ithome.com.tw/news/152373


# Creeate Request Object & Give fake User-Agent
request = req.Request(url, headers = {
  "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36"
})

# Get Response within utf-8 encoded
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

# Parse HTML structure within bs4
root = bs4.BeautifulSoup(data, "html.parser")

# Get header and summary in root level
header = root.find("h1", "page-header");
summary = root.find("div", "content-summary");

print(header.text)
print(summary.text)

# Get contents in text and filter link
even = root.find("div", "contents-wrap");
content = even.find("div", "content");
hidden = content.find("div", "field field-name-body field-type-text-with-summary field-label-hidden");
items = hidden.find("div", "field-items");
even = items.find("div", "field-item even");
for item in even.contents:
      hasLink = item.find("a")
      if hasLink is None:
        print(item.get_text())

# Write the result to txt
with open(header.get_text() + ".txt","w",encoding="utf-8") as file:
    file.write("Title: " + header.get_text() + "\n")
    file.write("Summary: " + summary.get_text() + "\n")
    file.write("Content: ")
    for item in even.contents:
      hasLink = item.find("a")
      if hasLink is None:
        file.write(item.get_text())


# References：https://stackoverflow.com/questions/2081586/web-scraping-with-python
