#!/usr/bin/env python3
"""PROBE 2 magnitude leg — the single connected [1^4] SU(4) supermultiplet
interface-operator MAGNITUDE at A=4 (⁴He) vs the measured 2.093× super-pairwise
excess, and its A=6 (⁶Li) vanishing.

This is the ONE gated lever named in
docs/scope/2026-07-05-gap-a4-interface-operator-attack-scoping.md §3 Lever 1 and
docs/audits/2026-07-05-delta-lambda-gate-status.md §3 (Option-E via PROBE 2):
the gate (QOU.MassTheory.SU4SupermultipletGate, sorry-free: dim[1^A]=C(4,A),
0 iff A>4) is proved and the LOCALITY is measured (super-pairwise peaks 2.093×
at ⁴He, 0.944× at ⁶Li). The UNTRIED piece is the MAGNITUDE: does the single
connected 4-body [1^4] operator, built from CANONICAL machinery with NO fit,
supply the 2.093× enhancement?

CANONICAL INGREDIENTS (zero-fit, all from the committed pairwise-ceiling probe /
closed_form_tau_M):
  z    = 1/(√q+1/√q)                     Markov parameter
  h    = q − 1/q                         Hecke skein parameter
  f_pp = z,  f_nn = z−h,  f_pn = z−h·(½−δ/4),  δ = flavor_split_leading(q)

The connected 4-body [1^4] operator is the genuinely-connected (Ursell/Mayer)
4-vertex cluster of the ⁴He interface graph K4 on nodes {p,p,n,n}, with the
per-bond Mayer function g_ij = 1 − f_ij (the standard connected-cluster kernel:
1 − ∏_{i<j}(1 − g_ij) = Σ_{clusters} …, the multiplicative binding proxy the
ceiling probe already uses). The connected 4-body magnitude is

  b4c = Σ_{S ⊆ K4, S spans & connects all 4 vertices} ∏_{e∈S} (−g_e)

i.e. the part of the cluster expansion that no product of ≤3-body clusters can
produce — the irreducible 4-body term. The SU(4) gate multiplies by C(4,A):
present (=1) at the ⁴He [1^4] singlet, exactly 0 for A>4 (no [1^5]).

We measure the enhancement the connected term delivers ON TOP of the pairwise
assembly and compare to the required 2.093×. No fit, no scan; a single operator.

`-- Ref:` Wigner 1937 (SU(4) supermultiplet); Ursell 1927 / Mayer cluster
expansion; scoping note §3 Lever 1.
"""
from __future__ import annotations

import sys as _sys
from itertools import combinations
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP),):
    if _p not in _sys.path:
        _sys.path.insert(0, _p)

from mpmath import mp, mpf, log, fabs  # noqa: E402
from closed_form_tau_M import markov_z, hecke_h  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# AME2020 total nuclear binding (MeV), matching the ceiling probe.
AME = {"D": mpf("2.224566"), "4He": mpf("28.295673"), "6Li": mpf("31.994564")}


def bond_factor(a, b, z, h, fpn):
    if a == "p" and b == "p":
        return z
    if a == "n" and b == "n":
        return z - h
    return fpn


def nodes(Z, N):
    return ["p"] * Z + ["n"] * N


def connected_spanning_subgraphs(n):
    """All edge-subsets of K_n (n labeled vertices) that connect all n vertices."""
    verts = list(range(n))
    edges = list(combinations(verts, 2))
    out = []
    for r in range(n - 1, len(edges) + 1):          # need ≥ n−1 edges to span
        for S in combinations(range(len(edges)), r):
            chosen = [edges[i] for i in S]
            # union-find connectivity over all n vertices
            parent = list(range(n))

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            for (u, v) in chosen:
                ru, rv = find(u), find(v)
                if ru != rv:
                    parent[ru] = rv
            if len({find(v) for v in verts}) == 1:
                out.append(chosen)
    return out


def connected_kbody(order, z, h, fpn):
    """Irreducible connected A-body Mayer cluster b_A^c over the K_A interface
    graph for the given node ordering, with g_ij = 1 − f_ij."""
    n = len(order)
    # Mayer functions per (unordered) vertex pair
    g = {}
    for (i, j) in combinations(range(n), 2):
        g[(i, j)] = mpf(1) - bond_factor(order[i], order[j], z, h, fpn)
    total = mpf(0)
    for S in connected_spanning_subgraphs(n):
        prod = mpf(1)
        for (u, v) in S:
            key = (u, v) if (u, v) in g else (v, u)
            prod *= (-g[key])
        total += prod
    return total


