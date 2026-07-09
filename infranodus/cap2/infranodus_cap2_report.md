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
- Tokens significativos: **28,194**
- Grafo bruto: **7060** nós · **66357** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3600** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `artificial` | 1861 |
| 2 | `inteligencia` | 1854 |
| 3 | `latour` | 1149 |
| 4 | `militar` | 1114 |
| 5 | `ciencia` | 1025 |
| 6 | `rotulo` | 879 |
| 7 | `rede` | 809 |
| 8 | `analise` | 766 |
| 9 | `vocabulario` | 764 |
| 10 | `humano` | 690 |
| 11 | `campo` | 660 |
| 12 | `figuracao` | 616 |
| 13 | `aime` | 552 |
| 14 | `rotulos` | 546 |
| 15 | `teoria` | 527 |
| 16 | `catalogo` | 521 |
| 17 | `ocorrencias` | 515 |
| 18 | `tecnologia` | 511 |
| 19 | `science` | 489 |
| 20 | `tecnociencia` | 466 |
| 21 | `ator` | 466 |
| 22 | `action` | 465 |
| 23 | `objeto` | 450 |
| 24 | `descreve` | 449 |
| 25 | `obras` | 444 |
| 26 | `leitura` | 424 |
| 27 | `dado` | 417 |
| 28 | `densidade` | 413 |
| 29 | `figuracoes` | 412 |
| 30 | `capes` | 410 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `artificial` | 0.0320 |
| 2 | `inteligencia` | 0.0319 |
| 3 | `latour` | 0.0210 |
| 4 | `militar` | 0.0191 |
| 5 | `ciencia` | 0.0186 |
| 6 | `rotulo` | 0.0156 |
| 7 | `rede` | 0.0153 |
| 8 | `analise` | 0.0146 |
| 9 | `vocabulario` | 0.0139 |
| 10 | `humano` | 0.0130 |
| 11 | `campo` | 0.0128 |
| 12 | `figuracao` | 0.0115 |
| 13 | `aime` | 0.0105 |
| 14 | `rotulos` | 0.0101 |
| 15 | `tecnologia` | 0.0099 |
| 16 | `catalogo` | 0.0099 |
| 17 | `teoria` | 0.0097 |
| 18 | `ocorrencias` | 0.0094 |
| 19 | `tecnociencia` | 0.0093 |
| 20 | `descreve` | 0.0089 |
| 21 | `science` | 0.0088 |
| 22 | `dado` | 0.0088 |
| 23 | `obras` | 0.0087 |
| 24 | `objeto` | 0.0087 |
| 25 | `ator` | 0.0087 |
| 26 | `leitura` | 0.0085 |
| 27 | `action` | 0.0084 |
| 28 | `figuracoes` | 0.0082 |
| 29 | `capes` | 0.0082 |
| 30 | `partir` | 0.0080 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `press` | 156 | 97 | +59 |
| 2 | `university` | 171 | 119 | +52 |
| 3 | `traducao` | 135 | 112 | +23 |
| 4 | `joler` | 163 | 142 | +21 |
| 5 | `crawford` | 176 | 157 | +19 |
| 6 | `quadro` | 82 | 72 | +10 |
| 7 | `modelo` | 60 | 51 | +9 |
| 8 | `brasileira` | 84 | 75 | +9 |
| 9 | `producao` | 58 | 50 | +8 |
| 10 | `cadeia` | 91 | 83 | +8 |
| 11 | `cientifico` | 111 | 103 | +8 |
| 12 | `argumento` | 127 | 120 | +7 |
| 13 | `investigacao` | 141 | 134 | +7 |
| 14 | `conhecimento` | 37 | 31 | +6 |
| 15 | `taxa` | 110 | 104 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `latour` | 0.3244 |
| 2 | `inteligencia` | 0.2156 |
| 3 | `artificial` | 0.2092 |
| 4 | `ciencia` | 0.1435 |
| 5 | `militar` | 0.1426 |
| 6 | `vocabulario` | 0.1370 |
| 7 | `rotulo` | 0.0948 |
| 8 | `capes` | 0.0838 |
| 9 | `catalogo` | 0.0701 |
| 10 | `rede` | 0.0694 |
| 11 | `conceito` | 0.0686 |
| 12 | `analise` | 0.0541 |
| 13 | `humano` | 0.0532 |
| 14 | `figuracoes` | 0.0525 |
| 15 | `teoria` | 0.0522 |
| 16 | `aime` | 0.0476 |
| 17 | `campo` | 0.0459 |
| 18 | `figuracao` | 0.0443 |
| 19 | `descreve` | 0.0442 |
| 20 | `tecnociencia` | 0.0358 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `laboratory` | `life` | 0.871 | 109 |
| 2 | `hope` | `pandora` | 0.869 | 123 |
| 3 | `inteligencia` | `artificial` | 0.828 | 819 |
| 4 | `university` | `press` | 0.818 | 64 |
| 5 | `interna` | `taxa` | 0.803 | 54 |
| 6 | `action` | `science` | 0.790 | 171 |
| 7 | `joler` | `crawford` | 0.740 | 41 |
| 8 | `quadro` | `conclusao` | 0.722 | 62 |
| 9 | `mediacao` | `tecnica` | 0.711 | 96 |
| 10 | `maquina` | `aprendizado` | 0.710 | 126 |
| 11 | `ator` | `teoria` | 0.707 | 152 |
| 12 | `refinada` | `contagem` | 0.647 | 46 |
| 13 | `topologico` | `textil` | 0.644 | 46 |
| 14 | `lexicometrica` | `analise` | 0.627 | 95 |
| 15 | `modelo` | `linguagem` | 0.597 | 63 |
| 16 | `ator` | `rede` | 0.593 | 154 |
| 17 | `clarifications` | `recalling` | 0.571 | 27 |
| 18 | `disponivel` | `acesso` | 0.565 | 18 |
| 19 | `brasileira` | `traducao` | 0.563 | 27 |
| 20 | `action` | `pandora` | 0.562 | 54 |
| 21 | `industria` | `militar` | 0.552 | 89 |
| 22 | `publico` | `repositorio` | 0.530 | 33 |
| 23 | `haraway` | `stengers` | 0.527 | 29 |
| 24 | `topologico` | `vocabulario` | 0.521 | 58 |
| 25 | `catalogo` | `lexical` | 0.518 | 43 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (47 termos): latour, rede, analise, teoria, tecnociencia, ator
- **Tópico 2** (36 termos): militar, rotulo, vocabulario, figuracao, aime, rotulos
- **Tópico 3** (35 termos): ciencia, humano, campo, tecnologia, antropologia, conhecimento
- **Tópico 4** (31 termos): obras, leitura, dado, capes, partir, artigos
- **Tópico 5** (23 termos): artificial, inteligencia, objeto, pesquisa, maquina, tecnica
- **Tópico 6** (6 termos): science, action, pandora, hope, laboratory, life
- **Tópico 7** (2 termos): joler, crawford

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [militar, rotulo, vocabulario] e **Tópico 5** [artificial, inteligencia, objeto] — densidade ponderada de ligação = 0.3261
- Lacuna entre **Tópico 2** [militar, rotulo, vocabulario] e **Tópico 3** [ciencia, humano, campo] — densidade ponderada de ligação = 0.3500
- Lacuna entre **Tópico 1** [latour, rede, analise] e **Tópico 4** [obras, leitura, dado] — densidade ponderada de ligação = 0.6712
- Lacuna entre **Tópico 1** [latour, rede, analise] e **Tópico 3** [ciencia, humano, campo] — densidade ponderada de ligação = 0.7173
- Lacuna entre **Tópico 3** [ciencia, humano, campo] e **Tópico 4** [obras, leitura, dado] — densidade ponderada de ligação = 0.8940
- Lacuna entre **Tópico 2** [militar, rotulo, vocabulario] e **Tópico 4** [obras, leitura, dado] — densidade ponderada de ligação = 0.9462

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
