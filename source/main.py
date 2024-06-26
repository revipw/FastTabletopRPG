import enter, sheet, os

def clear():
  os.system('cls')

def main_gui():
  print("MENU PRINCIPAL")
  print("="*60)
  print(f"Seja bem vindo {character_name}!")
  print()
  print("[1] Fazer Teste")
  print("[2] Sair")
  print()
  print("="*60)

def roll_gui():
  options = [
    ['[1] INT', '[2] SAB', '[3] CAR', '[4] DES', '[5] FOR', '[6] VIT',"\n"],
    ['[7] Sanidade', '[8] Sorte',"\n"],
    ['[9] Atividades', '[10] Especializações', '', '[0] Voltar'],
  ]
  print("SELECIONE A OPÇÃO")
  print("="*60)
  for j in range(3):
    for i in options[j]:
      print(i, end="        ")
      print()
  print("="*60+"\n")
  enter_input = int(input(": "))
  return enter_input

def ativ_gui():
  clear()
  options = [
    ['[1] Acrobacias', '[2] Arremessar', '[3] Atletismo', '[4] Atuar', '[5] Charme', '[6] Enganar'],
    ['[7] Escutar', '[8] Esquivar', '[9] Furtividade', '[10] Intimidar', '[11] Intuição', '[12] Ler Lábios'],
    ['[13] Lidar com Animais', '[14] Lutar/Briga', '[15] Navegar', '[16] Perceber', '[17] Persuadir', '[18] Pilotar'],
    ['[19] Prestidigitar', '[20] Primeiros Socorros', '[21] Psicoanálise', '[22] Rastrear', '[23] Sobrevivência', '[24] Usar Bibliotecas', '', '[0] Voltar'],
  ]
  print("SELECIONE A OPÇÃO")
  print("="*60)
  for j in range(4):
    for i in options[j]:
      print(i, end="        ")
      print()
  print("="*60+"\n")
  enter_input = int(input(": "))
  return enter_input

def espec_gui():
  clear()
  options = [
    ['[1] Análise Forense', '[2] Armas Brancas Leves', '[3] Armas Brancas Pesadas', '[4] Arrombamento', '[5] Caligrafia', '[6] Ciência Natural'],
    ['[7] Criptografia', '[8] Direito', '[9] Espingardas', '[10] Explosivos', '[11] História', '[12] Interrogatório'],
    ['[13] Investigação', '[14] Língua Estrangeira', '[15] Língua Nativa', '[16] Medicina', '[17] Ocultismo', '[18] Pistolas'],
    ['[19] Química', '[20] Religião', '[21] Reparos Elétricos', '[22] Reparos Mecânicos', '[23] Rifles de Assalto', '[24] Rifles de Precisão', '', '[0] Voltar'],
  ]
  print("SELECIONE A OPÇÃO")
  print("="*60)
  for j in range(4):
    for i in options[j]:
      print(i, end="        ")
      print()
  print("="*60+"\n")
  enter_input = int(input(": "))
  return enter_input

character_name, character_sheet, config_file = enter.main()
field_values = sheet.get_sheet(character_sheet)

while True:
  try:
    clear()
    main_gui()
    enter_input = int(input(": "))
    if enter_input == 1:
      while True:
        clear()
        field_values = sheet.get_sheet(character_sheet)
        option_input = roll_gui()
        if 1 <= option_input <= 6:
          sheet.roll_attr(option_input, field_values)
        elif option_input == 7:
          sheet.roll_sanity(field_values)
        elif option_input == 8:
          sheet.roll_luck()
        elif option_input == 9:
          while True:
            field_values = sheet.get_sheet(character_sheet)
            ativ_input = ativ_gui()
            if ativ_input == 0:
              break
            sheet.roll_ativ(ativ_input, field_values)
        elif option_input == 10:
          while True:
            field_values = sheet.get_sheet(character_sheet)
            espec_input = espec_gui()
            if espec_input == 0:
              break
            sheet.roll_espec(espec_input, field_values)
        elif option_input == 0:
          break
        else:
          continue
    elif enter_input == 2:
      clear()
      break
    else:
      continue
  except ValueError or TypeError:
    continue