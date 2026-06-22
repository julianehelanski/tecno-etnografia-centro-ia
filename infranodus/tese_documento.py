#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tese_documento.py
=================
Extrai do `.tex` da tese os "paratextos" para apresentar na defesa:
resumo (PT), palavras-chave, sumário (capítulos · seções · subseções,
com um breve resumo por capítulo e uma nota por seção), lista de
ilustrações e lista de tabelas. Exporta JSON e, opcionalmente, reinjeta
num HTML (<script id="docdata">).

Uso:
    python3 infranodus/tese_documento.py --source-root /tmp/tese --inject index.html
"""
import argparse
import json
import re
import sys
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR.parent / "scripts"))
from relatorio_divergencia_tese import clean_title, _match_brace_arg  # noqa: E402

# Síntese para a banca, ancorada no Resumo e nas Considerações Finais (cap.5).
# Curada (não gerada): revise/ajuste se quiser outra ênfase.
TESE = {
    "tema": "A pesquisa em inteligência artificial como prática tecnocientífica "
            "situada — uma etnografia do Centro de Inteligência Artificial da "
            "USP (C4AI) entre 2020 e 2025.",
    "objeto": "A rede sociotécnica que associou universidade pública e "
              "corporação transnacional (USP · IBM · FAPESP) na pesquisa de IA "
              "no Brasil, da fundação à dissolução; e a cadeia técnica do projeto "
              "SPIRA, da voz do paciente ao diagnóstico.",
    "pergunta": "Onde está o laboratório de IA e onde estão os seus cientistas? "
                "O que cientistas e engenheiros fazem quando desenvolvem "
                "inteligência artificial?",
    "objetivo": "Descrever o arranjo das práticas tecnocientíficas dessa rede e "
                "analisar como o plano institucional-corporativo e o plano "
                "técnico-situado se articulam na produção de conhecimento em IA "
                "e na produção de conhecimento sobre IA pelas ciências sociais.",
    "questoes": [
        "Como se faz IA, na prática, num centro de pesquisa?",
        "Como um arranjo público-privado nasce, opera e se dissolve?",
        "Como a voz de um paciente se converte em dado e em diagnóstico — e o "
        "que se perde nessa cadeia de inscrições?",
        "Que vocabulário (figurações) descreve a tecnociência sem denunciá-la "
        "nem celebrá-la?",
    ],
    "conclusao": "Fazer IA é fazer tecnociência: construir fatos e, ao mesmo "
                 "tempo, sustentar as redes que os tornam possíveis. O "
                 "laboratório está distribuído (no computador, em casa, na "
                 "enfermaria) e as redes que pareciam estáveis revelaram-se "
                 "composições precárias — a falha de generalização do SPIRA e a "
                 "dissolução da parceria IBM-C4AI (dez. 2025) tornaram visível "
                 "essa fragilidade.",
    "contribuicoes": [
        "Empírica — o registro etnográfico do ciclo completo de uma parceria "
        "público-privada em IA no Brasil, do nascimento à dissolução (inclui "
        "relatórios não-públicos e entrevistas que preservam a ciência em "
        "construção).",
        "Metodológica — as quatro lições do Capítulo 1, a proposta da "
        "tecnoetnografia e o uso das notas de rodapé como dispositivo "
        "teórico-metodológico.",
        "Analítica — o conceito de inscrição tecnoetnográfica, a leitura do "
        "SPIRA como objeto fracional (Mol/Law) e a proposta descritiva de "
        "tecnopoder.",
    ],
    "desdobramentos": [
        "Acompanhar o SPIRA-BM (segunda fase) e realizar a entrevista com "
        "Larissa Berti.",
        "Acompanhar o C4AI após a saída da IBM — o que resta quando a rede se "
        "desfaz.",
        "Investigar a composição entre pesquisadora e modelo de linguagem "
        "(Claude) na produção da tese.",
    ],
}

# capítulo: (arquivo, número, título, resumo [o que faz], conclusão [a que chega])
CHAPTERS = [
    ("ex_cap0.tex", "", "Apresentação",
     "A entrada em campo: a pergunta que move a tese e o primeiro encontro com "
     "um sistema de IA (o SPIRA), que abre o percurso etnográfico.",
     ""),
    ("ex_cap1.tex", "1", "Método",
     "Documenta o percurso da etnógrafa pelo campo e constrói o método a partir "
     "da experiência: o patchwork como figuração, as existências parciais "
     "(incluindo o fazer-com IA generativa) e a compostagem.",
     "Chega a quatro lições metodológicas e à proposta da tecnoetnografia — "
     "modo de pesquisa que habita a tensão entre a circulabilidade técnica das "
     "inscrições e a realidade sensível dos corpos."),
    ("ex_cap2.tex", "2", "Metáforas, figurações e alianças",
     "Reconstrói as alianças teóricas da tese em duas tramas: a análise "
     "lexicométrica das figurações em seis obras de Latour e o mapeamento "
     "bibliométrico do campo brasileiro de IA nas ciências humanas.",
     "Mostra que a figuração militar-industrial é situada e que o vocabulário "
     "têxtil-topológico organiza os textos metateóricos de Latour; documenta um "
     "campo brasileiro em formação, onde a pesquisa se insere."),
    ("ex_cap3.tex", "3", "A rede que Fábio e Cláudio construíram",
     "Segue Fábio e Cláudio pela rede longa que sustentou o C4AI por cinco "
     "anos, dos cartões de Hollerith (1890) à genealogia da IBM e à "
     "racionalidade do ecossistema de inovação.",
     "Documenta o ciclo completo da parceria (2020–2025) e identifica um padrão "
     "de construção de dependência sedimentado pela IBM ao longo de 135 anos — "
     "proposto como tecnopoder; encerra com a dissolução IBM-C4AI (dez. 2025)."),
    ("ex_cap4.tex", "4", "A rede que Marcelo construiu",
     "Segue Marcelo Finger pela rede curta do SPIRA: a cadeia de translações "
     "que converte a voz de pacientes com Covid-19 em espectrogramas "
     "processados por redes neurais — da fala ao dado ao diagnóstico.",
     "Mostra que o modelo (96,5% de precisão) aprendeu uma insuficiência "
     "respiratória específica ao covideiro pandêmico: sua falha de "
     "generalização é evidência empírica da tensão ontológica (Mol). Propõe a "
     "inscrição tecnoetnográfica."),
    ("ex_cap5.tex", "", "Considerações finais",
     "Cruza as redes longas (Cap. 3) e curtas (Cap. 4) e reúne as contribuições "
     "empírica, metodológica e analítica da tese.",
     "Os dois pontos de cruzamento — a falha do SPIRA e a dissolução IBM-C4AI — "
     "revelam a fragilidade de redes que pareciam estáveis: as inscrições "
     "carregavam, ocultas, as condições de sua produção."),
]

ENV_RE = re.compile(
    r'\\begin\{(figure|table|longtable)\*?\}'
    r'|\\end\{(figure|table|longtable)\*?\}'
    r'|\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}'
    r'|\\caption(?:\[([^\]]*)\])?\{')

SEC_RE = re.compile(r'\\(section|subsection)\*?\s*\{')

# Diagrama interativo (MermaidChart) embutido na legenda via \href{...}.
MERMAID_RE = re.compile(r'https://mermaid\.ai/d/[0-9a-fA-F-]+')

# Pasta de figuras que o SITE de fato exibe (figuras/<slug>/...).
SITE_FIGURAS = THIS_DIR.parent / "figuras"


def _site_image(texpath: str | None) -> str | None:
    r"""Mapeia o \includegraphics da tese para a figura que o site exibe.

    Hoje só as inscrições de rede textual (InfraNodus) e as trajetórias
    narrativas têm cópia em figuras/<slug>/ com o nome do site. Retorna o
    caminho relativo ao repositório do site se o arquivo existir; senão None
    — mesmo princípio de sync_site_figuras.py: só mostra o que o site tem.
    """
    if not texpath:
        return None
    base = texpath.strip().replace("\\", "/").rsplit("/", 1)[-1].lower()
    mname = re.search(r"infranodus_cap(\d+)_", base)
    mdir = re.search(r"cap\.?(\d+)", texpath)
    m = mname or mdir
    if not m:
        return None
    slug = f"cap{m.group(1)}"
    name_map = {
        f"infranodus_cap{m.group(1)}_network.png":   f"{slug}-infranodus-network.png",
        f"infranodus_cap{m.group(1)}_focus.png":     f"{slug}-infranodus-focus.png",
        f"infranodus_cap{m.group(1)}_pmi.png":       f"{slug}-infranodus-pmi.png",
        f"infranodus_cap{m.group(1)}_focus_pmi.png": f"{slug}-infranodus-pmi.png",
        "trajectory_gantt.png":                      f"{slug}-trajectory-gantt.png",
        "trajectory_alluvial.png":                   f"{slug}-trajectory-alluvial.png",
        "trajectory_semantic.png":                   f"{slug}-trajectory-semantic.png",
    }
    mapped = name_map.get(base)
    if not mapped:
        return None
    rel = f"figuras/{slug}/{mapped}"
    return rel if (SITE_FIGURAS / slug / mapped).exists() else None


def _is_continuation(s: str) -> bool:
    """Rótulo de continuação (parte seguinte de uma figura/longtable),
    que compartilha o número e não entra na lista de ilustrações."""
    return re.sub(r"[()\.\s]", "", s).lower() in (
        "continua", "continuacao", "continuação")


def _trunc(s: str, n: int = 170) -> str:
    s = s.strip()
    return s if len(s) <= n else s[:n - 1].rstrip() + "…"


def _pre(s: str) -> str:
    """Remove ruído de LaTeX preservando caixa, acentos e hífens (para exibição)."""
    s = re.sub(r"(?<!\\)%.*", "", s)                                   # comentários
    s = re.sub(r"\\(begin|end)\{[^}]*\}", " ", s)                      # ambientes
    s = re.sub(r"\\label\{[^}]*\}", " ", s)
    s = re.sub(r"\\(ref|cref|Cref|autoref|eqref|pageref|nameref)\{[^}]*\}", " ", s)
    s = re.sub(r"\\(parencite|textcite|cite[a-zA-Z]*)\*?(?:\[[^\]]*\])*\{[^}]*\}", " ", s)
    s = re.sub(r"\\includegraphics(?:\[[^\]]*\])?\{[^}]*\}", " ", s)
    s = re.sub(r"\\footnote\{[^{}]*\}", " ", s)
    s = re.sub(r"\\(selectlanguage|setstretch|setlength)\{[^}]*\}", " ", s)
    s = re.sub(r"\\(begingroup|endgroup|noindent|large|Large|centering|small|par)\b", " ", s)
    return s


def first_sentence(tex_segment: str) -> str:
    """Primeira frase de prosa de um trecho .tex (para nota de seção)."""
    txt = re.sub(r"\s+", " ", clean_title(_pre(tex_segment))).strip()
    m = re.search(r"(.+?[.!?])(\s|$)", txt)
    sent = (m.group(1) if m else txt)
    return _trunc(sent, 180)


def parse_outline(tex: str) -> list[dict]:
    """Seções (com subseções e nota de 1ª frase), na ordem do documento."""
    secs: list[dict] = []
    seen = False
    matches = list(SEC_RE.finditer(tex))
    for idx, m in enumerate(matches):
        kind = m.group(1)
        arg, nxt = _match_brace_arg(tex, m.end() - 1)
        title = clean_title(arg)
        if not title:
            continue
        # trecho até o próximo section/subsection → nota (1ª frase)
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(tex)
        body = tex[nxt:end]
        # corta no primeiro ambiente para evitar legendas como "nota"
        cut = re.search(r"\\begin\{(figure|table|longtable|itemize|enumerate)", body)
        if cut:
            body = body[:cut.start()]
        nota = first_sentence(body)
        if kind == "section" or not seen:
            seen = seen or kind == "section"
            secs.append({"t": title, "nota": nota, "subs": []})
        else:
            if secs:
                secs[-1]["subs"].append(title)
    return secs


def parse_captions(tex: str):
    """(figuras, tabelas): legendas na ordem do documento, por ambiente."""
    figs, tabs = [], []
    stack = []
    last_img = None   # último \includegraphics do ambiente figure corrente
    for m in ENV_RE.finditer(tex):
        g = m.group(0)
        if g.startswith(r"\begin"):
            stack.append(m.group(1))
            last_img = None
        elif g.startswith(r"\end"):
            if stack:
                stack.pop()
            last_img = None
        elif g.startswith(r"\includegraphics"):
            last_img = m.group(3)
        else:  # \caption
            short = m.group(4)
            if short is not None and short.strip() == "":
                # \caption[]{...}: entrada vazia na lista de ilustrações
                # (típico de continuação de longtable) — não listar.
                continue
            arg, _ = _match_brace_arg(tex, m.end() - 1)
            cap = clean_title(short) if short else _trunc(clean_title(arg))
            if not cap or _is_continuation(cap):
                continue
            link_m = MERMAID_RE.search(arg)
            link = link_m.group(0) if link_m else None
            env = stack[-1] if stack else "figure"
            img = None if env in ("table", "longtable") else _site_image(last_img)
            (tabs if env in ("table", "longtable") else figs).append((cap, link, img))
    return figs, tabs


def parse_resumo(src: Path):
    raw = src.read_text(encoding="utf-8")
    clean = re.sub(r"\s+", " ", clean_title(_pre(raw))).strip()
    parts = re.split(r"Palavras[\s-]*chave\s*:?\s*", clean, maxsplit=1)
    resumo = parts[0].strip()
    palavras = []
    if len(parts) > 1:
        kw = parts[1].split(".")[0]   # só a frase das palavras-chave
        palavras = [k.strip() for k in re.split(r"[,;]", kw) if k.strip()]
    return resumo, palavras


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-root", type=Path, default=Path("/tmp/tese"))
    ap.add_argument("--out", type=Path, default=THIS_DIR / "tese_documento.json")
    ap.add_argument("--inject", type=Path, default=None)
    args = ap.parse_args()

    resumo, palavras = parse_resumo(args.source_root / "resumo.tex")

    sumario, figuras, tabelas = [], [], []
    fign = tabn = 0
    for fname, num, title, resumo_cap, conclusao_cap in CHAPTERS:
        src = args.source_root / fname
        if not src.exists():
            print(f"[doc] aviso: {fname} ausente, pulando.")
            continue
        tex = src.read_text(encoding="utf-8")
        sumario.append({
            "id": fname.replace("ex_", "").replace(".tex", ""),
            "num": num, "title": title, "resumo": resumo_cap,
            "conclusao": conclusao_cap,
            "sections": parse_outline(tex),
        })
        f, t = parse_captions(tex)
        for c, link, img in f:
            fign += 1
            entry = {"n": fign, "cap": num or title, "t": c}
            if link:
                entry["link"] = link
            if img:
                entry["img"] = img
            figuras.append(entry)
        for c, _link, _img in t:
            tabn += 1
            tabelas.append({"n": tabn, "cap": num or title, "t": c})

    payload = {
        "tese": TESE,
        "resumo": resumo,
        "palavras_chave": palavras,
        "sumario": sumario,
        "figuras": figuras,
        "tabelas": tabelas,
    }
    data_str = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    args.out.write_text(data_str, encoding="utf-8")
    print(f"[doc] JSON: {args.out} ({args.out.stat().st_size/1024:.0f} KB) | "
          f"resumo={len(resumo)}c · {len(palavras)} palavras-chave · "
          f"{len(sumario)} capítulos · {len(figuras)} figuras · {len(tabelas)} tabelas")

    if args.inject is not None:
        assert "</script" not in data_str.lower()
        html = args.inject.read_text(encoding="utf-8")
        pat = re.compile(r'(<script type="application/json" id="docdata">).*?(</script>)', re.DOTALL)
        new, n = pat.subn(lambda m: m.group(1) + data_str + m.group(2), html, count=1)
        if n != 1:
            print(f"[doc] ERRO: <script id=docdata> não encontrado em {args.inject}")
            return 1
        args.inject.write_text(new, encoding="utf-8")
        print(f"[doc] reinjetado em {args.inject}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
