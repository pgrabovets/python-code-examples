from urllib import request

url = input('Enter file url: ')
filename = input('Save as name: ')

res = request.urlopen(url)

f = open(filename, 'wb')
f.write(res.read())
f.close()
