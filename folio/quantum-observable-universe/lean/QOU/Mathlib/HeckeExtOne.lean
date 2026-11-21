import QOU.Mathlib.ExtensionClass
import QOU.GroundRingCore
import Mathlib.RingTheory.Ideal.Span
import Mathlib.Tactic

/-!
# QOU.Mathlib.HeckeExtOne — `Ext¹(V_asym, V_sym) ≅ R/(α − β)`

Bean `qou-zut2`. `phase-transition-boundary` asserted that the mixed-channel
Hecke representation is a **non-split** extension

    0 → V_sym → V_mixed → V_asym → 0

classified by `Ext¹_{H_n(q)}(V_asym, V_sym) ≅ ℤ`, while
`skein-resolution-obstruction` states that `H_n(q₀)` is **semisimple**
(`Rad = 0`) at the physical `q₀ ≈ 1.1099`. A semisimple algebra has
`Ext¹ = 0`, so the two looked inconsistent.

The Ext group is computed here by hand, over a general `CommRing` and with the
two eigenvalues carried as parameters `α, β`. The answer is `R/(α − β)` — a
*torsion* `R`-module supported exactly on the locus where the eigenvalues
collide, which is exactly the locus where the algebra fails to be semisimple.

**The computation is what this file is for; it does not rescue the block.**
An earlier reading of it did claim that, on the strength of `α = q, β = -1`
giving `R_q/(q+1) ≅ ℤ`. That normalisation is not the one
`phase-transition-boundary` uses, and under the one it does use the answer is
`ℤ[i]`; see "Which normalisation the block is under" below. The claim is
withdrawn on the block (`prop:phase-transition-boundary`, status note
2026-08-24); this file keeps the algebra and drops the verdict.

## The computation, which is elementary

Take the Hecke quadratic in the form `(T - α)(T - β) = 0`, so the two
one-dimensional modules are `V_α` with `T ↦ α` and `V_β` with `T ↦ β`. The
eigenvalues are carried as parameters rather than substituted, because the
corpus uses two normalisations in different chapters and the answer depends on
which — see below.

An extension of `V_β` by `V_α` is free of rank two: `T e₁ = α e₁` and
`T e₂ = β e₂ + c e₁` for some `c : R`. `extAction_quadratic` shows the quadratic
relation holds for **every** `c`, so every `c` really does give an extension —
there is no hidden constraint. Rebasing `e₂ ↦ e₂ + λ e₁` sends `c ↦ c + λ(β−α)`,
so the classification is `R` modulo the ideal `(α − β)`:

    Ext¹(V_β, V_α) ≅ R / (α − β).

`splits_iff_mem_span` is that statement in the form actually proved: the
extension splits precisely when `c` lies in the ideal.

## The semisimple half

`splits_of_isUnit_sub`: wherever `α − β` is invertible the ideal is everything,
the quotient is zero, and there is nothing to classify. That is the same fact as
`ExtensionClass.isCompl_ker_quadratic`, which states it for an arbitrary module
carrying the quadratic rather than for the rank-two model, and it is what
`skein-resolution-obstruction`'s `Rad = 0` demands.

## Which normalisation the block is under — bean `qou-oyty`, option 3

The corpus carries two Hecke normalisations, and the classification is not
invariant under the rescaling between them, because it depends on the
*difference* of the eigenvalues.

* **A.** `QOU/BraidKnot/HeckeAnyonicSubstrate.lean` uses `(T − q)(T + 1) = 0`:
  eigenvalues `q, -1`, ideal `(q + 1)`, and `R_q/(q+1) = ℤ[q, q⁻¹]/(q+1) ≅ ℤ`
  via `q ↦ -1`. Degenerate at `q = -1`.
* **B.** `rem:hecke-algebra-from-braiding` — which is the block that *defines*
  `H_n(R, q)` for this corpus — uses `(σ − q)(σ + q⁻¹) = 0`: eigenvalues `q`
  and `-q⁻¹`, ideal `(q + q⁻¹) = (q² + 1)` up to the unit `q⁻¹`, and
  `ℤ[q, q⁻¹]/(q² + 1) ≅ ℤ[i]` — the **Gaussian integers, not `ℤ`**.
  Degenerate at `q² = -1`.

