#print("*****************************************************")
#print("Projeto Desenvolvido por Ellen Caroline Santos Silva ")
#print(" Análise e Desenvolvimento de Sistemas               ")
#print("*****************************************************")

import json # import da biblioteca

def mostrar_menu_principal(): #menu principal (usado desde a semana02)
    print("*****************************************************")
    print("                MENU PRINCIPAL - PUC PR              ")
    print("*****************************************************")
    print("            1 - Estudantes                           ")
    print("            2 - Professores                          ")
    print("            3 - Disciplinas                          ")
    print("            4 - Turmas                               ")
    print("            5 - Matrículas                           ")
    print("            0 - Sair                                 ")
    print("*****************************************************")

    return input("Escolha uma opção: ")

def mostrar_menu_operacoes():
    print("**** MENU DE OPERAÇÕES ****")  #menu secundário (usado desde a semana02)
    print("1 - Incluir.")
    print("2 - Listar.")
    print("3 - Atualizar ")
    print("4 - Excluir ")
    print("9 - Voltar ao menu principal.")

    return input("Escolha uma operação: ")

def salvar_arquivo(lista, nome_arquivo): # função para salvar e criar o arquivo do JSON
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo_aberto: #video aula do tutor
        json.dump(lista, arquivo_aberto, ensure_ascii=False)


def ler_arquivo(nome_arquivo):# função para abrir e fazer a leitura dos dados contidos no arquivo do JSON
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo_aberto:
            return json.load(arquivo_aberto)
    except FileNotFoundError:
        return []  # se o arquivo não for encontrado, retorna uma lista vazia

# função reutilizada - usei para facilitar as demais ações a serem criadas - no caso da semana 08 - professor, disciplina, matrícula e turmas
#CRUD do projeto - criar, listar, atualizar e excluir.
# usei chave_identificacao para que ela se adapte aos dados das diferentes entidades e não precise criar várias funções, é o que confirma a veracidade e se cada "código" é unico , ex : um cpf

def incluir_item(nome_arquivo, item, chave_identificacao):
    lista = ler_arquivo(nome_arquivo)
    for registro in lista:
        if registro[chave_identificacao] == item[chave_identificacao]:
            print(f"Erro: {chave_identificacao} já existe! Tente novamente.")
            return
    lista.append(item)
    salvar_arquivo(lista, nome_arquivo)

# função reutilizada
def listar_items(nome_arquivo, tipo_item):
    lista = ler_arquivo(nome_arquivo)
    if not lista:
        print(f"Não há {tipo_item} cadastrados.")
    else:
        for item in lista:
            print(item)

# função reutilizada
def atualizar_item(nome_arquivo, chave_identificacao, tipo_item):
    lista = ler_arquivo(nome_arquivo)
    if not lista:
        print(f"Não há {tipo_item} cadastrados.")
        return

    listar_items(nome_arquivo, tipo_item)
    try:
        codigo_para_editar = int(input(f"Qual é o código do {tipo_item} que deseja atualizar? "))
    except ValueError:
        print("Erro: Código *inválido*.")
        return

    item_para_ser_modificado = None
    for item in lista:
        if item[chave_identificacao] == codigo_para_editar:
            item_para_ser_modificado = item
            break

    if item_para_ser_modificado is None:
        print(f"{tipo_item.capitalize()} com o código {codigo_para_editar} não encontrado.")
    else:
        try:
            item_para_ser_modificado["codigo"] = int(input("Digite o novo código: "))
        except ValueError:
            print("Erro: Código *inválido*.")
            return
        item_para_ser_modificado["nome"] = input("Digite o novo nome: ")
        if "cpf" in item_para_ser_modificado:
            item_para_ser_modificado["cpf"] = input("Digite o novo CPF: ")
        salvar_arquivo(lista, nome_arquivo)
        print(f"{tipo_item.capitalize()} atualizado: {item_para_ser_modificado}")


