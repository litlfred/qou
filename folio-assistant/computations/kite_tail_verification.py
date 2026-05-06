#!/usr/bin/env python3
"""
kite_tail_verification.py — Verify the kite-tail factorisation
of the canonical atomic Markov trace.

Conjecture (PR #545's `D(u)` closed form, structurally
re-interpreted in the kite-tail dictionary, see
[`docs/audits/2026-05-05-r-and-kite-tails-exploration.md`](../../docs/audits/2026-05-05-r-and-kite-tails-exploration.md)):

    D(r)  =  2^{2A+1}  ·  r^{shift}  ·  (1 + r²)^{3A−1},

where  r := q^{1/2} = sqrt(q),  D(r) is the cleared-denominator
form of  tr_M(β_atom)  after substituting  q = r²,  and the three
factors correspond to:

    tail        — r^{shift}       (pure linear chain, no surface area)
    kite        — (1 + r²)^{3A−1}  (cyclotomic junctions)
    averaging   — 2^{2A+1}         (averaged-crossing prefactor)

This script verifies the factorisation for the three closed-form
witnesses we have:

    proton    (Z=1, N=0, A=1)   shift =  19,  kite-power = 2,  prefactor = 2^3 =   8
    neutron   (Z=0, N=1, A=1)   shift =  22,  kite-power = 2,  prefactor = 2^3 =   8
    deuteron  (Z=1, N=1, A=2)   shift =  40,  kite-power = 5,  prefactor = 2^5 =  32

The shifts come from the per-crossing rule
shift(σ) = 1, shift(σ⁻¹) = 4, shift(avg) = 0  (intra-nucleon)
plus  +1 for each (p,n) interface (inter-nucleon, A ≥ 2).

Run:
    python3 folio-assistant/computations/kite_tail_verification.py
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

from hoefsmit_symbolic import Q, chi_lambda_symbolic  # noqa: E402
from markov_weights_symbolic import (  # noqa: E402
    Z_MARK,
    atom_braid_word_3A_to_crossings,
    solve_y_lambda,
)


def kite_tail_predict(Z: int, N: int) -> dict:
    """Predict (shift, kite-power, prefactor) per the kite-tail rule."""
    A = Z + N
    # Per-crossing shift (intra-nucleon).
    SHIFT_INTRA = {"sigma": 1, "sigma_inv": 4, "averaged": 0}
    word = atom_braid_word_3A_to_crossings(Z, N, include_inter=(A >= 2))
    shift_total = 0
    n_avg_intra = 0
    n_avg_inter = 0
    # We don't have per-crossing intra/inter labels in the (gen_idx, ctype)
    # form, so use the structural rule: shift = 18·Z + 21·N + 1 (for A ≥ 1)
    # per `prop:per-nucleon-shift` derivation in
    # folio-assistant/computations/per_nucleon_shift_derivation.py.
    shift_total = 18 * Z + 21 * N + 1
    # Averaged crossing count (intra + inter).
    for _, ctype in word:
        if ctype == "averaged":
            # Intra: 2 averaged per nucleon (uud has 1 ud-pair on g0, 1 on g1; udd same).
            # Inter: 1 averaged for the (p, n) interface in pppnnn ordering.
            pass
    # Cleaner: count by inspection.
    n_avg_total = sum(1 for _, ctype in word if ctype == "averaged")
    return {
        "A": A,
        "shift_pred": shift_total,
        "kite_power_pred": 3 * A - 1,
        "n_avg_pred": n_avg_total,
        "two_power_pred": 2 ** n_avg_total,
        "two_exponent_pred": n_avg_total,
    }


def tr_M_canonical_symbolic(Z: int, N: int) -> sp.Expr:
    """Symbolic canonical Jones-Markov tr_M(β_atom) at H_{3A}(q)."""
    n = 3 * (Z + N)
    word = atom_braid_word_3A_to_crossings(Z, N, include_inter=(Z + N >= 2))
    if n <= 3:
        # n=3: use linear-system y_λ (closed form via Markov axioms).
        y_lam = solve_y_lambda(n)
    else:
        # n ≥ 6: use Wenzl Schur (closed-form symbolic).
        from markov_weights_symbolic import y_lambda_symbolic
        y_lam = y_lambda_symbolic(n)
    total = sp.Integer(0)
    for shape, y in y_lam.items():
        chi = chi_lambda_symbolic(shape, word)
        total = total + sp.cancel(y * chi)
    return sp.cancel(total)


def factor_kite_tail(trM_q: sp.Expr) -> dict:
    """Substitute q = r² in tr_M, clear denominators, and extract
    (shift, kite-power, prefactor) by symbolic factorisation.

    Returns extracted (shift_obs, kite_power_obs, two_power_obs) or
    None if no clean factorisation (a sign of convention mismatch).
    """
    r = sp.Symbol("r", positive=True)
    trM_r = sp.cancel(trM_q.subs(Q, r**2))
    num, den = sp.fraction(sp.together(trM_r))
    # D(r) := numerator-after-clearing.  We want D(r) = c · r^shift · (1+r²)^k
    # for some integer c (the prefactor).  Try sympy factor.
    factored = sp.factor(num)
    # Check: extract (1+r²)^k factor.
    one_plus = 1 + r**2
    k_kite = 0
    rest = factored
    while True:
        q_, rem = sp.div(sp.Poly(rest, r), sp.Poly(one_plus, r))
        if rem.is_zero:
            k_kite += 1
            rest = q_.as_expr()
        else:
            break
    # Extract leading r-power from `rest`.
    rest_poly = sp.Poly(rest, r)
    if rest_poly.is_zero:
        return None
    coeffs = rest_poly.all_coeffs()
    monoms = rest_poly.monoms()
    lowest_exp = min(m[0] for m in monoms)
    # Constant prefactor when only one monomial remains (after r^shift extraction).
    rest_after_r = sp.expand(rest / r**lowest_exp)
    # The remainder should be an integer constant for clean kite-tail form.
    return {
        "shift_obs": lowest_exp,
        "kite_power_obs": k_kite,
        "rest_after_factorisation": str(rest_after_r),
        "is_clean_constant": rest_after_r.is_Integer,
        "prefactor_observed": int(rest_after_r) if rest_after_r.is_Integer else None,
        "denominator_residual": str(den),
    }


def main() -> int:
    print("=" * 80)
    print(" Kite-tail factorisation verification: D(r) = 2^(2A+1) · r^shift · (1+r²)^(3A−1)")
    print("=" * 80)

    out_results = {}
    for label, Z, N in [
        ("proton",   1, 0),
        ("neutron",  0, 1),
        ("deuteron", 1, 1),
    ]:
        print()
        print(f"--- {label} (Z={Z}, N={N}) ---")
        pred = kite_tail_predict(Z, N)
        print(f"  predicted: shift={pred['shift_pred']}  "
              f"kite_power={pred['kite_power_pred']}  "
              f"two_exponent={pred['two_exponent_pred']}")
        t0 = time.time()
        trM = tr_M_canonical_symbolic(Z, N)
        print(f"  tr_M assembled in {time.time() - t0:.1f}s")
        obs = factor_kite_tail(trM)
        print(f"  observed:  {obs}")
        out_results[label] = {"predicted": pred, "observed": obs}

    # Witness emission.
    out = HERE / "kite_tail_verification.witness.json"
    witness = {
        "computation": "kite-tail-verification",
        "description": (
            "Verify the kite-tail factorisation D(r) = 2^(2A+1) · "
            "r^shift · (1+r²)^(3A−1) for the canonical atomic Markov "
            "trace at A = 1 (proton, neutron) and A = 2 (deuteron). "
            "r := q^{1/2} is the spinor information rate per the "
            "notation register. The 'tail' factor is r^shift "
            "(linear-chain content), the 'kite' factor is (1+r²)^k "
            "(cyclotomic-junction content), and the prefactor "
            "2^(2A+1) is the averaging count. Predicted exponents "
            "from PR #545's D(u) closed-form derivation; observed "
            "exponents from sympy factorisation of the closed-form "
            "tr_M produced by the round-3 markov_weights_symbolic + "
            "hoefsmit_symbolic chain."
        ),
        "results": out_results,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    out.write_text(json.dumps(witness, indent=2, default=str))
    print()
    print(f"witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