def pairwise_2body_sum(order, z, h, fpn):
    """Σ_{i<j} g_ij — the total 2-body Mayer weight (the pairwise assembly scale)."""
    n = len(order)
    s = mpf(0)
    for (i, j) in combinations(range(n), 2):
        s += mpf(1) - bond_factor(order[i], order[j], z, h, fpn)
    return s


def additive_ceiling_ratio(Z, N, z, h, fpn):
    """Best pairwise ceiling as the additive complete-graph Σ(−log f) over D,
    reproducing the committed ceiling witness (add_complete is the max model)."""
    def logsum(Z, N):
        order = nodes(Z, N)
        return mp.fsum(-log(bond_factor(order[i], order[j], z, h, fpn))
                       for (i, j) in combinations(range(len(order)), 2))
    return logsum(Z, N) / logsum(1, 1)


def main() -> int:
    q = mpf(Q_50_DIGIT_STR)
    z, h = markov_z(q), hecke_h(q)
    fpn = z - h * (mpf(1) / 2 - flavor_split_leading(q) / 4)
    print(f"q0={mp.nstr(q,12)}  z={mp.nstr(z,8)}  h={mp.nstr(h,8)}  f_pn={mp.nstr(fpn,8)}")
    print(f"f_pp=z={mp.nstr(z,8)}  f_nn=z-h={mp.nstr(z-h,8)}\n")

    import math
    rows = []
    for atom, (Z, N) in {"D": (1, 1), "4He": (2, 2), "6Li": (3, 3)}.items():
        A = Z + N
        order = nodes(Z, N)
        gate = math.comb(4, A)                       # SU(4) [1^A] dim = C(4,A)
        b_conn = connected_kbody(order, z, h, fpn) if A >= 2 else mpf(0)
        b_pair = pairwise_2body_sum(order, z, h, fpn)
        gated_conn = gate * fabs(b_conn)
        # enhancement the connected [1^4] term delivers on top of pairwise
        # (fraction of the pairwise-2body Mayer scale carried by the irreducible
        #  connected A-body cluster)
        conn_over_pair = fabs(b_conn) / b_pair if b_pair != 0 else mpf(0)
        ceil = additive_ceiling_ratio(Z, N, z, h, fpn)
        r_ame = AME[atom] / AME["D"]
        super_needed = r_ame / ceil
        rows.append({
            "atom": atom, "A": A, "gate_C4A": gate,
            "b_conn_signed": b_conn, "b_conn_abs": fabs(b_conn),
            "b_pair": b_pair, "conn_over_pair": conn_over_pair,
            "gated_conn_abs": gated_conn,
            "ceiling_over_D": ceil, "ame_ratio_over_D": r_ame,
            "super_pairwise_needed": super_needed,
        })

    print(f"  {'atom':>5}{'A':>3}{'C(4,A)':>7}{'|b4c|':>12}{'Σg(2body)':>12}"
          f"{'|b4c|/Σg':>11}{'gated':>10}{'super_need':>11}")
    for d in rows:
        print(f"  {d['atom']:>5}{d['A']:>3}{d['gate_C4A']:>7}"
              f"{mp.nstr(d['b_conn_abs'],6):>12}{mp.nstr(d['b_pair'],6):>12}"
              f"{mp.nstr(d['conn_over_pair'],5):>11}"
              f"{mp.nstr(d['gated_conn_abs'],5):>10}"
              f"{mp.nstr(d['super_pairwise_needed'],5):>11}")

    he4 = next(d for d in rows if d["atom"] == "4He")
    li6 = next(d for d in rows if d["atom"] == "6Li")
    need = float(he4["super_pairwise_needed"])           # 2.093
    # The connected [1^4] operator must MULTIPLY the pairwise ceiling by `need`
    # to reach AME; the enhancement it actually delivers is 1 + |b4c|/Σg (the
    # irreducible 4-body lift over the 2-body scale).
    delivered = 1.0 + float(he4["conn_over_pair"])
    print(f"\n  ⁴He: need super-pairwise ×{need:.3f};  connected [1^4] delivers "
          f"×{delivered:.3f} (1 + |b4c|/Σg)")
    print(f"  ⁴He: gated connected magnitude |b4c|·C(4,4) = "
          f"{mp.nstr(he4['gated_conn_abs'],6)}  vs target excess {need:.3f}")
    print(f"  ⁶Li: SU(4) gate C(4,6)=0 ⟹ gated connected [1^4] = "
          f"{mp.nstr(li6['gated_conn_abs'],4)} (VANISHES — locality ✓)")

    supplies = abs(delivered - need) / need < 0.05        # within 5% = supplies
    partial = 0.5 < delivered / need < 2.0                # right order of magnitude
    verdict = ("SUPPLIES" if supplies else
               "PARTIAL" if partial else "DOES-NOT")
    print(f"\n  VERDICT (magnitude leg): {verdict}")
    print(f"    delivered/need = {delivered/need:.3f}  "
          f"(SUPPLIES if |Δ|<5%, PARTIAL if 0.5–2×, else DOES-NOT)")
    print(f"    A=6 vanishing: {'✓' if float(li6['gated_conn_abs'])==0 else '✗'} "
          f"(SU(4) gate C(4,6)=0)")
    print("    CAVEAT: `delivered` uses a Σg-normalization convention (hidden DOF, "
          "Rule 14); the direct |b4c|=1.96 vs 2.093 (6%) is UNITS-MISMATCHED — "
          "a dimensionless Mayer sum vs a binding-ratio ratio — NOT a derivation.")

    # ── durable witness ──────────────────────────────────────────────
    import json, datetime
    witness = {
        "engine": "mpmath", "engineVersion": "50dps",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "computation": "su4-connected-1111-magnitude",
        "scriptFile": "su4_connected_1111_magnitude_probe.py",
        "description": (
            "PROBE 2 magnitude leg: the single connected 4-body [1^4] "
            "SU(4)-supermultiplet interface operator, realized as the "
            "irreducible connected (Ursell/Mayer) A-body cluster b_A^c of the "
            "canonical zero-fit interface graph (g_ij=1−f_ij; f_pp=z, f_nn=z−h, "
            "f_pn=z−h(½−δ/4)), gated by SU(4) dim C(4,A). Tests whether it "
            "supplies the measured 2.093× super-pairwise excess at ⁴He and "
            "vanishes at ⁶Li (C(4,6)=0). Audit-only, no fit, single operator."),
        "tier": "structural (zero-fit canonical bond factors + proved SU(4) gate)",
        "data": {
            "q0": str(q), "z": str(z), "h": str(h), "f_pn": str(fpn),
            "per_atom": {
                d["atom"]: {
                    "A": d["A"], "gate_C4A": d["gate_C4A"],
                    "b_conn_abs": str(d["b_conn_abs"]),
                    "b_pair_2body": str(d["b_pair"]),
                    "conn_over_pair": str(d["conn_over_pair"]),
                    "gated_conn_abs": str(d["gated_conn_abs"]),
                    "super_pairwise_needed": str(d["super_pairwise_needed"]),
                } for d in rows},
            "he4_delivered_enhancement": float(delivered),
            "he4_needed_enhancement": float(need),
            "he4_delivered_over_needed": float(delivered / need),
            "verdict": verdict,
            "verdict_note": (
                "PARTIAL / scope-(a): the connected [1^4] cluster is right-KIND "
                "(irreducible 4-body), right-LOCALITY (A=6 vanishing supplied by "
                "the PROVED gate C(4,6)=0 — the ungated cluster overshoots to "
                "22.2, so the gate is load-bearing), and right-ORDER at A=4 "
                "(×1.54 delivered vs ×2.09 needed, 74%). It does NOT close the "
                "magnitude parameter-free: the exact value is convention-"
                "dependent (Σg-normalization hidden DOF). Does NOT exclude the "
                "ingredient; constrains the magnitude."),
        },
        "assertions": [
            {"name": "a6_vanishes_via_gate",
             "computed": str(float(li6["gated_conn_abs"]) == 0.0), "expected": "True",
             "passed": float(li6["gated_conn_abs"]) == 0.0},
            {"name": "a4_right_order_of_magnitude",
             "computed": str(partial), "expected": "True", "passed": bool(partial)},
        ],
        "allPassed": bool(float(li6["gated_conn_abs"]) == 0.0 and partial),
        "auditOnly": True,
        "context": {
            "axis": "GAP-A-4 class-D — A=4 interface operator (Δ_λ magnitude leg)",
            "gate_lean": "qou:QOU.MassTheory.SU4SupermultipletGate",
            "locality_witness": "probes/su4-supermultiplet-locality.witness.json",
            "scoping": "docs/scope/2026-07-05-gap-a4-interface-operator-attack-scoping.md §3",
        },
    }
    out = _HERE / "su4-connected-1111-magnitude.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
    witness["scriptFile"] = _os.path.basename(__file__)
    out.write_text(json.dumps(witness, indent=2, default=str), encoding="utf-8")
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
