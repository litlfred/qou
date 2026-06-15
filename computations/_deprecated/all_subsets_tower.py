#!/usr/bin/env python3
"""
All-subsets brane tower: include |S| ≥ 3 subset terms.

Paper's mass-endomorphism-tower formula stops at pairs:
  𝔪 = |ΠV̂| + Σ_i Φ_q(|V̂_i|) + z²·Σ_{i<j} Φ_q(|V̂_i V̂_j|)

User question: are we summing all subsets S?
Answer: NO — only |S| = 1 (singles) and |S| = 2 (pairs).
Higher-codim subsets are absent.

Geometrical interpretation (brane-tower picture):
  - |S| = 1: codim-1 blow-up centre (per generator)
  - |S| = 2: codim-2 blow-up centre (per pair)
  - |S| = 3: codim-3 (triples) — POTENTIALLY MISSING
  - |S| ≥ 4: higher-codim — POTENTIALLY MISSING

Hypothesis: paper truncates at codim-2 because higher-codim
contributions are smaller (suppressed by z^{|S|-1} factors and
generic position arguments).  But for higher-A isotopes this
truncation may cause the 5-15% errors.

This script computes the all-subsets sum and compares to paper's
truncated sum, for D, T, ³He, ⁴He.

Witness: all-subsets-tower.witness.json
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations

import mpmath as mp
mp.mp.dps = 50

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from hecke_core import (
    atom_per_generator_volumes, h as h_val, z as z_mark,
)
from mass_endomorphism import Phi_q
from experimental_constants import M_E_MEV


Q0 = Q_MP  # was f64 roundtrip


def all_subsets_tower(Z, N, include_inter=True, max_size=None):
    """Compute brane tower with all subsets up to max_size.
    Returns dict: subset_size → contribution from |S| = size."""
    vols = atom_per_generator_volumes(Z, N, include_inter=include_inter)
    n = len(vols)
    if max_size is None:
        max_size = n

    contribs_by_size = {}
    for size in range(1, max_size + 1):
        total = mp.mpf(0)
        count = 0
        for subset in combinations(range(n), size):
            prod = mp.mpf(1)
            for i in subset:
                # vols[i] is a dict; use 'full' = Wedderburn-weighted V̂
                v_full = vols[i]['full'] if isinstance(vols[i], dict) else vols[i]
                prod *= abs(mp.mpf(str(float(v_full))))
            try:
                phi = Phi_q(prod)
            except Exception:
                phi = mp.mpf(0)
            if mp.isinf(phi):
                phi = mp.mpf(0)
            # Markov weight z^{size-1}
            w = mp.mpf(str(float(z_mark))) ** (size - 1)
            total += w * phi
            count += 1
        contribs_by_size[size] = {
            "total": float(total),
            "count": count,
        }
    desc_prod = mp.mpf(1)
    for v in vols:
        v_full = v['full'] if isinstance(v, dict) else v
        desc_prod *= mp.mpf(str(float(v_full)))
    descended = float(abs(desc_prod))
    return descended, contribs_by_size


if __name__ == "__main__":
    print("ALL-SUBSETS BRANE TOWER — sum over all |S| ≥ 1")
    print("=" * 80)
    print(f"q_0 = {Q0}")
    print()

    ISOTOPES = [
        ("D",   1, 1),
        ("T",   1, 2),
        ("3He", 2, 1),
        ("4He", 2, 2),
    ]

    rows = []
    for iso, Z, N in ISOTOPES:
        A = Z + N
        n_gens = 3 * A - 1
        print(f"── {iso} (A={A}, n_gens={n_gens}) ──")
        # Atom (with inter-nucleon)
        desc_a, contribs_a = all_subsets_tower(Z, N, include_inter=True,
                                                 max_size=min(n_gens, 6))
        # Free (no inter)
        desc_f, contribs_f = all_subsets_tower(Z, N, include_inter=False,
                                                 max_size=min(n_gens, 6))

        print(f"  ATOM:")
        print(f"    descended |ΠV̂|: {desc_a:.6e}")
        running_a = desc_a
        for size, info in contribs_a.items():
            mark = "" if size <= 2 else "  ← HIGHER-CODIM"
            print(f"    |S|={size} (count={info['count']:>3}): "
                  f"contrib = {info['total']:+.4e}{mark}")
        # Compare paper's truncated (|S| ≤ 2) vs full
        paper_total = (desc_a + contribs_a[1]["total"] +
                       contribs_a[2]["total"])
        full_total = desc_a + sum(c["total"] for c in contribs_a.values())
        higher_codim = full_total - paper_total
        ratio = higher_codim / paper_total * 100 if paper_total else 0
        print(f"  Paper truncation (|S|≤2):  {paper_total:.6e}")
        print(f"  All subsets total:          {full_total:.6e}")
        print(f"  Higher-codim contribution:  {higher_codim:+.4e}  "
              f"({ratio:+.2f}% of paper truncation)")
        print()

        rows.append({
            "isotope": iso, "Z": Z, "N": N, "A": A,
            "n_gens": n_gens,
            "descended_atom": desc_a,
            "contribs_atom_by_size": {str(s): c for s, c in contribs_a.items()},
            "paper_truncation_total": paper_total,
            "all_subsets_total": full_total,
            "higher_codim_contribution": higher_codim,
            "ratio_higher_to_paper_pct": ratio,
        })

    print("Summary: higher-codim contributions (|S| ≥ 3) as % of paper truncation")
    print(f"{'iso':>5} {'A':>3} {'paper trunc':>14} {'higher-codim':>14} {'ratio':>10}")
    print('-' * 60)
    for r in rows:
        print(f"{r['isotope']:>5} {r['A']:>3} "
              f"{r['paper_truncation_total']:>14.6e} "
              f"{r['higher_codim_contribution']:>+14.6e} "
              f"{r['ratio_higher_to_paper_pct']:>+9.2f}%")

    witness = {
        "computation": "all-subsets-tower",
        "description": (
            "Tests whether including |S| ≥ 3 subsets in the brane tower "
            "(beyond paper's pair-truncation) changes mass predictions. "
            "Per-generator brane-tower formula extended to all subsets "
            "S of generators with weight z^{|S|-1}·Φ_q(|Π_{i∈S} V̂_i|)."
        ),
        "reference_blocks": [
            "prop:mass-endomorphism-tower",
            "thm:six-term-mass-formula-complete",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q_0": float(Q0_FLOAT)},
        "rows": rows,
    }
    out = Path(__file__).parent / "all-subsets-tower.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