`phase-transition-boundary` is under **B**, not A. Its interpreting remark
`rem:phase-transition-interpretation` names the two channels by their
eigenvalues `q` and `-q⁻¹`, and `rem:hecke-algebra-from-braiding` writes the
defining relation in that form. So the classification for that block is `ℤ[i]`,
which is `ℤ²` as a group and has no distinguished generator — the Hopf
invariant of `π₃(S²) = ℤ` cannot generate it.

Two further facts finish the matter, both in `ExtensionClass`:

* `twoQ_eq_zero_iff` — under B the eigenvalues collide exactly on `q² + 1 = 0`,
  i.e. at `q = ±i`, not at `q = -1`.
* `twoQ_ne_zero_of_ordered` and `heckeSES_isSplit_of_ordered` — that locus is
  not real, so on the archimedean side of the §7c wall, where
  `phase-transition-boundary` lives (`abbrev R_q := ℝ` in its Lean sibling), the
  sequence splits at **every** nonzero `q`. There is no real substrate value,
  root of unity or not, at which a non-split extension exists to be classified.

Anyone quoting a value for this Ext group must say which relation they mean.

-- Ref: [leitner2026] quantum-observable-universe/information-theory
-/

namespace QOU.Mathlib.HeckeExtOne

universe u

variable {R : Type u} [CommRing R]

/-- **The rank-two extension** `M_c` of `V_β` by `V_α`.

    Carrier `R × R`, with `e₁ = (1,0)` spanning the sub-object `V_α` and
    `e₂ = (0,1)` lifting `V_β`. The generator acts by

        T (x, y) = (α x + c y, β y).

    Read off the matrix: `T e₁ = α e₁` and `T e₂ = c e₁ + β e₂`. -/
def extAction (α β c : R) : (R × R) →ₗ[R] (R × R) where
  toFun p := (α * p.1 + c * p.2, β * p.2)
  map_add' p r := by
    simp only [Prod.fst_add, Prod.snd_add, Prod.mk_add_mk, Prod.mk.injEq]
    constructor <;> ring
  map_smul' r p := by
    simp only [Prod.smul_fst, Prod.smul_snd, Prod.smul_mk, smul_eq_mul,
      RingHom.id_apply, Prod.mk.injEq]
    constructor <;> ring

@[simp] theorem extAction_apply (α β c : R) (p : R × R) :
    extAction α β c p = (α * p.1 + c * p.2, β * p.2) := rfl

/-- **Every `c` gives a genuine extension.**

    `(T − α)(T − β) = 0` holds for all `c`, so the Hecke quadratic relation
    places no constraint on the extension parameter. This is what makes the
    classification a full quotient of `R` rather than of a subset. -/
theorem extAction_quadratic (α β c : R) :
    ((extAction α β c) - α • LinearMap.id).comp
      ((extAction α β c) - β • LinearMap.id) = 0 := by
  ext <;>
  · simp only [LinearMap.comp_apply, LinearMap.sub_apply, LinearMap.smul_apply,
      LinearMap.id_apply, extAction_apply, Prod.smul_fst, Prod.smul_snd,
      smul_eq_mul, Prod.fst_sub, Prod.snd_sub, LinearMap.zero_apply,
      Prod.fst_zero, Prod.snd_zero]
    ring

/-- The extension **splits** when the quotient generator lifts equivariantly:
    a section `y ↦ (λ y, y)` commuting with `T`. -/
def Splits (α β c : R) : Prop := ∃ lam : R, c = lam * (β - α)

/-- **The classification.** `M_c` splits exactly when `c` lies in the ideal
    generated by `α − β`.

    The section must be `y ↦ (λ y, y)` for some `λ`, and equivariance forces
    `α λ + c = λ β`. So the splittings are parametrised by solutions of
    `c = λ(β − α)`, and the extension classes by `R / (α − β)`. -/
