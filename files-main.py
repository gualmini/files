import os
import pathlib
from zipfile import ZipFile


def clean_cache():
    if not os.path.exists("cache"):
        os.mkdir("cache")
    else:
        for file in os.listdir("cache"):
            os.remove(os.path.join("cache", file))

def cache_zip(zipped_file, directory):
    with ZipFile(zipped_file, "r") as zf:
        zf.extractall(directory)

def cached_files():
    my_directory = pathlib.Path("cache")
    list_of_files = list(my_directory.iterdir())
    list_of_files_absolute_path = []
    for individual_file in list_of_files:
        list_of_files_absolute_path.append(os.path.abspath(individual_file))
    return list_of_files_absolute_path


#clean_cache()
#cache_zip("data.zip")
#print(cached_files())
list_of_files_absolute_path = cached_files()

def find_password(list_of_files):
    for individual_file in list_of_files:
        with open(individual_file, 'r') as file:
            content = file.read()
            if "password" in content:
                print(f"The word password was found in file {individual_file}.")
                with open(individual_file, 'r') as file:
                    individual_lines = file.readlines()
                    for individual_line in individual_lines:
                        if "password" in individual_line:
                            print(individual_line.split()[1])


find_password(list_of_files_absolute_path)
   