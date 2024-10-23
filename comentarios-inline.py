import requests

# Defina o nome do repositório e o token de acesso
REPO = "twbs/bootstrap"
TOKEN = "token"

# Obter pull requests fechados do repositório
url = f"https://api.github.com/repos/{REPO}/pulls?state=closed&per_page=100"
headers = {"Authorization": f"token {TOKEN}"}
response = requests.get(url, headers=headers)
pull_requests = response.json()

total_commits = 0
commits_with_comments = 0

# Verificar cada pull request
for pr in pull_requests:
    commits_url = pr['commits_url']
    commits_response = requests.get(commits_url, headers=headers)
    commits = commits_response.json()

    for commit in commits:
        total_commits += 1

        # Verificar se há comentários no commit (usando o endpoint review_comments_url do PR)
        review_comments_url = pr['_links']['review_comments']['href']
        review_comments_response = requests.get(review_comments_url, headers=headers)
        review_comments = review_comments_response.json()

        if len(review_comments) > 0:
            commits_with_comments += 1
            break

# Calcular o percentual de commits com comentários in-line
if total_commits > 0:
    percent_commits_with_comments = (commits_with_comments / total_commits) * 100
    print(f"Percentual de commits com comentários in-line: {percent_commits_with_comments:.2f}%")
else:
    print("Nenhum commit encontrado.")
