/-
# Q_β f-map power-class pincer — ζ₄ character-parity prune (Arm 2, §4.3)

Formalizes the **Arm-2** invariant of the Q_β f-map *power-class pincer* stated
(before any probe) in the scope doc
[`docs/scope/2026-07-06-qbeta-fmap-power-class-pincer-scope.md`](../../../../../docs/scope/2026-07-06-qbeta-fmap-power-class-pincer-scope.md)
(beans `571x`/`ebf5`/`2x2i`). The hypothesis class under attack is the minimal
non-linear f-map, the **pure power monomials** `f(Δtr_M) = A·(Δtr_M)^m`,
`m ∈ {1,…,6}` (C13 refuted only the *linear / bar-even* seedings; power maps are
the minimal non-linear class — the correct next structural target, *to refute or
constrain, not to fit*).

Arm 2 (ζ₄ character parity) is the fibre-level constraint: per bean `5nx8`'s
Lean-certified `IsZeta4Faithful` (`QOU.Mass.ComplexVolumeZeta4Partner`), any
candidate single-`𝔙` assembly is supported on the two **faithful** `±i`
characters of `ℤ₄` (its trivial- and sign-isotype orbit sums vanish). A monomial
power of a `ζ₄ = i` eigenfunction transforms with eigenvalue `i^m`; for **even**
`m` this is `i^m ∈ {±1}` — a *non-faithful* (trivial/sign) isotype. Hence an
even-degree monomial that is also ζ₄-faithful must vanish identically. This
**excludes the order-permitted `m = 4, 6` powers on the faithful arm**, with zero
anchor sweeps and no c_k value.

## What is proved here (sorry-free, generic base ring per §7c)

* `eigen_pow` — the eigenvalue of a monomial power: `A(σz) = ζ·A z ⟹
  Aᵐ(σz) = ζᵐ·Aᵐ z`. Pure algebra, generic `[CommRing R]`.
* `four_mul_eq_zero_of_eigen_sq_one` — an eigenfunction with eigenvalue `μ`,
  `μ² = 1`, whose trivial- and sign-isotype ℤ₄-orbit sums both vanish, satisfies
  `4·g z = 0` (the two isotypes each capture `2(1±μ)·g z`; their sum is
  `4·g z`). Generic `[CommRing R]`.
* `pow_even_faithful_four_mul_zero` — the pincer's Arm-2 core: for a `ζ₄`
  eigenfunction (`ζ² = −1`) and **even** `m`, ζ₄-faithfulness of the monomial
  power `Aᵐ` forces `4·Aᵐ ≡ 0`. Generic `[CommRing R]`.
* ℂ bridge to bean `5nx8`: `pow_even_isZeta4Faithful_eq_zero` (over ℂ, `4 ≠ 0`,
  so faithful ⟹ `Aᵐ ≡ 0`) and `exp_pow_even_not_isZeta4Faithful` — **no even
  power of the faithful carrier `exp` is ζ₄-faithful** (the concrete
  non-vacuous refutation: `exp 0 = 1 ≠ 0`).

This is a structural **prune**, not a closure: it kills the even-degree *monomial*
sub-class on the faithful arm. The surviving f-space is non-monomial and remains
open (merged into the keystone `W_λ` axis per the refuted-class map §3 / C14). No
c_k is proposed; nothing is wired; the registry is untouched.

**Verification status (2026-07-13).** Proofs are sorry-free and
**machine-verified** via `lean`-direct (exit 0) against the restored
`lake-cache/qou-v4-24-0` Mathlib oleans plus a freshly-rebuilt
`ComplexVolumeZeta4Partner.olean` (the cached dep olean was two days stale —
predating this file's `exp_zeta4_eigen` / `IsZeta4Faithful` dependencies — so
the dep was recompiled from current source before the check). The hand-audit
was confirmed correct: the only earlier obstacle was the stale dep olean, not
the proofs.

-- Ref: [leitner2026] docs/scope/2026-07-06-qbeta-fmap-power-class-pincer-scope.md §4.2–4.3
-/
import Mathlib.Tactic
import QOU.Mass.ComplexVolumeZeta4Partner

namespace QOU.Mass.QbetaFmapPowerClassPrune

