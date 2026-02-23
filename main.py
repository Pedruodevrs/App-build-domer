#!/usr/bin/env python3
import sys
import os

def run():

    target = sys.argv[1] if len(sys.argv) > 1 else None
    
    if not target:
        print("DOMER Language v1.0")
        print("Uso: domer <arquivo.dom>")
        return

    if not os.path.exists(target):
        print(f"Erro: O arquivo '{target}' não foi encontrado.")
        return

    vars_dom = {}
    
    try:
        with open(target, "r", encoding="utf-8") as f:
            linhas = f.readlines()
            
        i = 0
        while i < len(linhas):
            l = linhas[i].strip()
            
            # Pula linhas vazias ou comentários
            if not l or l.startswith("#"):
                i += 1
                continue
            
            # COMANDO: falar
            if l.startswith("falar"):
                try:
                    content = l.split('"')[1]
                    for k, v in vars_dom.items():
                        content = content.replace(f"{{{k}}}", str(v))
                    print(content)
                except IndexError:
                    print(f"Erro na linha {i+1}: Faltam aspas no comando falar.")
            
            # COMANDO: perguntar
            elif l.startswith("perguntar"):
                try:
                    msg = l.split('"')[1]
                    var_name = l.split(" em ")[1].strip()
                    res = input(msg + " ")
                    vars_dom[var_name] = int(res) if res.isdigit() else res
                except:
                    print(f"Erro na linha {i+1}: Sintaxe do comando perguntar inválida.")

            # COMANDO: calcular
            elif l.startswith("calcular"):
                expr = l.replace("calcular", "").strip()
                print(eval(expr, {}, vars_dom))

            # COMANDO: definir
            elif l.startswith("definir"):
                try:
                    parts = l.replace("definir", "").strip().split("=")
                    var_name = parts[0].strip()
                    vars_dom[var_name] = eval(parts[1].strip(), {}, vars_dom)
                except:
                    print(f"Erro na linha {i+1}: Erro na definição de variável.")

            # COMANDO: se / fimse
            elif l.startswith("se"):
                condicao = l.replace("se", "").strip()
                try:
                    if not eval(condicao, {}, vars_dom):
                        while i < len(linhas) and "fimse" not in linhas[i]:
                            i += 1
                except:
                    print(f"Erro na linha {i+1}: Condição inválida.")
            
            i += 1

    except Exception as e:
        print(f"Erro crítico no Interpretador: {e}")

if __name__ == "__main__":
    run()
                