theorem splits_iff_mem_span (α β c : R) :
    Splits α β c ↔ c ∈ Ideal.span ({α - β} : Set R) := by
  rw [Ideal.mem_span_singleton]
  constructor
  · rintro ⟨lam, rfl⟩
    exact ⟨-lam, by ring⟩
  · rintro ⟨k, rfl⟩
    exact ⟨-k, by ring⟩

/-- **The semisimple half.** If the two eigenvalues differ by a unit, every
    extension splits — the ideal is everything and the quotient is zero.

    This is why `Ext¹ = 0` at the physical point: `q₀ ≈ 1.1099` makes
    `q₀ + 1 ≈ 2.11` invertible, and `skein-resolution-obstruction`'s
    `Rad = 0` is the same fact. -/
theorem splits_of_isUnit_sub (α β c : R) (h : IsUnit (α - β)) :
    Splits α β c := by
  rw [splits_iff_mem_span]
  rw [Ideal.span_singleton_eq_top.mpr h]
  trivial

/-- **The degenerate half.** Where the eigenvalues collide the ideal is zero,
    so `c` classifies on the nose and every nonzero `c` is a non-split
    extension.

    `α = β` is exactly where `(T − α)(T − β)` acquires a double root, i.e.
    where the algebra stops being semisimple. The extensions live there and
    nowhere else. -/
theorem not_splits_of_eq_of_ne_zero {α β c : R} (hαβ : α = β) (hc : c ≠ 0) :
    ¬ Splits α β c := by
  rintro ⟨lam, rfl⟩
  exact hc (by rw [hαβ]; ring)

/-! ### Normalisation A only

    The two results below are specific to normalisation **A**,
    `(T − q)(T + 1) = 0` (`HeckeAnyonicSubstrate`). They say nothing about
    `phase-transition-boundary`, which is under **B** — see the module
    docstring. Under B the degenerate locus is `q² = -1`, and
    `ExtensionClass.twoQ_ne_zero_of_ordered` shows it is not real. -/

/-- Under normalisation A, `(T − q)(T + 1) = 0`, the classifying ideal is
    `(q + 1)`. -/
theorem span_eq_q_add_one (q : R) :
    Ideal.span ({q - (-1)} : Set R) = Ideal.span ({q + 1} : Set R) := by
  norm_num

/-- Under normalisation A the extension is non-split exactly at `q = -1` — the
    double-root point of `(T − q)(T + 1)`, hence the non-semisimple point.

    Stated for `c = 1`, the generator of the classification. -/
theorem hecke_not_splits_at_neg_one {R : Type u} [CommRing R] [Nontrivial R]
    (q : R) (hq : q = -1) : ¬ Splits q (-1) (1 : R) :=
  not_splits_of_eq_of_ne_zero (by rw [hq]) one_ne_zero

/-! ### The nontriviality hypothesis is free over the QOU ground ring

    `hecke_not_splits_at_neg_one` carries `[Nontrivial R]`, and over an
    arbitrary `CommRing` it has to: in the zero ring `1 = 0` and every
    extension splits vacuously.

    It is **not** an added assumption in the QOU setting.
    `QOU.GroundRing.instNontrivialR_q` records that `R_q` is not the zero ring,
    so the hypothesis is discharged rather than assumed. Cited rather than
    re-derived — the fact has one home, next to `R_q` itself. -/

/-- The normalisation-A non-split extension at `q = -1`, over the ground ring.

    No hypothesis beyond `q = -1`: nontriviality of `R_q` is supplied by
    instance search, so this is a statement about the actual ground ring rather
    than about some ring that might be trivial. It is still a statement about
    normalisation A at a root of unity, which `def:substrate-parameter` excludes
    — not about any `q` a QOU admits. -/
theorem groundRing_not_splits_at_neg_one (q : QOU.GroundRing.R_q) (hq : q = -1) :
    ¬ Splits q (-1) (1 : QOU.GroundRing.R_q) :=
  hecke_not_splits_at_neg_one q hq

end QOU.Mathlib.HeckeExtOne
