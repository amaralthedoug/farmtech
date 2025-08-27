# Programa para FarmTech Solutions: Aplicação de Agricultura Digital
# Suporte a 2 culturas: Soja e Milho (principais no estado de Mato Grosso, por exemplo)
# Cálculo de área: Assumimos áreas retangulares para simplicidade (comprimento x largura)
# Manejo de insumos: Para Soja, aplicação de fosfato a 500 mL por metro quadrado
# Para Milho, aplicação de inseticida a 300 mL por metro quadrado
# Dados armazenados em uma lista de dicionários (vetor)
# Menu com opções usando loops e decisões

import math  # Para cálculos matemáticos, se necessário (não usado aqui, mas pronto para expansão)

# Vetor principal para armazenar os dados das plantações
plantacoes = []

def calcular_area_retangular(comprimento, largura):
    """Função para calcular área retangular"""
    return comprimento * largura

def calcular_insumos(cultura, area):
    """Função para calcular quantidade de insumos baseada na cultura e área"""
    if cultura.lower() == 'soja':
        # 500 mL por m² para fosfato na soja
        quantidade_por_m2 = 500
        insumo = 'Fosfato'
    elif cultura.lower() == 'milho':
        # 300 mL por m² para inseticida no milho
        quantidade_por_m2 = 300
        insumo = 'Inseticida'
    else:
        return None, 0  # Cultura inválida
    
    total_insumo = (quantidade_por_m2 * area) / 1000  # Convertendo mL para Litros
    return insumo, total_insumo

def entrada_dados():
    """Opção 1: Entrada de dados"""
    print("\nEntrada de Dados para Nova Plantação")
    cultura = input("Digite a cultura (Soja ou Milho): ").strip()
    if cultura.lower() not in ['soja', 'milho']:
        print("Cultura inválida! Apenas Soja ou Milho são suportados.")
        return
    
    comprimento = float(input("Digite o comprimento da área (em metros): "))
    largura = float(input("Digite a largura da área (em metros): "))
    
    area = calcular_area_retangular(comprimento, largura)
    insumo, total_insumo = calcular_insumos(cultura, area)
    
    if insumo is None:
        print("Erro no cálculo de insumos.")
        return
    
    # Adiciona ao vetor
    plantacoes.append({
        'cultura': cultura,
        'comprimento': comprimento,
        'largura': largura,
        'area': area,
        'insumo': insumo,
        'total_insumo_litros': total_insumo
    })
    print("Dados inseridos com sucesso!")

def saida_dados():
    """Opção 2: Saída de dados"""
    if not plantacoes:
        print("\nNenhuma plantação cadastrada.")
        return
    
    print("\nLista de Planticações:")
    for i, plantacao in enumerate(plantacoes):
        print(f"Plantação {i+1}:")
        print(f"  Cultura: {plantacao['cultura']}")
        print(f"  Área: {plantacao['area']} m² (Comprimento: {plantacao['comprimento']}m, Largura: {plantacao['largura']}m)")
        print(f"  Insumo: {plantacao['insumo']}")
        print(f"  Total de Insumo Necessário: {plantacao['total_insumo_litros']:.2f} Litros")
        print("---")

def atualizacao_dados():
    """Opção 3: Atualização de dados"""
    if not plantacoes:
        print("\nNenhuma plantação para atualizar.")
        return
    
    posicao = int(input("\nDigite o número da plantação a atualizar (1 a {len(plantacoes)}): ")) - 1
    if posicao < 0 or posicao >= len(plantacoes):
        print("Posição inválida!")
        return
    
    print("Atualizando Plantação {posicao+1}")
    cultura = input("Nova cultura (Soja ou Milho, ou ENTER para manter): ").strip()
    if cultura:
        if cultura.lower() not in ['soja', 'milho']:
            print("Cultura inválida! Mantendo a atual.")
        else:
            plantacoes[posicao]['cultura'] = cultura
    
    comprimento_str = input("Novo comprimento (em metros, ou ENTER para manter): ").strip()
    if comprimento_str:
        plantacoes[posicao]['comprimento'] = float(comprimento_str)
    
    largura_str = input("Nova largura (em metros, ou ENTER para manter): ").strip()
    if largura_str:
        plantacoes[posicao]['largura'] = float(largura_str)
    
    # Recalcula área e insumos
    area = calcular_area_retangular(plantacoes[posicao]['comprimento'], plantacoes[posicao]['largura'])
    insumo, total_insumo = calcular_insumos(plantacoes[posicao]['cultura'], area)
    
    plantacoes[posicao]['area'] = area
    plantacoes[posicao]['insumo'] = insumo
    plantacoes[posicao]['total_insumo_litros'] = total_insumo
    
    print("Dados atualizados com sucesso!")

def delecao_dados():
    """Opção 4: Deleção de dados"""
    if not plantacoes:
        print("\nNenhuma plantação para deletar.")
        return
    
    posicao = int(input("\nDigite o número da plantação a deletar (1 a {len(plantacoes)}): ")) - 1
    if posicao < 0 or posicao >= len(plantacoes):
        print("Posição inválida!")
        return
    
    del plantacoes[posicao]
    print("Plantação deletada com sucesso!")

def menu():
    """Menu principal com loop"""
    while True:
        print("\nMenu FarmTech Solutions")
        print("1. Entrada de Dados")
        print("2. Saída de Dados")
        print("3. Atualização de Dados")
        print("4. Deleção de Dados")
        print("5. Sair do Programa")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            entrada_dados()
        elif opcao == '2':
            saida_dados()
        elif opcao == '3':
            atualizacao_dados()
        elif opcao == '4':
            delecao_dados()
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Inicia o programa
if __name__ == "__main__":
    menu()