import requests
from datetime import datetime

# Defina o nome do repositório e o token
REPO = "twbs/bootstrap"  # Substitua pelo repositório desejado
TOKEN = "token"

# Função para calcular a diferença em dias entre duas datas
def days_between(date1, date2):
    return (date2 - date1).days

# Requisição para obter issues fechadas
url = f"https://api.github.com/repos/{REPO}/issues?state=closed&per_page=100"
headers = {"Authorization": f"token {TOKEN}"}
response = requests.get(url, headers=headers)
issues = response.json()

# Variáveis para calcular a média de tempo para fechar issues
total_days = 0
closed_issues_count = 0

# Iterar sobre as issues fechadas e calcular a diferença de tempo
for issue in issues:
    if 'created_at' in issue and 'closed_at' in issue:
        created_at = datetime.strptime(issue['created_at'], '%Y-%m-%dT%H:%M:%SZ')
        closed_at = datetime.strptime(issue['closed_at'], '%Y-%m-%dT%H:%M:%SZ')
        issue_days = days_between(created_at, closed_at)
        total_days += issue_days
        closed_issues_count += 1

# Calcular e exibir a média de dias
if closed_issues_count > 0:
    average_time = total_days / closed_issues_count
    print(f"Tempo médio para resolver uma issue: {average_time:.2f} dias")
else:
    print("Nenhuma issue fechada encontrada.")
