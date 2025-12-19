import os
import subprocess

REPO_URL = "https://github.com/microsoft/JARVIS.git"
REPO_NAME = "JARVIS"

def run_git(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            shell=True,
            encoding="utf-8",
            errors="replace"
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Erro ao executar comando: {e}"

def main():
    print(f">>> Iniciando analise do repositorio: {REPO_NAME}...\n")

    if not os.path.exists(REPO_NAME):
        print(f">>> Clonando {REPO_URL}...")
        run_git(f"git clone {REPO_URL}")
    else:
        print(">>> Repositorio ja existe. Pulando clone.")

    os.chdir(REPO_NAME)
    print(f">>> Diretorio de trabalho atual: {os.getcwd()}\n")

    print(">>> Extraindo evidencias do Git...\n")

    branches = run_git("git branch -r")

    tags = run_git(
        'git tag --sort=-creatordate --format="%(refname:short)|%(creatordate:iso)"'
    )
    if not tags:
        tags = "(Nenhuma tag de versao encontrada - Output vazio)"

    grafo = run_git("git log --graph --oneline --all")

    relatorio_final = f"""
ATUE COMO UM ENGENHEIRO DE SOFTWARE E ANALISE OS DADOS ABAIXO:

1. Identifique o Branching Model (Fluxo de Trabalho) analisando o grafo e os merges.
   (Procure por padrões como Gitflow, GitHub Flow ou Trunk-Based).
   Cite evidências do log, como nomes de branches (ex: patch-1, dependabot).

2. Identifique a Estratégia de Release (Lançamento).
   (Verifique se existem TAGS de versão semântica ou se o fluxo é Contínuo/CD).

=====================================================
    DADOS TECNICOS EXTRAIDOS DO REPOSITORIO: {REPO_NAME}
=====================================================

[1] ESTRUTURA DE BRANCHES (git branch -r)
{branches}

-----------------------------------------------------

[2] HISTORICO DE VERSOES/TAGS (git tag)
{tags}

-----------------------------------------------------

[3] FLUXO VISUAL / GRAFO (git log --graph --oneline)
{grafo}
=====================================================
    """

    nome_arquivo = "log_para_ia.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(relatorio_final)

    print(f">>> ANALISE CONCLUIDA! O arquivo '{nome_arquivo}' foi gerado.")
    print(">>> COPIE TUDO ABAIXO E COLE NO HUGGINGCHAT (MODELO QWEN): \n")

    try:
        print(relatorio_final)
    except UnicodeEncodeError:
        print("\n[AVISO: Nao foi possivel imprimir o grafo no terminal.]")
        print(f"[Abra o arquivo '{nome_arquivo}' para copiar o conteudo.]")

    os.chdir("..")

if __name__ == "__main__":
    main()
