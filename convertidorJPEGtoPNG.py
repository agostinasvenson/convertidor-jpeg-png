import os
from PIL import Image

def convertidor(folder, new_folder):
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print(f"Error: La carpeta '{folder}' no existe.")
        return
    except PermissionError:
        print(f"Error: No tienes permiso para acceder a la carpeta '{folder}'.")
        return
    except OSError as e:
        print(f"Error al acceder a la carpeta '{folder}': {e}")
        return
        
#os.listdir(folder) --> Lista archivos en carpeta de origen(folder):
    for filename in os.listdir(folder):
        #Verificar terminación de archivos. Si son JPEG o JPG:
        if filename.lower().endswith(".jpeg") or filename.lower().endswith(".jpg"):
            #Contruir ruta completa para cada archivo y lo guarda en variable
            filepath = os.path.join(folder, filename)


            try:
                # Abrir y convertir la imagen
                with Image.open(filepath) as img:
                    img.verify()  # Verifica que la imagen es válida
                    img = Image.open(filepath)  # Volver a abrir después de verificar
                    new_filename = os.path.splitext(filename)[0] + ".png"
                    new_filepath = os.path.join(new_folder, new_filename)
                    
                    img.save(new_filepath, "PNG")
                    
                    print(f"Convertido: {filename} -> {new_filename}")
            
            except FileNotFoundError:
                print(f"Error: El archivo '{filepath}' no se encontró.")
            except UnidentifiedImageError:
                print(f"Error: El archivo '{filepath}' no es una imagen válida.")
            except PermissionError:
                print(f"Error: No tienes permiso para guardar en '{new_folder}'.")
            except OSError as e:
                print(f"Error al procesar la imagen '{filename}': {e}")

           

#Ejemplo de llamada a la función:
convertidor("pokeimages", "nueva_carpeta")