#!/usr/bin/env bash
#
# atualizar_figuras_tese.sh
#
# Atualiza as figuras da tese copiando, de uma pasta de origem, apenas os
# arquivos cujo nome ja existe em algum lugar da arvore de destino. O
# casamento e feito pelo nome do arquivo (basename), de modo que o LaTeX
# nunca precisa ser editado: cada figura ja referenciada na tese e
# substituida pela versao mais recente gerada no repo de origem.
#
# Uso:
#   ./atualizar_figuras_tese.sh --origem <pasta_origem> <pasta_destino>... [--dry-run]
#
# Exemplo:
#   ./atualizar_figuras_tese.sh \
#       --origem ../analise-figuracoes-latour/outputs/figuras \
#       figuras --dry-run
#
# Opcoes:
#   --origem <dir>   Pasta com as figuras recem-geradas (fonte da verdade).
#   --dry-run        Apenas relata o que mudaria; nao copia nada.
#   <pasta_destino>  Uma ou mais pastas (varridas recursivamente) onde
#                    procurar arquivos de mesmo nome para substituir.
#
# Saida: lista de arquivos atualizados, identicos (pulados) e nao
# encontrados no destino. Codigo de saida 0 em sucesso.

set -euo pipefail

origem=""
dry_run=0
destinos=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --origem)
      origem="${2:-}"
      shift 2
      ;;
    --dry-run)
      dry_run=1
      shift
      ;;
    -h|--help)
      grep '^#' "$0" | sed 's/^# \{0,1\}//'
      exit 0
      ;;
    -*)
      echo "Opcao desconhecida: $1" >&2
      exit 2
      ;;
    *)
      destinos+=("$1")
      shift
      ;;
  esac
done

if [[ -z "$origem" ]]; then
  echo "Erro: --origem e obrigatorio." >&2
  exit 2
fi
if [[ ! -d "$origem" ]]; then
  echo "Erro: pasta de origem nao existe: $origem" >&2
  exit 2
fi
if [[ ${#destinos[@]} -eq 0 ]]; then
  echo "Erro: informe ao menos uma pasta de destino." >&2
  exit 2
fi
for d in "${destinos[@]}"; do
  if [[ ! -d "$d" ]]; then
    echo "Erro: pasta de destino nao existe: $d" >&2
    exit 2
  fi
done

if [[ $dry_run -eq 1 ]]; then
  echo "== MODO DRY-RUN (nenhum arquivo sera alterado) =="
fi
echo "Origem:   $origem"
echo "Destinos: ${destinos[*]}"
echo

n_atualizados=0
n_identicos=0
n_ausentes=0

# Itera sobre os arquivos regulares da origem (apenas no nivel da pasta;
# a origem e plana por convencao em outputs/figuras).
shopt -s nullglob
for src in "$origem"/*; do
  [[ -f "$src" ]] || continue
  nome="$(basename "$src")"

  # Procura, em cada destino, arquivos de mesmo basename.
  encontrou=0
  for destdir in "${destinos[@]}"; do
    while IFS= read -r -d '' alvo; do
      encontrou=1
      if cmp -s "$src" "$alvo"; then
        n_identicos=$((n_identicos + 1))
        echo "  identico  $alvo"
      else
        n_atualizados=$((n_atualizados + 1))
        if [[ $dry_run -eq 1 ]]; then
          echo "  ATUALIZA  $alvo  (<- $nome)"
        else
          cp -- "$src" "$alvo"
          echo "  copiado   $alvo  (<- $nome)"
        fi
      fi
    done < <(find "$destdir" -type f -name "$nome" -print0)
  done

  if [[ $encontrou -eq 0 ]]; then
    n_ausentes=$((n_ausentes + 1))
  fi
done
shopt -u nullglob

echo
echo "Resumo: $n_atualizados atualizado(s), $n_identicos identico(s), $n_ausentes da origem sem correspondencia no destino."
if [[ $dry_run -eq 1 ]]; then
  echo "(dry-run: rode novamente sem --dry-run para aplicar.)"
fi
