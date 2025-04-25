alunos = []
orientadores = {}

mensagem1 = """
📘 MENU PRINCIPAL
Escolha uma das seguintes opções:
1 - Cadastrar orientadores
2 - Cadastrar alunos
3 - Realizar Operações
q - Sair
"""

mensagem2 = """
🛠️ MENU DE OPERAÇÕES
Escolha uma das seguintes opções:
1 - Registrar nova entrega
2 - Registrar nota
3 - Listar alunos por orientador
4 - Listar versões entregues por aluno
5 - Listar pendências de avaliação
6 - Gerar relatório do orientador
q - Voltar ao menu principal
"""

def cadastrar_orientador():
  orientador = input("Digite o nome do orientador: ")
  orientadores[orientador] = []
  print("\n✅ Orientador cadastrado com sucesso!\n")

def listar_orientarores():
  print("\n📚 Orientadores cadastrados:\n")
  for orientador in orientadores:
    print(f" - {orientador}")
  print()

def cadastrar_aluno():
  aluno = input("Digite o nome do aluno: ")
  matricula = input("Digite a matricula do aluno: ")
  print("\n📚 Orientadores disponíveis:\n")
  listar_orientarores()
  orientador = input("Digite o orientador do aluno: ")

  if orientador not in orientadores:
    print("\n❌ Orientador não cadastrado.\n")
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
  lista_de_alunos = "\n👥 Alunos cadastrados:\n"

  for aluno in alunos:
    if orientador:
      if aluno["orientador"] != orientador:
        pass
      else:
        lista_de_alunos += f" - Nome: {aluno['nome']} | Matrícula: {aluno['matricula']}\n"
    else:
      lista_de_alunos += f" - Nome: {aluno['nome']} | Matrícula: {aluno['matricula']}\n"

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
          print("\n⚠️ Não foi possível adicionar envio pois a última entrega ainda não foi corrigida!\n")
          break

      aluno["entregas"].append((f"v{len(aluno['entregas'])+1}", data, None))
      print("\n📦 Entrega registrada com sucesso:\n", aluno, "\n")
      break

  if not aluno_encontrado:
    print("\n❌ Aluno não cadastrado.\n")

def listar_entregas_por_aluno(matricula_aluno: str):
  aluno_encontrado = False

  for aluno in alunos:
    if aluno["matricula"] == matricula_aluno:
      aluno_encontrado = True
      print("\n📦 Entregas realizadas:\n", aluno["entregas"], "\n")
      break

  if not aluno_encontrado:
    print("\n❌ Aluno não cadastrado.\n")

def listar_pendencias_de_avaliacao():
  lista_de_alunos = "\n📌 Alunos com avaliação pendente:\n"
  for aluno in alunos:
    if len(aluno["entregas"]) == 0:
      continue
    versao, data, nota = aluno["entregas"][-1]
    if nota == None:
      lista_de_alunos += (
        f"\n🧑 Aluno: {aluno['nome']} | Matrícula: {aluno['matricula']}\n"
        f"⏳ Atividade Pendente:\n  • Versão: {versao}\n  • Data: {data}\n  • Nota: {nota}\n"
      )

  print(lista_de_alunos)

def registrar_nota(matricula_aluno: str):
  aluno_encontrado = False

  for aluno in alunos:
    if aluno["matricula"] == matricula_aluno:
      aluno_encontrado = True
      versao, data, nota = aluno["entregas"][-1]

      if nota != None:
        print("\n⚠️ Esta entrega já foi corrigida!\n")
        break

      aluno["entregas"][-1] = (versao, data, float(input("Digite a nota: ")))
      print("\n✅ Entrega corrigida com sucesso!\n")
      break

  if not aluno_encontrado:
    print("\n❌ Aluno não cadastrado.\n")

def relatorio_do_orientador(orientador: str):
  lista_de_alunos = f"\n📋 Relatório do orientador: {orientador}\n"

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
      lista_de_alunos += (
        f"\n👨‍🎓 Aluno: {aluno['nome']}\n"
        f"📎 Matrícula: {aluno['matricula']}\n"
        f"📊 Média das entregas: {media:.2f}\n"
        f"📈 Última nota registrada: {media_geral}\n"
      )

  print(lista_de_alunos)

while True:
  print(mensagem1)

  opcao = input("Digite a opção desejada: ")

  match opcao:
    case "1":
      print("\n➡️ Cadastrar orientadores\n")
      cadastrar_orientador()
    case "2":
      print("\n➡️ Cadastrar alunos\n")
      cadastrar_aluno()
      listar_alunos()
    case "3":
      while True:
        print(mensagem2)
        opcao2 = input("Digite a opção desejada: ")

        match opcao2:
          case "1":
            print("\n📝 Registrar nova entrega\n")
            listar_alunos()
            criar_entrega(input("Digite a matricula do aluno: "))
          case "2":
            print("\n📝 Registrar nota\n")
            listar_pendencias_de_avaliacao()
            registrar_nota(input("Digite a matricula do aluno: "))
          case "3":
            print("\n📄 Listar alunos por orientador\n")
            print("\n📚 Orientadores disponíveis:\n")
            listar_orientarores()
            listar_alunos(input("Digite o orientador: "))
          case "4":
            print("\n📄 Listar versões entregues por aluno\n")
            listar_alunos()
            listar_entregas_por_aluno(input("Digite a matricula do aluno: "))
          case "5":
            print("\n📌 Listar pendências de avaliação\n")
            listar_pendencias_de_avaliacao()
          case "6":
            print("\n📋 Gerar relatório do orientador\n")
            listar_orientarores()
            relatorio_do_orientador(input("Digite o orientador: "))
          case "q":
            print("\n🔄 Voltar ao menu principal\n")
            break
    case "q":
      print("\n👋 Saindo do sistema...\n")
      break
