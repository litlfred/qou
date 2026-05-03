#!/usr/bin/env python3
"""
Path A — extract T2 + T3 (combined) as residue of tr_M(T_w) at q = 1.

Per `prop:terms-2-6-higher-operations.md`:
    "the level-ℓ = 1 residue is absorbed into Terms 2, 3 as the
     dominant ζ_1 = 1 pole"

So T2 + T3 = Res_{q=1}[tr_M(T_w)] / (q_0 - 1) (combined; the
filtration-level split between T2 and T3 is finer Hochschild work).

This probe extracts that residue at q = 1 directly using sympy's
symbolic Markov trace from `markov_peel.tr_M_atomic`, the same
machinery PR #526 uses for ζ_ℓ ≥ 2 (Term 6).  The resulting
contribution is a Markov-invariant trace by construction — residues
of an invariant function are invariant.

Output: path-a-zeta1-residue-probe.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp
import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from markov_peel import tr_M_atomic                  # noqa: E402
from hecke_symbolic import q as q_sym                 # noqa: E402
from q_parameter import Q as Q0_FLOAT                 # noqa: E402


def extract_zeta1_residue(Z: int, N: int, *, label: str = "") -> dict:
    """Compute Res_{q=1}[tr_M(T_w)] for atom (Z, N)."""
    print(f"\n  === {label or f'(Z={Z}, N={N})'} ===")
    t0 = time.time()
    tr_sym = tr_M_atomic(Z, N)
    t_peel = time.time() - t0

    # Try to put into rational form (numerator/denominator).
    t0 = time.time()
    tr_canonical = sp.cancel(tr_sym)
    t_cancel = time.time() - t0

    # Extract residue at q = 1.  For atomic braids tr_M is regular at q = 1
    # in the Habiro (cyclotomic) sense, but the rational form may have a
    # pole there.  sp.residue handles both cases:
    #   - if regular: returns 0
    #   - if simple pole: returns the standard residue
    #   - if higher-order pole: returns the Laurent coefficient (q-1)^(-1)
    t0 = time.time()
    try:
        res_at_q1 = sp.residue(tr_canonical, q_sym, 1)
        res_at_q1 = sp.cancel(sp.expand(res_at_q1))
    except Exception as exc:
        print(f"    residue extraction failed: {type(exc).__name__}: {exc}")
        res_at_q1 = None
    t_res = time.time() - t0

    # Numerical value at q_0 (for the Mittag-Leffler contribution
    # T2+T3 = Res / (q_0 - 1))
    res_at_q0 = None
    contribution = None
    if res_at_q1 is not None:
        try:
            q0 = sp.Float(str(Q0_FLOAT), 50)
            # Residue might have its own q-dependence (unusual but possible
            # if the form is multi-variable); evaluate at q_0 just in case.
            res_at_q0_val = res_at_q1.subs(q_sym, q0).evalf(30)
            res_at_q0 = complex(res_at_q0_val)
            contribution = res_at_q0 / (Q0_FLOAT - 1)
        except Exception as exc:
            print(f"    numerical eval of residue failed: {type(exc).__name__}: {exc}")

    # Also evaluate tr_canonical at q_0 to confirm it matches markov_peel's value
    tr_at_q0 = None
    try:
        tr_at_q0_val = tr_canonical.subs(q_sym, sp.Float(str(Q0_FLOAT), 50)).evalf(30)
        tr_at_q0 = complex(tr_at_q0_val)
    except Exception:
        pass

    print(f"    peel={t_peel:.1f}s  cancel={t_cancel:.2f}s  residue={t_res:.2f}s")
    print(f"    tr_M(q_0)             = {tr_at_q0}")
    print(f"    Res_{{q=1}}[tr_M]      = {res_at_q1}")
    print(f"    Res_{{q=1}}[tr_M]@q_0  = {res_at_q0}")
    print(f"    T2+T3 = Res / (q_0-1) = {contribution}")

    return {
        "atom": label,
        "Z": Z, "N": N, "A": Z + N,
        "tr_M_at_q0": str(tr_at_q0) if tr_at_q0 is not None else None,
        "residue_at_q1_symbolic": str(res_at_q1) if res_at_q1 is not None else None,
        "residue_at_q1_numerical": str(res_at_q0) if res_at_q0 is not None else None,
        "T2_plus_T3_contribution_at_q0": str(contribution) if contribution is not None else None,
        "elapsed_peel_sec": t_peel,
        "elapsed_residue_sec": t_res,
    }


def main() -> int:
    print("=" * 80)
    print("  Path A — T2 + T3 as residue of tr_M(T_w) at q = 1 (zeta_1)")
    print(f"  q_0 = {Q0_FLOAT}")
    print("=" * 80)
    print("\n  Per terms-2-6-higher-operations.md:")
    print('    "the level-ell=1 residue is absorbed into Terms 2, 3')
    print('     as the dominant zeta_1 = 1 pole"')
    print("  So T2 + T3 (combined) = Res_{q=1}[tr_M(T_w)] / (q_0 - 1).")

    atoms = [
        ("proton",   1, 0),
        ("neutron",  0, 1),
        ("deuteron", 1, 1),
    ]

    rows = []
    for label, Z, N in atoms:
        try:
            row = extract_zeta1_residue(Z, N, label=label)
            rows.append(row)
        except Exception as exc:
            print(f"\n  ERROR on {label}: {type(exc).__name__}: {exc}")
            rows.append({
                "atom": label, "Z": Z, "N": N, "A": Z + N,
                "error": f"{type(exc).__name__}: {exc}",
            })

    # Compare to brane-tower T2+T3 (legacy form) for reference
    print("\n" + "=" * 80)
    print("  Comparison to brane-tower form (paper_six_term_isotope_sweep)")
    print("=" * 80)
    print("    proton brane T2+T3  ~ 1.18e6 Hecke-units (legacy form)")
    print("    deuteron brane T2+T3 ~ 1.61e6 Hecke-units")
    print("  Path A residue form gives a SINGLE complex number per atom;")
    print("  no per-generator amplification.")

    witness = {
        "computation": "path-a-zeta1-residue-probe",
        "description": (
            "Path A from docs/audits/2026-05-03-T2T3-derivation-chain-"
            "analysis.md.  Identifies zeta_1 = 1 explicitly per "
            "terms-2-6-higher-operations.md and extracts T2+T3 "
            "(combined) as Res_{q=1}[tr_M(T_w)] / (q_0 - 1) using "
            "markov_peel + sympy.residue.  The result is Markov-"
            "invariant by construction (residue of an invariant "
            "function).  Filtration-level split into T2 (level 1) "
            "vs T3 (level 2) is finer Hochschild work; this probe "
            "extracts the combined sum."
        ),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "zeta_1_identified_as": "1 (the trivial root of unity)",
        "source_for_zeta_1_definition":
            "content/quantum-observable-universe/braids-and-knots/terms-2-6-higher-operations.md",
        "rows": rows,
    }
    out = HERE / "path-a-zeta1-residue-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
