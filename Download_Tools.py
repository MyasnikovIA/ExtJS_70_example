import requests as req
import os

# URL корневой путь 
urlSrc = 'https://examples.sencha.com/extjs/7.0.0/' 

# локальный корневой путь к расположению файлов скаченого
dirDst = "F:\\AppServ\\var\\www\\ExtJS\\Tut_003\\"

# url = 'http://127.0.0.1:9090/ExtJS/Tut_003/examples/kitchensink/classic/samples/model/pivot/Sale.js?_dc=1599394480222'
while True:
    url = input("URL= ")
    if len(url) == 0:
        break
    shotPath = url[url.find('examples'):]
    if '?' in url:
        shotPath = shotPath[:shotPath.find('?')]

    FileName = dirDst + shotPath
    dirFileName = FileName[:FileName.rfind("/")].replace('/', '\\')
    urlSrcFile = urlSrc + shotPath

    if not os.path.exists(dirFileName):
        os.makedirs(dirFileName)
    print('FileName', FileName)
    print('urlSrcFile', urlSrcFile)
    print('dirFileName', dirFileName)
    r = req.get(urlSrcFile, allow_redirects=True)
    open(FileName, 'wb').write(r.content)
    print(r.content)
