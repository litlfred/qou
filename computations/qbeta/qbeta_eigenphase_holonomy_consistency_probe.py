#!/usr/bin/env python3
"""Is the ladder phase holonomy-shaped?  A second-order test, and what discriminates.

Bean `qou-pdix`, branch 3 of the route-5 trichotomy.

## Why this test

`QOU.QBeta.EigenphaseCarrier` §3 establishes that a derivation of the ladder
phase `α` can only live in one place: an exponential/holonomy of an
independently-defined connection whose monodromy reproduces the Hecke braiding.
Branch 1 (`α` as a braid-word character) is excluded by rationality; branch 2
(`α` from an arbitrary matrix) is circular.

Before building such a connection, ask a cheap falsifiable question: **does `α`
even look like a holonomy angle?**

The Kohno–Drinfeld parametrisation fixes the scale.  The braiding is
`P·exp(ħt/2)` with `t` of eigenvalues `±1`, which matches the Hecke eigenvalues
`{q, −q⁻¹}` exactly when `q = e^{ħ/2}`, i.e. **`ħ = 2 ln q`**.  A holonomy angle
is then a multiple of `ħ`, i.e. of `ln q` — so the test is whether `α` agrees
with `c·ln q` for a *single* constant `c`.

**The scale is not free.**  `c` is fixed by the `O(t)` coefficient at `q = 1+t`.
Every higher order is then a genuine prediction that can fail.

## Result

    c·ln q  series:   t¹: c      t²: −c/2    t³: c/3

    α_C = (z_C−1)h/2  t¹: −1/2  ⇒ c = −1/2
                      t²: predicted 1/4    actual 1/4     MATCH
                      t³: predicted −1/6   actual −5/16   differ

    α_D = (z_D−1)h/2  t¹: −1/2  ⇒ c = −1/2
                      t²: predicted 1/4    actual 5/4     differ

So `α_C` is second-order consistent with a logarithmic (holonomy) form; `α_D` is
only first-order consistent.  **Neither IS a logarithm** — both fail at `t³`.

## What actually discriminates them — a structural criterion, not a coincidence

Expanding `α = (z−1)h/2` about `q = 1+t`, with `h = 2t − t² + …`:

    t¹ coefficient:  z(1) − 1        ⇒ log-match needs z(1) = 1/2
    t² coefficient:  1/4 + z′(1)     ⇒ log-match needs **z′(1) = 0**

Both conventions satisfy `z(1) = 1/2` (they agree at the classical point — see
`qbeta_zcd_classical_coincidence_probe.py`).  They differ on the derivative:

    z_C:  z′(1) = 0        z″(1) = −1/8
    z_D:  z′(1) = 1        z″(1) = 1/2

**`α` is second-order logarithmic exactly when the Markov parameter is
STATIONARY at the classical point.**  `z_C`'s only critical point on `q > 0` is
`q = 1`, and it is a *maximum*; `z_D` is not stationary there.  That is the whole
content of the second-order agreement, stated structurally.

## The crux, stated exactly — and a candidate explanation I tested and refuted

Realising `σ₁ = diag(q, −q⁻¹)` as a half-monodromy `exp(iπA)` fixes the
infinitesimal braiding, and its log-eigenvalue gap is

    log-gap(σ₁) = 2 ln q − iπ

I reached for the obvious story — that `α` is a quarter of that gap, the two
halvings being half-monodromy and Markov symmetrisation.  **That is wrong.**
`target/gap = −ln q/(4 ln q − 2iπ)` is not constant, and at `q₀` the `iπ`
dominates the real part by **15×**, so no fixed multiple of the gap gives `α`.
Recorded as refuted rather than quietly dropped, because it is the first thing
the next reader will also reach for.

What *is* exact:

    α_leading / Re(log-gap) = −1/4          (Re(log-gap) = 2 ln q)

So `α` is a quarter of the **real** part, with the `iπ` excluded.  Two things
are unexplained and together they are the whole remaining content: **why 1/4**,
and **why the `iπ` is discarded**.

## A structural consequence worth flagging

`σ₁`'s eigenvalues are `q` (modulus `q`, phase `0`) and `−q⁻¹` (modulus `q⁻¹`,
phase `π`).  So its *phase* content is `{0, π}` — **constant, with no
`q`-dependence at all** — while every bit of `q`-dependence sits in the
*moduli*, whose log-ratio is `2 ln q`.

`α` tracks the moduli.  That makes "eigenphase" a questionable name for it: it
is a log-modulus, not a phase, of this operator.  It also constrains branch 3
sharply — **a unitary holonomy cannot produce a `q`-dependent `α` from this
spectrum**, since a unitary monodromy's eigenvalues have modulus 1 and this
spectrum's phases are `q`-independent.  Either the connection is non-unitary, or
the phase comes from somewhere other than `σ₁`'s spectrum.  That is a falsifiable
fork, not a refutation: it says what a working construction must look like.

## The modular horn is EXCLUDED — `cos` cannot be re-read as `cosh`

If `α` really tracks the *moduli* (previous section), the natural resummation is
`cosh`, not `cos` — and that would be a large simplification, because
`cosh(c·ln q) = (q^c + q^{−c})/2` is **algebraic** in `q` for rational `c`.  The
whole rationality obstruction would dissolve and no transcendental construction
would be needed.

**It does not survive one line of arithmetic.**  The N=1 factor the ladder
requires is

    N1_req = Q_codata / (Q_A·(1 + c₂u²)) = 0.99839767…  < 1

and `cosh(x) ≥ 1` for every real `x`.  So no modular resummation can supply it;
the ladder needs a genuine oscillation.  `cosh((1/2)ln q) = 1.00136…`, on the
wrong side of 1.

**A near-miss, fenced deliberately.**  The two deviations are of comparable size
and opposite sign — `1 − N1_req = 1.60e-3` against `cosh − 1 = 1.36e-3` — which
invites an identity.  There is none: the closest candidates, `2 − cosh` and
`1/cosh`, are off by `2.4e-4` relative, i.e. they part company at the 4th digit.
Recorded so the resemblance is not chased.

## A refinement of the previous section's claim

"`σ₁`'s phases are `q`-free" is exact **for `σ₁`**, and must not be read as a
statement about the representation.  *Products* do carry `q`-dependent phases —
the route-3 enumeration found elliptic words such as `σ₁σ₂⁻¹`, whose trace
`−q²+1−q⁻²` is manifestly `q`-dependent.  So the Hecke representation does
supply oscillatory, `q`-dependent phases; what it never supplies is **this** one,
and that is the rationality exclusion, not a shortage of phases.

## The gap is ABELIAN — branch 3's target is a period, not a curvature integral

Sibling commit `93d211598f` proves `2α = ε(Δ) − tr_M(Δ)`, the counit-minus-trace
gap, via `CrossingWeightAffine.evalMap h w = h²/2 − h·w`.  That map is **affine
in the crossing weight** — degree exactly 1 — and the consequence for branch 3
does not appear in either PR:

    E(w₀) − E(w₀ + d) = d·h          the d² coefficient is EXACTLY 0

A genuine non-abelian holonomy carries a second-order Magnus/BCH term in the
departure.  **This gap has none.**  So the phase is an *abelian period* of an
affine map, not a curvature integral — a much smaller object than the
"non-abelian Stokes" holonomy the canonical chain invokes at step 2.

### That fork is now settled: affineness is NOT a truncation

The previous version of this probe left two readings open and said settling
them meant chasing where `evalMap` comes from.  Chased, and it settles cleanly.

`evalMap` is a **linear functional evaluated on one fixed vector**.  The `N=0`
neutron−proton normal-form difference, in the basis `[γ, σ₀, σ₁, L₊, L₋, e⁻]`
= `[1, s₁, s₂, s₁s₂, s₂s₁, s₁s₂s₁]`, is

    (n − p) = [h²/2, −h/2, −h/2, 0, 0, 0]

and the Markov rule is `tr_M(eᵢ) = z^{#cr(eᵢ)}` (the counit is that rule at
`z = 1`).  So

    deg_z E  =  max{ #cr(eᵢ) : cᵢ ≠ 0 }  =  1

because the support is `{γ (0 crossings), σ₀, σ₁ (1 each)}`.  Nothing was
expanded and nothing was dropped: there is no small parameter anywhere in the
step, so "truncation" was never the right category for it.  Reading (a) is
adopted — the non-abelian Stokes framing is not what produces *this* phase.

### But the abelian character belongs to the DIFFERENCE, not to the evaluation

This is the part worth carrying forward, and it is sharper than the fork it
replaces.  `L₊ = s₁s₂` has **two** crossings and coefficient **1 in both `n`
and `p`** — it cancels in the difference.  Restore it and the map is quadratic
in `w` with `d²`-coefficient `−1` (assertion 15).  So `n` and `p` *each* carry
a genuine second-order-in-weight term; the abelian gap is what survives their
cancellation.

That inverts the acceptance test into something much more specific:

**Sharpened acceptance test.**  Previously: reproduce `α` through `t²` in `q`,
and be exactly first-order in the crossing weight.  The second clause is now
wrong as stated — a non-abelian construction is *not* forbidden from carrying
second-order weight structure.  What it must do is have that structure
**cancel between `n` and `p`**, exactly as `L₊` does.  A construction whose
second-order term survives the difference contradicts `evalMap_affine`.

### The residual, named narrowly

The NF vector above is asserted in the audit doc (`audit step 5`) and
transcribed everywhere downstream: the Lean `epsNP`/`trMNP` are `def`s
encoding it, and the one probe in `computations/` that carries it
(`probes/probe_path_a_net_vs_trm_leading_order.py:137`) comments *"from the
.md"*.  No committed script recomputes it.  So the whole chain rests on a
single upstream computation that is not machine-checked here.

That residual is narrow, because assertion 16 shows the conclusion does not
depend on the coefficient *values* — only on the **support**.  The one thing
that would overturn it is a nonzero `L₊`, `L₋`, or `e⁻` coefficient in the
difference; the `L₊` cancellation in particular is the load-bearing line.

## Scope — this is consistency, NOT a derivation

  * It does **not** derive `α`, in either convention.
  * It does **not** establish that the holonomy angle is `−ħ/4`.  The scale `c`
    was fixed from `O(t)`; what is tested is the *shape* at the next order.
  * The evidence is **one** successful prediction (`t²`).  Real — a generic
    function with the right value and first derivative need not have `t² = 1/4`
    — but modest, and `t³` fails, so `α_C` is not a logarithm either.
  * It is a **falsifiable target** for branch 3: a genuine KZ/Stokes holonomy
    should reproduce `α` through `t²` and may deviate at `t³`.  If a constructed
    holonomy misses at `t²`, the N=1 factor is wrong.

## Tension with the 2026-08-15 ruling, stated plainly

The ruling makes convention **D** canonical.  On this test the decay channel's
phase looks **C**-shaped: `α_C` passes the second-order holonomy check and `α_D`
fails it by a factor of 5.  This does not overturn the ruling — that is a
corpus-wide trace-convention decision, and this is one channel's phase — but it
does *deepen* an already-recorded tension: `QOU.QBeta.decayLadder_zC_threeRow_ne_zero`
already proves the C-frame ladder and the two-row forcing are mutually
exclusive.  Recorded, not resolved.

Exact symbolic ℚ throughout; the one numerical line is mpmath.  No float64.
"""
from __future__ import annotations

