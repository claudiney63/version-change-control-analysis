# version-change-control-analysis
Análise de controle de versão e mudança de software, incluindo extração de dados de commits e issues, identificação dos principais desenvolvedores, arquivos mais modificados, tempo médio de resolução de issues, percentual de issues ligadas a commits e aplicação do algoritmo SZZ para bugs.

## 1. Usando Perceval para Coletar Dados de Commits (Controle de Versão)

### 1.1. Coletar Commits
Para obter os dados dos commits de um repositório GitHub, use o seguinte comando:

```
perceval github --json-line --category commits -t YOUR_GITHUB_TOKEN owner repository > commits.json

```

### 1.2. Top-5 desenvolvedores (#commits)

```
  9849  Mark Otto
  3052  Chris Rebert
  2768  XhmikosR
   854  Jacob Thornton
   765  dependabot[bot]
```

### Top-5 arquivos mais modificados 

````
Count Name                      Group
----- ----                      -----
    4 docs/assets/js/vendor/... {docs/assets/js/vendor/Blob.js, docs/assets/js/vendor/blob.js, docs/assets/js/vendor/Blob.js, docs/assets/js/vendor/blob.js}      
    4 docs/assets/js/vendor/... {docs/assets/js/vendor/filesaver.js, docs/assets/js/vendor/FileSaver.js, docs/assets/js/vendor/filesaver.js, docs/assets/js/ve... 
    1 site/content/docs/5.2/... {site/content/docs/5.2/components/alerts.md}
    1 site/content/docs/5.2/... {site/content/docs/5.2/components/accordion.md}
    1 site/content/docs/5.2/... {site/content/docs/5.2/about/team.md}
```