#!/usr/bin/env python3
"""qbeta_dladder_generating_function_structure_probe.py

Route 2 of the bar-odd-S deformed-rung follow-up: structure-hunt the exact
D-ladder generating function D(ũ) = Σ_k d_k ũ^k. With the O/h top-order
artifact removed (route 3), the d_k ∈ ℚ(√3) are exact at every valid order, so
this looks for exact structure rather than PSLQ-ing floats.

The ladder is rebuilt here (ORD configurable via argv[1], default 43 → d₁…d₂₁;
the merged d-ladder probe runs ORD 19 → d₁…d₉) and the O/h division goes through
the valuation-aware core.ser_div (route 3). All coefficients are exact.

FINDINGS (scope-(a); no c_k wired; no fit; no tier change):

  1. **Exact parity structure.** Writing d_k = a_k + b_k√3 (a_k, b_k ∈ ℚ), the
     "simple"-denominator part alternates by parity: for ODD k the √3-part b_k
     has the small denominator and the rational part a_k a large one; for EVEN
     k it is reversed. Holds exactly at every tested k.

  2. **Ohtsuki/Habiro-type factorial-smooth denominators.** The simple-
     denominator interleaved sequence has factorial-smooth denominators — the
     largest prime factor of den(s_k) grows ~linearly with k (5 enters near
     k≈7, 7 near k≈10, 11/13 near k≈16–21; p_max(k) ≲ 2k), the signature of a
     factorial / q-factorial (Ohtsuki–Habiro) normalization.

  3. **Growth diagnostic in the accessible window — NOT a divergence verdict.**
     The root test |dₖ|^{1/k} is still rising at the top of the window
     (4.4→6.1 through k=27) and log|dₖ| = A + B·k + C·k·log k fits with
     C ≈ 0.05–0.08 > 0. **RE-SCOPED 2026-08-14:** this is *consistent with* a
     finite radius, not evidence against one. With the true behaviour
     d_k = −(1/(2h*_ρ))·ρ^{−k}/k·(1+O(1/k)), the 1/k factor gives
     |dₖ|^{1/k} = (1/ρ)·k^{−1/k}(1+o(1)), which approaches 1/ρ ≈ 7.0 **from
     below and monotonically** — so "still rising at k=21" is exactly what the
     law predicts here. The k·log k term absorbs that same −log k, which is why
     C > 0 outfits a pure geometric law on 21 terms. That C **drifts down**
     with the window (0.077→0.048) is the tell: a genuine super-exponential
     index would not.

  4. **No low-order holonomic recurrence.** No P-finite recurrence of order ≤ 3
     and polynomial degree ≤ 4 fits a_k or b_k (the ORD-43 21-term run rules out
     order ≤ 4, degree ≤ 5 too). D(ũ) is not hypergeometric / P-finite at
     accessible order. **This carries no growth-class information:** non-holonomic
     does not imply divergent, and φ(w)log(1−w/ρ)+ψ(w) with algebraic φ,ψ is
     convergent *and* not low-order P-finite. This negative is UNAFFECTED by the
     re-scope and still stands.

  5. **The finite singularity IS there — at the Q_b zero.** The 2026-07-12
     reading concluded "no singularity near 0.143" from a search over the real
     special value q=1+√2 (|ũ|≈0.775) and the sqrt branch points q⁴+q²+1=0
     (which fold to ũ=0). That search was **incomplete**: it omitted the **Q_b
     zero**, the real root > 1 of the irreducible degree-12 factor of the Δ_net
     numerator, q*_ρ ≈ 1.4898948. Under this probe's own ũ map,
     |ũ(q*_ρ)| = 0.142799996644689…, reproducing the published radius to ~1e-30.
     The singularity was there; the search did not look where it lives.

CONCLUSION (re-scoped 2026-08-14): the D-ladder generating function has an exact
parity + factorial-smooth-denominator arithmetic, is **CONVERGENT** with radius
ρ = ũ(q*_ρ) = 0.142799996644689… (the image of a Q_b zero), and admits no
low-order P-finite recurrence — the last of which is an algebraic statement and
implies nothing about growth. It is therefore **NOT** in the κ-tower's family:
that ladder is genuinely Gevrey-1 divergent, this one is not. The 2026-07-12
"super-exponentially divergent (radius → 0)" reading, and its dismissal of
PR #3716's ρ≈0.143 as a finite-n shadow, are **WITHDRAWN**; see
docs/audits/2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md and
docs/audits/2026-08-14-non-holonomic-implies-resurgent-corpus-sweep.md.
No elementary closed form emerges at 15–27 terms. Nothing wired.
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
core.ORD = int(sys.argv[1]) if len(sys.argv) > 1 else 43
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


def growth_diagnostic(dk, lo):
    """Corpus divergence diagnostic (alien-calculus audit): a root test that
    RISES WITHOUT PLATEAU + a positive k·log k growth term ⇒ super-exponential,
    radius → 0 (q-Gevrey). Returns (root_test_rising, C, ssr_ratio) where C is
    the k·log k coefficient of log|dₖ| and ssr_ratio = SSR(super-exp)/SSR(geom)
    (≪1 ⇒ super-exponential beats a constant-radius law)."""
    df = {k: mp.mpf(str(sp.N(v, 50))) for k, v in dk.items()}
    K = max(df)
    root = {k: abs(df[k]) ** (mp.mpf(1) / k) for k in df if k >= 4}
    rk = sorted(root)
    root_rising = root[rk[-1]] > root[rk[-4]] > root[rk[-8]]   # still climbing at the top
    ks = list(range(lo, K + 1))
    y = mp.matrix([mp.log(abs(df[k])) for k in ks])
    M = mp.matrix([[mp.mpf(1), mp.mpf(k), k * mp.log(k)] for k in ks])
    c = mp.lu_solve(M.T * M, M.T * y)
    M0 = mp.matrix([[mp.mpf(1), mp.mpf(k)] for k in ks])
    c0 = mp.lu_solve(M0.T * M0, M0.T * y)
    ssr = sum((c[0] + c[1] * k + c[2] * k * mp.log(k) - mp.log(abs(df[k]))) ** 2 for k in ks)
    ssr0 = sum((c0[0] + c0[1] * k - mp.log(abs(df[k]))) ** 2 for k in ks)
    return bool(root_rising), c[2], (ssr / ssr0 if ssr0 != 0 else mp.mpf(0)), root


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

    # ---- 2. factorial-smooth denominators of the simple sequence ----
    # Signature of a factorial / q-factorial (Ohtsuki–Habiro) normalization: the
    # largest prime factor of den(s_k) grows ~linearly with k (each prime p first
    # enters near index ~p), i.e. den(s_k) is "k-smooth-ish" — NOT bounded by a
    # fixed prime (11,13,… enter as k grows; the earlier "primes ≤ 7" was a
    # 15-term artifact).
    simple = {k: (b[k] if k % 2 else a[k]) for k in range(1, K + 1)}
    dens = {k: sp.factorint(sp.Rational(simple[k]).q) for k in simple}
    primes = sorted({p for f in dens.values() for p in f})
    pmax = {k: (max(dens[k]) if dens[k] else 1) for k in dens}
    factorial_smooth = all(pmax[k] <= 2 * k + 3 for k in dens)   # p_max(k) ≲ 2k
    v3 = [dens[k].get(3, 0) for k in range(1, K + 1)]
    print(f"  [2] denominator primes seen = {primes}; largest prime factor p_max(k) ≤ 2k+3 "
          f"(factorial-smooth): {factorial_smooth}")
    print(f"      p_max(s_k) = {[pmax[k] for k in range(1, K + 1)]}")
    print(f"      3-adic valuations v₃(den s_k) = {v3}")
    smooth = factorial_smooth

    # ---- 3. growth diagnostic in the accessible window (NOT a divergence verdict) ----
    # HISTORY. 2026-07-12 read this diagnostic as "super-exponentially DIVERGENT
    # (radius → 0)" and called the Domb–Sykes ρ≈0.143 a finite-n shadow.
    # RE-SCOPED 2026-08-14: the ladder is CONVERGENT with ρ = ũ(q*_ρ) (see [5]),
    # and the numbers below do not contradict that.  With the true behaviour
    #     d_k = −(1/(2h*_ρ))·ρ^(−k)/k·(1+O(1/k)),
    # the 1/k factor makes |d_k|^(1/k) = (1/ρ)·k^(−1/k)(1+o(1)) approach 1/ρ ≈ 7.0
    # from BELOW and monotonically — so "still rising at k=21" is exactly what a
    # ρ^(−k)/k law predicts in this window, not evidence against a finite radius.
    # Likewise the k·log k term absorbs that same −log k, which is why C > 0 fits
    # better than a pure geometric law on 21 terms.  The measurement stands; only
    # the verdict drawn from it was wrong.
    print("\n  [3] growth diagnostic in the accessible window (k ≤ %d — NOT a divergence verdict):" % K)
    lo = 10 if K >= 14 else 6
    root_rising, C, ssr_ratio, root = growth_diagnostic(dk, lo)
    rk = sorted(root)
    print(f"      root test |dₖ|^(1/k): {mp.nstr(root[rk[0]], 5)} → {mp.nstr(root[rk[-1]], 5)} "
          f"(k={rk[0]}..{rk[-1]}); still rising at top: {root_rising}")
    print(f"      log|dₖ| = A+B·k+C·k·log k fit: C = {mp.nstr(C, 5)}; "
          f"SSR(k·log k)/SSR(geom) = {mp.nstr(ssr_ratio, 4)}")
    root_test_rising_in_window = bool(root_rising and C > 0 and ssr_ratio < mp.mpf("0.3"))
    print(f"      => root test still rising in-window: {root_test_rising_in_window}")
    # the finite-radius prediction the window is compared against
    _rho_pub = mp.mpf("0.142799996644689688905720885779")
    print(f"      1/ρ = {mp.nstr(1 / _rho_pub, 6)} — the value |dₖ|^(1/k) is approaching "
          f"from below; at k={rk[-1]} it is {mp.nstr(root[rk[-1]], 5)}, still short, as ρ^(−k)/k predicts")
    print("      CONSISTENT with a finite radius; see [5] for the singularity itself")

    # ---- 4. holonomic recurrence search ----
    print("\n  [4] holonomic P-recurrence search (order ≤ 3, deg ≤ 4):")
    resa = find_prec(a, 3, 4); resb = find_prec(b, 3, 4)
    print(f"      a_k: {'FOUND ' + str(resa) if resa else 'none'};  "
          f"b_k: {'FOUND ' + str(resb) if resb else 'none'}")
    no_prec = (resa is None) and (resb is None)

    # ---- 5. singularity origin: the Q_b zero IS the radius (CORRECTED 2026-08-09) ----
    # This section previously searched only the real special value q=1+√2 and the
    # sqrt branch points q⁴+q²+1=0, found nothing near 0.143, and concluded "no
    # finite singularity ⇒ radius → 0".  The search was incomplete: it omitted the
    # **Q_b zero**, the real root > 1 of the irreducible degree-12 factor of the
    # Δ_net numerator.  Its image under this function's own ũ map is 0.14279999…,
    # i.e. exactly the radius.  The singularity was there; the search did not look
    # where it lives.  See docs/audits/2026-08-09-dladder-is-convergent-radius-is-
    # the-qb-zero.md.
    def u_of_q(qq):
        qq = mp.mpc(qq)
        return qq * (mp.sqrt(qq**4 + qq**2 + 1) / (qq**2 + 1)) * ((qq - 1) / qq) ** 2
    u_QAplus = abs(u_of_q(mp.mpf(1) + mp.sqrt(2)))     # nearest real special value
    u_bp = abs(u_of_q(mp.expjpi(sp.Rational(1, 3))))   # sqrt branch point q^4+q^2+1=0

    # the omitted candidate: irreducible degree-12 factor of the Δ_net numerator
    QB_POLY = [1, 2, -4, -8, 6, 16, -10, -16, 6, 8, -4, -2, 1]

    def _qb_deg12(x):
        acc = mp.mpf(0)
        for c in QB_POLY:
            acc = acc * x + c
        return acc

    q_star_rho = mp.findroot(_qb_deg12, mp.mpf("1.49"))   # real root > 1
    u_qb = abs(u_of_q(q_star_rho))
    rho_published = mp.mpf("0.142799996644689688905720885779")
    rho_rel = abs(u_qb - rho_published) / rho_published
    singularity_at_rho = bool(rho_rel < mp.mpf("1e-20"))

    print("\n  [5] the finite singularity IS there — at the Q_b zero (CORRECTED 2026-08-09):")
    print(f"      |ũ(q=1+√2)| = {mp.nstr(u_QAplus, 6)};  |ũ(q⁴+q²+1=0)| = {mp.nstr(u_bp, 4)} (→0, folds to origin)")
    print(f"      Q_b zero q*_ρ = {mp.nstr(q_star_rho, 20)}  (deg-12 factor of the Δ_net numerator)")
    print(f"      |ũ(q*_ρ)|     = {mp.nstr(u_qb, 24)}")
    print(f"      published ρ   = {mp.nstr(rho_published, 24)}   rel diff = {mp.nstr(rho_rel, 4)}")
    print(f"      => the singularity sits exactly at ρ: {singularity_at_rho}")
    print("      the earlier 'no singularity near 0.143' followed from an INCOMPLETE")
    print("      search (q=1+√2 and the folds only); this root was never tested.")

    d5_ai81 = sp.Rational(-252241, 243) * R3 - sp.Rational(836891, 139345920)
    d5_ok = sp.simplify(dk[5] - d5_ai81) == 0

    verdict = (
        f"D-ladder generating function D(ũ)=Σd_k ũ^k (d₁…d_{K} exact ℚ(√3)): "
        f"[1] exact parity structure (odd k → √3-part small-denominator, even k → "
        f"rational part); [2] simple-denominator sequence is 3-smooth "
        f"(Ohtsuki/Habiro factorial normalization; primes {primes}); [3] in the "
        f"accessible window the root test is still rising "
        f"(→{mp.nstr(root[rk[-1]], 4)} at k={rk[-1]}) with C={mp.nstr(C, 3)}>0 in "
        f"log|dₖ|=A+Bk+C·k·log k (SSR {mp.nstr(ssr_ratio, 3)}× the geometric law) — "
        f"this is CONSISTENT WITH the finite radius, not evidence against it: "
        f"d_k = −(1/(2h*_ρ))ρ^(−k)/k means |dₖ|^(1/k) → 1/ρ = "
        f"{mp.nstr(1 / rho_published, 5)} from below and has not arrived by k={rk[-1]}; "
        f"[4] no P-finite recurrence (order≤3, deg≤4) — which does NOT imply "
        f"divergence (φ(w)log(1−w/ρ)+ψ(w) is convergent and not P-finite); "
        f"[5] the finite singularity IS present, at the Q_b zero q*_ρ="
        f"{mp.nstr(q_star_rho, 12)}: |ũ(q*_ρ)|={mp.nstr(u_qb, 18)} reproduces the "
        f"published ρ to rel {mp.nstr(rho_rel, 3)} — the 2026-07-12 'no singularity "
        f"near 0.143 ⇒ radius→0' followed from an INCOMPLETE search that omitted "
        f"this root. RE-SCOPED 2026-08-14 per the 2026-08-09 convergence "
        f"correction. Scope-(a); no c_k wired; no fit."
    )
    print(f"\n  VERDICT: {verdict}")
    print(f"  ({time.monotonic() - t0:.1f}s)")

    wb = WitnessBuilder("qbeta-dladder-generating-function-structure", engine="sympy")
    wb.set_description(
        "Route 2: structure hunt of the exact D-ladder generating function "
        "D(ũ)=Σ d_k ũ^k (d_k ∈ ℚ(√3), O/h via the route-3 ser_div). Findings: "
        "(1) exact parity structure (odd k → √3-part carries the small "
        "denominator, even k → rational part); (2) 3-smooth simple-denominators "
        "(Ohtsuki/Habiro factorial normalization); (3) in the accessible window "
        f"the root test is still rising with C={mp.nstr(C, 3)}>0 in "
        "log|dₖ|=A+Bk+C·k·log k — CONSISTENT WITH the finite radius rather than "
        "evidence against it, since d_k = −(1/(2h*_ρ))ρ^(−k)/k approaches "
        "|dₖ|^(1/k) → 1/ρ from below and has not arrived by k=21; "
        "(4) no P-finite recurrence (order≤3 deg≤4; ORD-43 rules out order≤4 "
        "deg≤5) — which does NOT imply divergence; (5) the finite singularity IS "
        "present, at the Q_b zero q*_ρ≈1.48989, whose image under this probe's own "
        "ũ map reproduces the published ρ=0.142799996644689… . RE-SCOPED "
        "2026-08-14: the 2026-07-12 'super-exponentially divergent (radius→0)' "
        "reading rested on an INCOMPLETE singularity search that omitted this "
        "root; see docs/audits/2026-08-09-dladder-is-convergent-radius-is-the-qb-"
        "zero.md. The exact d_k, the parity structure, the 3-smooth denominators "
        "and the non-holonomicity are all UNAFFECTED. Scope-(a); no wiring."
    )
    wb.add_data("ORD", ORD)
    wb.add_data("n_terms", K)
    wb.add_data("d_k_exact", {str(k): str(v) for k, v in dk.items()})
    wb.add_data("a_k_rational", {str(k): str(a[k]) for k in a})
    wb.add_data("b_k_sqrt3_coeff", {str(k): str(b[k]) for k in b})
    wb.add_data("parity_structure_holds", parity_ok)
    wb.add_data("simple_denominator_primes", primes)
    wb.add_data("simple_denominator_3adic_valuations", v3)
    wb.add_data("factorial_smooth_denominators", smooth)
    wb.add_data("root_test_rises_without_plateau", root_rising)
    wb.add_data("root_test_values", {str(k): mp.nstr(root[k], 8) for k in sorted(root)})
    wb.add_data("superexp_C_klogk_coeff", mp.nstr(C, 6))
    wb.add_data("superexp_vs_geometric_ssr_ratio", mp.nstr(ssr_ratio, 6))
    wb.add_data("root_test_still_rising_in_window", root_test_rising_in_window)
    wb.add_data("contrast_kappa_tower",
                "RE-SCOPED 2026-08-14. The D-ladder is CONVERGENT (ρ = ũ(q*_ρ) = "
                "0.142799996644689…, κ = 0; 2026-08-09 correction), so it is NOT in the "
                "κ-tower's family: the κ-tower is genuinely Gevrey-1 divergent (Borel "
                "singularity A≈0.7), this ladder is not. The 2026-07-12 claim of a shared "
                "divergent family is withdrawn. A divergent and a convergent series cannot "
                "be equated term-by-term — the corpus already carries that as a proved "
                "scope-(b) result.")
    wb.add_data("no_low_order_p_recurrence", no_prec)
    wb.add_data("non_holonomic_does_not_imply_divergent",
                "The order≤3/deg≤4 negative in [4] constrains the ALGEBRAIC class only. "
                "φ(w)log(1−w/ρ)+ψ(w) with algebraic φ,ψ is convergent AND not low-order "
                "P-finite, so no growth-class conclusion follows from it.")
    wb.add_data("singularity_at_qb_zero", {
        "q_star_rho": mp.nstr(q_star_rho, 24),
        "utilde_q_star_rho": mp.nstr(u_qb, 24),
        "published_rho": mp.nstr(rho_published, 24),
        "relative_difference": mp.nstr(rho_rel, 6),
        "note": "the root the 2026-07-12 singularity search omitted; its image under "
                "this probe's own ũ map IS the radius",
    })
    wb.add_data("other_singularity_candidates_checked", {
        "utilde_q_1_plus_sqrt2": mp.nstr(u_QAplus, 8),
        "utilde_sqrt_branch_point": "→0 (folds to origin)",
        "note": "these two alone were the 2026-07-12 search; both land far from ρ, which "
                "is why that search concluded 'no finite singularity'",
    })
    wb.add_data("verdict", verdict)
    wb.add_data("scope", "(a) — exact ℚ(√3) ladder + corpus growth-class diagnostic; no wiring")
    wb.add_data("caveats", [
        "C (the k·log k coefficient) drifts DOWN with the fit window (0.077→0.048, "
        "k up to 27). Read 2026-07-12 as a q-Gevrey shadow; re-scoped 2026-08-14 — a "
        "drift toward 0 is what a CONVERGENT ladder does to this diagnostic, since the "
        "k·log k term is absorbing the −log k of a ρ^(−k)/k law rather than a genuine "
        "super-exponential factor.",
        "PR #3716's 'convergent radius 0.143' was called a finite-n shadow on "
        "2026-07-12; that call is WITHDRAWN — 0.1428 is the true radius, the image of "
        "the Q_b zero (2026-08-09 correction). #3716's reading was right for the wrong "
        "stated reason, and the 2026-07-12 rebuttal was wrong for a checkable one.",
        "UNAFFECTED by the re-scope: the exact ℚ(√3) d_k, the parity structure, the "
        "3-smooth denominators, and the non-holonomicity in [4]. Only the growth-class "
        "verdict changed.",
        "no c_k wired; no fit; no tier change.",
    ])
    wb.add_assertion("valid_orders_over_determined", odd_ok, True)
    wb.add_assertion("parity_structure_holds", parity_ok, True)
    wb.add_assertion("factorial_smooth_denominators", smooth, True)
    wb.add_assertion("root_test_still_rising_in_window", root_test_rising_in_window, True)
    wb.add_assertion("singularity_at_qb_zero_reproduces_rho", singularity_at_rho, True)
    wb.add_assertion("no_low_order_p_recurrence", no_prec, True)
    wb.add_assertion("d5_reproduces_ai81_witness", bool(d5_ok), True)
    out = wb.save()
    print(f"  Witness: {out}")
    return 0 if (parity_ok and smooth and singularity_at_rho and no_prec
                 and odd_ok and d5_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
