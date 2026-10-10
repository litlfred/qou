#!/usr/bin/env python3
"""
Schur-Weyl global sum witness with Murnaghan–Nakayama characters.

Per prop:schur-weyl-mass-decomposition + Murnaghan–Nakayama:

    tr_M(𝒜, q) = Σ_{λ ⊢ 3A} w_λ(q) · χ^λ(π(𝒜))

with
    w_λ(q)        = s_λ(q, q⁻¹) / H_q(λ)                   [symbolic]
    χ^λ(π(𝒜))     = classical S_{3A} character on the braid  [integer]

This script plugs real atomic-braid cycle types into the global
Wedderburn sum and evaluates the exact symbolic trace at q_0.

Compared to schur_weyl_symbolic.py's trivial-character output, this
uses the Murnaghan-Nakayama character of the permutation underlying
the atomic braid.  The q=1 classical character is an approximation
to the full Hecke-algebra character χ^λ_q(T_w); the q-deformation
(ribbon q-weights) is the next iteration.

Atoms: p, n, D, T, ³He, ⁴He (where A ≤ 4, manageable symbolic output)

Witness: schur-weyl-mn.witness.json
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
from sympy import Rational, Symbol, Integer

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as _Q_CANONICAL
from schur_weyl_symbolic import (
    global_wedderburn_sum_symbolic,
    h3_additive_approximation_symbolic,
    partitions_of,
)
from murnaghan_nakayama import (
    character_on_atomic_braid,
    atomic_braid_word,
    permutation_from_braid_word,
    cycle_type_of_permutation,
)


def witness_atom(Z, N, include_inter=True):
    """Compute the MN-character Schur-Weyl sum for atom (Z, N)."""
    A = Z + N
    q = sp.Symbol('q', positive=True, real=True)
    q0 = Rational(int(_Q_CANONICAL * 10 ** 16), 10 ** 16)

    # Derive permutation + cycle type
    word = atomic_braid_word(Z, N, include_inter)
    perm = permutation_from_braid_word(word, 3 * A)
    cyc = cycle_type_of_permutation(perm)

    # Global MN-character sum (symbolic in q)
    total_mn, terms_mn = global_wedderburn_sum_symbolic(
        A, q, char_kind="mn-atom", Z=Z, N=N, include_inter=include_inter,
    )
    # Trivial-character baseline (for comparison)
    total_triv, _ = global_wedderburn_sum_symbolic(
        A, q, char_kind="trivial",
    )

    # Numerical evaluation at q_0
    total_mn_q0 = float(total_mn.subs(q, q0).evalf(30))
    total_mn_q0_polynomial_q = expose_polynomial(total_mn, q)
    total_triv_q0 = float(total_triv.subs(q, q0).evalf(30))
    total_triv_q0_polynomial_q = expose_polynomial(total_triv, q)

    # Top contributing partitions by |w_λ · χ^λ| at q_0
    contribs = []
    for t in terms_mn:
        val = float(t["contribution"].subs(q, q0).evalf(30))
        val_polynomial_q = expose_polynomial(t["contribution"], q)
        contribs.append({
            "partition": t["partition"],
            "weight_at_q0": float(t["weight"].subs(q, q0).evalf(30)),
            "weight_at_q0_polynomial_q": expose_polynomial(t["weight"], q),
            "character": int(t["character"]),
            "contribution_at_q0": val,
        })
    contribs.sort(key=lambda c: -abs(c["contribution_at_q0"]))

    return {
        "Z": Z, "N": N, "A": A,
        "braid_word_length": len(word),
        "cycle_type": cyc,
        "n_partitions_total": len(partitions_of(3 * A)),
        "n_partitions_nonzero_chi": len(terms_mn),
        "total_mn_symbolic": str(sp.simplify(total_mn)),
        "total_mn_at_q0": total_mn_q0,
        "total_trivial_at_q0": total_triv_q0,
        "mn_vs_trivial_ratio": (total_mn_q0 / total_triv_q0
                                 if total_triv_q0 else None),
        "top_contributions": contribs[:8],
    }


if __name__ == "__main__":
    print("SCHUR–WEYL with Murnaghan–Nakayama characters")
    print("=" * 80)

    ATOMS = [
        ("p",   1, 0),
        ("n",   0, 1),
        ("D",   1, 1),
        ("T",   1, 2),
        ("3He", 2, 1),
        ("4He", 2, 2),
    ]

    results = {}
    for label, Z, N in ATOMS:
        print(f"\n── {label} (Z={Z}, N={N}, A={Z+N}) ──")
        r = witness_atom(Z, N, include_inter=(Z + N > 1))
        print(f"  braid word length: {r['braid_word_length']}")
        print(f"  cycle type:        {r['cycle_type']}")
        print(f"  partitions (total / with nonzero χ^λ): "
              f"{r['n_partitions_total']} / {r['n_partitions_nonzero_chi']}")
        print(f"  Σ_λ w_λ · χ^λ @ q_0 (MN)       = {r['total_mn_at_q0']:+.6e}")
        print(f"  Σ_λ w_λ        @ q_0 (trivial) = "
              f"{r['total_trivial_at_q0']:+.6e}")
        if r['mn_vs_trivial_ratio'] is not None:
            print(f"  ratio MN/trivial:              = "
                  f"{r['mn_vs_trivial_ratio']:+.6e}")
        print(f"  top partitions:")
        for t in r['top_contributions']:
            print(f"    λ={t['partition']!s:<26} "
                  f"w_λ={t['weight_at_q0']:+.4e} "
                  f"χ^λ={t['character']:+3d} "
                  f"contrib={t['contribution_at_q0']:+.4e}")
        results[label] = r

    # Free-nucleon calibration + binding prediction for light atoms
    print("\nBINDING PREDICTIONS (β-decay calibration)")
    print("-" * 72)
    p_free = results["p"]["total_mn_at_q0"]
    n_free = results["n"]["total_mn_at_q0"]
    Q_cat = n_free - p_free
    from experimental_constants import Q_NEUTRON_MEV
    E_0 = float(Q_NEUTRON_MEV) / abs(Q_cat) if abs(Q_cat) > 0 else 0.0
    print(f"  |tr_M(p)| @ q_0  = {p_free:+.6e}")
    print(f"  |tr_M(n)| @ q_0  = {n_free:+.6e}")
    print(f"  Q_cat            = {Q_cat:+.6e}")
    print(f"  E_0 = Q_β(n) / Q_cat = {E_0:.6e} MeV/cat.unit "
          f"(Q_β = {float(Q_NEUTRON_MEV):.8f} MeV)\n")

    print(f"  {'Atom':>5} {'A':>3} "
          f"{'|tr_M(free)|':>15} {'|tr_M(atom)|':>15} "
          f"{'B_pred (MeV)':>14} {'B_AME':>8}  |Δm/m|%")
    print("  " + "-" * 84)
    # Free-nucleon baselines (no inter-nucleon crossings)
    free_traces = {}
    for label, Z, N in [("p", 1, 0), ("n", 0, 1)]:
        free_traces[label] = abs(results[label]["total_mn_at_q0"])
    B_AME_MeV = {"D": 2.22, "T": 8.48, "3He": 7.72, "4He": 28.30}
    for label in ["D", "T", "3He", "4He"]:
        Z, N = {"D": (1, 1), "T": (1, 2), "3He": (2, 1),
                "4He": (2, 2)}[label]
        A = Z + N
        # Free = |tr(p)|^Z · |tr(n)|^N
        free = (free_traces["p"] ** Z) * (free_traces["n"] ** N)
        atom = abs(results[label]["total_mn_at_q0"])
        B_cat = free - atom
        B_MeV = E_0 * abs(B_cat)
        M_total = A * 938.272
        dm = abs(B_MeV - B_AME_MeV[label]) / M_total * 100
        print(f"  {label:>5} {A:>3} {free:>15.4e} {atom:>15.4e} "
              f"{B_MeV:>14.4f} {B_AME_MeV[label]:>8.2f}  {dm:>7.4f}%")

    # Witness
    witness = {
        "computation": "schur-weyl-mn",
        "description": (
            "Schur-Weyl global mass trace with classical Murnaghan-Nakayama "
            "Specht characters on the S_{3A}-projection of the atomic braid. "
            "This plugs in real atomic-braid cycle types, replacing the "
            "trivial χ^λ = 1 of schur_weyl_symbolic.py. q is kept symbolic; "
            "final evaluation at q_0 uses sympy.evalf(30)."
        ),
        "reference_blocks": [
            "prop:schur-weyl-mass-decomposition",
            "prop:full-pole-structure-mass-trace",
        ],
        "method_notes": [
            "Classical χ^λ (q=1 limit of Hecke character χ^λ_q).",
            "S_{3A} permutation obtained by projecting braid word "
            "(sign-ignoring, since σ^±1 → same transposition).",
            "Full q-deformed Hecke character requires ribbon q-weights "
            "(next iteration).",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": str(float(_Q_CANONICAL)),
            "evalf_dps": 30,
            "engine": "sympy + custom Murnaghan-Nakayama",
        },
        "results_by_atom": results,
    }
    out = Path(__file__).parent / "schur-weyl-mn.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
