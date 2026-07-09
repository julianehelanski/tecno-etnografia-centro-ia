#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
render_tese_network_figura.py
=============================
Gera a figura estática da rede textual da TESE INTEIRA a partir de
``tese_network.json`` (o mesmo grafo que a capa do site renderiza de forma
interativa), reaproveitando o ``render_network`` deste repositório, de modo
que a figura das Considerações finais compartilha a identidade visual das
figuras dos capítulos: mesma paleta de comunidades e arestas arqueadas
coloridas pela mistura das cores das pontas.

Saída:
    figuras/rede_tese_inteira.png

Uso:
    python3 infranodus/render_tese_network_figura.py
    (rode antes tese_network.py --source-root .. para atualizar o JSON)
"""
from __future__ import annotations

import json
from pathlib import Path

import networkx as nx

from infranodus_cap1 import render_network

THIS_DIR = Path(__file__).resolve().parent
REPO_ROOT = THIS_DIR.parent

# Poda de legibilidade da versão impressa: o grafo interativo do site
# suporta todas as arestas; em papel, mantenho as de peso mais alto.
MIN_EDGE_WEIGHT = 15


def carregar_grafo(json_path: Path):
    data = json.loads(json_path.read_text(encoding="utf-8"))
    nodes, edges, comunidades = data["nodes"], data["edges"], data["communities"]

    G = nx.Graph()
    for n in nodes:
        G.add_node(n["id"], freq=n.get("freq", 0))
    for e in edges:
        G.add_edge(e["s"], e["t"], weight=float(e["w"]), npmi=float(e.get("npmi", 0.0)))

    deg = {n["id"]: float(n.get("degree", 0.0)) for n in nodes}

    id_por_comm: dict[int, set[str]] = {}
    for n in nodes:
        id_por_comm.setdefault(int(n["community"]), set()).add(n["id"])
    ordem = [int(c["id"]) for c in sorted(comunidades, key=lambda z: z.get("size", 0),
                                          reverse=True)]
    comms = [id_por_comm.get(cid, set()) for cid in ordem if id_por_comm.get(cid)]
    return G, comms, deg


def main() -> None:
    json_path = THIS_DIR / "tese_network.json"
    if not json_path.exists():
        raise FileNotFoundError(
            f"{json_path} não existe. Rode antes tese_network.py --source-root .."
        )
    G, comms, deg = carregar_grafo(json_path)

    G.remove_edges_from([(u, v) for u, v, d in G.edges(data=True)
                         if d["weight"] < MIN_EDGE_WEIGHT])
    G.remove_nodes_from(list(nx.isolates(G)))

    out = REPO_ROOT / "figuras" / "rede_tese_inteira.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    render_network(G, comms, deg, out,
                   title="Rede textual — tese inteira · núcleo (Apresentação, "
                         "capítulos 1 a 4 e Considerações finais)",
                   label_top=32)
    print(f"Figura gerada: {out} "
          f"({G.number_of_nodes()} nós, {G.number_of_edges()} arestas)")


if __name__ == "__main__":
    main()
