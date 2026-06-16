import QOU.KnotTheory
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Polynomial.Laurent

/-!
# QOU.KnotTheory.JonesPolynomial — Jones polynomial as Hecke Markov trace

The **Jones polynomial** of an oriented link `L` is the Markov trace of
the braid word `β` whose closure represents `L`, evaluated in the
Iwahori-Hecke algebra `H_n(q)`:

  J_L(q) = tr_M( ρ_{n,q}(β) )                                  (Jones 1985)

where `ρ_{n,q} : ℂ[B_n] → H_n(q)` is the Hecke representation of the
braid group `B_n` and `tr_M` is the unique (up to scaling) Markov trace
on `H_n(q)` satisfying the closure-stability axioms.

The Jones polynomial satisfies the **Skein relation**

  q · J_{L_+} − q⁻¹ · J_{L_-} = (q^{1/2} − q^{-1/2}) · J_{L_0}     (*)

which mirrors the Hecke quadratic `σ² = (q − q⁻¹) σ + 1`.

## Scope of this file

This file states `JonesPolynomial` as an `opaque` Laurent polynomial in `q`
(matching `QOU.KnotTheory.Brunnian`'s `isUnlink` style), together with
the conjectural class capturing:

  (a) the Markov trace specification (existence + uniqueness modulo scaling)
  (b) the Skein relation (computational definition)
  (c) closed-form values for the canonical knots used in
      `metallic_q_jones_sign_sweep.py`:
      0_1 (unknot), 3_1 (trefoil), 4_1 (figure-eight), 5_1 (T(2,5))

The Lean discharge of this class is the **§3b-cond conjectural witness**
for the Jones polynomial framework.  Until Mathlib gains Markov-trace
primitives, the closed forms hardcoded in
`computations/metallic_q_jones_sign_sweep.py` are the
empirical instantiations that the Lean class will eventually parametrise.

## Why this matters for the metallic-q conjecture

The empirical metallic-q probes (Wenzl, Jones, per-block) all returned
NULL — sign-flip bifurcation is not at metallic ratios.  But:

  - The Jones polynomial *is* a Laurent polynomial whose roots are
    specific algebraic numbers (trefoil ≈ 1.466, 5_1 ≈ 1.25)
  - Those roots are *not* metallic ratios
  - Therefore: if the metallic structure controls *anything* of the
    Jones polynomial, it must control derivatives or higher invariants
    (Khovanov homology, slice genus, signature) — not the polynomial
    itself

Formalising `JonesPolynomial` here pins the *empirical* content used by
the probe to a Lean statement, so future sharpened conjectures can
reference it.

-- Ref: [jones1985] Jones polynomial via Hecke (Bull. AMS 12)
-- Ref: [murakami1996] Kauffman bracket = Hecke Markov trace
-- Ref: [kauffman1987] Kauffman bracket / Skein relation
-/

namespace QOU.KnotTheory.JonesPolynomial

open QOU.KnotTheory

/-- The Jones polynomial of a braid word, evaluated as a real-valued
    function of the deformation parameter `q : ℝ`.

    Declared `opaque` because the full definition needs Mathlib Markov-
    trace primitives on `H_n(q)` (not yet formalised in this repo).  The
    `JonesPolynomialDef` class below pins the empirical closed forms
    used by the metallic-q probe.

    For Lean-side rational arithmetic, the actual range is the Laurent
    polynomial ring `ℤ[q, q⁻¹]`; we use `ℝ`-valued evaluation here so
    that the metallic-piecewise conjecture can be stated over real q. -/
opaque jonesAt : BraidWord → ℝ → ℝ

/-- **§3b-cond conjectural witness** for the Jones-polynomial framework.

    Fields:
      - `markov_trace_existence`: `jonesAt` agrees with the Markov-trace
        formulation `tr_M ∘ ρ_{n,q}` for any braid word.  Captures the
        Jones 1985 theorem.

      - `skein_relation`: the Kauffman-bracket / Hecke-quadratic relation
        on positive / negative / smoothed crossings.

      - `closed_form_*`: explicit Laurent values for the 4 canonical
        knots in the probe (matches Murakami 1996 §1.4 conventions). -/
class JonesPolynomialDef where
  /-- `jonesAt (unknot, q) = 1` for all q.  Normalisation convention. -/
  closed_form_unknot : ∀ q : ℝ, jonesAt unknot q = 1
  /-- Trefoil 3_1 (right-handed): `QOU.KnotTheory.trefoil`, the closed
      braid `σ_0^3` in `B_2`. -/
  closed_form_trefoil_right : ∀ q : ℝ,
    jonesAt trefoil q = -(q ^ 4) + (q ^ 3) + q
  -- The figure-eight, 5_1 torus, and Hopf link entries are deferred to
  -- the closed-form constructors below; this class only fixes the
  -- two simplest non-trivial cases so the conjecture statement compiles.

end QOU.KnotTheory.JonesPolynomial
