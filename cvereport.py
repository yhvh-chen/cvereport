# Author: James Chen
# Last edit: 2021/11/14

import requests
from pyecharts.components import Table
from pyecharts.charts import Page
from pyecharts.options import ComponentTitleOpts
from datetime import date
import yaml

miniscore = '4'
items = '10'
x = date.today()
y = x.strftime("%m-%d-%Y")
headers = ['CVE ID', 'Publish', 'CVSS Score', 'Summary', 'details']
with open('id.yaml', encoding='utf-8') as file:
    dict = yaml.load(file, Loader=yaml.FullLoader)

def check_input(input):
    try:
        val = int(input)
    except ValueError:
        print("Please input a valid number.")

def Getinfo(vendor_id, product_id):
    rows = []
    api = 'http://www.cvedetails.com/json-feed.php?cvssscoremin='+miniscore+'&numrows='+items+'&vendor_id='+vendor_id+'&product_id='+product_id
    r = requests.get(api)
    data = r.json()
    for i in data:

        id = i['cve_id']
        publish = i['publish_date']
        cwe = i['cwe_id']
        cvss = i['cvss_score']
        details = i['url']
        summary = i['summary']
        rows.append([id, publish, float(cvss), summary, details])
    return rows

def Pltable(title, rows):
    table = Table(page_title="CVE Report")
    Table()
    table.add(headers, rows)
    table.set_global_opts(title_opts=ComponentTitleOpts(title=title))
    # table.render(fname)
    return table

def Aio():
    page = Page(page_title="CVE Report")
    fname = 'report/All_' + y + '.html'
    for i, k in dict.items():
        vendor_id = str(dict[i]['vid'])
        product_id = str(dict[i]['pid'])
        data = Getinfo(vendor_id, product_id)
        table = Pltable(i, data)
        page.add(table)
    page.render(fname)
    Opt_html(fname)

def Single(product):
    fname = f'report/{product}_{y}.html'
    vendor_id = str(dict[product]['vid'])
    product_id = str(dict[product]['pid'])
    data = Getinfo(vendor_id, product_id)
    table = Pltable(product, data)
    table.render(fname)
    Opt_html(fname)

def Opt_html(fname):
    with open(fname, 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('white-space: nowrap;', 'table-layout: fixed; ')

    with open(fname, 'w') as file:
      file.write(filedata)

    print(f'\n{fname} generate success!')

def Menue():
    print('Products List\n')
    print('0 rener_all')
    dict_list = list(dict)
    for (li, i) in enumerate(dict_list, start=1):
        print(li, i)

    choose = int(input('\nInput a number: '))
    check_input(choose)
    print('\n Report Generating...')
    if choose == 0:
        Aio()
    else:
        Single(dict_list[choose-1])
Menue()