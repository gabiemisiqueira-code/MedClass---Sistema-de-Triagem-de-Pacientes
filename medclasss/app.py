from triagem import classificar_risco


def perguntar_sim_ou_nao(pergunta):
    while True:
        resposta = input(pergunta).strip().lower()

        if resposta in ["s", "sim"]:
            return True
        elif resposta in ["n", "nao", "não"]:
            return False
        else:
            print("Resposta inválida. Digite apenas: s ou n.")


def salvar_paciente(nome, idade, risco):
    with open("pacientes.txt", "a") as arquivo:
        arquivo.write(f"{nome} | {idade} anos | {risco}\n")


def listar_pacientes():
    print("\n=== PACIENTES CADASTRADOS ===")

    try:
        with open("pacientes.txt", "r") as arquivo:
            dados = arquivo.readlines()

            if not dados:
                print("Nenhum paciente cadastrado.")
            else:
                for paciente in dados:
                    print(paciente.strip())
    except FileNotFoundError:
        print("Arquivo não encontrado.")


def nova_triagem():
    print("\n=== NOVA TRIAGEM ===")

    nome = input("Nome do paciente: ").strip()

    while True:
        try:
            idade = int(input("Idade: "))
            break
        except:
            print("Digite um número válido.")

    febre = perguntar_sim_ou_nao("Febre? ")
    falta_ar = perguntar_sim_ou_nao("Falta de ar? ")
    dor_peito = perguntar_sim_ou_nao("Dor no peito? ")
    saturacao_baixa = perguntar_sim_ou_nao("Saturação baixa? ")
    inconsciente = perguntar_sim_ou_nao("Inconsciente? ")

    risco = classificar_risco(
        idade,
        febre,
        falta_ar,
        dor_peito,
        saturacao_baixa,
        inconsciente
    )

    print(f"\nClassificação: {risco}")
    salvar_paciente(nome, idade, risco)


def main():
    while True:
        print("\n" + "=" * 40)
        print("MEDCLASS - MENU")
        print("=" * 40)
        print("1 - Nova triagem")
        print("2 - Ver pacientes")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nova_triagem()
        elif opcao == "2":
            listar_pacientes()
        elif opcao == "3":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
