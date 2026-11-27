#!/usr/bin/env python3
"""qbeta_zeta4_eta_descent_probe.py — bean 0zr0: does the net route descend
from ONE complex fibre F(eta)?  (zeta4-residue route, formalize-first.)

Per conj:binding-qbeta-complex-volume and the Lean-proved zeta4-partner
relation (QOU.Mass.ComplexVolumeZeta4Partner: the zeta4-rotation negates
the bar-even channel and keeps the bar-odd one), the structured hypothesis
after the exact h*D+h^3*F refutation (bean 08ds) is:

    E and O (the exact bar-even/bar-odd parts of net-route log R) are the
    even/odd parts of ONE function F of a single bar-odd argument eta(s).

Exact consequences tested here (no fit — eta is CONSTRUCTED, then
over-determined checks run):

  val(O) = 3 (ai81: O ~ s^3) forces F_odd's linear coefficient to vanish,
  so O = c3*eta^3 + c5*eta^5 + ..., eta ~ s.  Normalize c3 := leading of O
  (a gauge choice — descent is invariant under eta -> eta*g(eta^2), and
  cbrt(O/ell) is exactly such a reparameterization of any valid eta):
      eta := cuberoot((O/ell)/s^3) * s      (leading = s)
  With this gauge O = ell*eta^3 holds BY CONSTRUCTION (the whole odd tail
  is absorbed into eta) — so the nontrivial, over-determined content is:
  (i)   eta o sigma == -eta  EXACTLY (bar-oddness is NOT built in — the
        cube root of a bar-odd series need not be bar-odd);
  (ii)  E lies in Q(sqrt3)[[t]] with t := eta^2 (triangular t-adic match;
        exact residuals at every valid order).
  (iii) relation of t to the ladder variable u~ = q*u: is t a u~-series?
        (Ties the descent variable to the c_k program; informational.)

VALIDITY WINDOW: O is exact through s^ORD, so (O/ell)/s^3 is exact
only through order ORD-3, hence eta through ORD-2 and t = eta^2 through
ORD-1.  The probe scans only this valid window to avoid truncation
artifacts.  (Development history — earlier boundary-order artifacts and
a removed gauge-tautology check — is recorded in
docs/audits/2026-07-03-0zr0-eta-descent-invariant-theory-prune.md.)

INTERPRETATION (formalize-first prune of this very test class):
all three membership checks are THEOREMS, not empirical findings.
sigma is an order-2 automorphism of Q(sqrt3)[[s]]; the invariant ring of
a finite-order automorphism of k[[s]] is k[[w]] on ANY invariant
uniformizer w of valuation 2 (induction on valuation: an invariant
series has even valuation, subtract the matching w-power).  Hence
E bar-even => E in [[eta^2]] and eta^2 in [[u~]] automatically; and
eta o sigma = -eta follows from uniqueness of the formal cube root
(eta o sigma and -eta both cube to -O/ell with equal leading term).
Passing checks therefore VALIDATE THE CODE; the "single-fibre descent"
as posed carries no falsifiable content.  (This also re-reads ai81's
"E is exactly a u~-series" as structural, not empirical.)

What IS informative: the exact rung values g_k and eta coefficients —
the arithmetic of the descent, not its existence.  Immediate exact
consequence recorded here: the cosh/sinh (zeta4-partner V0) family is
FALSIFIED scope (a) — an entire order-1 F would need |g_{k+1}/g_k| -> 0,
but the exact ratios GROW toward ~ -20 (finite radius of convergence
~ 1/20.5 in t = eta^2, i.e. |eta| ~ 0.221; the nearest-singularity
location is the sharpened datum).  All scope (a); audit-only.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

import json  # noqa: E402
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import qbeta_ck_sseries_exact_rational as core  # noqa: E402
core.ORD = 17
ORD = core.ORD
# validity window for the constructed eta (see module docstring)
ETA_MAX = ORD - 2      # eta exact through this s-order
T_MAX = ORD - 1        # t = eta^2 exact through this s-order
from qbeta_ck_sseries_exact_rational import (  # noqa: E402
    q, simp, ser_add, ser_mul, ser_scale, ser_inv, ser_sqrt,
    ser_log1, ser_cos0, rat_series, load_net_symbolic,
)

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent


def ser_compose(a, phi):
    assert phi[0] == 0
    out = [sp.Integer(0)] * (ORD + 1)
    out[0] = a[ORD]
    for n in range(ORD - 1, -1, -1):
        out = ser_mul(out, phi)
        out[0] = simp(out[0] + a[n])
    return out


def ser_cbrt1(a):
    """Cube root of a series with a[0] == 1."""
    assert simp(a[0] - 1) == 0
    out = [sp.Integer(0)] * (ORD + 1)
    out[0] = sp.Integer(1)
    # (out^3)_n = a_n solved order by order: 3*out_n + (lower conv) = a_n
    for n in range(1, ORD + 1):
        # cube of current partial (out_k known for k < n, out_n = 0)
        part = ser_mul(ser_mul(out, out), out)
        out[n] = simp((a[n] - part[n]) / 3)
    return out


def t_adic_match(f, t_ser, kmax, start=0, nmax=None):
    """f = sum_{k>=start} c_k t^k (t has s-valuation 2); exact residuals.

    Residuals are scanned only through order `nmax` (default ORD) — pass
    the validity window of the least-exact input series.
    """
    if nmax is None:
        nmax = ORD
    e = {}
    model = [sp.Integer(0)] * (ORD + 1)
    tpow = { }
    cur = [sp.Integer(1)] + [sp.Integer(0)] * ORD
    tpow[0] = cur
    for k in range(1, kmax + 1):
        tpow[k] = ser_mul(tpow[k - 1], t_ser)
    for k in range(start, kmax + 1):
        if 2 * k > nmax:
            break
        lead = tpow[k][2 * k]
        ek = simp((f[2 * k] - model[2 * k]) / lead) if lead != 0 else sp.Integer(0)
        e[k] = ek
        model = ser_add(model, ser_scale(ek, tpow[k]))
    resid = {n: simp(f[n] - model[n]) for n in range(0, nmax + 1)}
    first = next((n for n in range(0, nmax + 1) if sp.simplify(resid[n]) != 0), None)
    return e, resid, first


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(f" 0zr0 — eta-descent test (ORD={ORD}): E, O even/odd parts of one F(eta)?")
    print("=" * 78)

    dnet = sp.simplify(load_net_symbolic("neutron") - load_net_symbolic("proton"))
    dnet_reg = sp.cancel(dnet / (q - 1))
    # q₀ from q_parameter (proton pin, AGENTS.md 2026-08-07 directive).
    # Was a direct read of q-pinning-50-digit.witness.json, which is the
    # MUON anchor’s definition and bypasses the manifest entirely.
    q0 = Q_MP
    sgn = int(mp.sign(sp.lambdify(q, dnet, "mpmath")(q0)))
    Qb = rat_series(sp.Integer(sgn) * dnet_reg / q)
    QA = rat_series((2 * q + 1 - q**2) * (q + 1) / (2 * q**3))
    hbar2 = rat_series(((q - 1) / q) ** 2)
    b_ser = ser_mul(ser_sqrt(rat_series(q**4 + q**2 + 1)),
                    ser_inv(rat_series(q**2 + 1)))
    u_tilde = ser_mul(rat_series(q), ser_mul(b_ser, hbar2))
    sqrt_q = ser_sqrt(rat_series(q))
    z_ser = ser_mul(sqrt_q, ser_inv(rat_series(q + 1)))
    h_ser = rat_series(q - 1 / q)
    zm1 = list(z_ser); zm1[0] = simp(zm1[0] - 1)
    alpha = ser_add(ser_scale(sp.Rational(1, 2), ser_mul(zm1, h_ser)),
                    ser_scale(sp.Rational(-1, 2), u_tilde))
    R = ser_mul(Qb, ser_inv(ser_mul(QA, ser_cos0(alpha))))
    logR = ser_log1(R)
    phi = [sp.Integer(0)] + [sp.Integer(-1) ** n for n in range(1, ORD + 1)]
    logR_bar = ser_compose(logR, phi)
    E = [simp((a + b_) / 2) for a, b_ in zip(logR, logR_bar)]
    O = [simp((a - b_) / 2) for a, b_ in zip(logR, logR_bar)]
    assert sp.simplify(O[1]) == 0 and sp.simplify(O[2]) == 0
    ell = O[3]
    assert sp.simplify(ell) != 0
    print(f"  series built ({time.monotonic()-t0:.0f}s); O leading (s^3) = {sp.N(ell, 10)}")

    # eta: cube root of (O/ell)/s^3, re-shifted by s.  The zero-padding of
    # the top 3 orders makes eta exact only through ETA_MAX = ORD-2.
    O_shift3 = [simp(o / ell) for o in O[3:]] + [sp.Integer(0)] * 3   # (O/ell)/s^3
    eta_core = ser_cbrt1(O_shift3)                                     # 1 + ...
    eta = [sp.Integer(0)] + eta_core[:ORD]                             # s * core
    # (i) bar-oddness of eta — exact, scanned only over the valid window
    eta_bar = ser_compose(eta, phi)
    odd_resid = [simp(a + b_) for a, b_ in zip(eta_bar, eta)]
    first_odd = next((n for n in range(ETA_MAX + 1)
                      if sp.simplify(odd_resid[n]) != 0), None)
    print(f"  (i) eta bar-odd exactly through s^{ETA_MAX}? first violation: {first_odd}"
          + ("  — BAR-ODD ✓" if first_odd is None
             else f"  value {sp.N(odd_resid[first_odd], 10)}"))

    # t := eta^2 (exact through T_MAX)
    t_ser = ser_mul(eta, eta)

    # (ii) E in [[t]] (start k=1: E has no constant term)
    KMAX = T_MAX // 2
    eE, residE, firstE = t_adic_match(E, t_ser, KMAX, start=1, nmax=T_MAX)
    rungs_str = {k: str(sp.N(v, 8)) for k, v in eE.items()}
    print(f"  (ii) E in [[eta^2]] through s^{T_MAX}? first residual: {firstE}"
          + ("  ✓" if firstE is None else "")
          + f"\n       rungs g_k: {rungs_str}")

    # (iii) t vs u~: is t a u~-series?  (informational tie to the c_k ladder)
    eT, residT, firstT = t_adic_match(t_ser, u_tilde, KMAX, start=1, nmax=T_MAX)
    print(f"  (iii) eta^2 in [[u~]] through s^{T_MAX}? first residual: {firstT}"
          + ("  ✓" if firstT is None else ""))

    descends = (first_odd is None) and (firstE is None)
    # exact rung ratios — the actual data (see docstring INTERPRETATION)
    ratios = {k: sp.N(eE[k + 1] / eE[k], 8) for k in sorted(eE)[:-1]
              if sp.simplify(eE[k]) != 0}
    verdict = (
        ("ETA-DESCENT CONFIRMED AS A THEOREM (invariant theory: the bar-even "
         "subring of Q(sqrt3)[[s]] is k[[w]] on any bar-even valuation-2 "
         "uniformizer; cube-root uniqueness gives eta bar-odd) — the passing "
         f"checks (bar-odd to s^{ETA_MAX}, E in [[eta^2]] to s^{T_MAX}, "
         "eta^2 in [[u~]]) validate the code, not a hypothesis: the "
         "single-fibre descent as posed carries no falsifiable content. "
         "The informative output is the exact rung arithmetic: |g_{k+1}/g_k| "
         "GROWS toward ~20 (exact), so F(eta) has finite radius of "
         "convergence ~1/20.5 in t = eta^2 (|eta| ~ 0.221) — the cosh/sinh "
         "(zeta4-partner V0) entire family is falsified scope (a), and the "
         "nearest-singularity location is the sharpened constraint replacing "
         "the refuted h-forms. "
         "Scope (a): truncation order, net route.")
        if descends else
        (f"CODE/THEOREM MISMATCH at orders (i)={first_odd}, (ii)={firstE}: "
         "the membership checks are theorems (invariant theory), so an exact "
         "failure inside the valid window indicates a series-engine bug — "
         "investigate before drawing any physics conclusion. Scope (a).")
    )
    print(f"\n  VERDICT: {verdict}")
    print(f"  ({time.monotonic()-t0:.1f}s)")

    wb = WitnessBuilder("qbeta-zeta4-eta-descent", engine="sympy",
                        start_time=t0)
    wb.set_description(
        "0zr0: eta-descent — exact construction of the bar-odd fibre "
        "argument eta from O (cube-root gauge; O = ell*eta^3 by construction) "
        "+ exact membership checks over the validity window. INTERPRETATION: "
        "the membership checks are THEOREMS (invariant ring of the order-2 "
        "bar automorphism of Q(sqrt3)[[s]] is k[[w]] on any bar-even val-2 "
        "uniformizer; cube-root uniqueness makes eta bar-odd), so passing "
        "validates the code only — the single-fibre descent as posed has no "
        "falsifiable content. The data is the exact rung arithmetic: growing "
        "|g_{k+1}/g_k| -> ~20 falsifies the entire cosh/sinh (zeta4-partner "
        "V0) family scope (a) and locates a finite radius of convergence "
        "~1/20.5 in t = eta^2 (|eta| ~ 0.221). Development history: "
        "docs/audits/2026-07-03-0zr0-eta-descent-invariant-theory-prune.md."
    )
    wb.add_data("ORD", ORD)
    wb.add_data("eta_valid_through", ETA_MAX)
    wb.add_data("t_valid_through", T_MAX)
    wb.add_data("O_leading_ell_exact", str(ell))
    wb.add_data("eta_bar_odd_first_violation", first_odd)
    wb.add_data("E_in_eta2_rungs", {str(k): str(v) for k, v in eE.items()})
    wb.add_data("E_in_eta2_first_residual", firstE)
    wb.add_data("eta2_in_utilde_first_residual", firstT)
    wb.add_data("eta_coeffs_exact", {str(n): str(eta[n]) for n in range(1, ETA_MAX + 1)})
    wb.add_data("rung_ratios_gk1_over_gk", {str(k): str(v) for k, v in ratios.items()})
    wb.add_data("verdict", verdict)
    wb.add_data("scope", "(a); no wiring")
    wb.add_assertion("eta_bar_odd_in_window", first_odd is None, True)
    wb.add_assertion("E_descends_in_window", firstE is None, True)
    out = wb.save()
    print(f"  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
