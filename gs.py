import random

def menu_principal():
    print("\nSistema de Monitoramento de Saúde do Smartwatch")
    print("1. Login")
    print("2. Registrar Novo Usuário")
    print("3. Sair")
    return input("Escolha uma opção (1-3): ")


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
    contato_emergencia = input("Contato de emergência: ")
    usuarios[usuario] = {"senha": senha, "contato_emergencia": contato_emergencia}
    print("Usuário registrado com sucesso!")
    return usuario


def gerar_dados_saudaveis():
    dados = {
        "frequencia_cardiaca": random.randint(60, 100),  # bpm
        "pressao_sanguinea": f"{random.randint(110, 130)}/{random.randint(70, 90)}",  # mmHg
        "niveis_oxigenio": random.randint(95, 100),  # %
        "qualidade_sono": random.choice(["Boa", "Normal", "Interrompido"])
    }
    return dados


def monitorar_sinais_vitais(dados_saude, usuario):
    dados = gerar_dados_saudaveis()
    dados_saude[usuario] = dados
    print("Sinais vitais monitorados e armazenados com sucesso.")


def visualizar_dados_saude(dados_saude, usuario):
    if usuario in dados_saude:
        print("Dados de Saúde:")
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


def definir_limites_sinais_vitais(alertas_saude, usuario):
    """
    Definir limites personalizados para sinais vitais.
    """
    print("Definindo limites para sinais vitais (função simulada).")
    alertas_saude[usuario]["limites"] = {"frequencia_cardiaca": (60, 100)}
    print("Limites definidos com sucesso.")


def agendar_consultas(alertas_saude, usuario):
    """
    Agendar consultas de rotina.
    """
    print("Agendando consultas de rotina.")
    dia = input("Escolha um dia da semana (Segunda a Sexta): ")
    horario = input("Escolha um horário (formato 24h, ex: 14:00): ")
    alertas_saude[usuario]["consulta"] = {"dia": dia, "horario": horario}
    print(f"Consulta agendada para {dia} às {horario}.")


def menu_feedback():
    print("\nFeedback do Usuário")
    print("1. Avaliar Qualidade do Atendimento")
    print("2. Sugerir Melhorias")
    print("3. Voltar")
    return input("Escolha uma opção (1-3): ")


def avaliar_atendimento(feedbacks, usuario):
    print("Avaliando qualidade do atendimento (função simulada).")
    feedbacks[usuario].append("Atendimento bom.")
    print("Feedback registrado com sucesso.")


def sugerir_melhorias(feedbacks, usuario):
    print("Digite sua sugestão para melhorias no sistema ou serviço:")
    sugestao = input()
    feedbacks[usuario].append(f"Sugestão: {sugestao}")
    print("Sua sugestão foi registrada com sucesso.")


def feedback_situacao_saude(dados_saude, alertas_saude, usuario):
    print("\nFeedback sobre a Situação de Saúde")
    print("Sua saúde está em bom estado. Continue monitorando seus sinais vitais.")

    if "consulta" in alertas_saude[usuario]:
        consulta = alertas_saude[usuario]["consulta"]
        print(f"Você tem uma consulta agendada para {consulta['dia']} às {consulta['horario']}.")


def principal():
    usuarios = {}
    dados_saude = {}
    alertas_saude = {}
    feedbacks = {}

    while True:
        escolha_principal = menu_principal()
        if escolha_principal == '1':
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
                            definir_limites_sinais_vitais(alertas_saude, usuario_atual)
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
        elif escolha_principal == '2':
            novo_usuario = registrar_usuario(usuarios)
            if novo_usuario:
                dados_saude[novo_usuario] = {}
                alertas_saude[novo_usuario] = {}
                feedbacks[novo_usuario] = []
        elif escolha_principal == '3':
            print("Saindo do sistema.")
            break


principal()
