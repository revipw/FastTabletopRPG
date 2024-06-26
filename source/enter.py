import os, glob, sys
import tkinter as tk
from tkinter import filedialog

def clear():
  os.system('cls')

def get_path():
  if getattr(sys, 'frozen', False):
    return os.path.dirname(sys.executable)
  else:
    return os.path.dirname(os.path.abspath(__file__))

absolute_path = get_path()

def write(file, content):
  with open(file, 'w') as file:
    for line in content:
      file.write(line)

def read (file):
  with open(file, 'r') as file:
    lines = file.readlines()
  return lines

# NEW =*
def file_check_gui():
  print("Um arquivo de configuração já existe, deseja sobrescrevê-lo ou criar um novo?")
  print("="*60)
  print()
  print("[1] Sobrescrever")
  print("[2] Criar Novo")
  print()
  print("="*60)

def file_check(absolute_path, filename, extension, content):
    clear()
    new_file = absolute_path+filename+extension
    if os.path.exists(new_file):
      file_check_gui()
      enter_input = int(input(":"))
      if enter_input == 1:
        write(new_file, content)
      elif enter_input == 2:
        files = glob.glob(absolute_path + f"\\{filename}*.ini")
        new_file = absolute_path+filename+str((len(files)+1))+extension
        content[2] = new_file + "\n"
        write(new_file, content)
      else:
        file_check(absolute_path, filename, extension, content)
    else:
      write(new_file, content)
    return new_file

def select_sheet():
  root = tk.Tk()
  root.withdraw()
  file_path = filedialog.askopenfilename(
    title = "Selecione o arquivo PDF",
    filetypes=[("Arquivos PDF", "*.pdf")]
  )
  return file_path

def new():
  clear()
  character_name = str(input("Digite o nome do seu personagem: "))
  clear()
  character_sheet = select_sheet()
  filename = "\\" + character_name 
  extension = ".ini"
  content = [
    "[DEFAULT]\n",
    character_sheet + "\n",
    absolute_path + filename + extension + "\n",
    character_name
  ]
  config_file = file_check(absolute_path, filename, extension, content)
  return character_name, character_sheet, config_file
# NEW *=

# LOAD =*
def load_gui():
  clear()
  files = glob.glob(absolute_path+"\\*.ini")
  index = len(files)
  if index <= 0:
    return files
  print("Qual aventura gostaria de carregar?")
  print("="*60)
  counter = 0
  for i in files:
    counter += 1
    print(f"[{counter}] {i}")
  print("="*60)
  return files

def load():
  clear()
  files = load_gui()
  if len(files) == 0:
    return  
  enter_input = int(input(": "))
  try:
    config_file = files[enter_input-1]
  except IndexError or ValueError:
    return
  content = read(config_file)
  character_name = content[3]
  character_sheet = content[1][:-1]
  return character_name, character_sheet, config_file

def main_gui():
  clear()
  print("Fast Tabletop RPG v1.0 - Unveiling Secrets Rules System")
  print("="*60)
  print()
  print("[1] Nova Aventura")
  print("[2] Carregar Aventura")
  print()
  print("="*60)

def main():
  while True:
    main_gui()
    try:
      enter_input = int(input(": "))
      if enter_input == 1:
        try:
          character_name, character_sheet, config_file = new()
        except TypeError or ValueError:
          continue
      elif enter_input == 2:
        try:
          character_name, character_sheet, config_file = load()
        except TypeError or ValueError:
          continue
      try:
        if config_file is not None:
          return character_name, character_sheet, config_file
      except UnboundLocalError:
        continue
    except ValueError or TypeError:
      continue


