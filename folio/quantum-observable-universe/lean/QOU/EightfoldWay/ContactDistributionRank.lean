import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# QOU.Eightfold.ContactDistributionRank — the contact volume form gives a
**complex** rank-`n` object, and rank 3 forces `dim M = 7`

Bean `qou-xlw1`, epic `qou-8lxd`.  Companion to
`QOU.QuantumObservableUniverse.VolumeFormDegree` (the categorical side) and
`QOU.Eightfold.CircleBundleBettiObstruction` (which rules the corpus's contact
manifold out of being `S³`).

## The question

The owner asked whether the ambient `S³` of the Markov closure "has a natural
volume form" — whether a restriction of a tetraplectic or contact structure
supplies the degree-3 form the eightfold way needs.  The corpus does carry such
a form: `Θ ∧ dΘ` appears by name in four blocks, and
[`brings-qou-4tuple`](../../../brings-surface/brings-qou-4tuple.md) builds it
from the canonical Liouville form on `T*S`, so it is **natural rather than
postulated**.  It is nonetheless **prose tier** — zero `definition`, zero Lean,
and no block connects it to `Λ³`
([`2026-09-04-where-the-ambient-s3-comes-from`](../../../../../docs/audits/2026-09-04-where-the-ambient-s3-comes-from.md)).

This file supplies the arithmetic that decides the question, and the answer is
sharper than a yes or a no.

## Why the contact route is not the tangent-bundle route

Every previous `S³` attempt died on **Frobenius–Schur type**: the tangent bundle
of a real 3-manifold is a real rank-3 bundle, so it is self-dual, and
`QOU.Eightfold.Sym2GateFSTrichotomy.real_triple_fails_gate` excludes it.  Four
independent routes have now landed there — `𝔰𝔲(2) = Im ℍ`, the tetraplectic
`Sp(1)ⁿ`, the affine-`W` compactification, and `Ad(A)`.

**The contact distribution is a different object and it escapes that argument.**
On a contact `M^{2n+1}` with contact form `α`, the distribution `ξ = ker α` has
*real* rank `2n`, `dα|_ξ` is symplectic, and a compatible `J` makes `ξ` a
**complex** bundle of **complex rank `n`**.  A complex bundle is not
self-conjugate by construction, so the type obstruction does not apply to it.
This is the first `S³`-adjacent route that survives it.

What it does not survive is the arithmetic below.

## The arithmetic, and what it decides

`ξ` is complex rank `n = (dim M − 1)/2`.  So the eightfold's `Λ³_ℂ ξ ≅ 𝟙` —
the trivial-canonical-bundle / Sasaki–Einstein condition — needs `n = 3`, hence

  **`dim M = 7`, and no other dimension.**

Read against the corpus's own candidates that is decisive, and negative for
every one of them:

| manifold | `dim` | `n` | complex rank of `ξ` | supplies `W`? |
|---|---|---|---|---|
| any `S³` — `S³_AM`, `S³_Reeb`, `SU(2)` | `3` | `1` | **1** (a complex *line*) | no |
| `M_S` under the 3-dimensional reading | `3` | `1` | **1** | no |
| `M_S` under the rank-4 `ker Θ` reading | `5` | `2` | **2** | no |
| what would be needed | `7` | `3` | `3` | yes |

So the contact structure on **any three-dimensional** manifold gives a complex
line, not a three-dimensional object — and that is a statement about the
dimension, independent of which `S³` is meant, which is what makes it robust to
the three-way `S³` ambiguity the corpus carries.

**The degree-1 accident, again.**  At `n = 1` the canonical bundle `Λ¹_ℂ ξ` *is*
`ξ` itself, exactly as `Λ^{N-1}W = W` iff `N = 2` in `VolumeFormDegree`.  Both
files are recording the same shape: the low case is degenerate because the
exterior power collapses onto its argument, and it is that collapse — not a
property of volume forms — that the corpus has been reading as structure.

