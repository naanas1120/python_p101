import os
from threading import local
import dropbox
from dropbox.files import WriteMode

class TransferData:
   def  __init__(self, access_token):
     self.access_token=access_token

   def uploadFile(self,file_from,file_to):
       dbx=dropbox.Dropbox(self.access_token)

       for root,dirs,files, in os.walk(file_from):
            for fileman in files:
                local_path = os.path.join(root,fileman)
                relative_path=os.path.realpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)

                with open (local_path,'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token="sl.BB27vOMHiYr4xZhtGEXG5qgEe4Mj0gba9s5MFV_jw9HLlO0SIa7c48bouluHW_g41XABmPgNHm-8oNn6-ecGAN7xerDzA-62qxdvxrzyjTQaCeetVhMxk5f_ax7PEofEih00M8M"
    
    transferData_1=TransferData(access_token)
    
    file_from=str(input("enter the file path to be backed up: "))
    file_to=input("enter the destination folder in the dropbox: ")

    transferData_1.uploadFile(file_from,file_to)
    print("file has been backed up")

main()
