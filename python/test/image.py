import requests
def dowloadPic(imageUrl,filePath):
    r = requests.get(imageUrl)
    with open(filePath, "wb") as code:
        code.write(r.content)

url = 'ns2.bdstatic.com/static/fisp_static/common/img/show_top_qrcode/img/1014720j_63c8044.png'
filePath = "1.png"
dowloadPic(url,filePath)