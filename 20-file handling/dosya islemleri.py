#File Handing
# f=open("Files/demo.txt","x")
f=open("Files/demo.txt","r",encoding="utf-8")
#satır satır yazdırmak icin
# print(f.readline())
# print(f.readline())

#direkt yazdırma işlemi icin
# print(f.read())

#Boşluk sorununu çözmek icin
# print(f.readline(),end="")

# for line in f:
#     print(line,end="")

#dosya kapatmak icin
# f.close()

#tüm satırları çeker ve list halinde ekrana yazdırır
# print(f.readlines())
#list üzerinden satırlara ulasmak
# my_line=f.readlines()
# print(my_line[2])

#daha uzun satırlarda for döngüsü kullanılır
# for line in f.readlines():
#     print(line,end="")


#Dosya imleç konumunu değiştirme
#f=open("Files/demo.txt","r",encoding="utf-8")

# print(f.read(10))

# print("---------")
# f.seek(0)
# print(f.read())

# f.close()


#Dosya açık mı kontrolü
# f=open("Files/demo.txt","r",encoding="utf-8")

# print(f.closed)
# f.close()
# print(f.closed)
# print(f.read())  #dosya kapandıgı icin okuma işlemi yapamam

#Dosyamı açtıgım anda nasıl kapatabilirim?
# with open("Files/demo.txt",encoding="utf-8") as f:
#     print(f.read())

#Tell metodu=imlecimin nerede oldugunu gösterir

# with open("Files/demo.txt",encoding="utf-8") as f:
#     print(f.read(10))
#     print(f.tell())
#     print(f.read(10))
#     print(f.tell())

#with kullanarak for döngüsü ile tüm metni okuma islemi
# with open("Files/demo.txt",encoding="utf-8") as f:
#     for line in f:
#         print(line,end="")


#with ile satır satır okuma islemi
# with open("Files/demo.txt",encoding="utf-8") as f:
#     print(f.readline(),end="")
#     print(f.readline(),end="")
#     print(f.readline(),end="")
    
#with ile satır satır okuma islemi ama for döngüsü ile
# with open("Files/demo.txt",encoding="utf-8") as f:
#      for lines in f.readlines():
#           print(lines,end="")

#Dosyanın okuma modunda açılıp açılmadıgını kontrol etmek icin readable metodu
# with open("Files/demo.txt",encoding="utf-8") as f:
#     print(f.readable())

# with open("Files/demo.txt","x",encoding="utf-8") as f:
#     print(f.readable())


#seekable metodu
# with open("Files/demo.txt","r",encoding="utf-8") as f:
#     print(f.seekable())


# with open("Files/demo.txt","r",encoding="utf-8") as f:
#     f.seek(53)
#     print(f.read())

#Truncate metodu: Dosya kesme










#Dosya yazma ve ekleme işlemleri
# with open("Files/newfile.txt","w",encoding="utf-8") as f:
#     f.write("How is it going?\n")

# with open("Files/newfile.txt","r",encoding="utf-8")  as f:
#     print(f.read())


#writelines metodu:
# fruits=["grape\n","strawberry\n","fig\n","banana"]

# with open("Files/newfile.txt","w",encoding="utf-8") as f:
#      f.writelines(fruits)

# with open("Files/newfile.txt","r",encoding="utf-8") as f:
#      print(f.read())

#append metodu= Dosyanın iceriğini silmeden veri ekler
# fruits=["grape\n","strawberry\n","fig\n","banana"]

# with open("Files/newfile.txt","a",encoding="utf-8") as f:
#      f.write("\nThis line was added later!")

# with open("Files/newfile.txt","r",encoding="utf-8") as f:
#      print(f.read())


#Dosyayı hem yazma hem de okumak icin w+
# with open("Files/newfile.txt","w+",encoding="utf-8") as f:
#      f.write("New Content!")
#      f.seek(0)
#      print(f.read())

#Dosyaya hem ekleme hem de okuma yapmak icin a+
# with open("Files/newfile.txt","a+",encoding="utf-8") as f:
#     f.write("Append mod\n")
#     f.seek(0)
#     print(f.read())

#Dosyayı hem okuma hem de yazma r+
# with open("Files/newfile.txt","r+",encoding="utf-8") as f:
#     print("Original Content:")
#     print(f.read())

#     f.seek(0)
#     f.write("Updated")

#     f.seek(0)
#     print("nUpdated Content:")
#     print(f.read())



#Dosya silme remove:

# import os

# if(os.path.exists("Files/newfile.txt")):
#     os remove("Files\newfile.txt")

# else:
#     print("The file does not exist")

#Klasör silme işlemi i.in rmmdir

# import os
# os.rmdir("deneme")

#Dosya ve klasör listlemek icin 
# import os
# print(os.listdir())

#Klasör olusturmak icin
# import as 
# print(os.listdir())
# os.mkdir(C:\Users\buse\Desktop\git hub\python-learning-journal\20-dosya islemleri\dosya islemleri.py)

# print(os.listdir())
# os.rmdir("NewFolder")

#Dosyada veri güncelleme ve en başa veri yazdırma
# with open("Files/demo.txt","r+",encoding="utf-8") as f:
#     my text=f.read()
#     my_"1_Python\n" + my_text
#     f.seek(0)
#     f.write(my_text)
#     f.seek(0)
#     print(f.read())
    
#Dosyanın ortasına nasıl veri ekleyeceğiz:

# with open("Files/demo.txt","r+",encoding="utf-8") as f:
#     my_list=f.readlines()
#     my_list.insert(3,"4-Java\n")
#     f.seek(0)
#     f.writelines(my_list)
#     f.seek(0)
#     print(f.read())