**Where it points.** `dim M = 7` is where `qou-8p1f`'s three-forms-with-an-open-
orbit case lives (`G₂`), and `qou-uq5x` independently found `S⁶ = G₂/SU(3)`
viable with complex `𝟑` isotropy.  Two legs reached from opposite directions —
contact/CR and octonionic — arrive at 7 and at a complex 3-dimensional object.
That convergence is a **lead, and is asserted nowhere below**.

## What is proved here, and what is not

**Proved (unconditional integer arithmetic):** the whole table — the
odd-dimension parametrisation, that the complex rank determines the dimension
and conversely, that complex rank 3 holds exactly at `dim M = 7`, that no
3-dimensional contact manifold gives complex rank 3, and the degree-1 collapse.

**Not proved, and asserted nowhere below:**

* that a compatible `J` **exists** on `ker Θ` for the corpus's `Θ`.  A contact
  distribution admits one (the space of compatible `J` is contractible and
  non-empty), but that is a cited fact about contact geometry, not something
  stated here, and nothing in the corpus attaches a `J` to `ker Θ`.
* that `Λ^n_ℂ ξ ≅ 𝟙` **holds** for any manifold in the corpus.  Triviality of
  the canonical bundle is a genuine geometric condition (Sasaki–Einstein), not a
  consequence of being contact.  This file says which `n` it *would* require.
* the identification of `ξ` with a fundamental object of the braided category.
  Mathlib has exterior powers of **modules** (`⋀[R]^n M`,
  `Mathlib.LinearAlgebra.ExteriorPower.Basic`) and of `ModuleCat`, but no `Λ^k`
  of an **object of an abstract monoidal category** and no wedge product as a
  named operation; it has differential forms with `extDeriv` on a **normed
  space** (`Mathlib.Analysis.Calculus.DifferentialForm.Basic`) but none on
  **manifolds** — so every declaration below is about `ℕ`.
* anything about `dim M` for the corpus's `M_S`, which the corpus states
  inconsistently — 3-dimensional in one block, `ker Θ` of rank 4 (hence 5) in two
  others.  The table above is stated for **both** readings precisely because that
  contradiction is unresolved and is the author's to settle.

Base ring: none — integer arithmetic (§7c: no `ℝ`, no ring at all).
-/

namespace QOU.Eightfold.ContactDistributionRank

/-- The dimension of a contact manifold with `n`-fold symplectic
distribution: `dim M = 2n + 1`. -/
def contactDim (n : ℕ) : ℕ := 2 * n + 1

/-- The **real** rank of the contact distribution `ξ = ker α`. -/
def distributionRealRank (n : ℕ) : ℕ := 2 * n

/-- The **complex** rank of `ξ` once a compatible `J` is chosen — half the real
rank.  This is the object whose top exterior power the eightfold way needs. -/
def distributionComplexRank (n : ℕ) : ℕ := n

/-- The degree of the contact volume form `α ∧ (dα)^n`: the top degree. -/
def volumeFormDegree (n : ℕ) : ℕ := contactDim n

@[simp] theorem volumeFormDegree_eq (n : ℕ) : volumeFormDegree n = 2 * n + 1 := rfl

/-- The volume form is a top form: its degree is the manifold's dimension.
This is what makes it a *volume* form rather than merely a closed form. -/
theorem volumeFormDegree_eq_contactDim (n : ℕ) :
    volumeFormDegree n = contactDim n := rfl

/-- The contact volume form's degree is always **odd** — so it can never equal
the *even* degree an exterior square would need, at any `n`. -/
theorem volumeFormDegree_odd (n : ℕ) : volumeFormDegree n % 2 = 1 := by
  simp only [volumeFormDegree_eq]; omega

/-- The real rank of the distribution is one less than the dimension. -/
theorem realRank_succ (n : ℕ) : distributionRealRank n + 1 = contactDim n := by
  simp [distributionRealRank, contactDim]

