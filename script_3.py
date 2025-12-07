import zipfile
import os

# List all files to include in the archive
files = [
    'online-grocery-system/index.html', 'online-grocery-system/home.html', 'online-grocery-system/products.html',
    'online-grocery-system/cart.html', 'online-grocery-system/address.html', 'online-grocery-system/payment.html',
    'online-grocery-system/confirmation.html', 'online-grocery-system/orders.html', 'online-grocery-system/profile.html',
    'style.css', 'data.js', 'common.js', 'auth.js', 'home.js', 'products.js'
]

# Also copy files to their respective directories in the folder structure for a real app
os.makedirs('online-grocery-system/css', exist_ok=True)
os.makedirs('online-grocery-system/js', exist_ok=True)

# Move files to correct directories
import shutil
shutil.move('style.css', 'online-grocery-system/css/style.css')
shutil.move('data.js', 'online-grocery-system/js/data.js')
shutil.move('common.js', 'online-grocery-system/js/common.js')
shutil.move('auth.js', 'online-grocery-system/js/auth.js')
shutil.move('home.js', 'online-grocery-system/js/home.js')
shutil.move('products.js', 'online-grocery-system/js/products.js')

# Zip the app
with zipfile.ZipFile('online-grocery-system.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    for folder, _, files in os.walk('online-grocery-system'):
        for file in files:
            filepath = os.path.join(folder, file)
            zipf.write(filepath, arcname=os.path.relpath(filepath, 'online-grocery-system'))

print('Zipped all files to online-grocery-system.zip')
