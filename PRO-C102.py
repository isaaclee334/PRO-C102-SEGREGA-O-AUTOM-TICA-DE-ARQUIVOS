import os
import shutil


from_dir = "C:/Users/lee/Documents/Arquivos_teste1"

to_dir = "C:/Users/lee/Documents/Arquivos_teste2"

list_of_files = os.listdir(from_dir)

#print(list_of_files)


for file_name in list_of_files:
  name,extension = os.path.splitext(file_name)
  #print(extension)
  if extension == '':
    continue
  if extension in ['.txt', '.doc', '.docx', '.pdf']:
    path1 = from_dir+'/'+file_name
    path2 = to_dir+'/'+"ArquivoTeste"
    path3 = to_dir+'/'+"ArquivoTest"+'/'+file_name

    print("path1",path1)
    print("path2",path2)
if os.path.exists(path2):
 print('movendo'+file_name+'......')
 shutil.move(path1,path2)
else:
 os.makedirs(path2)
 print('movendo'+file_name+'......')
 shutil.move(path1,path3)