/-- **The complex rank determines the dimension.**  `dim M = 2·rank_ℂ ξ + 1`. -/
theorem contactDim_eq_two_mul_complexRank (n : ℕ) :
    contactDim n = 2 * distributionComplexRank n + 1 := rfl

/-- …and conversely, so the two are interchangeable data. -/
theorem complexRank_of_contactDim {n d : ℕ} (h : contactDim n = d) :
    distributionComplexRank n = (d - 1) / 2 := by
  simp only [contactDim] at h
  simp only [distributionComplexRank]
  omega

/-- **The decision.**  The contact distribution is complex rank `3` — the rank
the eightfold way needs for `Λ³_ℂ ξ ≅ 𝟙` — exactly when the manifold is
**seven**-dimensional. -/
theorem complexRank_three_iff_dim_seven {n : ℕ} :
    distributionComplexRank n = 3 ↔ contactDim n = 7 := by
  simp only [distributionComplexRank, contactDim]
  omega

/-- **No three-dimensional manifold can supply it.**  At `dim M = 3` the
distribution is a complex *line*.  This is the statement that closes the `S³`
route, and it is a statement about the dimension alone — so it holds for all
three of the corpus's distinct `S³`s (`S³_AM`, `S³_Reeb`, `SU(2)`) at once,
without needing that ambiguity resolved. -/
theorem dim_three_gives_complex_line {n : ℕ} (h : contactDim n = 3) :
    distributionComplexRank n = 1 := by
  simp only [contactDim] at h
  simp only [distributionComplexRank]
  omega

/-- Restated as the exclusion: a 3-dimensional contact manifold does **not**
give complex rank 3. -/
theorem dim_three_not_complex_rank_three {n : ℕ} (h : contactDim n = 3) :
    distributionComplexRank n ≠ 3 := by
  rw [dim_three_gives_complex_line h]; norm_num

/-- The other reading of the corpus's `M_S` (`ker Θ` of rank 4, hence `dim = 5`)
fails too — complex rank `2`, not `3`. -/
theorem dim_five_gives_complex_rank_two {n : ℕ} (h : contactDim n = 5) :
    distributionComplexRank n = 2 := by
  simp only [contactDim] at h
  simp only [distributionComplexRank]
  omega

/-- **Both readings of `M_S` fail, so the contradiction in the corpus does not
need resolving to settle this question.**  Whether `ker Θ` has rank 2 or rank 4,
the complex rank is 1 or 2 and never 3. -/
theorem m_s_fails_either_reading {n : ℕ} (h : contactDim n = 3 ∨ contactDim n = 5) :
    distributionComplexRank n ≠ 3 := by
  rcases h with h | h
  · exact dim_three_not_complex_rank_three h
  · rw [dim_five_gives_complex_rank_two h]; norm_num

/-- **The degree-1 collapse — the same shape as `VolumeFormDegree`.**  At `n = 1`
the canonical bundle `Λ^n_ℂ ξ` is `Λ¹_ℂ ξ = ξ` itself, exactly as
`Λ^{N-1}W = Λ¹W = W` iff `N = 2` there.  The low case is degenerate because the
exterior power collapses onto its argument. -/
theorem canonicalDegree_eq_one_iff_complexRank_one {n : ℕ} :
    distributionComplexRank n = 1 ↔ contactDim n = 3 := by
  simp only [distributionComplexRank, contactDim]
  omega

/-- The dimension the eightfold way requires, named. -/
theorem eightfold_requires_dim_seven :
    contactDim 3 = 7 ∧ distributionComplexRank 3 = 3 := by
  constructor <;> rfl

/-- And `S³`'s own contact data, named, for the same reason. -/
theorem sphere_three_contact_data :
    contactDim 1 = 3 ∧ distributionComplexRank 1 = 1 ∧ volumeFormDegree 1 = 3 := by
  refine ⟨rfl, rfl, rfl⟩

