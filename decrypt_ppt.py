import sys
import os
import pathlib
import shutil
from zipfile import ZipFile
import re
import time
file1 = sys.argv

def descripta(encr_file):
    new_file_inter = pathlib.Path(encr_file) 
    pastaArquivo = os.path.splitext(new_file_inter)[0]
    new_file_copy = pastaArquivo + "_cp.zip"
    #os.rename(encr_file,new_file)
    if not os.path.exists(pastaArquivo):
        os.mkdir(pastaArquivo)
    shutil.copy(new_file_inter,new_file_copy)
    archive = ZipFile(new_file_copy)
    for file in archive.namelist():
        #if file.startswith('ppt/'):
            archive.extract(file,pastaArquivo)
    archive.close()
    file_to_change = pastaArquivo+"/ppt/presentation.xml"
    file1 = open(file_to_change, "r")
    s =file1.read()
    file1.close()
    new_s = re.sub(r"<p:modifyVerifier[^>]+>", '',s)
    file1 = open(file_to_change, "w+")
    file1.write(new_s)
    file1.close()
    shutil.make_archive(os.path.splitext(pathlib.Path(new_file_copy))[0] , 'zip', pastaArquivo)
    arquivoNovo=pastaArquivo+"_novo"+os.path.splitext(new_file_inter)[1]
    if os.path.exists(arquivoNovo):
        os.remove(arquivoNovo)
    os.rename(new_file_copy,arquivoNovo)
    shutil.rmtree(pastaArquivo)
for file in file1:
    if ".py" == os.path.splitext(file)[1]: continue
    elif len(file1) == 1:print("precisa passar o caminho dos arquivos ou pasta como argumento!")
    if len(file1) == 2 and os.path.isdir(file): 
        listaArquivos =os.listdir(file)
        for arquivo in listaArquivos:
            if os.path.splitext(arquivo)[1] == '.ppsx'or os.path.splitext(arquivo)[1] == '.pptx':
                time.sleep(1)
                descripta(file+"/"+arquivo)
    else: descripta(file)