# Goal: Degree name, degree type, department, faculty, link

def extract_courses_by_year(year):
    main_url = 'https://www.ucl.ac.uk/prospective-students/undergraduate/degrees?query=&year=' + str(year)
    return main_url

# extract_courses_by_year(2026)

import requests
from bs4 import BeautifulSoup

url = extract_courses_by_year(2026)

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

# # Print the Pretty HTML for structure
# print(soup.prettify())

# want all result-item clearfix 
# want from these, href and the name/label of href
# and the class 'search-results__dept'


# 
import requests
from bs4 import BeautifulSoup

url = "https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all result-item blocks
blocks = soup.find_all('div', class_='result-item')

results = []

for block in blocks:
    # Get the <a> tag (href and label)
    a_tag = block.find('a')
    href = a_tag['href'] if a_tag and 'href' in a_tag.attrs else None
    label = a_tag.text.strip() if a_tag else None

    # Get department and description
    spans = block.find_all('span', class_='search-results__dept')
    department = spans[0].text.strip() if len(spans) > 0 else None
    description = spans[1].text.strip() if len(spans) > 1 else None

    results.append({
        'label': label,
        'href': href,
        'department': department,
        'description': description
    })

# # Print results
# for r in results:
#     print(f"Label: {r['label']}")
#     print(f"Href: {r['href']}")
#     print(f"Department: {r['department']}")
#     print(f"Description: {r['description']}")
#     print('-' * 80)
print(results[0])

###
degree_types = []

# Find all input elements with class 'facet-degree-level'
inputs = soup.find_all('input', class_='facet-degree-level')

for input_tag in inputs:
    input_id = input_tag.get('id')
    if not input_id:
        continue
    # Find the label with matching 'for' attribute
    label = soup.find('label', attrs={'for': input_id})
    if label:
        # Extract label text without the count in parentheses
        full_text = label.get_text(strip=True)
        degree_type = full_text.split('(')[0].strip()
        degree_types.append(degree_type)

# Remove duplicates and sort
degree_types = sorted(set(degree_types))

# for degree in degree_types:
#     print(degree)

# print(degree_types)

