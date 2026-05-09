#!/usr/bin/env python3
"""
deuteron_tr_M_symbolic.py — Closed-form symbolic Markov trace of the
internal A=2 (deuteron) braid in the Iwahori–Hecke algebra H_6(q).

Continues the proton/neutron closed-form work in
[`hoefsmit_symbolic.py`](hoefsmit_symbolic.py) and the audit doc
[`docs/audits/2026-05-05-symbolic-hoefsmit-fix-proton-tr-m.md`](../../docs/audits/2026-05-05-symbolic-hoefsmit-fix-proton-tr-m.md).

The deuteron internal braid (no inter-nucleon crossings) is a
22-crossing word in B_6, derived from `proton_cross` ⊕ `neutron_cross`
via `atomic_braid_to_crossings(1, 1, include_inter=False)`.

The tr_M closed form is computed as
    tr_M(β) = Σ_{λ ⊢ 6} w_λ · χ^λ(β) / f^λ
with w_λ = dim_q(λ)² / [6]_q! and f^λ = #SYT(λ).

All 11 partitions of 6 contribute; per-partition χ^λ takes 0.1–22.5 s
on this machine (total ~80 s including the partition sum).

Result (PR #547 derivation):
  numerator     : palindromic degree-68 polynomial (35 nonzero terms)
  denominator   : 11520·q^19·(1 + 5q^2 + 14q^4 + 29q^6 + 49q^8 + 71q^10
                                  + 90q^12 + 101q^14 + 101q^16 + 90q^18
                                  + 71q^20 + 49q^22 + 29q^24 + 14q^26
                                  + 5q^28 + q^30)
  pole at q=0   : 19   (matches dp_pole_probe upper bound)
  leading coef  : +1/128 = +1/2^7   (POSITIVE — opposite sign from
                                     proton/neutron −1/8 = −1/2^3)
  value at q_0  : ≈ 0.32110

The change of sign and the larger pole order (19 vs 10/8) refute the
naive "universal −1/(2 n!)" conjecture from the round-1 audit.  The
leading coefficient is still a power of 2 (1/2^7 here, 1/2^3 there),
suggesting a refined conjecture in terms of $\\dim_q$ specializations.

Run:  python3 folio-assistant/computations/deuteron_tr_M_symbolic.py
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from hoefsmit_symbolic import (  # noqa: E402
    Q,
    chi_lambda_symbolic,
    dim_q,
    pole_order_at_zero,
    q_fac,
    tr_M_symbolic,
)
from hecke_characters import partitions_of, standard_young_tableaux  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings as atomic_braid_to_crossings  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402  — single source of truth

# Canonical 50-dps q_0 (full precision; matches y-lambda-mpfr-witness.json
# and other round-3 scripts). Defined at module level to avoid duplicated
# magic values across functions.
Q0_CANONICAL = sp.Float(Q_50_DIGIT_STR, 50)


def main() -> int:
    deut = atomic_braid_to_crossings(1, 1, include_inter=False)
    print(f"deuteron internal braid: {len(deut)} crossings (n=6)")

    # Per-partition timing for transparency.
    parts = []
    for shape in partitions_of(6):
        syts, _, _ = standard_young_tableaux(list(shape))
        parts.append((len(syts), tuple(shape)))
    parts.sort()

    chi_per_lam: dict = {}
    print()
    print("per-partition χ^λ timings:")
    for f, shape in parts:
        t0 = time.time()
        chi = chi_lambda_symbolic(shape, deut)
        dt = time.time() - t0
        chi_q0 = float(sp.N(chi.subs(Q, Q0_CANONICAL), 30))
        chi_per_lam[shape] = {
            "f_lambda": f,
            "chi_at_q0": chi_q0,
            "compute_seconds": round(dt, 2),
        }
        print(f"  {str(shape):<22} f={f:>2}  {dt:6.1f}s  χ(q0)={chi_q0:+.4f}")

    print()
    print("computing partition sum...")
    t0 = time.time()
    trM = tr_M_symbolic(deut, 6)
    dt_total = time.time() - t0
    print(f"  tr_M assembled in {dt_total:.1f}s")
    pole, leading = pole_order_at_zero(trM)
    val_q0 = float(sp.N(trM.subs(Q, Q0_CANONICAL), 30))
    print()
    print(f"pole order at q=0   : {pole}")
    print(f"leading coefficient : {leading}")
    print(f"value at q_0        : {val_q0}")

    # Write witness JSON.
    out = HERE / "deuteron_tr_M_symbolic.witness.json"
    witness = {
        "computation": "deuteron-tr_M-symbolic",
        "description": (
            "Closed-form symbolic Markov trace of the internal A=2 "
            "(deuteron) braid in H_6(q), via "
            "tr_M = Σ_λ w_λ · χ^λ / f^λ with w_λ = dim_q(λ)² / [6]_q!. "
            "Per-irrep χ^λ delegates to "
            "hecke_character_symbolic.q_character_on_braid_word; "
            "no LP/SDP solve required (this is a partition sum, "
            "not an operator-selection program)."
        ),
        "atom": {"Z": 1, "N": 1, "A": 2, "include_inter": False},
        "n_strands": 6,
        "n_crossings": len(deut),
        "n_partitions": len(parts),
        "tr_M_numerator": str(sp.numer(trM)),
        "tr_M_denominator": str(sp.denom(trM)),
        "pole_order_at_q0": int(pole),
        "leading_coefficient": str(leading),
        "value_at_q0": val_q0,
        "per_partition": {str(k): v for k, v in chi_per_lam.items()},
        "total_compute_seconds": round(dt_total, 2),
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    out.write_text(json.dumps(witness, indent=2))
    print()
    print(f"witness written: {out.relative_to(HERE.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
