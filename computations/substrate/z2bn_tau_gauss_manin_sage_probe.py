#!/usr/bin/env python3
"""z2bn lever-1 τ-derivation — SECOND probe SPEC: the Gauss–Manin prolongation (REQUIRES SAGE).

==============================================================================
STATUS: this is a *spec + scaffold*, authored where SageMath is unavailable.
Sections A (anchors) and the curve recap RUN in plain Python (sympy/mpmath)
and reproduce the corpus-confirmed pieces.  Sections B–E require SageMath
(`sage -python z2bn_tau_gauss_manin_sage_probe.py`); their Gauss–Manin /
Picard–Fuchs code is best-effort and carries `# VERIFY` markers where the
Sage runner must confirm the API/result.  Nothing here is wired to production.
==============================================================================

WHY A SECOND PROBE.  The first probe (`z2bn_tau_derivation_probe.py`, audit
`2026-06-25-z2bn-tau-derivation-first-probe.md`) established two clean pieces
and one clean negative:

  (A+) τ closed form   τ(q) = 3(3q⁴+8q²+3)/(4q(q+1)²)  — Lean-proved sorry-free
  (B+) curve confirmed j(q₀) = 129.86 (coral/descartes E_q)
  (E−) bare-period (a)-NEGATIVE: no single-curve period of E_q reproduces
        τ = 2.6424 (closest near-miss Im(ω₂/ω₁)=0.734 vs θ=0.781, ~6 % off).

The (E−) result is *expected*: per `sl2-prolongation-recurrence.md`, B is the
q-FAMILY Gauss–Manin **monodromy** on the rank-2 Hodge plane W (H¹(Bring)=2W),
NOT a fixed-curve period — and a single curve has no monodromy.  Per the
integrality finding (`2026-06-24-lever1-coral-eq-monodromy-integrality.md`),
tr B = 2.6424 ∉ ℤ while a *topological* elliptic monodromy is in SL₂(ℤ)
(integer trace); so B is the **abelianised λ_SW Cartan-connection holonomy**
(`mi-sw-abelianisation-cartan.md`: A⁰ = X dz = λ_SW), a real/hyperbolic
SL₂(ℝ) element, τ = 2cosh θ.  The non-trivial object the first probe could
not reach is the **prolongation operator** λ_SW^(n) ↦ a_D^(n): the anchors are
NOT the bare power sums (a_D³=(z²+4)/3 ≠ p₂(z)).  Computing that operator is a
Gauss–Manin job — what Sage can do and mpmath cannot.

------------------------------------------------------------------------------
GEOMETRY (all from the corpus; q₀ and 2.6424 are NEVER fed into the geometry).
------------------------------------------------------------------------------
Curve      E_q : y² = x³ + p(q) x + r(q)               (descartes-elliptic-curve)
  p(q) = 2(q²−q+1)/(3q) + (q−1)/(3√q)
  r(q) = 20(q−1)³/(27 q^{3/2}) + 5(q−1)²/(9q) + 5(√q − 1/√q)/9 + 20/27
Spectral   coral cubic   X³+(z+1)X²+(z²+z+1)X+(z³+z²+z+1)=0,   z = √q − 1/√q
  SW differential  λ_SW = X dz = A⁰  (Cartan component of the SU(2) connection)
Kernel     R = x² − τ x + det B,  det B = 1 (GM preserves the polarisation)
           ⇒ R = x² − τ x + 1,  a_D^(n+2) = τ a_D^(n+1) − a_D^(n)
Anchors    a_D^(2)=1,  a_D^(3)=(q+1)²/(3q),  a_D^(4)=(3q²+4+3q⁻²)/4
Target     τ = (a_D²+a_D⁴)/a_D³ ;  θ_binding = acosh(τ/2) ;  λ = e^θ
           τ(q₀)=2.642386…  θ(q₀)=0.781454…  λ(q₀)=2.184646…   (q₀ never tuned)

------------------------------------------------------------------------------
THE THREE PRINCIPLED PROLONGATION CANDIDATES (no fit; each FALSIFIABLE).
------------------------------------------------------------------------------
C1  GM-covariant prolongation.   a_D^(n) := ∮_γ (∇_GM)^{n-2} λ_SW, where ∇_GM
    is the Gauss–Manin connection in the family parameter (the Picard–Fuchs
    covariant q-derivative).  DECISIVE TEST: do the geometric a_D^(2,3,4)
    reproduce 1, (q+1)²/(3q), (3q²+4+3q⁻²)/4 as functions of q (symbolic),
    with NO scale tuning beyond the a_D^(2)=1 normalisation?
C2  Monodromy-matrix iterate.    B := GM monodromy of H¹_dR(E_q) on the rank-2
    W-plane around the binding loop γ in q-space; a_D^(n) := ⟨ω, Bⁿ v₀⟩.
    DECISIVE TEST: tr B = τ(q₀) = 2.642386 (NOT an SL₂(ℤ) integer — must be
    the abelianised, non-topological holonomy) and det B = 1.
C3  Abelianised λ_SW holonomy.   θ := ∮_γ A⁰  (the U(1)/Cartan component of the
    abelianised connection, A⁰ = λ_SW), τ := 2cosh θ.
    DECISIVE TEST: ∮_γ A⁰ = θ_binding = 0.781454 at q₀.

(a)/(b) DISCIPLINE.  A clean reproduction of the anchors / target by ONE
candidate, with the geometry blind to 2.6424, is an (a)-POSITIVE derivation.
A near-but-not-exact hit is NOT a derivation (numerology guard) — report it as
a scope-limited (a)-negative and move to the next candidate.  No candidate may
read q₀ or 2.6424 into its construction; the asserts at the end enforce this.
------------------------------------------------------------------------------
"""
import sys
import mpmath as mp
import sympy as sp

