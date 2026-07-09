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
- Tokens significativos: **22,696**
- Grafo bruto: **6513** nós · **57302** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3237** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `rede` | 1269 |
| 2 | `pesquisa` | 965 |
| 3 | `etnografia` | 923 |
| 4 | `artificial` | 698 |
| 5 | `inteligencia` | 693 |
| 6 | `ciencia` | 601 |
| 7 | `latour` | 595 |
| 8 | `campo` | 542 |
| 9 | `metodo` | 518 |
| 10 | `objeto` | 488 |
| 11 | `corte` | 459 |
| 12 | `humano` | 429 |
| 13 | `descricao` | 412 |
| 14 | `pratica` | 390 |
| 15 | `strathern` | 374 |
| 16 | `inscricao` | 360 |
| 17 | `modelo` | 358 |
| 18 | `relacao` | 351 |
| 19 | `analise` | 337 |
| 20 | `ator` | 336 |
| 21 | `dado` | 328 |
| 22 | `maquina` | 322 |
| 23 | `gesto` | 320 |
| 24 | `parte` | 313 |
| 25 | `haraway` | 308 |
| 26 | `teoria` | 302 |
| 27 | `descreve` | 278 |
| 28 | `sociais` | 270 |
| 29 | `conceito` | 267 |
| 30 | `claude` | 264 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `rede` | 0.0330 |
| 2 | `pesquisa` | 0.0255 |
| 3 | `etnografia` | 0.0244 |
| 4 | `artificial` | 0.0166 |
| 5 | `inteligencia` | 0.0165 |
| 6 | `latour` | 0.0160 |
| 7 | `ciencia` | 0.0158 |
| 8 | `campo` | 0.0147 |
| 9 | `metodo` | 0.0143 |
| 10 | `objeto` | 0.0132 |
| 11 | `corte` | 0.0126 |
| 12 | `humano` | 0.0121 |
| 13 | `descricao` | 0.0113 |
| 14 | `pratica` | 0.0108 |
| 15 | `strathern` | 0.0105 |
| 16 | `inscricao` | 0.0104 |
| 17 | `modelo` | 0.0102 |
| 18 | `relacao` | 0.0099 |
| 19 | `analise` | 0.0093 |
| 20 | `maquina` | 0.0092 |
| 21 | `dado` | 0.0091 |
| 22 | `haraway` | 0.0090 |
| 23 | `parte` | 0.0089 |
| 24 | `gesto` | 0.0089 |
| 25 | `ator` | 0.0087 |
| 26 | `descreve` | 0.0080 |
| 27 | `teoria` | 0.0078 |
| 28 | `conceito` | 0.0077 |
| 29 | `claude` | 0.0075 |
| 30 | `sociais` | 0.0075 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `cientifico` | 139 | 124 | +15 |
| 2 | `diagrama` | 106 | 92 | +14 |
| 3 | `instituicao` | 94 | 84 | +10 |
| 4 | `computacional` | 109 | 99 | +10 |
| 5 | `infraestrutura` | 72 | 64 | +8 |
| 6 | `acesso` | 115 | 108 | +7 |
| 7 | `funcionam` | 122 | 115 | +7 |
| 8 | `decisao` | 134 | 127 | +7 |
| 9 | `fato` | 141 | 135 | +6 |
| 10 | `termos` | 50 | 45 | +5 |
| 11 | `cortes` | 102 | 97 | +5 |
| 12 | `disponivel` | 153 | 148 | +5 |
| 13 | `materiais` | 38 | 34 | +4 |
| 14 | `actante` | 52 | 48 | +4 |
| 15 | `ausencia` | 56 | 52 | +4 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `rede` | 0.3934 |
| 2 | `pesquisa` | 0.2632 |
| 3 | `etnografia` | 0.2021 |
| 4 | `latour` | 0.1505 |
| 5 | `corte` | 0.1186 |
| 6 | `campo` | 0.0878 |
| 7 | `ciencia` | 0.0745 |
| 8 | `metodo` | 0.0610 |
| 9 | `descricao` | 0.0589 |
| 10 | `inscricao` | 0.0566 |
| 11 | `humano` | 0.0475 |
| 12 | `objeto` | 0.0415 |
| 13 | `strathern` | 0.0400 |
| 14 | `tecnociencia` | 0.0368 |
| 15 | `maquina` | 0.0314 |
| 16 | `dado` | 0.0266 |
| 17 | `claude` | 0.0257 |
| 18 | `modos` | 0.0254 |
| 19 | `parcial` | 0.0227 |
| 20 | `hinterland` | 0.0210 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `ausencia` | `manifesta` | 0.864 | 67 |
| 2 | `artificial` | `inteligencia` | 0.857 | 310 |
| 3 | `parciais` | `existencias` | 0.825 | 81 |
| 4 | `existencia` | `parcial` | 0.744 | 59 |
| 5 | `teoria` | `ator` | 0.727 | 101 |
| 6 | `agencia` | `distribuida` | 0.725 | 52 |
| 7 | `ausencia` | `presenca` | 0.706 | 43 |
| 8 | `manifesta` | `otherness` | 0.683 | 40 |
| 9 | `tecnico` | `letramento` | 0.654 | 46 |
| 10 | `conexao` | `parcial` | 0.639 | 43 |
| 11 | `computacional` | `infraestrutura` | 0.630 | 38 |
| 12 | `presenca` | `manifesta` | 0.621 | 28 |
| 13 | `ausencia` | `otherness` | 0.616 | 34 |
| 14 | `modelo` | `linguagem` | 0.610 | 84 |
| 15 | `figuracao` | `textil` | 0.599 | 54 |
| 16 | `heterogeneos` | `materiais` | 0.598 | 36 |
| 17 | `ciencia` | `sociais` | 0.580 | 94 |
| 18 | `analise` | `textual` | 0.563 | 54 |
| 19 | `artificial` | `generativa` | 0.553 | 62 |
| 20 | `tecno` | `etnografia` | 0.553 | 73 |
| 21 | `computacao` | `cientista` | 0.550 | 22 |
| 22 | `simetria` | `principio` | 0.546 | 18 |
| 23 | `acesso` | `disponivel` | 0.543 | 18 |
| 24 | `presenca` | `otherness` | 0.543 | 25 |
| 25 | `materiais` | `condicoes` | 0.539 | 31 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (43 termos): pesquisa, etnografia, campo, metodo, descricao, pratica
- **Tópico 2** (40 termos): latour, corte, strathern, gesto, haraway, conceito
- **Tópico 3** (28 termos): artificial, inteligencia, objeto, modelo, claude, laboratorio
- **Tópico 4** (19 termos): humano, relacao, maquina, parcial, plano, agencia
- **Tópico 5** (16 termos): rede, analise, ator, teoria, termos, actante
- **Tópico 6** (15 termos): inscricao, parte, descreve, tecnociencia, modos, diagrama
- **Tópico 7** (12 termos): ciencia, dado, sociais, tecnologia, tecnico, letramento
- **Tópico 8** (7 termos): hinterland, otherness, ausencia, presenca, manifesta, palavra

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [latour, corte, strathern] e **Tópico 3** [artificial, inteligencia, objeto] — densidade ponderada de ligação = 0.3223
- Lacuna entre **Tópico 1** [pesquisa, etnografia, campo] e **Tópico 4** [humano, relacao, maquina] — densidade ponderada de ligação = 0.5435
- Lacuna entre **Tópico 2** [latour, corte, strathern] e **Tópico 4** [humano, relacao, maquina] — densidade ponderada de ligação = 0.6158
- Lacuna entre **Tópico 3** [artificial, inteligencia, objeto] e **Tópico 4** [humano, relacao, maquina] — densidade ponderada de ligação = 0.6241
- Lacuna entre **Tópico 4** [humano, relacao, maquina] e **Tópico 5** [rede, analise, ator] — densidade ponderada de ligação = 0.7303
- Lacuna entre **Tópico 3** [artificial, inteligencia, objeto] e **Tópico 5** [rede, analise, ator] — densidade ponderada de ligação = 0.7589

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
