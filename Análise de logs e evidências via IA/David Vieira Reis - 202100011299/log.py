import subprocess
def git(cmd): 
    return subprocess.run(cmd, capture_output=True, text=True, shell=True).stdout

with open("log.txt", "w", encoding="utf-8") as f:
    f.write(f"BRANCHES:\n{git('git branch -r')}\n")
    f.write(f"TAGS:\n{git('git tag --sort=-creatordate --format=\"%(refname:short)|%(creatordate:iso)\"')}\n")
    f.write(f"GRAFO:\n{git('git log --graph --oneline -n 100 --all')}")
print("Arquivo log.txt gerado!")