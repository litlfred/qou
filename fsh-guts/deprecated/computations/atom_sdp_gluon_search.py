#!/usr/bin/env python3
# DEPRECATION-CANDIDATE: witness was moved to computations/_deprecated/ in PR #554 (dead-exploratory).
# This .py script is kept in place because it is still imported by live code; revisit when the live importer is itself retired or rewired.
"""
Full-atom SDP gluon search (P2.1b of the 1-ppm workplan).

Per-nucleon gluon decoration is currently uniform (2·σ₀ on every
nucleon) via ``hecke_core.nucleon_gen_chains``.  The session probe
``atom_braid_sdp_gluon.py`` tested swapping neutron to L+L− under the
H_3-LP optimum — it HURT performance, confirming per-nucleon H_3
optima don't transfer to atom-level H_{3A}.

The true fix searches per-nucleon gluons under the **atom-level**
objective: for each combination of gluons on each nucleon, compute
the full 3A-strand Markov trace via partition-sum seminormal
characters, assemble canonical binding B = E_0 · (|tr_M_free| −
|tr_M_atom|), and compare to AME.

Frobenius-positivity is satisfied automatically: Candidate #2 of the
V-hat-within-level probes verified that every real Hecke braid
product has xᵀGx > 0 on the atom NF (cf.
v-hat-gram-projection-probe.witness.json).  So the "SDP" here is the
moral feasibility certificate, guaranteed a priori, and the search
reduces to a per-nucleon integer program over candidate gluon
decorations.

Candidate gluons (H_3 right-multiplication by each):
  ∅       — no extra gluon
  σ₀      — one σ_0
  σ₀σ₀    — two σ_0 (current default)
  σ₀σ₁σ₁σ₀ (= L+ L-)

For each atom (Z, N), enumerates K^{Z+N} combinations where K =
len(candidates) = 4.  For D this is 16; for T/3He 64; for 4He 256.
Partitions dominate cost; D runs in seconds, 4He in minutes.
"""
from __future__ import annotations

import sys
import json
import math
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
from hecke_core import _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1


# ── Candidate gluon tails (sequence of (c, d, local_gen_index)) ──
#
# Candidate set derived from the LP-DUAL of confinement-lp.py:
# the H_3(q) LP-dual's active NF-basis directions are
#   {𝟙, σ₀, σ₁, σ₀σ₁ (= L+), σ₁σ₀ (= L−), σ₀σ₁σ₀ (= e⁻)}.
# `integer-lp-gluon.py` extracts the four single-op integer
# directions {σ₀, σ₁, L+, L−} as gluon primitives (with 𝟙 implicit
# = "no gluon"; e⁻ excluded as length-3).
#
# The atom-level gluon candidate set is therefore the LP-dual-
# active integer set:
#
#     {∅, σ₀, σ₁, L+, L−}            (K = 5, single-op LP-dual basis)
#
# Length-2+ compositions (σ₀σ₀, L+L−, ...) live in the length-2
# simplex of the same dual cone; include them as an extended set
# for the robustness check but not by default.
#
# Earlier versions hard-coded only {∅, σ₀, σ₀σ₀, L+L−} — a subset
# biased toward length-matching the pre-existing 2·σ₀ default.
# That missed σ₁, L+, L− as per-nucleon candidates (gemini-style
# LP-dual critique on session discussion).
#
# local_gen_index ∈ {0, 1}: 0 = σ at base_gen, 1 = σ at base_gen+1.

CANDIDATES_DUAL = {
    "none": [],
    "s0":   [(1.0, 0.0, 0)],
    "s1":   [(1.0, 0.0, 1)],
    "Lp":   [(1.0, 0.0, 0), (1.0, 0.0, 1)],
    "Lm":   [(1.0, 0.0, 1), (1.0, 0.0, 0)],
}

CANDIDATES_EXTENDED = {
    **CANDIDATES_DUAL,
    "s0s0": [(1.0, 0.0, 0), (1.0, 0.0, 0)],
    "s1s1": [(1.0, 0.0, 1), (1.0, 0.0, 1)],
    "LpLm": [(1.0, 0.0, 0), (1.0, 0.0, 1),
             (1.0, 0.0, 1), (1.0, 0.0, 0)],
    "LmLp": [(1.0, 0.0, 1), (1.0, 0.0, 0),
             (1.0, 0.0, 0), (1.0, 0.0, 1)],
}

# Default: LP-dual-correct K=5 single-op set.
CANDIDATES = CANDIDATES_DUAL
CAND_NAMES = list(CANDIDATES.keys())


def _strip_gluon_tail(chain: list[tuple[float, float]]
                       ) -> list[tuple[float, float]]:
    """Remove trailing (1,0)(1,0) gluon pair from a g0 chain."""
    if len(chain) < 2:
        return list(chain)
    last_two = [(float(c), float(d)) for (c, d) in chain[-2:]]
    if last_two == [(1.0, 0.0), (1.0, 0.0)]:
        return list(chain[:-2])
    return list(chain)


