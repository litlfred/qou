#!/usr/bin/env python3
"""
Probe — the q-adic order of the n = 4 interleaving cross term (test T1 of the
2026-09-05 binding-gap survey, route B): is the one positive many-body signal
the corpus holds an "all orders in q" object, or an order-zero one?

THE QUESTION (docs/audits/2026-09-05-binding-gap-groupoids-derived-categories-
full-tower.md, §5 route B "Falsifiable test", §7 item 3).  The interleaved
n = 4 word s0 s1 s0 s2 s1 has Markov trace

    I(q) = z (z² + h z + h² z²),          the sequential product
    S(q) = z (h z + 1)²,                  and their difference
    Δ(q) = I − S = z (z² − h z − 1)       (QOU/MathlibExt/MarkovTraceInterleavedCrossTerm.lean,
                                           `interleaved_sub_sequential`; bean qou-kru4).

Does Δ vanish at q = 1 to STRICTLY higher order than S?  If yes, the cross
term lives in the "all orders in q" half of the 2026-09-03 owner ruling and
route B is where it belongs; if no, interleaving is an order-zero phenomenon
and route B's claim on b₃ is weakened.

THE ANSWER IS NO, and the order-zero term has a name.  At convention D
(z = q³/(q²+1), h = q − q⁻¹) everything is an explicit rational function:

    S = q³ (q⁴+1)² / (q²+1)³        I = q⁵ (q⁶+q²−1) / (q²+1)³
    Δ = −q³ (q⁴+q²+1) / (q²+1)³     = −q³ Φ₃(q) Φ₆(q) / Φ₄(q)³

with ν_{q−1}(S) = ν_{q−1}(I) = ν_{q−1}(Δ) = 0 and S(1) = 1/2, I(1) = 1/8,
Δ(1) = −3/8.  At q = 1 the Ocneanu trace with z = 1/2 on the group algebra
of S₄ is tr(w) = 2^{c(w) − 4}, c(w) the number of cycles of the underlying
permutation — i.e. the number of COMPONENTS of the braid closure.  The
interleaved word closes to a knot (c = 1) and the sequential word to a
three-component link (c = 3): the cross term at order zero is the difference
of two component counts.  It is word topology in the most classical sense,
exactly the attribution §7b of the survey reached from the Lean side
(ordering owns the degree-0 phenomenon).

What the q-deformation adds is measured, not guessed: the ℏ-expansion
(ℏ = 1 − q⁻¹, the corpus's parameter) of Δ, S, I and of the ratio I/S is
computed exactly to order 8, its radius of convergence is √2 (the nearest
poles are the Φ₄ zeros q = ±i, where ℏ = 1 ± i), and at the proton pin
(ℏ ≈ 0.099) the order-zero term carries the reported fraction of Δ(q₀).

The Habiro-ring half of route B is also settled as far as this word goes.
The NORMALISED traces have a pole of order 3 at Φ₄, so none of S, I, Δ is a
Laurent polynomial, let alone a Habiro element — but the pole is the
normalisation tr(1) = 1, i.e. division by [2]_q⁴, and the UNNORMALISED
quantum-trace cross term

    [2]_q⁴ · Δ = −(q²+1)(q⁴+q²+1)/q = −(q⁶ + 2q⁴ + 2q² + 1)/q

is a Laurent polynomial with simple zeros at Φ₃, Φ₄, Φ₆ and value −6 at
q = 1.  Its q-adic order at q = 1 is still zero.  (That the pole locus of the
normalised trace, q² = −1, is the locus where the H₂ Kähler ideal of
QOU/Hecke/H2KaehlerDegrees.lean is proper is recorded as a coincidence of
loci, not as a derived relation.)

SCOPE — scope-(a).  Everything here is about this one n = 4 word pair at
convention D.  No production number moves: the production word is monotone
(QOU/MathlibExt/MonotoneWordTraceFactorizes.lean), so no cross term enters
it.  Nothing is wired and nothing is fitted; the single evaluation at the
proton pin is a diagnostic of how much of Δ(q₀) is classical.

Arithmetic: sympy exact rational functions and integer synthetic division
for every valuation; mpmath at 50 dps for the one anchor evaluation, via
lambdify(..., "mpmath") on the exact expression.  No float64 anywhere.

Run: python3 -u computations/probes/interleaving_cross_term_q_adic_order_probe.py \\
       2>&1 | tee /tmp/interleaving_q_adic_order.log
"""
from __future__ import annotations

