#!/usr/bin/env python3
"""
Signed-integer crossing-assignment feasibility probe (EXPLORATORY).

Tests the ILP-with-chirality hypothesis for nuclear binding: in the
canonical atom braid the inter-nucleon bonds are integer crossings of
the COMPLETE graph (n_pp = C(Z,2), n_pn = Z·N, n_nn = C(N,2)), each with
the derived per-bond kernel f_bond. The corpus uses all crossings with
chirality +1 (which OVERSHOOTS). This probe asks the sharper question
the "ILP not LP" framing raises:

    Can ANY signed-integer chirality assignment s_i ∈ {+1, -1} (or
    {+1, 0, -1} allowing absence) to the canonical-graph crossings make

        B(K) = E_0 · Σ_crossings s_i · log(1/f_{type(i)})

    match the AME binding within ±5%?

If the best signed assignment still misses, the whole crossing-counting
family — continuous LP (fractional + circular), non-negative integer
enumeration, AND signed integer (this) — is closed, and the obstruction
is a genuinely FRACTIONAL effective coupling (knot-geometry-dependent
bond strength), not an edge/sign choice.

Exact arithmetic (mpmath); ZERO free parameters beyond the ± signs we
exhaustively enumerate. AME used only for the final comparison.

Kernel + E_0 + AME provenance: derived_bond_graph_binding.py,
prearchimedean_bond_factor.py, ame-2020-binding-energies.witness.json.

Output: signed-crossing-feasibility.witness.json
"""
from __future__ import annotations

import itertools
import json
from math import comb
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50
HERE = Path(__file__).resolve().parent

# ── Substrate constants (q0, m_e → E_0; derived f_bond) ──────────────
Q0 = mp.mpf("1.1099785955573347198997632204832250266562084087802")
M_E_MEV = mp.mpf("0.51099895069")          # CAL-1
E0 = M_E_MEV / (Q0 * (Q0 - 1))             # ≈ 4.186 MeV (calibration-fixed)

h = Q0 - 1 / Q0
z = mp.sqrt(Q0) / (Q0 + 1)                 # Markov parameter z = √q/(q+1)
delta = mp.mpf("0.00137705")               # color split

# Derived per-bond kernels (fibre-level, no fit) — see prearchimedean_bond_factor.py
f_pp = z
f_nn = z - h
f_pn = z - h * (mp.mpf(1) / 2 - delta / 4)

# Per-bond contribution in log units L = log(1/f); E_0·L = bond energy [MeV]
L = {"pp": mp.log(1 / f_pp), "pn": mp.log(1 / f_pn), "nn": mp.log(1 / f_nn)}

# ── AME 2020 binding targets [MeV] ───────────────────────────────────
AME = {
    "D":   mp.mpf("2.224566"),
    "T":   mp.mpf("8.481798"),
    "3He": mp.mpf("7.718043"),
    "4He": mp.mpf("28.295673"),
}
ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}


def canonical_graph(Z, N):
    """Complete-graph crossing counts per bond type (the canonical braid)."""
    return {"pp": comb(Z, 2), "pn": Z * N, "nn": comb(N, 2)}


def best_signed_assignment(target_over_E0, counts, allow_absence):
    """Exhaustively enumerate sign (or sign/absence) assignments to each
    canonical-graph crossing; return the best achievable Σ s_i L_type and
    its |miss| vs target (both in log units, i.e. B/E_0)."""
    # Build the multiset of per-crossing log-values.
    logs = []
    for t, n in counts.items():
        logs.extend([L[t]] * n)
    states = [mp.mpf(1), mp.mpf(-1)] + ([mp.mpf(0)] if allow_absence else [])
    best = None
    for signs in itertools.product(states, repeat=len(logs)):
        val = sum(s * lg for s, lg in zip(signs, logs))
        miss = abs(val - target_over_E0)
        if best is None or miss < best[0]:
            best = (miss, val, signs)
    return best


