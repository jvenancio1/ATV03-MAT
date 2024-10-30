def avaliar_evento(pessoa1_presente, pessoa2_presente, traz_item):
    """Avalia se o evento será animado com base na presença de Pessoa1, Pessoa2 e se alguém traz um item."""
    evento_animado = (pessoa1_presente and pessoa2_presente) or (not pessoa1_presente and traz_item)
    return evento_animado

def exibir_tabela():
    """Exibe a tabela verdade das proposições."""
    print("Tabela Verdade:")
    print("Pessoa1 | Pessoa2 | Item | Evento Animado")
    print("--------|---------|------|---------------")
    for pessoa1 in [True, False]:
        for pessoa2 in [True, False]:
            for item in [True, False]:
                resultado_evento = avaliar_evento(pessoa1, pessoa2, item)
                print(f"{'Sim' if pessoa1 else 'Não'} | {'Sim' if pessoa2 else 'Não'} | {'Sim' if item else 'Não'} | {'Sim' if resultado_evento else 'Não'}")
    print()

def capturar_input(mensagem):
    """Captura e valida a entrada do usuário."""
    while True:
        resposta = input(mensagem)
        if resposta == "!s":
            print("Saindo do programa. Obrigado pela participação.")
            exit()
        if resposta not in ["S", "N"]:
            print("Digite apenas 'S' ou 'N'. Para sair, digite '!s'.")
            continue
        return resposta == "S"

def rodar_programa():
    """Executa o programa principal."""
    exibir_tabela()
    
    while True:
        print("\nPara sair, digite '!s' quando solicitado.")
        
        pessoa1 = capturar_input("Pessoa1 está presente? (S ou N): ")
        pessoa2 = capturar_input("Pessoa2 está presente? (S ou N): ")
        item = capturar_input("Alguém traz o item? (S ou N): ")

        evento = avaliar_evento(pessoa1, pessoa2, item)
        
        print("\nResultado:")
        print(f"Pessoa1: {'Sim' if pessoa1 else 'Não'} | Pessoa2: {'Sim' if pessoa2 else 'Não'} | Item: {'Sim' if item else 'Não'} | Evento: {'Sim' if evento else 'Não'}")

        # Pergunta se o usuário quer testar outro cenário
        continuar = input("\nDeseja testar outro cenário? (S para Sim, N para Não): ")
        if continuar.upper() == "N":
            print("Encerrando o programa.")
            break

if __name__ == "__main__":
    rodar_programa()
