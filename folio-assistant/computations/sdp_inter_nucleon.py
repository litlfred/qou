#!/usr/bin/env python3
"""
Inter-nucleon SDP — replaces the greedy-min sweep in
inter_nucleon_crossing_sweep.py with the unified sdp_decide core.

Decision variables: (m_pp, m_pn, m_nn) ∈ {1..3}³ — integer crossing
counts for proton-proton, proton-neutron, and neutron-neutron pair
couplings in the atom braid word.

Per atom, each candidate triple yields a distinct braid word via
mass_at_3A_proper.atom_braid_word_3A, and we compute tr_M_atom at
the H_{3A} Plancherel level. The SDP decide core returns:
  • optimal triple (argmin tr_M_atom)
  • dual gap per candidate (SDP certificate)
  • all 27 tr_M values for transparency

For real Hecke products the Frobenius positivity constraint is
auto-satisfied (no need for Lasserre moment lift); the LP dual
provides the optimality certificate.

Witness records per-atom picks + dual gaps so we can diagnose whether
different atoms agree on optimal (m_pp, m_pn, m_nn) or diverge.
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
from mass_at_3A_proper import _cached_seminormal, atom_braid_word_3A
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


def inter_nucleon_sdp(Z: int, N: int, B_AME: float,
                          m_range: range = range(1, 4)) -> dict:
    """SDP over (m_pp, m_pn, m_nn) candidate triples for one atom."""
    A = Z + N
    n = 3 * A
    cands = []
    for (mpp, mpn, mnn) in itertools.product(m_range, m_range, m_range):
        name = f"pp{mpp}_pn{mpn}_nn{mnn}"
        word = list(atom_braid_word_3A(
            Z, N, m_pp=mpp, m_pn=mpn, m_nn=mnn,
            include_inter=True, include_electrons=True))
        cands.append((name, word))

    # Free baseline (no inter, no electrons) is independent of the triple
    word_free = list(atom_braid_word_3A(
        Z, N, include_inter=False, include_electrons=False))
    trM_f = _trM_word(word_free, n)

    t0 = time.time()
    rep = sdp_decide(candidates=cands, n_strands=n,
                        compute_trM=_trM_word,
                        label=f"(Z={Z},N={N}) inter-nucleon")
    dt = time.time() - t0

    # Compute B_pred and err for each candidate
    sweep = []
    for name in rep.trM_by_candidate:
        trM_a = rep.trM_by_candidate[name]
        B = E_0_BETA_DECAY_MEV * (abs(trM_f) - abs(trM_a))
        err = abs(B - B_AME) / (A * 938.272) * 100
        sweep.append({"triple": name,
                          "trM_atom": trM_a, "trM_free": trM_f,
                          "B_pred_MeV": B, "err_pct": err,
                          "dual_gap": rep.dual_gaps[name]})
    chosen = rep.optimal_name
    chosen_row = next(s for s in sweep if s["triple"] == chosen)
    chosen_err = min(sweep, key=lambda s: s["err_pct"])

    return {
        "Z": Z, "N": N, "A": A, "B_AME_MeV": B_AME,
        "n_strands": n,
        "n_candidates": len(cands),
        "sdp_optimal": {
            "triple": chosen,
            "trM_atom": chosen_row["trM_atom"],
            "B_pred_MeV": chosen_row["B_pred_MeV"],
            "err_pct": chosen_row["err_pct"],
            "dual_gap": chosen_row["dual_gap"],
        },
        "lowest_err": {
            "triple": chosen_err["triple"],
            "B_pred_MeV": chosen_err["B_pred_MeV"],
            "err_pct": chosen_err["err_pct"],
            "dual_gap": chosen_err["dual_gap"],
        },
        "sweep": sweep,
        "time_sec": dt,
    }


if __name__ == "__main__":
    ATOMS = [
        ("D",   1, 1,  2.22452),
        ("T",   1, 2,  8.481821),
        ("3He", 2, 1,  7.71804),
    ]

    out = (Path(__file__).parent
             / "inter-nucleon-sdp.witness.json")
    print("=" * 110)
    print("INTER-NUCLEON SDP  — (m_pp, m_pn, m_nn) ∈ {1..3}³")
    print(f"q0 = {Q0}, E_0 = {E_0_BETA_DECAY_MEV} MeV")
    print("=" * 110)

    all_results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        print(f"\n{name} (Z={Z}, N={N}, A={A}, n={3*A}):")
        r = inter_nucleon_sdp(Z, N, B_AME)
        r["atom"] = name
        all_results.append(r)
        opt = r["sdp_optimal"]
        lerr = r["lowest_err"]
        print(f"  SDP optimal:  {opt['triple']}  "
              f"trM_a={opt['trM_atom']:+.4e}  "
              f"B={opt['B_pred_MeV']:+.4f}  err={opt['err_pct']:.4f}%  "
              f"[{r['time_sec']:.1f}s]")
        print(f"  lowest err:   {lerr['triple']}  "
              f"B={lerr['B_pred_MeV']:+.4f}  err={lerr['err_pct']:.4f}%  "
              f"(gap={lerr['dual_gap']:+.3e})")
        # Top 5 by dual gap (smallest first = closest to optimal)
        top5 = sorted(r["sweep"], key=lambda s: s["dual_gap"])[:5]
        for s in top5:
            print(f"    {s['triple']:>20}  gap={s['dual_gap']:+.3e}  "
                  f"err={s['err_pct']:.4f}%")
        out.write_text(json.dumps({
            "computation": "inter-nucleon-sdp",
            "description": (
                "SDP (via unified sdp_decide core) over integer "
                "triples (m_pp, m_pn, m_nn) ∈ {1,2,3}³ for the "
                "inter-nucleon crossing counts in the atom braid. "
                "Each triple produces a distinct Hecke word; optimum "
                "= argmin tr_M_atom at H_{3A} Plancherel level with "
                "LP-dual gap certificates. Frobenius auto-valid for "
                "real Hecke products."),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "parameters": {"q0": Q0, "E_0_MeV": E_0_BETA_DECAY_MEV,
                              "m_range": list(range(1, 4))},
            "results": all_results,
        }, indent=2, default=str))

    # Cross-atom agreement check
    print("\n" + "=" * 110)
    print("CROSS-ATOM AGREEMENT")
    picks = {r["atom"]: r["sdp_optimal"]["triple"] for r in all_results}
    print(f"  SDP optima per atom: {picks}")
    unique = set(picks.values())
    if len(unique) == 1:
        print(f"  All atoms agree on optimal triple: {unique.pop()}")
    else:
        print(f"  Atoms disagree — {len(unique)} distinct optima: {unique}")

    print(f"\nWitness: {out}")
