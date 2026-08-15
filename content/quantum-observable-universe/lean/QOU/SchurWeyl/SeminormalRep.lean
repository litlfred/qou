import QOU.SchurWeyl.TableauCells
import QOU.SchurWeyl.SeminormalParam

/-!
# `QOU.SchurWeyl.SeminormalRep` — the generator matrices on all of `SYT μ` (bean `qou-gjg6`)

Step (ii) of the general-`λ` construction, taking **route (c)** of the three recorded in
bean `qou-7xt3`: rather than building an object for "the `⟨s_k, s_{k+1}⟩`-orbit" and
assembling block-diagonally, define the generator matrix on *all* of `SYT μ` at once, with
the per-generator trichotomy (`axialDist_trichotomy`) supplying the case split, and use the
orbit-local identities (`Orbit3Braid`, `Orbit6Braid`, `seminormalBlock`) only as the
algebraic content of the relations.

Why (c) rather than (a) or (b): the `s_k`-action `swapTableau` is **partial** — defined only
under `SwapAdmissible` — so an "orbit" is a connected component under partial moves, not a
group orbit, and formalising that notion is itself the work.  Routes (a) and (b) both force
one to build the per-orbit basis correspondence that makes `Orbit3Braid`/`Orbit6Braid`'s
explicit index orderings usable.  Indexing the matrix by `SYT μ` directly sidesteps the
correspondence: there is no re-indexing to justify.

## What is delivered here

* `offDiag q d` — the off-diagonal entry of a size-`2` orbit pair, carrying the orientation
  convention: the member with **negative** axial distance is "first" and its column gets
  `1 + a(d)·a(-d)`; the other gets the plain `1`.  This is the asymmetry of the
  square-root-free (seminormal, not orthogonal) form, and it is the convention fixed by the
  verified `(2,1)` instance and used throughout `Orbit3Braid` / `Orbit6Braid`.
* `genMat q k` — the matrix of `σ_k`, indexed by `SYT μ` on both sides:
  - the diagonal is `a(axialDist T k)` **uniformly**, which is what makes the trichotomy a
    case split on *block size* only: at axial distance `±1` (a size-`1` orbit) `a` is the
    scalar `q` resp. `-q⁻¹`, by `seminormalParam_one` / `_neg_one`;
  - the entry at `(s_k·T, T)` is `offDiag`, when the swap is admissible;
  - everything else is `0`.
* `genMat_diag`, `genMat_of_not_admissible`, `genMat_apply_of_ne` — the computation rules.
* `genMat_quadratic` — **the Hecke quadratic relation `σ² = (q - q⁻¹)σ + 1`, on all of
  `SYT μ` at once**, for arbitrary shape.  This is what route (c) was chosen for: the
  relation is proved *globally*, not one orbit at a time and then glued.

## Scope

The quadratic relation is proved.  **Far commutation and the braid relation are not** —
they remain open under bean `qou-gjg6`, and `hoefsmit_seminormal_rep` keeps its
`-- Ref:`-cited `sorry` until all three are in hand.

The quadratic is the *easy* one of the three, and it is worth saying why: it is
**column-local**.  Each column of `genMat` has support in `{T, s_k·T}`
(`sum_mul_genMat_column`), so `(M²)_{·,T}` never sees a third tableau and the identity
reduces to a `2 × 2` Cayley–Hamilton — trace `q - q⁻¹` by `seminormalParam_add_neg`,
determinant `-1` by `offDiag_mul_neg`.  The braid relation is not column-local: it mixes
`σ_k` and `σ_{k+1}`, whose supports differ, and that is exactly the content of
`Orbit3Braid` / `Orbit6Braid`.

Refs:
- [hoefsmit1974] Hoefsmit, PhD thesis (UBC 1974) — the seminormal form.
- [ram1997] Ram, *Seminormal representations of Weyl groups and Iwahori–Hecke algebras*,
  https://doi.org/10.1112/S0024611597000373 — the axial-distance formulas.
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)
open TableauCells Seminormal

namespace SeminormalRep

variable {μ : YoungDiagram} (q : ℝ)

/-- The off-diagonal entry of a size-`2` orbit pair, at axial distance `d` **as measured in
the source tableau**.  The negative-distance member is the "first" of the pair and its
column carries `1 + a(d)·a(-d)`; the other carries the plain `1`.

The asymmetry is not a choice of presentation: `seminormalBlock` is the square-root-free
form, which is not symmetric under exchanging the pair, and mixing the two orientations
breaks the braid relation (recorded in `Orbit6Braid`). -/
noncomputable def offDiag (d : ℤ) : ℝ :=
  if d < 0 then 1 + seminormalParam q d * seminormalParam q (-d) else 1

/-- **The matrix of `σ_k` on all of `SYT μ`.**  Rows and columns are indexed by standard
tableaux directly, so no basis correspondence is needed.

