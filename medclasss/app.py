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


def main():
    print("=" * 50)
    print("MEDCLASS - SISTEMA DE TRIAGEM DE PACIENTES")
    print("=" * 50)

    nome = input("Nome do paciente: ").strip()

    while True:
        try:
            idade = int(input("Idade do paciente: ").strip())
            if idade < 0:
                print("A idade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Digite uma idade válida.")

    print("\nResponda com s para sim ou n para não.\n")

    febre = perguntar_sim_ou_nao("Paciente está com febre? ")
    falta_ar = perguntar_sim_ou_nao("Paciente está com falta de ar? ")
    dor_peito = perguntar_sim_ou_nao("Paciente está com dor no peito? ")
    saturacao_baixa = perguntar_sim_ou_nao("Paciente está com saturação baixa? ")
    inconsciente = perguntar_sim_ou_nao("Paciente está inconsciente? ")

    risco = classificar_risco(
        idade,
        febre,
        falta_ar,
        dor_peito,
        saturacao_baixa,
        inconsciente
    )

    print("\n" + "=" * 50)
    print("RESULTADO DA TRIAGEM")
    print("=" * 50)
    print(f"Paciente: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Classificação: {risco}")
    print("=" * 50)


if __name__ == "__main__":
    main()
