<p align="center">
  <img src="images.png" width="160" alt="DOMER Logo">
</p>

<h1 align="center">DOMER Language</h1>

<p align="center">
  <b>Uma linguagem de programação autêntica, criada e desenvolvida inteiramente via mobile.</b>
</p>

---

## 🚀 Sobre o DOMER
O **DOMER** é uma linguagem de script interpretada, projetada para ser simples, direta e eficiente. Diferente de outras linguagens, o DOMER nasceu da necessidade de programar em qualquer lugar, usando o poder do celular.

## 🛠️ Comandos Principais

| Comando | O que faz | Exemplo |
| :--- | :--- | :--- |
| `falar` | Exibe um texto ou variável na tela | `falar "Olá Mundo"` |
| `perguntar` | Recebe um dado do usuário | `perguntar "Idade:" em idade` |
| `definir` | Cria uma variável ou faz cálculos | `definir total = a + b` |
| `se` | Cria uma condição | `se total > 10` |
| `fimse` | Encerra o bloco da condição | `fimse` |

## 💻 Exemplo de Código (`script.dom`)

```text
falar "--- BEM-VINDO AO DOMER ---"
perguntar "Digite o valor A:" em a
perguntar "Digite o valor B:" em b

definir resultado = a + b

falar "A soma de {a} com {b} é: {resultado}"

se resultado > 50
  falar "Resultado alto!"
fimse

falar "Fim do programa."
