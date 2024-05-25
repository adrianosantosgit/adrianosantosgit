from os import system

system('clear')

def entrar_hora ():
    while True:

        entrada = input().lower()

        if codigo == "s":
            print("Saindo do programa...")
            exit()
        # Verifique se a entrada tem 3 ou 4 dígitos
        elif len(entrada) not in (3, 4):
            if entrada == "s":
                    print("Saindo do programa...")
                    exit()
            else:
                print("Entrada inválida:", entrada)
                print("Entrada inválida. Digite 3 ou 4 dígitos.")
            break  # Sai do loop quando a entrada é válida
        else:
            # Obtenha a hora e os minutos
            if len(entrada) == 3:
                hora = int(entrada[:1])
                minutos = int(entrada[1:])
            else:
                hora = int(entrada[:2])
                minutos = int(entrada[2:])

            # Verifique os limites
            while True:
                if hora > 23 or minutos > 59:
                    if entrada == "s":
                        print("Saindo do programa...")
                        exit()
                    print("Entrada inválida:", entrada)
                    print("Hora ou minutos fora dos limites.")
                    print("Digite o horário, hora e os minutos (sem separador : ) ou (s) para sair: ")
                # print(f"Substituido por: XXX")
                # return "XXX"
                
                else:
                # Exiba a hora e os minutos com separador
                    return f"{hora:02d}:{minutos:02d}"

                break  # Sai do loop quando a entrada é válida

# Solicita ao usuário o código e o horário inicial
codigo = input("Digite o código da posição ou (s) para sair: ").lower()
if codigo == "s":
    print("Saindo do programa...")
    exit()

print("Digite o horário do chamado, hora e os minutos (sem separador : ) ou (s) para sair: ")
horario_chamado = entrar_hora()

print("Digite o horário do inicio, hora e os minutos (sem separador : ) ou (s) para sair: ")
horario_inicio = entrar_hora()

print("Digite o horário do término, hora e os minutos (sem separador : ) ou (s) para sair: ")
horario_termino = entrar_hora()

fato = input("Descreva o fato: ").capitalize()
causa = input("Descreva a causa: ").capitalize()
acao = input("Descreva a ação: ").capitalize()

print("\n")

print(f"*LOCAL:*", codigo.upper(),"\n\n*CHAMADO*", horario_chamado, "\n*INÍCIO:*", horario_inicio, "\n*TERMINO:*", horario_termino, "\n")

print("*FATO:* ",fato + ".\n")

print("*CAUSA:* ",causa + ".\n")

print("*AÇÃO:* ",acao + ".")


# equipamentos = {
#         "a02": "A02", "a04": A04, "a06": A06, "a08": A08,
#         "b07": B07, "b09": B09, "b11": B11, "b13": B13,
#         "b02": B02, "b04": B04, "b06": B06, "b08": B08, "b10": B10, "b12": B12, "b14": B14,
#         "c05": C05, "c07": C07, "c09": C09, "c11": C11, "c13": C13, "c15": C15,
#         "c02": C02, "c04": C04, "c06": C06, "c08": C08, "c10": C10, "c12": C12, "c14": C14,
#         # Adicione mais códigos e instâncias de Equipamento conforme necessário
#     }