import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Module.Basic


/-!
# QOU.Photon — degree-one Hecke elements have trivial archimedean volume

A degree-one element of `H_n(q)` is

  γ = 1 + Σ_i φ_i σ_i

(in additive notation; `1` denotes the identity, and `φ_i ∈ ℂ` are
arbitrary scalars). Its closure is a disjoint union of unlinks — hence
non-hyperbolic — so the hyperbolic volume vanishes. By linearity of
the Markov trace and the volume map, `Vol(closure γ) = 0`.

This file states the lemma in lightweight form: it takes the
*interface* — an additive volume map `vol : Hecke →+ ℝ`, an axiom
`vol_one_zero`, and a per-generator vanishing — and concludes
vanishing on every degree-one element. Concrete callers (the
algebraic-quantum-volume pipeline) supply the actual volume map.

LaTeX label: `lem:degree-one-braid-trivial-volume`

## References

- [jones1987] https://doi.org/10.2307/1971403 (linearity of the
  Markov trace).
- [kashaev1997] https://doi.org/10.1023/A:1007364912784 (volume of a
  non-hyperbolic link is zero by convention).
- [manuscript] braids-and-knots / degree-one-braid-trivial-volume
-/

namespace QOU.Photon

/-- Minimal interface for a Hecke-algebra-like carrier on which we can
    state "degree-one element = identity + linear combination of
    generators" and "the volume of its closure is zero on each summand".

    The carrier is an additive commutative monoid; the volume map is an
    additive monoid homomorphism `vol : carrier →+ ℝ`. The two physical
    facts that drive the lemma are stated as fields of the structure:

    * `vol_one_zero` — closure of the identity is the trivial unlink, so
      its hyperbolic volume is zero.
    * `vol_gen_zero` — the closure of a single twisted strand is again
      a (possibly framed) unlink, again of zero hyperbolic volume.
-/
structure VolumeInterface where
  /-- Carrier of the algebra (additively). -/
  carrier : Type*
  /-- Carrier is an additive commutative monoid. Declared as an
      instance field so typeclass resolution sees it. -/
  [addCommMonoid : AddCommMonoid carrier]
  /-- Distinguished identity element (the trace of `1`). -/
  one : carrier
  /-- Number of strand generators. -/
  m : ℕ
  /-- Generators `σ_0, …, σ_{m-1}`. The "scaled generator" `φ_i · σ i`
      is encoded as part of the user-supplied family `term i`, since
      we do not need a full `ℂ`-module structure on the carrier — only
      additivity + a trace. -/
  term : Fin m → carrier
  /-- Volume map. -/
  vol : carrier →+ ℝ
  /-- The closure of the identity is non-hyperbolic. -/
  vol_one_zero : vol one = 0
  /-- Each scaled generator term has volume zero (linearity in `φ_i`
      reduces to vanishing on the underlying generator). -/
  vol_term_zero : ∀ i, vol (term i) = 0

/-- A degree-one element: the identity plus a finite sum of scaled
    generator terms. -/
noncomputable def degreeOne (V : VolumeInterface) : V.carrier :=
  letI := V.addCommMonoid
  V.one + ∑ i : Fin V.m, V.term i

/-- **Degree-one volume lemma.**
    For any volume interface `V`, the volume of `1 + Σ_i term i` is
    zero.

    Proof: `vol` is an `AddMonoidHom`, so commutes with sums; both
    `vol V.one = 0` and `vol (V.term i) = 0` are part of the interface.
-/
-- Ref: [manuscript] lem:degree-one-braid-trivial-volume
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
-- Ref: [kashaev1997] Kashaev, "The hyperbolic volume of knots from the quantum dilogarithm," Lett. Math. Phys. 39 (1997)
theorem geom_degree_one_zero (V : VolumeInterface) :
    V.vol (degreeOne V) = 0 := by
  classical
  letI := V.addCommMonoid
  unfold degreeOne
  -- vol (one + ∑ term i) = vol one + ∑ vol (term i) = 0 + 0 = 0
  rw [map_add, map_sum]
  rw [V.vol_one_zero]
  simp [V.vol_term_zero]

end QOU.Photon
