import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# QOU.QuantumObservableUniverse.SelfDualityDegree — self-duality of 2-forms
exists in exactly one dimension, and the corpus asserts it in three

Bean `qou-xlw1`, epic `qou-8lxd`.  Companion to
`QOU.Eightfold.ContactDistributionRank`.

## The one fact everything below turns on

The Hodge star on an oriented `m`-dimensional space maps `Λ^k → Λ^{m−k}`.  It is
an **endomorphism** of `Λ^k` — the only way it can have `±1` eigenspaces, hence
the only way a self-dual/anti-self-dual splitting can exist — precisely when
`m − k = k`, i.e. `m = 2k`.

For `k = 2` that is `m = 4`, **and no other dimension**:

| `rank_ℝ H = 2n` | `n` | `dim M = 2n+1` | `dim Λ²H*` | `⋆ : Λ² →` | splitting? |
|---|---|---|---|---|---|
| 2 | 1 | **3** | 1 | `Λ⁰` | no |
| **4** | **2** | **5** | 6 | `Λ²` | **yes** |
| 6 | 3 | **7** | 15 | `Λ⁴` | no |
| 8 | 4 | 9 | 28 | `Λ⁶` | no |

## Why this matters here: the corpus asserts the splitting three times, at three
   incompatible dimensions

**(1) Categorically.**  `self-dual-ses.md` opens *"The `q`-Hodge star `⋆_q` is an
involution on `Ω²(A)`"*, and defines `Ω^±(A) = ker(id ∓ ⋆_q)`.  But
`categorical-hodge-star.md` defines `⋆ : Ω^k(A) → Ω^{n−k}(A)`, so `⋆_q` is an
endomorphism of `Ω²` only at calculus dimension `n = 4` — while
`brings-is-qou-verification.md:3` and `brings-is-qou-proof.md:10` declare the
calculus to be the **Woronowicz left-covariant 3-dimensional** one, `n = 3`,
where `⋆ : Ω² → Ω¹`.  No manifold is involved in this one; it is a typing
mismatch inside the categorical layer.

**(2) Archimedeanly, in general.**  `self-dual-2group.md`,
`emergence-to-quantum-flat-proof.md`, `glossary-quantum-flatness.md` and
`self-dual-ses.md` all write the simplicity constraint as
`B ∈ Γ(Λ^+H^* ⊗ Ad(P))` — the splitting is of `Λ²H^*`, the exterior square of
the **contact distribution**, not of the manifold's 2-forms.  By the table that
forces `rank_ℝ H = 4`, hence `n = 2`, hence `dim M = 5`.  This is what
`archimedean-realisations.md:3`'s *"the rank-4 distribution `H = ker Θ`"* is
recording, and it is **derived, not asserted** — it is the hypothesis under
which `Λ^±H^*` is well-formed at all.

**(3) In the worked example.**  `brings-qou-4tuple.md:12` builds `M_S` as the
unit circle bundle in `T*S` over Bring's surface, a Riemann surface of real
dimension 2 — so `M_S` is **3**-dimensional, `rank_ℝ H = 2`, and `Λ²H^*` is
**one**-dimensional.  There is no splitting to have.  Yet nineteen lines later
the same block defines the substrate parameter as
`q(p) = 1 + |⟨L_Θ, F_A^+⟩|(p)`.

So the framework's single substrate modulus is defined, in its own defining
block, by a quantity that does not exist at the dimension that block assigns.

## The three-way collision, stated plainly

Three requirements, three dimensions, pairwise exclusive
(`self_duality_and_eightfold_exclusive`, `bring_dim_admits_no_splitting`):

* **self-duality** (instanton, quantum flatness, `F_A^+`, `q(p)`) → `dim M = 5`;
* **the eightfold way** (`Λ³_ℂ ξ ≅ 𝟙`, `ContactDistributionRank`) → `dim M = 7`;
* **Bring's worked example** (`T*S` circle bundle) → `dim M = 3`.

No single contact manifold satisfies two of these.  In particular **fixing the
rank-3-vs-rank-4 disagreement in favour of either side does not open the
eightfold route** — 5 and 7 are as incompatible as 3 and 5.

## What is proved here, and what is not

**Proved (unconditional integer arithmetic):** the endomorphism criterion and
every row of the table; that the splitting exists at `rank_ℝ H = 4` and nowhere
else; that Bring's dimension admits none; that the calculus dimension must be 4
for `⋆_q` on `Ω²`; and the pairwise exclusions.

**Not proved, and asserted nowhere below:**

* that `Λ^±H^*` *should* be what the corpus means.  This file takes the corpus's
  own notation at face value and reports what it requires.  If the intended
  object were the 2-forms of the ambient `T*S` (a real 4-manifold, where the
  splitting does exist) rather than `Λ²H^*`, the general-theory blocks would
  need rewriting but the arithmetic below would be untouched.
* which resolution the author wants.  Both readings cost real content and the
  choice is not a measurement.
