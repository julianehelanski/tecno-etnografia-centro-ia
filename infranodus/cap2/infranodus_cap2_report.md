# Análise de rede textual — Capítulo 2

> Análise de rede textual (*text network analysis*, Paranyushkin 2019)
> aplicada ao arquivo `ex_cap2.tex`. O texto foi limpo de comandos LaTeX,
> citações e notas de rodapé foram reincorporadas; janela deslizante de
> 4 *tokens* com pesos decrescentes pela distância (3-2-1). Comunidades
> detectadas por Louvain ponderado. Esta versão acrescenta duas métricas
> *informativas* que não dependem da frequência bruta: **PageRank** dos
> nós e **NPMI** das arestas. As métricas baseadas em frequência são
> mantidas em paralelo, para comparação.

## 1. Resumo quantitativo
- Tokens significativos: **28,094**
- Grafo bruto: **7051** nós · **66189** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3602** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `artificial` | 1859 |
| 2 | `inteligencia` | 1849 |
| 3 | `latour` | 1165 |
| 4 | `militar` | 1117 |
| 5 | `ciencia` | 1022 |
| 6 | `rotulo` | 872 |
| 7 | `rede` | 819 |
| 8 | `analise` | 773 |
| 9 | `vocabulario` | 759 |
| 10 | `humano` | 687 |
| 11 | `campo` | 662 |
| 12 | `figuracao` | 616 |
| 13 | `aime` | 555 |
| 14 | `rotulos` | 546 |
| 15 | `teoria` | 529 |
| 16 | `catalogo` | 521 |
| 17 | `ocorrencias` | 516 |
| 18 | `tecnologia` | 513 |
| 19 | `science` | 484 |
| 20 | `ator` | 477 |
| 21 | `tecnociencia` | 469 |
| 22 | `action` | 459 |
| 23 | `objeto` | 453 |
| 24 | `descreve` | 450 |
| 25 | `leitura` | 430 |
| 26 | `obras` | 425 |
| 27 | `dado` | 415 |
| 28 | `figuracoes` | 415 |
| 29 | `densidade` | 410 |
| 30 | `capes` | 410 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `artificial` | 0.0319 |
| 2 | `inteligencia` | 0.0319 |
| 3 | `latour` | 0.0215 |
| 4 | `militar` | 0.0193 |
| 5 | `ciencia` | 0.0186 |
| 6 | `rede` | 0.0155 |
| 7 | `rotulo` | 0.0155 |
| 8 | `analise` | 0.0147 |
| 9 | `vocabulario` | 0.0138 |
| 10 | `humano` | 0.0130 |
| 11 | `campo` | 0.0129 |
| 12 | `figuracao` | 0.0115 |
| 13 | `aime` | 0.0106 |
| 14 | `rotulos` | 0.0101 |
| 15 | `tecnologia` | 0.0100 |
| 16 | `catalogo` | 0.0099 |
| 17 | `teoria` | 0.0098 |
| 18 | `ocorrencias` | 0.0095 |
| 19 | `tecnociencia` | 0.0094 |
| 20 | `ator` | 0.0090 |
| 21 | `descreve` | 0.0089 |
| 22 | `objeto` | 0.0088 |
| 23 | `science` | 0.0088 |
| 24 | `dado` | 0.0087 |
| 25 | `leitura` | 0.0086 |
| 26 | `obras` | 0.0083 |
| 27 | `action` | 0.0083 |
| 28 | `figuracoes` | 0.0083 |
| 29 | `capes` | 0.0082 |
| 30 | `partir` | 0.0080 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `press` | 156 | 96 | +60 |
| 2 | `university` | 167 | 119 | +48 |
| 3 | `crawford` | 178 | 156 | +22 |
| 4 | `joler` | 162 | 142 | +20 |
| 5 | `traducao` | 140 | 121 | +19 |
| 6 | `producao` | 58 | 48 | +10 |
| 7 | `quadro` | 82 | 72 | +10 |
| 8 | `brasileira` | 84 | 76 | +8 |
| 9 | `brasil` | 118 | 110 | +8 |
| 10 | `modelo` | 59 | 52 | +7 |
| 11 | `cientifico` | 111 | 104 | +7 |
| 12 | `conhecimento` | 37 | 31 | +6 |
| 13 | `cadeia` | 89 | 83 | +6 |
| 14 | `collins` | 130 | 124 | +6 |
| 15 | `investigacao` | 141 | 135 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `latour` | 0.3293 |
| 2 | `inteligencia` | 0.2146 |
| 3 | `artificial` | 0.2087 |
| 4 | `ciencia` | 0.1439 |
| 5 | `militar` | 0.1434 |
| 6 | `vocabulario` | 0.1387 |
| 7 | `rotulo` | 0.0940 |
| 8 | `capes` | 0.0839 |
| 9 | `rede` | 0.0803 |
| 10 | `catalogo` | 0.0712 |
| 11 | `conceito` | 0.0692 |
| 12 | `analise` | 0.0602 |
| 13 | `teoria` | 0.0544 |
| 14 | `humano` | 0.0534 |
| 15 | `figuracoes` | 0.0533 |
| 16 | `aime` | 0.0480 |
| 17 | `campo` | 0.0458 |
| 18 | `descreve` | 0.0446 |
| 19 | `figuracao` | 0.0438 |
| 20 | `tecnociencia` | 0.0359 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `laboratory` | `life` | 0.871 | 106 |
| 2 | `hope` | `pandora` | 0.869 | 120 |
| 3 | `inteligencia` | `artificial` | 0.828 | 819 |
| 4 | `press` | `university` | 0.818 | 64 |
| 5 | `taxa` | `interna` | 0.803 | 54 |
| 6 | `action` | `science` | 0.789 | 168 |
| 7 | `crawford` | `joler` | 0.740 | 41 |
| 8 | `quadro` | `conclusao` | 0.728 | 62 |
| 9 | `mediacao` | `tecnica` | 0.711 | 96 |
| 10 | `maquina` | `aprendizado` | 0.710 | 126 |
| 11 | `teoria` | `ator` | 0.707 | 152 |
| 12 | `textil` | `topologico` | 0.650 | 46 |
| 13 | `refinada` | `contagem` | 0.644 | 46 |
| 14 | `lexicometrica` | `analise` | 0.626 | 95 |
| 15 | `modelo` | `linguagem` | 0.597 | 63 |
| 16 | `ator` | `rede` | 0.592 | 154 |
| 17 | `recalling` | `clarifications` | 0.571 | 27 |
| 18 | `traducao` | `brasileira` | 0.563 | 27 |
| 19 | `action` | `pandora` | 0.559 | 52 |
| 20 | `industria` | `militar` | 0.552 | 89 |
| 21 | `publico` | `repositorio` | 0.530 | 33 |
| 22 | `stengers` | `haraway` | 0.527 | 29 |
| 23 | `vocabulario` | `topologico` | 0.522 | 58 |
| 24 | `lexical` | `catalogo` | 0.518 | 43 |
| 25 | `ciencia` | `humano` | 0.517 | 177 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (45 termos): artificial, inteligencia, ciencia, humano, campo, tecnologia
- **Tópico 2** (43 termos): latour, rede, analise, teoria, ator, tecnociencia
- **Tópico 3** (39 termos): militar, rotulo, vocabulario, figuracao, aime, rotulos
- **Tópico 4** (37 termos): obras, dado, capes, partir, scielo, producao
- **Tópico 5** (7 termos): science, action, pandora, hope, laboratory, life
- **Tópico 6** (5 termos): quadro, modos, conclusao, investigacao, grupo
- **Tópico 7** (2 termos): press, university
- **Tópico 8** (2 termos): joler, crawford

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 4** [obras, dado, capes] e **Tópico 5** [science, action, pandora] — densidade ponderada de ligação = 0.2046
- Lacuna entre **Tópico 1** [artificial, inteligencia, ciencia] e **Tópico 5** [science, action, pandora] — densidade ponderada de ligação = 0.2952
- Lacuna entre **Tópico 1** [artificial, inteligencia, ciencia] e **Tópico 3** [militar, rotulo, vocabulario] — densidade ponderada de ligação = 0.4803
- Lacuna entre **Tópico 2** [latour, rede, analise] e **Tópico 4** [obras, dado, capes] — densidade ponderada de ligação = 0.5839
- Lacuna entre **Tópico 2** [latour, rede, analise] e **Tópico 5** [science, action, pandora] — densidade ponderada de ligação = 0.6512
- Lacuna entre **Tópico 3** [militar, rotulo, vocabulario] e **Tópico 4** [obras, dado, capes] — densidade ponderada de ligação = 0.7339

