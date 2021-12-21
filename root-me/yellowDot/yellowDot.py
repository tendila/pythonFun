from PIL import Image

# If an image has been scan from a printer (ex: ch18.png)
blue = Image.open("ch18.png").split()[2]
blue.point(lambda x: (256-x)**2).show()
# yellow dot are visible and date & time can be deduct

######## Also try this
# https://github.com/dfd-tud/deda