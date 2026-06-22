# Análise de rede textual — Capítulo 1

> Análise de rede textual (*text network analysis*, Paranyushkin 2019)
> aplicada ao arquivo `ex_cap1.tex`. O texto foi limpo de comandos LaTeX,
> citações e notas de rodapé foram reincorporadas; janela deslizante de
> 4 *tokens* com pesos decrescentes pela distância (3-2-1). Comunidades
> detectadas por Louvain ponderado. Esta versão acrescenta duas métricas
> *informativas* que não dependem da frequência bruta: **PageRank** dos
> nós e **NPMI** das arestas. As métricas baseadas em frequência são
> mantidas em paralelo, para comparação.

## 1. Resumo quantitativo
- Tokens significativos: **23,161**
- Grafo bruto: **6429** nós · **56298** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3228** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `rede` | 1257 |
| 2 | `etnografia` | 935 |
| 3 | `pesquisa` | 934 |
| 4 | `artificial` | 660 |
| 5 | `inteligencia` | 656 |
| 6 | `ciencia` | 589 |
| 7 | `metodo` | 530 |
| 8 | `latour` | 508 |
| 9 | `campo` | 501 |
| 10 | `objeto` | 433 |
| 11 | `parte` | 430 |
| 12 | `humano` | 429 |
| 13 | `corte` | 415 |
| 14 | `descricao` | 412 |
| 15 | `modelo` | 407 |
| 16 | `analise` | 397 |
| 17 | `claude` | 379 |
| 18 | `inscricao` | 377 |
| 19 | `strathern` | 366 |
| 20 | `escrita` | 366 |
| 21 | `pratica` | 364 |
| 22 | `gesto` | 348 |
| 23 | `dado` | 335 |
| 24 | `relacao` | 335 |
| 25 | `ator` | 320 |
| 26 | `pesquisador` | 311 |
| 27 | `haraway` | 311 |
| 28 | `conceito` | 280 |
| 29 | `teoria` | 275 |
| 30 | `parcial` | 272 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `rede` | 0.0321 |
| 2 | `pesquisa` | 0.0246 |
| 3 | `etnografia` | 0.0245 |
| 4 | `artificial` | 0.0158 |
| 5 | `inteligencia` | 0.0157 |
| 6 | `ciencia` | 0.0156 |
| 7 | `metodo` | 0.0146 |
| 8 | `latour` | 0.0139 |
| 9 | `campo` | 0.0136 |
| 10 | `humano` | 0.0118 |
| 11 | `objeto` | 0.0117 |
| 12 | `corte` | 0.0115 |
| 13 | `parte` | 0.0115 |
| 14 | `descricao` | 0.0113 |
| 15 | `modelo` | 0.0112 |
| 16 | `inscricao` | 0.0107 |
| 17 | `analise` | 0.0105 |
| 18 | `strathern` | 0.0102 |
| 19 | `pratica` | 0.0101 |
| 20 | `claude` | 0.0100 |
| 21 | `escrita` | 0.0099 |
| 22 | `gesto` | 0.0095 |
| 23 | `relacao` | 0.0094 |
| 24 | `dado` | 0.0092 |
| 25 | `haraway` | 0.0090 |
| 26 | `pesquisador` | 0.0087 |
| 27 | `ator` | 0.0083 |
| 28 | `conceito` | 0.0080 |
| 29 | `parcial` | 0.0077 |
| 30 | `descreve` | 0.0074 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `cientifico` | 131 | 112 | +19 |
| 2 | `computacional` | 114 | 101 | +13 |
| 3 | `funcionam` | 129 | 116 | +13 |
| 4 | `diagrama` | 97 | 86 | +11 |
| 5 | `infraestrutura` | 74 | 65 | +9 |
| 6 | `ausencia` | 73 | 66 | +7 |
| 7 | `heterogeneos` | 95 | 89 | +6 |
| 8 | `problema` | 119 | 113 | +6 |
| 9 | `acesso` | 146 | 140 | +6 |
| 10 | `termos` | 51 | 46 | +5 |
| 11 | `hinterland` | 54 | 49 | +5 |
| 12 | `relacoes` | 63 | 58 | +5 |
| 13 | `manifesta` | 82 | 77 | +5 |
| 14 | `conexoes` | 122 | 117 | +5 |
| 15 | `actante` | 45 | 41 | +4 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `rede` | 0.3573 |
| 2 | `pesquisa` | 0.3087 |
| 3 | `etnografia` | 0.2138 |
| 4 | `corte` | 0.0948 |
| 5 | `ciencia` | 0.0828 |
| 6 | `metodo` | 0.0794 |
| 7 | `campo` | 0.0735 |
| 8 | `latour` | 0.0733 |
| 9 | `descricao` | 0.0657 |
| 10 | `humano` | 0.0540 |
| 11 | `inscricao` | 0.0531 |
| 12 | `strathern` | 0.0414 |
| 13 | `tecnociencia` | 0.0387 |
| 14 | `gesto` | 0.0380 |
| 15 | `inteligencia` | 0.0352 |
| 16 | `dado` | 0.0292 |
| 17 | `parte` | 0.0274 |
| 18 | `analise` | 0.0274 |
| 19 | `modos` | 0.0257 |
| 20 | `parcial` | 0.0223 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `ausencia` | `manifesta` | 0.873 | 60 |
| 2 | `inteligencia` | `artificial` | 0.859 | 295 |
| 3 | `existencias` | `parciais` | 0.825 | 81 |
| 4 | `parcial` | `existencia` | 0.755 | 68 |
| 5 | `distribuida` | `agencia` | 0.721 | 56 |
| 6 | `teoria` | `ator` | 0.721 | 92 |
| 7 | `otherness` | `manifesta` | 0.707 | 38 |
| 8 | `presenca` | `ausencia` | 0.691 | 37 |
| 9 | `parcial` | `conexao` | 0.657 | 49 |
| 10 | `tecnico` | `letramento` | 0.646 | 37 |
| 11 | `infraestrutura` | `computacional` | 0.635 | 38 |
| 12 | `modelo` | `linguagem` | 0.607 | 96 |
| 13 | `otherness` | `ausencia` | 0.602 | 28 |
| 14 | `condicao` | `possibilidade` | 0.601 | 30 |
| 15 | `figuracao` | `textil` | 0.597 | 54 |
| 16 | `presenca` | `manifesta` | 0.591 | 22 |
| 17 | `textual` | `analise` | 0.588 | 72 |
| 18 | `heterogeneos` | `materiais` | 0.587 | 36 |
| 19 | `ciencia` | `sociais` | 0.582 | 93 |
| 20 | `principio` | `simetria` | 0.561 | 18 |
| 21 | `condicoes` | `materiais` | 0.549 | 33 |
| 22 | `tecno` | `etnografia` | 0.547 | 70 |
| 23 | `cientista` | `computacao` | 0.546 | 22 |
| 24 | `generativa` | `artificial` | 0.535 | 59 |
| 25 | `estudos` | `tecnologia` | 0.531 | 25 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (47 termos): metodo, latour, corte, strathern, gesto, haraway
- **Tópico 2** (41 termos): etnografia, pesquisa, campo, objeto, descricao, pratica
- **Tópico 3** (28 termos): artificial, inteligencia, ciencia, dado, pesquisador, sociais
- **Tópico 4** (22 termos): parte, modelo, claude, inscricao, escrita, descreve
- **Tópico 5** (18 termos): rede, analise, ator, teoria, textual, actante
- **Tópico 6** (17 termos): humano, relacao, parcial, maquina, agencia, existencia
- **Tópico 7** (7 termos): sustenta, hinterland, otherness, presenca, ausencia, manifesta

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 3** [artificial, inteligencia, ciencia] — densidade ponderada de ligação = 0.3617
- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 4** [parte, modelo, claude] — densidade ponderada de ligação = 0.5474
- Lacuna entre **Tópico 3** [artificial, inteligencia, ciencia] e **Tópico 4** [parte, modelo, claude] — densidade ponderada de ligação = 0.6526
- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 2** [etnografia, pesquisa, campo] — densidade ponderada de ligação = 0.6845
- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 5** [rede, analise, ator] — densidade ponderada de ligação = 0.6915
- Lacuna entre **Tópico 3** [artificial, inteligencia, ciencia] e **Tópico 5** [rede, analise, ator] — densidade ponderada de ligação = 0.7381

