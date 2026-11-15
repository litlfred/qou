import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# QOU.QuantumObservableUniverse.CalculusDimensionObstruction — the categorical
route gives the volume form and the distribution, and it kills self-duality
without ever mentioning a manifold

Bean `qou-xlw1`, epic `qou-8lxd`.  Fourth companion to
`QOU.QuantumObservableUniverse.SelfDualityDegree`,
`QOU.Eightfold.ContactDistributionRank`, `QOU.Eightfold.HyperbolicVolumeFormType`.

## The question

Asked by the owner: *"Is there perhaps a category-theoretic approach that might
give the needed volume forms and distributions?"*

**Yes, and the corpus already has both.**  They are not archimedean objects that
have to be transported into the category — they are objects of the differential
calculus on `A = 𝒪_q(SU(2))`, and no manifold appears anywhere in their
construction.

## Where they already are

`quantum-observable-universes/categorical-reeb-brings.md` gives the whole
package, from the **Woronowicz left-covariant 3-dimensional calculus**:

* `Ω¹(A)` is free of rank **3** over `A`, with left-invariant basis
  `ω₊, ω₋, ω₃`;
* the **contact form** is `Θ_A = ω₃`, normalised by `ω₃(e₃) = 1`;
* the **structure equation** is `dΘ_A = −q⁻¹ ω₊ ∧ ω₋`;
* hence the **distribution** `H_A := ker Θ_A = span_A{ω₊, ω₋}`, free of rank
  **2**;
* hence the **volume form** `Θ_A ∧ dΘ_A = −q⁻¹ ω₃ ∧ ω₊ ∧ ω₋`, which is the top
  form of `Ω^•(A)`.

So the categorical layer supplies a contact form, a rank-2 distribution and a
degree-3 volume form outright.  What it does *not* supply is a **complex** rank-3
object — that remains `Λ³W ≅ 𝟙`, i.e. condition 5 at degree 3, which is bean
`qou-j3w6` and the author's.

## The obstruction this file proves, and it is stronger than the geometric one

Write `d` for the dimension of the calculus — the rank of `Ω¹(A)` over `A`.  Then
`ker Θ` has rank `d − 1`, and two requirements the corpus places on the same
calculus pull in opposite directions:

* **A contact form needs `d` ODD.**  `dΘ` restricted to `ker Θ` must be
  non-degenerate and alternating, so `ker Θ` has **even** rank; `d − 1` even
  means `d` odd (`contact_forces_odd`).
* **Self-duality of 2-forms needs `d = 4`.**  `⋆ : Ω^k → Ω^{d−k}` is an
  endomorphism of `Ω²` — the only way `Ω^± = ker(id ∓ ⋆)` can be defined — iff
  `d = 4` (`selfDual_forces_four`, and `SelfDualityDegree` for the same fact one
  layer down).

**Four is even.  So no differential calculus carries both**
(`no_calculus_has_both`).  `self-dual-ses.md` asserts `⋆_q` is an involution on
`Ω²(A)` and `categorical-reeb-brings.md` builds a contact form on the same `A`;
those two blocks cannot both be describing one calculus.

This is the categorical form of what `SelfDualityDegree` proves archimedeanly —
and it is **stronger**, because it needs no manifold, no metric, no `H = ker Θ ⊂
TM`, and no resolution of the corpus's three-way `S³` ambiguity.  It is a
statement about `Ω^•(A)` alone.

## The dimension dictionary, and what it says about the rank dispute

Matching the two layers, `rank_ℝ(ker Θ) = d − 1` categorically and `= 2n`
archimedeanly, so `d = 2n + 1 = dim M`: **the calculus dimension is the manifold
dimension** (`calculusDim_eq_crDim`).  The declared Woronowicz calculus has
`d = 3`, giving `n = 1`, `rank H = 2`, `dim M = 3`.

That is a **third independent vote for the 3-dimensional reading**, after Bring's
`T*S` construction and the nine `dim M_S = 3` sites — and it is the only one of
the three with no geometry in it at all.  The rank-4 reading would need `d = 5`
(rank-4 distribution, still odd `d`, still contact) — **not** the 4-dimensional
bicovariant calculus, which by the above is not contact at all.

## What is proved here, and what is not

**Proved (unconditional integer arithmetic):** the parity argument, that `d = 4`
is forced by self-duality and excluded by contactness, the exterior-algebra
dimensions of a rank-3 calculus, that `Θ ∧ dΘ` sits in top degree there, and the
calculus/manifold dimension dictionary.

**Not proved, and asserted nowhere below:**

* the Woronowicz structure equations, or that `Ω¹(𝒪_q(SU(2)))` is free of rank 3
  in the left-covariant calculus.  Cited — `categorical-reeb-brings.md` and
  `brings-is-qou-verification.md:3` state them; Mathlib has no covariant-
  differential-calculus API.
