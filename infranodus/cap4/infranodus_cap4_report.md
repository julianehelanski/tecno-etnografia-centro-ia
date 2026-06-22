# Análise de rede textual — Capítulo 4

> Análise de rede textual (*text network analysis*, Paranyushkin 2019)
> aplicada ao arquivo `ex_cap4.tex`. O texto foi limpo de comandos LaTeX,
> citações e notas de rodapé foram reincorporadas; janela deslizante de
> 4 *tokens* com pesos decrescentes pela distância (3-2-1). Comunidades
> detectadas por Louvain ponderado. Esta versão acrescenta duas métricas
> *informativas* que não dependem da frequência bruta: **PageRank** dos
> nós e **NPMI** das arestas. As métricas baseadas em frequência são
> mantidas em paralelo, para comparação.

## 1. Resumo quantitativo
- Tokens significativos: **15,222**
- Grafo bruto: **4368** nós · **38803** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2402** arestas
- Tópicos detectados (Louvain): **9**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 934 |
| 2 | `covideiro` | 586 |
| 3 | `rede` | 512 |
| 4 | `artigo` | 501 |
| 5 | `modelo` | 451 |
| 6 | `dado` | 427 |
| 7 | `respiratoria` | 403 |
| 8 | `inscricao` | 382 |
| 9 | `insuficiencia` | 375 |
| 10 | `cadeia` | 349 |
| 11 | `objeto` | 330 |
| 12 | `artigos` | 300 |
| 13 | `coleta` | 251 |
| 14 | `audio` | 234 |
| 15 | `projeto` | 233 |
| 16 | `espectrograma` | 226 |
| 17 | `pandemico` | 226 |
| 18 | `pacientes` | 225 |
| 19 | `sinal` | 221 |
| 20 | `cientifico` | 213 |
| 21 | `marcelo` | 207 |
| 22 | `condicoes` | 207 |
| 23 | `analise` | 197 |
| 24 | `actante` | 194 |
| 25 | `pratica` | 186 |
| 26 | `covid` | 181 |
| 27 | `ponto` | 176 |
| 28 | `condicao` | 169 |
| 29 | `dataset` | 167 |
| 30 | `torna` | 156 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0387 |
| 2 | `covideiro` | 0.0242 |
| 3 | `rede` | 0.0214 |
| 4 | `artigo` | 0.0209 |
| 5 | `modelo` | 0.0193 |
| 6 | `dado` | 0.0181 |
| 7 | `inscricao` | 0.0163 |
| 8 | `respiratoria` | 0.0160 |
| 9 | `cadeia` | 0.0150 |
| 10 | `insuficiencia` | 0.0147 |
| 11 | `objeto` | 0.0144 |
| 12 | `artigos` | 0.0125 |
| 13 | `coleta` | 0.0114 |
| 14 | `audio` | 0.0107 |
| 15 | `sinal` | 0.0104 |
| 16 | `espectrograma` | 0.0102 |
| 17 | `projeto` | 0.0101 |
| 18 | `pacientes` | 0.0099 |
| 19 | `pandemico` | 0.0096 |
| 20 | `marcelo` | 0.0092 |
| 21 | `condicoes` | 0.0092 |
| 22 | `cientifico` | 0.0090 |
| 23 | `actante` | 0.0088 |
| 24 | `pratica` | 0.0086 |
| 25 | `analise` | 0.0086 |
| 26 | `ponto` | 0.0083 |
| 27 | `covid` | 0.0078 |
| 28 | `condicao` | 0.0078 |
| 29 | `dataset` | 0.0075 |
| 30 | `secao` | 0.0074 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `frequencia` | 122 | 109 | +13 |
| 2 | `acesso` | 111 | 99 | +12 |
| 3 | `celular` | 99 | 88 | +11 |
| 4 | `forca` | 118 | 108 | +10 |
| 5 | `fala` | 82 | 73 | +9 |
| 6 | `resultado` | 95 | 86 | +9 |
| 7 | `operacao` | 115 | 106 | +9 |
| 8 | `pesquisa` | 69 | 61 | +8 |
| 9 | `linguagem` | 86 | 78 | +8 |
| 10 | `escolha` | 120 | 113 | +7 |
| 11 | `lugar` | 125 | 118 | +7 |
| 12 | `acustico` | 42 | 36 | +6 |
| 13 | `virus` | 52 | 46 | +6 |
| 14 | `instituicao` | 72 | 66 | +6 |
| 15 | `onda` | 130 | 124 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.4946 |
| 2 | `covideiro` | 0.2171 |
| 3 | `artigo` | 0.1736 |
| 4 | `dado` | 0.1397 |
| 5 | `modelo` | 0.1183 |
| 6 | `rede` | 0.1032 |
| 7 | `inscricao` | 0.0722 |
| 8 | `audio` | 0.0713 |
| 9 | `cadeia` | 0.0689 |
| 10 | `respiratoria` | 0.0548 |
| 11 | `sinal` | 0.0524 |
| 12 | `coleta` | 0.0485 |
| 13 | `repositorio` | 0.0459 |
| 14 | `objeto` | 0.0404 |
| 15 | `insuficiencia` | 0.0362 |
| 16 | `projeto` | 0.0349 |
| 17 | `pandemico` | 0.0340 |
| 18 | `espectrograma` | 0.0298 |
| 19 | `pratica` | 0.0255 |
| 20 | `artigos` | 0.0242 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `respiratoria` | `insuficiencia` | 0.839 | 156 |
| 2 | `imutavel` | `movel` | 0.829 | 48 |
| 3 | `vista` | `ponto` | 0.604 | 30 |
| 4 | `sinal` | `acustico` | 0.600 | 43 |
| 5 | `neural` | `rede` | 0.590 | 66 |
| 6 | `entrevista` | `marcelo` | 0.580 | 40 |
| 7 | `marilia` | `hospitais` | 0.578 | 26 |
| 8 | `tornou` | `possivel` | 0.562 | 23 |
| 9 | `versao` | `especifica` | 0.541 | 14 |
| 10 | `tornou` | `visivel` | 0.531 | 18 |
| 11 | `fapesp` | `financiamento` | 0.523 | 15 |
| 12 | `designa` | `fenomeno` | 0.519 | 12 |
| 13 | `inscrito` | `roteiro` | 0.514 | 11 |
| 14 | `publico` | `repositorio` | 0.508 | 18 |
| 15 | `covideiro` | `pandemico` | 0.504 | 73 |
| 16 | `publico` | `saude` | 0.499 | 12 |
| 17 | `linguagem` | `processamento` | 0.492 | 12 |
| 18 | `deteccao` | `distintos` | 0.490 | 12 |
| 19 | `fonoaudiologos` | `medicos` | 0.489 | 11 |
| 20 | `saude` | `pesquisa` | 0.488 | 12 |
| 21 | `ciencia` | `acao` | 0.484 | 12 |
| 22 | `textual` | `analise` | 0.481 | 22 |
| 23 | `controles` | `pacientes` | 0.471 | 28 |
| 24 | `condicoes` | `producao` | 0.469 | 27 |
| 25 | `acesso` | `disponivel` | 0.468 | 9 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (38 termos): spira, artigo, artigos, projeto, cientifico, marcelo
- **Tópico 2** (31 termos): audio, espectrograma, sinal, torna, acustico, virus
- **Tópico 3** (22 termos): dado, respiratoria, insuficiencia, pacientes, covid, ruido
- **Tópico 4** (19 termos): rede, inscricao, cadeia, analise, ponto, neural
- **Tópico 5** (19 termos): modelo, repositorio, treinado, pesquisa, publico, linguagem
- **Tópico 6** (18 termos): covideiro, pandemico, actante, produziu, configuracao, humano
- **Tópico 7** (16 termos): objeto, condicoes, pratica, observador, distintos, producao
- **Tópico 8** (9 termos): coleta, condicao, hospitais, protocolo, clinica, momento

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [audio, espectrograma, sinal] e **Tópico 5** [modelo, repositorio, treinado] — densidade ponderada de ligação = 0.2954
- Lacuna entre **Tópico 4** [rede, inscricao, cadeia] e **Tópico 5** [modelo, repositorio, treinado] — densidade ponderada de ligação = 0.3352
- Lacuna entre **Tópico 1** [spira, artigo, artigos] e **Tópico 2** [audio, espectrograma, sinal] — densidade ponderada de ligação = 0.3421
- Lacuna entre **Tópico 3** [dado, respiratoria, insuficiencia] e **Tópico 5** [modelo, repositorio, treinado] — densidade ponderada de ligação = 0.3517
- Lacuna entre **Tópico 2** [audio, espectrograma, sinal] e **Tópico 4** [rede, inscricao, cadeia] — densidade ponderada de ligação = 0.3837
- Lacuna entre **Tópico 2** [audio, espectrograma, sinal] e **Tópico 3** [dado, respiratoria, insuficiencia] — densidade ponderada de ligação = 0.4018