import os
import sys
import time

import mpmath as mp
import sympy as sp
from sympy.combinatorics import Permutation

# Path bootstrap FIRST, then the bridge (per _path_bridge's documented USAGE).
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import _path_bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

try:  # proton pin at 50 digits (owner directive 2026-08-07: proton is the default)
    from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
except Exception:  # pragma: no cover — bare container without the package path
    Q_50_DIGIT_STR = None

mp.mp.dps = 50
T0 = time.monotonic()
SERIES_ORDER = 8
N_STRANDS = 4


def log(msg: str) -> None:
    print(f"  [{time.monotonic() - T0:5.1f}s] {msg}", flush=True)


# ----------------------------------------------------------------------------
# exact valuation at q = 1 (integer synthetic division, as in
# qbeta_5two_masbaum_valuation_probe.py — no floats, no tolerance)
# ----------------------------------------------------------------------------
def valuation_at_one(coeffs):
    c = [int(x) for x in coeffs]
    v = 0
    while c and any(c):
        if sum(c) != 0:
            break
        desc = c[::-1]
        out, carry = [], 0
        for a in desc:
            carry += a
            out.append(carry)
        assert out[-1] == 0, "synthetic division left a remainder"
        c = out[:-1][::-1]
        v += 1
    return v


def poly_val_at_one(expr, q):
    """ν_{q−1} of a rational function: ν(num) − ν(den), each by synthetic
    division on the integer coefficient list (ascending powers)."""
    num, den = sp.fraction(sp.cancel(sp.together(expr)))
    pn, pd = sp.Poly(sp.expand(num), q), sp.Poly(sp.expand(den), q)
    return (valuation_at_one(pn.all_coeffs()[::-1])
            - valuation_at_one(pd.all_coeffs()[::-1]))


def cyclotomic_orders(expr, q, m_max=12):
    """Order of vanishing (negative = pole) of a rational function of q at a
    primitive m-th root of unity, for m = 1..m_max, by exact division by Φ_m."""
    num, den = sp.fraction(sp.cancel(sp.together(expr)))
    out = {}
    for m in range(1, m_max + 1):
        phi = sp.Poly(sp.cyclotomic_poly(m, q), q)
        v = 0
        for poly, sign in ((sp.Poly(sp.expand(num), q), +1),
                           (sp.Poly(sp.expand(den), q), -1)):
            p = poly
            while p.degree() >= phi.degree():
                quo, rem = sp.div(p, phi)
                if not rem.is_zero:
                    break
                p, v = quo, v + sign
        if v:
            out[m] = v
    return out


def hbar_series(expr, q, hb, order):
    """Exact Taylor coefficients of expr(q = 1/(1−ℏ)) in ℏ, orders 0..order."""
    e = sp.cancel(sp.together(expr.subs(q, 1 / (1 - hb))))
    s = sp.series(e, hb, 0, order + 1).removeO()
    return [sp.nsimplify(s.coeff(hb, k)) for k in range(order + 1)]