def main() -> int:
    print("=" * 72)
    print("  Signed-integer crossing-assignment feasibility (ILP-with-chirality)")
    print(f"  E_0 = {mp.nstr(E0, 8)} MeV   f_pp={mp.nstr(f_pp,6)} f_pn={mp.nstr(f_pn,6)} f_nn={mp.nstr(f_nn,6)}")
    print(f"  L_pp={mp.nstr(L['pp'],6)}  L_pn={mp.nstr(L['pn'],6)}  L_nn={mp.nstr(L['nn'],6)}")
    print("=" * 72)
    print(f"\n  {'atom':>5} {'graph(pp,pn,nn)':>16} {'B/E0':>9} "
          f"{'pureChir B':>12} {'miss%':>7} {'≤5%':>6} {'+absMiss%':>9} {'≤5%':>7}")

    rows = []
    n_close_pure = 0       # closes under pure chirality (signs only, fixed graph)
    n_close_absence = 0    # closes once edge-absence (selection) is also allowed
    for atom, (Z, N) in ZN.items():
        counts = canonical_graph(Z, N)
        target = AME[atom] / E0
        miss, val, signs = best_signed_assignment(target, counts, allow_absence=False)
        miss_abs, val_abs, signs_abs = best_signed_assignment(target, counts, allow_absence=True)
        B_pred = val * E0
        B_pred_abs = val_abs * E0
        rel = abs(B_pred - AME[atom]) / AME[atom] * 100
        rel_abs = abs(B_pred_abs - AME[atom]) / AME[atom] * 100
        closes_pure = rel <= 5
        closes_absence = rel_abs <= 5
        n_close_pure += int(closes_pure)
        n_close_absence += int(closes_absence)
        print(f"  {atom:>5} {str((counts['pp'],counts['pn'],counts['nn'])):>16} "
              f"{mp.nstr(target,5):>9} {mp.nstr(B_pred,7):>12} {mp.nstr(rel,4):>7}% "
              f"{str(closes_pure):>6} {mp.nstr(rel_abs,4):>9}% {str(closes_absence):>7}")
        rows.append({
            "atom": atom, "Z": Z, "N": N,
            "graph": counts,
            "B_AME_MeV": str(AME[atom]),
            "target_over_E0": str(target),
            "best_signed_B_MeV": str(B_pred),
            "best_signed_miss_pct": str(rel),
            "closes_within_5pct_pure_chirality": bool(closes_pure),
            "best_signed_with_absence_B_MeV": str(B_pred_abs),
            "best_signed_with_absence_miss_pct": str(rel_abs),
            "closes_within_5pct_with_absence": bool(closes_absence),
            "best_signs": [int(s) for s in signs],
        })

    print("\n" + "=" * 72)
    print(f"  Pure chirality (signs only, canonical graph fixed): "
          f"{n_close_pure}/4 close within ±5%.")
    print(f"  + edge absence (re-adds edge SELECTION = the fitting freedom): "
          f"{n_close_absence}/4 close.")
    if n_close_pure == 0:
        print("  ✗ NO nucleus closes under pure chirality. Sign assignment alone")
        print("    cannot reproduce binding — and the only nuclei reachable at all")
        print("    require edge SELECTION (absence), the very fitting freedom the")
        print("    construction must avoid. The crossing-counting family is closed;")
        print("    the obstruction is a FRACTIONAL effective coupling.")
    else:
        print(f"  ⚠ {n_close_pure}/4 close under pure chirality — inspect those cases.")
    # Deuteron is the analytic crux: only pn bonds, target/L_pn not integer
    d_ratio = (AME["D"] / E0) / L["pn"]
    print(f"\n  Deuteron crux: (B_D/E_0)/L_pn = {mp.nstr(d_ratio, 6)}  "
          f"(needs {mp.nstr(d_ratio,4)} pn bonds — fractional, no signed integer matches)")
    print("=" * 72)

    w = {
        "computation": "signed-crossing-feasibility",
        "kind": "exploratory-probe",
        "content_block": "conj:brane-tower-z-habiro / step-9 binding",
        "engine": "mpmath-exact",
        "hypothesis": "ILP-with-chirality: signed integer crossing assignment of the canonical complete-graph bonds",
        "constants": {
            "q0": str(Q0), "E0_MeV": str(E0),
            "f_pp": str(f_pp), "f_pn": str(f_pn), "f_nn": str(f_nn),
            "L_pp": str(L["pp"]), "L_pn": str(L["pn"]), "L_nn": str(L["nn"]),
        },
        "result": {
            "n_close_pure_chirality_of_4": n_close_pure,
            "n_close_with_edge_absence_of_4": n_close_absence,
            "deuteron_pn_bond_count_needed": str(d_ratio),
            "verdict": ("signed-ILP-pure-chirality-refuted"
                        if n_close_pure == 0
                        else "signed-ILP-pure-chirality-partial"),
            "note": ("pure chirality (signs only, canonical graph fixed) closes "
                     f"{n_close_pure}/4; adding edge absence (= edge selection, the "
                     f"fitting freedom) closes {n_close_absence}/4 — only 3He, via "
                     "selection not signs. Deuteron needs 0.572 pn bonds (fractional)."),
        },
        "atoms": rows,
        "_provenance": {
            "kernel": "f_pp=z, f_nn=z-h, f_pn=z-h(1/2-delta/4), z=sqrt(q)/(q+1)",
            "E0": "m_e/(q0(q0-1))",
            "binding_form": "B = E0 * sum_crossings sign * log(1/f_bond)",
            "graph": "canonical complete graph: n_pp=C(Z,2), n_pn=Z*N, n_nn=C(N,2)",
            "refs": ["derived_bond_graph_binding.py", "prearchimedean_bond_factor.py",
                     "ame-2020-binding-energies.witness.json"],
        },
    }
    out = HERE.parent / "signed-crossing-feasibility.witness.json"
    out.write_text(json.dumps(w, indent=2))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
