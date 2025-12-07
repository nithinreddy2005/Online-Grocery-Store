import zipfile
import os

with zipfile.ZipFile('online-grocery-system-files.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    for folder, subfolders, files in os.walk('online-grocery-system'):
        for file in files:
            filepath = os.path.join(folder, file)
            zipf.write(filepath, arcname=os.path.relpath(filepath, 'online-grocery-system'))
print('Zipped all app files to online-grocery-system-files.zip')
