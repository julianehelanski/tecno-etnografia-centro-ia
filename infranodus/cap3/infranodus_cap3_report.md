# Análise de rede textual — Capítulo 3

> Análise de rede textual (*text network analysis*, Paranyushkin 2019)
> aplicada ao arquivo `ex_cap3.tex`. O texto foi limpo de comandos LaTeX,
> citações e notas de rodapé foram reincorporadas; janela deslizante de
> 4 *tokens* com pesos decrescentes pela distância (3-2-1). Comunidades
> detectadas por Louvain ponderado. Esta versão acrescenta duas métricas
> *informativas* que não dependem da frequência bruta: **PageRank** dos
> nós e **NPMI** das arestas. As métricas baseadas em frequência são
> mantidas em paralelo, para comparação.

## 1. Resumo quantitativo
- Tokens significativos: **17,888**
- Grafo bruto: **5348** nós · **46033** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2572** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 796 |
| 2 | `pesquisa` | 717 |
| 3 | `rede` | 602 |
| 4 | `centro` | 539 |
| 5 | `fabio` | 501 |
| 6 | `publico` | 438 |
| 7 | `arranjo` | 398 |
| 8 | `seguir` | 393 |
| 9 | `corporacao` | 364 |
| 10 | `inteligencia` | 317 |
| 11 | `brasil` | 309 |
| 12 | `artificial` | 302 |
| 13 | `hollerith` | 301 |
| 14 | `ator` | 299 |
| 15 | `tecnologia` | 293 |
| 16 | `laboratorio` | 284 |
| 17 | `infraestrutura` | 255 |
| 18 | `ecossistema` | 253 |
| 19 | `fapesp` | 244 |
| 20 | `empresa` | 242 |
| 21 | `cientifico` | 239 |
| 22 | `trajetoria` | 232 |
| 23 | `universidade` | 231 |
| 24 | `instituicao` | 229 |
| 25 | `modelo` | 228 |
| 26 | `maquina` | 228 |
| 27 | `associacao` | 213 |
| 28 | `campo` | 209 |
| 29 | `informacao` | 208 |
| 30 | `encerramento` | 200 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `claudio` | 0.0270 |
| 2 | `pesquisa` | 0.0260 |
| 3 | `rede` | 0.0221 |
| 4 | `centro` | 0.0196 |
| 5 | `fabio` | 0.0169 |
| 6 | `publico` | 0.0162 |
| 7 | `arranjo` | 0.0148 |
| 8 | `seguir` | 0.0142 |
| 9 | `corporacao` | 0.0138 |
| 10 | `hollerith` | 0.0119 |
| 11 | `tecnologia` | 0.0117 |
| 12 | `brasil` | 0.0117 |
| 13 | `ator` | 0.0113 |
| 14 | `inteligencia` | 0.0112 |
| 15 | `artificial` | 0.0107 |
| 16 | `laboratorio` | 0.0106 |
| 17 | `infraestrutura` | 0.0102 |
| 18 | `ecossistema` | 0.0096 |
| 19 | `empresa` | 0.0095 |
| 20 | `fapesp` | 0.0094 |
| 21 | `modelo` | 0.0093 |
| 22 | `cientifico` | 0.0092 |
| 23 | `trajetoria` | 0.0092 |
| 24 | `maquina` | 0.0091 |
| 25 | `universidade` | 0.0089 |
| 26 | `instituicao` | 0.0088 |
| 27 | `associacao` | 0.0083 |
| 28 | `campo` | 0.0083 |
| 29 | `partir` | 0.0077 |
| 30 | `encerramento` | 0.0077 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `natural` | 117 | 96 | +21 |
| 2 | `conta` | 142 | 124 | +18 |
| 3 | `linguagem` | 84 | 71 | +13 |
| 4 | `estatistica` | 113 | 102 | +11 |
| 5 | `dependencia` | 100 | 90 | +10 |
| 6 | `tecnica` | 68 | 59 | +9 |
| 7 | `projetos` | 129 | 120 | +9 |
| 8 | `processamento` | 91 | 83 | +8 |
| 9 | `unidos` | 95 | 87 | +8 |
| 10 | `pratica` | 122 | 114 | +8 |
| 11 | `mostra` | 170 | 162 | +8 |
| 12 | `conhecimento` | 96 | 89 | +7 |
| 13 | `censo` | 104 | 97 | +7 |
| 14 | `financiamento` | 72 | 66 | +6 |
| 15 | `tecnociencia` | 137 | 131 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `centro` | 0.2418 |
| 2 | `rede` | 0.2213 |
| 3 | `pesquisa` | 0.2210 |
| 4 | `claudio` | 0.1721 |
| 5 | `fabio` | 0.1267 |
| 6 | `publico` | 0.1131 |
| 7 | `corporacao` | 0.0854 |
| 8 | `seguir` | 0.0812 |
| 9 | `tecnologia` | 0.0762 |
| 10 | `ator` | 0.0754 |
| 11 | `hollerith` | 0.0671 |
| 12 | `ecossistema` | 0.0531 |
| 13 | `cientifico` | 0.0526 |
| 14 | `brasil` | 0.0463 |
| 15 | `modelo` | 0.0411 |
| 16 | `fapesp` | 0.0334 |
| 17 | `empresa` | 0.0307 |
| 18 | `inteligencia` | 0.0306 |
| 19 | `trajetoria` | 0.0304 |
| 20 | `dado` | 0.0287 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `informacao` | `verbal` | 0.871 | 80 |
| 2 | `inteligencia` | `artificial` | 0.871 | 147 |
| 3 | `unidos` | `estados` | 0.859 | 57 |
| 4 | `porta` | `voz` | 0.858 | 53 |
| 5 | `linguagem` | `natural` | 0.824 | 42 |
| 6 | `relatorios` | `anuais` | 0.759 | 43 |
| 7 | `aberto` | `codigo` | 0.748 | 45 |
| 8 | `linguagem` | `processamento` | 0.728 | 30 |
| 9 | `processamento` | `natural` | 0.658 | 20 |
| 10 | `historica` | `investigacao` | 0.631 | 24 |
| 11 | `elaboracao` | `base` | 0.601 | 21 |
| 12 | `acesso` | `disponivel` | 0.597 | 30 |
| 13 | `passagem` | `ponto` | 0.589 | 30 |
| 14 | `claudio` | `fabio` | 0.583 | 168 |
| 15 | `novembro` | `dezembro` | 0.565 | 23 |
| 16 | `research` | `brasil` | 0.544 | 38 |
| 17 | `inovacao` | `ecossistema` | 0.532 | 46 |
| 18 | `translacao` | `cadeias` | 0.531 | 15 |
| 19 | `cientifico` | `producao` | 0.520 | 37 |
| 20 | `relatorios` | `elaboracao` | 0.512 | 16 |
| 21 | `mapa` | `problemas` | 0.506 | 12 |
| 22 | `gente` | `dinheiro` | 0.497 | 15 |
| 23 | `research` | `fechamento` | 0.488 | 12 |
| 24 | `relatorios` | `base` | 0.487 | 18 |
| 25 | `hollerith` | `maquina` | 0.481 | 54 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (46 termos): corporacao, hollerith, tecnologia, infraestrutura, empresa, trajetoria
- **Tópico 2** (33 termos): pesquisa, centro, fapesp, cientifico, partir, relatorios
- **Tópico 3** (31 termos): rede, ator, associacao, descrevo, ponto, analise
- **Tópico 4** (24 termos): publico, arranjo, brasil, laboratorio, universidade, instituicao
- **Tópico 5** (19 termos): claudio, fabio, seguir, campo, informacao, verbal
- **Tópico 6** (13 termos): inteligencia, artificial, ecossistema, inovacao, brasileiro, historica
- **Tópico 7** (11 termos): modelo, codigo, aberto, negocio, linguagem, processamento
- **Tópico 8** (3 termos): estados, unidos, censo

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [pesquisa, centro, fapesp] e **Tópico 3** [rede, ator, associacao] — densidade ponderada de ligação = 0.3519
- Lacuna entre **Tópico 1** [corporacao, hollerith, tecnologia] e **Tópico 2** [pesquisa, centro, fapesp] — densidade ponderada de ligação = 0.3610
- Lacuna entre **Tópico 1** [corporacao, hollerith, tecnologia] e **Tópico 5** [claudio, fabio, seguir] — densidade ponderada de ligação = 0.3741
- Lacuna entre **Tópico 3** [rede, ator, associacao] e **Tópico 4** [publico, arranjo, brasil] — densidade ponderada de ligação = 0.4019
- Lacuna entre **Tópico 1** [corporacao, hollerith, tecnologia] e **Tópico 3** [rede, ator, associacao] — densidade ponderada de ligação = 0.4292
- Lacuna entre **Tópico 1** [corporacao, hollerith, tecnologia] e **Tópico 4** [publico, arranjo, brasil] — densidade ponderada de ligação = 0.4973