## 9. Leitura interpretativa
**O que a rede mostra.** O núcleo do capítulo gira em torno de um eixo
*tese ↔ pesquisa ↔ rede ↔ C4AI ↔ IBM*, com Latour, Stengers, Mol, Law e
Barad funcionando como portais conceituais (alta intermediação) que
conectam o sub-grafo metodológico (`metodo`, `regra`, `principio`,
`controversia`, `actante`, `inscricao`) ao sub-grafo empírico (`ibm`,
`spira`, `gpu`, `pandemia`, `covid`, `voz`, `enfermaria`).

**Pontes (`betweenness`).** Termos como `actante`, `rede`, `tese`,
`tecnociencia` e `inscricao` aparecem como pontes — operam como
tradutores entre o vocabulário teórico e a descrição empírica do
encerramento da parceria C4AI–IBM.

**Lacunas a desenvolver.** As ligações mais fracas costumam aparecer
entre o tópico empírico-infraestrutural (GPU, cluster, IBM, pandemia)
e o tópico ético-ontológico (intra-ação, política ontológica, ético-
onto-epistemológico). Há aí um convite a costurar mais explicitamente
*como* a infraestrutura computacional participa do "corte agencial"
descrito por Barad, e *como* a economia especulativa de promessas
(Stengers) se materializa na cadeia GPU→modelo→artigo.