/-! ## Generic core (any `CommRing`, no archimedean structure) -/

variable {X : Type*} {R : Type*} [CommRing R]

/-- A function `A : X → R` is an **eigenfunction** of a self-map `rot : X → X`
with eigenvalue `ζ` iff `A (rot z) = ζ · A z` for all `z`. This abstracts the
`ζ₄ = i` rotation `z ↦ z + iπ/2` of the fibre argument (whose `exp`-eigenfunction
is `exp_zeta4_eigen` in `ComplexVolumeZeta4Partner`). -/
def IsEigen (rot : X → X) (ζ : R) (A : X → R) : Prop := ∀ z, A (rot z) = ζ * A z

/-- **Eigenvalue of a monomial power.** If `A` is a `rot`-eigenfunction with
eigenvalue `ζ`, then the pointwise power `Aᵐ` is a `rot`-eigenfunction with
eigenvalue `ζᵐ`: `Aᵐ(rot z) = (ζ·A z)ᵐ = ζᵐ·Aᵐ z`. Pure algebra. -/
theorem eigen_pow {rot : X → X} {ζ : R} {A : X → R} (h : IsEigen rot ζ A) (m : ℕ) :
    IsEigen rot (ζ ^ m) (fun z => (A z) ^ m) := by
  intro z
  show (A (rot z)) ^ m = ζ ^ m * (A z) ^ m
  rw [h z, mul_pow]

/-- **Isotype collapse.** Let `g` be a `rot`-eigenfunction with eigenvalue `μ`,
`μ² = 1`. If both non-faithful ℤ₄ orbit sums vanish — the trivial isotype
`g z + g(rot z) + g(rot² z) + g(rot³ z)` and the sign isotype
`g z − g(rot z) + g(rot² z) − g(rot³ z)` — then `4·g z = 0`. (With `μ² = 1` the
two sums are `2(1+μ)·g z` and `2(1−μ)·g z`; their sum is `4·g z`.) -/
theorem four_mul_eq_zero_of_eigen_sq_one {rot : X → X} {μ : R} {g : X → R}
    (hg : IsEigen rot μ g) (hμ : μ ^ 2 = 1)
    (horbit : ∀ z, g z + g (rot z) + g (rot (rot z)) + g (rot (rot (rot z))) = 0)
    (hsign  : ∀ z, g z - g (rot z) + g (rot (rot z)) - g (rot (rot (rot z))) = 0)
    (z : X) : (4 : R) * g z = 0 := by
  have e1 : g (rot z) = μ * g z := hg z
  have e2 : g (rot (rot z)) = μ ^ 2 * g z := by rw [hg (rot z), hg z]; ring
  have e3 : g (rot (rot (rot z))) = μ ^ 3 * g z := by
    rw [hg (rot (rot z)), hg (rot z), hg z]; ring
  have ho := horbit z
  have hs := hsign z
  rw [e1, e2, e3] at ho hs
  linear_combination ho + hs - 2 * g z * hμ

/-- **Pincer Arm-2 core.** For a `ζ₄` eigenfunction (`ζ² = −1`) and an **even**
power `m`, ζ₄-faithfulness of the monomial power `Aᵐ` (both non-faithful orbit
sums vanish) forces `4·Aᵐ ≡ 0`. Because `m` is even, `μ = ζᵐ` has `μ² = ζ²ᵐ =
(ζ²)ᵐ = (−1)ᵐ = 1`, so the isotype collapse fires. Generic `[CommRing R]`. -/
theorem pow_even_faithful_four_mul_zero {rot : X → X} {ζ : R} {A : X → R}
    (hA : IsEigen rot ζ A) (hζ : ζ ^ 2 = -1) {m : ℕ} (hm : Even m)
    (horbit : ∀ z, (A z) ^ m + (A (rot z)) ^ m + (A (rot (rot z))) ^ m
        + (A (rot (rot (rot z)))) ^ m = 0)
    (hsign  : ∀ z, (A z) ^ m - (A (rot z)) ^ m + (A (rot (rot z))) ^ m
        - (A (rot (rot (rot z)))) ^ m = 0)
    (z : X) : (4 : R) * (A z) ^ m = 0 := by
  have hg : IsEigen rot (ζ ^ m) (fun z => (A z) ^ m) := eigen_pow hA m
  have hμ : (ζ ^ m) ^ 2 = 1 := by
    rw [← pow_mul, mul_comm m 2, pow_mul, hζ, hm.neg_one_pow]
  exact four_mul_eq_zero_of_eigen_sq_one hg hμ horbit hsign z

