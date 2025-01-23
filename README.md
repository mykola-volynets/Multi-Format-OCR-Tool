# Multi-Format-OCR-Tool
Important: To launch this app, you need to download Google's Tesseract and place its folder right next to this script (folder should be named TESSERACT) AND download poppler, to work with PDFs. You can download tesseract here: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe OR you can download all the files and virtual environment from here: https://drive.google.com/drive/folders/1TxeEEYcwwRR-ZtDroUUie-_ylkRX97rc?usp=sharing 

This application allows you to extract text in Ukrainian from picture (PNG, JPG, PDF, GIF, etc.) using a simple and easy-to-understand interface. The app utilizes Google's Tesseract tool as the main base for the OCR process but also allows for extensive customization of the output file with very little change to the code (e.g. text alignment, line density).

This algorithm is also easily adjustable for different languages. How to change language:

Find and download the needed language from here: https://github.com/tesseract-ocr/tessdata
Place it in the TESSERACT/tessdata
In line 20 of this script, change "ukr" to the language of your choice. Done!

This is what the interface looks like:

![image](https://github.com/user-attachments/assets/9bc55999-75bc-4e20-9c19-36e711ff37af)

There is a test.gif file on Google Drive. Here it's content:

![image](https://github.com/user-attachments/assets/25e173b4-1867-47e7-96bf-7edb985cec8c)

And here is the output after running it through the script (with default PSM):

![image](https://github.com/user-attachments/assets/a193eda3-b287-4dea-b25f-b7dfdd9b1633)
