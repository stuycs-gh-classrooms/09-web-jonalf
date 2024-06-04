#!/usr/bin/python
print('Content-type: text/html\n')

import cgitb #
cgitb.enable() #These 2 lines will allow error messages to appear on a web page in the browser

import matplotlib.pyplot as plt
import io
import base64
import cgi


# As long as you have already created a
# plot (eg. used plt.scatter or plt.plot
# This function will save the current plot
# as a data string that can then be put
# directly into the src attribute of an
# <img> HTML element.
# This function returns the full code for the
# <img> element.
def make_image_element():
    #create buffer to store the graph image
    buffer = io.BytesIO()
    #save graph image to buffer
    plt.savefig(buffer, format='png')
    #reset buffer to the start of the image data
    buffer.seek(0)
    #encode the image data in buffer to base64, then
    #translate that to utf-8
    image_code = base64.b64encode(buffer.read()).decode('utf-8')
    src = "data:image/png;base64,"
    src+= image_code
    html = '<img src="' + src
    html+= '">'
    return html

def get_data():
    rent = open('manhattan_rent.csv').read()
    
    data = {'rents': [],
            'size': [],
            'rooms': []}
    for line in rent.split()[1:]:
        row = line.split(',')
        data['rents'].append(int(row[0]))
        data['size'].append(int(row[1]))
        data['rooms'].append((float(row[2])))
    return data

def make_html(title, body):
    html = """
    <!DOCTYPE html>
    <html lang="en">

    <head>
    <meta charset="utf-8">
    """
    html+= '<title>' + title + '</title></head>'
    html+= '<body>' + body + '</body>'
    html+= '</body></html>'
    return html

def make_body(img, form):
    body = """
    <h1>Graph Demo</h1>
    <p>
    If this works correctly, we should see a scatterplot generated in matplotlib by this python file.
    """
    body+= img + '</p>'
    body+= '<p>Try it again!<br>'
    body+= form + '</p>'
    return body

def make_form(select_options):
    html = """
    <form action="hello.py" method="GET">
    Type of graph:
    """
    select = """
    <select name="graph_type">
    """
    for option in select_options:
        o = '<option value="' + option + '">'
        o+= option + '</option>\n'
        select+= o
    select+= '</select>\n'
    
    html+= select
    html+= '<input type="submit" value="Submit!">'
    return html

#get form input
form_input = cgi.FieldStorage()

#get the data
data = get_data()
#make the graph
plt.ylabel('rent price $')
plt.xlabel('apartment size sq ft')
if ('graph_type' in form_input):
    plt.scatter(data['size'], data['rents'])
else:
    plt.bar(data['size'], data['rents'])
#create the image element
img = make_image_element()
form = make_form(['scatter', 'bar'])
body = make_body(img, form)
html = make_html('Graph Demo', body)
print(html)
