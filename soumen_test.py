import urllib.request as request
import lxml.html

#with request.urlopen("http://tsumugiya.net/ec/4282.html") as page:
with request.urlopen("http://tsumugiya.net/ec/7131.html") as page:
    html = ''
    for line in page.readlines():
        html += line.decode('utf-8')

    doc = lxml.html.fromstring(html)
    elem = doc.xpath('//div[@class="item-desc"]/p[@class="item-name"]')
    print(elem)

    for el in elem:
        print(el.text)

    elem2 = doc.xpath('//span[@class="regular-price"]/span[@class="price"]')
    print(elem2)

    for el in elem2:
        print(el.text)
