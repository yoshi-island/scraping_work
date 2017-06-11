
import urllib.request as request
import lxml.html
import random

# pickup restaurant
def get_taberogu(url):
    ran_num = random.randint(1,21)

    with request.urlopen(url) as page:
          html = ''
          for line in page.readlines():
              html += line.decode('utf-8')

          doc = lxml.html.fromstring(html)
          elem = doc.xpath('//*[@id="column-main"]/ul/li[%s]/div[2]/div[1]/div/div/div/a' % ran_num)
          #print(elem)

          for el in elem:
              res_name = el.text
              print(el.text)

          doc = lxml.html.fromstring(html)
          elem = doc.xpath('//*[@id="column-main"]/ul/li[%s]/div[2]/div[2]/div[1]/div/div[2]/p[1]/span' % ran_num)
          #print(elem)

          for el in elem:
              res_point = el.text
              print(el.text)

          doc = lxml.html.fromstring(html)
          elem = doc.xpath('//*[@id="column-main"]/ul/li[%s]/div[2]/div[1]/div/div/div/a/@href' % ran_num)
          #print(elem)

          for el in elem:
              res_url = el
              print(el)

          doc = lxml.html.fromstring(html)
          elem = doc.xpath('//*[@id="column-main"]/ul/li[%s]/div[2]/div[1]/div/div/div/span' % ran_num)
          #print(elem)

          for el in elem:
              res_cate = el.text
              print(el.text)

          return res_name, res_point, res_url, res_cate


if __name__ == '__main__':
#def execution():
  # get till page 5 (yaesu)
  ran_num = random.randint(1,5)
  result = get_taberogu("https://tabelog.com/tokyo/C13102/C36139/rstLst/lunch/?sort_mode=1&svd=20170611&svt=1900&svps=%s" % ran_num)
  #return result
  #print(result)
