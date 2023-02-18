import os
import glob
import time

print("\nEjemplo: c:/Users/username/Download/")
opath = input("PATH: ")
dirs = [['Videos',['mp4', 'mov','mkv']],['Audios',['mp3','wav']],['Images',['jpg','png','jpeg','tif','gif']],['Text',['txt']],['Documents',['pdf','doc','docx']],['Apps',['exe','msi']],['Comprimidos',['zip','rar','rarx','7zip']]]

def getFiles(path, extension):
    fullpath = path+'*.'+extension
    files = glob.glob(fullpath)
    return files

def organizeFiles():
    print("Organizing files...")
    time.sleep(1)
    for d in dirs:
        #clasificate file for each directory
        for ex in d[1]:
            files = getFiles(opath,ex)
            if len(files) > 0:
                #create a folder to hold the files
                if not os.path.exists(opath+d[0]):
                    os.mkdir(opath+d[0])
                # move the files to the new folder
                for file in files:
                    os.rename(file, opath+d[0]+'/' + os.path.basename(file))
    time.sleep(1)
    print("DONE!!")

def main():
    print("loging...")
    time.sleep(1)
    if os.path.exists(opath):
        organizeFiles()
    else:
        print("La ruta no Existe.")
        exit(0)

if __name__ == "__main__":
    main()