_PROTON_G0_BODY = _strip_gluon_tail(_PROTON_G0)
_NEUTRON_G0_BODY = _strip_gluon_tail(_NEUTRON_G0)


def atom_word_with_gluons(Z: int, N: int, gluons: tuple[str, ...],
                             *, include_inter: bool,
                             m_pp: int = 1, m_pn: int = 1,
                             m_nn: int = 1
                             ) -> list[tuple[float, float, int]]:
    """Atom braid word with per-nucleon gluon tail specified by
    `gluons[k]` — a name from CANDIDATES — for nucleon k."""
    A = Z + N
    assert len(gluons) == A, f"expected {A} gluon names, got {len(gluons)}"
    ordering = ['p'] * Z + ['n'] * N
    word: list[tuple[float, float, int]] = []
    for k, nuc in enumerate(ordering):
        base = 3 * k
        body_g0 = _PROTON_G0_BODY if nuc == 'p' else _NEUTRON_G0_BODY
        body_g1 = _PROTON_G1 if nuc == 'p' else _NEUTRON_G1
        for (c, d) in body_g0:
            word.append((float(c), float(d), base))
        for (c, d) in body_g1:
            word.append((float(c), float(d), base + 1))
        for (c, d, local_g) in CANDIDATES[gluons[k]]:
            word.append((c, d, base + local_g))
        if include_inter and k < A - 1:
            i_inter = 3 * k + 2
            nxt = ordering[k + 1]
            if nuc == 'p' and nxt == 'p':
                base_cross = (1.0, 0.0); m_this = m_pp
            elif nuc == 'n' and nxt == 'n':
                base_cross = (1.0, -h); m_this = m_nn
            else:
                base_cross = (1.0, -h / 2); m_this = m_pn
            c, d = base_cross
            for _ in range(m_this):
                word.append((c, d, i_inter))
    return word


def trM_plancherel(Z: int, N: int, gluons: tuple[str, ...],
                     include_inter: bool) -> float:
    """Plancherel-weighted Markov trace on the atom braid word."""
    from scipy.sparse import issparse, eye as speye
    A = Z + N
    n = 3 * A
    word = atom_word_with_gluons(Z, N, gluons, include_inter=include_inter)
    nfac = qfac(n)
    total = 0.0
    for shape in partitions_of(n):
        sigmas, dim, _syts = _cached_seminormal(shape)
        if dim == 0:
            continue
        dq = dim_q(shape)
        if dq == 0:
            continue
        w = (dq * dq) / nfac
        sparse = bool(sigmas) and issparse(sigmas[0])
        if sparse:
            prod = speye(dim, format='csr')
            I = speye(dim, format='csr')
        else:
            prod = np.eye(dim)
            I = np.eye(dim)
        for (c, d, g) in word:
            if g < len(sigmas):
                prod = prod @ (c * sigmas[g] + d * I)
        chi = float(prod.diagonal().sum()) if sparse \
            else float(np.trace(prod))
        total += w * chi / dim
    return total


