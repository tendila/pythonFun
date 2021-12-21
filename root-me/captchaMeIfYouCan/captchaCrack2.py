from PIL import Image
import requests, re, base64, os, subprocess

s = requests.Session()
base = "http://challenge01.root-me.org//programmation/ch8/"
s.cookies.update({
    "spip_session": "622538_4b3b6c9d0505f9f661303e38093fe761",
    "PHPSESSID": "e86b55c1b5925bc2cd92f4a36c736483"
})
d = s.get(base).text

# print(d)
# for cookie in s.cookies:
#     print(cookie.name, cookie.value)

im = re.match(r".*base64,(.*?)\".*", d)
im = im.group(1)
with open("im.png", "wb") as f:
    f.write(base64.b64decode(im))

img = Image.open("im.png")  # delete all the noise ;)
width, height = img.size
pix = img.load()
for i in range(width):
    for j in range(height):
        if pix[i, j] == (0, 0, 0):
            pix[i, j] = (255, 255, 255)
img.save("im.png")

# Now we have a clear image so gocr will always return a 70% valid answear
r = str(subprocess.check_output(
    "gocr im.png -C 'a-z0-9A-Z' -u ''", shell=True).decode()).strip()
d = s.post(base, data={"cametu": r})
print(d.text)

# Delete '.png' file from '.'
for file in os.listdir('.'):
    if file.endswith('.png'):
        os.remove(file)