def excluir_item(nome_arquivo, chave_identificacao, tipo_item):
    lista = ler_arquivo(nome_arquivo)
    if not lista:
        print(f"Não há {tipo_item} cadastrados.")
        return

    listar_items(nome_arquivo, tipo_item)
    try:
        codigo_para_excluir = int(input(f"Qual é o código do {tipo_item} que deseja excluir? "))
    except ValueError:
        print("Erro: Código **inválido**.")
        return

    item_para_ser_removido = None
    for item in lista:
        if item[chave_identificacao] == codigo_para_excluir:
            item_para_ser_removido = item
            break

    if item_para_ser_removido is None:
        print(f"{tipo_item.capitalize()} com o código {codigo_para_excluir} não foi encontrado, tente novamente.")
    else:
        lista.remove(item_para_ser_removido)
        salvar_arquivo(lista, nome_arquivo)
        print(f"{tipo_item.capitalize()} {item_para_ser_removido['nome']} foi removido da lista com sucesso!")

# as funções de item são para auxiliar na leitura do JSON para os demais setores além dos estudantes, ele procura o item na base e faz exibe no console a ação solicitada
# os itemms precisam ser inclusos para serem armazenados no JSON


def incluir_estudante(nome_arquivo):
    try:
        codigo = int(input("Digite o código do estudante: "))
    except ValueError:
        print("Erro: Código inválido.")
        return

    nome = input("Digite o nome do estudante: ")
    cpf = input("Digite o CPF do estudante: ")

    incluir_item(nome_arquivo, {"codigo": codigo, "nome": nome, "cpf": cpf}, "codigo")
    print(f"{nome} foi adicionado à lista de estudantes!")
#chama a função de item para armazenar no JSON e usa a lógica da semana07

#função reutilizada
def incluir_professor(nome_arquivo):
    try:
        codigo = int(input("Digite o código do professor: "))
    except ValueError:
        print("Erro: Código inválido.")
        return

    nome = input("Digite o nome do professor: ")
    cpf = input("Digite o CPF do professor: ")

    incluir_item(nome_arquivo, {"codigo": codigo, "nome": nome, "cpf": cpf}, "codigo")
    print(f"{nome} foi adicionado à lista de professores!")

#função reutilizada
def incluir_disciplina(nome_arquivo):
    try:
        codigo = int(input("Digite o código da disciplina: ")) # número
    except ValueError:
        print("Erro: Código inválido.")
        return

    nome = input("Digite o nome da disciplina: ") #string

    incluir_item(nome_arquivo, {"codigo": codigo, "nome": nome}, "codigo")
    print(f"{nome} foi adicionada à lista de disciplinas!")

#função reutilizada
def incluir_turma(nome_arquivo):
    try:
        codigo = int(input("Digite o código da turma: "))
        codigo_professor = int(input("Digite o código do professor responsável: "))
        codigo_disciplina = int(input("Digite o código da disciplina: "))
    except ValueError:
        print("Erro: Código inválido.")
        return

    nome = input("Digite o nome da turma: ")

    incluir_item(nome_arquivo, {
        "codigo": codigo,
        "nome": nome,
        "codigo_professor": codigo_professor,
        "codigo_disciplina": codigo_disciplina
    }, "codigo")
    print(f"Turma {nome} foi adicionada à lista de turmas!")

#função reutilizada - seguir a lógica do arquivo word
def incluir_matricula(nome_arquivo, estudantes_arquivo, turmas_arquivo):
    try:
        codigo_turma = int(input("Digite o código da turma: "))
        codigo_estudante = int(input("Digite o código do estudante: "))
    except ValueError: #exemplo de exceções
        print("Erro: Código inválido.")
        return

    turmas = ler_arquivo(turmas_arquivo)
    turma_existe = any(turma["codigo"] == codigo_turma for turma in turmas)
    if not turma_existe:
        print(f"Erro: Turma com código {codigo_turma} não existe.")
        return

    estudantes = ler_arquivo(estudantes_arquivo)
    estudante_existe = any(estudante["codigo"] == codigo_estudante for estudante in estudantes)
    if not estudante_existe:
        print(f"Erro: Estudante com código {codigo_estudante} não existe.")
        return


    incluir_item(nome_arquivo, {"codigo_turma": codigo_turma, "codigo_estudante": codigo_estudante}, "codigo_turma")
    print(f"Estudante {codigo_estudante} foi matriculado na turma {codigo_turma}!")

