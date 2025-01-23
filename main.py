import pytesseract
from gooey import Gooey, GooeyParser
import os
from pdf2image import convert_from_path
import docx
from PIL import Image
import ntpath

path = os.getcwd()
full_path_tessdata = os.path.join(path, r'TESSERACT\tessdata')
full_path_tesseract = os.path.join(path, r'TESSERACT\tesseract.exe')

TESSDATA_PREFIX = full_path_tessdata
pytesseract.pytesseract.tesseract_cmd = full_path_tesseract


def ocr_image(image):
    image = image.convert('1', dither=Image.NONE)
    print('Reading image')
    options = f"-l 'ukr' --psm {args['PSM']}"
    print("OCR'ing")
    text = pytesseract.image_to_string(image, config=options)
    paragraph = mydoc.add_paragraph(text)
    paragraph.alignment = 0  # 0-left, 1-center, 2-right


@Gooey(advanced=True,
       default_size=(400, 500),
       required_cols=1,
       optional_cols=2,
       program_name='OCR',
       program_description='OCR app made by Volynets')
def start_interface():
    global args
    global mydoc

    ap = GooeyParser()
    ap.add_argument('Image', help="image to process", widget='FileChooser')
    ap.add_argument("-p", "--PSM", type=int, default=3,
                    help="Tesseract PSM mode,\n3-auto page segmentation,\n13-single raw line")
    args = vars(ap.parse_args())
    print('Arguments parsed')
    mydoc = docx.Document()
    if '.pdf' in args["Image"]:
        images = convert_from_path(args["Image"], poppler_path=os.path.join(path, r'bin\poppler\Library\bin'))
        for i in range(len(images)):
            images[i].save('page' + str(i) + '.jpg', 'JPEG')
            image = Image.open(rf'page{i}.jpg')
            ocr_image(image)
    else:
        image = Image.open(args["Image"])
        ocr_image(image)

    mydoc.save(os.path.join(path, fr'{ntpath.basename(args["Image"])}.docx'))
    print("Finished, result in 'result.txt'")
    os.startfile(os.path.join(path, fr'{ntpath.basename(args["Image"])}.docx'))


if __name__ == '__main__':
    start_interface()
