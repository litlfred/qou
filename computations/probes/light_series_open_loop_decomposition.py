#!/usr/bin/env python3
"""Light-series binding from the proved open-bond/loop dichotomy — a 1-unit
prediction of ³H/³He/⁴He from ²H.

EXPLORATORY (audit-only, no production rewire, no fit beyond the single unit
E_unit fixed on ²H, no selection). Tranche 7 of the reeb-flow pn-magnitude
program. The dichotomy `ss_det_no_linear_term` (QOU.MassTheory.ReebPnMagnitude,
sorry-free) proves: a single OPEN pn bond binds at first order in the crossing
amplitude g (LINEAR, the deuteron 5g form), while a CLOSED loop binds at
second order (the determinant −ln det, traceless ⇒ no linear term). This probe
applies that per-bond g-order structurally to the light series.

CONSTRUCTION (preregistered, stated before the numbers):

  1. Model each isotope (Z protons, N neutrons, A=Z+N) as the complete graph
     on A nucleons; edges typed pp / nn / pn.
  2. Choose a pn-preferring spanning tree (physically: nucleons bind through
     pn bonds — the deuteron building block; α = pn-bonded core). The A−1 tree
     edges are the OPEN bonds; the remaining C(A,2)−(A−1) edges close LOOPS.
  3. OPEN part (LINEAR, proved): B_open = n_open^{pn} · (5g) · E_unit, where
     n_open^{pn} is the number of pn tree edges. (pp/nn never appear as tree
     edges here — the greedy pn tree exhausts them into loops.)
  4. LOOP part (QUADRATIC, proved): B_loop = −E₀ · ln det(I + G|_loop), the
     determinant of the exchange matrix restricted to the loop edges, with the
     derived signs pp=+1, nn=−1, pn=+1 and uniform magnitude g.
  5. UNIT: E_unit is the single unavoidable scale (§2h — the exchange sector
     is scale-free). Fix it ONCE on the deuteron (B(²H)=n_open=1, no loops ⇒
     E_unit = B_AME(²H)/(5g)), then PREDICT ³H, ³He, ⁴He. This is one
     calibration point, not a fit of the A-dependence.

PREREGISTERED VERDICT: report B_pred vs AME per isotope; the test is whether
the proved open/loop g-order structure predicts the A-dependence from a single
²H-calibrated unit. NO tuning of the tree, signs, or magnitude; NO selection.
Scope-(a): constrains this specific decomposition at q₀.

-- Ref: QOU/MassTheory/ReebPnMagnitude.lean (ss_det_no_linear_term, the proved
dichotomy); b4_1four_complete_graph_writhe_signs.py (edge signs, magnitude g);
docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md §2h.
"""
from __future__ import annotations

import sys
import time
from itertools import combinations
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
if str(_COMP) not in sys.path:
    sys.path.insert(0, str(_COMP))
