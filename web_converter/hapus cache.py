import shutil
import os
import win32com.client.gencache

gen_py_path = win32com.client.gencache.GetGeneratePath()
print(f"Menghapus folder cache COM: {gen_py_path}")

if os.path.exists(gen_py_path):
    shutil.rmtree(gen_py_path)
    print("Cache COM berhasil dihapus.")
else:
    print("Folder cache COM tidak ditemukan.")