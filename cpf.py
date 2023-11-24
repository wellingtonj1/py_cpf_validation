def valida_cpf(cpf):
    soma_decimo = 0
    
    for i in range(10, 1, -1):
        soma_decimo += i * int(cpf[10-i])
        
    if soma_decimo % 11 < 2:
        if int(cpf[9]) != 0:
            return False
    else:
        if 11 - (soma_decimo % 11) != int(cpf[9]):
            return False
    
    soma_decimo_primeiro = 0
    for i in range(11, 1, -1):
        soma_decimo_primeiro += i * int(cpf[11-i])
    
    if soma_decimo_primeiro % 11 < 2:
        if int(cpf[10]) != 0:
            return False
    else:
        if 11 - (soma_decimo_primeiro % 11) != int(cpf[10]):
            return False
    
    if len(set(cpf)) == 1:
        return False
    
    return True

cpf = input("digite o cpf: ")
if valida_cpf(cpf):
    print("cpf valido")
else:
    print("cpf invalido")