/-- The volume form has degree 3 at `dim M = 3` — which is *why* the route looked
promising — while the object it is a top form **of** has complex rank 1.  The two
threes are different threes, and conflating them is the trap this file exists to
close. -/
theorem degree_three_but_rank_one {n : ℕ} (h : contactDim n = 3) :
    volumeFormDegree n = 3 ∧ distributionComplexRank n ≠ 3 :=
  ⟨by rw [volumeFormDegree_eq_contactDim]; exact h, dim_three_not_complex_rank_three h⟩

section ThreeSasakian

/-! ## The 3-Sasakian rung, and a second pair of "different threes"

The corpus carries a **Bring-cone 3-Sasakian structure**, which it itself calls
*"degenerate quaternionic-contact"*
([`bring-cone-reeb-quaternionic-twist.md:4`](../../../brings-surface/bring-cone-reeb-quaternionic-twist.md)) —
`4n + 3` at `n = 0`.  Since `dim M = 7` is `4n + 3` at `n = 1`, it is worth
saying exactly how far that is from what the eightfold needs, and exactly which
distribution the question is about.  Both are one line of arithmetic, and the
second is a trap of the same shape as `degree_three_but_rank_one`.
-/

/-- The dimension of a 3-Sasakian manifold: `4n + 3`. -/
def threeSasakianDim (n : ℕ) : ℕ := 4 * n + 3

/-- **A 3-Sasakian manifold is contact, with Sasakian parameter `2n + 1`.**
Each of its three Sasakian structures has a contact form whose distribution has
complex rank `2n + 1`. -/
theorem threeSasakianDim_eq_contactDim (n : ℕ) :
    threeSasakianDim n = contactDim (2 * n + 1) := by
  simp only [threeSasakianDim, contactDim]; omega

/-- So the **Sasakian** complex rank of a 3-Sasakian manifold is `2n + 1`, and it
is `3` exactly at `n = 1`, i.e. exactly in dimension 7. -/
theorem threeSasakian_complexRank_three_iff {n : ℕ} :
    distributionComplexRank (2 * n + 1) = 3 ↔ threeSasakianDim n = 7 := by
  simp only [distributionComplexRank, threeSasakianDim]
  omega

/-- **The corpus's own case is `n = 0`, hence dimension 3, hence complex rank 1.**
The gap between what it has and what the eightfold needs is exactly one step in
`n`. -/
theorem bring_cone_degenerate_case :
    threeSasakianDim 0 = 3 ∧ distributionComplexRank (2 * 0 + 1) = 1 := by
  refine ⟨rfl, rfl⟩

/-- The **quaternionic-contact** distribution of a 3-Sasakian manifold — the
common kernel of all three contact forms — has real rank `4n`. -/
def quaternionicContactRealRank (n : ℕ) : ℕ := 4 * n

/-- …hence complex rank `2n`. -/
def quaternionicContactComplexRank (n : ℕ) : ℕ := 2 * n

/-- **The second pair of different threes.**  In dimension 7 the *Sasakian*
distribution has complex rank `3` — what the eightfold needs — while the
*quaternionic-contact* distribution has complex rank `2`.  They are distributions
of different rank on the same manifold, and only one of them answers the
question. -/
theorem dim_seven_two_distributions :
    distributionComplexRank (2 * 1 + 1) = 3 ∧ quaternionicContactComplexRank 1 = 2 := by
  refine ⟨rfl, rfl⟩

/-- The quaternionic-contact distribution never has complex rank 3, at any `n` —
its complex rank is even. -/
theorem quaternionicContact_never_rank_three (n : ℕ) :
    quaternionicContactComplexRank n ≠ 3 := by
  simp only [quaternionicContactComplexRank]; omega

end ThreeSasakian

end QOU.Eightfold.ContactDistributionRank
