import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:  # dest_dir as inputs, and w as write mode

        for filepath in filepaths:  # archive represents zip file object instance
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)  # each filepath in filepaths list
                                    # so extract only file name from filepath

if __name__ == "__main__":  # if this script is executed as main script
    make_archive(filepaths=["a.py", "b.py"], dest_dir="dest")
