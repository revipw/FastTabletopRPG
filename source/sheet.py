import PyPDF2
import random, os

def clear():
  os.system('cls')

def get_sheet(sheet_path):
  with open(sheet_path, 'rb') as pdf:
    reader = PyPDF2.PdfReader(pdf)
    if not reader.get_fields():
      return
        
    form_fields = reader.get_fields()
    field_values = {}

    for field_name, field_data in form_fields.items():
      field_values[field_name] = field_data.get('/V', None)
    
    return field_values
  
def roll(attribute, moddifier):
  clear()
  attribute = int(attribute)
  moddifier = int(moddifier)

  normal = (attribute/2)+1
  good = normal/2

  dice = random.randint(1,100)

  play = dice + moddifier
  if play <= 0:
    play = 1
  
  print(f"Atributo: {attribute}")
  print()
  dsp_msg = f"Resultado obtido: {dice} - {moddifier*-1} = {play}"

  if play <= attribute:
    print(dsp_msg)
    if normal <= play <= attribute:
      print("Sucesso Normal.")
    elif good <= play <= normal-1:
      print("Sucesso BOM!")
    else:
      print("SUCESSO EXTREMO!")
  elif dice == 100:
    print(f"Resultado obtido: {dice} / MODIFICADOR ANULADO!")
    print("DESASTRE!")
  else:
    print(dsp_msg)
    print("Falha!")
  print() 
  print("Pressione ENTER para continuar...") 
  input()

def roll_attr(option_input, field_values):
  chosen_attr = option_input-1
  attributes = [field_values['INT'], field_values['SAB'], field_values['CAR'], field_values['DES'], field_values['FOR'], field_values['VIT']]
  moddifiers = [field_values['MODINT'], field_values['MODSAB'], field_values['MODCAR'], field_values['MODDES'], field_values['MODFOR'], field_values['MODVIT']]
  
  roll(attributes[chosen_attr], moddifiers[chosen_attr])

def roll_sanity(field_values):
  string = field_values['PS'].split('/')
  current = string[0].strip()

  current_int = int(current)

  roll(current_int, 0)

def roll_luck():
  clear()
  dice = random.randint(1, 100)
  if 1 <= dice <= 49:
    print("SORTE!")
  elif dice == 50:
    print("Neutro.")
  else:
    print("AZAR!")
  print() 
  print("Pressione ENTER para continuar...") 
  input()

def sort(item):
  if item.startswith('MOD'):
    try:
      return int(item[3:])
    except ValueError:
      return float('inf')
  else:
    return item

def roll_ativ(option_input, field_values):
  chosen_ativ = option_input-1
  dictionary = {key: value for key, value in field_values.items() if key.startswith('MOD')}
  sorted_dict = sorted(dictionary)
  activities = sorted(sorted_dict, key=sort)
  activities = [item for item in activities if item.startswith("MOD") and item[3:].isdigit()]
  force = [activities[2], activities[13]]
  dexterity = [activities[0], activities[7], activities[13], activities[18], activities[8], activities[1], activities[17]]
  charism = [activities[3], activities[4], activities[5], activities[9], activities[16],activities[12]]
  intelligence = [activities[19], activities[20], activities[18], activities[8], activities[6], activities[14], activities[15], activities[21], activities[23], activities[10], activities[11]]
  try:
    if activities[chosen_ativ] in force:
      attribute = int(field_values["FOR"])
      try:
        moddifier = int(field_values[activities[chosen_ativ]])
      except TypeError:
        moddifier = 0
    elif activities[chosen_ativ] in dexterity:
      attribute = int(field_values["DES"])
      try:
        moddifier = int(field_values[activities[chosen_ativ]])
      except TypeError:
        moddifier = 0
    elif activities[chosen_ativ] in charism:
      attribute = int(field_values["CAR"])
      try:
        moddifier = int(field_values[activities[chosen_ativ]])
      except TypeError:
        moddifier = 0
    elif activities[chosen_ativ] in intelligence:
      attribute = int(field_values["INT"])
      try:
        moddifier = int(field_values[activities[chosen_ativ]])
      except TypeError:
        moddifier = 0
    else:
      attribute = int(field_values["VIT"])
      try:
        moddifier = int(field_values[activities[chosen_ativ]])
      except TypeError:
        moddifier = 0
  except IndexError or ValueError or TypeError:
    return
  roll(attribute, moddifier)

def roll_espec(option_input, field_values):
  chosen_espec = option_input-1
  dictionary = {key: value for key, value in field_values.items() if key.startswith('EMOD')}
  sorted_dict = sorted(dictionary)
  expertises = sorted(sorted_dict, key=lambda x: int(x[4:]))
  expertises = [item for item in expertises if item.startswith("EMOD") and item[4:].isdigit()]
 
  force = [expertises[2], expertises[8]]
  dexterity = [expertises[1], expertises[3], expertises[23], expertises[22], expertises[21], expertises[20], expertises[17], expertises[9]]
  charism = [expertises[13]]
  intelligence = [expertises[0], expertises[4], expertises[6], expertises[12]]
  try:
    if expertises[chosen_espec] in force:
      attribute = int(field_values["FOR"])
      try:
        moddifier = int(field_values[expertises[chosen_espec]])
      except TypeError:
        moddifier = 0
    elif expertises[chosen_espec] in dexterity:
      attribute = int(field_values["DES"])
      try:
        moddifier = int(field_values[expertises[chosen_espec]])
      except TypeError:
        moddifier = 0
    elif expertises[chosen_espec] in charism:
      attribute = int(field_values["CAR"])
      try:
        moddifier = int(field_values[expertises[chosen_espec]])
      except TypeError:
        moddifier = 0
    elif expertises[chosen_espec] in intelligence:
      attribute = int(field_values["INT"])
      try:
        moddifier = int(field_values[expertises[chosen_espec]])
      except TypeError:
        moddifier = 0
    else:
      attribute = int(field_values["SAB"])
      try:
        moddifier = int(field_values[expertises[chosen_espec]])
      except TypeError:
        moddifier = 0
  except IndexError or ValueError or TypeError:
    return
  roll(attribute, moddifier)

  


  


  

