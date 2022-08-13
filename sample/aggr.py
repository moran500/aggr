from os import listdir
from os.path import isfile, join
import shutil
class AggrTxtFile():

    def __init__(self, folder:str) -> None:
        self.merge_files(self.get_files_names_list(folder), folder)

    def merge_files(self, files_list:list, folder_path:str) -> None:
        for file in files_list:
            with open(folder_path +"/"+ file,'r') as firstfile, open(folder_path +"/"+"final.txt",'a') as secondfile:
                secondfile.write("===============TEST=================================")
                for line in firstfile:
                    # append content to second file
                    secondfile.write(line)

    def get_files_names_list(self, folder_path:str) -> list:
        return  [f for f in listdir(folder_path) if isfile(join(folder_path, f))]


if __name__ == "__main__":
    AggrTxtFile("C:/Users/roman/OneDrive/Počítač/toptal_folder/exercises")