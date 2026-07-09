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
- Tokens significativos: **18,907**
- Grafo bruto: **5696** nós · **49187** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2602** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 897 |
| 2 | `pesquisa` | 724 |
| 3 | `rede` | 551 |
| 4 | `fabio` | 532 |
| 5 | `centro` | 503 |
| 6 | `seguir` | 359 |
| 7 | `inteligencia` | 346 |
| 8 | `artificial` | 345 |
| 9 | `arranjo` | 342 |
| 10 | `publico` | 341 |
| 11 | `brasil` | 333 |
| 12 | `corporacao` | 333 |
| 13 | `tecnologia` | 322 |
| 14 | `maquina` | 303 |
| 15 | `fapesp` | 298 |
| 16 | `ecossistema` | 293 |
| 17 | `ator` | 283 |
| 18 | `hollerith` | 274 |
| 19 | `laboratorio` | 271 |
| 20 | `dado` | 265 |
| 21 | `modelo` | 264 |
| 22 | `empresa` | 257 |
| 23 | `informacao` | 236 |
| 24 | `universidade` | 235 |
| 25 | `campo` | 215 |
| 26 | `instituicao` | 215 |
| 27 | `associacao` | 211 |
| 28 | `verbal` | 208 |
| 29 | `infraestrutura` | 207 |
| 30 | `trajetoria` | 207 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `claudio` | 0.0307 |
| 2 | `pesquisa` | 0.0263 |
| 3 | `rede` | 0.0204 |
| 4 | `centro` | 0.0183 |
| 5 | `fabio` | 0.0181 |
| 6 | `seguir` | 0.0134 |
| 7 | `arranjo` | 0.0130 |
| 8 | `corporacao` | 0.0128 |
| 9 | `publico` | 0.0128 |
| 10 | `tecnologia` | 0.0128 |
| 11 | `brasil` | 0.0126 |
| 12 | `inteligencia` | 0.0121 |
| 13 | `artificial` | 0.0121 |
| 14 | `maquina` | 0.0116 |
| 15 | `fapesp` | 0.0116 |
| 16 | `hollerith` | 0.0109 |
| 17 | `ecossistema` | 0.0108 |
| 18 | `ator` | 0.0108 |
| 19 | `dado` | 0.0107 |
| 20 | `modelo` | 0.0105 |
| 21 | `laboratorio` | 0.0102 |
| 22 | `empresa` | 0.0099 |
| 23 | `universidade` | 0.0090 |
| 24 | `campo` | 0.0085 |
| 25 | `instituicao` | 0.0084 |
| 26 | `infraestrutura` | 0.0084 |
| 27 | `trajetoria` | 0.0083 |
| 28 | `associacao` | 0.0083 |
| 29 | `informacao` | 0.0081 |
| 30 | `pergunta` | 0.0080 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `conta` | 148 | 126 | +22 |
| 2 | `vida` | 171 | 158 | +13 |
| 3 | `estatistica` | 112 | 102 | +10 |
| 4 | `mostra` | 136 | 127 | +9 |
| 5 | `tecnica` | 66 | 58 | +8 |
| 6 | `humano` | 89 | 81 | +8 |
| 7 | `indigenas` | 101 | 93 | +8 |
| 8 | `linguas` | 107 | 99 | +8 |
| 9 | `actante` | 69 | 63 | +6 |
| 10 | `unidos` | 73 | 67 | +6 |
| 11 | `pratica` | 84 | 78 | +6 |
| 12 | `relacoes` | 96 | 90 | +6 |
| 13 | `cadeia` | 116 | 110 | +6 |
| 14 | `censo` | 134 | 128 | +6 |
| 15 | `pessoas` | 165 | 159 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `pesquisa` | 0.3108 |
| 2 | `centro` | 0.2565 |
| 3 | `claudio` | 0.2174 |
| 4 | `rede` | 0.1670 |
| 5 | `fabio` | 0.1360 |
| 6 | `tecnologia` | 0.0826 |
| 7 | `inteligencia` | 0.0716 |
| 8 | `dado` | 0.0711 |
| 9 | `seguir` | 0.0691 |
| 10 | `fapesp` | 0.0669 |
| 11 | `hollerith` | 0.0643 |
| 12 | `ator` | 0.0590 |
| 13 | `brasil` | 0.0510 |
| 14 | `ecossistema` | 0.0476 |
| 15 | `corporacao` | 0.0447 |
| 16 | `empresa` | 0.0429 |
| 17 | `artificial` | 0.0421 |
| 18 | `maquina` | 0.0406 |
| 19 | `trajetoria` | 0.0373 |
| 20 | `entrevistas` | 0.0344 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `verbal` | `informacao` | 0.872 | 83 |
| 2 | `inteligencia` | `artificial` | 0.864 | 150 |
| 3 | `estados` | `unidos` | 0.860 | 54 |
| 4 | `indigenas` | `linguas` | 0.782 | 40 |
| 5 | `linguagem` | `natural` | 0.750 | 46 |
| 6 | `codigo` | `aberto` | 0.733 | 54 |
| 7 | `processamento` | `natural` | 0.695 | 28 |
| 8 | `processamento` | `linguagem` | 0.676 | 40 |
| 9 | `disponivel` | `acesso` | 0.654 | 40 |
| 10 | `maquina` | `aprendizado` | 0.648 | 53 |
| 11 | `historica` | `investigacao` | 0.619 | 24 |
| 12 | `claudio` | `fabio` | 0.580 | 183 |
| 13 | `research` | `brasil` | 0.573 | 51 |
| 14 | `ecossistema` | `inovacao` | 0.550 | 58 |
| 15 | `laboratorio` | `fechamento` | 0.516 | 34 |
| 16 | `tabulacao` | `hollerith` | 0.512 | 39 |
| 17 | `contexto` | `brasileiro` | 0.508 | 12 |
| 18 | `comercial` | `tecnica` | 0.502 | 19 |
| 19 | `claudio` | `informacao` | 0.490 | 72 |
| 20 | `tabulacao` | `sistema` | 0.487 | 24 |
| 21 | `gente` | `dinheiro` | 0.487 | 15 |
| 22 | `entrevistas` | `documentos` | 0.485 | 21 |
| 23 | `fapesp` | `convenio` | 0.484 | 23 |
| 24 | `observacao` | `entrevistas` | 0.482 | 20 |
| 25 | `translacao` | `cadeia` | 0.459 | 12 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (35 termos): rede, seguir, ator, campo, associacao, entrevistas
- **Tópico 2** (33 termos): publico, corporacao, ecossistema, empresa, universidade, instituicao
- **Tópico 3** (32 termos): tecnologia, maquina, hollerith, tabulacao, ciencia, aprendizado
- **Tópico 4** (30 termos): pesquisa, centro, arranjo, fapesp, analise, cientifico
- **Tópico 5** (19 termos): inteligencia, artificial, brasil, laboratorio, pesquisador, acesso
- **Tópico 6** (18 termos): dado, modelo, codigo, linguagem, aberto, processamento
- **Tópico 7** (13 termos): claudio, fabio, informacao, verbal, pergunta, bluetalks

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [rede, seguir, ator] e **Tópico 5** [inteligencia, artificial, brasil] — densidade ponderada de ligação = 0.3083
- Lacuna entre **Tópico 1** [rede, seguir, ator] e **Tópico 3** [tecnologia, maquina, hollerith] — densidade ponderada de ligação = 0.3375
- Lacuna entre **Tópico 1** [rede, seguir, ator] e **Tópico 2** [publico, corporacao, ecossistema] — densidade ponderada de ligação = 0.3957
- Lacuna entre **Tópico 3** [tecnologia, maquina, hollerith] e **Tópico 4** [pesquisa, centro, arranjo] — densidade ponderada de ligação = 0.4146
- Lacuna entre **Tópico 2** [publico, corporacao, ecossistema] e **Tópico 3** [tecnologia, maquina, hollerith] — densidade ponderada de ligação = 0.4375
- Lacuna entre **Tópico 3** [tecnologia, maquina, hollerith] e **Tópico 5** [inteligencia, artificial, brasil] — densidade ponderada de ligação = 0.4622

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