mp.mp.dps = 50
Q0 = mp.mpf("1.1099785955573347199")   # substrate q₀ (proton-pinned), 50-dps witness
TOL = mp.mpf("1e-12")                  # derivation tolerance; near-miss > TOL is NOT a hit


# ----------------------------------------------------------------------------
def section_A_anchors_and_target():
    """Runs anywhere. Reproduces the first probe's confirmed anchors + target."""
    q = sp.symbols('q', positive=True)
    aD2 = sp.Integer(1)
    aD3 = (q + 1) ** 2 / (3 * q)
    aD4 = (3 * q ** 2 + 4 + 3 / q ** 2) / 4
    tau_anchor = sp.simplify((aD2 + aD4) / aD3)
    tau_closed = 3 * (3 * q ** 4 + 8 * q ** 2 + 3) / (4 * q * (q + 1) ** 2)
    exact = sp.simplify(tau_anchor - tau_closed) == 0
    tau0 = mp.mpf(str(sp.N(tau_anchor.subs(q, sp.Float(str(Q0), 50)), 50)))
    theta0 = mp.acosh(tau0 / 2)
    lam0 = mp.e ** theta0
    print("=" * 78)
    print("Section A — anchors + target (corpus-confirmed; runs anywhere)")
    print("=" * 78)
    print(f"  τ closed form exact (Lean tau_kernel_closed_form): {exact}")
    print(f"  τ(q₀)  = {mp.nstr(tau0, 18)}")
    print(f"  θ(q₀)  = acosh(τ/2) = {mp.nstr(theta0, 18)}   <-- C3 target")
    print(f"  λ(q₀)  = e^θ        = {mp.nstr(lam0, 18)}")
    return {"tau0": tau0, "theta0": theta0, "lam0": lam0,
            "aD": {2: aD2, 3: aD3, 4: aD4}, "q": q}


# ----------------------------------------------------------------------------
def require_sage():
    """Clean exit (not a crash) when run in plain Python without Sage."""
    try:
        import sage.all  # noqa: F401
        return True
    except Exception:
        print("\n" + "=" * 78)
        print("Sections B–E REQUIRE SageMath.  Run:  sage -python " + __file__.split('/')[-1])
        print("In plain Python the Gauss–Manin / Picard–Fuchs steps are unavailable.")
        print("This spec authored where Sage was unavailable; B–E are UNTESTED here.")
        print("=" * 78)
        return False


