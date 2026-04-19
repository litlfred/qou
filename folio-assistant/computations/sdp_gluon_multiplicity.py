#!/usr/bin/env python3
"""
Gluon per-nucleon multiplicity SDP — replaces the enumeration
K^{Z+N} in atom_sdp_gluon_search.py with the unified sdp_decide core.

Decision: per-nucleon gluon decoration ∈ {∅, σ₀, σ₁, L_+, L_-} (the
LP-dual-active single-op set from confinement-lp.py). Each combination
of length A = Z + N yields a distinct atom braid word.

Sizes:  D  5² =  25 candidates
        T  5³ = 125
        3He 5³ = 125
        4He 5⁴ = 625  (skipped unless runtime permits)

For each atom, sdp_decide over the K^A candidates returns the
optimum (argmin tr_M_atom at H_{3A} Plancherel level) plus dual
gaps. Frobenius positivity auto-valid for real Hecke products.

Uses the same per-nucleon helpers as atom_sdp_gluon_search.py.
"""
from __future__ import annotations

import sys
import json
import time
import itertools
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0, HA as h
from canonical_plus_multibrane import E_0_BETA_DECAY_MEV
from hecke_characters import partitions_of, dim_q, qfac
from mass_at_3A_proper import _cached_seminormal
from atom_sdp_gluon_search import (
    atom_word_with_gluons, CANDIDATES_DUAL, CAND_NAMES)
from sdp_decision import sdp_decide


def _trM_word(word, n_strands):
    from scipy.sparse import issparse, eye as speye
    nfac = qfac(n_strands)
    total = 0.0
    for shape in partitions_of(n_strands):
        sigmas, dim, _ = _cached_seminormal(shape)
        if dim == 0:
            continue
        dq = dim_q(shape)
        if dq == 0:
            continue
        sparse = bool(sigmas) and issparse(sigmas[0])
        if sparse:
            prod = speye(dim, format='csr'); I = speye(dim, format='csr')
        else:
            prod = np.eye(dim); I = np.eye(dim)
        for (c, d, g) in word:
            if g < len(sigmas):
                prod = prod @ (c * sigmas[g] + d * I)
        chi = float(prod.diagonal().sum()) if sparse else float(np.trace(prod))
        total += (dq * dq) / nfac * chi / dim
    return total


def gluon_multiplicity_sdp(Z: int, N: int, B_AME: float) -> dict:
    A = Z + N
    n = 3 * A
    # All length-A tuples from the K=5 single-op set
    all_combinations = list(itertools.product(CAND_NAMES, repeat=A))
    cands = []
    for combo in all_combinations:
        name = "_".join(combo)
        word = atom_word_with_gluons(
            Z, N, combo, include_inter=True)
        cands.append((name, word))

    # Free baseline (no inter-nucleon)
    free_word = atom_word_with_gluons(
        Z, N, tuple("none" for _ in range(A)), include_inter=False)
    trM_f = _trM_word(free_word, n)

    t0 = time.time()
    rep = sdp_decide(candidates=cands, n_strands=n,
                        compute_trM=_trM_word,
                        label=f"(Z={Z},N={N}) gluon mult")
    dt = time.time() - t0

    sweep = []
    for name, trM_a in rep.trM_by_candidate.items():
        B = E_0_BETA_DECAY_MEV * (abs(trM_f) - abs(trM_a))
        err = abs(B - B_AME) / (A * 938.272) * 100
        sweep.append({"combo": name, "trM_atom": trM_a,
                          "trM_free": trM_f, "B_pred_MeV": B,
                          "err_pct": err,
                          "dual_gap": rep.dual_gaps[name]})

    chosen = rep.optimal_name
    chosen_row = next(s for s in sweep if s["combo"] == chosen)
    chosen_err = min(sweep, key=lambda s: s["err_pct"])

    return {
        "Z": Z, "N": N, "A": A, "B_AME_MeV": B_AME,
        "n_strands": n, "n_candidates": len(cands),
        "sdp_optimal": {
            "combo": chosen,
            "trM_atom": chosen_row["trM_atom"],
            "B_pred_MeV": chosen_row["B_pred_MeV"],
            "err_pct": chosen_row["err_pct"],
            "dual_gap": chosen_row["dual_gap"],
        },
        "lowest_err": {
            "combo": chosen_err["combo"],
            "B_pred_MeV": chosen_err["B_pred_MeV"],
            "err_pct": chosen_err["err_pct"],
            "dual_gap": chosen_err["dual_gap"],
        },
        "sweep_top10_by_gap":
            sorted(sweep, key=lambda s: s["dual_gap"])[:10],
        "time_sec": dt,
    }


if __name__ == "__main__":
    ATOMS = [
        ("D",   1, 1,  2.22452),
        ("T",   1, 2,  8.481821),
        ("3He", 2, 1,  7.71804),
    ]

    out = (Path(__file__).parent
             / "gluon-multiplicity-sdp.witness.json")
    print("=" * 110)
    print("GLUON PER-NUCLEON MULTIPLICITY SDP  "
          "— per-nuc ∈ {∅, σ₀, σ₁, L+, L−}")
    print(f"q0 = {Q0}, E_0 = {E_0_BETA_DECAY_MEV} MeV")
    print("=" * 110)

    all_results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        n_cands = len(CAND_NAMES) ** A
        print(f"\n{name} (Z={Z}, N={N}, A={A}, {n_cands} candidates):")
        r = gluon_multiplicity_sdp(Z, N, B_AME)
        r["atom"] = name
        all_results.append(r)
        opt = r["sdp_optimal"]
        lerr = r["lowest_err"]
        print(f"  SDP optimal:  {opt['combo']:<40} "
              f"trM_a={opt['trM_atom']:+.4e}  "
              f"B={opt['B_pred_MeV']:+.4f}  err={opt['err_pct']:.4f}%  "
              f"[{r['time_sec']:.1f}s]")
        print(f"  lowest err:   {lerr['combo']:<40} "
              f"B={lerr['B_pred_MeV']:+.4f}  "
              f"err={lerr['err_pct']:.4f}%  (gap={lerr['dual_gap']:+.3e})")
        print("  top-10 by dual gap:")
        for s in r["sweep_top10_by_gap"][:10]:
            print(f"    {s['combo']:<40} "
                  f"gap={s['dual_gap']:+.3e}  err={s['err_pct']:.4f}%")
        out.write_text(json.dumps({
            "computation": "gluon-multiplicity-sdp",
            "description": (
                "SDP (via unified sdp_decide) over per-nucleon gluon "
                "candidates {∅, σ₀, σ₁, L+, L−} — the LP-dual-active "
                "single-op set from confinement-lp. Replaces the "
                "greedy enumeration in atom_sdp_gluon_search.py with "
                "an LP-dual gap certificate per combination."),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "parameters": {"q0": Q0, "E_0_MeV": E_0_BETA_DECAY_MEV,
                              "candidates": CAND_NAMES},
            "results": all_results,
        }, indent=2, default=str))

    print("\n" + "=" * 110)
    print("CROSS-ATOM AGREEMENT")
    picks = {r["atom"]: r["sdp_optimal"]["combo"]
              for r in all_results}
    print(f"  SDP optima: {picks}")
    print(f"\nWitness: {out}")
