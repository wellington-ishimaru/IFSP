# -*- coding: UTF-8 -*-
print("******************************")
print(" Venda de passagens de ônibus ")
print("******************************\n")

poltrona_janela_esq = [0 for x in range(0, 12)]
poltrona_corredor_esq = [0 for x in range(0, 12)]
poltrona_janela_dir = [0 for x in range(0, 12)]
poltrona_corredor_dir = [0 for x in range(0, 12)]
vagas = 48
escolha = 1
while vagas != 0 and escolha != 0:
    print("1 - Venda de passagem.")
    print("2 - Mapa de ocupação.")
    print("0 - Sair.")

    escolha = int(input("Escolha a opção desejada: "))

    if escolha == 1:
        print("\n>>>>>>>>>> Venda de passagens <<<<<<<<<<\n")
        escolha_jan_corr = int(input("Escolha 1 para janela e 2 para corredor: "))
        escolha_num_poltrona = int(input("Escolha o número da poltrona de 1 a 12: "))
        if escolha_jan_corr == 1:
            if poltrona_janela_dir[escolha_num_poltrona - 1] == 0:
                poltrona_janela_dir[escolha_num_poltrona - 1] = 1
                print("Venda efetivada.")
                vagas -= 1
            elif poltrona_janela_esq[escolha_num_poltrona - 1] == 0:
                poltrona_janela_esq[escolha_num_poltrona - 1] = 1
                print("Venda efetivada.")
                vagas -= 1
            else:
                print("\nPoltrona ocupada.")
        if escolha_jan_corr == 2:
            if poltrona_corredor_dir[escolha_num_poltrona - 1] == 0:
                poltrona_corredor_dir[escolha_num_poltrona - 1] = 1
                print("Venda efetivada.")
                vagas -= 1
            elif poltrona_corredor_esq[escolha_num_poltrona - 1] == 0:
                poltrona_corredor_esq[escolha_num_poltrona - 1] = 1
                print("Venda efetivada.")
                vagas -= 1
            else:
                print("\nPoltrona ocupada.")
        print(f"Restam {vagas} \n")

    if escolha == 2:
        print("\n")
        print(poltrona_janela_esq)
        print(poltrona_corredor_esq, "\n")
        print(poltrona_corredor_dir)
        print(poltrona_janela_dir, "\n")

print("Ônibus lotado.")



