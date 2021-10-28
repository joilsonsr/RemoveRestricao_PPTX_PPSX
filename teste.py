import os
import pathlib

print(os.path.splitext(pathlib.Path("Mecânica.ppsx"))[0])
print(pathlib.Path("Mecânica.ppsx").absolute().parent)
    # with ZipFile(filepath, 'w') as zipf:
    #     # Add a file located at the source_path to the destination within the zip
    #     # file. It will overwrite existing files if the names collide, but it
    #     # will give a warning
    #     source_path = new_file_inter.stem
    #     destination = "/"
    #     zipf.write(source_path, destination)
    #subprocess.call(["zip", "-r", new_file_copy,file_to_change ])
    #subprocess.call(['zip', '-r', 'example.zip', directory])
       
    #os.rename(new_file, encr_file)
    #folder_to_remove = str(pathlib.Path(file_to_change).parent)