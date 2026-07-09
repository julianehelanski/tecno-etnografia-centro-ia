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
- Tokens significativos: **32,765**
- Grafo bruto: **6757** nós · **78125** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4024** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 1902 |
| 2 | `covideiro` | 1183 |
| 3 | `inscricao` | 1102 |
| 4 | `cadeia` | 1027 |
| 5 | `rede` | 944 |
| 6 | `artigo` | 890 |
| 7 | `objeto` | 886 |
| 8 | `respiratoria` | 765 |
| 9 | `dado` | 730 |
| 10 | `insuficiencia` | 730 |
| 11 | `modelo` | 666 |
| 12 | `projeto` | 655 |
| 13 | `marcelo` | 617 |
| 14 | `espectrograma` | 537 |
| 15 | `artigos` | 527 |
| 16 | `coleta` | 505 |
| 17 | `actante` | 461 |
| 18 | `condicoes` | 436 |
| 19 | `cientifico` | 430 |
| 20 | `covid` | 420 |
| 21 | `pratica` | 417 |
| 22 | `audio` | 414 |
| 23 | `partir` | 403 |
| 24 | `sinal` | 386 |
| 25 | `pacientes` | 385 |
| 26 | `ruido` | 376 |
| 27 | `analise` | 371 |
| 28 | `secao` | 360 |
| 29 | `laboratorio` | 350 |
| 30 | `torna` | 350 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0373 |
| 2 | `covideiro` | 0.0234 |
| 3 | `inscricao` | 0.0222 |
| 4 | `cadeia` | 0.0206 |
| 5 | `rede` | 0.0190 |
| 6 | `objeto` | 0.0179 |
| 7 | `artigo` | 0.0178 |
| 8 | `dado` | 0.0148 |
| 9 | `respiratoria` | 0.0145 |
| 10 | `modelo` | 0.0139 |
| 11 | `insuficiencia` | 0.0138 |
| 12 | `projeto` | 0.0132 |
| 13 | `marcelo` | 0.0126 |
| 14 | `espectrograma` | 0.0113 |
| 15 | `artigos` | 0.0106 |
| 16 | `coleta` | 0.0105 |
| 17 | `actante` | 0.0097 |
| 18 | `condicoes` | 0.0091 |
| 19 | `pratica` | 0.0090 |
| 20 | `audio` | 0.0089 |
| 21 | `covid` | 0.0088 |
| 22 | `cientifico` | 0.0088 |
| 23 | `partir` | 0.0085 |
| 24 | `sinal` | 0.0084 |
| 25 | `ruido` | 0.0083 |
| 26 | `pacientes` | 0.0081 |
| 27 | `torna` | 0.0078 |
| 28 | `secao` | 0.0078 |
| 29 | `analise` | 0.0077 |
| 30 | `ponto` | 0.0076 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `escala` | 81 | 66 | +15 |
| 2 | `processo` | 117 | 107 | +10 |
| 3 | `leitor` | 127 | 118 | +9 |
| 4 | `clinica` | 87 | 79 | +8 |
| 5 | `coeficientes` | 96 | 88 | +8 |
| 6 | `pesquisa` | 74 | 67 | +7 |
| 7 | `processamento` | 76 | 69 | +7 |
| 8 | `resultado` | 88 | 81 | +7 |
| 9 | `existir` | 115 | 109 | +6 |
| 10 | `acesso` | 128 | 122 | +6 |
| 11 | `grade` | 138 | 132 | +6 |
| 12 | `parte` | 151 | 145 | +6 |
| 13 | `microfone` | 154 | 148 | +6 |
| 14 | `parametros` | 157 | 151 | +6 |
| 15 | `analitico` | 163 | 157 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.5503 |
| 2 | `inscricao` | 0.2291 |
| 3 | `covideiro` | 0.2074 |
| 4 | `cadeia` | 0.1266 |
| 5 | `artigo` | 0.0974 |
| 6 | `rede` | 0.0964 |
| 7 | `objeto` | 0.0937 |
| 8 | `respiratoria` | 0.0749 |
| 9 | `modelo` | 0.0745 |
| 10 | `espectrograma` | 0.0646 |
| 11 | `dado` | 0.0638 |
| 12 | `projeto` | 0.0485 |
| 13 | `insuficiencia` | 0.0328 |
| 14 | `coleta` | 0.0326 |
| 15 | `ruido` | 0.0293 |
| 16 | `sinal` | 0.0282 |
| 17 | `marcelo` | 0.0259 |
| 18 | `pratica` | 0.0259 |
| 19 | `torna` | 0.0237 |
| 20 | `instituicao` | 0.0213 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `respiratoria` | `insuficiencia` | 0.844 | 308 |
| 2 | `movel` | `imutavel` | 0.842 | 81 |
| 3 | `calculo` | `centro` | 0.771 | 85 |
| 4 | `clinica` | `escuta` | 0.640 | 42 |
| 5 | `neural` | `rede` | 0.591 | 127 |
| 6 | `programa` | `acao` | 0.566 | 38 |
| 7 | `acustico` | `sinal` | 0.548 | 61 |
| 8 | `tornou` | `possivel` | 0.535 | 34 |
| 9 | `mapa` | `analitico` | 0.529 | 25 |
| 10 | `processamento` | `linguagem` | 0.525 | 27 |
| 11 | `marcelo` | `entrevista` | 0.504 | 100 |
| 12 | `publico` | `repositorio` | 0.497 | 24 |
| 13 | `disponivel` | `acesso` | 0.493 | 24 |
| 14 | `enfermaria` | `ruido` | 0.488 | 57 |
| 15 | `torna` | `visivel` | 0.482 | 45 |
| 16 | `covideiro` | `pandemico` | 0.477 | 97 |
| 17 | `producao` | `condicoes` | 0.470 | 51 |
| 18 | `saude` | `publico` | 0.467 | 18 |
| 19 | `ciencia` | `construcao` | 0.462 | 19 |
| 20 | `treinado` | `modelo` | 0.459 | 49 |
| 21 | `fonoaudiologos` | `medicos` | 0.457 | 28 |
| 22 | `tornar` | `visivel` | 0.453 | 20 |
| 23 | `cadeia` | `translacoes` | 0.436 | 51 |
| 24 | `referencia` | `conceito` | 0.435 | 16 |
| 25 | `controles` | `enfermaria` | 0.424 | 27 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (39 termos): inscricao, cadeia, analise, secao, torna, dispositivo
- **Tópico 2** (32 termos): dado, modelo, audio, sinal, campo, acustico
- **Tópico 3** (28 termos): spira, artigo, projeto, marcelo, artigos, cientifico
- **Tópico 4** (28 termos): espectrograma, actante, partir, paciente, arquivo, produz
- **Tópico 5** (21 termos): covideiro, coleta, condicoes, pacientes, ruido, pandemico
- **Tópico 6** (12 termos): objeto, pratica, condicao, distintas, distintos, clinica
- **Tópico 7** (11 termos): respiratoria, insuficiencia, covid, deteccao, acustica, versao
- **Tópico 8** (9 termos): rede, neural, associacao, topologia, arquitetura, ator

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [inscricao, cadeia, analise] e **Tópico 2** [dado, modelo, audio] — densidade ponderada de ligação = 0.6322
- Lacuna entre **Tópico 1** [inscricao, cadeia, analise] e **Tópico 5** [covideiro, coleta, condicoes] — densidade ponderada de ligação = 0.7998
- Lacuna entre **Tópico 2** [dado, modelo, audio] e **Tópico 4** [espectrograma, actante, partir] — densidade ponderada de ligação = 0.8292
- Lacuna entre **Tópico 2** [dado, modelo, audio] e **Tópico 3** [spira, artigo, projeto] — densidade ponderada de ligação = 0.9286
- Lacuna entre **Tópico 1** [inscricao, cadeia, analise] e **Tópico 4** [espectrograma, actante, partir] — densidade ponderada de ligação = 0.9789
- Lacuna entre **Tópico 2** [dado, modelo, audio] e **Tópico 5** [covideiro, coleta, condicoes] — densidade ponderada de ligação = 1.0134

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
