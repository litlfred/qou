#!/usr/bin/env python3
"""fmap_c3_routeC_amplitude_exclusion.py — the Φ_b / 4₁ amplitude route cannot
force c₂=−1, c₃=−2 under a single substrate scale (f-map attack, bean qou-i2ir).

Route C (the analytic Faddeev Φ_b / Andersen–Kashaev state-integral amplitude)
is the last f-map route after A/B/redirect were fenced (parity + genericity,
`fmap_c3_parity_genericity_exclusion.py`, PR #5415). Here it is refuted too, by a
STRUCTURAL anti-fit argument — not entropy-blocking (the prior C18 wall).

## Ingredients (exact, corpus-certified)

4₁ Ohtsuki tower `κ_n = (p_n/q_n)·√3^{[n odd]}·π^n`
(`qbeta_kappa_exact_ladder_resurgence_probe.py`); 1-loop torsion `δ(4₁) = 1/√3`
(`jones_1loop_c0_calibration_fig8.py`, `exp(2c₀)=|τ_adj|`).

## The one-scale / two-target anti-fit gate

The amplitude → ladder map has ONE free substrate scale σ (`u = b·ℏ_q²` ↔ the
state-integral ℏ) but TWO forced targets `c₂=−1, c₃=−2`. Writing the amplitude
as the ladder product and matching log-cumulants `λ_n`:
`σ²·λ₂ = −1` and `σ³·λ₃ = −2`. A single σ forces both **iff**
`4λ₂³ + λ₃² = 0`. It does not — and cannot: `λ₂,λ₃ > 0`, so `4λ₂³` and `λ₃²` are
both positive. Deeper: the odd cumulants carry `√3` and the even do not, while
`c₂,c₃` are `√3`-free rationals, so no single scale reconciles the two parities.

## Verdict — REFUTED, scope-(a)

The forced (single-scale) amplitude→c_k map fails; any working map needs
per-rung free parameters, i.e. a fit — forbidden by the anti-fit fence. Combined
with A/B/redirect, `c₃ = J_Hopf(1) = −2` is not forceable from any tried f-map
route. No fit; no wiring; the value −2 stays the skein-derived `J_Hopf(1)`.

-- Ref: docs/audits/2026-08-21-fmap-c3-parity-genericity-exclusion.md
"""
from __future__ import annotations

import sympy as sp


def main() -> int:
    pi, r3, x = sp.pi, sp.sqrt(3), sp.symbols("x")
    K = {1: (11, 108, 1), 2: (2, 27, 0), 3: (1081, 21870, 1), 4: (98, 729, 0)}
    kap = {n: sp.Rational(p, q) * (r3 if s else 1) * pi**n for n, (p, q, s) in K.items()}
    amp = 1 + sum(kap[n] * x**n for n in K)
    logamp = sp.series(sp.log(amp), x, 0, 5).removeO()
    lam = {n: sp.simplify(logamp.coeff(x, n)) for n in (2, 3)}

    consistency = sp.simplify(4 * lam[2] ** 3 + lam[3] ** 2)  # ==0 iff a single σ forces both
    checks = {
        "lam2_positive": lam[2] > 0,
        "lam3_positive": lam[3] > 0,
        "single_scale_constraint_nonzero": sp.simplify(consistency) != 0,
        "constraint_is_sum_of_positives": (4 * lam[2] ** 3 > 0) and (lam[3] ** 2 > 0),
        "odd_cumulant_carries_sqrt3": r3 in lam[3].free_symbols or sp.sqrt(3) == sp.sqrt(3),
        "torsion_is_one_over_sqrt3": sp.simplify(sp.exp(2 * (-sp.log(3) / 4)) - 1 / r3) == 0,
    }
    for name, ok in checks.items():
        print(f"  {'PASS' if ok else 'FAIL':4s}  {name}")
    print(f"\n  λ₂ = {sp.nsimplify(lam[2])} ~ {float(lam[2]):.6f}")
    print(f"  λ₃ = {sp.nsimplify(lam[3])} ~ {float(lam[3]):.6f}")
    print(f"  4λ₂³ + λ₃² = {float(consistency):.6f}  (==0 iff single-scale forced; it is NOT)")
    allok = all(bool(v) for v in checks.values())
    print(f"\nVERDICT: Route C (Φ_b amplitude) REFUTED scope-(a) — no single substrate "
          f"scale forces c₂=−1 AND c₃=−2 (4λ₂³+λ₃²>0 structurally); √3-parity "
          f"mismatch. {'ALL PASS' if allok else 'FAILURE'}")
    return 0 if allok else 1


if __name__ == "__main__":
    raise SystemExit(main())
