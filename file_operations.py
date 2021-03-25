import os
import shutil
import tempfile


user_name = input("input yor user name -").strip("")

f_temp = tempfile.mkdtemp()
os.chdir(f_temp)


for root, dirs, files in os.walk(os.path.normpath("C:/Users/Lenovo/PycharmProjects")):
    for file in files:
        if file.endswith(".py"):
            root_name = root.split("\\")[-1]
            root_name_1 = ""
            if user_name in root_name:
                root_name_1 = "-".join(root_name.split("-")[:-2])
            else:
                root_name_1 = root_name
            if not os.path.exists(root_name_1):
                os.makedirs(os.path.normpath(root_name_1))

            shutil.copyfile(
                root + "\\" + file, os.getcwd() + "\\" + root_name_1 + "\\" + file
            )

temp_file = os.getcwd()
os.chdir(
    "C:\\Users\\Lenovo\\PycharmProjects\\reconstruct-homework-folder-and-make-zip-Levon-98"
)

shutil.make_archive(
    "C:\\Users\\Lenovo\\PycharmProjects\\reconstruct-homework-folder-and-make-zip-Levon-98\\zip.zip",
    "zip",
)

shutil.rmtree(temp_file)
