import Mathlib.Tactic

/-!
# QOU.ArchimedeanUniverse.mi_sw_cartan_reduction

Content block
[`lem:mi-sw-abelianisation-cartan`](../../../quantum-observable-universe/brings-surface/mi-sw-abelianisation-cartan.md): *Cartan reduction recovers the Seiberg--Witten differential*.

## Lean structure (§3b-cond: hypotheses in the class, conclusion derived)

The narrative lemma has three clauses on the exceptional divisor
`𝒮_c ≅ ℙ¹(ℂ)`:

1. the `SU(2)`-bundle trivialises, so `∇_A` reduces to an
   `𝔰𝔲(2)`-valued `1`-form `A|_{𝒮_c}`;
2. under the weight-space decomposition
   `A|_{𝒮_c} = A⁰ ⊗ H + A⁺ ⊗ E₊ + A⁻ ⊗ E₋`, and the off-diagonal
   weight components vanish (abelianisation);
3. the Cartan component is the Seiberg–Witten differential:
   `A⁰ = X·dz = λ_SW`.

`WeightDecomposedForm` models clause 2's decomposition (the three
weight components of the reduced form); `cartanEmbed` is the abelian
embedding `ω ↦ ω ⊗ H`.  The class
`MiSwCartanReductionHypotheses` carries the genuine geometric
**inputs** — the vanishing of the off-diagonal components on the
exceptional divisor, the local Higgs-eigenvalue computation
`A⁰ = X • dz`, and the definitional `λ_SW = X • dz` of the
Seiberg–Witten differential on the spectral curve.  The theorem
`mi_sw_cartan_reduction` then **derives** (not projects) the
conclusion: the reduced connection *is* the Cartan embedding of
`X • dz` (via the proved helper `eq_cartanEmbed_of_offdiag_zero`),
and its Cartan component *is* `λ_SW` (by composing the two local
identifications).  No class field is conclusion-typed; no instance is
fabricated — the open geometric content is precisely the existence of
an instance for the actual Bring-surface data.

Stated over a generic module `(R, Ω)` per AGENTS.md §7c: the
identification is purely algebraic (equalities in a module of scalar
`1`-forms); no archimedean construct is required.

## References

- [leitner2026] quantum-observable-universe/brings-surface/mi-sw-abelianisation-cartan.md.
-/

namespace QOU.ArchimedeanUniverse

/-- An `𝔰𝔲(2)`-valued `1`-form recorded in the weight-space
    decomposition `A = A⁰ ⊗ H + A⁺ ⊗ E₊ + A⁻ ⊗ E₋`:
    the three components are the coefficients of the standard
    generators `H, E₊, E₋`.  `Ω` is the (additive) group of scalar
    `1`-forms on the exceptional divisor. -/
structure WeightDecomposedForm (Ω : Type*) where
  /-- The Cartan (`H`-weight-`0`) component `A⁰`. -/
  cartan : Ω
  /-- The raising (`E₊`) component `A⁺`. -/
  plus : Ω
  /-- The lowering (`E₋`) component `A⁻`. -/
  minus : Ω

/-- The abelian (Cartan) embedding: a `U(1)`-valued `1`-form `ω`
    viewed as the `𝔰𝔲(2)`-valued form `ω ⊗ H` with vanishing
    off-diagonal weight components. -/
def cartanEmbed {Ω : Type*} [Zero Ω] (ω : Ω) : WeightDecomposedForm Ω :=
  ⟨ω, 0, 0⟩

/-- **Helper (proved).**  A weight-decomposed form whose off-diagonal
    components vanish *is* the Cartan embedding of its Cartan
    component.  This is the abelianisation step of the lemma. -/
theorem eq_cartanEmbed_of_offdiag_zero {Ω : Type*} [Zero Ω]
    (A : WeightDecomposedForm Ω) (hp : A.plus = 0) (hm : A.minus = 0) :
    A = cartanEmbed A.cartan := by
  obtain ⟨cartan, plus, minus⟩ := A
  simp only at hp hm
  subst hp hm
  rfl