def main() -> int:
    print("=" * 76)
    print(" T1 — q-adic order of the n = 4 interleaving cross term (convention D)")
    print("=" * 76)

    q, z, h, hb = sp.symbols("q z h hbar")
    z_D = q ** 3 / (q ** 2 + 1)
    h_q = q - 1 / q

    # --- the three traces, first symbolic in (z, h), then at convention D ----
    I_zh = z * (z ** 2 + h * z + h ** 2 * z ** 2)
    S_zh = z * (h * z + 1) ** 2
    D_zh = sp.expand(I_zh - S_zh)
    lean_D = sp.expand(z * (z ** 2 - h * z - 1))
    chk_closed_zh = sp.simplify(D_zh - lean_D) == 0

    sub = {z: z_D, h: h_q}
    S = sp.cancel(sp.together(S_zh.subs(sub)))
    I = sp.cancel(sp.together(I_zh.subs(sub)))
    D = sp.cancel(sp.together(D_zh.subs(sub)))
    S_closed = q ** 3 * (q ** 4 + 1) ** 2 / (q ** 2 + 1) ** 3
    I_closed = q ** 5 * (q ** 6 + q ** 2 - 1) / (q ** 2 + 1) ** 3
    D_closed = -q ** 3 * (q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 3
    chk_closed_D = all(sp.simplify(a - b) == 0 for a, b in
                       ((S, S_closed), (I, I_closed), (D, D_closed)))
    log(f"closed forms: S = {sp.factor(S)}")
    log(f"              I = {sp.factor(I)}")
    log(f"              Δ = {sp.factor(D)}")

    # --- q-adic order at q = 1 ------------------------------------------------
    nu = {"S": poly_val_at_one(S, q), "I": poly_val_at_one(I, q),
          "Delta": poly_val_at_one(D, q)}
    at1 = {"S": S.subs(q, 1), "I": I.subs(q, 1), "Delta": D.subs(q, 1)}
    log(f"ν_(q−1):  S {nu['S']}   I {nu['I']}   Δ {nu['Delta']}")
    log(f"at q = 1: S {at1['S']}   I {at1['I']}   Δ {at1['Delta']}")
    chk_test_answer_no = (nu["Delta"] == 0 and nu["S"] == 0 and nu["I"] == 0)
    chk_values_at_one = (at1["S"] == sp.Rational(1, 2) and at1["I"] == sp.Rational(1, 8)
                         and at1["Delta"] == sp.Rational(-3, 8))
    # the order-zero cross term is a difference of component counts
    chk_nonzero_order0 = at1["Delta"] != 0

    # --- the classical name of the order-zero term: cycle counts --------------
    def perm_of_word(word):
        p = Permutation(list(range(N_STRANDS)))
        for i in word:
            p = p * Permutation(i, i + 1, size=N_STRANDS)
        return p
    cyc = {"interleaved": perm_of_word([0, 1, 0, 2, 1]).cycles,
           "sequential": perm_of_word([0, 0, 1, 1, 2]).cycles}
    classical = {k: sp.Rational(1, 2) ** (N_STRANDS - c) for k, c in cyc.items()}
    chk_cycle_count = (classical["interleaved"] == at1["I"]
                       and classical["sequential"] == at1["S"]
                       and cyc["interleaved"] == 1 and cyc["sequential"] == 3)
    log(f"q = 1 is the cycle-count trace 2^(c−4): c(interleaved) = {cyc['interleaved']} "
        f"→ {classical['interleaved']},  c(sequential) = {cyc['sequential']} → {classical['sequential']}")

    # --- cyclotomic (Habiro-relevant) structure -------------------------------
    cyc_orders = {k: cyclotomic_orders(e, q) for k, e in (("S", S), ("I", I), ("Delta", D))}
    log(f"orders at Φ_m (neg = pole):  S {cyc_orders['S']}  I {cyc_orders['I']}  Δ {cyc_orders['Delta']}")
    chk_phi4_pole = all(v.get(4) == -3 for v in cyc_orders.values())
    chk_delta_zeros = cyc_orders["Delta"].get(3) == 1 and cyc_orders["Delta"].get(6) == 1
    # the unnormalised quantum-trace cross term: multiply by [2]_q^4
    two_q = q + 1 / q
    D_unnorm = sp.cancel(sp.together(two_q ** N_STRANDS * D))
    D_unnorm_closed = -(q ** 6 + 2 * q ** 4 + 2 * q ** 2 + 1) / q
    chk_unnorm_laurent = (sp.simplify(D_unnorm - D_unnorm_closed) == 0
                          and sp.Poly(sp.expand(D_unnorm * q), q).domain == sp.ZZ)
    nu_unnorm = poly_val_at_one(D_unnorm, q)
    unnorm_orders = cyclotomic_orders(D_unnorm, q)
    log(f"[2]_q⁴·Δ = {sp.factor(D_unnorm)}   ν_(q−1) = {nu_unnorm}   value at 1 = {D_unnorm.subs(q, 1)}   Φ-orders {unnorm_orders}")
    chk_unnorm_order0 = nu_unnorm == 0 and D_unnorm.subs(q, 1) == -6

    # --- ℏ-expansion, exact, and its radius -----------------------------------
    ser = {k: hbar_series(e, q, hb, SERIES_ORDER)
           for k, e in (("S", S), ("I", I), ("Delta", D), ("ratio_I_over_S", I / S))}
    chk_series_consistent = all(ser["I"][k] - ser["S"][k] == ser["Delta"][k]
                                for k in range(SERIES_ORDER + 1))
    chk_series_order0 = (ser["Delta"][0] == sp.Rational(-3, 8)
                         and ser["ratio_I_over_S"][0] == sp.Rational(1, 4))
    # poles of Δ in ℏ: q = ±i  ⇒  ℏ = 1 − 1/q = 1 ± i, |ℏ| = √2; no pole at q = 0
    # (numerator carries q³) and none at q = ∞ (ℏ = 1) since Δ → −1 there.
    pole_hb = [sp.nsimplify(1 - 1 / r) for r in sp.roots(sp.Poly(q ** 2 + 1, q))]
    radius = min(sp.Abs(p) for p in pole_hb)
    chk_radius = sp.simplify(radius - sp.sqrt(2)) == 0
    log(f"ℏ-series of Δ: {[str(c) for c in ser['Delta']]}")
    log(f"ℏ-series of I/S: {[str(c) for c in ser['ratio_I_over_S']]}")
    log(f"radius of convergence in ℏ: {radius}")

    # --- anchor evaluation (proton pin, 50 dps, exact expression) -------------
    anchor = {}
    if Q_50_DIGIT_STR is not None:
        q0 = Q_MP
        fD = sp.lambdify(q, D, modules="mpmath")
        fS = sp.lambdify(q, S, modules="mpmath")
        fI = sp.lambdify(q, I, modules="mpmath")
        D0, S0, I0 = fD(q0), fS(q0), fI(q0)
        hb0 = 1 - 1 / q0
        order0_fraction = mp.mpf(-3) / 8 / D0
        # partial sums of the exact ℏ-series against the exact value
        partial = [sum(mp.mpf(sp.Rational(c).p) / mp.mpf(sp.Rational(c).q) * hb0 ** k
                       for k, c in enumerate(ser["Delta"][: n + 1]))
                   for n in range(SERIES_ORDER + 1)]
        resid = [abs(p - D0) for p in partial]
        anchor = {
            "q0": Q_50_DIGIT_STR,
            "hbar_q0": mp.nstr(hb0, 30),
            "S": mp.nstr(S0, 40), "I": mp.nstr(I0, 40), "Delta": mp.nstr(D0, 40),
            "ratio_I_over_S": mp.nstr(I0 / S0, 30),
            "extra_nats_q0": mp.nstr(-mp.log(I0 / S0), 30),
            "extra_nats_classical": "2·ln 2 = " + mp.nstr(2 * mp.log(2), 30),
            "order0_fraction_of_Delta": mp.nstr(order0_fraction, 30),
            "hbar_series_residual_by_order": [mp.nstr(r, 6) for r in resid],
        }
        chk_order0_dominates = order0_fraction > mp.mpf(1) / 2
        chk_series_converges = resid[-1] < resid[0] and resid[-1] < mp.mpf("1e-8")
        log(f"proton pin: ℏ = {anchor['hbar_q0'][:12]}…  Δ(q₀) = {anchor['Delta'][:14]}…  "
            f"order-0 fraction {anchor['order0_fraction_of_Delta'][:8]}…  "
            f"nats {anchor['extra_nats_q0'][:8]}… vs classical {mp.nstr(2 * mp.log(2), 6)}")
    else:
        chk_order0_dominates = chk_series_converges = None
        log("q_parameter not importable — anchor evaluation skipped; every exact check unaffected")

    checks = [
        ("closed form matches the Lean: I − S = z(z² − hz − 1)", chk_closed_zh),
        ("convention-D closed forms for S, I, Δ", chk_closed_D),
        ("T1 answer is NO: ν_(q−1)(Δ) = ν_(q−1)(S) = ν_(q−1)(I) = 0", chk_test_answer_no),
        ("S(1) = 1/2, I(1) = 1/8, Δ(1) = −3/8", chk_values_at_one),
        ("the cross term is nonzero at order zero", chk_nonzero_order0),
        ("q = 1 is the cycle-count trace: c = 1 (knot) vs c = 3 (3-component closure)", chk_cycle_count),
        ("all three normalised traces have a pole of order 3 at Φ₄ (q² = −1)", chk_phi4_pole),
        ("Δ has simple zeros at Φ₃ and Φ₆", chk_delta_zeros),
        ("[2]_q⁴·Δ is the Laurent polynomial −(q⁶+2q⁴+2q²+1)/q", chk_unnorm_laurent),
        ("unnormalised cross term: ν_(q−1) = 0, value −6 at q = 1", chk_unnorm_order0),
        ("ℏ-series of I − S equals ℏ-series of Δ to order 8", chk_series_consistent),
        ("ℏ-series leading terms: Δ → −3/8, I/S → 1/4", chk_series_order0),
        ("radius of convergence in ℏ is √2 (poles at q = ±i)", chk_radius),
    ]
    if chk_order0_dominates is not None:
        checks += [
            ("proton pin: the order-zero term carries more than half of Δ(q₀)", chk_order0_dominates),
            ("proton pin: exact ℏ-series partial sums converge to Δ(q₀)", chk_series_converges),
        ]

    print()
    ok = 0
    for name, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
        ok += bool(passed)
    print(f"\n  {ok}/{len(checks)} checks passed   ({time.monotonic() - T0:.1f}s)")

    # --- witness ---------------------------------------------------------------
    wb = WitnessBuilder("interleaving-cross-term-q-adic-order", engine="sympy",
                        _script_path=__file__)
    wb.set_description(
        "Test T1 of the 2026-09-05 binding-gap survey (route B): the q-adic order "
        "at q = 1 of the n = 4 interleaving cross term Δ = z(z² − hz − 1) against "
        "the sequential product S = z(hz+1)², at convention D. Answer NO: "
        "ν(Δ) = ν(S) = ν(I) = 0 with S(1) = 1/2, I(1) = 1/8, Δ(1) = −3/8 — at q = 1 "
        "the trace is the cycle-count trace 2^(c−4) and the cross term is the "
        "difference between a knot closure (c = 1) and a 3-component closure (c = 3). "
        "Interleaving is an order-zero, word-topology phenomenon; the q-deformation "
        "is an exact ℏ-series of radius √2 whose order-zero term carries the recorded "
        "fraction of Δ at the proton pin. The normalised traces have a triple pole at "
        "Φ₄ (the tr(1) = 1 normalisation, [2]_q⁴); the unnormalised cross term is the "
        "Laurent polynomial −(q⁶+2q⁴+2q²+1)/q with simple zeros at Φ₃, Φ₄, Φ₆. "
        "Exact sympy throughout; mpmath 50 dps for the single anchor evaluation. "
        "Scope (a), one word pair; nothing wired, nothing fitted.")
    wb.set_content_block("prop:markov-trace-axiomatic-closed-form")
    for name, passed in checks:
        wb.add_assertion(name.replace(" ", "_")[:80], computed="1" if passed else "0",
                         expected="1", tolerance="0.5", source="exact (sympy / integer)")
    wb.add_parameter("convention", "D: z = q^3/(q^2+1), h = q - 1/q")
    wb.add_parameter("words", {"interleaved": "s0 s1 s0 s2 s1", "sequential": "s0^2 s1^2 s2"})
    wb.add_parameter("series_variable", "hbar = 1 - 1/q")
    wb.add_parameter("series_order", SERIES_ORDER)
    if Q_50_DIGIT_STR is not None:
        wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_data("closed_forms", {"S": str(sp.factor(S)), "I": str(sp.factor(I)),
                                 "Delta": str(sp.factor(D)),
                                 "Delta_unnormalised": str(sp.factor(D_unnorm))})
    wb.add_data("valuation_at_q_equals_1", {**nu, "Delta_unnormalised": nu_unnorm})
    wb.add_data("value_at_q_equals_1", {k: str(v) for k, v in at1.items()})
    wb.add_data("cycle_counts", cyc)
    wb.add_data("cyclotomic_orders", {k: {str(m): v for m, v in d.items()}
                                      for k, d in {**cyc_orders,
                                                   "Delta_unnormalised": unnorm_orders}.items()})
    wb.add_data("hbar_series", {k: [str(c) for c in v] for k, v in ser.items()})
    wb.add_data("hbar_radius_of_convergence", str(radius))
    wb.add_data("anchor_evaluation", anchor)
    wb.add_data("verdict", (
        "T1: NO. The interleaving cross term has q-adic order 0 — the same as the "
        "sequential product — and its order-zero value −3/8 is the difference of "
        "two closure component counts. Route B's claim that the cross term is an "
        "'all orders in q' object is WEAKENED (scope (a): this word pair, convention "
        "D). The q-deformation of the cross term is real but perturbative on top of "
        "a classical term; the Habiro-ring reading applies only to the "
        "unnormalised trace, whose cross term is a Laurent polynomial."))
    wb.add_caveat("Scope (a): one n = 4 word pair at convention D. Says nothing about "
                  "whether a nucleus is an interleaved word class (qou-5vhf).")
    wb.add_caveat("The coincidence of the Φ₄ pole locus with the locus where the H₂ "
                  "Kähler ideal is proper (H2KaehlerDegrees.lean) is an observation, "
                  "not a derived relation.")
    out = wb.save()
    print(f"  witness -> {os.path.relpath(out, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))}")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