/-! ## ℂ bridge to bean `5nx8` (`IsZeta4Faithful`, `zeta4Rot`)

The generic core specialises to the concrete ζ₄ fibre model. Over ℂ, `4 ≠ 0`, so
`four_mul_eq_zero` upgrades to `Aᵐ ≡ 0`: **an even-degree monomial in a
ζ₄-faithful carrier vanishes identically.** The carrier `exp` (the `+i`
eigenvector, `exp_zeta4_eigen`) then gives the non-vacuous refutation. -/

open QOU.Mass.ComplexVolumeZeta4Partner

/-- `Complex.exp` is a `zeta4Rot`-eigenfunction with eigenvalue `i` (repackaging
`exp_zeta4_eigen`). -/
theorem exp_isEigen : IsEigen zeta4Rot Complex.I Complex.exp := fun z => exp_zeta4_eigen z

/-- **Even monomial powers of a ζ₄-faithful carrier vanish (over ℂ).** If `A` is
a `zeta4Rot`-eigenfunction with eigenvalue `i` and the even power `Aᵐ` is
`IsZeta4Faithful`, then `(A z)ᵐ = 0` for every `z`. (`4 ≠ 0` in ℂ upgrades the
generic `4·Aᵐ = 0`.) -/
theorem pow_even_isZeta4Faithful_eq_zero {A : ℂ → ℂ} (hA : IsEigen zeta4Rot Complex.I A)
    {m : ℕ} (hm : Even m) (hfaith : IsZeta4Faithful (fun z => (A z) ^ m)) (z : ℂ) :
    (A z) ^ m = 0 := by
  have hζ : (Complex.I) ^ 2 = -1 := Complex.I_sq
  obtain ⟨horbit, hsign⟩ := hfaith
  have h4 : (4 : ℂ) * (A z) ^ m = 0 :=
    pow_even_faithful_four_mul_zero hA hζ hm horbit hsign z
  have h4ne : (4 : ℂ) ≠ 0 := by norm_num
  exact (mul_eq_zero.mp h4).resolve_left h4ne

/-- **The concrete refutation.** No **even** power (`m > 0`) of the ζ₄-faithful
carrier `exp` is itself ζ₄-faithful: if it were, `pow_even_isZeta4Faithful_eq_zero`
at `z = 0` would give `(exp 0)ᵐ = 1ᵐ = 1 = 0`, false. This is the Arm-2 pincer
applied to a genuine faithful carrier — the even-degree pure-power monomial
f-maps are excluded on the faithful arm (bean `5nx8` `IsZeta4Faithful`), no
anchor sweep, no c_k. -/
theorem exp_pow_even_not_isZeta4Faithful {m : ℕ} (hm : Even m) (_hm0 : 0 < m) :
    ¬ IsZeta4Faithful (fun z => (Complex.exp z) ^ m) := by
  intro hfaith
  have hzero : (Complex.exp 0) ^ m = 0 :=
    pow_even_isZeta4Faithful_eq_zero exp_isEigen hm hfaith 0
  rw [Complex.exp_zero, one_pow] at hzero
  exact one_ne_zero hzero

/-- Specialisation to the exponential eigenfunction: if an even power `(Complex.exp ·) ^ m`
    satisfies `IsZeta4Faithful`, then `(Complex.exp z) ^ m = 0` at every `z : ℂ`. -/
theorem exp_pow_even_isZeta4Faithful_apply_eq_zero {m : ℕ} (hm : Even m)
    (hfaith : IsZeta4Faithful (fun z => (Complex.exp z) ^ m)) (z : ℂ) :
    (Complex.exp z) ^ m = 0 :=
  pow_even_isZeta4Faithful_eq_zero exp_isEigen hm hfaith z

end QOU.Mass.QbetaFmapPowerClassPrune
