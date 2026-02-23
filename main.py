import sys
import os

def run():
    target = sys.argv[1] if len(sys.argv) > 1 else "script.dom"
    if not os.path.exists(target): return

    vars_dom = {}

    with open(target, "r", encoding="utf-8") as f:
        for line in f:
            l = line.strip()
            if not l or l.startswith("#"): continue
            
            if l.startswith("falar"):
                try:
                    content = l.split('"')[1]
                    for k, v in vars_dom.items():
                        content = content.replace(f"{{{k}}}", str(v))
                    print(content)
                except: pass
            
            elif l.startswith("perguntar"):
                try:
                    msg = l.split('"')[1]
                    var_name = l.split(" em ")[1].strip()
                    vars_dom[var_name] = input(msg + " ")
                except: pass

            elif l.startswith("calcular"):
                try:
                    expr = l.replace("calcular", "").strip()
                    print(eval(expr, {}, vars_dom))
                except: pass

            elif l.startswith("definir"):
                try:
                    parts = l.replace("definir", "").strip().split("=")
                    var_name = parts[0].strip()
                    vars_dom[var_name] = eval(parts[1].strip(), {}, vars_dom)
                except: pass

if __name__ == "__main__":
    run()
    