* anything about Woronowicz's classification.  That `𝒪_q(SU(2))` also admits
  **4-dimensional bicovariant** calculi is standard and cited, not formalised —
  `library/` holds no source on it, and the corpus declares only the 3D
  left-covariant one.

Base ring: none — integer arithmetic (§7c: no `ℝ`, no ring at all).
-/

namespace QOU.QuantumObservableUniverse.SelfDualityDegree

/-- The degree the Hodge star sends `Λ^k` to, on an `m`-dimensional space. -/
def hodgeTarget (m k : ℕ) : ℕ := m - k

/-- **The endomorphism criterion.**  `⋆ : Λ^k → Λ^{m−k}` is an endomorphism of
`Λ^k` — hence can carry a `±1` eigenspace splitting — exactly when `m = 2k`. -/
theorem hodgeTarget_eq_self_iff {m k : ℕ} (hk : k ≤ m) :
    hodgeTarget m k = k ↔ m = 2 * k := by
  simp only [hodgeTarget]
  omega

/-- **Self-duality of 2-forms exists in dimension 4 and nowhere else.** -/
theorem selfDual_two_forms_iff_dim_four {m : ℕ} (hm : 2 ≤ m) :
    hodgeTarget m 2 = 2 ↔ m = 4 := by
  simp only [hodgeTarget]
  omega

/-- The real rank of the contact distribution of a `(2n+1)`-manifold. -/
def distributionRealRank (n : ℕ) : ℕ := 2 * n

/-- The dimension of the CR manifold. -/
def crDim (n : ℕ) : ℕ := 2 * n + 1

/-- **`Λ^±H^*` forces CR dimension `n = 2`, hence `dim M = 5`.**  This is the
content of `archimedean-realisations.md:3`'s rank-4 claim: it is not an
assertion but the hypothesis under which the corpus's own simplicity constraint
`B ∈ Γ(Λ^+H^* ⊗ Ad(P))` is well-formed. -/
theorem splitting_forces_n_two {n : ℕ} (hn : 1 ≤ n)
    (h : hodgeTarget (distributionRealRank n) 2 = 2) : n = 2 := by
  simp only [hodgeTarget, distributionRealRank] at h
  omega

/-- …equivalently, `dim M = 5`. -/
theorem splitting_forces_dim_five {n : ℕ} (hn : 1 ≤ n)
    (h : hodgeTarget (distributionRealRank n) 2 = 2) : crDim n = 5 := by
  rw [splitting_forces_n_two hn h]; rfl

/-- **Bring's `M_S` admits no splitting.**  At `dim M_S = 3` the distribution has
real rank 2 and `Λ²H^*` is one-dimensional — `⋆` maps it to `Λ⁰`, so there is no
endomorphism and no `Λ^±`.  Hence `F_A^+` does not exist at that dimension. -/
theorem bring_dim_admits_no_splitting :
    hodgeTarget (distributionRealRank 1) 2 ≠ 2 := by decide

/-- And the exterior square is a line there, not a six-dimensional space with
room to split. -/
theorem bring_extSquare_is_a_line :
    Nat.choose (distributionRealRank 1) 2 = 1 := by decide

/-- At `n = 2` it is six-dimensional, which is what splits `3 + 3`. -/
theorem rank_four_extSquare_dim :
    Nat.choose (distributionRealRank 2) 2 = 6 := by decide

/-- **The categorical mismatch.**  `⋆_q : Ω^k(A) → Ω^{n−k}(A)` is an involution
*on `Ω²`* only at calculus dimension 4; the declared Woronowicz left-covariant
calculus has dimension 3, where `⋆` maps `Ω²` to `Ω¹`. -/
theorem categorical_star_needs_calculus_dim_four {ncal : ℕ} (h : 2 ≤ ncal) :
    hodgeTarget ncal 2 = 2 ↔ ncal = 4 :=
  selfDual_two_forms_iff_dim_four h

/-- The Woronowicz 3-dimensional calculus sends `Ω²` to `Ω¹`. -/
theorem woronowicz_three_star_target : hodgeTarget 3 2 = 1 := by decide

/-- The dimension the eightfold way requires, from
`ContactDistributionRank.complexRank_three_iff_dim_seven`. -/
def eightfoldDim : ℕ := 7

/-- The dimension self-duality requires. -/
def selfDualityDim : ℕ := 5

/-- Bring's worked example. -/
def bringDim : ℕ := 3

/-- **The three-way collision.**  No contact manifold satisfies two of the three
requirements — so resolving the rank-2-vs-rank-4 disagreement in *either*
direction leaves the eightfold route closed. -/
theorem three_requirements_pairwise_distinct :
    bringDim ≠ selfDualityDim ∧ selfDualityDim ≠ eightfoldDim ∧
      bringDim ≠ eightfoldDim := by
  refine ⟨by decide, by decide, by decide⟩

/-- Stated as the consequence that matters: fixing the rank disagreement does
**not** open the eightfold route. -/
theorem self_duality_and_eightfold_exclusive :
    selfDualityDim ≠ eightfoldDim := by decide

end QOU.QuantumObservableUniverse.SelfDualityDegree
