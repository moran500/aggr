from os import listdir
from os.path import isfile, join
import shutil
from fpdf import FPDF

class AggrTxtFile():

    def __init__(self, folder:str) -> None:
        self.merge_files(self.get_files_names_list(folder), folder)
        self.save_to_pdf(folder+"/"+"final.txt", folder)

    def merge_files(self, files_list:list, folder_path:str) -> None:
        for file in files_list:
            with open(folder_path +"/"+ file,'r') as firstfile, open(folder_path +"/"+"final.txt",'a') as secondfile:
                secondfile.write("\n==================================================================\n")
                secondfile.write("========================="+ file +"=================================\n")
                secondfile.write("==================================================================\n\n")
                for line in firstfile:
                    # append content to second file
                    secondfile.write(line)
                secondfile.write("\n\n")

    def save_to_pdf(self, file_name:str, folder_name:str) -> None:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 12)
        f = open(file_name, "r")
        for x in f:
            pdf.cell(50,5, txt = x, ln = 10, align = 'C') 
        pdf.output(folder_name+"/"+"final.pdf")

    def get_files_names_list(self, folder_path:str) -> list:
        return  [f for f in listdir(folder_path) if isfile(join(folder_path, f))]


if __name__ == "__main__":
    AggrTxtFile("C:/Users/roman/OneDrive/Počítač/toptal_folder/exercises")