import requests

# Defina o nome do repositório e o token de acesso
REPO = "twbs/bootstrap"  # Exemplo: Bootstrap
TOKEN = "token"

# Obter issues fechadas ou abertas do repositório
url = f"https://api.github.com/repos/{REPO}/issues?state=all&per_page=100"
headers = {"Authorization": f"token {TOKEN}"}
response = requests.get(url, headers=headers)
issues = response.json()

total_comments = 0
total_issues = 0

# Contar os comentários em cada issue
for issue in issues:
    if 'pull_request' in issue:
        # Pular pull requests
        continue
    total_issues += 1
    total_comments += issue['comments']

# Calcular a média de comentários por issue
if total_issues > 0:
    avg_comments = total_comments / total_issues
    print(f"Média de comentários por issue: {avg_comments:.2f}")
else:
    print("Nenhuma issue encontrada.")