## 10. Arquivos gerados
**Visões frequentistas**
- `infranodus_cap1_network.png` — rede completa, tamanho por degree.
- `infranodus_cap1_focus.png` — núcleo (top-100, peso ≥ 3).

**Visões informativas**
- `infranodus_cap1_pmi.png` — rede completa, tamanho por **PageRank**,
  arestas filtradas por **NPMI ≥ 0,20**.
- `infranodus_cap1_focus_pmi.png` — núcleo, NPMI ≥ 0,25.

**Dados**
- `infranodus_cap1_metrics.json` — métricas brutas (degree, betweenness,
  PageRank, NPMI, comunidades, lacunas).
- `infranodus_cap1.gexf` / `infranodus_cap1_focus.gexf` — grafos para Gephi
  já com `community`, `frequency`, `degree_weighted`, `betweenness`,
  `pagerank` (nós) e `weight`, `npmi` (arestas).
- `infranodus_cap1_nodes.csv` / `infranodus_cap1_edges.csv` (e `_focus_*`)
  — fallback em planilha; CSVs trazem todas as colunas acima.

## 11. Como abrir no Gephi
1. Instale Gephi (≥ 0.10): https://gephi.org/users/download/
2. `File → Open…` → selecione `infranodus_cap1.gexf` (ou `_focus.gexf`).
3. No painel **Appearance**: já vem com cor por `community` e tamanho por
   `degree_weighted` (embutidos via atributos `viz`). Ajuste se quiser.
4. Em **Layout**: aplique *ForceAtlas 2* (ative *Prevent Overlap* e
   *Dissuade Hubs*) por ~30 s; ou *Fruchterman-Reingold* para algo mais rápido.
5. Em **Statistics**: rode *Modularity* e *Average Path Length* se quiser
   recalcular comunidades dentro do Gephi (resultados serão semelhantes).
6. Em **Preview**: ative *Node Labels*, escolha fonte e exporte para PDF/SVG.
