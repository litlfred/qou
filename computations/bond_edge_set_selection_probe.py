#!/usr/bin/env python3
"""Edge-set selection for the bond-graph binding — can ANY static graph close?

EXPLORATORY (no production rewire). Owner directive 2026-06-10 next-step 1:
"edge-set selection — derive the physical bond graph". Follows the derived
per-bond kernel (`derived_bond_graph_binding.py`, `f_bond = c·z + d`).

## The sharp question (formalize-first style)

With the per-bond energies FIXED by the substrate (E_0·log(1/f): pp 2.907,
pn 3.890, nn 5.178 MeV — derived, not fitted), the bond-graph binding over an
edge multiset E is B(E) = Σ_{e∈E} E_0·log(1/f_e). Does any STATIC edge set
(chain, complete, or anything between) close D/T/³He/⁴He simultaneously?

Invert per nucleus: the REQUIRED total log is L_req = B_AME/E_0; compare to the
available bond menus. Since each nucleus's possible pair types are fixed by
(Z, N), the full class of static graphs is the integer box
0 ≤ n_pp ≤ C(Z,2), 0 ≤ n_pn ≤ Z·N, 0 ≤ n_nn ≤ C(N,2) — small enough to
ENUMERATE EXACTLY (≤ 8 combos for A ≤ 4). The verdict is decided by the
extreme points:

  - D (Z=N=1): only menu is {0 or 1 pn} → max L = 0.929, required 0.531.
    The single bond OVERSHOOTS by 1.75× and the only smaller option is 0.
    **No integer edge set hits D** — the deuteron is anomalously loose
    (a sub-unit bond occupancy ~0.57, halo physics).
  - ⁴He (Z=N=2): the COMPLETE graph (1 pp + 4 pn + 1 nn) gives max
    L = 5.649, required 6.760. **Even the complete graph under-binds ⁴He
    by 1.20×** — no pairwise edge set suffices; a genuine many-body /
    doubly-magic term is REQUIRED (consistent with the step9 ledger §3
    "3-body residual is genuine many-body").

So the static-edge-set class is REFUTED as a complete closure: D needs
< 1 bond, ⁴He needs > complete. The bond graph is not a static integer
graph — the physical structure is fractional occupancy / shell weighting
(Pauli/saturation), which is the per-nucleus volume route (#2078), not an
edge-set choice. This probe records the exact per-nucleus enumeration so the
refutation is checkable, plus the best integer edge set per nucleus (for
the record — T's chain at 0.94 and ³He's chain+ at ~1 are individually
close; only the JOINT closure fails).

Output: bond-edge-set-selection.witness.json
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from witness_base import WitnessBuilder  # noqa: E402


def _constants():
    from q_parameter import Q as q0, HA as h
    from codata_constants import M_E_MEV as me
    q0, h, me = float(q0), float(h), float(me)
    z = 1.0 / (q0 ** 0.5 + q0 ** (-0.5))
    try:
        from canonical_braid_crossings import _avg_color_delta
        delta = float(_avg_color_delta())
    except Exception:
        delta = 0.0
    E0 = me / (q0 * (q0 - 1.0))
    return q0, h, z, delta, me, E0


def main() -> int:
    t0 = time.time()
    q0, h, z, delta, me, E0 = _constants()
    f = {"pp": z, "nn": z - h, "pn": z - h * (0.5 - delta / 4.0)}
    lg = {k: math.log(1.0 / v) for k, v in f.items()}  # per-bond log

    bc = json.loads((HERE / "binding-canonical.witness.json").read_text())
    res = {(r["Z"], r["N"]): r for r in bc["data"]["results"]
           if r.get("status") == "solved"}

    rows = []
    joint_closure_possible = True
    for (Z, N), r in sorted(res.items(), key=lambda kv: (kv[0][0] + kv[0][1], kv[0])):
        A = Z + N
        B_ame = float(r["B_AME_MeV"])
        L_req = B_ame / E0
        max_pp, max_pn, max_nn = Z * (Z - 1) // 2, Z * N, N * (N - 1) // 2

        # EXACT enumeration of every integer edge multiset (the static class).
        best = None
        combos = []
        for npp in range(max_pp + 1):
            for npn in range(max_pn + 1):
                for nnn in range(max_nn + 1):
                    L = npp * lg["pp"] + npn * lg["pn"] + nnn * lg["nn"]
                    miss = (B_ame / (E0 * L)) if L > 0 else float("inf")
                    combos.append({"pp": npp, "pn": npn, "nn": nnn,
                                   "L": round(L, 4),
                                   "miss_x": round(miss, 3) if L > 0 else None})
                    if L > 0 and (best is None or
                                  abs(math.log(miss)) < abs(math.log(best["miss_x"]))):
                        best = combos[-1]
        L_complete = max_pp * lg["pp"] + max_pn * lg["pn"] + max_nn * lg["nn"]
        closable = any(c["L"] > 0 and 0.95 <= c["miss_x"] <= 1.05 for c in combos)
        if not closable:
            joint_closure_possible = False

        rows.append({
            "atom": r["atom"], "Z": Z, "N": N, "A": A,
            "B_AME_MeV": round(B_ame, 4),
            "L_required": round(L_req, 4),
            "edge_box": {"pp": max_pp, "pn": max_pn, "nn": max_nn},
            "L_complete_graph": round(L_complete, 4),
            "complete_vs_required": round(L_req / L_complete, 3) if L_complete else None,
            "n_integer_edge_sets": len(combos),
            "best_integer_edge_set": best,
            "closable_within_5pct": closable,
            "all_combos": combos,
        })

    w = WitnessBuilder("bond-edge-set-selection", engine="python",
                       start_time=t0)
    w.set_description(
        "Edge-set selection refutation: with the DERIVED per-bond energies "
        "(f_bond = c·z+d; pp 2.907 / pn 3.890 / nn 5.178 MeV), EXACT "
        "enumeration of every static integer edge multiset per nucleus shows "
        "NO static bond graph closes D/T/³He/⁴He jointly — D needs a sub-unit "
        "bond (0.57 of its only pn bond; halo-loose), ⁴He needs MORE than the "
        "complete graph (1.20× over 1pp+4pn+1nn; doubly-magic many-body). The "
        "physical structure is fractional occupancy / shell weighting, not an "
        "edge-set choice — pointing at the per-nucleus volume route (#2078). "
        "T (chain 0.94×) and ³He (~1.1×) are individually close; the JOINT "
        "static closure is what fails. Formalize-first refutation of the "
        "static-graph class; no fit attempted."
    )
    w.add_parameter("E_0_MeV", round(E0, 4))
    w.add_data("per_bond_log", {k: round(v, 4) for k, v in lg.items()})
    w.add_data("per_bond_energy_MeV", {k: round(E0 * v, 4) for k, v in lg.items()})
    w.add_data("rows", [{k: v for k, v in r.items() if k != "all_combos"}
                        for r in rows])
    w.add_data("full_enumeration", {r["atom"]: r["all_combos"] for r in rows})
    w.add_data("verdict", {
        "joint_static_closure": False,
        "D_blocker": "single pn bond overshoots 1.75×; only smaller integer "
                     "option is 0 bonds — needs occupancy ≈ 0.57 (halo).",
        "He4_blocker": "complete graph (1pp+4pn+1nn) under-binds 1.20× — "
                       "needs a positive many-body/doubly-magic term beyond "
                       "all pairwise bonds.",
        "conclusion": "The bond graph is NOT a static integer graph. The "
                      "remaining structure is fractional bond occupancy / "
                      "shell weighting (saturation, Pauli, magic) — i.e. the "
                      "per-nucleus volume / shell route (#2078), not edge "
                      "choice. Refutation recorded so the static-graph "
                      "direction is not re-chased.",
    })
    # Assertions: the two extreme blockers, checked from the enumeration.
    d_row = [r for r in rows if r["A"] == 2][0]
    he4_row = [r for r in rows if r["A"] == 4][0]
    w.add_assertion(
        name="deuteron_not_closable_by_integer_edge_set",
        computed=bool(d_row["closable_within_5pct"]), expected=False,
        tolerance=0.0,
        source="exact enumeration of {0,1}-pn edge sets for D: none within 5%.",
    )
    w.add_assertion(
        name="he4_requires_more_than_complete_graph",
        computed=he4_row["complete_vs_required"], expected=1.2, tolerance=0.05,
        source="L_required/L_complete for ⁴He ≈ 1.20 > 1: even the complete "
               "graph under-binds; pairwise-additive closure impossible.",
    )
    out = w.save()

    print("=" * 88)
    print(" Edge-set selection — EXACT enumeration of static integer bond graphs")
    print(f"   per-bond E [MeV]: pp={E0*lg['pp']:.3f}  pn={E0*lg['pn']:.3f}  "
          f"nn={E0*lg['nn']:.3f}   (derived, fixed)")
    print("=" * 88)
    print(f" {'atom':>7}{'A':>3}{'L_req':>8}{'box(pp,pn,nn)':>15}{'L_complete':>11}"
          f"{'req/compl':>10}{'best set':>16}{'best miss':>10}{'closable':>9}")
    print(" " + "-" * 86)
    for r in rows:
        b = r["best_integer_edge_set"]
        bs = f"({b['pp']},{b['pn']},{b['nn']})"
        eb = r["edge_box"]
        print(f" {r['atom']:>7}{r['A']:>3}{r['L_required']:>8.3f}"
              f"{str((eb['pp'], eb['pn'], eb['nn'])):>15}{r['L_complete_graph']:>11.3f}"
              f"{r['complete_vs_required']:>10.2f}{bs:>16}{b['miss_x']:>9.2f}×"
              f"{str(r['closable_within_5pct']):>9}")
    print(" " + "-" * 86)
    print(" VERDICT: no static integer edge set closes jointly —")
    print("   D: 1 bond overshoots 1.75× (needs occupancy ~0.57, halo-loose);")
    print("   ⁴He: complete graph under-binds 1.20× (needs many-body/magic term).")
    print("   → fractional occupancy / shell weighting (per-nucleus volume, #2078),")
    print("     NOT an edge-set choice. Static-graph direction refuted; recorded.")
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