## 9. Leitura interpretativa
_Leitura interpretativa ainda não escrita para este capítulo. Crie `interpretation_cap4.md` ao lado dos outputs para que o conteúdo seja embutido aqui automaticamente._

## 10. Arquivos gerados
**Visões frequentistas**
- `infranodus_cap4_network.png` — rede completa, tamanho por degree.
- `infranodus_cap4_focus.png` — núcleo (top-100, peso ≥ 3).

**Visões informativas**
- `infranodus_cap4_pmi.png` — rede completa, tamanho por **PageRank**,
  arestas filtradas por **NPMI ≥ 0,20**.
- `infranodus_cap4_focus_pmi.png` — núcleo, NPMI ≥ 0,25.

**Dados**
- `infranodus_cap4_metrics.json` — métricas brutas (degree, betweenness,
  PageRank, NPMI, comunidades, lacunas).
- `infranodus_cap4.gexf` / `infranodus_cap4_focus.gexf` — grafos para Gephi
  já com `community`, `frequency`, `degree_weighted`, `betweenness`,
  `pagerank` (nós) e `weight`, `npmi` (arestas).
- `infranodus_cap4_nodes.csv` / `infranodus_cap4_edges.csv` (e `_focus_*`)
  — fallback em planilha; CSVs trazem todas as colunas acima.

## 11. Como abrir no Gephi
1. Instale Gephi (≥ 0.10): https://gephi.org/users/download/
2. `File → Open…` → selecione `infranodus_cap4.gexf` (ou `_focus.gexf`).
3. No painel **Appearance**: já vem com cor por `community` e tamanho por
   `degree_weighted` (embutidos via atributos `viz`). Ajuste se quiser.
4. Em **Layout**: aplique *ForceAtlas 2* (ative *Prevent Overlap* e
   *Dissuade Hubs*) por ~30 s; ou *Fruchterman-Reingold* para algo mais rápido.
5. Em **Statistics**: rode *Modularity* e *Average Path Length* se quiser
   recalcular comunidades dentro do Gephi (resultados serão semelhantes).
6. Em **Preview**: ative *Node Labels*, escolha fonte e exporte para PDF/SVG.
