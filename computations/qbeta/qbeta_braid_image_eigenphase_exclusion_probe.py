#!/usr/bin/env python3
"""No braid-image transfer matrix carries the Q_β ladder phase — in ANY convention.

Bean `qou-cds1` (tranche S1).  This is the **formalize-first** step the bean's
Discipline section demands, run before any numerical re-fit.  It proposes no
`c_k`, runs no extractor, and fits nothing.

## Where this sits

The bean's own record already narrows S1 to one residual:

  * `QOU.BraidKnot.Q_beta_categorical_ofPhase_tail_common` (corpus, sorry-free)
    — `z` reaches the ladder at exactly one place, the N=1 eigenphase `α`, so
    the N=2..5 tail is phase-blind.  `c₂ … c₅` do **not** need re-deriving.
  * `qbeta_ladder_required_phase_probe.py` — the class *"α = (z−1)h/2 with `z` a
    convention parameter"* is pruned for D: the required phase sits in a window
    of half-width ≈1.09e-5 rad and `z_D` misses by ≈1.19e-2 rad.
  * `QOU.QBeta.EigenphaseCarrier` — the Lean class that was supposed to carry
    the spectral identification of `α` is **vacuous**, so `α` is asserted in the
    C frame and derived in neither.  That file leaves a trichotomy: a transfer
    matrix `M` with spectrum `{e^{±iα}}` is either (1) in the braid image,
    (2) arbitrary — circular, or (3) a holonomy of an independently-defined
    connection (the KZ / Kohno–Drinfeld route).  It calls branch (1) excluded
    *by transcendence of `2cos((z−1)h/2)` over `ℚ(q,z)`* — an assertion carried
    in a docstring, not proved.

**This probe replaces that transcendence assertion with an elementary
boundedness argument, and in doing so widens it from C to every convention at
once.**  The exclusion never reads `z`'s formula; it reads only that `q ↦ α(q)`
is non-constant.

## The constraint

Work in the substrate variable `s = √q`, so both conventions are rational:

    z_C(s) = s/(s²+1)          z_D(s) = s⁶/(s⁴+1)          h(s) = s² − s⁻²
    α_X(s) = (z_X(s) − 1)·h(s)/2

Suppose `M` is the image of a braid word `w ∈ B₃` in the 2-dimensional irrep
`V_(2,1)` of `H₃(q)`, and suppose its spectrum is `{e^{+iα}, e^{−iα}}`.  Then

    tr M = 2 cos α(s)   and   det M = 1.

Two facts about the braid image, both verified exactly below:

  A. `det ρ(σ_i) = −1` **identically in q** (assertion 2), so `det ρ(w) = ±1`
     is fixed by the exponent sum of `w` and carries no substrate dependence.
  B. `tr ρ(w)` is a **Laurent polynomial in s with integer coefficients**
     (assertion 4, spot-checked over every word of length ≤ 5).

Now the kill.  `|2 cos α(s)| ≤ 2` for every `s`.  A Laurent polynomial bounded
on `(0,∞)` is constant — its top coefficient dies at `s → ∞` and its bottom
coefficient at `s → 0⁺`.  So `tr ρ(w) = 2 cos α(s)` forces `cos α` constant on
the substrate branch, hence (α continuous) `α` constant.  But `α_C` and `α_D`
are both non-constant (assertions 5, 6) — indeed both are *unbounded*, `α_C`
below and `α_D` above (assertions 8–10).

**Therefore no braid-image `M` has the ladder's eigenphase, in either
convention.**  Scope-(b) — a structural exclusion citing a proved invariant
(boundedness of `cos` against unboundedness of a non-constant Laurent
polynomial), not a scope-(a) numerical miss.  The Lean twin is
`QOU/QBeta/BraidImageEigenphaseExclusion.lean`.

## What this does NOT do

It does **not** derive `α`, in any convention, and it does **not** state a
D-frame ladder.  It closes branch (1) of the trichotomy *for every convention
simultaneously* — which is the part that bears on S1: re-picking `z` cannot
repair the D-frame ladder inside the braid picture.  Branch (3), the KZ /
Kohno–Drinfeld holonomy route, is untouched and remains the only place a
derivation of `α` can live.  Branch (2) remains circular.

**It closes the *character* case, not the *eigenvalue-pair* case.**  Branch (1)
as `EigenphaseCarrierVacuity` states it is a `2 × 2` matrix on `V_(2,1)` with
`trace = 2cos α` and `det = 1`, and that is what is excluded.  Were `α` instead
**one** eigenphase among several of a *larger* braid-image matrix, `2cos α`
would be a sum of two eigenvalues — an **algebraic** function of `q`, not a
Laurent polynomial — and boundedness does not extend, since an algebraic
function can be bounded on `(0,∞)` and non-constant (`q/(q+1)`).  That sub-case
still needs the transcendence argument.  Net: one unproved corpus assertion
becomes *(proved half)* + *(still assumed half)*, with the boundary named.

Assertion 3 makes the failure concrete rather than merely asymptotic: the
canonical single-wrap candidate `ρ(σ₁σ₂)` has `det = 1` and `tr = −1`
*identically in q*, i.e. eigenphase `2π/3` for every substrate value — while
`α_C(q₀) ≈ −0.0523`.  A q-independent phase cannot be a ladder rung.

## Method

Exact symbolic ℚ(s) / ℚ(q) via sympy and exact `Fraction` arithmetic; the one
substrate evaluation (assertion 12) is mpmath at 60 dps from the 50-digit
proton-pin string.  No float64 anywhere, per AGENTS.md §"PROBES ARE NOT
EXEMPT".
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction

import sympy as sp

s = sp.symbols("s", positive=True)  # substrate variable, q = s²
q = sp.symbols("q", positive=True)


# ── The 2-dimensional irrep V_(2,1) of H₃(q) ─────────────────────────────────
# Hecke normalisation: σ_i has eigenvalues {q, −q⁻¹}, i.e.
#     σ_i² = (q − q⁻¹)·σ_i + 1                      (the corpus §7a relation)
# This is the reduced Burau representation at t = q⁻², rescaled by q.

def sigma1(qq):
    return sp.Matrix([[-1 / qq, qq], [0, qq]])


def sigma2(qq):
    return sp.Matrix([[qq, 0], [1 / qq, -1 / qq]])


def word_matrix(word, qq):
    """Image of a word in σ₁^{±1}, σ₂^{±1}; `word` is a list of ±1, ±2."""
    M = sp.eye(2)
    inv = {1: sigma1(qq).inv(), 2: sigma2(qq).inv()}
    pos = {1: sigma1(qq), 2: sigma2(qq)}
    for g in word:
        M = M * (pos[abs(g)] if g > 0 else inv[abs(g)])
    return sp.simplify(M)


# ── Markov parameters and the ladder phase, in the substrate variable s ──────

def z_C_s(ss):
    """Convention C: z = √q/(q+1)  →  s/(s²+1)."""
    return ss / (ss ** 2 + 1)


def z_D_s(ss):
    """Convention D (canonical, owner ruling 2026-08-15): z = q³/(q²+1)  →  s⁶/(s⁴+1)."""
    return ss ** 6 / (ss ** 4 + 1)


def h_s(ss):
    """h = q − q⁻¹  →  s² − s⁻²."""
    return ss ** 2 - 1 / ss ** 2


def alpha_s(zfun, ss):
    """The asserted ladder eigenphase α = (z − 1)·h/2."""
    return (zfun(ss) - 1) * h_s(ss) / 2


def alpha_exact(zfun, s_rat: Fraction) -> Fraction:
    """α at an exact rational s, in exact `Fraction` arithmetic."""
    z = zfun(sp.Rational(s_rat.numerator, s_rat.denominator))
    hh = h_s(sp.Rational(s_rat.numerator, s_rat.denominator))
    val = sp.nsimplify(sp.cancel((z - 1) * hh / 2))
    r = sp.Rational(val)
    return Fraction(int(r.p), int(r.q))


def main() -> int:
    failures: list[str] = []

    def check(name: str, ok: bool, detail: str) -> None:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        if not ok:
            failures.append(name)

    print("Assertions (exact symbolic / exact rational; one 60-dps mpmath readout):")

    # ---- 1. The rep is the 2-dim irrep of H₃(q): braid + Hecke relations. ----
    s1, s2 = sigma1(q), sigma2(q)
    braid = sp.simplify(s1 * s2 * s1 - s2 * s1 * s2)
    hecke1 = sp.simplify(s1 * s1 - (q - 1 / q) * s1 - sp.eye(2))
    hecke2 = sp.simplify(s2 * s2 - (q - 1 / q) * s2 - sp.eye(2))
    check(
        "1. braid relation and Hecke relation hold identically in q",
        braid == sp.zeros(2, 2) and hecke1 == sp.zeros(2, 2) and hecke2 == sp.zeros(2, 2),
        "sigma1 sigma2 sigma1 = sigma2 sigma1 sigma2 and sigma_i^2 = (q-1/q) sigma_i + 1",
    )

    # ---- 2. det ρ(σ_i) = −1, identically in q. ----
    d1 = sp.simplify(s1.det())
    d2 = sp.simplify(s2.det())
    check(
        "2. det rho(sigma_i) = -1, q-independently",
        d1 == -1 and d2 == -1,
        f"det sigma1 = {d1}, det sigma2 = {d2}  (so det rho(w) = (-1)^(exponent sum))",
    )

    # ---- 3. The canonical single-wrap candidate is q-INDEPENDENT. ----
    M12 = word_matrix([1, 2], q)
    tr12 = sp.simplify(M12.trace())
    det12 = sp.simplify(M12.det())
    check(
        "3. rho(sigma1 sigma2) has det 1 and trace -1, identically in q",
        det12 == 1 and tr12 == -1,
        f"det = {det12}, trace = {tr12}  =>  eigenphase 2*pi/3 for EVERY substrate value",
    )

    # ---- 4. Braid-word characters are Laurent polynomials in q (spot-check). --
    # tr rho(w) in Z[q, q^-1] for every word of length <= 5 over {+-1, +-2}.
    bad = []
    gens = [1, -1, 2, -2]
    for L in range(1, 6):
        for w in itertools.product(gens, repeat=L):
            tr = sp.cancel(sp.together(word_matrix(list(w), q).trace()))
            num, den = sp.fraction(tr)
            # Laurent in q  <=>  denominator is a monomial q^k (up to sign),
            # and the numerator is a polynomial with integer coefficients.
            den_poly = sp.Poly(sp.expand(den), q)
            num_poly = sp.Poly(sp.expand(num), q)
            is_monomial = len(den_poly.monoms()) == 1
            int_coeffs = all(c.is_Integer for c in num_poly.all_coeffs()) and \
                all(c.is_Integer for c in den_poly.all_coeffs())
            if not (is_monomial and int_coeffs):
                bad.append((w, tr))
    check(
        "4. every braid word of length <= 5 has trace in Z[q, q^-1]",
        not bad,
        f"checked {sum(4 ** L for L in range(1, 6))} words; offenders: {len(bad)}",
    )

    # ---- 5/6. α_C and α_D are NON-CONSTANT (exact rational witnesses). ----
    aC2, aC3 = alpha_exact(z_C_s, Fraction(2)), alpha_exact(z_C_s, Fraction(3))
    aD2, aD3 = alpha_exact(z_D_s, Fraction(2)), alpha_exact(z_D_s, Fraction(3))
    check(
        "5. alpha_C is non-constant",
        aC2 != aC3,
        f"alpha_C(s=2) = {aC2}, alpha_C(s=3) = {aC3}",
    )
    check(
        "6. alpha_D is non-constant",
        aD2 != aD3,
        f"alpha_D(s=2) = {aD2}, alpha_D(s=3) = {aD3}",
    )

    # ---- 7. z_C <= 1/2 on the whole positive branch (the C unboundedness key). -
    gap = sp.cancel(sp.Rational(1, 2) - z_C_s(s))
    gap_target = sp.cancel((s - 1) ** 2 / (2 * (s ** 2 + 1)))
    check(
        "7. 1/2 - z_C(s) = (s-1)^2 / (2(s^2+1)) >= 0 for all s > 0",
        sp.simplify(gap - gap_target) == 0,
        f"1/2 - z_C = {sp.factor(gap)}",
    )

    # ---- 8. Hence α_C(s) <= -(s^2 - s^-2)/4 for s >= 1 — exact identity. ----
    lhs = sp.cancel(alpha_s(z_C_s, s) + h_s(s) / 4)
    rhs = sp.cancel((z_C_s(s) - sp.Rational(1, 2)) * h_s(s) / 2)
    check(
        "8. alpha_C + h/4 = (z_C - 1/2)*h/2, which is <= 0 for s >= 1",
        sp.simplify(lhs - rhs) == 0,
        "so alpha_C(s) <= -(s^2 - s^-2)/4 -> -infinity  (unbounded BELOW)",
    )

    # ---- 9. α_C passes below -4π by s = 10 (exact rational vs exact π). ----
    aC10 = alpha_exact(z_C_s, Fraction(10))
    below = sp.Rational(aC10.numerator, aC10.denominator) < -4 * sp.pi
    check(
        "9. alpha_C(s=10) < -4*pi  (so cos(alpha_C) attains +1 and -1 on [1,10])",
        bool(below),
        f"alpha_C(10) = {aC10} = {float(aC10):.4f}",
    )

    # ---- 10. α_D passes above +4π by s = 10 (unbounded ABOVE). ----
    aD10 = alpha_exact(z_D_s, Fraction(10))
    above = sp.Rational(aD10.numerator, aD10.denominator) > 4 * sp.pi
    check(
        "10. alpha_D(s=10) > 4*pi  (unbounded ABOVE; -alpha_D is unbounded below)",
        bool(above),
        f"alpha_D(10) = {aD10} = {float(aD10):.4f}",
    )

    # ---- 11. The rational-normalisation loophole is closed by det M = 1. ------
    # Objection to the argument above: a *normalised* character (divided by a
    # q-integer, as Markov normalisations routinely are) is a rational function,
    # and a bounded rational function need NOT be constant -- e.g. 1/(1+q^2).
    # So the boundedness kill would not apply.
    #
    # It does apply, because the unimodular-spectrum requirement det M = 1 pins
    # the normalisation. If M = c*rho(w) for a real scalar c, then
    #     det M = c^2 * det rho(w) = c^2 * (-1)^{e(w)},
    # so det M = 1 forces e(w) EVEN and c = +-1. No q-dependent normalisation
    # survives, and tr M = +- tr rho(w) is a Laurent polynomial after all.
    c = sp.symbols("c", real=True)
    w_odd = [1, 2, 1]  # exponent sum 3
    det_odd = sp.simplify((c * word_matrix(w_odd, q)).det())
    sols_odd = sp.solve(sp.Eq(det_odd, 1), c)
    w_even = [1, 2]  # exponent sum 2
    det_even = sp.simplify((c * word_matrix(w_even, q)).det())
    sols_even = sorted(sp.solve(sp.Eq(det_even, 1), c), key=str)
    check(
        "11. det M = 1 pins any scalar normalisation to c = +-1 (no rational escape)",
        sols_odd == [] and sols_even == [-1, 1],
        f"det(c*rho(s1 s2 s1)) = {det_odd} = 1 has real solutions {sols_odd}; "
        f"det(c*rho(s1 s2)) = {det_even} = 1 has {sols_even}",
    )

    # ---- 12. The concrete miss at the substrate anchor (60 dps, no float64). --
    from mpmath import mp, mpf, cos as mpcos, sqrt as mpsqrt

    mp.dps = 60
    from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # proton pin (owner default)

    q0 = Q_MP
    s0 = mpsqrt(q0)
    hq0 = q0 - 1 / q0
    zC0 = s0 / (q0 + 1)
    zD0 = q0 ** 3 / (q0 ** 2 + 1)
    aC0 = (zC0 - 1) * hq0 / 2
    aD0 = (zD0 - 1) * hq0 / 2
    twocosC = 2 * mpcos(aC0)
    twocosD = 2 * mpcos(aD0)
    check(
        "12. neither 2cos(alpha) matches the braid value -1 at the proton pin",
        twocosC != mpf(-1) and twocosD != mpf(-1),
        f"2cos(alpha_C(q0)) = {mp.nstr(twocosC, 20)}, "
        f"2cos(alpha_D(q0)) = {mp.nstr(twocosD, 20)}, braid tr rho(s1 s2) = -1",
    )

    print()
    if failures:
        print(f"FAILED {len(failures)}/12: {', '.join(failures)}")
        return 1
    print("12/12 assertions hold.")
    print()
    print("CONSEQUENCE (scope-(b), structural exclusion):")
    print("  A braid-image transfer matrix has a Laurent-polynomial character and a")
    print("  q-independent determinant. A Laurent polynomial bounded by 2 on (0,inf)")
    print("  is constant, so any braid-image realisation forces the ladder eigenphase")
    print("  to be CONSTANT in the substrate. alpha_C and alpha_D are both non-constant")
    print("  -- indeed unbounded, C below and D above. So branch (1) of the")
    print("  EigenphaseCarrierVacuity trichotomy is closed for EVERY convention, not")
    print("  only for C, and re-picking z cannot repair the D-frame ladder inside the")
    print("  braid picture. No D-frame c_k is proposed here; -974 remains a")
    print("  sensitivity measurement. Branch (3) (KZ / Kohno-Drinfeld holonomy) is")
    print("  untouched and is still the only place a derivation of alpha can live.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
