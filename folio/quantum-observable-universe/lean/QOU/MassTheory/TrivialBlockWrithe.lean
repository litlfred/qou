import Mathlib.Algebra.GroupWithZero.Units.Lemmas
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Tactic

/-!
# QOU.MassTheory.TrivialBlockWrithe — the 1-dim Hecke block characters are writhe monomials

Formalize-first prune for the charm-mass **Frobenius/Wedderburn block-projection**
route (`docs/audits/2026-08-02-charm-mass-frobenius-block-projection-negative.md`,
PR #4594). The generation hierarchy was tested as the ratio of $H_3$ Wedderburn
blocks $y_\lambda\chi_\lambda$ on the Borromean baryon braid and came out $O(1)$
(1.35), not the observed $O(100)$ charm/light hierarchy.

This file proves the **structural reason**: the two 1-dimensional block
characters of $H_n(q)$ — the trivial $[n]$ block ($\sigma_i\mapsto q$) and the
sign $[1^n]$ block ($\sigma_i\mapsto -q^{-1}$) — are **pure writhe monomials**:

  `χ_triv(β) = q ^ writhe(β)`,   `χ_sign(β) = (-q⁻¹) ^ writhe(β)`.

Consequently, on a **writhe-balanced** braid (writhe $= 0$, e.g. the Borromean
baryon $(\sigma_1\sigma_2^{-1})^3$) *both* 1-dim block characters collapse to `1`
independent of `q` — they carry no winding / generation information, so their
mutual ratio is pinned to `1` and any hierarchy would have to come entirely from
the remaining 2-dimensional `[2,1]` block. That last step is **not** proved here
(no bound on the `[2,1]` character is claimed), so this is a **scope-(a)
sharpening** of the block-ratio negative, not a structural exclusion of the
complex-mass functional: it says do not look for the generation hierarchy in the
*1-dim* blocks at balanced writhe, and it measures how much the 2-dim block
would have to supply.

A braid word is modelled as `List ℤ`: each letter is a **signed generator**
(nonzero integer; the *sign* is the crossing sign $\pm$, the magnitude is the
generator index, irrelevant to a 1-dim representation where every $\sigma_i$ maps
to the same scalar). The writhe is the sum of the crossing signs.

Base ring (§7c): generic `[DivisionRing R]` — the identities are pure algebra
(`zpow` over a nonzero scalar, plus the ring negation for the sign block's
`-q⁻¹`), no archimedean construct. `q ≠ 0` is the only hypothesis (a Hecke
eigenvalue is a unit).

This file is **sorry-free** and self-contained: it imports only Mathlib and
depends on no QOU block. The route it prunes is scoped against
`conj:complex-mass-constituent-functional`, which is **not yet on `main`** (open
draft PR #4584) — that is a forward reference for the reader, not a dependency.

-- Ref: [leitner2026] docs/audits/2026-08-02-charm-mass-frobenius-block-projection-negative.md
-/

namespace QOU.MassTheory.TrivialBlockWrithe

variable {R : Type*} [DivisionRing R]

/-- Writhe of a braid word = sum of the crossing signs. -/
def writhe (w : List ℤ) : ℤ := (w.map Int.sign).sum

/-- Character of the **trivial** ($[n]$) 1-dim Hecke block on a braid word:
each positive crossing contributes `q`, each negative `q⁻¹` (= `q ^ sign`). -/
def chiTrivial (q : R) (w : List ℤ) : R := (w.map (fun g => q ^ (Int.sign g))).prod

/-- Character of the **sign** ($[1^n]$) 1-dim Hecke block on a braid word:
each generator maps to the second Hecke eigenvalue `-q⁻¹`, so the letter
contributes `(-q⁻¹) ^ sign`. -/
def chiSign (q : R) (w : List ℤ) : R := (w.map (fun g => (-q⁻¹) ^ (Int.sign g))).prod

@[simp] theorem writhe_nil : writhe ([] : List ℤ) = 0 := rfl

@[simp] theorem writhe_cons (a : ℤ) (w : List ℤ) :
    writhe (a :: w) = Int.sign a + writhe w := by
  simp [writhe]

/-- **Trivial-block character is a writhe monomial:** `χ_triv(β) = q ^ writhe(β)`.
The falsifiable content — a 1-dim block sees *only* the writhe, not the braid's
internal structure. Proved by list induction + `zpow_add₀` (needs `q ≠ 0`). -/
theorem chi_trivial_eq_q_zpow_writhe (q : R) (hq : q ≠ 0) (w : List ℤ) :
    chiTrivial q w = q ^ (writhe w) := by
  induction w with
  | nil => simp [chiTrivial]
  | cons a t ih =>
      unfold chiTrivial at ih ⊢
      rw [List.map_cons, List.prod_cons, ih, writhe_cons, zpow_add₀ hq]

/-- **Sign-block character is a writhe monomial:** `χ_sign(β) = (-q⁻¹) ^ writhe(β)`. -/
theorem chi_sign_eq_negqinv_zpow_writhe (q : R) (hq : q ≠ 0) (w : List ℤ) :
    chiSign q w = (-q⁻¹) ^ (writhe w) := by
  have hne : (-q⁻¹ : R) ≠ 0 := by simpa using inv_ne_zero hq
  induction w with
  | nil => simp [chiSign]
  | cons a t ih =>
      unfold chiSign at ih ⊢
      rw [List.map_cons, List.prod_cons, ih, writhe_cons, zpow_add₀ hne]

/-- **The prune.** On a writhe-balanced braid (`writhe w = 0`) the trivial-block
character collapses to `1`, independent of `q`: a balanced baryon braid carries
no generation information in its trivial block. -/
theorem chi_trivial_writhe_zero (q : R) (hq : q ≠ 0) (w : List ℤ)
    (hw : writhe w = 0) : chiTrivial q w = 1 := by
  rw [chi_trivial_eq_q_zpow_writhe q hq w, hw, zpow_zero]

/-- Likewise the sign block collapses to `1` at writhe 0. -/
theorem chi_sign_writhe_zero (q : R) (hq : q ≠ 0) (w : List ℤ)
    (hw : writhe w = 0) : chiSign q w = 1 := by
  rw [chi_sign_eq_negqinv_zpow_writhe q hq w, hw, zpow_zero]

/-- The **Borromean baryon** $(\sigma_1\sigma_2^{-1})^3$ has writhe `0`: three
positive `σ₁` (letter `1`) and three negative `σ₂⁻¹` (letter `-2`). Concrete,
decidable. -/
theorem writhe_borromean : writhe [1, -2, 1, -2, 1, -2] = 0 := by decide

/-- Both 1-dim block characters of the Borromean baryon are pinned to `1` — the
generation hierarchy provably cannot come from these blocks' ratio. -/
theorem borromean_1dim_blocks_trivial (q : R) (hq : q ≠ 0) :
    chiTrivial q [1, -2, 1, -2, 1, -2] = 1 ∧
    chiSign q [1, -2, 1, -2, 1, -2] = 1 :=
  ⟨chi_trivial_writhe_zero q hq _ writhe_borromean,
   chi_sign_writhe_zero q hq _ writhe_borromean⟩

end QOU.MassTheory.TrivialBlockWrithe
