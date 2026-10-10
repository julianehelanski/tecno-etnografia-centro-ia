# Tecnografias de um centro de inteligência artificial: seguindo cientistas e engenheiros universidade afora

Este repositório contém o texto-fonte em LaTeX da minha tese de doutorado (Programa de Pós-Graduação em Ciências Sociais, IFCH, Unicamp, 2026), uma tecnografia do Centro de Inteligência Artificial da USP (C4AI, parceria USP/FAPESP/IBM) e do sistema Spira, de detecção de insuficiência respiratória pela voz. É o repositório central do conjunto: reúne o texto, a bibliografia e as figuras de todos os capítulos, e o mapa que liga cada figura e tabela ao repositório de dados de onde vem.

## Conteúdo

| Arquivo ou pasta | Descrição |
|---|---|
| `tese.tex`, `configuracao.tex`, `pacotes.tex` | documento principal e configuração |
| `ex_cap.tex`, `ex_cap0.tex` a `ex_cap5.tex` | prefácio, apresentação, capítulos 1 a 4 e considerações finais |
| `ex_ane1.tex` | anexo 1, declaração de uso de IA generativa |
| `ex_ape1.tex` a `ex_ape3.tex` | arquivos de apêndice vazios ou comentados, fora da compilação |
| `tese.bib` | bibliografia (biblatex) |
| `figuras/` | figuras por capítulo |
| `docs/MAPA_DE_DADOS.md` | mapa dos repositórios de dados e de onde cada resultado entra na tese |
| `atualizar_figuras_tese.sh` | copia para `figuras/` as figuras regeneradas nos repositórios de análise |

## Repositórios de dados

Os dados, *scripts* e figuras das análises estão em repositórios próprios, cada um com o detalhamento figura a figura em `docs/USO_NA_TESE.md`:

| Repositório | Capítulo | Produto |
|---|---|---|
| [`analise-figuracoes-latour`](https://github.com/julianehelanski/analise-figuracoes-latour) | 2 | análise lexicométrica do vocabulário figurativo em seis textos de Latour |
| [`bibliometria-ia-humanas`](https://github.com/julianehelanski/bibliometria-ia-humanas) | 2 | mapeamento da IA nas ciências humanas brasileiras (CAPES, SciELO, OpenAlex) |
| [`bibliometria-publicacoes-c4ai`](https://github.com/julianehelanski/bibliometria-publicacoes-c4ai) | 3 | base curada e análise das publicações do C4AI |
| [`spira-espectrogramas`](https://github.com/julianehelanski/spira-espectrogramas) | 4 | formas de onda e espectrogramas mel do *dataset* do SPIRA |
| [`tecno-etnografia-tese-site`](https://github.com/julianehelanski/tecno-etnografia-tese-site) | 1 a 5 | análise de rede textual da tese e site que a acompanha |

O material de campo (entrevistas e diário de campo) não está em nenhum dos repositórios.

## Compilação

Compilar `tese.tex` com `pdflatex` e `biber` (biblatex), no Overleaf conectado a este repositório ou localmente.

## Uso de inteligência artificial generativa

O texto da tese é meu. Fiz a tese com três ferramentas de IA generativa, todas descritas no Anexo 1. Com o Claude, interface de conversação, fiz interlocução argumentativa, revisão gramatical e edição. Com o Claude Code, interface de linha de comando que dá ao modelo de linguagem acesso aos arquivos do projeto, escrevi os *scripts* das análises, a análise de rede textual dos capítulos (no repositório `tecno-etnografia-tese-site`), os diagramas e a padronização das figuras, e organizei os repositórios para o depósito. Com o NotebookLM organizei conjuntos temáticos de obras da bibliografia. A recursividade desse trabalho com o modelo de linguagem é parte do argumento da tese e está descrita nos capítulos 1 e 4.

**Modelos registrados no histórico de versões:** Claude Opus 4.7, Claude Opus 4.8, Claude Opus 5.5 e Claude Sonnet 5.5 (junho a outubro de 2026), além das versões registradas nos demais repositórios (Claude Sonnet 4.6 e Claude Sonnet 5).

Os *commits* com autor `Claude`, ou com a linha `Co-Authored-By: Claude …`, foram feitos em sessões do Claude Code; a marcação é gerada pela ferramenta e registra em que pontos do histórico o modelo participou do trabalho. A autoria e a responsabilidade pelo conteúdo são minhas e, conforme a Deliberação CONSU-A-005/2026 da Unicamp, as ferramentas de IA generativa não figuram como coautoras. A declaração formal de uso de IA generativa, no modelo da Pró-Reitoria de Pós-Graduação da Unicamp, está no [Anexo 1](ex_ane1.tex).

## Citação

> CARDOSO, Juliane Cristina Helanski. *Tecnografias de um centro de inteligência artificial*: seguindo cientistas e engenheiros universidade afora. Orientadora: Maria Suely Kofes. 2026. Tese (Doutorado em Ciências Sociais) – Instituto de Filosofia e Ciências Humanas, Universidade Estadual de Campinas, Campinas, 2026.

ORCID da autora: https://orcid.org/0000-0001-8649-8986.