## 9. Leitura interpretativa
_Leitura interpretativa ainda não escrita para este capítulo. Crie `interpretation_cap2.md` ao lado dos outputs para que o conteúdo seja embutido aqui automaticamente._

## 10. Arquivos gerados
**Visões frequentistas**
- `infranodus_cap2_network.png` — rede completa, tamanho por degree.
- `infranodus_cap2_focus.png` — núcleo (top-100, peso ≥ 3).

**Visões informativas**
- `infranodus_cap2_pmi.png` — rede completa, tamanho por **PageRank**,
  arestas filtradas por **NPMI ≥ 0,20**.
- `infranodus_cap2_focus_pmi.png` — núcleo, NPMI ≥ 0,25.

**Dados**
- `infranodus_cap2_metrics.json` — métricas brutas (degree, betweenness,
  PageRank, NPMI, comunidades, lacunas).
- `infranodus_cap2.gexf` / `infranodus_cap2_focus.gexf` — grafos para Gephi
  já com `community`, `frequency`, `degree_weighted`, `betweenness`,
  `pagerank` (nós) e `weight`, `npmi` (arestas).
- `infranodus_cap2_nodes.csv` / `infranodus_cap2_edges.csv` (e `_focus_*`)
  — fallback em planilha; CSVs trazem todas as colunas acima.

## 11. Como abrir no Gephi
1. Instale Gephi (≥ 0.10): https://gephi.org/users/download/
2. `File → Open…` → selecione `infranodus_cap2.gexf` (ou `_focus.gexf`).
3. No painel **Appearance**: já vem com cor por `community` e tamanho por
   `degree_weighted` (embutidos via atributos `viz`). Ajuste se quiser.
4. Em **Layout**: aplique *ForceAtlas 2* (ative *Prevent Overlap* e
   *Dissuade Hubs*) por ~30 s; ou *Fruchterman-Reingold* para algo mais rápido.
5. Em **Statistics**: rode *Modularity* e *Average Path Length* se quiser
   recalcular comunidades dentro do Gephi (resultados serão semelhantes).
6. Em **Preview**: ative *Node Labels*, escolha fonte e exporte para PDF/SVG.
