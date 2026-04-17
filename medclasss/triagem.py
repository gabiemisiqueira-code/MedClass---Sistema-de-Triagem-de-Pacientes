def classificar_risco(idade, febre, falta_ar, dor_peito, saturacao_baixa, inconsciente):
    if inconsciente or saturacao_baixa or dor_peito and falta_ar:
        return "VERMELHO - atendimento imediato"

    if falta_ar or dor_peito or febre and idade >= 60:
        return "AMARELO - atendimento urgente"

    return "VERDE - pode aguardar atendimento"