The diagonal is `a(axialDist T k)` for *every* `T`, which is exactly why the trichotomy is a
case split on block size and not on the parameter: at distance `+1` this is `q` and at `-1`
it is `-q⁻¹` (`seminormalParam_one` / `_neg_one`), the two size-`1` orbit scalars, while at
`|d| ≥ 2` it is the diagonal of a `seminormalBlock`. -/
noncomputable def genMat (k : ℕ) (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card) :
    Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ := by
  classical
  exact Matrix.of fun T' T =>
    if T' = T then seminormalParam q (axialDist T k)
    else if h : SwapAdmissible T k then
      (if T' = swapTableau T k hk hkn h then offDiag q (axialDist T k) else 0)
    else 0

/-- The diagonal entry is the seminormal parameter at the tableau's own axial distance. -/
@[simp] theorem genMat_diag (k : ℕ) (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card)
    (T : StandardYoungTableau μ) :
    genMat q k hk hkn T T = seminormalParam q (axialDist T k) := by
  classical
  simp [genMat]

/-- Off the diagonal, an inadmissible generator contributes nothing — the size-`1` orbits
are exactly the scalar rows. -/
theorem genMat_of_not_admissible (k : ℕ) (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card)
    {T' T : StandardYoungTableau μ} (hne : T' ≠ T) (h : ¬ SwapAdmissible T k) :
    genMat q k hk hkn T' T = 0 := by
  classical
  simp [genMat, hne, h]

/-- Off the diagonal and away from the swap partner, the entry is `0`: each column has at
most two nonzero entries. -/
theorem genMat_apply_of_ne (k : ℕ) (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card)
    {T' T : StandardYoungTableau μ} (hne : T' ≠ T) (h : SwapAdmissible T k)
    (hswap : T' ≠ swapTableau T k hk hkn h) :
    genMat q k hk hkn T' T = 0 := by
  classical
  simp [genMat, hne, h, hswap]

/-- The swap-partner entry, when the swap is admissible. -/
theorem genMat_swap (k : ℕ) (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card)
    {T : StandardYoungTableau μ} (h : SwapAdmissible T k)
    (hne : swapTableau T k hk hkn h ≠ T) :
    genMat q k hk hkn (swapTableau T k hk hkn h) T = offDiag q (axialDist T k) := by
  classical
  simp [genMat, hne, h]

/-! ## The Hecke quadratic relation, globally

The first relation provable on all of `SYT μ` at once.  `genMat` has no block structure to
induct over — the block decomposition is a *consequence* of the entry rules, not an input —
so the proof reads each column's support directly: `{T}` when `σ_k` fixes `T`, `{T, s_k·T}`
when it does not.
-/

section Quadratic

open scoped Classical

noncomputable local instance : Fintype (StandardYoungTableau μ) := Fintype.ofFinite _

/-- **The two off-diagonal entries of a size-`2` pair multiply to `1 + a(d)·a(-d)`.**  One
of them is the plain `1` and the other carries the whole factor — which one depends on the
orientation, and the product does not.  This is the determinant condition in disguise: the
block has trace `a(d) + a(-d) = q - q⁻¹` and determinant
`a(d)a(-d) - (1 + a(d)a(-d)) = -1`. -/
theorem offDiag_mul_neg {d : ℤ} (hd : d ≠ 0) :
    offDiag q d * offDiag q (-d) = 1 + seminormalParam q d * seminormalParam q (-d) := by
  unfold offDiag
  rcases lt_or_gt_of_ne hd with h | h
  · rw [if_pos h, if_neg (by omega : ¬((-d : ℤ) < 0)), mul_one]
  · rw [if_neg (by omega : ¬((d : ℤ) < 0)), if_pos (by omega : (-d : ℤ) < 0), one_mul,
      neg_neg]
    ring

/-- **A real `q > 0`, `q ≠ 1` is not a root of unity**, so `q ^ (-2d) ≠ 1` for every nonzero
axial distance `d`.  This is what puts `seminormalParam` off its pole at every generator —
the archimedean side of `axialDist_ne_zero`. -/
theorem zpow_ne_one {q : ℝ} (hq : 0 < q) (hq1 : q ≠ 1) {m : ℤ} (hm : m ≠ 0) :
    q ^ m ≠ 1 := by
  intro h
  have hlog : (m : ℝ) * Real.log q = 0 := by
    rw [← Real.log_zpow, h, Real.log_one]
  have hlq : Real.log q ≠ 0 := Real.log_ne_zero_of_pos_of_ne_one hq hq1
  rcases mul_eq_zero.mp hlog with h1 | h2
  · exact hm (by exact_mod_cast h1)
  · exact hlq h2

/-- **The swap moves every tableau it is defined on.**  `s_k·T` differs from `T` already at
the cell holding `k`, which carries `k+1` afterwards. -/
theorem swapTableau_ne (T : StandardYoungTableau μ) {k : ℕ} (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hadm : SwapAdmissible T k) :
    swapTableau T k hk hkn hadm ≠ T := by
  intro h
  have hkI : k ∈ Set.Icc 1 μ.cells.card := ⟨hk, by omega⟩
  have he : T.entry (cellOf T k).1 (cellOf T k).2 = k := entry_cellOf T hkI
  have hs : (swapTableau T k hk hkn hadm).entry (cellOf T k).1 (cellOf T k).2
      = swapVal k (T.entry (cellOf T k).1 (cellOf T k).2) := swapTableau_entry T hk hkn hadm _ _
  rw [h, he] at hs
  unfold swapVal at hs
  rw [if_pos rfl] at hs
  omega

/-- **The column support of `genMat`.**  Column `T` has its nonzero entries at `T` itself
and — when `σ_k` moves `T` — at `s_k·T`; nowhere else.  Summing any weight against that
column therefore collapses to two terms. -/
theorem sum_mul_genMat_column (k : ℕ) (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card)
    {T : StandardYoungTableau μ} (hadm : SwapAdmissible T k)
    (f : StandardYoungTableau μ → ℝ) :
    ∑ S, f S * genMat q k hk hkn S T
      = f T * seminormalParam q (axialDist T k)
        + f (swapTableau T k hk hkn hadm) * offDiag q (axialDist T k) := by
  classical
  set S₀ := swapTableau T k hk hkn hadm with hS₀
  have hne : S₀ ≠ T := swapTableau_ne T hk hkn hadm
  rw [← Finset.sum_subset (Finset.subset_univ ({T, S₀} : Finset (StandardYoungTableau μ)))
      (by
        intro x _ hx
        have hxT : x ≠ T := by intro h; exact hx (by simp [h])
        have hxS : x ≠ S₀ := by intro h; exact hx (by simp [h])
        rw [genMat_apply_of_ne q k hk hkn hxT hadm hxS, mul_zero])]
  rw [Finset.sum_pair (Ne.symm hne), genMat_diag, genMat_swap q k hk hkn hadm hne]

/-- **The Hecke quadratic relation, on all of `SYT μ` at once.**

`ρ(σ_k)² = (q - q⁻¹)·ρ(σ_k) + 1` — the relation `Hecke.σ_quadratic` imposes, in the
normalisation `σ² = (q - q⁻¹)σ + (q·q⁻¹)·1`.

The proof is a two-case split on `SwapAdmissible`, which is the trichotomy of
`TableauCells`:

* **`σ_k` fixes `T`** (axial distance `±1`).  The column is the single entry `a(±1)`, which
  `seminormalParam_one` / `_neg_one` evaluate to `q` resp. `-q⁻¹` — the two roots of
  `X² - (q - q⁻¹)X - 1`.
* **`σ_k` moves `T`.**  The column is `{T, s_k·T}`, and the `2 × 2` block it spans has
  trace `a(d) + a(-d) = q - q⁻¹` (`seminormalParam_add_neg`, using
  `axialDist_swapTableau`) and determinant `-1` (`offDiag_mul_neg`).  Cayley–Hamilton
  does the rest.

No block-diagonal decomposition is constructed or needed: the block structure is read off
the entry rules column by column. -/
theorem genMat_quadratic (hq : 0 < q) (hq1 : q ≠ 1) (k : ℕ) (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) :
    genMat q k hk hkn * genMat q k hk hkn
      = (q - q⁻¹) • genMat q k hk hkn
        + (1 : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ) := by
  classical
  have hq0 : q ≠ 0 := ne_of_gt hq
  ext T' T
  have hkI : k ∈ Set.Icc 1 μ.cells.card := ⟨hk, by omega⟩
  have hkI' : k + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hkn⟩
  have hd0 : axialDist T k ≠ 0 := axialDist_ne_zero T hkI hkI'
  have hpow : q ^ (-2 * axialDist T k) ≠ 1 := zpow_ne_one hq hq1 (by omega)
  have hsum : seminormalParam q (axialDist T k) + seminormalParam q (-axialDist T k)
      = q - q⁻¹ := seminormalParam_add_neg q _ hq0 hpow
  rw [Matrix.mul_apply, Matrix.add_apply, Matrix.smul_apply, smul_eq_mul, Matrix.one_apply]
  by_cases hadm : SwapAdmissible T k
  · -- `σ_k` moves `T`: the `2 × 2` block `{T, s_k·T}`
    set S₀ := swapTableau T k hk hkn hadm with hS₀
    have hne : S₀ ≠ T := swapTableau_ne T hk hkn hadm
    have hadmS : SwapAdmissible S₀ k := swapAdmissible_swapTableau T hk hkn hadm
    have hdS : axialDist S₀ k = -axialDist T k := axialDist_swapTableau T hk hkn hadm
    have hback : swapTableau S₀ k hk hkn hadmS = T := swapTableau_involutive T hk hkn hadm
    have hprod : offDiag q (axialDist T k) * offDiag q (-axialDist T k)
        = 1 + seminormalParam q (axialDist T k) * seminormalParam q (-axialDist T k) :=
      offDiag_mul_neg q hd0
    have hTS₀ : genMat q k hk hkn T S₀ = offDiag q (-axialDist T k) := by
      have := genMat_swap q k hk hkn hadmS (by rw [hback]; exact Ne.symm hne)
      rw [hback, hdS] at this
      exact this
    have hS₀T : genMat q k hk hkn S₀ T = offDiag q (axialDist T k) :=
      genMat_swap q k hk hkn hadm hne
    have hS₀S₀ : genMat q k hk hkn S₀ S₀ = seminormalParam q (-axialDist T k) := by
      rw [genMat_diag, hdS]
    rw [sum_mul_genMat_column q k hk hkn hadm (fun S => genMat q k hk hkn T' S)]
    by_cases hT'T : T' = T
    · -- diagonal: `a(d)² + (1 + a(d)a(-d)) = (q - q⁻¹)·a(d) + 1`
      subst hT'T
      rw [genMat_diag, hTS₀, if_pos rfl]
      linear_combination hprod + seminormalParam q (axialDist T' k) * hsum
    · by_cases hT'S : T' = S₀
      · -- the partner row: `off·a(d) + a(-d)·off = (q - q⁻¹)·off`
        subst hT'S
        rw [hS₀T, hS₀S₀, if_neg hT'T]
        linear_combination offDiag q (axialDist T k) * hsum
      · -- every other row is zero on both sides
        have h1 : genMat q k hk hkn T' T = 0 :=
          genMat_apply_of_ne q k hk hkn hT'T hadm hT'S
        have h2 : genMat q k hk hkn T' S₀ = 0 :=
          genMat_apply_of_ne q k hk hkn hT'S hadmS (by rw [hback]; exact hT'T)
        rw [h1, h2, if_neg hT'T]
        ring
  · -- `σ_k` fixes `T`: a scalar column at axial distance `±1`
    have hcol : ∑ S, genMat q k hk hkn T' S * genMat q k hk hkn S T
        = genMat q k hk hkn T' T * seminormalParam q (axialDist T k) := by
      rw [Finset.sum_eq_single T]
      · rw [genMat_diag]
      · intro b _ hb
        rw [genMat_of_not_admissible q k hk hkn hb hadm, mul_zero]
      · intro h; exact absurd (Finset.mem_univ T) h
    rw [hcol]
    have hroot : seminormalParam q (axialDist T k) * seminormalParam q (axialDist T k)
        = (q - q⁻¹) * seminormalParam q (axialDist T k) + 1 := by
      have hq2 : q ^ 2 ≠ 1 := by
        intro h
        have hfac : (q - 1) * (q + 1) = 0 := by nlinarith [h]
        rcases mul_eq_zero.mp hfac with h1 | h2
        · exact hq1 (by linarith)
        · linarith
      rcases axialDist_trichotomy T hkI hkI' with h | h | h
      · rw [h, seminormalParam_one q hq0 hq2]; field_simp; ring
      · rw [h, seminormalParam_neg_one q hq0 hq2]; field_simp; ring
      · exact absurd h hadm
    rcases eq_or_ne T' T with rfl | hT'T
    · rw [genMat_diag, if_pos rfl]; linarith [hroot]
    · rw [genMat_of_not_admissible q k hk hkn hT'T hadm, if_neg hT'T]; ring

end Quadratic

/-! ## Far commutation

`σ_k σ_l = σ_l σ_k` for `|k - l| ≥ 2`, again on all of `SYT μ` at once.  Like the
quadratic and unlike the braid, this relation is **column-local**: a far swap at `l` moves
no cell that `σ_k` looks at (`cellOf_swapTableau_of_ne`), so every input to `σ_k`'s row
rule — the parameter, the admissibility, the partner — survives it untouched
(`axialDist_swapTableau_of_far`, `swapAdmissible_far_iff`).

Note what is *not* needed: no hypothesis on `q` at all.  The quadratic had to know that
`a(d)` and `a(-d)` sum to `q - q⁻¹`; far commutation never combines two parameters, it only
observes that both sides pair the same four entries.
-/

section FarComm

open scoped Classical

noncomputable local instance : Fintype (StandardYoungTableau μ) := Fintype.ofFinite _

/-- The column of a tableau that `σ_k` fixes is the single diagonal entry. -/
theorem sum_mul_genMat_column_of_not_admissible (k : ℕ) (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) {T : StandardYoungTableau μ} (hadm : ¬ SwapAdmissible T k)
    (f : StandardYoungTableau μ → ℝ) :
    ∑ S, f S * genMat q k hk hkn S T = f T * seminormalParam q (axialDist T k) := by
  classical
  rw [Finset.sum_eq_single T]
  · rw [genMat_diag]
  · intro b _ hb
    rw [genMat_of_not_admissible q k hk hkn hb hadm, mul_zero]
  · intro h; exact absurd (Finset.mem_univ T) h

/-- **One factor peeled off a product.**  Multiplying on the right by `genMat q l` replaces
column `T` by the two-term combination its support dictates.  Iterating this is how a
product of generators is evaluated: three applications turn the braid's triple product into
a sum over the `⟨s_k, s_{k+1}⟩`-orbit of `T`. -/
theorem genMat_mul_apply (l : ℕ) (hl : 1 ≤ l) (hln : l + 1 ≤ μ.cells.card)
    (M : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ)
    {T : StandardYoungTableau μ} (hadm : SwapAdmissible T l)
    (T' : StandardYoungTableau μ) :
    (M * genMat q l hl hln) T' T
      = M T' T * seminormalParam q (axialDist T l)
        + M T' (swapTableau T l hl hln hadm) * offDiag q (axialDist T l) := by
  rw [Matrix.mul_apply]
  exact sum_mul_genMat_column q l hl hln hadm (fun S => M T' S)

/-- The scalar-column case of `genMat_mul_apply`. -/
theorem genMat_mul_apply_of_not_admissible (l : ℕ) (hl : 1 ≤ l) (hln : l + 1 ≤ μ.cells.card)
    (M : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ)
    {T : StandardYoungTableau μ} (hadm : ¬ SwapAdmissible T l)
    (T' : StandardYoungTableau μ) :
    (M * genMat q l hl hln) T' T = M T' T * seminormalParam q (axialDist T l) := by
  rw [Matrix.mul_apply]
  exact sum_mul_genMat_column_of_not_admissible q l hl hln hadm (fun S => M T' S)

/-- **Two far swaps of the same tableau land in different places.**  At the cell holding
`k`, `s_k·T` carries `k+1` while `s_l·T` still carries `k`.

This is the distinctness the four-element support `{T, s_k·T, s_l·T, s_k s_l·T}` rests on:
from it, `T ≠ s_k s_l·T` follows by applying `s_k` to both sides. -/
theorem swapTableau_far_ne (T : StandardYoungTableau μ) {k l : ℕ} (hk : 1 ≤ k) (hl : 1 ≤ l)
    (hkn : k + 1 ≤ μ.cells.card) (hln : l + 1 ≤ μ.cells.card)
    (hfar : k + 1 < l ∨ l + 1 < k)
    (hadmk : SwapAdmissible T k) (hadml : SwapAdmissible T l) :
    swapTableau T k hk hkn hadmk ≠ swapTableau T l hl hln hadml := by
  intro h
  have hkI : k ∈ Set.Icc 1 μ.cells.card := ⟨hk, by omega⟩
  have he : T.entry (cellOf T k).1 (cellOf T k).2 = k := entry_cellOf T hkI
  have h1 : (swapTableau T k hk hkn hadmk).entry (cellOf T k).1 (cellOf T k).2
      = swapVal k (T.entry (cellOf T k).1 (cellOf T k).2) :=
    swapTableau_entry T hk hkn hadmk _ _
  have h2 : (swapTableau T l hl hln hadml).entry (cellOf T k).1 (cellOf T k).2
      = swapVal l (T.entry (cellOf T k).1 (cellOf T k).2) :=
    swapTableau_entry T hl hln hadml _ _
  rw [h, h2, he] at h1
  unfold swapVal at h1
  rw [if_neg (by omega : ¬(k = l)), if_neg (by omega : ¬(k = l + 1)), if_pos rfl] at h1
  omega

/-- **Far commutation, on all of `SYT μ` at once.**

`ρ(σ_k) ρ(σ_l) = ρ(σ_l) ρ(σ_k)` for `|k - l| ≥ 2`, arbitrary shape `μ`.

Both products are supported on the same four tableaux `{T, s_k·T, s_l·T, s_k s_l·T}`, and
each pairs them the same way — because a far swap at `l` changes nothing `σ_k` reads
(`axialDist_swapTableau_of_far`, `swapAdmissible_far_iff`) and the two actions commute
(`swapTableau_comm`).  The four rows then match term by term, with the factors merely
transposed.

**No hypothesis on `q`.**  The quadratic needed `a(d) + a(-d) = q - q⁻¹` and hence
`q > 0`, `q ≠ 1`; far commutation never combines two parameters, so it holds for every
real `q`. -/
theorem genMat_far_comm {k l : ℕ} (hk : 1 ≤ k) (hl : 1 ≤ l)
    (hkn : k + 1 ≤ μ.cells.card) (hln : l + 1 ≤ μ.cells.card)
    (hfar : k + 1 < l ∨ l + 1 < k) :
    genMat q k hk hkn * genMat q l hl hln = genMat q l hl hln * genMat q k hk hkn := by
  classical
  have hkI : k ∈ Set.Icc 1 μ.cells.card := ⟨hk, by omega⟩
  have hkI' : k + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hkn⟩
  have hlI : l ∈ Set.Icc 1 μ.cells.card := ⟨hl, by omega⟩
  have hlI' : l + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hln⟩
  have hfar' : l + 1 < k ∨ k + 1 < l := by omega
  ext T' T
  rw [Matrix.mul_apply, Matrix.mul_apply]
  by_cases hka : SwapAdmissible T k
  · by_cases hla : SwapAdmissible T l
    · -- both generators move `T`: the full four-element support
      set A := swapTableau T k hk hkn hka with hA
      set B := swapTableau T l hl hln hla with hB
      have hBk : SwapAdmissible B k :=
        (swapAdmissible_far_iff T hl hln hla hkI hkI' hfar).mpr hka
      have hAl : SwapAdmissible A l :=
        (swapAdmissible_far_iff T hk hkn hka hlI hlI' hfar').mpr hla
      set C := swapTableau B k hk hkn hBk with hC
      have hCA : C = swapTableau A l hl hln hAl :=
        swapTableau_comm T hk hl hkn hln hfar hka hla
      have hdBk : axialDist B k = axialDist T k :=
        axialDist_swapTableau_of_far T hl hln hla hkI hkI' hfar
      have hdAl : axialDist A l = axialDist T l :=
        axialDist_swapTableau_of_far T hk hkn hka hlI hlI' hfar'
      have hAT : A ≠ T := swapTableau_ne T hk hkn hka
      have hBT : B ≠ T := swapTableau_ne T hl hln hla
      have hAB : A ≠ B := swapTableau_far_ne T hk hl hkn hln hfar hka hla
      have hCB : C ≠ B := swapTableau_ne B hk hkn hBk
      have hCA' : C ≠ A := by rw [hCA]; exact swapTableau_ne A hl hln hAl
      have hCT : C ≠ T := by
        -- read both off at the cell holding `k`: `C` carries `k+1` there, `T` carries `k`
        intro h
        have hBc : cellOf B k = cellOf T k :=
          cellOf_swapTableau_of_ne T hl hln hla hkI (by omega) (by omega)
        have heB : B.entry (cellOf T k).1 (cellOf T k).2 = k := by
          rw [← hBc]; exact entry_cellOf B hkI
        have hCe : C.entry (cellOf T k).1 (cellOf T k).2
            = swapVal k (B.entry (cellOf T k).1 (cellOf T k).2) :=
          swapTableau_entry B hk hkn hBk _ _
        rw [heB] at hCe
        unfold swapVal at hCe
        rw [if_pos rfl] at hCe
        have heT : T.entry (cellOf T k).1 (cellOf T k).2 = k := entry_cellOf T hkI
        rw [h] at hCe
        omega
      rw [sum_mul_genMat_column q l hl hln hla (fun S => genMat q k hk hkn T' S),
        sum_mul_genMat_column q k hk hkn hka (fun S => genMat q l hl hln T' S)]
      by_cases h1 : T' = T
      · subst h1
        rw [genMat_diag, genMat_diag,
          genMat_apply_of_ne q k hk hkn (Ne.symm hBT) hBk (Ne.symm hCT),
          genMat_apply_of_ne q l hl hln (Ne.symm hAT) hAl (by rw [← hCA]; exact Ne.symm hCT)]
        ring
      · by_cases h2 : T' = A
        · subst h2
          rw [genMat_swap q k hk hkn hka hAT, genMat_diag,
            genMat_apply_of_ne q k hk hkn hAB hBk (Ne.symm hCA'),
            genMat_apply_of_ne q l hl hln h1 hla hAB, hdAl]
          ring
        · by_cases h3 : T' = B
          · subst h3
            rw [genMat_swap q l hl hln hla hBT, genMat_diag,
              genMat_apply_of_ne q k hk hkn h1 hka (by exact h2),
              genMat_apply_of_ne q l hl hln (by exact h2) hAl
                (by rw [← hCA]; exact Ne.symm hCB), hdBk]
            ring
          · by_cases h4 : T' = C
            · subst h4
              rw [genMat_apply_of_ne q k hk hkn hCT hka hCA',
                genMat_apply_of_ne q l hl hln hCT hla hCB,
                genMat_swap q k hk hkn hBk hCB,
                (by rw [hCA] : genMat q l hl hln C A
                  = genMat q l hl hln (swapTableau A l hl hln hAl) A),
                genMat_swap q l hl hln hAl (by rw [← hCA]; exact hCA'), hdBk, hdAl]
              ring
            · rw [genMat_apply_of_ne q k hk hkn h1 hka h2,
                genMat_apply_of_ne q k hk hkn h3 hBk h4,
                genMat_apply_of_ne q l hl hln h1 hla h3,
                genMat_apply_of_ne q l hl hln h2 hAl (by rw [← hCA]; exact h4)]
              ring
    · -- `σ_k` moves `T`, `σ_l` fixes it
      set A := swapTableau T k hk hkn hka with hA
      have hAl : ¬ SwapAdmissible A l := fun h =>
        hla ((swapAdmissible_far_iff T hk hkn hka hlI hlI' hfar').mp h)
      have hdAl : axialDist A l = axialDist T l :=
        axialDist_swapTableau_of_far T hk hkn hka hlI hlI' hfar'
      have hAT : A ≠ T := swapTableau_ne T hk hkn hka
      rw [sum_mul_genMat_column_of_not_admissible q l hl hln hla
          (fun S => genMat q k hk hkn T' S),
        sum_mul_genMat_column q k hk hkn hka (fun S => genMat q l hl hln T' S)]
      by_cases h1 : T' = T
      · subst h1
        rw [genMat_diag, genMat_diag,
          genMat_of_not_admissible q l hl hln (Ne.symm hAT) hAl]
        ring
      · by_cases h2 : T' = A
        · subst h2
          rw [genMat_swap q k hk hkn hka hAT, genMat_diag,
            genMat_of_not_admissible q l hl hln h1 hla, hdAl]
          ring
        · rw [genMat_apply_of_ne q k hk hkn h1 hka h2,
            genMat_of_not_admissible q l hl hln h1 hla,
            genMat_of_not_admissible q l hl hln h2 hAl]
          ring
  · by_cases hla : SwapAdmissible T l
    · -- the mirror: `σ_l` moves `T`, `σ_k` fixes it
      set B := swapTableau T l hl hln hla with hB
      have hBk : ¬ SwapAdmissible B k := fun h =>
        hka ((swapAdmissible_far_iff T hl hln hla hkI hkI' hfar).mp h)
      have hdBk : axialDist B k = axialDist T k :=
        axialDist_swapTableau_of_far T hl hln hla hkI hkI' hfar
      have hBT : B ≠ T := swapTableau_ne T hl hln hla
      rw [sum_mul_genMat_column q l hl hln hla (fun S => genMat q k hk hkn T' S),
        sum_mul_genMat_column_of_not_admissible q k hk hkn hka
          (fun S => genMat q l hl hln T' S)]
      by_cases h1 : T' = T
      · subst h1
        rw [genMat_diag, genMat_diag,
          genMat_of_not_admissible q k hk hkn (Ne.symm hBT) hBk]
        ring
      · by_cases h2 : T' = B
        · subst h2
          rw [genMat_swap q l hl hln hla hBT, genMat_diag,
            genMat_of_not_admissible q k hk hkn h1 hka, hdBk]
          ring
        · rw [genMat_of_not_admissible q k hk hkn h1 hka,
            genMat_of_not_admissible q k hk hkn h2 hBk,
            genMat_apply_of_ne q l hl hln h1 hla h2]
          ring
    · -- both fix `T`: two scalar columns
      rw [sum_mul_genMat_column_of_not_admissible q l hl hln hla
          (fun S => genMat q k hk hkn T' S),
        sum_mul_genMat_column_of_not_admissible q k hk hkn hka
          (fun S => genMat q l hl hln T' S)]
      by_cases h1 : T' = T
      · subst h1
        rw [genMat_diag, genMat_diag]
        ring
      · rw [genMat_of_not_admissible q k hk hkn h1 hka,
          genMat_of_not_admissible q l hl hln h1 hla]
        ring

end FarComm

/-! ## Towards the braid

The braid is the one relation that is **not** column-local: `σ_k` and `σ_{k+1}` have
different supports, so no single-column argument reaches it.  What replaces the column is
the `⟨s_k, s_{k+1}⟩`-orbit, and the two lemmas below carry the triple product down to
entries at *named* tableaux of that orbit, with every coefficient already identified.

Writing `p = axialDist T k` and `r = axialDist T (k+1)`, the third parameter that appears
is `a(p + r)` — not a new unknown, by `axialDist_succ_swapTableau` /
`axialDist_swapTableau_succ`.  That is exactly the `a₃` of `Orbit6Braid`, whose one
relation `a₃(a₁ + a₂ - c) = a₁a₂` (`seminormalParam_mul_rel`) is what the braid needs.

After both expansions the identity to prove is, for every row `T'`,

```
  ρ_k[T',T]·a(r)·a(p) + ρ_k[T',s_{k+1}T]·off(r)·a(p)
    + ρ_k[T',s_kT]·a(p+r)·off(p) + ρ_k[T',s_{k+1}s_kT]·off(p+r)·off(p)
=
  ρ_{k+1}[T',T]·a(p)·a(r) + ρ_{k+1}[T',s_kT]·off(p)·a(r)
    + ρ_{k+1}[T',s_{k+1}T]·a(p+r)·off(r) + ρ_{k+1}[T',s_ks_{k+1}T]·off(p+r)·off(r)
```

which is pure algebra in the orbit once each `ρ` entry is resolved.  **What is still
missing is the orbit-size classification** (bean `qou-7xt3`): the row cases depend on which
of `s_kT`, `s_{k+1}T`, `s_{k+1}s_kT`, `s_ks_{k+1}T` exist and which coincide, and
`s_{k+1}s_kT ≠ s_ks_{k+1}T` is precisely what distinguishes the size-6 orbit from the
smaller ones.
-/

section Braid

open scoped Classical

noncomputable local instance : Fintype (StandardYoungTableau μ) := Fintype.ofFinite _

/-- **The braid's left-hand side, expanded onto the orbit.**  Two applications of
`genMat_mul_apply` reduce `ρ(σ_k)ρ(σ_{k+1})ρ(σ_k)` at column `T` to four entries of
`ρ(σ_k)` — at `T`, at `s_{k+1}T`, at `s_kT`, and at `s_{k+1}s_kT` — with coefficients built
from `a(p)`, `a(r)`, `a(p+r)` and the matching `offDiag`s.

The `a(p + r)` is where the third parameter enters, supplied by
`axialDist_succ_swapTableau`: `σ_{k+1}` acting on `s_kT` reads the *sum* of the two
distances, not a new quantity. -/
theorem genMat_braid_lhs_expand (k : ℕ) (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card)
    (hl : 1 ≤ k + 1) (hln : k + 1 + 1 ≤ μ.cells.card)
    {T : StandardYoungTableau μ} (hka : SwapAdmissible T k)
    (hla : SwapAdmissible T (k + 1))
    (hAl : SwapAdmissible (swapTableau T k hk hkn hka) (k + 1))
    (T' : StandardYoungTableau μ) :
    (genMat q k hk hkn * genMat q (k + 1) hl hln * genMat q k hk hkn) T' T
      = (genMat q k hk hkn T' T * seminormalParam q (axialDist T (k + 1))
          + genMat q k hk hkn T' (swapTableau T (k + 1) hl hln hla)
            * offDiag q (axialDist T (k + 1)))
          * seminormalParam q (axialDist T k)
        + (genMat q k hk hkn T' (swapTableau T k hk hkn hka)
            * seminormalParam q (axialDist T k + axialDist T (k + 1))
          + genMat q k hk hkn T'
              (swapTableau (swapTableau T k hk hkn hka) (k + 1) hl hln hAl)
            * offDiag q (axialDist T k + axialDist T (k + 1)))
          * offDiag q (axialDist T k) := by
  classical
  have hshift : axialDist (swapTableau T k hk hkn hka) (k + 1)
      = axialDist T k + axialDist T (k + 1) :=
    axialDist_succ_swapTableau T hk hkn (by omega) hka
  rw [genMat_mul_apply q k hk hkn _ hka T',
    genMat_mul_apply q (k + 1) hl hln _ hla T',
    genMat_mul_apply q (k + 1) hl hln _ hAl T', hshift]

/-- **The braid's right-hand side, expanded onto the same orbit.**  The mirror of
`genMat_braid_lhs_expand`, with `k` and `k+1` exchanged; the third parameter is again
`a(p + r)`, now by `axialDist_swapTableau_succ`.

Comparing the two expansions is what the braid reduces to — and comparing them needs the
orbit-size classification, because the row cases turn on which of the four named tableaux
coincide. -/
theorem genMat_braid_rhs_expand (k : ℕ) (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card)
    (hl : 1 ≤ k + 1) (hln : k + 1 + 1 ≤ μ.cells.card)
    {T : StandardYoungTableau μ} (hka : SwapAdmissible T k)
    (hla : SwapAdmissible T (k + 1))
    (hBk : SwapAdmissible (swapTableau T (k + 1) hl hln hla) k)
    (T' : StandardYoungTableau μ) :
    (genMat q (k + 1) hl hln * genMat q k hk hkn * genMat q (k + 1) hl hln) T' T
      = (genMat q (k + 1) hl hln T' T * seminormalParam q (axialDist T k)
          + genMat q (k + 1) hl hln T' (swapTableau T k hk hkn hka)
            * offDiag q (axialDist T k))
          * seminormalParam q (axialDist T (k + 1))
        + (genMat q (k + 1) hl hln T' (swapTableau T (k + 1) hl hln hla)
            * seminormalParam q (axialDist T k + axialDist T (k + 1))
          + genMat q (k + 1) hl hln T'
              (swapTableau (swapTableau T (k + 1) hl hln hla) k hk hkn hBk)
            * offDiag q (axialDist T k + axialDist T (k + 1)))
          * offDiag q (axialDist T (k + 1)) := by
  classical
  have hshift : axialDist (swapTableau T (k + 1) hl hln hla) k
      = axialDist T k + axialDist T (k + 1) :=
    axialDist_swapTableau_succ T hk (by omega) hla
  rw [genMat_mul_apply q (k + 1) hl hln _ hla T',
    genMat_mul_apply q k hk hkn _ hka T',
    genMat_mul_apply q k hk hkn _ hBk T', hshift]

end Braid

end SeminormalRep

end QOU.SchurWeyl