/-- **§3b-cond hypothesis class** for
    [`lem:mi-sw-abelianisation-cartan`]: the geometric inputs of the
    Cartan-reduction lemma on the exceptional divisor
    `𝒮_c ≅ ℙ¹(ℂ)`.

    Fields are genuine *hypotheses* (never the conclusion):

    * `abelianised_plus` / `abelianised_minus` — the off-diagonal
      weight components of the reduced connection vanish on `𝒮_c`
      (weight-space abelianisation; narrative clause 2);
    * `cartan_local_form` — the local Higgs-eigenvalue computation:
      in the coordinate chart the Cartan component is `X • dz`, where
      `X` is the color coordinate cut out on the single spectral-curve
      sheet over `𝒮_c` (open geometric input; not in Mathlib);
    * `sw_eq_local_form` — the Seiberg–Witten differential is the
      tautological form `X • dz` on the spectral curve (its defining
      property, recorded as a hypothesis on the opaque `lambdaSW`).

    The conclusion `A⁰ = X·dz = λ_SW` plus the structural
    trivialisation statement is *derived* in
    `mi_sw_cartan_reduction` below.  No instance is declared —
    fabricating one would be the §3b-tax violation; the open content
    is the existence of an instance for the Bring-surface geometry. -/
-- Ref: [leitner2026] quantum-observable-universe/brings-surface/mi-sw-abelianisation-cartan.md
class MiSwCartanReductionHypotheses (R Ω : Type*) [CommRing R]
    [AddCommGroup Ω] [Module R Ω] where
  /-- The restriction `A|_{𝒮_c}` of the reduced connection, in the
      weight-space decomposition (clause 1's trivialised form). -/
  A : WeightDecomposedForm Ω
  /-- The color coordinate `X` (Higgs-field eigenvalue on the single
      sheet of the spectral curve over `𝒮_c`). -/
  X : R
  /-- The local coordinate `1`-form `dz` on `𝒮_c ≅ ℙ¹`. -/
  dz : Ω
  /-- The Seiberg–Witten differential `λ_SW`. -/
  lambdaSW : Ω
  /-- Abelianisation: the raising component vanishes on `𝒮_c`. -/
  abelianised_plus : A.plus = 0
  /-- Abelianisation: the lowering component vanishes on `𝒮_c`. -/
  abelianised_minus : A.minus = 0
  /-- Local computation: the Cartan component is `X • dz` in the
      chart (Higgs-eigenvalue input). -/
  cartan_local_form : A.cartan = X • dz
  /-- Defining property of the SW differential on the spectral
      curve: `λ_SW = X • dz`. -/
  sw_eq_local_form : lambdaSW = X • dz

/-- **Lemma (conditional on the geometric inputs above)**
    ([`lem:mi-sw-abelianisation-cartan`]): *Cartan reduction recovers
    the Seiberg–Witten differential.*

    Under the weight-space abelianisation and the two local
    identifications carried by `MiSwCartanReductionHypotheses`, the
    reduced connection **is** the Cartan embedding of `X • dz`
    (trivialisation + abelianisation, clauses 1–2), and its Cartan
    component **is** the Seiberg–Witten differential (clause 3,
    `A⁰ = X·dz = λ_SW`).

    Derived, not projected: the first conjunct composes the proved
    helper `eq_cartanEmbed_of_offdiag_zero` with the local form; the
    second composes the two local identifications by transitivity.
    Neither conjunct is a class field (§3b-cond item 5). -/
-- Ref: [leitner2026] quantum-observable-universe/brings-surface/mi-sw-abelianisation-cartan.md
theorem mi_sw_cartan_reduction {R Ω : Type*} [CommRing R]
    [AddCommGroup Ω] [Module R Ω]
    [ctx : MiSwCartanReductionHypotheses R Ω] :
    ctx.A = cartanEmbed (ctx.X • ctx.dz) ∧ ctx.A.cartan = ctx.lambdaSW := by
  constructor
  · rw [eq_cartanEmbed_of_offdiag_zero ctx.A ctx.abelianised_plus
      ctx.abelianised_minus, ctx.cartan_local_form]
  · rw [ctx.cartan_local_form, ctx.sw_eq_local_form]

end QOU.ArchimedeanUniverse
