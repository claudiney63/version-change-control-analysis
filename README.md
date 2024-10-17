# version-change-control-analysis
Análise de controle de versão e mudança de software, incluindo extração de dados de commits e issues, identificação dos principais desenvolvedores, arquivos mais modificados, tempo médio de resolução de issues, percentual de issues ligadas a commits e aplicação do algoritmo SZZ para bugs.

## 1. Usando Perceval para Coletar Dados de Commits (Controle de Versão)

### 1.1. Coletar Commits
Para obter os dados dos commits de um repositório GitHub, use o seguinte comando:

```
perceval github --json-line --category commits -t YOUR_GITHUB_TOKEN owner repository > commits.json

```
