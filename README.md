# {tecnografia} de um centro de inteligência artificial: seguindo cientistas e engenheiros, universidade afora

Texto-fonte em LaTeX da tese de doutorado de Juliane Helanski (Programa de Pós-Graduação em Ciências Sociais, IFCH, Unicamp, 2026), uma tecnografia do Centro de Inteligência Artificial da USP (C4AI-USP/FAPESP/IBM) e do sistema Spira.

## Conteúdo

| Arquivo ou pasta | Descrição |
|---|---|
| `tese.tex`, `configuracao.tex`, `pacotes.tex` | documento principal e configuração |
| `ex_cap0.tex` a `ex_cap5.tex` | introdução e capítulos 1 a 5 |
| `ex_ape1.tex` a `ex_ape4.tex`, `ex_ane1.tex` | apêndices e anexo |
| `tese.bib` | bibliografia (biblatex) |
| `figuras/` | figuras por capítulo |
| `infranodus/` | análise de rede textual dos capítulos e da tese inteira |
| `atualizar_figuras_tese.sh` | copia figuras recém-geradas dos repositórios de análise para `figuras/`, pelo nome do arquivo |
| `docs/MAPA_DE_DADOS.md` | mapa dos repositórios de dados, onde cada resultado entra na tese e pendências antes do depósito |

## Repositórios relacionados

Os dados, scripts e figuras de análise vivem em repositórios próprios: `analise-figuracoes-latour` (capítulo 2), `bibliometria-ia-humanas` (capítulo 2), `bibliometria-publicacoes-c4ai` (capítulo 3), `spira-espectrogramas` (capítulo 4) e `tecno-etnografia-tese-site` (rede textual e site). O detalhamento figura a figura está em [`docs/MAPA_DE_DADOS.md`](docs/MAPA_DE_DADOS.md) e no arquivo `docs/USO_NA_TESE.md` de cada repositório.

## Uso de inteligência artificial generativa

O texto da tese é meu. Usei três ferramentas de IA generativa, todas descritas no Anexo 1. Com o Claude, interface de conversação, fiz interlocução argumentativa, revisão gramatical e edição. Com o Claude Code, interface de linha de comando que dá ao modelo de linguagem acesso aos arquivos do projeto, escrevi os *scripts* das análises, a rede textual dos capítulos (`infranodus/`), os diagramas e a padronização das figuras, e organizei os repositórios para o depósito (este README e `docs/MAPA_DE_DADOS.md`). Com o NotebookLM organizei conjuntos temáticos de obras da bibliografia. A recursividade desse trabalho com o modelo de linguagem é parte do argumento da tese e está descrita nos capítulos 1 e 4.

**Modelos registrados no histórico de versões:** Claude Opus 4.7, Claude Opus 4.8, Claude Opus 5.5 e Claude Sonnet 5.5 (junho a outubro de 2026), além das versões registradas nos demais repositórios (Claude Sonnet 4.6 e Claude Sonnet 5).

**Sobre o autor `Claude` e a linha `Co-Authored-By: Claude …` nos *commits*.** Os *commits* com autor `Claude`, ou com essa linha no fim da mensagem, foram feitos em sessões do Claude Code. A marcação é gerada pela própria ferramenta e funciona como registro técnico de rastreabilidade: indica em que pontos do histórico o modelo de linguagem participou do trabalho. A autoria e a responsabilidade pelo conteúdo deste repositório são minhas. Conforme a Deliberação CONSU-A-005/2026 da Unicamp, as ferramentas de IA generativa não figuram como coautoras.

A declaração formal de uso de IA generativa da tese, no modelo da Pró-Reitoria de Pós-Graduação da Unicamp, está no [Anexo 1 da tese](https://github.com/julianehelanski/tecno-etnografia-centro-ia/blob/main/ex_ane1.tex). Este texto também serve à descrição do depósito no Repositório de Dados de Pesquisa da Unicamp (REDU).

## Compilação

Compilar `tese.tex` com `pdflatex`/`biber` (biblatex), preferencialmente no Overleaf conectado a este repositório.
