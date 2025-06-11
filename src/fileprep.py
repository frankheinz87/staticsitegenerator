import os
import shutil


def file_preparation(sourcedir,destdir):
    dest_list=os.listdir(destdir)
    source_list=os.listdir(sourcedir)
    print(f"destination: {dest_list}")
    print(f"source: {source_list}")
    #file deletion in destination
    empty_destdir(destdir)
    #copy files from source to destination
    copy_source_to_dest(sourcedir,destdir)

def empty_destdir(destdir):
    dest_list=os.listdir(destdir)

    if dest_list==[]:
        print(f"target directory already empty")
        return

    for item in dest_list:
        item_path=os.path.join(destdir,item)
        if os.path.isfile(item_path):
            os.unlink(item_path)
            print(f"deleting file: {item_path}")                 
        else:
            print(f"going into: {item_path}")
            empty_destdir(item_path)
            print(f"deleting directory: {item_path}")
            os.rmdir(item_path)

def copy_source_to_dest(sourcedir,destdir):
    dest_list=os.listdir(destdir)
    source_list=os.listdir(sourcedir)
    if dest_list!=[]:
        print("target directory not empty")
        return
    if source_list==[]:
        print("nothing to copy")
        return
    if dest_list==source_list:
        print("source and target contain the same elements")
        return 
    
    for item in source_list:
        source_path=os.path.join(sourcedir,item)
        dest_path=os.path.join(destdir,item)
        if os.path.isfile(source_path):
            shutil.copy(source_path,dest_path)
            print(f"copying file: {source_path} to {dest_path}")
        elif os.path.isdir(source_path) and os.listdir(source_path)==[]: 
            os.mkdir(dest_path)
            print(f"creating directory: {dest_path}")                   
        else:
            print(f"creating directory: {dest_path}") 
            os.mkdir(dest_path)
            print(f"going into: {source_path}")
            copy_source_to_dest(source_path,dest_path)