#!/usr/bin/env python3
"""C12 — Hydrogen capacity formula verification.

Backs `prop:hydrogen-capacity` in the Organic Chemistry chapter.

Statement
---------
For an open-chain CₙHₘ molecule with bond-order pattern
(k₁, …, k_{N-1}), the hydrogen capacity is

    m = 2N + 2 − 2·d        (open chain),
    m = 2N − 2·d            (closed ring),

where d = Σ_i (k_i − 1) is the total degree of unsaturation.

This script verifies the formula across the standard organic taxonomy
(alkanes, alkenes, alkynes, dienes, cumulenes, cycloalkanes,
benzene, polycyclic aromatics) and compares against IUPAC molecular
formulae from `data/experimental-organic.json`.

Usage
-----
    python3 hydrogen_capacity.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from witness_base import WitnessBuilder


DATA_PATH = Path(__file__).parent / "data" / "experimental-organic.json"


def predicted_H(N: int, d: int, closed: bool) -> int:
    """Hydrogen capacity formula."""
    return (2 * N - 2 * d) if closed else (2 * N + 2 - 2 * d)


def main() -> int:
    data = json.loads(DATA_PATH.read_text())
    families = data["organic_taxonomy"]["families"]

    rows = []
    for fam in families:
        N = fam["N"]
        d = fam["degree_of_unsaturation"]
        closed = fam["closed"]
        m_predicted = predicted_H(N, d, closed)
        m_actual = fam["hydrogens"]
        rows.append({
            "name": fam["name"],
            "formula": fam["formula"],
            "N": N,
            "degree_of_unsaturation": d,
            "closed": closed,
            "H_predicted": m_predicted,
            "H_actual": m_actual,
            "agreement": m_predicted == m_actual,
        })

    n_agree = sum(1 for r in rows if r["agreement"])
    n_total = len(rows)

    w = WitnessBuilder("hydrogen-capacity", engine="python")
    w.set_description(
        "Hydrogen-capacity formula m = 2N + 2 − 2d (open) or "
        "m = 2N − 2d (closed) verified across the organic taxonomy."
    )
    w.set_content_block("prop:hydrogen-capacity")
    w.add_data("table", rows)
    w.add_data("agreement_count", n_agree)
    w.add_data("agreement_total", n_total)

    w.add_assertion(
        "all H-capacity predictions match IUPAC formulae",
        computed=str(n_agree == n_total),
        expected="True",
    )
    w.add_assertion(
        "agreement count",
        computed=n_agree,
        expected=n_total,
    )

    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