import sys

import mpmath as mp
import sympy as sp

q, t, c = sp.symbols("q t c")


def series_at_one(expr, n=7):
    return sp.series(expr.subs(q, 1 + t), t, 0, n).removeO().expand()


def main() -> int:
    failures: list[str] = []

    def check(name, ok, detail):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        if not ok:
            failures.append(name)

    h = q - 1 / q
    zC = sp.sqrt(q) / (1 + q)
    zD = q ** 3 / (q ** 2 + 1)
    aC = (zC - 1) * h / 2
    aD = (zD - 1) * h / 2

    print("Assertions (exact symbolic ℚ):")

    # 1. the KZ scale relation
    check(
        "1. q = e^{hbar/2} matches the Hecke eigenvalues, so hbar = 2 ln q",
        sp.simplify(sp.exp(2 * sp.log(q) / 2) - q) == 0,
        "braiding P*exp(hbar*t/2), t eigenvalues +-1 -> {e^{hbar/2}, -e^{-hbar/2}} = {q, -1/q}",
    )

    # 2-3. one-parameter log family; scale fixed at t^1, higher orders predicted
    logP = sp.Poly(series_at_one(c * sp.log(q)), t)
    for nm, a, expect_order in (("alpha_C", aC, 2), ("alpha_D", aD, 1)):
        P = sp.Poly(series_at_one(a), t)
        csol = sp.solve(sp.Eq(logP.coeff_monomial(t ** 1), P.coeff_monomial(t ** 1)), c)[0]
        agree = 1
        for k in range(2, 6):
            pred = sp.simplify(logP.coeff_monomial(t ** k).subs(c, csol))
            act = sp.simplify(P.coeff_monomial(t ** k))
            if sp.simplify(pred - act) == 0:
                agree = k
            else:
                break
        check(
            f"{'2' if nm=='alpha_C' else '3'}. {nm} agrees with c*ln(q) through t^{expect_order}",
            agree == expect_order,
            f"c fixed = {sp.nsimplify(csol)} from t^1; agreement runs to t^{agree}",
        )

    # 4. the structural discriminator: z'(1) = 0
    dC = sp.simplify(sp.diff(zC, q).subs(q, 1))
    dD = sp.simplify(sp.diff(zD, q).subs(q, 1))
    check(
        "4. the discriminator is z'(1): zero for C, nonzero for D",
        dC == 0 and dD != 0,
        f"z_C'(1) = {dC}, z_D'(1) = {dD} -- the t^2 coefficient of alpha is 1/4 + z'(1)",
    )

    # 5. z_C is stationary at q=1 and it is its MAXIMUM on q>0
    crit = sp.solve(sp.diff(zC, q), q)
    d2C = sp.simplify(sp.diff(zC, q, 2).subs(q, 1))
    check(
        "5. z_C's only critical point on q>0 is q=1, and it is a maximum",
        crit == [sp.Integer(1)] and d2C < 0,
        f"critical points {crit}; z_C''(1) = {d2C} < 0; z_C(1) = {sp.simplify(zC.subs(q,1))}",
    )

    # 6. neither alpha IS a logarithm -- both fail at t^3
    P_C = sp.Poly(series_at_one(aC), t)
    t3_C = sp.simplify(P_C.coeff_monomial(t ** 3))
    check(
        "6. alpha_C is NOT a logarithm -- t^3 differs",
        sp.simplify(t3_C - sp.Rational(-1, 6)) != 0,
        f"alpha_C t^3 = {sp.nsimplify(t3_C)} vs log's -1/6",
    )

    # 7. numerical size of the second-order agreement at the substrate
    mp.mp.dps = 30
    q0 = mp.mpf("1.1099785827513808")
    aC0 = (mp.sqrt(q0) / (1 + q0) - 1) * (q0 - 1 / q0) / 2
    log0 = -mp.log(q0) / 2
    rel = (log0 - aC0) / aC0
    check(
        "7. at q0 the log form sits within 0.5% of alpha_C",
        abs(rel) < mp.mpf("0.005"),
        f"alpha_C = {mp.nstr(aC0,12)}, -(ln q)/2 = {mp.nstr(log0,12)}, rel {mp.nstr(rel*100,5)}%",
    )

    # ---- 8. the 'quarter of the gap' story is REFUTED ----
    lg = 2 * sp.log(q) - sp.I * sp.pi
    ratio_gap = sp.simplify((-sp.log(q) / 2) / lg)
    ratio_re = sp.simplify((-sp.log(q) / 2) / (2 * sp.log(q)))
    check(
        "8. alpha is -1/4 of Re(log-gap), NOT of the gap itself",
        sp.simplify(sp.diff(ratio_gap, q)) != 0
        and sp.simplify(ratio_re - sp.Rational(-1, 4)) == 0,
        f"target/gap = {ratio_gap} (NOT constant); target/Re(gap) = {ratio_re}",
    )

    # ---- 9. sigma_1's PHASE content is q-independent; the q-dependence is modular
    mp.mp.dps = 25
    q0n = mp.mpf("1.1099785827513808")
    dom = mp.pi / (2 * mp.log(q0n))
    check(
        "9. sigma_1's phases are {0, pi} (q-free); all q-dependence is in the moduli",
        dom > 10,
        f"at q0 the topological i*pi dominates Re(log-gap) by {mp.nstr(dom,4)}x, so a "
        f"UNITARY holonomy cannot produce a q-dependent alpha from this spectrum",
    )

    # ---- 10. the modular/cosh horn is excluded: the required N1 is below 1 ----
    N1_req = mp.mpf("0.9983976687192552")
    coshv = (mp.sqrt(q0n) + 1 / mp.sqrt(q0n)) / 2
    check(
        "10. required N1 < 1, but cosh >= 1 -- the modular resummation is excluded",
        N1_req < 1 and coshv >= 1,
        f"N1_req = {mp.nstr(N1_req,12)} < 1 <= cosh((1/2)ln q) = {mp.nstr(coshv,12)}; "
        "a genuine oscillation is required, so cos cannot be re-read as cosh",
    )

    # ---- 11. and the tempting near-miss is not an identity ----
    best = min(abs(v - N1_req) / N1_req for v in (2 - coshv, 1 / coshv))
    check(
        "11. the comparable-magnitude cosh near-miss is NOT an identity",
        best > mp.mpf("1e-4"),
        f"1 - N1_req = {mp.nstr(1-N1_req,6)} vs cosh - 1 = {mp.nstr(coshv-1,6)}; "
        f"closest candidate (2-cosh, 1/cosh) still off by {mp.nstr(best,4)} relative",
    )

    # ---- 12. the counit-minus-trace gap reproduces alpha exactly ----
    hs, ws, zs, ds, w0s = sp.symbols("h w z d w0")
    evalMap = lambda hh, ww: hh ** 2 / 2 - hh * ww
    gap = sp.expand(evalMap(hs, 1) - evalMap(hs, zs))
    check(
        "12. sibling identity: E(1) - E(z) = 2*alpha, exactly",
        sp.simplify(gap - 2 * ((zs - 1) * hs / 2)) == 0,
        f"E(1)-E(z) = {gap} = h(z-1) = 2*alpha",
    )

    # ---- 13. evalMap is AFFINE in the weight: no second-order Magnus term ----
    deg = sp.Poly(sp.expand(evalMap(hs, ws)), ws).degree()
    dep = sp.expand(evalMap(hs, w0s) - evalMap(hs, w0s + ds))
    second = sp.Poly(dep, ds).coeff_monomial(ds ** 2)
    check(
        "13. the gap is ABELIAN — d^2 coefficient exactly 0, so no curvature term",
        deg == 1 and second == 0,
        f"deg_w(evalMap) = {deg}; E(w0)-E(w0+d) = {dep}; d^2 coeff = {second}. "
        "A non-abelian holonomy would carry a Magnus/BCH second-order term",
    )

    # ---- 14. the affineness is the vanishing of the >=2-crossing coefficients ----
    # NF basis + crossing numbers (audit 2026-06-16 §"The two canonical
    # functionals"; probe_path_a_net_vs_trm_leading_order.py:33):
    #   gamma = 1 (0 crossings); sigma0 = s1, sigma1 = s2 (1 each);
    #   L+ = s1 s2, L- = s2 s1 (2 each); e- = s1 s2 s1 (3).
    # Markov rule tr_M(e_i) = z^{#cr(e_i)}; the counit is the same rule at z = 1.
    ncr = {"gamma": 0, "sigma0": 1, "sigma1": 1, "Lplus": 2, "Lminus": 2, "eminus": 3}
    dNF = {"gamma": hs ** 2 / 2, "sigma0": -hs / 2, "sigma1": -hs / 2,
           "Lplus": 0, "Lminus": 0, "eminus": 0}
    evalFromNF = sp.expand(sum(c * ws ** ncr[k] for k, c in dNF.items()))
    support = sorted({ncr[k] for k, c in dNF.items() if c != 0})
    check(
        "14. evalMap IS the NF vector under tr_M(e_i) = w^#cr(e_i) — not a truncation",
        sp.expand(evalFromNF - evalMap(hs, ws)) == 0 and max(support) == 1,
        f"sum_i c_i w^#cr(i) = {evalFromNF}; support crossing-numbers = {support}. "
        "deg_w = max #cr over the SUPPORT: nothing was expanded, nothing dropped",
    )

    # ---- 15. ... and it is CONTINGENT: L+ carries the second order, and cancels ----
    withLp = evalFromNF + ws ** ncr["Lplus"]      # L+ has coefficient 1 in BOTH n
    depLp = sp.expand(withLp.subs(ws, w0s)        # and p, so it survives in each
                      - withLp.subs(ws, w0s + ds))  # and cancels only in (n - p)
    degLp = sp.Poly(sp.expand(withLp), ws).degree()
    d2Lp = sp.Poly(depLp, ds).coeff_monomial(ds ** 2)
    check(
        "15. restoring L+ (coeff 1 in both n and p) makes the map QUADRATIC in w",
        degLp == 2 and d2Lp != 0,
        f"with L+: deg_w = {degLp}, d^2 coeff = {d2Lp}. So the abelian character "
        "belongs to the DIFFERENCE, not to the Hecke evaluation: n and p each "
        "carry a second-order-in-w term, and it cancels between them",
    )

    # ---- 16. the conclusion rests on the SUPPORT, not on the coefficient values ----
    c0, c1a, c1b = sp.symbols("c0 c1a c1b")
    generic = c0 + (c1a + c1b) * ws
    check(
        "16. affineness survives ARBITRARY support-{0,1} coefficients",
        sp.Poly(sp.expand(generic), ws).degree() <= 1,
        f"generic support-{{0,1}} vector gives {generic}: degree <= 1 for any "
        "c0, c1a, c1b. So the residual risk in the NF computation is confined to "
        "its SUPPORT (are the >=2-crossing coefficients really 0?), not its values",
    )

    print()
    if failures:
        print(f"FAILED {len(failures)}/16: {', '.join(failures)}")
        return 1
    print("16/16 assertions hold.")
    print()
    print("READING: alpha is second-order logarithmic exactly when the Markov")
    print("parameter is STATIONARY at the classical point. z_C is (q=1 is its")
    print("maximum on q>0); z_D is not. So the decay phase looks C-shaped on this")
    print("test. CONSISTENCY, not a derivation -- one predicted order, and t^3")
    print("fails for C too. Falsifiable target for branch 3: a real KZ/Stokes")
    print("holonomy should reproduce alpha through t^2.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
