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

## Compilação

Compilar `tese.tex` com `pdflatex`/`biber` (biblatex), preferencialmente no Overleaf conectado a este repositório.