## 9. Leitura interpretativa
_Leitura interpretativa ainda não escrita para este capítulo. Crie `interpretation_cap3.md` ao lado dos outputs para que o conteúdo seja embutido aqui automaticamente._

## 10. Arquivos gerados
**Visões frequentistas**
- `infranodus_cap3_network.png` — rede completa, tamanho por degree.
- `infranodus_cap3_focus.png` — núcleo (top-100, peso ≥ 3).

**Visões informativas**
- `infranodus_cap3_pmi.png` — rede completa, tamanho por **PageRank**,
  arestas filtradas por **NPMI ≥ 0,20**.
- `infranodus_cap3_focus_pmi.png` — núcleo, NPMI ≥ 0,25.

**Dados**
- `infranodus_cap3_metrics.json` — métricas brutas (degree, betweenness,
  PageRank, NPMI, comunidades, lacunas).
- `infranodus_cap3.gexf` / `infranodus_cap3_focus.gexf` — grafos para Gephi
  já com `community`, `frequency`, `degree_weighted`, `betweenness`,
  `pagerank` (nós) e `weight`, `npmi` (arestas).
- `infranodus_cap3_nodes.csv` / `infranodus_cap3_edges.csv` (e `_focus_*`)
  — fallback em planilha; CSVs trazem todas as colunas acima.

## 11. Como abrir no Gephi
1. Instale Gephi (≥ 0.10): https://gephi.org/users/download/
2. `File → Open…` → selecione `infranodus_cap3.gexf` (ou `_focus.gexf`).
3. No painel **Appearance**: já vem com cor por `community` e tamanho por
   `degree_weighted` (embutidos via atributos `viz`). Ajuste se quiser.
4. Em **Layout**: aplique *ForceAtlas 2* (ative *Prevent Overlap* e
   *Dissuade Hubs*) por ~30 s; ou *Fruchterman-Reingold* para algo mais rápido.
5. Em **Statistics**: rode *Modularity* e *Average Path Length* se quiser
   recalcular comunidades dentro do Gephi (resultados serão semelhantes).
6. Em **Preview**: ative *Node Labels*, escolha fonte e exporte para PDF/SVG.