def search_atom(Z: int, N: int, B_AME: float, *,
                  E_0: float = E_0_BETA_DECAY_MEV,
                  limit: int = None) -> dict:
    """Enumerate all per-nucleon gluon combinations; rank by
    |B_pred − B_AME|.  Returns the best + top-5 runner-ups."""
    A = Z + N
    Mtot = A * 938.272
    # tr_M for the FREE path depends only on gluon choice (no inter
    # crossings).  tr_M for ATOM also depends on inter crossings.
    # We enumerate (gluon_0, ..., gluon_{A-1}) ∈ CAND_NAMES^A.
    combos = list(itertools.product(CAND_NAMES, repeat=A))
    if limit is not None:
        combos = combos[:limit]
    t0 = time.time()

    # Cache tr_M_free per gluon tuple (doesn't depend on inter crossings).
    free_cache: dict[tuple[str, ...], float] = {}
    rows = []
    for combo in combos:
        if combo not in free_cache:
            free_cache[combo] = trM_plancherel(
                Z, N, combo, include_inter=False)
        trM_free = free_cache[combo]
        trM_atom = trM_plancherel(Z, N, combo, include_inter=True)
        B_pred = E_0 * (abs(trM_free) - abs(trM_atom))
        err_pct = abs(B_pred - B_AME) / Mtot * 100
        rows.append({
            "gluons": list(combo),
            "trM_free": trM_free,
            "trM_atom": trM_atom,
            "B_pred_MeV": B_pred,
            "err_pct": err_pct,
        })

    rows.sort(key=lambda r: r["err_pct"])
    dt = time.time() - t0
    return {
        "Z": Z, "N": N, "A": A,
        "E_0_MeV": E_0, "B_AME_MeV": B_AME,
        "n_combos": len(rows),
        "elapsed_sec": dt,
        "best": rows[0],
        "top5": rows[:5],
        "default_s0s0": next(
            (r for r in rows if r["gluons"] == ["s0s0"] * A),
            None),  # current hecke_core default (two sigma_0 per nucleon)
        "default_s0": next(
            (r for r in rows if r["gluons"] == ["s0"] * A),
            None),  # P2.1b finding (one sigma_0 per nucleon)
    }


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(
        description="Full-atom SDP gluon search (P2.1b)")
    ap.add_argument("--atoms", default="D,T,3He",
                      help="Comma-separated atom symbols to search")
    ap.add_argument("--limit", type=int, default=None,
                      help="Limit combinations per atom (for quick runs)")
    ap.add_argument("--extended", action="store_true",
                      help="Use extended K=9 candidate set (LP-dual "
                           "single ops + length-2 compositions)")
    args = ap.parse_args()

    if args.extended:
        CANDIDATES = CANDIDATES_EXTENDED
        CAND_NAMES = list(CANDIDATES.keys())

    ALL = {
        "H":   (1, 0,  0.0),
        "D":   (1, 1,  2.22452),
        "T":   (1, 2,  8.481821),
        "3He": (2, 1,  7.71804),
        "4He": (2, 2, 28.295674),
    }
    atoms = [a for a in args.atoms.split(",") if a in ALL]

    print("=" * 110)
    print("FULL-ATOM SDP GLUON SEARCH  (P2.1b)")
    print(f"q0 = {Q0},  E_0 = {E_0_BETA_DECAY_MEV} MeV,  "
          f"candidates = {CAND_NAMES}")
    print("=" * 110)

    results = []
    for name in atoms:
        Z, N, B_AME = ALL[name]
        A = Z + N
        print(f"\n{name} (Z={Z}, N={N}, A={A}, "
              f"{len(CAND_NAMES)}^{A} = {len(CAND_NAMES) ** A} combos, "
              f"B_AME = {B_AME} MeV)")
        r = search_atom(Z, N, B_AME, limit=args.limit)
        print(f"  elapsed {r['elapsed_sec']:.1f}s, "
              f"{r['n_combos']} combos enumerated")
        d22 = r.get("default_s0s0") or {}
        d21 = r.get("default_s0") or {}
        if d22:
            print(f"  baseline s0s0×A (hecke_core default): "
                  f"B={d22.get('B_pred_MeV', 0):+10.4f}  "
                  f"err={d22.get('err_pct', 0):.4f}%")
        if d21:
            print(f"  baseline s0×A   (P2.1b earlier finding): "
                  f"B={d21.get('B_pred_MeV', 0):+10.4f}  "
                  f"err={d21.get('err_pct', 0):.4f}%")
        print(f"  Top-5 (lowest err):")
        for i, row in enumerate(r["top5"]):
            marker = "  ★" if row["gluons"] == ["s0s0"] * A else "  "
            print(f"{marker} [{i+1}] gluons={row['gluons']}  "
                  f"B={row['B_pred_MeV']:+10.4f}  "
                  f"err={row['err_pct']:.4f}%")
        results.append({"atom": name, **r})

    # Verdict
    print("\n" + "=" * 110)
    print("VERDICT: best per-atom gluon combination vs baselines")
    print("=" * 110)
    for r in results:
        best = r["best"]
        d22 = r.get("default_s0s0") or {}
        d21 = r.get("default_s0") or {}
        line = f"  {r['atom']:>5}: best={best['gluons']}  " \
               f"err={best['err_pct']:.4f}%"
        if d22:
            line += f"  vs s0s0×A: {d22.get('err_pct', 0):.4f}%" \
                    f" (Δ={best['err_pct']-d22['err_pct']:+.4f}%)"
        if d21:
            line += f"  vs s0×A: {d21.get('err_pct', 0):.4f}%" \
                    f" (Δ={best['err_pct']-d21['err_pct']:+.4f}%)"
        print(line)

    witness = {
        "computation": "atom-sdp-gluon-search",
        "description": (
            "Full-atom SDP gluon selection (P2.1b): enumerate per-"
            "nucleon gluon decorations (∅ / σ₀ / σ₀σ₀ / L+L−) and "
            "rank by binding error vs AME.  Frobenius positivity is "
            "automatic for real Hecke products (Candidate #2 "
            "finding); the search is therefore a combinatorial "
            "integer program with SDP feasibility implicit.  Uses "
            "the Plancherel-weighted partition-sum trace for "
            "performance (canonical symbolic trace is infeasible for "
            "n ≥ 9 in a full sweep)."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q0": Q0, "E_0_MeV": E_0_BETA_DECAY_MEV,
            "candidates": CAND_NAMES,
        },
        "results": results,
    }
    out = Path(__file__).parent / "atom-sdp-gluon-search.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
