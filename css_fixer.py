import re

file_path = "single.html"
replacement_start = "{{ url_for('static',filename='"
replacement_end = "') }}"

list_of_exceptions = [
    "http://w3layouts.com/",
    ]


with open(file_path, "r") as file:
    html = file.readlines()

lines_to_alter_href = []
lines to alter_src = []

for index in range(len(html)):
    line = html[index]
    if "href" in line:
        if 'href="#"' not in line:
            lines_to_alter.append((line, index))

lines_to_alter = [x for x in lines_to_alter if not [y for y in list_of_exceptions if y in x[0]]]

altered_lines = []

for line in lines_to_alter:
    match = re.findall('href=".*?"', line[0])
    if not match:
        match = re.findall("href='.*?'", line[0])
    if not match:
        raise ValueError("Regular Expression can't match pattern")
    match = match[0][6:-1]

    print(match)

# for line in lines_to_alter:
#     print(line)
