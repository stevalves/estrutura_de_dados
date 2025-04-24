alunos = []
orientadores = {}


mensagem1 = """
Escolha uma das seguintes opções:
1 - Cadastrar orientadores
2 - Cadastrar alunos
3 - Realizar Operações
q - Sair
"""

mensagem2 = """
Escolha uma das seguintes opções:
1 - Registrar nova entrega.
2 - Registrar nota.
3 - Listar alunos por orientador.
4 - Listar versões entregues por aluno.
5 - Listar pendências de avaliação.
6 - Gerar relatório do orientador.
q - Voltar ao menu principal.
"""

def cadastrar_orientador():
  orientador = input("Digite o nome do orientador: ")
  orientadores[orientador] = []

def listar_orientarores():
  for orientador in orientadores:
    print(orientador)

def cadastrar_aluno():
  aluno = input("Digite o nome do aluno: ")
  matricula = input("Digite a matricula do aluno: ")
  print("Orientadores disponíveis: ")
  listar_orientarores()
  orientador = input("Digite o orientador do aluno: ")

  if orientador not in orientadores:
    print("Orientador não cadastrado.")
    return
  entregas = []

  orientadores[orientador].append(aluno)

  alunos.append({
    "nome": aluno,
    "matricula": matricula,
    "orientador": orientador,
    "entregas": entregas
  })

def listar_alunos(orientador: str = None):
  lista_de_alunos = "\nAlunos cadastrados: \n"

  for aluno in alunos:
    if orientador:
      if aluno["orientador"] != orientador:
        pass
      else:
        lista_de_alunos += f"{aluno['nome'], aluno["matricula"]}\n"
    else:
      lista_de_alunos += f"{aluno['nome'], aluno["matricula"]}"

  print(lista_de_alunos)

def criar_entrega(matricula_aluno: str):
  aluno_encontrado = False

  data = input("Digite a data (aaaa-mm-dd): ")

  for aluno in alunos:
    if aluno["matricula"] == matricula_aluno:
      aluno_encontrado = True
      if len(aluno["entregas"]) != 0:
        *_, nota = aluno["entregas"][-1]
        if nota == None:
          print("Não foi possível adicionar envio pois a última entrega ainda não foi corrigida!")
          break

      aluno["entregas"].append((f"v{len(aluno['entregas'])+1}", data, None))
      print(aluno)
      break

  if not aluno_encontrado:
    print("Aluno não cadastrado.")

def listar_entregas_por_aluno(matricula_aluno: str):
  aluno_encontrado = False

  for aluno in alunos:
    if aluno["matricula"] == matricula_aluno:
      aluno_encontrado = True
      print(aluno["entregas"])
      break

  if not aluno_encontrado:
    print("Aluno não cadastrado.")

def listar_pendencias_de_avaliacao():
  lista_de_alunos = "\nAlunos com avaliação pendente: \n"
  for aluno in alunos:
    if len(aluno["entregas"]) == 0:
      continue
    versao, data, nota = aluno["entregas"][-1]
    if nota == None:
      lista_de_alunos += f"\n{aluno["nome"], aluno["matricula"]}\nAtividade Pendente:\nVersão: {versao} \nData: {data} \nNota: {nota}\n"

  print(lista_de_alunos)

def registrar_nota(matricula_aluno: str):
  aluno_encontrado = False

  for aluno in alunos:
    if aluno["matricula"] == matricula_aluno:
      aluno_encontrado = True
      versao, data, nota = aluno["entregas"][-1]

      if nota != None:
        print("Esta entrega ja foi corrigida!")
        break

      aluno["entregas"][-1] = (versao, data, float(input("Digite a nota: ")))
      print("Entrega corrigida com sucesso!")
      break

  if not aluno_encontrado:
    print("Aluno não cadastrado.")

def relatorio_do_orientador(orientador: str):
  lista_de_alunos = "\nLista de alunos: \n"

  for aluno in alunos:
    if aluno["orientador"] == orientador:
      media = 0
      media_geral = 0
      notas_corrigidas = 0
      for entrega in aluno["entregas"]:
        *_, nota = entrega
        if nota != None:
          media += nota
          media_geral = nota
          notas_corrigidas += 1
      if notas_corrigidas == 0:
        break
      media /= notas_corrigidas
      lista_de_alunos += "Aluno: " + aluno["nome"] + "\nMatricula: " + aluno["matricula"] + "\nMedia: " + str(media) + "\nMedia geral: " + str(media_geral) + "\n\n"

  print(lista_de_alunos)
      

while True:
  print(mensagem1)

  opcao = input("Digite a opção desejada: ")

  match opcao:
    case "1":
      print("Cadastrar orientadores")
      cadastrar_orientador()
    case "2":
      print("Cadastrar alunos")
      cadastrar_aluno()
      listar_alunos()
    case "3":
      while True:
        print(mensagem2)
        opcao2 = input("Digite a opção desejada: ")

        match opcao2:
          case "1":
            print("Registrar nova entrega.")
            listar_alunos()
            criar_entrega(input("Digite a matricula do aluno: "))
          case "2":
            print("Registrar nota.")
            listar_pendencias_de_avaliacao()
            registrar_nota(input("Digite a matricula do aluno: "))
          case "3":
            print("Listar alunos por orientador.")
            print("Orientadores disponíveis: ")
            listar_orientarores()
            listar_alunos(input("Digite o orientador: "))
          case "4":
            print("Listar versões entregues por aluno.")
            listar_alunos()
            listar_entregas_por_aluno(input("Digite a matricula do aluno: "))
          case "5":
            print("Listar pendências de avaliação.")
            listar_pendencias_de_avaliacao()
          case "6":
            print("Gerar relatório do orientador.")
            listar_orientarores()
            relatorio_do_orientador(input("Digite o orientador: "))
          case "q":
            print("Voltar ao menu principal.")
            break
      
    case "q":
      print("Sair")
      break

