import math
import os

class FarmTechSolutions:
    def __init__(self):
        # Vetores para armazenar os dados
        self.culturas = []           # Tipo de cultura (Café ou Milho)
        self.areas_plantio = []      # Área calculada em m²
        self.insumos_aplicados = []  # Tipo de insumo usado
        self.quantidades_insumos = [] # Quantidade total necessária
        self.geometrias_areas = []   # Tipo de geometria usada
        self.dimensoes_areas = []    # Dimensões originais da área
        
        print("🌱 Sistema FarmTech Solutions Iniciado!")
        print("Culturas suportadas: Café e Milho")
        print("=" * 50)

    def limpar_tela(self):
        """Limpa a tela do console"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def calcular_area_circular(self, raio):
        """Calcula área circular para plantio de café (plantio em curvas de nível)"""
        area = math.pi * (raio ** 2)
        return round(area, 2)

    def calcular_area_retangular(self, comprimento, largura):
        """Calcula área retangular para plantio de milho (fileiras retas)"""
        area = comprimento * largura
        return round(area, 2)

    def calcular_insumos_cafe(self, area_m2, tipo_insumo):
        """
        Calcula insumos para café
        Fosfato: 800g por m²
        Calcário: 500g por m²  
        Adubo NPK: 300g por m²
        """
        dosagens = {
            "fosfato": 0.8,      # 800g/m² = 0.8 kg/m²
            "calcario": 0.5,     # 500g/m² = 0.5 kg/m²
            "adubo_npk": 0.3     # 300g/m² = 0.3 kg/m²
        }
        
        if tipo_insumo.lower() in dosagens:
            quantidade_kg = area_m2 * dosagens[tipo_insumo.lower()]
            return round(quantidade_kg, 2)
        return 0

    def calcular_insumos_milho(self, area_m2, ruas_lavoura, tipo_insumo):
        """
        Calcula insumos para milho considerando número de ruas
        Herbicida: 500mL por metro de rua
        Fertilizante: 200g por metro de rua
        Defensivo: 300mL por metro de rua
        """
        # Estimativa de metros de rua baseada na área e número de ruas
        if ruas_lavoura > 0:
            metros_por_rua = math.sqrt(area_m2) / ruas_lavoura * 10  # Estimativa
            metros_totais = metros_por_rua * ruas_lavoura
        else:
            metros_totais = 0

        dosagens = {
            "herbicida": 0.5,      # 500mL/metro = 0.5L/metro
            "fertilizante": 0.2,   # 200g/metro = 0.2 kg/metro  
            "defensivo": 0.3       # 300mL/metro = 0.3L/metro
        }
        
        if tipo_insumo.lower() in dosagens:
            quantidade_total = metros_totais * dosagens[tipo_insumo.lower()]
            return round(quantidade_total, 2), round(metros_totais, 2)
        return 0, 0

    def entrada_dados(self):
        """Função para entrada de novos dados"""
        self.limpar_tela()
        print("=" * 60)
        print("           🌱 ENTRADA DE DADOS - NOVA CULTURA")
        print("=" * 60)
        
        print("\nTipos de culturas disponíveis:")
        print("1. ☕ Café (Área Circular - Plantio em curvas de nível)")
        print("2. 🌽 Milho (Área Retangular - Fileiras retas)")
        
        try:
            opcao_cultura = int(input("\nEscolha a cultura (1 ou 2): "))
            
            if opcao_cultura == 1:
                # CAFÉ - Área circular
                print("\n--- PLANTIO DE CAFÉ (Área Circular) ---")
                raio = float(input("Digite o raio da área de plantio (metros): "))
                area = self.calcular_area_circular(raio)
                cultura = "Café"
                geometria = "Circular"
                dimensoes = f"Raio: {raio}m"
                
                print(f"\n📏 Área calculada: {area} m²")
                print("\nInsumos disponíveis para CAFÉ:")
                print("1. Fosfato (800g/m²)")
                print("2. Calcário (500g/m²)")
                print("3. Adubo NPK (300g/m²)")
                
                opcao_insumo = int(input("\nEscolha o insumo (1, 2 ou 3): "))
                insumos_cafe = ["fosfato", "calcario", "adubo_npk"]
                insumos_nomes = ["Fosfato", "Calcário", "Adubo NPK"]
                
                if 1 <= opcao_insumo <= 3:
                    insumo_escolhido = insumos_cafe[opcao_insumo - 1]
                    nome_insumo = insumos_nomes[opcao_insumo - 1]
                    quantidade = self.calcular_insumos_cafe(area, insumo_escolhido)
                    
                    print(f"\n✅ RESULTADO DO CÁLCULO:")
                    print(f"Insumo: {nome_insumo}")
                    print(f"Quantidade necessária: {quantidade} kg")
                else:
                    print("❌ Opção de insumo inválida!")
                    return
                    
            elif opcao_cultura == 2:
                # MILHO - Área retangular  
                print("\n--- PLANTIO DE MILHO (Área Retangular) ---")
                comprimento = float(input("Digite o comprimento da lavoura (metros): "))
                largura = float(input("Digite a largura da lavoura (metros): "))
                ruas = int(input("Digite o número de ruas da lavoura: "))
                
                area = self.calcular_area_retangular(comprimento, largura)
                cultura = "Milho"
                geometria = "Retangular"
                dimensoes = f"{comprimento}m x {largura}m ({ruas} ruas)"
                
                print(f"\n📏 Área calculada: {area} m²")
                print("\nInsumos disponíveis para MILHO:")
                print("1. Herbicida (500mL/metro de rua)")
                print("2. Fertilizante (200g/metro de rua)")
                print("3. Defensivo (300mL/metro de rua)")
                
                opcao_insumo = int(input("\nEscolha o insumo (1, 2 ou 3): "))
                insumos_milho = ["herbicida", "fertilizante", "defensivo"]
                insumos_nomes = ["Herbicida", "Fertilizante", "Defensivo"]
                
                if 1 <= opcao_insumo <= 3:
                    insumo_escolhido = insumos_milho[opcao_insumo - 1]
                    nome_insumo = insumos_nomes[opcao_insumo - 1]
                    quantidade, metros_totais = self.calcular_insumos_milho(area, ruas, insumo_escolhido)
                    
                    print(f"\n✅ RESULTADO DO CÁLCULO:")
                    print(f"Metros totais de ruas: {metros_totais} m")
                    print(f"Insumo: {nome_insumo}")
                    if "herbicida" in insumo_escolhido or "defensivo" in insumo_escolhido:
                        print(f"Quantidade necessária: {quantidade} litros")
                    else:
                        print(f"Quantidade necessária: {quantidade} kg")
                else:
                    print("❌ Opção de insumo inválida!")
                    return
            else:
                print("❌ Opção de cultura inválida!")
                return
            
            # Armazenar nos vetores
            self.culturas.append(cultura)
            self.areas_plantio.append(area)
            self.insumos_aplicados.append(nome_insumo)
            self.quantidades_insumos.append(quantidade)
            self.geometrias_areas.append(geometria)
            self.dimensoes_areas.append(dimensoes)
            
            print(f"\n🎉 DADOS SALVOS COM SUCESSO!")
            print(f"Registro #{len(self.culturas)} adicionado ao sistema.")
            
        except ValueError:
            print("❌ Erro: Por favor, digite apenas números válidos!")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
        
        input("\nPressione ENTER para voltar ao menu...")

    def saida_dados(self):
        """Exibe todos os dados cadastrados"""
        self.limpar_tela()
        print("=" * 80)
        print("               📊 RELATÓRIO COMPLETO - CULTURAS CADASTRADAS")
        print("=" * 80)
        
        if len(self.culturas) == 0:
            print("\n❌ Nenhuma cultura cadastrada ainda!")
            print("💡 Use a opção 1 do menu para adicionar culturas.")
        else:
            print(f"\n📈 Total de registros: {len(self.culturas)}")
            print("\n" + "=" * 80)
            
            for i in range(len(self.culturas)):
                print(f"\n🔸 REGISTRO #{i+1}")
                print(f"   Cultura: {self.culturas[i]}")
                print(f"   Geometria: {self.geometrias_areas[i]}")
                print(f"   Dimensões: {self.dimensoes_areas[i]}")
                print(f"   Área de plantio: {self.areas_plantio[i]} m²")
                print(f"   Insumo aplicado: {self.insumos_aplicados[i]}")
                
                # Definir unidade baseada no tipo de insumo
                if self.culturas[i] == "Café":
                    unidade = "kg"
                else:  # Milho
                    if "Fertilizante" in self.insumos_aplicados[i]:
                        unidade = "kg"
                    else:
                        unidade = "litros"
                
                print(f"   Quantidade necessária: {self.quantidades_insumos[i]} {unidade}")
                print("-" * 50)
            
            # Estatísticas resumidas
            area_total = sum(self.areas_plantio)
            print(f"\n📊 RESUMO ESTATÍSTICO:")
            print(f"   🌱 Área total plantada: {area_total} m²")
            print(f"   ☕ Registros de Café: {self.culturas.count('Café')}")
            print(f"   🌽 Registros de Milho: {self.culturas.count('Milho')}")
        
        input("\nPressione ENTER para voltar ao menu...")

    def atualizar_dados(self):
        """Atualiza dados em uma posição específica do vetor"""
        self.limpar_tela()
        print("=" * 60)
        print("            ✏️ ATUALIZAÇÃO DE DADOS")
        print("=" * 60)
        
        if len(self.culturas) == 0:
            print("\n❌ Nenhuma cultura cadastrada para atualizar!")
            print("💡 Use a opção 1 do menu para adicionar culturas primeiro.")
            input("\nPressione ENTER para voltar ao menu...")
            return
        
        # Mostrar registros disponíveis
        print(f"\nRegistros disponíveis para atualização:")
        print("-" * 50)
        for i in range(len(self.culturas)):
            print(f"{i+1}. {self.culturas[i]} - {self.areas_plantio[i]} m² - {self.insumos_aplicados[i]}")
        
        try:
            posicao = int(input(f"\nDigite o número do registro a atualizar (1 a {len(self.culturas)}): "))
            
            if 1 <= posicao <= len(self.culturas):
                indice = posicao - 1  # Converter para índice do vetor
                
                print(f"\n--- ATUALIZANDO REGISTRO #{posicao} ---")
                print(f"Cultura atual: {self.culturas[indice]}")
                print(f"Área atual: {self.areas_plantio[indice]} m²")
                print(f"Insumo atual: {self.insumos_aplicados[indice]}")
                
                print("\nO que deseja atualizar?")
                print("1. Apenas as dimensões da área")
                print("2. Apenas o tipo de insumo")
                print("3. Ambos (área e insumo)")
                
                opcao_atualizacao = int(input("Escolha (1, 2 ou 3): "))
                
                if opcao_atualizacao in [1, 3]:  # Atualizar área
                    if self.culturas[indice] == "Café":
                        novo_raio = float(input("Digite o novo raio (metros): "))
                        nova_area = self.calcular_area_circular(novo_raio)
                        self.areas_plantio[indice] = nova_area
                        self.dimensoes_areas[indice] = f"Raio: {novo_raio}m"
                    else:  # Milho
                        novo_comprimento = float(input("Digite o novo comprimento (metros): "))
                        nova_largura = float(input("Digite a nova largura (metros): "))
                        novas_ruas = int(input("Digite o novo número de ruas: "))
                        nova_area = self.calcular_area_retangular(novo_comprimento, nova_largura)
                        self.areas_plantio[indice] = nova_area
                        self.dimensoes_areas[indice] = f"{novo_comprimento}m x {nova_largura}m ({novas_ruas} ruas)"
                
                if opcao_atualizacao in [2, 3]:  # Atualizar insumo
                    if self.culturas[indice] == "Café":
                        print("\nNovos insumos para CAFÉ:")
                        print("1. Fosfato (800g/m²)")
                        print("2. Calcário (500g/m²)")
                        print("3. Adubo NPK (300g/m²)")
                        
                        nova_opcao = int(input("Escolha o novo insumo (1, 2 ou 3): "))
                        insumos_cafe = ["fosfato", "calcario", "adubo_npk"]
                        nomes_cafe = ["Fosfato", "Calcário", "Adubo NPK"]
                        
                        if 1 <= nova_opcao <= 3:
                            novo_insumo = insumos_cafe[nova_opcao - 1]
                            nome_novo_insumo = nomes_cafe[nova_opcao - 1]
                            nova_quantidade = self.calcular_insumos_cafe(self.areas_plantio[indice], novo_insumo)
                            
                            self.insumos_aplicados[indice] = nome_novo_insumo
                            self.quantidades_insumos[indice] = nova_quantidade
                    
                    else:  # Milho
                        print("\nNovos insumos para MILHO:")
                        print("1. Herbicida (500mL/metro de rua)")
                        print("2. Fertilizante (200g/metro de rua)")
                        print("3. Defensivo (300mL/metro de rua)")
                        
                        nova_opcao = int(input("Escolha o novo insumo (1, 2 ou 3): "))
                        ruas_atuais = int(self.dimensoes_areas[indice].split("(")[1].split(" ruas")[0])
                        
                        insumos_milho = ["herbicida", "fertilizante", "defensivo"]
                        nomes_milho = ["Herbicida", "Fertilizante", "Defensivo"]
                        
                        if 1 <= nova_opcao <= 3:
                            novo_insumo = insumos_milho[nova_opcao - 1]
                            nome_novo_insumo = nomes_milho[nova_opcao - 1]
                            nova_quantidade, _ = self.calcular_insumos_milho(self.areas_plantio[indice], ruas_atuais, novo_insumo)
                            
                            self.insumos_aplicados[indice] = nome_novo_insumo
                            self.quantidades_insumos[indice] = nova_quantidade
                
                print(f"\n✅ REGISTRO #{posicao} ATUALIZADO COM SUCESSO!")
                
            else:
                print("❌ Número de registro inválido!")
        
        except ValueError:
            print("❌ Erro: Digite apenas números válidos!")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
        
        input("\nPressione ENTER para voltar ao menu...")

    def deletar_dados(self):
        """Remove dados de uma posição específica do vetor"""
        self.limpar_tela()
        print("=" * 60)
        print("             🗑️ EXCLUSÃO DE DADOS")
        print("=" * 60)
        
        if len(self.culturas) == 0:
            print("\n❌ Nenhuma cultura cadastrada para excluir!")
            print("💡 Use a opção 1 do menu para adicionar culturas primeiro.")
            input("\nPressione ENTER para voltar ao menu...")
            return
        
        # Mostrar registros disponíveis
        print(f"\nRegistros disponíveis para exclusão:")
        print("-" * 50)
        for i in range(len(self.culturas)):
            print(f"{i+1}. {self.culturas[i]} - {self.areas_plantio[i]} m² - {self.insumos_aplicados[i]}")
        
        try:
            posicao = int(input(f"\nDigite o número do registro a excluir (1 a {len(self.culturas)}): "))
            
            if 1 <= posicao <= len(self.culturas):
                indice = posicao - 1  # Converter para índice do vetor
                
                # Mostrar dados que serão excluídos
                print(f"\n⚠️ CONFIRMAÇÃO DE EXCLUSÃO:")
                print(f"   Registro #{posicao}")
                print(f"   Cultura: {self.culturas[indice]}")
                print(f"   Área: {self.areas_plantio[indice]} m²")
                print(f"   Insumo: {self.insumos_aplicados[indice]}")
                print(f"   Quantidade: {self.quantidades_insumos[indice]}")
                
                confirmacao = input("\n❓ Tem certeza que deseja excluir este registro? (S/N): ").upper()
                
                if confirmacao == 'S':
                    # Remover dados de todos os vetores na mesma posição
                    cultura_removida = self.culturas.pop(indice)
                    self.areas_plantio.pop(indice)
                    self.insumos_aplicados.pop(indice)
                    self.quantidades_insumos.pop(indice)
                    self.geometrias_areas.pop(indice)
                    self.dimensoes_areas.pop(indice)
                    
                    print(f"\n✅ Registro de {cultura_removida} excluído com sucesso!")
                    print(f"📊 Total de registros restantes: {len(self.culturas)}")
                else:
                    print("\n❌ Exclusão cancelada!")
            else:
                print("❌ Número de registro inválido!")
        
        except ValueError:
            print("❌ Erro: Digite apenas números válidos!")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
        
        input("\nPressione ENTER para voltar ao menu...")

    def menu_principal(self):
        """Menu principal com loop de navegação"""
        while True:  # Loop principal do programa
            self.limpar_tela()
            print("=" * 60)
            print("        🌱 FARMTECH SOLUTIONS - V2.0")
            print("          Sistema de Agricultura Digital")
            print("=" * 60)
            print("                 MENU PRINCIPAL")
            print("-" * 60)
            print("1. 📊 Entrada de Dados (Cadastrar nova cultura)")
            print("2. 📋 Saída de Dados (Ver relatório completo)")
            print("3. ✏️  Atualização de Dados (Modificar registro)")
            print("4. 🗑️  Exclusão de Dados (Remover registro)")
            print("5. 🚪 Sair do Programa")
            print("=" * 60)
            print(f"📈 Registros atuais: {len(self.culturas)}")
            print("=" * 60)
            
            try:
                opcao = int(input("Digite sua escolha (1 a 5): "))
                
                # Estrutura de decisão para o menu
                if opcao == 1:
                    self.entrada_dados()
                elif opcao == 2:
                    self.saida_dados()
                elif opcao == 3:
                    self.atualizar_dados()
                elif opcao == 4:
                    self.deletar_dados()
                elif opcao == 5:
                    self.limpar_tela()
                    print("=" * 60)
                    print("        🎉 OBRIGADO POR USAR FARMTECH!")
                    print("      Sistema desenvolvido para FIAP 2024")
                    print("        Agricultura Digital do Futuro")
                    print("=" * 60)
                    break  # Sai do loop while, encerrando o programa
                else:
                    print("❌ Opção inválida! Digite um número de 1 a 5.")
                    input("Pressione ENTER para tentar novamente...")
            
            except ValueError:
                print("❌ Erro: Digite apenas números inteiros!")
                input("Pressione ENTER para tentar novamente...")
            except KeyboardInterrupt:
                print("\n\n🛑 Programa interrompido pelo usuário.")
                print("Até mais!")
                break

# Função principal para iniciar o sistema
def main():
    """Função principal que inicia o sistema FarmTech"""
    print("🚀 Iniciando Sistema FarmTech Solutions...")
    sistema_farmtech = FarmTechSolutions()
    sistema_farmtech.menu_principal()

# Executa o programa se este arquivo for executado diretamente
if __name__ == "__main__":
    main()