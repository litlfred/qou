#!/usr/bin/env python3
"""
lever1_bridge_alien_datum_probe.py — the Bridge-equation / alien-derivative datum of the
classical binding period at ω₀ = 1/√2, in closed form + verified (lever-1 / z2bn, W5).

Context. PR #3694 located the dominant level-1/2 Borel singularity of the classical
binding period a_D^(n) = I(n)/n at ξ = ω₀ = 1/√2 (positive axis, non-polar). The
Bridge-equation content at a singularity is its ALIEN DATUM: the local singular model
Δ_{ω₀}B̂ and its Stokes constant. At q = 1 this is fully DERIVABLE (formalize-first)
from the proved involution asymptotics I(n) ~ (n/e)^{n/2} e^{√n−1/4}/√2 via the Laguerre
generating identity Σ_n L_n^{(α)}(−A)uⁿ = (1−u)^{−α−1} e^{Au/(1−u)}:

    B̂(ξ) ~ A_ω·(1−√2·ξ)^{3/2}·exp( 1/(4(1−√2·ξ)) )   near ξ = 1/√2,  with

    ω₀  = 1/√2        (level-1/2 action — the singularity location),
    A₂  = 1/4         (second-level action: the e^{√n} = e^{2√(A₂n)} factor),
    γ   = 3/2         (branch exponent: n^{−3/2} = n^{α/2−1/4}, α = −5/2),
    A_ω = 4√2·e^{−3/8} ≈ 3.8884   (the Stokes constant / alien-derivative amplitude).

The e^{√n} factor means the singularity is exponential-of-pole type — the alien datum
lives on an Écalle ACCELERATION chain (A₂ is the action at the next critical time), not
a simple algebraic branch point. Scope note: the literal Bridge equation
Δ_ω f = A_ω·df/dz is the one-parameter-ODE-transseries form; at q=1 the binding EGF
e^{x+x²/2} is entire (no equational Stokes), so the resurgence here is CO-EQUATIONAL
(coefficient-plane); A_ω above is the co-equational Stokes constant.

Verification (exact I(n) to n = 400, mpmath 600 dps):
  1. coefficient constant  K_c = e^{−1/4}/√(2π): b_n·(√2)^{−n}·e^{−√n}·n^{3/2} → K_c;
  2. second-level action:  ln(b_n·(√2)^{−n}·n^{3/2})/√n → 1  ⇒ A₂ = 1/4;
  3. branch exponent:      ln(b_n·(√2)^{−n}·e^{−√n})/ln n → −3/2  ⇒ γ = 3/2;
  4. Stokes constant:      b_n·(√2)^{−n} / (e^{1/4}·L_n^{(−5/2)}(−1/4)) → A_ω = 4√2·e^{−3/8};
  (each with a + b/√n + c/n three-point extrapolation at n = 100, 200, 400).
  5. q-RIGIDITY (bar-even ⇒ the alien datum is STATIONARY at q = 1): the deformation
     ln(S_q(n₀)/I(n₀)) at q = 1±ε scales like ε² (fitted exponent ≈ 2) and is even in ε
     — the derived, testable version of the external dialog's "A_ω(q) carries (q−1)²"
     claim. (The Φ_m root-of-unity part needs |q| = 1 evaluations — out of real-q scope.)

Anti-fit: every closed form is derived BEFORE measurement from proved asymptotics +
classical Laguerre identities; nothing tuned; no wiring. Binding a_D only (not Q_β c_k).
EXPLORATORY, scope-(a) with derived-exact leading forms.

Audit: docs/audits/2026-07-12-alien-calculus-review-binding-gevrey-half.md (addendum 2)
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
for p in (str(HERE / "substrate"), str(HERE)):
    if p not in sys.path:
        sys.path.insert(0, p)

import mpmath as mp  # noqa: E402
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

mp.mp.dps = 600
NS = (100, 200, 400)


def involution_numbers(nmax):
    I = [1, 1]
    for n in range(2, nmax + 1):
        I.append(I[n - 1] + (n - 1) * I[n - 2])
    return I


def extrap3(vals):
    """fit v(n) = a + b/√n + c/n at the three NS points; return a."""
    A = mp.matrix(3, 3)
    rhs = mp.matrix(3, 1)
    for i, n in enumerate(NS):
        A[i, 0], A[i, 1], A[i, 2] = 1, 1 / mp.sqrt(n), mp.mpf(1) / n
        rhs[i, 0] = vals[i]
    return mp.lu_solve(A, rhs)[0, 0]


def qint(qv, k):
    return (qv ** k - qv ** (-k)) / (qv - 1 / qv)


def S_q(qv, n):
    def parts(n, m):
        if n == 0:
            yield ()
            return
        for k in range(min(n, m), 0, -1):
            for r in parts(n - k, k):
                yield (k,) + r

    def hooks(lam):
        conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
        return [(row - j - 1) + (conj[j] - i - 1) + 1
                for i, row in enumerate(lam) for j in range(row)]

    tot = mp.mpf(0)
    for lam in parts(n, n):
        d = mp.mpf(1)
        for k in range(1, n + 1):
            d *= qint(qv, k)
        for h in hooks(lam):
            d /= qint(qv, h)
        tot += d
    return tot


def main() -> int:
    print("=== lever-1 W5: alien datum at ω₀ = 1/√2 — closed forms verified ===\n")
    I = involution_numbers(NS[-1])
    SQRT2 = mp.sqrt(2)

    b = {}
    for n in NS:
        b[n] = mp.mpf(I[n]) / n / mp.gamma(mp.mpf(n) / 2 + 1)

    # 1. coefficient constant K_c = e^{-1/4}/√(2π)
    Kc_pred = mp.e ** (mp.mpf(-1) / 4) / mp.sqrt(2 * mp.pi)
    Kc_vals = [b[n] * SQRT2 ** (-n) * mp.e ** (-mp.sqrt(n)) * n ** mp.mpf('1.5') for n in NS]
    Kc = extrap3(Kc_vals)
    e1 = abs(Kc / Kc_pred - 1)
    print(f"1. K_c: measured→ {float(Kc):.6f}  predicted e^(-1/4)/√(2π) = "
          f"{float(Kc_pred):.6f}  (rel err {float(e1):.4f})")

    # 2. second-level action A₂ = 1/4 (√n-coefficient → 1)
    a2_vals = [mp.log(b[n] * SQRT2 ** (-n) * n ** mp.mpf('1.5')) / mp.sqrt(n) for n in NS]
    a2 = extrap3(a2_vals)
    e2 = abs(a2 - 1)
    print(f"2. √n-coefficient: measured→ {float(a2):.5f}  predicted 1  "
          f"(⇒ A₂ = coeff²/4 = {float(a2**2/4):.5f} vs 1/4; err {float(e2):.4f})")

    # 3. branch exponent γ = 3/2 (power → −3/2) — constant-cancelling two-point
    # log-slopes (ln v(2n) − ln v(n))/ln 2, Richardson in 1/√n
    v = {n: mp.log(b[n] * SQRT2 ** (-n) * mp.e ** (-mp.sqrt(n))) for n in NS}
    s12 = (v[200] - v[100]) / mp.log(2)
    s23 = (v[400] - v[200]) / mp.log(2)
    # slope(n) = −3/2 + c/√n: eliminate c with the 1/√100, 1/√200 pair
    x1, x2 = 1 / mp.sqrt(100), 1 / mp.sqrt(200)
    gpow = s23 + (s23 - s12) * x2 / (x1 - x2)
    e3 = abs(gpow + mp.mpf('1.5'))
    print(f"3. n-power (two-point log-slope, Richardson): measured→ {float(gpow):.4f}  "
          f"predicted −3/2  (err {float(e3):.4f})")

    # 4. Stokes constant A_ω = 4√2·e^{−3/8} via the exact Laguerre local model
    Aw_pred = 4 * SQRT2 * mp.e ** (mp.mpf(-3) / 8)
    Aw_vals = [b[n] * SQRT2 ** (-n)
               / (mp.e ** (mp.mpf(1) / 4) * mp.laguerre(n, mp.mpf('-2.5'), mp.mpf('-0.25')))
               for n in NS]
    Aw = extrap3(Aw_vals)
    e4 = abs(Aw / Aw_pred - 1)
    print(f"4. Stokes constant A_ω: measured→ {float(Aw):.5f}  predicted 4√2·e^(-3/8) = "
          f"{float(Aw_pred):.5f}  (rel err {float(e4):.4f})")
    print(f"   local model: B̂(ξ) ≈ A_ω·(1−√2ξ)^(3/2)·exp(1/(4(1−√2ξ)))  near ξ = 1/√2")

    # 5. q-rigidity: alien datum stationary at q=1 (deformation even + O(ε²))
    set_compute_dps()
    n0 = 20
    eps_list = [mp.mpf('0.02'), mp.mpf('0.04')]
    I20 = mp.mpf(I[n0])
    deltas = {}
    for eps in eps_list:
        dp = mp.log(S_q(1 + eps, n0) / I20)
        dm = mp.log(S_q(1 / (1 + eps), n0) / I20)   # bar-even ⇒ dm = dp exactly
        deltas[float(eps)] = (dp, dm)
    slope = (mp.log(abs(deltas[0.04][0])) - mp.log(abs(deltas[0.02][0]))) / mp.log(2)
    bar_even_ok = all(abs(dp - dm) / abs(dp) < 1e-12 for dp, dm in deltas.values())
    print(f"5. q-rigidity: Δ(ε)=ln(S_q/I) at n₀={n0}: ε=0.02→{float(deltas[0.02][0]):.3e}, "
          f"ε=0.04→{float(deltas[0.04][0]):.3e}; scaling exponent {float(slope):.3f} (≈2), "
          f"bar-even (q↔1/q exact): {'PASS' if bar_even_ok else 'FAIL'}")
    print("   ⇒ the alien datum is STATIONARY at q=1 to O((q−1)²) — the derived, testable")
    print("     form of the dialog's 'A_ω(q) carries (q−1)²' claim (Φ_m part out of real-q scope).")

    ok = (e1 < 0.02 and e2 < 0.02 and e3 < 0.05 and e4 < 0.02
          and mp.mpf('1.8') < slope < mp.mpf('2.2') and bar_even_ok)
    print(f"\n### Verdict: {'ALL CHECKS PASS' if ok else 'CHECK FAILED'} — alien datum "
          f"(ω₀=1/√2, A₂=1/4, γ=3/2, A_ω=4√2e^(-3/8)) derived + verified; stationary at q=1.")

    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("lever1-bridge-alien-datum", engine="mpmath")
        wb.set_description(
            "Lever-1 (z2bn) W5: the Bridge-equation / alien-derivative datum of the classical "
            "binding period at its level-1/2 Borel singularity, in closed form (derived from "
            "proved involution asymptotics + the Laguerre generating identity BEFORE "
            "measurement): omega0=1/sqrt2, second-level action A2=1/4, branch exponent "
            "gamma=3/2, Stokes constant A_omega=4*sqrt2*e^(-3/8)~3.8884; local model "
            "B(xi) ~ A_omega*(1-sqrt2*xi)^(3/2)*exp(1/(4(1-sqrt2*xi))). Verified against exact "
            "I(n) to n=400 with 3-point extrapolation (all components <2-5%). q-rigidity: the "
            "deformation of the datum is bar-even and O((q-1)^2) (measured exponent ~2) — the "
            "alien datum is stationary at the classical point, the derived form of the external "
            "dialog's '(q-1)^2 in A_omega(q)' claim. Co-equational scope: the q=1 EGF is entire, "
            "so the resurgence is coefficient-plane; the literal ODE Bridge form does not apply "
            "verbatim. No fit; no wiring; binding only. Scope-(a) with derived-exact leading forms.")
        wb.add_data("omega0", float(1 / SQRT2))
        wb.add_data("Kc_measured_vs_pred", [float(Kc), float(Kc_pred)])
        wb.add_data("sqrtn_coeff_measured", float(a2))
        wb.add_data("A2_derived", 0.25)
        wb.add_data("npower_measured", float(gpow))
        wb.add_data("gamma_derived", 1.5)
        wb.add_data("A_omega_measured_vs_pred", [float(Aw), float(Aw_pred)])
        wb.add_data("q_rigidity_scaling_exponent", float(slope))
        wb.add_data("q_rigidity_bar_even_exact", bool(bar_even_ok))
        wb.add_assertion(
            name="alien_datum_closed_form_verified_and_q_stationary",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("K_c err %.4f; sqrt-n coeff err %.4f; n-power err %.4f; A_omega err %.4f; "
                    "q-deformation exponent %.3f (bar-even exact) — datum "
                    "(1/sqrt2, 1/4, 3/2, 4*sqrt2*e^(-3/8)) verified, stationary at q=1."
                    % (float(e1), float(e2), float(e3), float(e4), float(slope))))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness skipped: {e})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
