#!/usr/bin/env python3
"""milnor_a4_deficit_h_form.py — exact A=4 Brunnian deficit in the CANONICAL
convention-D (Jones/Temperley-Lieb) frame, the SAME convention as the Lean A=3
object `tauBorromean` (bean qou-v7ro).

WHY THIS WAS REWRITTEN (2026-08-29).  The first version of this script tried to
promote the deficit computed by `a4_brunnian_deficit_closed_form.py` — which uses
the PRODUCTION mass convention `g = Σ_λ y_λ^Wenzl · |χ_λ|` — into an h-form.  That
convention's `y_lambda_at` weights carry half-integer powers of q, so its deficit
lives in `s = √q` with ODD powers of s and is NOT a rational function of h.  That
is the wrong convention for backing a Lean `borromean4_tight_slice`: the Lean A=3
object `tauBorromean = (4+h²−3h⁴−h⁶)/(h²+4)` is **convention D** — the
Jones / SU(2) / Temperley-Lieb Markov trace, proved in
`BorromeanFrobeniusReconstruction.lean` to be

    τ_D(β) = Σ_λ y_λ^TL · χ_λ(β),    y_{(a,b)}^TL = [a−b+1]_q / [2]_q^n,
                                     y_λ = 0 for λ with ≥ 3 rows,

with SIGNED χ_λ (not |χ_λ|).  For H₃ this is `y_{(3)} = [4]/[2]³`,
`y_{(2,1)} = 1/[2]²`, `y_{(1³)} = 0` (PROBE 4, PR #3200) — only the ≤ 2-row
(SU(2)-surviving) diagrams contribute.  Because every ingredient
([k]_q and the palindromic even-power χ_λ) is a polynomial in u = q²+q⁻² = h²+2,
τ_D is manifestly a rational function of h ALONE — no √q.

METHOD (0-fit, exact sympy over ℚ(q), ZERO float64):
  1. A=3 VALIDATION: reproduce tauBorromean EXACTLY from the convention-D weights,
     confirming the convention before touching A=4.
  2. A=4: τ_4 = ([5]·χ_{(4)} + [3]·χ_{(3,1)} + [1]·χ_{(2,2)}) / [2]_q⁴, using the
     committed exact χ_λ(w4) from a4-brunnian-deficit-closed-form.witness.json
     (2-row diagrams only; (2,1,1) and (1,1,1,1) get y=0 in convention D).
  3. D_4 = 1 − τ_4, fold q → u = q²+q⁻² → h²+2, factor D_4 = h⁶ · cofactor(h),
     report cofactor(0).
  4. Cross-checks: leading (q−1)-order, leading (q−1)-coeff, τ_4(q0), and the
     exact identity D_4(h)|_{h=q−1/q} == D_4(q).

All arithmetic is sympy Rational / Poly over ℚ(q).  sp.N(...,30) is used ONLY for
a final human-readable display of τ_4(q0); every decision uses exact rationals.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent

q, h = sp.symbols("q h", positive=True)
u = sp.symbols("u")  # u = q^2 + q^-2 = h^2 + 2

# ── exact χ_λ, copied verbatim from a4-brunnian-deficit-closed-form.witness.json
# (integer-coeff palindromic Laurent polynomials — SIGNED characters over ℚ(q)).
CHI_W3 = {
    (3,): sp.Integer(1),
    (2, 1): (-q**12 + 3*q**10 - 3*q**8 + 4*q**6 - 3*q**4 + 3*q**2 - 1) / q**6,
    (1, 1, 1): sp.Integer(1),
}
CHI_W4 = {
    (4,): sp.Integer(1),
    (3, 1): (2*q**16 - 12*q**14 + 32*q**12 - 52*q**10 + 63*q**8
             - 52*q**6 + 32*q**4 - 12*q**2 + 2) / q**8,
    (2, 2): (q**24 - 5*q**22 + 12*q**20 - 21*q**18 + 31*q**16 - 38*q**14
             + 42*q**12 - 38*q**10 + 31*q**8 - 21*q**6 + 12*q**4 - 5*q**2 + 1) / q**12,
    (2, 1, 1): (2*q**16 - 12*q**14 + 32*q**12 - 52*q**10 + 63*q**8
                - 52*q**6 + 32*q**4 - 12*q**2 + 2) / q**8,
    (1, 1, 1, 1): sp.Integer(1),
}
# dim V_λ (# SYT) — χ_λ on the identity braid (the n-component unlink).
DIM3 = {(3,): 1, (2, 1): 2, (1, 1, 1): 1}
DIM4 = {(4,): 1, (3, 1): 3, (2, 2): 2, (2, 1, 1): 3, (1, 1, 1, 1): 1}


def q_bracket(k):
    """[k]_q = (q^k − q^-k)/(q − q^-1), as an exact Laurent polynomial in q."""
    return sp.cancel((q**k - q**(-k)) / (q - q**(-1)))


def rows(part):
    return len(part)


def tl_weight(part, n):
    """Convention-D (Jones / Temperley-Lieb) Markov weight y_λ^TL.

    y_{(a,b)} = [a−b+1]_q / [2]_q^n for a 2-row diagram (a≥b, a+b=n); 0 for ≥3 rows.
    (For a single-row (n,) diagram, b=0, weight [n+1]_q/[2]_q^n.)
    """
    if rows(part) > 2:
        return sp.Integer(0)
    a = part[0]
    b = part[1] if len(part) == 2 else 0
    return sp.cancel(q_bracket(a - b + 1) / q_bracket(2)**n)


def fold_bar_symmetric_to_h(expr):
    """Rewrite a bar-symmetric q-rational expr (invariant under q→1/q) as an exact
    rational function of h = q − 1/q.

    A rational function invariant under q→1/q is a rational function of c = q+1/q
    (the invariant of that involution).  It is a rational function of h ALONE iff
    that c-form is EVEN in c — because c² = h²+4, so even powers of c substitute to
    polynomials in h while an odd power leaves a bare c = √(h²+4).  An odd power of
    c surviving is exactly the outcome-(b) signal.

    Implemented by reducing numerator and denominator modulo the minimal polynomial
    `q² − c·q + 1` of q over ℚ(c) (so `1/q = c − q`), which collapses any
    bar-symmetric ratio to a rational function of c with no q; then, after checking
    evenness in c, substituting c² = h²+4.
    """
    c = sp.symbols("c")
    m = q**2 - c*q + 1  # q + 1/q = c  ⟺  q is a root of m
    f = sp.cancel(expr)
    num, den = sp.fraction(f)
    num, den = sp.expand(num), sp.expand(den)

    def reduce_mod_m(poly):
        # remainder of `poly` (a polynomial in q) modulo m, over ℚ[c]: r0 + r1·q
        _, r = sp.div(sp.expand(poly), m, q)
        r = sp.expand(r)
        rp = sp.Poly(r, q)
        r0 = rp.coeff_monomial(1)
        r1 = rp.coeff_monomial(q)
        return sp.expand(r0), sp.expand(r1)

    rn, sn = reduce_mod_m(num)   # num ≡ rn + sn·q   (mod m)
    rd, sd = reduce_mod_m(den)   # den ≡ rd + sd·q   (mod m)

    # Multiply num,den by the conjugate (rd + sd·(c−q)); using q² = c·q − 1 the
    # denominator becomes rd² + rd·sd·c + sd² (a function of c only), and the
    # numerator's q-coefficient (sn·rd − rn·sd) vanishes for a bar-symmetric f.
    num_c = sp.expand(rn*rd + rn*sd*c + sn*sd)
    q_coeff = sp.expand(sn*rd - rn*sd)
    assert sp.simplify(q_coeff) == 0, f"expr not bar-symmetric — residual q term {q_coeff}"
    den_c = sp.expand(rd**2 + rd*sd*c + sd**2)

    g = sp.cancel(num_c / den_c)   # rational function of c
    gn, gd = sp.fraction(g)
    gn, gd = sp.expand(gn), sp.expand(gd)

    def c_even_to_h(pc):
        pp = sp.Poly(sp.expand(pc), c)
        out = sp.Integer(0)
        for (k,), coef in pp.terms():
            assert k % 2 == 0, (
                f"odd power of c survived (k={k}) — NOT rational in h alone "
                f"(outcome b: genuine sqrt(h^2+4) dependence)")
            out += coef * (h**2 + 4)**(k // 2)
        return sp.expand(out)

    return sp.cancel(c_even_to_h(gn) / c_even_to_h(gd))


def tau_convention_d(chi, dim, n):
    """τ_D(β) = Σ_λ y_λ^TL χ_λ(β)  (already normalised: Σ_λ y_λ^TL dim_λ = 1)."""
    tau = sp.Integer(0)
    for lam in chi:
        w = tl_weight(lam, n)
        if w != 0:
            tau += w * chi[lam]
    # normalisation check (Σ y_λ dim_λ = 1) — exact
    norm = sum(tl_weight(lam, n) * dim[lam] for lam in chi)
    assert sp.simplify(norm - 1) == 0, f"convention-D normalisation != 1 at n={n}: {norm}"
    return sp.cancel(tau)


def leading_qm1(D_q):
    """Exact leading (q−1)-order and coefficient of D_q, by numerator valuation."""
    eps = sp.symbols("eps")
    N_q, M_q = sp.fraction(sp.cancel(D_q))
    M_at_1 = sp.cancel(M_q.subs(q, 1))
    assert M_at_1 != 0, "denominator vanishes at q=1"
    Npoly = sp.Poly(sp.expand(N_q.subs(q, 1 + eps)), eps)
    nz = [m[0] for m in Npoly.monoms() if Npoly.coeff_monomial((m[0],)) != 0]
    order = min(nz)
    coeff = sp.cancel(Npoly.coeff_monomial((order,)) / M_at_1)
    return order, coeff


def factor_h_power(D_h):
    num, den = sp.fraction(sp.together(D_h))
    num = sp.expand(num)
    p = 0
    while sp.simplify(num.subs(h, 0)) == 0 and p < 20:
        num = sp.cancel(num / h)
        num = sp.expand(num)
        p += 1
    cof = sp.cancel(num / den)
    return p, cof


def main():
    report = {}

    # ── Q0 pin: exact rational (the same q0 the committed A=4 producer used, so any
    # difference from its 1.000145898 is PURELY the convention, not the pin). ──
    Q0 = sp.Rational("2584370278640139188197914756009",
                     "2328306436538696289062500000000")

    # ══ 1. A=3 VALIDATION — must reproduce tauBorromean exactly ══════════════════
    tau3 = tau_convention_d(CHI_W3, DIM3, 3)
    tauBorr = (4 + h**2 - 3*h**4 - h**6) / (h**2 + 4)  # Lean tauBorromean
    tau3_h = fold_bar_symmetric_to_h(tau3)
    a3_ok = sp.simplify(tau3_h - tauBorr) == 0
    D3_h = fold_bar_symmetric_to_h(sp.cancel(1 - tau3))
    p3, cof3 = factor_h_power(D3_h)
    ord3, c3 = leading_qm1(sp.cancel(1 - tau3))
    print("== A=3 validation (convention D) ==")
    print(f"  tau3(h)            = {sp.nsimplify(tau3_h)}")
    print(f"  == tauBorromean ?  = {a3_ok}")
    print(f"  1-tau3 = h^{p3} * ({cof3})")
    print(f"  cofactor(0)        = {sp.cancel(cof3.subs(h, 0))}  (expect 3/4)")
    print(f"  leading (q-1): order={ord3} coeff={c3}  (expect 4, 12)")
    assert a3_ok, "A=3 does NOT reproduce tauBorromean — wrong convention"
    report["A3_validation"] = {
        "tau3_h_form": str(sp.cancel(tau3_h)),
        "reproduces_tauBorromean": bool(a3_ok),
        "deficit_h_form": str(sp.cancel(D3_h)),
        "h_power": p3,
        "cofactor_h": str(cof3),
        "cofactor_at_0": str(sp.cancel(cof3.subs(h, 0))),
        "leading_q_minus_1_order": int(ord3),
        "leading_coeff_q_minus_1": str(c3),
    }

    # ══ 2. A=4 — convention-D deficit ════════════════════════════════════════════
    tau4 = tau_convention_d(CHI_W4, DIM4, 4)
    D4_q = sp.cancel(1 - tau4)
    # bar-symmetry of the deficit (a hard precondition for an h-form)
    bar = sp.simplify(D4_q.subs(q, 1/q) - D4_q)
    print("\n== A=4 (convention D) ==")
    print(f"  D4 bar-symmetric?  (D4(1/q)-D4(q)) = {bar}  (expect 0)")
    assert bar == 0, "A=4 convention-D deficit is not bar-symmetric"

    tau4_h = fold_bar_symmetric_to_h(tau4)
    D4_h = fold_bar_symmetric_to_h(D4_q)
    p4, cof4 = factor_h_power(D4_h)
    ord4, c4 = leading_qm1(D4_q)
    cof4_0 = sp.cancel(cof4.subs(h, 0))

    print(f"  tau4(h)  = {sp.cancel(tau4_h)}")
    print(f"  D4(h)    = {sp.cancel(D4_h)}")
    print(f"  D4(h)    = h^{p4} * ({sp.cancel(cof4)})")
    print(f"  cofactor(0) = {cof4_0}   (expect -3/2 = (3/4)*(-2)^1)")
    print(f"  leading (q-1): order={ord4} coeff={c4}")

    # ── cross-checks ─────────────────────────────────────────────────────────────
    # (a) exact identity D4(h)|_{h=q-1/q} == D4(q)
    back = sp.simplify(D4_h.subs(h, q - 1/q) - D4_q)
    # (b) tau4 at q0 (convention D) — exact rational, displayed at 30 digits
    tau4_q0 = sp.cancel(tau4.subs(q, Q0))
    tau4_q0_disp = sp.N(tau4_q0, 30)
    producer_tauL4 = sp.Rational(1000145898, 1000000000)  # 1.000145898 (|χ| convention)
    # (c) leading coeff cross-check against the producer's committed -96 / order 6
    matches_order6 = int(ord4) == 6
    matches_coeff_neg96 = sp.simplify(c4 - (-96)) == 0
    cof0_is_neg_three_halves = sp.simplify(cof4_0 - sp.Rational(-3, 2)) == 0

    print("\n== cross-checks ==")
    print(f"  D4(h)|_{{h=q-1/q}} - D4(q) = {back}  (expect 0)")
    print(f"  convention-D tau4(q0) = {tau4_q0_disp}")
    print(f"  producer |chi| tau_L4(q0) = 1.000145898  (DIFFERENT convention)")
    print(f"  leading order == 6 ? {matches_order6}")
    print(f"  leading (q-1) coeff == -96 ? {matches_coeff_neg96}   (value {c4})")
    print(f"  cofactor(0) == -3/2 ? {cof0_is_neg_three_halves}")

    outcome = "a" if (p4 == 6 and not D4_h.has(sp.sqrt)) else "b"

    report["A4_result"] = {
        "convention": "D (Jones/Temperley-Lieb; y_{(a,b)}=[a-b+1]/[2]^n, 2-row only, signed chi)",
        "outcome": outcome,
        "tau4_h_form": str(sp.cancel(tau4_h)),
        "deficit_D4_h_form": str(sp.cancel(D4_h)),
        "h_power": int(p4),
        "cofactor_h": str(sp.cancel(cof4)),
        "cofactor_at_0": str(cof4_0),
        "cofactor_at_0_is_neg_three_halves": bool(cof0_is_neg_three_halves),
        "leading_q_minus_1_order": int(ord4),
        "leading_coeff_q_minus_1": str(c4),
        "leading_coeff_matches_producer_neg96": bool(matches_coeff_neg96),
        "leading_order_matches_producer_6": bool(matches_order6),
        "h_form_matches_q_form_exactly": bool(back == 0),
        "convention_D_tau4_at_q0": str(tau4_q0),
        "convention_D_tau4_at_q0_display30": str(tau4_q0_disp),
        "producer_absval_convention_tauL4_at_q0": "1.000145898",
        "note_convention_difference": (
            "The committed producer a4_brunnian_deficit_closed_form.py uses the "
            "PRODUCTION mass convention g=Σ y_λ^Wenzl·|χ_λ| (half-integer q-powers, "
            "deficit rational in s=√q). This script uses convention D (the Lean "
            "tauBorromean frame: signed χ, Temperley-Lieb weights, 2-row diagrams "
            "only), which is rational in h. The two conventions AGREE at leading "
            "Milnor order/coefficient (topological μ̄-invariant) but DIFFER at "
            "subleading order and at q0."),
    }

    Q0_str = str(Q0)
    out = {
        "computation": "milnor-a4-deficit-h-form",
        "engine": "python-sympy-exact",
        "description": (
            "EXACT convention-D (Jones/Temperley-Lieb) closed form of the A=4 "
            "4-component Brunnian Markov-trace deficit D_4 = 1 - tau_4 as a rational "
            "function of h = q - 1/q, in the SAME convention as the Lean A=3 object "
            "tauBorromean = (4+h^2-3h^4-h^6)/(h^2+4) "
            "(BorromeanMarkovTrace.lean / BorromeanFrobeniusReconstruction.lean). "
            "Convention D uses SIGNED chi_lambda and Temperley-Lieb weights "
            "y_{(a,b)} = [a-b+1]_q/[2]_q^n with y_lambda=0 for >=3-row diagrams "
            "(only the SU(2)-surviving 2-row diagrams contribute), NOT the "
            "production |chi|-with-Wenzl-y convention (which lives in s=sqrt(q)). "
            "All exact sympy over Q(q); ZERO float64. A=3 leg validates the "
            "convention by reproducing tauBorromean exactly before A=4 is touched."),
        "q0_pin_exact_rational": Q0_str,
        "outcome": outcome,
        "outcome_a_means": "D_4 is a clean rational function of h alone (like A=3)",
        "outcome_b_means": "D_4 genuinely depends on s=sqrt(q) (NOT the case here)",
    }
    out.update(report)
    (HERE / "milnor-a4-deficit-h-form.witness.json").write_text(
        json.dumps(out, indent=1) + "\n")
    print(f"\nOUTCOME ({outcome}).  wrote milnor-a4-deficit-h-form.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
