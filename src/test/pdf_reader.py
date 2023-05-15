from urllib.request import urlopen 
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from io import StringIO
from io import open 



def readPDF(pdfFile): 
    rsrcmgr = PDFResourceManager() 
    retstr = StringIO() 
    laparams = LAParams() 
    device = TextConverter(rsrcmgr, retstr, laparams = laparams) 
    
    fp = open(pdfFile) 
    parser = PDFParser(fp) 
    doc = PDFDocumnet() 


    PDFPage.get_pages(rsrcmgr, device, pdfFile) 
    device.close() 

    content = retstr.getValue() 
    retstr.close() 

    return content 



if __name__ == "__main__" : 
    pdfFile = urlopen("https://arxiv.org/pdf/2305.00554.pdf") 
    outputString = readPDF(pdfFile) 
    print(outputString) 
    pdfFile.close() 
