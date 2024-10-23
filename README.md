# Version Change Control Analysis
Análise de controle de versão e mudança de software, incluindo extração de dados de commits e issues, identificação dos principais desenvolvedores, arquivos mais modificados, tempo médio de resolução de issues, percentual de issues ligadas a commits e aplicação do algoritmo SZZ para bugs.

## 1. Usando Git para Coletar Dados de Commits (Controle de Versão)

### 1.1. Coletar Commits
Para obter os dados dos commits de um repositório GitHub, use o seguinte comando:

```
git clone https://github.com/user/repo-name.git
cd repo-name
```

Será analisado o repositorio do framework Bootstrap.

### 1.2. Top-5 desenvolvedores (#commits)

Abaixo é listado os 5 desenvolvedores que mais fizeram commits:

```
git shortlog -sn --all | Select-Object -First 5

  9849  Mark Otto
  3052  Chris Rebert
  2768  XhmikosR
   854  Jacob Thornton
   765  dependabot[bot]
```

### 1.3. Top-5 arquivos mais modificados 

Abaixo é listado os 5 arquivos do framework que foram modificados mais vezes:

```
git log --name-only --pretty=format: | Sort-Object | Get-Unique | Group-Object | Sort-Object Count -Descending | Select-Object -First 5

Count Name                      Group
----- ----                      -----
    4 docs/assets/js/vendor/... {docs/assets/js/vendor/Blob.js, docs/assets/js/vendor/blob.js, docs/assets/js/vendor/Blob.js, docs/assets/js/vendor/blob.js}      
    4 docs/assets/js/vendor/... {docs/assets/js/vendor/filesaver.js, docs/assets/js/vendor/FileSaver.js, docs/assets/js/vendor/filesaver.js, docs/assets/js/ve... 
    1 site/content/docs/5.2/... {site/content/docs/5.2/components/alerts.md}
    1 site/content/docs/5.2/... {site/content/docs/5.2/components/accordion.md}
    1 site/content/docs/5.2/... {site/content/docs/5.2/about/team.md}
```

### 1.4. Número médio de arquivos por commit

Para contar o número total de arquivos modificados:

```
git log --pretty=format: --name-only | Where-Object { $_ -ne "" } | Measure-Object

Count    : 65134
```

Para contar o número total de commits:

```
git rev-list --count HEAD

22909
```

Agora, dividimos o número total de arquivos pelo número total de commits para obter a média.

```
65134 / 22909 = 2.85
```

### 1.5. Tempo médio para resolver uma issue (dias)

Essa parte consiste em calcular o tempo médio que leva para as issues serem fechadas no repositório que você está analisando.

```
Tempo médio para resolver uma issue: 3.85 dias
```

  - Explicação do Código:

    - Requisição de Issues Fechadas: O script envia uma requisição para a API do GitHub, buscando as issues fechadas (state=closed) do repositório selecionado. Ele retorna até 100 issues por página.

    - Data de Criação e Fechamento: Para cada issue, o código coleta as datas de criação (created_at) e fechamento (closed_at), e então converte essas datas para o formato datetime do Python.

    - Cálculo da Diferença: A diferença entre as duas datas é calculada usando datetime do Python, o que resulta no número de dias que a issue levou para ser resolvida.

    - Cálculo da Média: O tempo total é somado para todas as issues e, no final, o tempo médio é obtido dividindo-se o total de dias pelo número de issues analisadas.

### 1.6. Percentual de issues fechadas que estão associadas a commits

É calculado o percentual de issues fechadas que estão vinculadas a um commit, ou seja, quantas issues foram fechadas diretamente devido a um commit ou foram mencionadas em mensagens de commit.

Explicações:
  - Fechamento por Pull Request: Se o campo 'pull_request' estiver presente na issue, conta como fechada por pull request.

  - Fechamento por Commit Direto: Se o evento 'closed' tem o campo 'commit_id', significa que a issue foi fechada diretamente por um commit.

  - Fechamento Manual: Se o evento de fechamento não tem um commit_id nem foi por um pull request, ela é contabilizada como fechamento manual (ou seja, um desenvolvedor a fechou manualmente sem associá-la a um commit específico).

```
Percentual de issues fechadas associadas a commits: 0.00%
Percentual de issues fechadas por pull requests: 72.00%
Percentual de issues fechadas manualmente: 23.00%
```

### 1.7. Aplicar o algoritmo SZZ para identificar o commit que introduziu um bug

O bug encontrado refere-se a uma correção de um erro tipográfico no código da documentação do Bootstrap. Especificamente, a variável Sass $enable-css-grid foi corrigida para $enable-cssgrid. Isso ocorreu na seção "Customize > Options" da documentação.

  - Commits efetuados:

![image](https://github.com/user-attachments/assets/56de9bc0-67bd-4441-ac51-2979b744f238)

  - Arquivo modificado:

![image](https://github.com/user-attachments/assets/cef84df4-d70a-45d5-8e70-bb691ad5f738)

  - Commit que foi inserido o bug:
    
![image](https://github.com/user-attachments/assets/2664186b-50eb-4f59-b227-30181cb49e5f)

O erro parece ser uma simples inconsistência no nome da variável que estava sendo referenciada. A correção foi feita para garantir que o nome da variável Sass estivesse correto, de forma a evitar possíveis problemas durante a compilação ou o uso do CSS Grid ao configurar o Bootstrap.

### 1.8. Média comentarios por issue

O script acessa a API do GitHub para recuperar todas as issues (abertas e fechadas) e contabiliza o número total de comentários em todas as issues que não são pull requests.
No final, ele calcula a média de comentários por issue.

```
Média de comentários por issue: 1.73
```

Média de comentários por issue: É a soma dos comentários de todas as issues dividido pelo número total de issues.

### 1.9. Percentual de commits com comentários in-line

Os comentários in-line são aqueles feitos diretamente em linhas de código em pull requests, associados a commits. Para calcular o percentual de commits que possuem comentários in-line, você precisará acessar os pull requests e verificar se há comentários em arquivos modificados.

```
Percentual de commits com comentários in-line: 2.86%
```

O script recupera todos os pull requests fechados e verifica os commits em cada PR.
Para cada commit, ele verifica se há comentários in-line no código, acessando o link review_comments.
No final, ele calcula o percentual de commits com comentários in-line.

Percentual de commits com comentários in-line: É o número de commits em pull requests que têm comentários in-line dividido pelo número total de commits, multiplicado por 100.