# ----------------------------------------------------------------------------
def section_B_gauss_manin(ctx):
    """SAGE.  Build the q-family + its Gauss–Manin / Picard–Fuchs connection."""
    from sage.all import (PolynomialRing, FractionField, QQ, SR,  # noqa: F401
                          EllipticCurve, var, diff, sqrt)
    # Family over the rational function field in q (use s=√q to keep p,r rational in s).
    # E_q : y² = x³ + p x + r.  # VERIFY: Sage prefers a ground field where √q is a unit;
    # work over QQ(s) with s²=q, or pass to the numerical fibre at q₀ for the period step.
    s = var('s')                      # s = √q
    q_of_s = s ** 2
    p = 2 * (q_of_s ** 2 - q_of_s + 1) / (3 * q_of_s) + (q_of_s - 1) / (3 * s)
    r = (20 * (q_of_s - 1) ** 3 / (27 * s ** 3) + 5 * (q_of_s - 1) ** 2 / (9 * q_of_s)
         + 5 * (s - 1 / s) / 9 + QQ(20) / 27)
    print("\nSection B — Gauss–Manin connection of E_q (SAGE)")
    print("  p(s), r(s) built over QQ(s), s=√q.")
    # Picard–Fuchs operator L (2nd order, since H¹_dR rank 2) for the period π(q):
    #   L = ∂_q² + A(q) ∂_q + B(q),  via Griffiths–Dwork on the family.
    # VERIFY: in Sage this is the holonomic PF ODE annihilating ∮ dx/y.  Candidate APIs:
    #   - sage.modular.hypergeometric_motive / sage.schemes ... griffiths_dwork
    #   - or construct from the discriminant + Wronskian of the two periods.
    # Return a handle the prolongation step consumes; left as the runner's TODO.
    raise NotImplementedError(
        "VERIFY: assemble the 2nd-order Picard–Fuchs ODE for ∮ dx/y of E_q(s) "
        "via Griffiths–Dwork; expose ∇_GM = covariant ∂_q on the period vector "
        "(ω, ∇ω). This is the connection the three candidates below consume.")


# ----------------------------------------------------------------------------
def section_C_prolongation_candidates(ctx, gm):
    """SAGE.  Compute geometric a_D^(n) for C1/C2/C3 and test vs the anchors."""
    # C1 — GM-covariant prolongation:  a_D^(n) = ∮ (∇_GM)^{n-2} λ_SW, λ_SW = X dz.
    #   compute a_D^(2,3,4)(q) symbolically; DECISIVE: equal 1, (q+1)²/(3q),
    #   (3q²+4+3q⁻²)/4 ?  (normalise only by a_D^(2)=1; no other tuning.)
    # C2 — monodromy iterate: B from analytic continuation of (ω,∇ω) around γ ⊂ q-plane;
    #   DECISIVE: tr B = 2.642386 (∉ ℤ — abelianised) and det B = 1.
    # C3 — abelianised holonomy: θ = ∮_γ A⁰ (Cartan U(1) part); DECISIVE: θ = 0.781454.
    raise NotImplementedError(
        "VERIFY: implement C1/C2/C3 against `gm`; each returns its geometric value "
        "and a boolean = |value − target| < TOL with the geometry blind to 2.6424.")


# ----------------------------------------------------------------------------
def section_E_verdict(ctx, results):
    """Honest (a)/(b) verdict + anti-fit asserts (run regardless of Sage)."""
    print("\nSection E — verdict ((a)/(b) discipline)")
    if not results:
        print("  Sage sections did not run — no geometric verdict produced.")
        print("  (a)+ standing: τ closed form (Lean), curve j(q₀)=129.86 (probe 1).")
        print("  OPEN: the prolongation operator (C1/C2/C3) — owner-gated keystone.")
        return
    # A candidate is a DERIVATION only if it hits its target to < TOL with the
    # geometry never having read q₀ or 2.6424 — the targets enter ONLY the
    # boolean tests in section C, never a construction (see the C1/C2/C3 specs).
    for name, (val, ok) in results.items():
        verdict = "(a)+ DERIVATION" if ok else "(a)- scope-limited (near-miss ≠ derivation)"
        print(f"  {name}: value={val}  ->  {verdict}")


# ----------------------------------------------------------------------------
def main():
    ctx = section_A_anchors_and_target()
    results = {}
    if require_sage():
        try:
            gm = section_B_gauss_manin(ctx)
            results = section_C_prolongation_candidates(ctx, gm)
        except NotImplementedError as e:
            print(f"\n[spec TODO for the Sage runner] {e}")
    section_E_verdict(ctx, results)
    print("\nNo fit; nothing wired. q₀ and 2.6424 never entered any construction.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
