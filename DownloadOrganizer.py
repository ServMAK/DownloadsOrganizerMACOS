import os
import shutil

#KONFIGURACJA 
DOWNLOAD_PATH = os.path.expanduser("~/Downloads")

#SLOWNIK 
FOLDER_MAP = {
     "Obrazy": ["jpg", "jpeg", "png", "gif", "bmp"],
     "Dokumenty": ["pdf", "docx", "txt", "xlsx"],
     "Muzyka": ["mp3", "wav", "flac"],
     "Wideo": ["mp4", "avi", "mkv"],
     "Instalatory": ["exe", "msi", "dmg"],
     "Inne": []
}

#KONWERTOWANIE ROZMIARU PLIKU
def sizer(bajty):
    if bajty < 1024**3:
        return f"{round(bajty / 1024**2, 2)} MB"
    else:
        return f"{round(bajty / 1024**3, 2)} GB"


#USTAWIENIE SCIEKI DOCELWEJ
def ustaw_target_path():
   print("KONFIGURACJA ŚCIEŻKI DOCELWEJ:")
   print("-" * 40)
   print("1. Dysk zewnętrzny (wpisz nazwę np. ADATA)")
   print("2. Inny folder (wpisz pełną ścieżkę)")
   print("3. Naciśnij Enter i Zostaw domyślnie (Downloads/Organized)")

   wybor = input("\n Wybierz opcję : ")

   if wybor == "1":
       nazwa = input("Podaj nazwę dysku zewnętrznego: ")
       return f"/Volumes/{nazwa}/Organized"
   elif wybor == "2":
       sciezka = input("Podaj pełną ścieżkę docelową: ") 
       return sciezka
   
   return os.path.expanduser("~/Downloads/Organized")
       

#FUNKCJA GLOWNA 

def organize():

    TARGET_PATH = ustaw_target_path()


    licznik = 0 
    suma_bajty = 0   

    print(f"\n ORGANIZOWANIE PLIKÓW Z: {DOWNLOAD_PATH}")

    for filename in os.listdir(DOWNLOAD_PATH):
        filepath = os.path.join(DOWNLOAD_PATH, filename)   

        if os.path.isfile(filepath):
            extension = os.path.splitext(filename)[1].lower()[1:]

            for folder_name, extensions in FOLDER_MAP.items():
                if extension in extensions:
                   rozmiar_pliku = os.path.getsize(filepath)

                   target_folder = os.path.join(TARGET_PATH, folder_name)

                   if not os.path.exists(target_folder):
                          os.makedirs(target_folder)

               # try:      
                          shutil.move(filepath, os.path.join(target_folder, filename))
                          licznik += 1
                          suma_bajty += rozmiar_pliku
                        
                          print("\n" + "-" * 40)
                          print(f"PLIK: {filename}")
                          print(f"TYP: {extension.upper()}")
                          print(f"CEL: {target_folder} ")
                          print("-" * 40) 


               # except Exception as e:
                      # print(f"BŁĄD: Nie udało się przenieść pliku '{filename}' do folderu '{target_folder}'. Szczegóły: {e}")


    print(f"\n GOTOWE!")                           
    print(f"Organizacja zakończona. Przeniesiono {licznik} plików.")
    print(f"Łączny rozmiar przeniesionych plików: {sizer(suma_bajty)}")

if __name__ == "__main__":
    organize()
    

    

          