#função reutilizada
def listar_matriculas(nome_arquivo, estudantes_arquivo):
    matriculas = ler_arquivo(nome_arquivo)
    estudantes = ler_arquivo(estudantes_arquivo)

    if not matriculas:
        print("Não há matrículas cadastradas.")
    else:
        for matricula in matriculas:
            codigo_estudante = matricula["codigo_estudante"]
            nome_estudante = next((estudante["nome"] for estudante in estudantes if estudante["codigo"] == codigo_estudante), "Estudante não encontrado")
            print(f"Turma: {matricula['codigo_turma']}, Estudante: {nome_estudante} (Código: {codigo_estudante})")


# igual o prof Well ensinou no vídeo, aqui estçao referenciados os nomes dos arquivos JSON p/ cada função saber qual vai utilizar.
#Dicionários
#Persistência de dados = .json
nome_arquivos = {
    "estudantes": "estudantes.json",
    "professores": "professores.json",
    "disciplinas": "disciplinas.json",
    "turmas": "turmas.json",
    "matriculas": "matriculas.json"
}
# laço de repetição - loop principal
while True:
    menu = mostrar_menu_principal()
    if menu == "1":  # alunos
        while True:
            operacao = mostrar_menu_operacoes()
            if operacao == "1":
                incluir_estudante(nome_arquivos["estudantes"])
            elif operacao == "2":
                listar_items(nome_arquivos["estudantes"], "estudante")
            elif operacao == "3":
                atualizar_item(nome_arquivos["estudantes"], "codigo", "estudante")
            elif operacao == "4":
                excluir_item(nome_arquivos["estudantes"], "codigo", "estudante")
            elif operacao == "9":
                break
            else:
                print("Opção *inválida*.")

    elif menu == "2":  # profs
        while True:
            operacao = mostrar_menu_operacoes()
            if operacao == "1":
                incluir_professor(nome_arquivos["professores"])
            elif operacao == "2":
                listar_items(nome_arquivos["professores"], "professor")
            elif operacao == "3":
                atualizar_item(nome_arquivos["professores"], "codigo", "professor")
            elif operacao == "4":
                excluir_item(nome_arquivos["professores"], "codigo", "professor")
            elif operacao == "9":
                break
            else:
                print("Opção *inválida*.")

    elif menu == "3":  # disciplinas
        while True:
            operacao = mostrar_menu_operacoes()
            if operacao == "1":
                incluir_disciplina(nome_arquivos["disciplinas"])
            elif operacao == "2":
                listar_items(nome_arquivos["disciplinas"], "disciplina")
            elif operacao == "3":
                atualizar_item(nome_arquivos["disciplinas"], "codigo", "disciplina")
            elif operacao == "4":
                excluir_item(nome_arquivos["disciplinas"], "codigo", "disciplina")
            elif operacao == "9":
                break
            else:
                print("Opção *inválida*.")

    elif menu == "4":  # turmas
        while True:
            operacao = mostrar_menu_operacoes()
            if operacao == "1":
                incluir_turma(nome_arquivos["turmas"])
            elif operacao == "2":
                listar_items(nome_arquivos["turmas"], "turma")
            elif operacao == "3":
                atualizar_item(nome_arquivos["turmas"], "codigo", "turma")
            elif operacao == "4":
                excluir_item(nome_arquivos["turmas"], "codigo", "turma")
            elif operacao == "9":
                break
            else:
                print("Opção *inválida*.")

    elif menu == "5":  # matrículas
        while True:
            operacao = mostrar_menu_operacoes()
            if operacao == "1":
                incluir_matricula(nome_arquivos["matriculas"], nome_arquivos["estudantes"], nome_arquivos["turmas"])
            elif operacao == "2":
                listar_matriculas(nome_arquivos["matriculas"], nome_arquivos["estudantes"])
            elif operacao == "3":
                atualizar_item(nome_arquivos["matriculas"], "codigo_turma", "matrícula")
            elif operacao == "4":
                excluir_item(nome_arquivos["matriculas"], "codigo_turma", "matrícula")
            elif operacao == "9":
                break
            else:
                print("Opção *inválida*.")

    elif menu == "0":  # Sair
        print("Saindo do sistema.")
        break
    else:
         print("Opção *inválida*.")
