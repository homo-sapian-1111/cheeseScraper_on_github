import wikipediaapi
from colors import *

wiki_wiki = wikipediaapi.Wikipedia('en')
page_name = "Cheese"


page_py = wiki_wiki.page(page_name)

# print Summary section
if not page_py.exists():
    raise ValueError("Page does not exist")

summary = page_py.summary.split(".")
for index in range(2):
    print(f"{color('[Summary]', fg='green')}  {summary[index]}.")

# new feature: print the second section of the page
sec2 = page_py.sections[2]   
sec2_text = sec2.text.split("\n")
for index in range(3):
    print(color(f'[{sec2.title}]', fg='blue') + f"  {sec2_text[index]}.")

# new feature: print the third section of the page
sec3 = page_py.sections[3]   
sec3_text = sec3.text.split("\n")
for index in range(1):
    print(color(f'[{sec3.title}]', fg='yellow') + f"  {sec3_text[index]}.")

# new feature: print the fourth section of the page
sec4 = page_py.sections[4]   
sec4_text = sec4.text.split("\n")
for index in range(1):
    print(color(f'[{sec4.title}]', fg='red') + f"  {sec4_text[index]}.")        # some changes made by homo-sapian-1111