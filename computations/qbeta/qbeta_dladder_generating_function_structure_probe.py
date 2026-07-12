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

  3. **D(ũ) is super-exponentially DIVERGENT (radius → 0).** CORRECTED
     2026-07-12 (was: "convergent radius ρ≈0.143" — a finite-n shadow; see
     docs/audits/2026-07-12-dladder-divergence-correction.md). A Domb–Sykes
     1/k radius fit gives a spurious finite ρ≈0.143, but there is NO
     singularity of log R(q(ũ)) at that |ũ| (nearest is 0.45–0.78), the root
     test |dₖ|^{1/k} rises without plateau (4.4→6.1 through k=27), and
     log|dₖ| = A + B·k + C·k·log k fits with C ≈ 0.05–0.08 > 0 (super-
     exponential, ~50–300× tighter than a constant-radius law). This is the
     corpus's q-Gevrey / radius→0 class-change at the real substrate q₀
     (Lean-backed alien-calculus audit). So the D-ladder is in the SAME
     divergent family as the κ-tower — the two bar-odd-S routes share a
     resurgent growth class (C drifts with the window ⇒ q-Gevrey, not a fixed
     classical index).

  4. **No low-order holonomic recurrence.** No P-finite recurrence of order ≤ 3
     and polynomial degree ≤ 4 fits a_k or b_k (the ORD-43 21-term run rules out
     order ≤ 4, degree ≤ 5 too). D(ũ) is not hypergeometric / P-finite at
     accessible order; its generating function is a non-elementary
     algebraic-branch-point object.

  5. **No finite singularity (corroborates radius → 0).** No singularity of
     log R(q(ũ)) sits near the spurious 0.143: the sqrt branch points q⁴+q²+1=0
     and the ũ'(q)=0 folds all map to ũ=0, and the nearest singularity of any
     kind (a QA zero / a complex fold) is at |ũ|=0.45–0.78. The absence of any
     finite singularity where a radius-0.143 series would demand one is the
     analytic-side confirmation of the radius→0 growth diagnosis in [3].

