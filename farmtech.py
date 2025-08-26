#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

cana_talhoes = []
laranja_talhoes = []
_next_id = {"cana": 1, "laranja": 1}

def m2_to_ha(area_m2: float) -> float:
    return area_m2 / 10_000.0

def leia_float(msg: str, minimo: float = None, maximo: float = None) -> float:
    while True:
        try:
            val = float(input(msg).replace(",", "."))
            if minimo is not None and val < minimo:
                print(f"Valor deve ser >= {minimo}.")
                continue
            if maximo is not None and val > maximo:
                print(f"Valor deve ser <= {maximo}.")
                continue
            return val
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def leia_int(msg: str, minimo: int = None, maximo: int = None) -> int:
    while True:
        try:
            val = int(input(msg))
            if minimo is not None and val < minimo:
                print(f"Valor deve ser >= {minimo}.")
                continue
            if maximo is not None and val > maximo:
                print(f"Valor deve ser <= {maximo}.")
                continue
            return val
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def pausar():
    input("\nPressione ENTER para continuar... ")

def cadastrar_talhao_cana():
    print("\n[CADASTRAR] Cana-de-açúcar")
    base = leia_float("Base do retângulo (m): ", minimo=0.1)
    altura = leia_float("Altura do retângulo (m): ", minimo=0.1)
    area_m2 = base * altura
    item = {
        "id": _next_id["cana"],
        "base_m": base,
        "altura_m": altura,
        "area_m2": area_m2,
        "area_ha": m2_to_ha(area_m2)
    }
    cana_talhoes.append(item)
    _next_id["cana"] += 1
    print(f"Talhão de Cana cadastrado! Área = {item['area_m2']:.2f} m² ({item['area_ha']:.4f} ha)")

def cadastrar_talhao_laranja():
    print("\n[CADASTRAR] Laranja")
    raio = leia_float("Raio do círculo (m): ", minimo=0.1)
    area_m2 = math.pi * (raio ** 2)
    item = {
        "id": _next_id["laranja"],
        "raio_m": raio,
        "area_m2": area_m2,
        "area_ha": m2_to_ha(area_m2)
    }
    laranja_talhoes.append(item)
    _next_id["laranja"] += 1
    print(f"Talhão de Laranja cadastrado! Área = {item['area_m2']:.2f} m² ({item['area_ha']:.4f} ha)")

def listar_talhoes():
    print("\n===== TALHÕES CANA =====")
    if not cana_talhoes:
        print("(vazio)")
    for it in cana_talhoes:
        print(f"ID {it['id']} | Área={it['area_m2']:.2f} m² ({it['area_ha']:.4f} ha)")

    print("\n===== TALHÕES LARANJA =====")
    if not laranja_talhoes:
        print("(vazio)")
    for it in laranja_talhoes:
        print(f"ID {it['id']} | Área={it['area_m2']:.2f} m² ({it['area_ha']:.4f} ha)")

def calcular_insumos_por_area():
    print("\n[INSUMOS POR ÁREA]")
    opc = leia_int("Cultura (1-Cana, 2-Laranja): ", 1, 2)
    alvo = None
    if opc == 1 and cana_talhoes:
        talhao_id = leia_int("ID do talhão: ")
        alvo = next((x for x in cana_talhoes if x["id"] == talhao_id), None)
    elif opc == 2 and laranja_talhoes:
        talhao_id = leia_int("ID do talhão: ")
        alvo = next((x for x in laranja_talhoes if x["id"] == talhao_id), None)

    if not alvo:
        print("Talhão não encontrado.")
        return

    dose_ha = leia_float("Dose por hectare (kg/ha ou L/ha): ", minimo=0.0)
    total = dose_ha * alvo["area_ha"]
    print(f"Área = {alvo['area_ha']:.4f} ha | Total necessário = {total:.3f}")

def calcular_insumos_por_metro_linear():
    print("\n[INSUMOS POR METRO LINEAR]")
    dose_ml_por_m = leia_float("Dose por metro (mL/m): ", minimo=0.0)
    q_ruas = leia_int("Número de ruas: ", minimo=1)
    comp_m = leia_float("Comprimento de cada rua (m): ", minimo=0.1)
    total_ml = dose_ml_por_m * q_ruas * comp_m
    total_l = total_ml / 1000.0
    print(f"Total necessário: {total_ml:.2f} mL ({total_l:.3f} L)")

def menu_principal():
    while True:
        print("\n==== FARMTECH SOLUTIONS ====")
        print("1) Cadastrar Cana")
        print("2) Cadastrar Laranja")
        print("3) Listar Talhões")
        print("4) Insumos por ÁREA")
        print("5) Insumos por METRO LINEAR")
        print("0) Sair")
        opc = leia_int("Opção: ", 0, 5)
        if opc == 0: break
        elif opc == 1: cadastrar_talhao_cana(); pausar()
        elif opc == 2: cadastrar_talhao_laranja(); pausar()
        elif opc == 3: listar_talhoes(); pausar()
        elif opc == 4: calcular_insumos_por_area(); pausar()
        elif opc == 5: calcular_insumos_por_metro_linear(); pausar()

if __name__ == "__main__":
    menu_principal()
