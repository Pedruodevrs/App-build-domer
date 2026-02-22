import os

def interpretador_dom():
    # Nome do arquivo que contém os seus comandos
    arquivo_script = "script.dom"

    # Verifica se o seu script existe na pasta
    if not os.path.exists(arquivo_script):
        print(f"❌ ERRO: O arquivo '{arquivo_script}' não foi encontrado!")
        print("Crie um arquivo chamado script.dom na mesma pasta deste main.py.")
        return

    print("\n" + "="*40)
    print("☢️  DOMER OS - EXECUTANDO VIA TERMINAL ☢️")
    print("="*40 + "\n")

    try:
        with open(arquivo_script, "r", encoding="utf-8") as f:
            linhas = f.readlines()
            
            for i, linha in enumerate(linhas):
                linha = linha.strip()
                
                # Pula linhas vazias ou comentários (que começam com #)
                if not linha or linha.startswith("#"):
                    continue
                
                # COMANDO: falar
                if linha.startswith("falar"):
                    try:
                        # Extrai o texto que está entre aspas
                        conteudo = linha.split('"')[1]
                        print(f"📢 [SAÍDA]: {conteudo}")
                    except IndexError:
                        print(f"⚠️  ERRO DE SINTAXE (Linha {i+1}): Use falar \"seu texto\"")

                # COMANDO: calcular
                elif linha.startswith("calcular"):
                    try:
                        # Remove a palavra 'calcular' e faz a conta
                        expressao = linha.replace("calcular", "").strip()
                        resultado = eval(expressao)
                        print(f"🔢 [CÁLCULO]: {expressao} = {resultado}")
                    except Exception as e:
                        print(f"⚠️  ERRO DE CÁLCULO (Linha {i+1}): {e}")
                
                # COMANDO DESCONHECIDO
                else:
                    print(f"❓ COMANDO NÃO RECONHECIDO (Linha {i+1}): {linha}")

    except Exception as e:
        print(f"❌ ERRO CRÍTICO AO LER O SCRIPT: {e}")

    print("\n" + "="*40)
    print("✅ EXECUÇÃO FINALIZADA COM SUCESSO")
    print("="*40 + "\n")

if __name__ == "__main__":
    interpretador_dom()
                                                           
