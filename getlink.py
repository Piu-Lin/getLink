import requests
from lxml import etree


def getLink(url):
    link = {}
    url = url.strip()
    req = requests.get(
        url=url)
    html = etree.HTML(req.text)
    alinks = html.xpath('//a')
    for i in range(len(alinks)):
        text = alinks[i].text
        text = str(text)
        text = text.strip()
        if len(text) == 0 or text == "None":
            continue
        att = alinks[i].attrib
        if att['href'] == url or att['href'] == "/" or att['href'][0:10] == 'javascript':
            continue
        if att['href'][0] == '/':
            href = ''.join([url, att['href']])
        else:
            href = att['href']
        link[text] = href
    return link


if __name__ == "__main__":
    url = 'http://hznu.fanya.chaoxing.com/portal'
    link = getLink(url)
    print(link)
