import urllib.request as request
import lxml.html
import random

ran_num = random.randint(1,21)


with request.urlopen("https://tabelog.com/tokyo/C13102/C36139/rstLst/lunch/?sort_mode=1&svd=20170611&svt=1900&svps=2&RdoCosTp=1") as page:
      html = ''
      for line in page.readlines():
          html += line.decode('utf-8')
  
      doc = lxml.html.fromstring(html)
      elem = doc.xpath('//*[@id="column-main"]/ul/li[%s]/div[2]/div[1]/div/div/div/a' % ran_num)
      #print(elem)
  
      for el in elem:
          print(el.text)
  
      doc = lxml.html.fromstring(html)
      elem = doc.xpath('//*[@id="column-main"]/ul/li[%s]/div[2]/div[2]/div[1]/div/div[2]/p[1]/span' % ran_num)
      #print(elem)
  
      for el in elem:
          print(el.text)
  
      doc = lxml.html.fromstring(html)
      elem = doc.xpath('//*[@id="column-main"]/ul/li[%s]/div[2]/div[1]/div/div/div/a/@href' % ran_num)
      #print(elem)
  
      for el in elem:
          print(el)
  
      doc = lxml.html.fromstring(html)
      elem = doc.xpath('//*[@id="column-main"]/ul/li[%s]/div[2]/div[1]/div/div/div/span' % ran_num)
      #print(elem)
  
      for el in elem:
          print(el.text)
