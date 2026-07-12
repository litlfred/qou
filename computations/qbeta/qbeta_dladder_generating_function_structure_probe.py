#!/usr/bin/env python3
"""qbeta_dladder_generating_function_structure_probe.py

Route 2 of the bar-odd-S deformed-rung follow-up: structure-hunt the exact
D-ladder generating function D(ũ) = Σ_k d_k ũ^k. With the O/h top-order
artifact removed (route 3), the d_k ∈ ℚ(√3) are exact at every valid order, so
this looks for exact structure rather than PSLQ-ing floats.

The ladder is rebuilt here (ORD configurable via argv[1], default 31 → d₁…d₁₅;
the merged d-ladder probe runs ORD 19 → d₁…d₉) and the O/h division goes through
the valuation-aware core.ser_div (route 3). All coefficients are exact.

FINDINGS (scope-(a); no c_k wired; no fit; no tier change):

  1. **Exact parity structure.** Writing d_k = a_k + b_k√3 (a_k, b_k ∈ ℚ), the
     "simple"-denominator part alternates by parity: for ODD k the √3-part b_k
     has the small denominator and the rational part a_k a large one; for EVEN
     k it is reversed. Holds exactly at every tested k.

  2. **Ohtsuki/Habiro-type smooth denominators.** The simple-denominator
     interleaved sequence has 3-smooth denominators — powers of 3 with 5
     entering near k≈7 and 7 near k≈10 (a prime p first divides at index ~p),
     the signature of a factorial / q-factorial (Ohtsuki–Habiro) normalization.

  3. **D(ũ) is CONVERGENT with a weak algebraic branch point.** Domb–Sykes
     extrapolation of the coefficient ratios gives a finite radius
     ρ ≈ 0.143 (stable across windows; the 21-term ORD-43 run sharpens it to
     0.1432) and a small exponent α ≈ 0.1 (f ~ (1−ũ/ρ)^{−α}, possibly
     log-type). This is the sharp contrast with routes 1: the state-integral
     Ohtsuki κ-tower is *divergent* (Gevrey-1, radius 0), whereas the net-route
     D-ladder is a genuinely *convergent* object — the two bar-odd-S routes are
     NOT the same series.

  4. **No low-order holonomic recurrence.** No P-finite recurrence of order ≤ 3
     and polynomial degree ≤ 4 fits a_k or b_k (the ORD-43 21-term run rules out
     order ≤ 4, degree ≤ 5 too). D(ũ) is not hypergeometric / P-finite at
     accessible order; its generating function is a non-elementary
     algebraic-branch-point object.

  5. **Singularity origin.** The radius is NOT set by any simple real special
     value of the underlying R(q): the sqrt branch points q⁴+q²+1=0 and the
     u'(q)=0 folds all map to ũ=0, and the nearest real singularity (the QA
     zero q=1+√2) sits at |ũ|=0.775 ≫ ρ. So the branch point at ρ is a *complex*
     singularity of log R(q(ũ)), left unidentified. ρ lands within ~1% of both
     √3/12 and 1/7, but the slow Domb–Sykes convergence forbids identifying it
     — reported as data, not a match (anti-fit).

CONCLUSION: the D-ladder generating function has an exact parity + smooth-
denominator arithmetic and is a convergent algebraic-branch-point series
(radius ≈ 0.143), structurally distinct from the divergent κ-tower — but no
elementary / P-finite closed form emerges at 15–21 terms. Nothing wired.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))

import json  # noqa: E402
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import qbeta_ck_sseries_exact_rational as core  # noqa: E402
core.ORD = int(sys.argv[1]) if len(sys.argv) > 1 else 31
ORD = core.ORD
from qbeta_ck_sseries_exact_rational import (  # noqa: E402
    q, simp, ser_add, ser_mul, ser_scale, ser_inv, ser_sqrt,
    ser_log1, ser_cos0, rat_series, load_net_symbolic, ser_div,
)

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent
R3 = sp.sqrt(3)


def ser_compose(a, phi):
    out = [sp.Integer(0)] * (ORD + 1)
    out[0] = a[ORD]
    for n in range(ORD - 1, -1, -1):
        out = ser_mul(out, phi)
        out[0] = simp(out[0] + a[n])
    return out


def build_d_ladder():
    """Exact d_k of O/h = Σ d_k ũ^k (same objects as the merged d-ladder probe,
    O/h through the valuation-aware ser_div)."""
    dnet = sp.simplify(load_net_symbolic("neutron") - load_net_symbolic("proton"))
    dnet_reg = sp.cancel(dnet / (q - 1))
    q0 = mp.mpf(json.load(open(_pb.witness_path(
        "q-pinning-50-digit.witness.json", HERE)))["derived_50_digit"]["q"])
    sgn = int(mp.sign(sp.lambdify(q, dnet, "mpmath")(q0)))
    Qb = rat_series(sp.Integer(sgn) * dnet_reg / q)
    QA = rat_series((2 * q + 1 - q**2) * (q + 1) / (2 * q**3))
    hbar2 = rat_series(((q - 1) / q) ** 2)
    b_ser = ser_mul(ser_sqrt(rat_series(q**4 + q**2 + 1)),
                    ser_inv(rat_series(q**2 + 1)))
    u_ser = ser_mul(rat_series(q), ser_mul(b_ser, hbar2))    # ũ = q·b·hbar²
    sqrt_q = ser_sqrt(rat_series(q))
    z_ser = ser_mul(sqrt_q, ser_inv(rat_series(q + 1)))
    h_ser = rat_series(q - 1 / q)
    zm1 = list(z_ser); zm1[0] = simp(zm1[0] - 1)
    alpha = ser_add(ser_scale(sp.Rational(1, 2), ser_mul(zm1, h_ser)),
                    ser_scale(sp.Rational(-1, 2), u_ser))
    R = ser_mul(Qb, ser_inv(ser_mul(QA, ser_cos0(alpha))))
    logR = ser_log1(R)
    phi = [sp.Integer(0)] + [sp.Integer(-1) ** n for n in range(1, ORD + 1)]
    O = [simp((x - y) / 2) for x, y in zip(logR, ser_compose(logR, phi))]
    G, valid_top = ser_div(O, h_ser)
    KMAX = valid_top // 2
    upow = [None, list(u_ser)]
    for k in range(2, KMAX + 1):
        upow.append(ser_mul(upow[k - 1], u_ser))
    dk, model = {}, [sp.Integer(0)] * (ORD + 1)
    for k in range(1, KMAX + 1):
        ek = simp((G[2 * k] - model[2 * k]) / upow[k][2 * k])
        dk[k] = ek
        model = ser_add(model, ser_scale(ek, upow[k]))
    # over-determination: odd-order valid residuals must vanish
    odd_ok = all(sp.simplify(G[n] - model[n]) == 0 for n in range(1, valid_top + 1, 2))
    return dk, KMAX, valid_top, odd_ok


def find_prec(seq, order_max, deg_max, hold=3):
    """Search a P-finite recurrence Σ_i p_i(k) s_{k-i}=0, p_i poly deg≤deg;
    fit on all-but-`hold` usable rows, require it to hold on the held-out."""
    ks = sorted(seq); kmin = min(ks)
    for order in range(1, order_max + 1):
        for deg in range(0, deg_max + 1):
            nun = (order + 1) * (deg + 1)
            rows_k = [k for k in ks if k - order >= kmin]
            if len(rows_k) < nun + hold:
                continue
            fit_k, val_k = rows_k[:-hold], rows_k[-hold:]
            M = sp.zeros(len(fit_k), nun)
            for r, k in enumerate(fit_k):
                col = 0
                for i in range(order + 1):
                    for dp in range(deg + 1):
                        M[r, col] = seq[k - i] * sp.Rational(k) ** dp
                        col += 1
            for vec in M.nullspace():
                cols = [(i, dp) for i in range(order + 1) for dp in range(deg + 1)]
                if all(sp.simplify(sum(vec[c] * seq[k - i] * sp.Rational(k) ** dp
                                       for c, (i, dp) in enumerate(cols))) == 0
                       for k in val_k):
                    return (order, deg)
    return None


def domb_sykes(dk, lo, hi):
    df = {k: mp.mpf(str(sp.N(v, 50))) for k, v in dk.items()}
    r = {k: df[k] / df[k - 1] for k in range(2, max(df) + 1)}
    ravg = {k: (r[k] + r[k + 1]) / 2 for k in range(2, max(df))}  # damp parity oscillation
    ks = [k for k in ravg if lo <= k <= hi]
    X = [1 / mp.mpf(k) for k in ks]; Y = [ravg[k] for k in ks]
    n = len(ks); sx = sum(X); sy = sum(Y); sxx = sum(x * x for x in X); sxy = sum(x * y for x, y in zip(X, Y))
    slope = (n * sxy - sx * sy) / (n * sxx - sx * sx); inter = (sy - slope * sx) / n
    return 1 / inter, slope / inter + 1


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(f" route 2 — D-ladder generating-function structure hunt (ORD {ORD})")
    print("=" * 78)

    dk, KMAX, valid_top, odd_ok = build_d_ladder()
    K = KMAX
    print(f"  built d₁…d_{K} (valid_top s^{valid_top}, odd-order over-det zero: {odd_ok})")
    a = {k: sp.Rational(sp.expand(dk[k]).coeff(R3, 0)) for k in dk}
    b = {k: sp.Rational(sp.expand(dk[k]).coeff(R3, 1)) for k in dk}

    # ---- 1. parity structure: which part carries the small denominator ----
    parity_ok = True
    for k in range(1, K + 1):
        da, db = a[k].q, b[k].q
        simple_is_b = db <= da
        if k % 2 == 1 and not simple_is_b:
            parity_ok = False
        if k % 2 == 0 and simple_is_b and da != db:
            parity_ok = False
    print(f"\n  [1] parity structure (odd k → √3-part simple, even k → rational simple): {parity_ok}")

    # ---- 2. smooth (3,5,7)-denominators of the simple sequence ----
    simple = {k: (b[k] if k % 2 else a[k]) for k in range(1, K + 1)}
    dens = {k: sp.factorint(sp.Rational(simple[k]).q) for k in simple}
    primes = sorted({p for f in dens.values() for p in f})
    smooth = all(all(p in (2, 3, 5, 7) for p in f) for f in dens.values())
    v3 = [dens[k].get(3, 0) for k in range(1, K + 1)]
    print(f"  [2] simple-denominator primes = {primes}; 3-smooth-ish (≤7): {smooth}")
    print(f"      3-adic valuations v₃(den s_k) = {v3}")

    # ---- 3. Domb–Sykes radius + exponent (stability across windows) ----
    print("\n  [3] Domb–Sykes ratio extrapolation (radius ρ, exponent α):")
    windows = [(6, K - 1), (8, K - 1)] if K >= 12 else [(4, K - 1)]
    rho = alpha = None
    for lo, hi in windows:
        rho, alpha = domb_sykes(dk, lo, hi)
        print(f"      window k={lo}..{hi}: ρ = {mp.nstr(rho, 7)}   α = {mp.nstr(alpha, 5)}")
    convergent = bool(mp.mpf("0.05") < rho < mp.mpf("0.5"))
    print(f"      => convergent (finite ρ): {convergent}; contrast: κ-tower is divergent (radius 0)")
    # candidate constants near ρ (reported, NOT identified — anti-fit)
    for name, val in [("√3/12", R3 / 12), ("1/7", sp.Rational(1, 7))]:
        vv = mp.mpf(str(sp.N(val, 30)))
        print(f"      ρ / ({name}={mp.nstr(vv, 8)}) = {mp.nstr(rho / vv, 6)}  (data only, not identified)")

    # ---- 4. holonomic recurrence search ----
    print("\n  [4] holonomic P-recurrence search (order ≤ 3, deg ≤ 4):")
    resa = find_prec(a, 3, 4); resb = find_prec(b, 3, 4)
    print(f"      a_k: {'FOUND ' + str(resa) if resa else 'none'};  "
          f"b_k: {'FOUND ' + str(resb) if resb else 'none'}")
    no_prec = (resa is None) and (resb is None)

    # ---- 5. singularity origin: simple real special values map far / to 0 ----
    def u_of_q(qq):
        qq = mp.mpc(qq)
        return qq * (mp.sqrt(qq**4 + qq**2 + 1) / (qq**2 + 1)) * ((qq - 1) / qq) ** 2
    u_QAplus = abs(u_of_q(mp.mpf(1) + mp.sqrt(2)))     # nearest real special value
    u_bp = abs(u_of_q(mp.expjpi(sp.Rational(1, 3))))   # sqrt branch point q^4+q^2+1=0
    print("\n  [5] singularity origin (simple real special values):")
    print(f"      |ũ(q=1+√2)| = {mp.nstr(u_QAplus, 6)} (≫ ρ);  |ũ(q⁴+q²+1=0)| = {mp.nstr(u_bp, 4)} (→0, folds to origin)")
    print(f"      ⇒ ρ≈{mp.nstr(rho, 5)} is a COMPLEX singularity of log R(q(ũ)), not a simple real value")

    d5_ai81 = sp.Rational(-252241, 243) * R3 - sp.Rational(836891, 139345920)
    d5_ok = sp.simplify(dk[5] - d5_ai81) == 0

    verdict = (
        f"D-ladder generating function D(ũ)=Σd_k ũ^k (d₁…d_{K} exact ℚ(√3)): "
        f"[1] exact parity structure (odd k → √3-part small-denominator, even k → "
        f"rational part); [2] simple-denominator sequence is 3-smooth "
        f"(Ohtsuki/Habiro factorial normalization; primes {primes}); [3] CONVERGENT "
        f"with radius ρ≈{mp.nstr(rho, 5)} and weak branch-point exponent α≈{mp.nstr(alpha, 3)} "
        f"— structurally distinct from the DIVERGENT Gevrey-1 κ-tower (routes 1); "
        f"[4] no P-finite recurrence (order≤3, deg≤4); [5] the branch point is a "
        f"complex singularity of log R(q(ũ)), not a simple real special value; ρ is "
        f"within ~1% of √3/12 and 1/7 but NOT identified (anti-fit). No closed form "
        f"emerges at {K} terms. Scope-(a); no c_k wired; no fit."
    )
    print(f"\n  VERDICT: {verdict}")
    print(f"  ({time.monotonic() - t0:.1f}s)")

    wb = WitnessBuilder("qbeta-dladder-generating-function-structure", engine="sympy")
    wb.set_description(
        "Route 2: structure hunt of the exact D-ladder generating function "
        "D(ũ)=Σ d_k ũ^k (d_k ∈ ℚ(√3), O/h via the route-3 ser_div). Findings: "
        "(1) exact parity structure (odd k → √3-part carries the small "
        "denominator, even k → rational part); (2) 3-smooth simple-denominators "
        "(Ohtsuki/Habiro factorial normalization); (3) CONVERGENT, Domb–Sykes "
        f"radius ρ≈{mp.nstr(rho, 5)}, weak branch-point exponent α≈{mp.nstr(alpha, 3)} — "
        "the sharp contrast with the DIVERGENT Gevrey-1 κ-tower of routes 1; "
        "(4) no P-finite recurrence (order≤3 deg≤4; ORD-43 rules out order≤4 "
        "deg≤5); (5) singularity is a complex point of log R(q(ũ)), not a simple "
        "real special value; ρ within ~1% of √3/12 and 1/7 but not identified "
        "(anti-fit). No elementary closed form at 15–21 terms. Scope-(a); no wiring."
    )
    wb.add_data("ORD", ORD)
    wb.add_data("n_terms", K)
    wb.add_data("d_k_exact", {str(k): str(v) for k, v in dk.items()})
    wb.add_data("a_k_rational", {str(k): str(a[k]) for k in a})
    wb.add_data("b_k_sqrt3_coeff", {str(k): str(b[k]) for k in b})
    wb.add_data("parity_structure_holds", parity_ok)
    wb.add_data("simple_denominator_primes", primes)
    wb.add_data("simple_denominator_3adic_valuations", v3)
    wb.add_data("smooth_denominators_le7", smooth)
    wb.add_data("domb_sykes_radius_rho", mp.nstr(rho, 8))
    wb.add_data("domb_sykes_exponent_alpha", mp.nstr(alpha, 6))
    wb.add_data("convergent_positive_radius", convergent)
    wb.add_data("contrast_kappa_tower", "κ-tower is divergent Gevrey-1 (radius 0); D-ladder is convergent")
    wb.add_data("no_low_order_p_recurrence", no_prec)
    wb.add_data("nearest_real_special_value_u_QAplus", mp.nstr(u_QAplus, 8))
    wb.add_data("rho_over_sqrt3_over_12", mp.nstr(rho / mp.mpf(str(sp.N(R3 / 12, 30))), 6))
    wb.add_data("rho_over_one_seventh", mp.nstr(rho * 7, 6))
    wb.add_data("verdict", verdict)
    wb.add_data("scope", "(a) — exact ℚ(√3) ladder + numerical singularity analysis; no wiring")
    wb.add_data("caveats", [
        "radius/exponent are Domb–Sykes extrapolations; small exponent (~0.1) "
        "converges slowly — ρ known to ~1%, α to a factor.",
        "ρ within ~1% of √3/12 and 1/7 is reported as data, NOT an identification.",
        "no c_k wired; no fit; no tier change.",
    ])
    wb.add_assertion("valid_orders_over_determined", odd_ok, True)
    wb.add_assertion("parity_structure_holds", parity_ok, True)
    wb.add_assertion("smooth_denominators_le7", smooth, True)
    wb.add_assertion("convergent_positive_radius", convergent, True)
    wb.add_assertion("no_low_order_p_recurrence", no_prec, True)
    wb.add_assertion("d5_reproduces_ai81_witness", bool(d5_ok), True)
    out = wb.save()
    print(f"  Witness: {out}")
    return 0 if (parity_ok and smooth and convergent and no_prec and odd_ok and d5_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