* that `𝒪_q(SU(2))` admits 4-dimensional **bicovariant** calculi.  Standard
  (Woronowicz's classification), cited, and `library/` holds no source on it.
* that a contact distribution *must* carry a compatible complex structure, or
  anything about Frobenius–Schur type.  That is `ContactDistributionRank`.
* which degree condition 5 should carry.  `qou-j3w6`, the author's.

Base ring: none — integer arithmetic (§7c: no `ℝ`, no ring at all).
-/

namespace QOU.QuantumObservableUniverse.CalculusDimensionObstruction

/-- The rank of `ker Θ` inside a calculus of dimension `d`: one less. -/
def distributionRank (d : ℕ) : ℕ := d - 1

/-- The degree the categorical Hodge star sends `Ω^k` to. -/
def starTarget (d k : ℕ) : ℕ := d - k

/-- **Contactness forces the calculus dimension to be odd.**  `dΘ` restricted to
`ker Θ` is alternating and non-degenerate, so `ker Θ` has even rank. -/
theorem contact_forces_odd {d : ℕ} (hd : 1 ≤ d)
    (h : distributionRank d % 2 = 0) : d % 2 = 1 := by
  simp only [distributionRank] at h
  omega

/-- **Self-duality of 2-forms forces the calculus dimension to be 4.**  Same fact
as `SelfDualityDegree.selfDual_two_forms_iff_dim_four`, restated for a calculus. -/
theorem selfDual_forces_four {d : ℕ} (hd : 2 ≤ d) :
    starTarget d 2 = 2 ↔ d = 4 := by
  simp only [starTarget]
  omega

/-- **No differential calculus carries both.**  Self-duality needs `d = 4`;
contactness needs `d` odd; `4` is even.

This is the categorical form of the archimedean obstruction, and it needs no
manifold, no metric, and no resolution of the `S³` ambiguity. -/
theorem no_calculus_has_both {d : ℕ} (hd : 2 ≤ d)
    (hcontact : distributionRank d % 2 = 0)
    (hselfdual : starTarget d 2 = 2) : False := by
  have h4 : d = 4 := (selfDual_forces_four hd).mp hselfdual
  have hodd : d % 2 = 1 := contact_forces_odd (by omega) hcontact
  omega

/-- The Woronowicz left-covariant calculus: `d = 3`, distribution rank 2, odd —
contact, as `categorical-reeb-brings.md` builds it. -/
theorem woronowicz_is_contact :
    distributionRank 3 = 2 ∧ (3 : ℕ) % 2 = 1 ∧ distributionRank 3 % 2 = 0 := by
  refine ⟨rfl, by decide, by decide⟩

/-- …and at `d = 3` the star sends `Ω²` to `Ω¹`, so `Ω^±` is not definable. -/
theorem woronowicz_has_no_selfDuality : starTarget 3 2 ≠ 2 := by decide

/-- The dimension of `Ω^k` for a calculus of dimension `d`. -/
def formDim (d k : ℕ) : ℕ := Nat.choose d k

/-- The exterior algebra of the Woronowicz 3-dimensional calculus: `1, 3, 3, 1`. -/
theorem woronowicz_form_dims :
    formDim 3 0 = 1 ∧ formDim 3 1 = 3 ∧ formDim 3 2 = 3 ∧ formDim 3 3 = 1 := by
  refine ⟨rfl, rfl, rfl, rfl⟩

/-- **`Θ ∧ dΘ` is a top form there.**  `Θ` has degree 1 and `dΘ` degree 2, so the
wedge has degree 3 — which is the top degree of a 3-dimensional calculus, and
`Ω³` is one-dimensional.  So the categorical volume form is a genuine volume
form, constructed with no manifold. -/
theorem contact_volume_is_top :
    1 + 2 = 3 ∧ formDim 3 3 = 1 := by
  refine ⟨rfl, rfl⟩

/-- **The dimension dictionary.**  Matching `rank(ker Θ) = d − 1` categorically
against `2n` archimedeanly gives `d = 2n + 1`: the calculus dimension is the
manifold dimension. -/
def crDim (n : ℕ) : ℕ := 2 * n + 1

theorem calculusDim_eq_crDim {d n : ℕ} (hd : 1 ≤ d)
    (h : distributionRank d = 2 * n) : d = crDim n := by
  simp only [distributionRank] at h
  simp only [crDim]
  omega

/-- The declared calculus gives `n = 1`, hence `dim M = 3` — a third independent
vote for the 3-dimensional reading, and the only one with no geometry in it. -/
theorem woronowicz_gives_n_one : distributionRank 3 = 2 * 1 ∧ crDim 1 = 3 := by
  refine ⟨rfl, rfl⟩

/-- The rank-4 distribution the self-duality blocks need would come from a
**five**-dimensional calculus, still odd and still contact — not from the
4-dimensional bicovariant one, which by `no_calculus_has_both` is not contact. -/
theorem rank_four_needs_calculus_five :
    distributionRank 5 = 4 ∧ (5 : ℕ) % 2 = 1 ∧ crDim 2 = 5 := by
  refine ⟨rfl, by decide, rfl⟩

end QOU.QuantumObservableUniverse.CalculusDimensionObstruction
