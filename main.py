import easyocr
import pyperclip
from PIL import ImageGrab, Image

if __name__ == '__main__':
    print('Loading models...')
    reader = easyocr.Reader(['ch_sim', 'en'], gpu=True)
    while True:
        input('\nCopy image to your clipboard and press any key to continue: ')
        img = ImageGrab.grabclipboard()
        if not isinstance(img, Image.Image):
            print('This is not a valid image, try again.')
            continue

        img.save('temp.png')
        res = ''.join(reader.readtext('temp.png', detail=0))
        pyperclip.copy(res)
        print(res)