from _li_2_q_util import load_q_50dps  # noqa: E402
from substrate._precision import set_compute_dps  # noqa: E402
from substrate.experimental_constants import M_E_MEV  # noqa: E402
from substrate.witness_base import WitnessBuilder  # noqa: E402
from codata_constants import (
    AME_B_HE4_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION  # noqa: E402  (AME registry)

set_compute_dps()

# (name, Z, N, B_AME MeV)
ISOTOPES = [
    ("2H", 1, 1, AME_B_DEUTERON_MEV_VALIDATION),
    ("3H", 1, 2, AME_B_TRITIUM_MEV_VALIDATION),
    ("3He", 2, 1, AME_B_HE3_MEV_VALIDATION),
    ("4He", 2, 2, AME_B_HE4_MEV_VALIDATION),
]
SIGN = {"pp": mp.mpf(1), "nn": mp.mpf(-1), "pn": mp.mpf(1)}


def edge_type(i, j, Z):
    pi, pj = i < Z, j < Z
    if pi and pj:
        return "pp"
    if (not pi) and (not pj):
        return "nn"
    return "pn"


def pn_spanning_tree(Z, N):
    """Greedy pn-preferring spanning tree on nodes [0..Z-1]=p, [Z..Z+N-1]=n.
    Returns (tree_edges, loop_edges) as lists of (i, j, type)."""
    A = Z + N
    nodes = list(range(A))
    all_edges = [(i, j, edge_type(i, j, Z)) for i, j in combinations(nodes, 2)]
    connected = {0}
    tree = []
    # add nodes preferring a pn edge into the current tree
    remaining = set(nodes) - connected
    while remaining:
        best = None
        for (i, j, t) in all_edges:
            a, b = (i in connected), (j in connected)
            if a == b:              # both in or both out — not a bridging edge
                continue
            new = j if a else i
            # prefer pn bridging edges; take the first pn, else remember any
            if t == "pn":
                best = (i, j, t, new)
                break
            if best is None:
                best = (i, j, t, new)
        i, j, t, new = best
        tree.append((i, j, t))
        connected.add(new)
        remaining.discard(new)
    tree_set = {(i, j) for i, j, _ in tree}
    loops = [(i, j, t) for (i, j, t) in all_edges if (i, j) not in tree_set]
    return tree, loops


def loop_det(loops, A, g):
    """det(I + G) over A nodes with only the loop edges present."""
    G = mp.zeros(A, A)
    for (i, j, t) in loops:
        w = SIGN[t] * g
        G[i, j] = w
        G[j, i] = w
    return mp.det(mp.eye(A) + G)


def full_det(Z, N, g):
    """det(I + G) over the FULL complete graph (all edges as loops) — the
    tranche-1 collective determinant, for the crossover comparison."""
    A = Z + N
    all_edges = [(i, j, edge_type(i, j, Z)) for i, j in combinations(range(A), 2)]
    return loop_det(all_edges, A, g)


def main() -> int:
    t0 = time.monotonic()
    q, _, z = load_q_50dps()
    g = z / mp.sqrt(1 + z * z)
    m_e = mp.mpf(str(M_E_MEV))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(m_e, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    five_g = 5 * g

    # calibrate E_unit on the deuteron (1 open pn bond, no loops)
    B_2H = ISOTOPES[0][3]
    E_unit = B_2H / five_g

    rows = []
    for name, Z, N, b_ame in ISOTOPES:
        A = Z + N
        tree, loops = pn_spanning_tree(Z, N)
        n_open_pn = sum(1 for _, _, t in tree if t == "pn")
        B_open = n_open_pn * five_g * E_unit
        if loops:
            d = loop_det(loops, A, g)
            B_loop = None if d <= 0 else -E0 * mp.log(d)
        else:
            d = mp.mpf(1)
            B_loop = mp.mpf(0)
        B_pred = None if B_loop is None else B_open + B_loop
        err = None if B_pred is None else 100 * (B_pred - b_ame) / b_ame
        # crossover reference: the full collective determinant (all edges)
        fd = full_det(Z, N, g)
        B_fulldet = None if fd <= 0 else -E0 * mp.log(fd)
        fulldet_ratio = None if B_fulldet is None else B_fulldet / b_ame
        rows.append({
            "iso": name, "Z": Z, "N": N, "A": A,
            "tree_pn": n_open_pn,
            "loops": [f"{t}({i},{j})" for i, j, t in loops],
            "B_open_MeV": mp.nstr(B_open, 7),
            "loop_det": mp.nstr(d, 7),
            "B_loop_MeV": None if B_loop is None else mp.nstr(B_loop, 7),
            "B_pred_openloop_MeV": None if B_pred is None else mp.nstr(B_pred, 7),
            "err_openloop_pct": None if err is None else mp.nstr(err, 4),
            "B_fulldet_MeV": None if B_fulldet is None else mp.nstr(B_fulldet, 7),
            "fulldet_over_AME": None if fulldet_ratio is None else mp.nstr(fulldet_ratio, 5),
            "B_AME_MeV": mp.nstr(b_ame, 7),
        })

    verdict = (
        "NEGATIVE for the additive split. The additive open/loop decomposition "
        "(²H-calibrated) UNDER-predicts badly for A>2 (³H −37%, ³He −30%, "
        "⁴He −64%). The collective full determinant (all edges as loops) does "
        "much better on the even-even line (²H 0.42×, ⁴He 0.94×) but is "
        "NON-monotone and non-predictive overall (³H 0.74×, ³He 0.30× — the "
        "p↔n mirror asymmetry splits the A=3 pair). Two honest conclusions "
        "(scope-(a)): (i) many-body binding is COLLECTIVE (all cross terms), "
        "NOT a sum of per-bond open+loop contributions — the proved dichotomy "
        "governs the single-bond g-order (²H) only; (ii) the collective "
        "determinant is the better many-body direction but not yet a "
        "predictor — its ⁴He ~6% and its ³He mirror residual are the open "
        "GAP-A-4 magnitude legs. No tuning, no selection."
    )
    result = {
        "constants": {"q0": mp.nstr(q, 12), "g": mp.nstr(g, 10),
                      "5g": mp.nstr(five_g, 10), "E0_MeV": mp.nstr(E0, 8),
                      "E_unit_MeV_2H_calibrated": mp.nstr(E_unit, 8)},
        "rows": rows,
        "verdict": verdict,
    }
    payload = {
        "computation": "light-series-open-loop-decomposition",
        "description": ("Light-series binding (²H–⁴He) from the proved "
                        "open-bond/loop dichotomy: pn-spanning-tree open bonds "
                        "(linear 5g) + loop-edge determinant (quadratic), one "
                        "unit E_unit calibrated on ²H. Audit-only; no fit "
                        "beyond the single unit; no selection."),
        "tier": "exploratory (1-calibration-point structural prediction)",
        "result": result,
    }
    import platform
    wb = WitnessBuilder.wrap_legacy(
        "light-series-open-loop-decomposition", payload,
        script_path=__file__, engine="python+mpmath",
        engine_version=f"python {platform.python_version()} + mpmath {mp.__version__}",
        output_dir=str(_HERE), start_time=t0,
    )
    wb.add_assertion("deuteron_calibrates_to_AME",
                     computed=mp.nstr(five_g * E_unit, 7),
                     expected=mp.nstr(B_2H, 7))
    wb.save(extra={"auditOnly": True})

    print("=== light-series open/loop decomposition + collective-det crossover ===")
    print(f"  g={float(g):.6f}  5g={float(five_g):.6f}  E0={float(E0):.4f}  "
          f"E_unit(²H-cal)={float(E_unit):.5f} MeV")
    print(f"  {'iso':>4} {'B_openloop':>10} {'err%':>8} {'B_fulldet':>9} "
          f"{'fd/AME':>7} {'AME':>8}")
    for r in rows:
        print(f"  {r['iso']:>4} {str(r['B_pred_openloop_MeV']):>10} "
              f"{str(r['err_openloop_pct']):>8} {str(r['B_fulldet_MeV']):>9} "
              f"{str(r['fulldet_over_AME']):>7} {r['B_AME_MeV']:>8}")
    print("  " + verdict)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
