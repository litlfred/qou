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

end SeminormalRep

end QOU.SchurWeyl