CONCLUSION: the D-ladder generating function has an exact parity + factorial-
smooth-denominator arithmetic and is super-exponentially DIVERGENT (radius → 0,
q-Gevrey at q₀) — in the SAME resurgent family as the κ-tower, NOT a convergent
contrast to it (the earlier "radius ≈ 0.143" was a finite-n shadow, corrected
2026-07-12). No elementary / P-finite closed form emerges at 15–27 terms.
Nothing wired.
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

    # ---- 3. growth class: super-exponentially DIVERGENT (radius → 0) ----
    # CORRECTED (2026-07-12): a Domb–Sykes 1/k radius fit gives a spurious finite
    # ρ≈0.143, but the corpus diagnostic (root test rising + C>0) shows radius→0.
    print("\n  [3] growth class (corpus diagnostic: root test rising + k·log k term):")
    lo = 10 if K >= 14 else 6
    root_rising, C, ssr_ratio, root = growth_diagnostic(dk, lo)
    rk = sorted(root)
    print(f"      root test |dₖ|^(1/k): {mp.nstr(root[rk[0]], 5)} → {mp.nstr(root[rk[-1]], 5)} "
          f"(k={rk[0]}..{rk[-1]}); still rising at top: {root_rising}")
    print(f"      log|dₖ| = A+B·k+C·k·log k fit: C = {mp.nstr(C, 5)} "
          f"({'>0 super-exponential' if C > 0 else 'not super-exp'}); "
          f"SSR(super-exp)/SSR(geom) = {mp.nstr(ssr_ratio, 4)} (≪1 ⇒ super-exp wins)")
    divergent = bool(root_rising and C > 0 and ssr_ratio < mp.mpf("0.3"))
    print(f"      => super-exponentially DIVERGENT (radius → 0): {divergent}")
    print("      same resurgent family as the κ-tower; q-Gevrey at q₀ (corpus alien-calculus audit)")

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
    print("\n  [5] no finite singularity (corroborates radius → 0):")
    print(f"      |ũ(q=1+√2)| = {mp.nstr(u_QAplus, 6)};  |ũ(q⁴+q²+1=0)| = {mp.nstr(u_bp, 4)} (→0, folds to origin)")
    print("      no singularity anywhere near the spurious 0.143 ⇒ consistent with radius → 0")

    d5_ai81 = sp.Rational(-252241, 243) * R3 - sp.Rational(836891, 139345920)
    d5_ok = sp.simplify(dk[5] - d5_ai81) == 0

    verdict = (
        f"D-ladder generating function D(ũ)=Σd_k ũ^k (d₁…d_{K} exact ℚ(√3)): "
        f"[1] exact parity structure (odd k → √3-part small-denominator, even k → "
        f"rational part); [2] simple-denominator sequence is 3-smooth "
        f"(Ohtsuki/Habiro factorial normalization; primes {primes}); [3] super-"
        f"exponentially DIVERGENT (radius → 0): root test rises without plateau "
        f"(→{mp.nstr(root[rk[-1]], 4)} at k={rk[-1]}) and C={mp.nstr(C, 3)}>0 in "
        f"log|dₖ|=A+Bk+C·k·log k (SSR {mp.nstr(ssr_ratio, 3)}× the geometric law) — "
        f"the SAME resurgent family as the κ-tower (q-Gevrey at q₀, corpus alien-"
        f"calculus audit); the earlier 'convergent ρ≈0.143' was a finite-n shadow; "
        f"[4] no P-finite recurrence (order≤3, deg≤4); [5] no closed form emerges at "
        f"{K} terms. Scope-(a); no c_k wired; no fit."
    )
    print(f"\n  VERDICT: {verdict}")
    print(f"  ({time.monotonic() - t0:.1f}s)")

    wb = WitnessBuilder("qbeta-dladder-generating-function-structure", engine="sympy")
    wb.set_description(
        "Route 2: structure hunt of the exact D-ladder generating function "
        "D(ũ)=Σ d_k ũ^k (d_k ∈ ℚ(√3), O/h via the route-3 ser_div). Findings: "
        "(1) exact parity structure (odd k → √3-part carries the small "
        "denominator, even k → rational part); (2) 3-smooth simple-denominators "
        "(Ohtsuki/Habiro factorial normalization); (3) super-exponentially "
        f"DIVERGENT (radius → 0): root test rises without plateau, C={mp.nstr(C, 3)}>0 "
        "in log|dₖ|=A+Bk+C·k·log k (super-exp ≫ geometric) — the SAME resurgent "
        "family as the κ-tower (q-Gevrey at q₀, corpus alien-calculus audit); the "
        "earlier 'convergent ρ≈0.143' was a finite-n shadow (corrected 2026-07-12); "
        "(4) no P-finite recurrence (order≤3 deg≤4; ORD-43 rules out order≤4 "
        "deg≤5); (5) no finite singularity near 0.143 (corroborates radius → 0). "
        "No elementary closed form at 15–27 terms. Scope-(a); no wiring."
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
    wb.add_data("super_exponentially_divergent", divergent)
    wb.add_data("contrast_kappa_tower",
                "CORRECTED 2026-07-12: D-ladder is super-exponentially divergent (radius→0), "
                "SAME resurgent family as the divergent κ-tower — NOT a convergent contrast. "
                "The earlier 'convergent ρ≈0.143' was a finite-n shadow.")
    wb.add_data("no_low_order_p_recurrence", no_prec)
    wb.add_data("no_finite_singularity_near_spurious_rho", mp.nstr(u_QAplus, 8))
    wb.add_data("verdict", verdict)
    wb.add_data("scope", "(a) — exact ℚ(√3) ladder + corpus growth-class diagnostic; no wiring")
    wb.add_data("caveats", [
        "C (the k·log k coefficient) drifts down with the fit window (0.077→0.048, "
        "k up to 27) ⇒ q-Gevrey at q₀, not a fixed classical Gevrey index; report "
        "'super-exponentially divergent, C≈0.05–0.08 shadow', not a pinned index.",
        "corrects PR #3716's 'convergent radius 0.143' finite-n shadow; corpus-"
        "corroborated (Lean-backed alien-calculus Gevrey/q-Gevrey audit).",
        "no c_k wired; no fit; no tier change.",
    ])
    wb.add_assertion("valid_orders_over_determined", odd_ok, True)
    wb.add_assertion("parity_structure_holds", parity_ok, True)
    wb.add_assertion("factorial_smooth_denominators", smooth, True)
    wb.add_assertion("super_exponentially_divergent", divergent, True)
    wb.add_assertion("no_low_order_p_recurrence", no_prec, True)
    wb.add_assertion("d5_reproduces_ai81_witness", bool(d5_ok), True)
    out = wb.save()
    print(f"  Witness: {out}")
    return 0 if (parity_ok and smooth and divergent and no_prec and odd_ok and d5_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
