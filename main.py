import random
import json
import re

def ler_limites_csv(arquivo):
    limites = {}
    with open(arquivo, 'r') as file:
        next(file)  # Pula o cabeçalho
        for linha in file:
            partes = linha.strip().split(',')
            limites[partes[0]] = (int(partes[1]), int(partes[2]))
    return limites

def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as file:
        json.dump(dados, file)

import json

def carregar_dados(arquivo):
    try:
        with open(arquivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def validar_entrada(mensagem, tipo, faixa=None):
    while True:
        try:
            entrada = tipo(input(mensagem))
            if faixa and entrada not in faixa:
                raise ValueError
            return entrada
        except ValueError:
            print("Entrada inválida. Por favor, tente novamente.")

def validar_telefone(numero):
    padrao = r"\(\d{2}\)\d{5}-\d{4}"
    return re.fullmatch(padrao, numero) is not None


def menu_principal():
    print("\nSistema de Monitoramento de Saúde do Smartwatch - MediSensi")
    opcoes = ["1. Login", "2. Registrar Novo Usuário", "3. Sair"]
    print("\n".join(opcoes)) 
    return validar_entrada("Escolha uma opção (1-3): ", int, range(1, 4))

def menu_usuario():
    print("\nMenu do Usuário")
    print("1. Monitorar Sinais Vitais")
    print("2. Visualizar Dados de Saúde")
    print("3. Configurar Alertas de Saúde")
    print("4. Feedback do Usuário")
    print("5. Sair")
    return input("Escolha uma opção (1-5): ")


def login(usuarios):
    usuario = input("Nome de usuário: ")
    senha = input("Senha: ")
    if usuario in usuarios and usuarios[usuario]['senha'] == senha:
        print("Login realizado com sucesso!")
        return usuario
    else:
        print("Usuário ou senha incorretos.")
        return None


def registrar_usuario(usuarios):
    usuario = input("Escolha um nome de usuário: ")
    if usuario in usuarios:
        print("Usuário já existe.")
        return None
    senha = input("Escolha uma senha: ")
    
    while True:
        contato_emergencia = input("Contato de emergência (formato (XX)XXXXX-XXXX): ")
        if validar_telefone(contato_emergencia):
            break
        else:
            print("Número de telefone inválido. Por favor, siga o formato (XX)XXXXX-XXXX.")
    
    usuarios[usuario] = {"senha": senha, "contato_emergencia": contato_emergencia}
    print("Usuário registrado com sucesso!")
    return usuario



def gerar_dados_saudaveis(): 
    dados = {
        "FREQUÊNCIA CARDÍACA": random.randint(50, 110), 
        "PRESSÃO SANGUÍNEA": f"{random.randint(100, 140)}/{random.randint(60, 100)}",
        "NÍVEIS DE OXIGÊNIO": random.randint(90, 100), 
        "QUALIDADE DO SONO": random.choice(["Boa", "Normal", "Interrompido"])
    }
    return dados


def monitorar_sinais_vitais(dados_saude, usuario):
    dados = gerar_dados_saudaveis()
    dados_saude[usuario] = dados
    print("Sinais vitais monitorados e armazenados com sucesso.")


def visualizar_dados_saude(dados_saude, usuario):
    if usuario in dados_saude and dados_saude[usuario]:
        print("Dados de Saúde: \n")
        for chave, valor in dados_saude[usuario].items():
            print(f"{chave}: {valor}")
    else:
        print("Nenhum dado de saúde disponível para este usuário.")



def menu_configuracao_alertas():
    print("\nConfiguração de Alertas de Saúde")
    print("1. Definir Limites para Sinais Vitais")
    print("2. Agendar Consultas de Rotina")
    print("3. Voltar")
    return input("Escolha uma opção (1-3): ")


def definir_limites_sinais_vitais(alertas_saude, usuario, limites_sinais_vitais):
    if usuario not in alertas_saude:
        alertas_saude[usuario] = {}
    alertas_saude[usuario]["limites"] = limites_sinais_vitais
    print("Limites definidos com sucesso (com base em seus dados de saúde normais).")


def validar_dia_semana(dia):
    return dia.lower() in ["segunda", "terça", "quarta", "quinta", "sexta"]

def validar_horario(horario):
    padrao = r"\d{2}:\d{2}"
    if re.fullmatch(padrao, horario):
        horas, minutos = map(int, horario.split(":"))
        return 0 <= horas <= 23 and 0 <= minutos <= 59
    return False

def agendar_consultas(alertas_saude, usuario):
    print("Agendando consultas de rotina.")

    while True:
        dia = input("Escolha um dia da semana (Segunda a Sexta): ")
        if validar_dia_semana(dia):
            break
        else:
            print("Dia inválido. Por favor, insira um dia da semana válido (Segunda a Sexta).")

    while True:
        horario = input("Escolha um horário (formato 24h, ex: 14:00): ")
        if validar_horario(horario):
            break
        else:
            print("Horário inválido. Por favor, insira um horário no formato 24h (ex: 14:00).")

    alertas_saude[usuario]["consulta"] = {"dia": dia, "horario": horario}
    print(f"Consulta agendada para {dia} às {horario}h.")

def menu_feedback():
    print("\nFeedback do Usuário")
    print("1. Avaliar Qualidade do Atendimento")
    print("2. Sugerir Melhorias")
    print("3. Voltar")
    return input("Escolha uma opção (1-3): ")


def avaliar_atendimento(feedbacks, usuario):
    if usuario not in feedbacks:
        feedbacks[usuario] = []
    
    print("Por favor, avalie a qualidade do atendimento de 1 a 5 estrelas (onde 5 é excelente):")
    while True:
        try:
            avaliacao = int(input("Sua avaliação (1-5): "))
            if 1 <= avaliacao <= 5:
                break
            else:
                print("Por favor, insira um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    feedbacks[usuario].append(f"Avaliação do Atendimento: {avaliacao} estrelas")
    print("Feedback registrado com sucesso.")




def sugerir_melhorias(feedbacks, usuario):
    if usuario not in feedbacks:
        feedbacks[usuario] = []
    print("Digite sua sugestão para melhorias no sistema ou serviço:")
    sugestao = input()
    feedbacks[usuario].append(f"Sugestão: {sugestao}")
    print("Sua sugestão foi registrada com sucesso.")

def analisar_saude_usuario(dados_usuario):
    feedback = "Sua saúde parece estar em bom estado. Continue monitorando seus sinais vitais."
    
    if dados_usuario.get("FREQUÊNCIA CARDÍACA", 0) not in range(60, 101):
        feedback = "Atenção com sua frequência cardíaca. Considere consultar um médico."

    pressao = dados_usuario.get("PRESSÃO SANGUÍNEA", "120/80").split("/")
    if not (90 <= int(pressao[0]) <= 120 and 60 <= int(pressao[1]) <= 80):
        feedback = "Verifique sua pressão sanguínea. Valores fora do normal podem exigir atenção médica."

    if dados_usuario.get("NÍVEIS DE OXIGÊNIO", 100) < 95:
        feedback = "Seus níveis de oxigênio estão baixos. É recomendável buscar aconselhamento médico."

    if dados_usuario.get("QUALIDADE DO SONO", "") == "Interrompido":
        feedback = "Sua qualidade de sono está interrompida. Tente melhorar suas condições de sono ou procure um especialista."

    return feedback

def feedback_situacao_saude(dados_saude, alertas_saude, usuario):
    print("\nFeedback sobre a Situação de Saúde")

    if usuario in dados_saude:
        feedback_usuario = analisar_saude_usuario(dados_saude[usuario])
        print(feedback_usuario)
    else:
        print("Não há dados de saúde disponíveis para análise.")

    if usuario in alertas_saude and "consulta" in alertas_saude[usuario]:
        consulta = alertas_saude[usuario]["consulta"]
        print(f"Você tem uma consulta agendada para {consulta['dia']} às {consulta['horario']}.")


def principal():
    usuarios = carregar_dados("usuarios.json")
    dados_saude = carregar_dados("dados_saude.json")
    alertas_saude = carregar_dados("alertas_saude.json")
    feedbacks = carregar_dados("feedbacks.json")
    limites_sinais_vitais = ler_limites_csv("limites_sinais_vitais.csv")

    while True:
        escolha_principal = menu_principal()
        if escolha_principal == 1:
            usuario_atual = login(usuarios)
            if usuario_atual:
                while True:
                    escolha_usuario = menu_usuario()
                    if escolha_usuario == '1':
                        monitorar_sinais_vitais(dados_saude, usuario_atual)
                    elif escolha_usuario == '2':
                        visualizar_dados_saude(dados_saude, usuario_atual)
                    elif escolha_usuario == '3':
                        escolha_configuracao = menu_configuracao_alertas()
                        if escolha_configuracao == '1':
                            definir_limites_sinais_vitais(alertas_saude, usuario_atual, limites_sinais_vitais)
                        elif escolha_configuracao == '2':
                            agendar_consultas(alertas_saude, usuario_atual)
                    elif escolha_usuario == '4':
                        escolha_feedback = menu_feedback()
                        if escolha_feedback == '1':
                            avaliar_atendimento(feedbacks, usuario_atual)
                        elif escolha_feedback == '2':
                            sugerir_melhorias(feedbacks, usuario_atual)
                    elif escolha_usuario == '5':
                        feedback_situacao_saude(dados_saude, alertas_saude, usuario_atual)
                        break
        elif escolha_principal == 2:
            novo_usuario = registrar_usuario(usuarios)
            if novo_usuario:
                dados_saude[novo_usuario] = {}
                alertas_saude[novo_usuario] = {}
                feedbacks[novo_usuario] = []
            salvar_dados("usuarios.json", usuarios)
        elif escolha_principal == 3:
            print("Saindo do sistema.")
            break

    salvar_dados("dados_saude.json", dados_saude)
    salvar_dados("alertas_saude.json", alertas_saude)
    salvar_dados("feedbacks.json", feedbacks)

principal()

