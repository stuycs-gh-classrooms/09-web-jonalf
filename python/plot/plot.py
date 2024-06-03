#!/usr/bin/python
print('Content-type: text/html\n')

import cgitb #
cgitb.enable() #These 2 lines will allow error messages to appear on a web page in the browser

import matplotlib.pyplot as plt
import io
import base64

HTML_HEADER = """
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8">
<title>Hello</title>
</head>
"""

HTML_FOOTER = """
</body>
</html>
"""


def make_image_element():
    #create buffer to store the graph image
    buffer = io.BytesIO()
    #save graph image to buffer
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    #image_code = buffer.getvalue().decode('utf-8')
    image_code = base64.b64encode(buffer.read()).decode('utf-8')
    src = "data:image/png;base64,"
    src+= image_code
    html = '<img src="' + src
    html+= '">'
    return html


def make_graph():
    rent = open('manhattan_rent.csv').read()

    rents = []
    size = []
    rooms = []
    for line in rent.split()[1:]:
        data = line.split(',')
        rents.append(int(data[0]))
        size.append(int(data[1]))
        rooms.append((float(data[2])))

    plt.scatter(rents, size)

#generate the graph
make_graph()
#create the image element
img = make_image_element()

html = HTML_HEADER
html+= """
<body>
<h1>Graph Demo</h1>
<p>
If this works correctly, we should see a scatterplot generated in matplotlib by this python file.
"""
html+= img
html+= '</p>'
html+= HTML_FOOTER

print(html)
