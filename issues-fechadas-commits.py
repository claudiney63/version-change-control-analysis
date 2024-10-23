import requests

# Defina o nome do repositório e o token de acesso do GitHub
REPO = "twbs/bootstrap"  # Exemplo: Bootstrap
TOKEN = "token"

# Requisição para obter issues fechadas
url = f"https://api.github.com/repos/{REPO}/issues?state=closed&per_page=100"
headers = {"Authorization": f"token {TOKEN}"}
response = requests.get(url, headers=headers)
issues = response.json()

# Variáveis para calcular o percentual
total_closed_issues = 0
closed_by_commit_issues = 0
closed_by_pull_requests = 0
closed_manually = 0

# Iterar sobre as issues fechadas
for issue in issues:
    if 'pull_request' in issue:
        # Se a issue foi fechada por um pull request
        closed_by_pull_requests += 1
        total_closed_issues += 1
        continue
    
    total_closed_issues += 1
    
    # Verificar os eventos da issue para saber como ela foi fechada
    events_url = issue['events_url']
    events_response = requests.get(events_url, headers=headers)
    events = events_response.json()

    closed_by_commit = False
    closed_manually_flag = False

    # Verificar eventos da issue
    for event in events:
        if event['event'] == 'closed':
            if event.get('commit_id'):
                closed_by_commit = True
                break  # A issue foi fechada diretamente por um commit
            else:
                closed_manually_flag = True  # A issue foi fechada manualmente

    # Verificar se foi fechada por commit direto
    if closed_by_commit:
        closed_by_commit_issues += 1
    elif closed_manually_flag:
        closed_manually += 1

# Calcular os percentuais
if total_closed_issues > 0:
    percent_closed_by_commit = (closed_by_commit_issues / total_closed_issues) * 100
    percent_closed_by_pull_requests = (closed_by_pull_requests / total_closed_issues) * 100
    percent_closed_manually = (closed_manually / total_closed_issues) * 100

    print(f"Percentual de issues fechadas associadas a commits: {percent_closed_by_commit:.2f}%")
    print(f"Percentual de issues fechadas por pull requests: {percent_closed_by_pull_requests:.2f}%")
    print(f"Percentual de issues fechadas manualmente: {percent_closed_manually:.2f}%")
else:
    print("Nenhuma issue fechada encontrada.")
