import os;

def renameFiles():
    #get the files from the folder
        file_addr="/home/saurav/Downloads/prank"
        cd=os.chdir(file_addr)
        file_list=os.listdir(file_addr)
        print(file_list)
        print(os.getcwd())
        
        #for each filename changed the name of the file

        for file_name in file_list:
            print("File name before changes: " +file_name)
            translate_table = str.maketrans("0123456789","          ","0123456789")
            os.rename(file_name, file_name.translate(translate_table))
            print("File name after changes: " +file_name.translate(translate_table))
            print("\n")
renameFiles()
