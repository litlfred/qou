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

**All three Hecke relations are proved on all of `SYT μ`, unconditionally** —
`genMat_quadratic`, `genMat_far_comm`, and `genMat_braid`.  No hypothesis on the orbit: the
braid dispatches on three admissibility flags to seven shape theorems (sizes `1`, `2` in two
orientations, `3` in three positions, and the generic `6`), with every further hypothesis
those need *derived* through the classification iffs in `TableauCells`.

What remains for `hoefsmit_seminormal_rep` is **packaging only** — feeding the three
relations to `Hecke.lift`, which is an index translation between `k : ℕ` here and
`Fin n` there.  The `-- Ref:`-cited `sorry` stands until that lands.

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

/-- `SYT μ` is finite (`QOU.Mathlib.StandardYoungTableau.instFinite`); this is the
`Fintype` that makes `Matrix (SYT μ) (SYT μ) ℝ` a ring, so that the generator matrices can
be multiplied at all.  Noncomputable — it goes through `Fintype.ofFinite`, which is fine
here because nothing in this file is meant to evaluate. -/
noncomputable instance instFintypeSYT : Fintype (StandardYoungTableau μ) := Fintype.ofFinite _

/-- Companion to `instFintypeSYT`: `Matrix`'s ring structure needs decidable equality on the
index type as well as finiteness (it is what makes the identity matrix definable). -/
noncomputable instance instDecEqSYT : DecidableEq (StandardYoungTableau μ) :=
  Classical.decEq _

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

/-- **The off-diagonal entry vanishes at the scalar distances.**  `offDiag q (-1) = 0` and
`offDiag q 1 = 1`, so a generator that *fixes* a tableau contributes a genuinely diagonal
row — even though the entry rule offers it an off-diagonal slot.

This is the coherence condition for the smaller orbits: the uniform rule in `genMat` would
give a size-`1` orbit an off-diagonal partner entry, and the construction only works because
`seminormalParam_mul_neg_one` forces that entry to `0`. -/
@[simp] theorem offDiag_neg_one (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) : offDiag q (-1) = 0 := by
  unfold offDiag
  rw [if_pos (by omega : (-1 : ℤ) < 0), neg_neg, mul_comm,
    seminormalParam_mul_neg_one q hq0 hq2]
  ring

/-- Off the negative branch, `offDiag` is the plain `1`. -/
theorem offDiag_of_not_neg {d : ℤ} (h : ¬ d < 0) : offDiag q d = 1 := by
  unfold offDiag
  rw [if_neg h]

/-- The positive scalar distance takes the plain branch. -/
@[simp] theorem offDiag_one : offDiag q 1 = 1 := by
  unfold offDiag
  rw [if_neg (by omega : ¬((1 : ℤ) < 0))]

/-- **The determinant factor vanishes at either scalar distance.**  The form the smaller
orbits consume: whenever a generator fixes a tableau, `1 + a(d)a(-d) = 0`. -/
theorem one_add_seminormalParam_mul_neg_of_scalar (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) {d : ℤ}
    (hd : d = 1 ∨ d = -1) :
    1 + seminormalParam q d * seminormalParam q (-d) = 0 := by
  rcases hd with rfl | rfl
  · rw [seminormalParam_mul_neg_one q hq0 hq2]; ring
  · rw [show -(-1 : ℤ) = 1 from rfl, mul_comm, seminormalParam_mul_neg_one q hq0 hq2]; ring

/-- **`q ≠ 0` and `q² ≠ 1` is exactly the condition for a real `q` not to be a root of
unity**, hence for `q ^ (-2d) ≠ 1` at every nonzero axial distance — which is what keeps
`seminormalParam` off its pole.

This is *sharp over `ℝ`*, and that matters for the hypotheses of the whole file.  `q^m = 1`
with `m ≠ 0` forces `|q| = 1`, hence `q = ±1`, hence `q² = 1`; so no further condition is
available to assume and none is needed.  In particular the natural-looking `0 < q ∧ q ≠ 1`
is **stronger than required** — negative `q` is fine as long as `q ≠ -1` — while a bare
`q ≠ 0` is **too weak**, since `q = -1` genuinely degenerates the seminormal form (see the
`S1` discussion in `SeminormalParam.lean`). -/
theorem zpow_ne_one {q : ℝ} (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) {m : ℤ} (hm : m ≠ 0) :
    q ^ m ≠ 1 := by
  intro h
  -- pass to `q²`, which is positive outright and is exactly what the hypothesis bounds
  have hsq : (q ^ 2 : ℝ) ^ m = 1 := by
    rw [show (q ^ 2 : ℝ) = q * q by ring, mul_zpow, h, one_mul]
  have hpos : (0 : ℝ) < q ^ 2 :=
    lt_of_le_of_ne (sq_nonneg q) (Ne.symm (pow_ne_zero 2 hq0))
  have hlog : (m : ℝ) * Real.log (q ^ 2) = 0 := by
    rw [← Real.log_zpow, hsq, Real.log_one]
  have hlq : Real.log (q ^ 2) ≠ 0 := Real.log_ne_zero_of_pos_of_ne_one hpos hq2
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
theorem genMat_quadratic (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (k : ℕ) (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) :
    genMat q k hk hkn * genMat q k hk hkn
      = (q - q⁻¹) • genMat q k hk hkn
        + (1 : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ) := by
  classical
  ext T' T
  have hkI : k ∈ Set.Icc 1 μ.cells.card := ⟨hk, by omega⟩
  have hkI' : k + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hkn⟩
  have hd0 : axialDist T k ≠ 0 := axialDist_ne_zero T hkI hkI'
  have hpow : q ^ (-2 * axialDist T k) ≠ 1 := zpow_ne_one hq0 hq2 (by omega)
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

/-- **The braid's diagonal row, as pure algebra — and the relation is exactly what closes
it.**

Resolving the two expansions above at row `T'  = T` leaves, with `a₁ = a(p)`, `a₂ = a(r)`,
`a₃ = a(p+r)` and `c = q - q⁻¹`:

* from the left, `a₁²a₂ + a₃·off(-p)·off(p)`;
* from the right, `a₁a₂² + a₃·off(-r)·off(r)`;

and `offDiag_mul_neg` turns each `off·off` into `1 + a(d)·a(-d) = 1 + a(d)(c - a(d))`
(`seminormalParam_add_neg`).  The difference of the two sides factors as

  `(a₁ - a₂)·[a₁a₂ - a₃(a₁ + a₂ - c)]`

whose second factor is `seminormalParam_rel` — vanishing identically.  Note the first factor
is *not* needed: the identity holds whether or not `a₁ = a₂`, so no genericity assumption
about the orbit enters here. -/
theorem braid_diag_identity (c a₁ a₂ a₃ : ℝ) (hrel : a₃ * (a₁ + a₂ - c) = a₁ * a₂) :
    a₁ * a₁ * a₂ + a₃ * (1 + a₁ * (c - a₁))
      = a₁ * a₂ * a₂ + a₃ * (1 + a₂ * (c - a₂)) := by
  linear_combination (a₂ - a₁) * hrel

/-- **The `s_k·T` row.**  Left gives `off(p)·(a₁a₂ + a₃·a(-p))`, right gives `off(p)·a₃a₂`;
the difference is `off(p)` times the relation. -/
theorem braid_rowA_identity (c a₁ a₂ a₃ o₁ : ℝ) (hrel : a₃ * (a₁ + a₂ - c) = a₁ * a₂) :
    o₁ * a₂ * a₁ + a₃ * (c - a₁) * o₁ = a₃ * o₁ * a₂ := by
  linear_combination (-o₁) * hrel

/-- **The `s_{k+1}·T` row** — the mirror of `braid_rowA_identity`, differing only in the
sign of the multiple of the relation. -/
theorem braid_rowB_identity (c a₁ a₂ a₃ o₂ : ℝ) (hrel : a₃ * (a₁ + a₂ - c) = a₁ * a₂) :
    a₃ * o₂ * a₁ = o₂ * a₁ * a₂ + a₃ * (c - a₂) * o₂ := by
  linear_combination o₂ * hrel

/-! ### Only three of the six rows carry content

Resolving both expansions against the entry rules at every row of a generic (size-`6`)
orbit — writing `A = s_k·T`, `B = s_{k+1}·T`, `D = s_{k+1}A`, `E = s_kB`,
`F = s_kD = s_{k+1}E` — gives:

| row | left | right | closes by |
|---|---|---|---|
| `T` | `a₁²a₂ + a₃·off(-p)off(p)` | `a₁a₂² + a₃·off(-r)off(r)` | `braid_diag_identity` |
| `A` | `off(p)(a₁a₂ + a₃a(-p))` | `off(p)·a₃a₂` | `braid_rowA_identity` |
| `B` | `a₃·off(r)a₁` | `off(r)(a₁a₂ + a₃a(-r))` | `braid_rowB_identity` |
| `D` | `a₂·off(p+r)off(p)` | `off(p+r)off(p)·a₂` | `ring` |
| `E` | `off(p+r)off(r)a₁` | `a₁·off(p+r)off(r)` | `ring` |
| `F` | `off(r)off(p+r)off(p)` | `off(p)off(p+r)off(r)` | `ring` |

**The last three rows are identities of the ambient ring** — the two sides are literally the
same product in a different order, with no parameter relation involved.  And the three that
do carry content all reduce to the *same* single relation
`a₃(a₁ + a₂ - c) = a₁a₂` (`seminormalParam_rel`), differing only in the multiple of it
required: `(a₂ - a₁)`, `-off(p)`, `+off(r)`.

This is the concrete payoff of indexing by `SYT μ` rather than by `Fin 6`.  `Orbit6Braid`
proves the same mathematics as an explicit `6 × 6` matrix identity whose triple product has
1296 scalar terms and needs `maxHeartbeats 1600000`; here the zero pattern is *given* by the
entry rules rather than discovered by `simp`, so half the rows collapse to `ring` and the
rest are one `linear_combination` each.
-/

/-- **The braid's diagonal entry, at the tableau level.**

The first row of the braid instantiated against the two expansions — `braid_diag_identity`
wired to actual `genMat` entries rather than to abstract parameters.

The hypotheses are the six admissibilities of a generic orbit.  They are *not* redundant
even for this single row: the `(T, D)` and `(T, E)` entries are only known to vanish once
`D` and `E` exist as tableaux, which is what `hDk` and `hEl` provide. -/
theorem genMat_braid_apply_diag (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (k : ℕ) (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hl : 1 ≤ k + 1) (hln : k + 1 + 1 ≤ μ.cells.card)
    {T : StandardYoungTableau μ}
    (hka : SwapAdmissible T k) (hla : SwapAdmissible T (k + 1))
    (hAl : SwapAdmissible (swapTableau T k hk hkn hka) (k + 1))
    (hBk : SwapAdmissible (swapTableau T (k + 1) hl hln hla) k)
    (hDk : SwapAdmissible
      (swapTableau (swapTableau T k hk hkn hka) (k + 1) hl hln hAl) k)
    (hEl : SwapAdmissible
      (swapTableau (swapTableau T (k + 1) hl hln hla) k hk hkn hBk) (k + 1)) :
    (genMat q k hk hkn * genMat q (k + 1) hl hln * genMat q k hk hkn) T T
      = (genMat q (k + 1) hl hln * genMat q k hk hkn * genMat q (k + 1) hl hln) T T := by
  classical
  have hkI : k ∈ Set.Icc 1 μ.cells.card := ⟨hk, by omega⟩
  have hkI' : k + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hkn⟩
  have hkI'' : k + 1 + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hln⟩
  -- the four non-`T` orbit elements that this row touches
  set A := swapTableau T k hk hkn hka with hA
  set B := swapTableau T (k + 1) hl hln hla with hB
  set D := swapTableau A (k + 1) hl hln hAl with hD
  set E := swapTableau B k hk hkn hBk with hE
  -- distinctness, all off the orbit entry table
  have hTA : T ≠ A := (swapTableau_ne T hk hkn hka).symm
  have hTB : T ≠ B := (swapTableau_ne T hl hln hla).symm
  have hTD : T ≠ D := by
    refine (ne_of_entry_ne (i := (cellOf T k).1) (j := (cellOf T k).2) ?_).symm
    rw [(orbitEntries_sl_sk T hk hkn hln hka hAl).1, entry_cellOf T hkI]
    omega
  have hTE : T ≠ E := by
    refine (ne_of_entry_ne (i := (cellOf T k).1) (j := (cellOf T k).2) ?_).symm
    rw [(orbitEntries_sk_sl T hk hkn hln hla hBk).1, entry_cellOf T hkI]
    omega
  have hTF : T ≠ swapTableau D k hk hkn hDk := by
    refine (ne_of_entry_ne (i := (cellOf T k).1) (j := (cellOf T k).2) ?_).symm
    rw [(orbitEntries_sk_sl_sk T hk hkn hln hka hAl hDk).1, entry_cellOf T hkI]
    omega
  have hTF' : T ≠ swapTableau E (k + 1) hl hln hEl := by
    rw [← swapTableau_braid T hk hkn hln hka hla hAl hBk hDk hEl]
    exact hTF
  -- the swapped-back partners
  have hAk : SwapAdmissible A k := swapAdmissible_swapTableau T hk hkn hka
  have hBl : SwapAdmissible B (k + 1) := swapAdmissible_swapTableau T hl hln hla
  have hAT : swapTableau A k hk hkn hAk = T := swapTableau_involutive T hk hkn hka
  have hBT : swapTableau B (k + 1) hl hln hBl = T := swapTableau_involutive T hl hln hla
  -- parameters
  have hdA : axialDist A k = -axialDist T k := axialDist_swapTableau T hk hkn hka
  have hdB : axialDist B (k + 1) = -axialDist T (k + 1) :=
    axialDist_swapTableau T hl hln hla
  have hdD : axialDist B k = axialDist T k + axialDist T (k + 1) :=
    axialDist_swapTableau_succ T hk (by omega) hla
  have hdE : axialDist A (k + 1) = axialDist T k + axialDist T (k + 1) :=
    axialDist_succ_swapTableau T hk hkn (by omega) hka
  -- expand both sides
  rw [genMat_braid_lhs_expand q k hk hkn hl hln hka hla hAl T,
    genMat_braid_rhs_expand q k hk hkn hl hln hka hla hBk T]
  -- the two off-diagonal entries this row sees
  have hentA : genMat q k hk hkn T A = offDiag q (axialDist A k) := by
    have h := genMat_swap q k hk hkn hAk (by rw [hAT]; exact hTA)
    rwa [hAT] at h
  have hentB : genMat q (k + 1) hl hln T B = offDiag q (axialDist B (k + 1)) := by
    have h := genMat_swap q (k + 1) hl hln hBl (by rw [hBT]; exact hTB)
    rwa [hBT] at h
  -- resolve every entry
  rw [genMat_diag, genMat_diag,
    genMat_apply_of_ne q k hk hkn hTB hBk (by rw [← hE]; exact hTE),
    genMat_apply_of_ne q k hk hkn hTD hDk hTF,
    genMat_apply_of_ne q (k + 1) hl hln hTA hAl (by rw [← hD]; exact hTD),
    genMat_apply_of_ne q (k + 1) hl hln hTE hEl hTF',
    hentA, hentB, hdA, hdB]
  -- the algebra
  have hp0 : axialDist T k ≠ 0 := axialDist_ne_zero T hkI hkI'
  have hr0 : axialDist T (k + 1) ≠ 0 := axialDist_ne_zero T hkI' hkI''
  have hpr0 : axialDist T k + axialDist T (k + 1) ≠ 0 := by
    rw [← hdE]; exact axialDist_ne_zero A hkI' hkI''
  have hprodp := offDiag_mul_neg q hp0
  have hprodr := offDiag_mul_neg q hr0
  have hsump := seminormalParam_add_neg q _ hq0 (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T k ≠ 0))
  have hsumr := seminormalParam_add_neg q _ hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T (k + 1) ≠ 0))
  have hrel := seminormalParam_rel q (axialDist T k) (axialDist T (k + 1)) hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T k ≠ 0))
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T (k + 1) ≠ 0))
    (zpow_ne_one hq0 hq2 (by omega : -2 * (axialDist T k + axialDist T (k + 1)) ≠ 0))
  -- `(a₂ - a₁)` times the relation, plus the two trace identities and the two
  -- determinant identities; see `braid_diag_identity` for the factorisation.
  linear_combination
    (seminormalParam q (axialDist T (k + 1)) - seminormalParam q (axialDist T k)) * hrel
      + seminormalParam q (axialDist T k + axialDist T (k + 1))
          * seminormalParam q (axialDist T k) * hsump
      - seminormalParam q (axialDist T k + axialDist T (k + 1))
          * seminormalParam q (axialDist T (k + 1)) * hsumr
      + seminormalParam q (axialDist T k + axialDist T (k + 1)) * hprodp
      - seminormalParam q (axialDist T k + axialDist T (k + 1)) * hprodr

/-- **The braid relation on a generic orbit, at the tableau level.**

`ρ(σ_k)ρ(σ_{k+1})ρ(σ_k) = ρ(σ_{k+1})ρ(σ_k)ρ(σ_{k+1})` in column `T`, for a `T` whose
`⟨s_k, s_{k+1}⟩`-orbit is the full size-`6` one — that is, all six admissibilities hold.

The six rows split three and three: `D`, `E`, `F` are identities of the ambient ring (the
two sides are the same product reordered), while `T`, `A`, `B` each reduce to the single
relation `seminormalParam_rel`, with multiples `(a₂ - a₁)`, `-off(p)`, `+off(r)`.

Non-generic orbits — where one of the five non-`T` words fails to be `SwapAdmissible` and
terms drop — are **not** covered here; that case tree is the remaining work on
`hoefsmit_seminormal_rep`. -/
theorem genMat_braid_generic (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (k : ℕ) (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hl : 1 ≤ k + 1) (hln : k + 1 + 1 ≤ μ.cells.card)
    {T : StandardYoungTableau μ}
    (hka : SwapAdmissible T k) (hla : SwapAdmissible T (k + 1))
    (hAl : SwapAdmissible (swapTableau T k hk hkn hka) (k + 1))
    (hBk : SwapAdmissible (swapTableau T (k + 1) hl hln hla) k)
    (hDk : SwapAdmissible
      (swapTableau (swapTableau T k hk hkn hka) (k + 1) hl hln hAl) k)
    (hEl : SwapAdmissible
      (swapTableau (swapTableau T (k + 1) hl hln hla) k hk hkn hBk) (k + 1))
    (T' : StandardYoungTableau μ) :
    (genMat q k hk hkn * genMat q (k + 1) hl hln * genMat q k hk hkn) T' T
      = (genMat q (k + 1) hl hln * genMat q k hk hkn * genMat q (k + 1) hl hln) T' T := by
  classical
  have hkI : k ∈ Set.Icc 1 μ.cells.card := ⟨hk, by omega⟩
  have hkI' : k + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hkn⟩
  have hkI'' : k + 1 + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hln⟩
  set A := swapTableau T k hk hkn hka with hA
  set B := swapTableau T (k + 1) hl hln hla with hB
  set D := swapTableau A (k + 1) hl hln hAl with hD
  set E := swapTableau B k hk hkn hBk with hE
  set F := swapTableau D k hk hkn hDk with hF
  -- the two routes to the longest word agree
  have hFE : F = swapTableau E (k + 1) hl hln hEl :=
    swapTableau_braid T hk hkn hln hka hla hAl hBk hDk hEl
  -- entry values at the two distinguished cells
  have eT1 : T.entry (cellOf T k).1 (cellOf T k).2 = k := entry_cellOf T hkI
  have eT2 : T.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 = k + 1 := entry_cellOf T hkI'
  have eA1 : A.entry (cellOf T k).1 (cellOf T k).2 = k + 1 := (orbitEntries_sk T hk hkn hka).1
  have eA2 : A.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 = k :=
    (orbitEntries_sk T hk hkn hka).2
  have eB1 : B.entry (cellOf T k).1 (cellOf T k).2 = k := (orbitEntries_sl T hk hln hla).1
  have eB2 : B.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 = k + 2 :=
    (orbitEntries_sl T hk hln hla).2
  have eD1 : D.entry (cellOf T k).1 (cellOf T k).2 = k + 2 :=
    (orbitEntries_sl_sk T hk hkn hln hka hAl).1
  have eD2 : D.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 = k :=
    (orbitEntries_sl_sk T hk hkn hln hka hAl).2
  have eE1 : E.entry (cellOf T k).1 (cellOf T k).2 = k + 1 :=
    (orbitEntries_sk_sl T hk hkn hln hla hBk).1
  have eE2 : E.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 = k + 2 :=
    (orbitEntries_sk_sl T hk hkn hln hla hBk).2
  have eF1 : F.entry (cellOf T k).1 (cellOf T k).2 = k + 2 :=
    (orbitEntries_sk_sl_sk T hk hkn hln hka hAl hDk).1
  have eF2 : F.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 = k + 1 :=
    (orbitEntries_sk_sl_sk T hk hkn hln hka hAl hDk).2
  -- the fifteen distinctness facts, each read off one column of the table
  have nTA : T ≠ A := ne_of_entry_ne (by rw [eT1, eA1]; omega)
  have nTB : T ≠ B := ne_of_entry_ne (by rw [eT2, eB2]; omega)
  have nTD : T ≠ D := ne_of_entry_ne (by rw [eT1, eD1]; omega)
  have nTE : T ≠ E := ne_of_entry_ne (by rw [eT1, eE1]; omega)
  have nTF : T ≠ F := ne_of_entry_ne (by rw [eT1, eF1]; omega)
  have nAB : A ≠ B := ne_of_entry_ne (by rw [eA1, eB1]; omega)
  have nAD : A ≠ D := ne_of_entry_ne (by rw [eA1, eD1]; omega)
  have nAE : A ≠ E := ne_of_entry_ne (by rw [eA2, eE2]; omega)
  have nAF : A ≠ F := ne_of_entry_ne (by rw [eA1, eF1]; omega)
  have nBD : B ≠ D := ne_of_entry_ne (by rw [eB1, eD1]; omega)
  have nBE : B ≠ E := ne_of_entry_ne (by rw [eB1, eE1]; omega)
  have nBF : B ≠ F := ne_of_entry_ne (by rw [eB1, eF1]; omega)
  have nDE : D ≠ E := ne_of_entry_ne (by rw [eD1, eE1]; omega)
  have nDF : D ≠ F := ne_of_entry_ne (by rw [eD2, eF2]; omega)
  have nEF : E ≠ F := ne_of_entry_ne (by rw [eE1, eF1]; omega)
  -- derived admissibilities and the swap-back identities
  have hAk : SwapAdmissible A k := swapAdmissible_swapTableau T hk hkn hka
  have hBl : SwapAdmissible B (k + 1) := swapAdmissible_swapTableau T hl hln hla
  have hDl : SwapAdmissible D (k + 1) := swapAdmissible_swapTableau A hl hln hAl
  have hEk : SwapAdmissible E k := swapAdmissible_swapTableau B hk hkn hBk
  have bAT : swapTableau A k hk hkn hAk = T := swapTableau_involutive T hk hkn hka
  have bBT : swapTableau B (k + 1) hl hln hBl = T := swapTableau_involutive T hl hln hla
  have bDA : swapTableau D (k + 1) hl hln hDl = A := swapTableau_involutive A hl hln hAl
  have bEB : swapTableau E k hk hkn hEk = B := swapTableau_involutive B hk hkn hBk
  -- the six axial distances
  have dAk : axialDist A k = -axialDist T k := axialDist_swapTableau T hk hkn hka
  have dBl : axialDist B (k + 1) = -axialDist T (k + 1) := axialDist_swapTableau T hl hln hla
  have dAl : axialDist A (k + 1) = axialDist T k + axialDist T (k + 1) :=
    axialDist_succ_swapTableau T hk hkn (by omega) hka
  have dBk : axialDist B k = axialDist T k + axialDist T (k + 1) :=
    axialDist_swapTableau_succ T hk (by omega) hla
  have dDk : axialDist D k = axialDist T (k + 1) :=
    axialDist_swapTableau_word_left T hk hkn (by omega) hka hAl
  have dEl : axialDist E (k + 1) = axialDist T k :=
    axialDist_swapTableau_word_right T hk (by omega) hla hBk
  -- the algebraic inputs
  have hp0 : axialDist T k ≠ 0 := axialDist_ne_zero T hkI hkI'
  have hr0 : axialDist T (k + 1) ≠ 0 := axialDist_ne_zero T hkI' hkI''
  have hpr0 : axialDist T k + axialDist T (k + 1) ≠ 0 := by
    rw [← dAl]; exact axialDist_ne_zero A hkI' hkI''
  have hprodp := offDiag_mul_neg q hp0
  have hprodr := offDiag_mul_neg q hr0
  have hsump := seminormalParam_add_neg q (axialDist T k) hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T k ≠ 0))
  have hsumr := seminormalParam_add_neg q (axialDist T (k + 1)) hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T (k + 1) ≠ 0))
  have hrel := seminormalParam_rel q (axialDist T k) (axialDist T (k + 1)) hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T k ≠ 0))
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T (k + 1) ≠ 0))
    (zpow_ne_one hq0 hq2 (by omega : -2 * (axialDist T k + axialDist T (k + 1)) ≠ 0))
  rw [genMat_braid_lhs_expand q k hk hkn hl hln hka hla hAl T',
    genMat_braid_rhs_expand q k hk hkn hl hln hka hla hBk T']
  by_cases h1 : T' = T
  · subst h1
    simp only [← hA, ← hB, ← hD, ← hE, ← hF]
    have entA : genMat q k hk hkn T' A = offDiag q (axialDist A k) := by
      have h := genMat_swap q k hk hkn hAk (by rw [bAT]; exact nTA)
      rwa [bAT] at h
    have entB : genMat q (k + 1) hl hln T' B = offDiag q (axialDist B (k + 1)) := by
      have h := genMat_swap q (k + 1) hl hln hBl (by rw [bBT]; exact nTB)
      rwa [bBT] at h
    rw [genMat_diag, genMat_diag, entA, entB, dAk, dBl,
      genMat_apply_of_ne q k hk hkn nTB hBk (by rw [← hE]; exact nTE),
      genMat_apply_of_ne q k hk hkn nTD hDk (by rw [← hF]; exact nTF),
      genMat_apply_of_ne q (k + 1) hl hln nTA hAl (by rw [← hD]; exact nTD),
      genMat_apply_of_ne q (k + 1) hl hln nTE hEl (by rw [← hFE]; exact nTF)]
    linear_combination
      (seminormalParam q (axialDist T' (k + 1)) - seminormalParam q (axialDist T' k)) * hrel
        + seminormalParam q (axialDist T' k + axialDist T' (k + 1))
            * seminormalParam q (axialDist T' k) * hsump
        - seminormalParam q (axialDist T' k + axialDist T' (k + 1))
            * seminormalParam q (axialDist T' (k + 1)) * hsumr
        + seminormalParam q (axialDist T' k + axialDist T' (k + 1)) * hprodp
        - seminormalParam q (axialDist T' k + axialDist T' (k + 1)) * hprodr
  by_cases h2 : T' = A
  · subst h2
    simp only [← hA, ← hB, ← hD, ← hE, ← hF]
    have entT : genMat q k hk hkn A T = offDiag q (axialDist T k) :=
      genMat_swap q k hk hkn hka (by rw [← hA]; exact nTA.symm)
    rw [entT,
      genMat_apply_of_ne q k hk hkn nAB hBk (by rw [← hE]; exact nAE),
      genMat_diag, dAk,
      genMat_apply_of_ne q k hk hkn nAD hDk (by rw [← hF]; exact nAF),
      genMat_apply_of_ne q (k + 1) hl hln nTA.symm hla (by rw [← hB]; exact nAB),
      genMat_diag, dAl,
      genMat_apply_of_ne q (k + 1) hl hln nAB hBl (by rw [bBT]; exact nTA.symm),
      genMat_apply_of_ne q (k + 1) hl hln nAE hEl (by rw [← hFE]; exact nAF)]
    linear_combination
      (-offDiag q (axialDist T k)) * hrel
        + seminormalParam q (axialDist T k + axialDist T (k + 1))
            * offDiag q (axialDist T k) * hsump
  by_cases h3 : T' = B
  · subst h3
    simp only [← hA, ← hB, ← hD, ← hE, ← hF]
    have entT : genMat q (k + 1) hl hln B T = offDiag q (axialDist T (k + 1)) :=
      genMat_swap q (k + 1) hl hln hla (by rw [← hB]; exact nTB.symm)
    rw [genMat_apply_of_ne q k hk hkn nTB.symm hka (by rw [← hA]; exact nAB.symm),
      genMat_diag, dBk,
      genMat_apply_of_ne q k hk hkn nAB.symm hAk (by rw [bAT]; exact nTB.symm),
      genMat_apply_of_ne q k hk hkn nBD hDk (by rw [← hF]; exact nBF),
      entT,
      genMat_apply_of_ne q (k + 1) hl hln nAB.symm hAl (by rw [← hD]; exact nBD),
      genMat_diag, dBl,
      genMat_apply_of_ne q (k + 1) hl hln nBE hEl (by rw [← hFE]; exact nBF)]
    linear_combination
      offDiag q (axialDist T (k + 1)) * hrel
        - seminormalParam q (axialDist T k + axialDist T (k + 1))
            * offDiag q (axialDist T (k + 1)) * hsumr
  by_cases h4 : T' = D
  · subst h4
    simp only [← hA, ← hB, ← hD, ← hE, ← hF]
    have entA : genMat q (k + 1) hl hln D A = offDiag q (axialDist A (k + 1)) :=
      genMat_swap q (k + 1) hl hln hAl (by rw [← hD]; exact nAD.symm)
    rw [genMat_apply_of_ne q k hk hkn nTD.symm hka (by rw [← hA]; exact nAD.symm),
      genMat_apply_of_ne q k hk hkn nBD.symm hBk (by rw [← hE]; exact nDE),
      genMat_apply_of_ne q k hk hkn nAD.symm hAk (by rw [bAT]; exact nTD.symm),
      genMat_diag, dDk,
      genMat_apply_of_ne q (k + 1) hl hln nTD.symm hla (by rw [← hB]; exact nBD.symm),
      entA, dAl,
      genMat_apply_of_ne q (k + 1) hl hln nBD.symm hBl (by rw [bBT]; exact nTD.symm),
      genMat_apply_of_ne q (k + 1) hl hln nDE hEl (by rw [← hFE]; exact nDF)]
    ring
  by_cases h5 : T' = E
  · subst h5
    simp only [← hA, ← hB, ← hD, ← hE, ← hF]
    have entB : genMat q k hk hkn E B = offDiag q (axialDist B k) :=
      genMat_swap q k hk hkn hBk (by rw [← hE]; exact nBE.symm)
    rw [genMat_apply_of_ne q k hk hkn nTE.symm hka (by rw [← hA]; exact nAE.symm),
      entB, dBk,
      genMat_apply_of_ne q k hk hkn nAE.symm hAk (by rw [bAT]; exact nTE.symm),
      genMat_apply_of_ne q k hk hkn nDE.symm hDk (by rw [← hF]; exact nEF),
      genMat_apply_of_ne q (k + 1) hl hln nTE.symm hla (by rw [← hB]; exact nBE.symm),
      genMat_apply_of_ne q (k + 1) hl hln nAE.symm hAl (by rw [← hD]; exact nDE.symm),
      genMat_apply_of_ne q (k + 1) hl hln nBE.symm hBl (by rw [bBT]; exact nTE.symm),
      genMat_diag, dEl]
    ring
  by_cases h6 : T' = F
  · subst h6
    simp only [← hA, ← hB, ← hD, ← hE, ← hF]
    have entD : genMat q k hk hkn F D = offDiag q (axialDist D k) :=
      genMat_swap q k hk hkn hDk (by rw [← hF]; exact nDF.symm)
    have entE : genMat q (k + 1) hl hln F E = offDiag q (axialDist E (k + 1)) := by
      rw [hFE]
      exact genMat_swap q (k + 1) hl hln hEl (by rw [← hFE]; exact nEF.symm)
    rw [genMat_apply_of_ne q k hk hkn nTF.symm hka (by rw [← hA]; exact nAF.symm),
      genMat_apply_of_ne q k hk hkn nBF.symm hBk (by rw [← hE]; exact nEF.symm),
      genMat_apply_of_ne q k hk hkn nAF.symm hAk (by rw [bAT]; exact nTF.symm),
      entD, dDk,
      genMat_apply_of_ne q (k + 1) hl hln nTF.symm hla (by rw [← hB]; exact nBF.symm),
      genMat_apply_of_ne q (k + 1) hl hln nAF.symm hAl (by rw [← hD]; exact nDF.symm),
      genMat_apply_of_ne q (k + 1) hl hln nBF.symm hBl (by rw [bBT]; exact nTF.symm),
      entE, dEl]
    ring
  · -- every other row is zero on both sides
    rw [genMat_apply_of_ne q k hk hkn h1 hka (by rw [← hA]; exact h2),
      genMat_apply_of_ne q k hk hkn h3 hBk (by rw [← hE]; exact h5),
      genMat_apply_of_ne q k hk hkn h2 hAk (by rw [bAT]; exact h1),
      genMat_apply_of_ne q k hk hkn h4 hDk (by rw [← hF]; exact h6),
      genMat_apply_of_ne q (k + 1) hl hln h1 hla (by rw [← hB]; exact h3),
      genMat_apply_of_ne q (k + 1) hl hln h2 hAl (by rw [← hD]; exact h4),
      genMat_apply_of_ne q (k + 1) hl hln h3 hBl (by rw [bBT]; exact h1),
      genMat_apply_of_ne q (k + 1) hl hln h5 hEl (by rw [← hFE]; exact h6)]
    ring

/-- **The braid relation on a size-`1` orbit** — both generators fix `T`.

Both columns are scalar, so each triple product collapses to a single entry times
`a(d_k)a(d_l)`, and the two sides differ by `a(d_k)a(d_l)·(a(d_k) - a(d_l))`.

That is *not* zero for arbitrary scalars: at `d = ±1` the parameter is `q` or `-q⁻¹`, and
the mixed product would give `-(q + q⁻¹) ≠ 0`.  The identity holds because the mixed
configuration cannot occur — `axialDist_eq_of_not_admissible` — which is the only place in
the whole construction where the braid depends on a *geometric* fact about `μ` rather than
on the parameter algebra. -/
theorem genMat_braid_of_both_fixed (k : ℕ) (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card)
    (hl : 1 ≤ k + 1) (hln : k + 1 + 1 ≤ μ.cells.card)
    {T : StandardYoungTableau μ}
    (hka : ¬ SwapAdmissible T k) (hla : ¬ SwapAdmissible T (k + 1))
    (T' : StandardYoungTableau μ) :
    (genMat q k hk hkn * genMat q (k + 1) hl hln * genMat q k hk hkn) T' T
      = (genMat q (k + 1) hl hln * genMat q k hk hkn * genMat q (k + 1) hl hln) T' T := by
  classical
  have hd : axialDist T k = axialDist T (k + 1) :=
    axialDist_eq_of_not_admissible T hk (by omega) hka hla
  rw [genMat_mul_apply_of_not_admissible q k hk hkn
      (genMat q k hk hkn * genMat q (k + 1) hl hln) hka T',
    genMat_mul_apply_of_not_admissible q (k + 1) hl hln (genMat q k hk hkn) hla T',
    genMat_mul_apply_of_not_admissible q (k + 1) hl hln
      (genMat q (k + 1) hl hln * genMat q k hk hkn) hla T',
    genMat_mul_apply_of_not_admissible q k hk hkn (genMat q (k + 1) hl hln) hka T']
  by_cases h : T' = T
  · -- the two sides become the same product once `hd` identifies the scalars
    subst h
    rw [genMat_diag, genMat_diag, hd]
  · rw [genMat_of_not_admissible q k hk hkn h hka,
      genMat_of_not_admissible q (k + 1) hl hln h hla]
    ring

/-- **The braid relation on a size-`2` orbit** — `σ_k` moves `T`, `σ_{k+1}` fixes both `T`
and `s_k·T`, so the orbit is exactly `{T, s_k·T}`.

Only two rows are non-zero, and they close differently:

* the `s_k·T` row is `braid_rowA_identity` verbatim — the same identity as in the generic
  case;
* the `T` row is the generic diagonal identity **minus** the term `a₃·(1 + a₂a(-r))`, which
  the right-hand side does not produce here.  The two sides match only because that factor
  is `0` — `one_add_seminormalParam_mul_neg_of_scalar`, available because `σ_{k+1}` fixing
  `T` forces `r = ±1` by the trichotomy.

So the smaller orbit is not a degenerate special case of the generic one: it is the generic
identity with a term deleted, and the deletion is legitimate exactly because of the scalar
degeneracy. -/
theorem genMat_braid_of_succ_fixed (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (k : ℕ) (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hl : 1 ≤ k + 1) (hln : k + 1 + 1 ≤ μ.cells.card)
    {T : StandardYoungTableau μ}
    (hka : SwapAdmissible T k) (hla : ¬ SwapAdmissible T (k + 1))
    (hAl : ¬ SwapAdmissible (swapTableau T k hk hkn hka) (k + 1))
    (T' : StandardYoungTableau μ) :
    (genMat q k hk hkn * genMat q (k + 1) hl hln * genMat q k hk hkn) T' T
      = (genMat q (k + 1) hl hln * genMat q k hk hkn * genMat q (k + 1) hl hln) T' T := by
  classical
  have hkI : k ∈ Set.Icc 1 μ.cells.card := ⟨hk, by omega⟩
  have hkI' : k + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hkn⟩
  have hkI'' : k + 1 + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hln⟩
  set A := swapTableau T k hk hkn hka with hA
  have nTA : T ≠ A := (swapTableau_ne T hk hkn hka).symm
  have hAk : SwapAdmissible A k := swapAdmissible_swapTableau T hk hkn hka
  have bAT : swapTableau A k hk hkn hAk = T := swapTableau_involutive T hk hkn hka
  have dAk : axialDist A k = -axialDist T k := axialDist_swapTableau T hk hkn hka
  have dAl : axialDist A (k + 1) = axialDist T k + axialDist T (k + 1) :=
    axialDist_succ_swapTableau T hk hkn (by omega) hka
  -- `σ_{k+1}` fixing `T` forces a scalar distance, hence the vanishing factor
  have hscalar : axialDist T (k + 1) = 1 ∨ axialDist T (k + 1) = -1 := by
    rcases axialDist_trichotomy T hkI' hkI'' with h | h | h
    · exact Or.inl h
    · exact Or.inr h
    · exact absurd h hla
  have hdeg : 1 + seminormalParam q (axialDist T (k + 1))
      * seminormalParam q (-axialDist T (k + 1)) = 0 :=
    one_add_seminormalParam_mul_neg_of_scalar q hq0 hq2 hscalar
  -- the algebraic inputs
  have hp0 : axialDist T k ≠ 0 := axialDist_ne_zero T hkI hkI'
  have hr0 : axialDist T (k + 1) ≠ 0 := axialDist_ne_zero T hkI' hkI''
  have hpr0 : axialDist T k + axialDist T (k + 1) ≠ 0 := by
    rw [← dAl]; exact axialDist_ne_zero A hkI' hkI''
  have hprodp := offDiag_mul_neg q hp0
  have hsump := seminormalParam_add_neg q (axialDist T k) hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T k ≠ 0))
  have hsumr := seminormalParam_add_neg q (axialDist T (k + 1)) hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T (k + 1) ≠ 0))
  have hrel := seminormalParam_rel q (axialDist T k) (axialDist T (k + 1)) hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T k ≠ 0))
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T (k + 1) ≠ 0))
    (zpow_ne_one hq0 hq2 (by omega : -2 * (axialDist T k + axialDist T (k + 1)) ≠ 0))
  -- peel the three factors; the `k+1` columns are scalar, the `k` column is not
  rw [genMat_mul_apply q k hk hkn (genMat q k hk hkn * genMat q (k + 1) hl hln) hka T',
    genMat_mul_apply_of_not_admissible q (k + 1) hl hln (genMat q k hk hkn) hla T',
    genMat_mul_apply_of_not_admissible q (k + 1) hl hln (genMat q k hk hkn) hAl T',
    genMat_mul_apply_of_not_admissible q (k + 1) hl hln
      (genMat q (k + 1) hl hln * genMat q k hk hkn) hla T',
    genMat_mul_apply q k hk hkn (genMat q (k + 1) hl hln) hka T', dAl]
  by_cases h1 : T' = T
  · subst h1
    simp only [← hA]
    have entA : genMat q k hk hkn T' A = offDiag q (axialDist A k) := by
      have h := genMat_swap q k hk hkn hAk (by rw [bAT]; exact nTA)
      rwa [bAT] at h
    rw [genMat_diag, genMat_diag, entA, dAk,
      genMat_of_not_admissible q (k + 1) hl hln nTA hAl]
    linear_combination
      (seminormalParam q (axialDist T' (k + 1)) - seminormalParam q (axialDist T' k)) * hrel
        + seminormalParam q (axialDist T' k + axialDist T' (k + 1))
            * seminormalParam q (axialDist T' k) * hsump
        - seminormalParam q (axialDist T' k + axialDist T' (k + 1))
            * seminormalParam q (axialDist T' (k + 1)) * hsumr
        + seminormalParam q (axialDist T' k + axialDist T' (k + 1)) * hdeg
        + seminormalParam q (axialDist T' k + axialDist T' (k + 1)) * hprodp
  by_cases h2 : T' = A
  · subst h2
    simp only [← hA]
    have entT : genMat q k hk hkn A T = offDiag q (axialDist T k) :=
      genMat_swap q k hk hkn hka (by rw [← hA]; exact nTA.symm)
    rw [entT, genMat_diag, dAk, genMat_diag, dAl,
      genMat_of_not_admissible q (k + 1) hl hln nTA.symm hla]
    linear_combination
      (-offDiag q (axialDist T k)) * hrel
        + seminormalParam q (axialDist T k + axialDist T (k + 1))
            * offDiag q (axialDist T k) * hsump
  · -- both rows outside `{T, s_k·T}` vanish on each side
    rw [genMat_apply_of_ne q k hk hkn h1 hka (by rw [← hA]; exact h2),
      genMat_apply_of_ne q k hk hkn h2 hAk (by rw [bAT]; exact h1),
      genMat_of_not_admissible q (k + 1) hl hln h1 hla,
      genMat_of_not_admissible q (k + 1) hl hln h2 hAl]
    ring

/-- **The braid on the mirror size-`2` orbit** — `σ_{k+1}` moves `T`, `σ_k` fixes both `T`
and `s_{k+1}·T`, so the orbit is `{T, s_{k+1}·T}`.

The mirror of `genMat_braid_of_succ_fixed`, and it deletes the *other* term: here the **left**
side lacks `a₃(1 + a₁a(-p))`, and the degeneracy that licenses it is at `p = ±1` rather than
`r = ±1`.  The moved row is `braid_rowB_identity` verbatim. -/
theorem genMat_braid_of_fixed_succ (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (k : ℕ) (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hl : 1 ≤ k + 1) (hln : k + 1 + 1 ≤ μ.cells.card)
    {T : StandardYoungTableau μ}
    (hka : ¬ SwapAdmissible T k) (hla : SwapAdmissible T (k + 1))
    (hBk : ¬ SwapAdmissible (swapTableau T (k + 1) hl hln hla) k)
    (T' : StandardYoungTableau μ) :
    (genMat q k hk hkn * genMat q (k + 1) hl hln * genMat q k hk hkn) T' T
      = (genMat q (k + 1) hl hln * genMat q k hk hkn * genMat q (k + 1) hl hln) T' T := by
  classical
  have hkI : k ∈ Set.Icc 1 μ.cells.card := ⟨hk, by omega⟩
  have hkI' : k + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hkn⟩
  have hkI'' : k + 1 + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hln⟩
  set B := swapTableau T (k + 1) hl hln hla with hB
  have nTB : T ≠ B := (swapTableau_ne T hl hln hla).symm
  have hBl : SwapAdmissible B (k + 1) := swapAdmissible_swapTableau T hl hln hla
  have bBT : swapTableau B (k + 1) hl hln hBl = T := swapTableau_involutive T hl hln hla
  have dBl : axialDist B (k + 1) = -axialDist T (k + 1) := axialDist_swapTableau T hl hln hla
  have dBk : axialDist B k = axialDist T k + axialDist T (k + 1) :=
    axialDist_swapTableau_succ T hk (by omega) hla
  -- `σ_k` fixing `T` forces a scalar distance at `p` this time
  have hscalar : axialDist T k = 1 ∨ axialDist T k = -1 := by
    rcases axialDist_trichotomy T hkI hkI' with h | h | h
    · exact Or.inl h
    · exact Or.inr h
    · exact absurd h hka
  have hdegp : 1 + seminormalParam q (axialDist T k)
      * seminormalParam q (-axialDist T k) = 0 :=
    one_add_seminormalParam_mul_neg_of_scalar q hq0 hq2 hscalar
  have hp0 : axialDist T k ≠ 0 := axialDist_ne_zero T hkI hkI'
  have hr0 : axialDist T (k + 1) ≠ 0 := axialDist_ne_zero T hkI' hkI''
  have hpr0 : axialDist T k + axialDist T (k + 1) ≠ 0 := by
    rw [← dBk]; exact axialDist_ne_zero B hkI hkI'
  have hprodr := offDiag_mul_neg q hr0
  have hsump := seminormalParam_add_neg q (axialDist T k) hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T k ≠ 0))
  have hsumr := seminormalParam_add_neg q (axialDist T (k + 1)) hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T (k + 1) ≠ 0))
  have hrel := seminormalParam_rel q (axialDist T k) (axialDist T (k + 1)) hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T k ≠ 0))
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T (k + 1) ≠ 0))
    (zpow_ne_one hq0 hq2 (by omega : -2 * (axialDist T k + axialDist T (k + 1)) ≠ 0))
  rw [genMat_mul_apply_of_not_admissible q k hk hkn
      (genMat q k hk hkn * genMat q (k + 1) hl hln) hka T',
    genMat_mul_apply q (k + 1) hl hln (genMat q k hk hkn) hla T',
    genMat_mul_apply q (k + 1) hl hln
      (genMat q (k + 1) hl hln * genMat q k hk hkn) hla T',
    genMat_mul_apply_of_not_admissible q k hk hkn (genMat q (k + 1) hl hln) hka T',
    genMat_mul_apply_of_not_admissible q k hk hkn (genMat q (k + 1) hl hln) hBk T', dBk]
  by_cases h1 : T' = T
  · subst h1
    simp only [← hB]
    have entB : genMat q (k + 1) hl hln T' B = offDiag q (axialDist B (k + 1)) := by
      have h := genMat_swap q (k + 1) hl hln hBl (by rw [bBT]; exact nTB)
      rwa [bBT] at h
    rw [genMat_diag, genMat_diag, entB, dBl,
      genMat_of_not_admissible q k hk hkn nTB hBk]
    linear_combination
      (seminormalParam q (axialDist T' (k + 1)) - seminormalParam q (axialDist T' k)) * hrel
        + seminormalParam q (axialDist T' k + axialDist T' (k + 1))
            * seminormalParam q (axialDist T' k) * hsump
        - seminormalParam q (axialDist T' k + axialDist T' (k + 1))
            * seminormalParam q (axialDist T' (k + 1)) * hsumr
        - seminormalParam q (axialDist T' k + axialDist T' (k + 1)) * hdegp
        - seminormalParam q (axialDist T' k + axialDist T' (k + 1)) * hprodr
  by_cases h2 : T' = B
  · subst h2
    simp only [← hB]
    have entT : genMat q (k + 1) hl hln B T = offDiag q (axialDist T (k + 1)) :=
      genMat_swap q (k + 1) hl hln hla (by rw [← hB]; exact nTB.symm)
    rw [entT, genMat_diag, dBk, genMat_diag, dBl,
      genMat_of_not_admissible q k hk hkn nTB.symm hka]
    linear_combination
      offDiag q (axialDist T (k + 1)) * hrel
        - seminormalParam q (axialDist T k + axialDist T (k + 1))
            * offDiag q (axialDist T (k + 1)) * hsumr
  · rw [genMat_of_not_admissible q k hk hkn h1 hka,
      genMat_of_not_admissible q k hk hkn h2 hBk,
      genMat_apply_of_ne q (k + 1) hl hln h1 hla (by rw [← hB]; exact h2),
      genMat_apply_of_ne q (k + 1) hl hln h2 hBl (by rw [bBT]; exact h1)]
    ring

/-! ### Size-`3` orbits, and why there are three of them

A size-`3` orbit is a domino plus a disjoint cell (`Orbit3Braid`), and `T` can sit at any of
its three positions.  Each position gives a *different* admissibility pattern, so the size-3
case is three theorems, not one:

| `T`'s position | `hka` | `hla` | further |
|---|---|---|---|
| the `σ_k`-fixed end | ✗ | ✓ | `s_{k+1}·T` is `k`-admissible |
| the middle | ✓ | ✓ | **neither** `s_k·T` nor `s_{k+1}·T` extends |
| the `σ_{k+1}`-fixed end | ✓ | ✗ | `s_k·T` is `(k+1)`-admissible |

Note the middle position has `hka` **and** `hla` — the same leading flags as a generic
size-`6` orbit.  So "both generators move `T`" does *not* imply the orbit is generic, and any
final assembly must split further on `hAl`/`hBk` rather than stopping at `(hka, hla)`.
-/

/-- **Size-`3` orbit, `T` at the `σ_{k+1}`-fixed end.**  `σ_k` moves `T`, `σ_{k+1}` fixes it,
but `s_k·T` *is* `(k+1)`-admissible, so the orbit runs `T → s_k·T → s_{k+1}s_k·T` and stops.

Compared with the size-`2` case `genMat_braid_of_succ_fixed`, the `T` and `s_k·T` rows carry
the *same* two identities; what is new is the third row, which closes by `ring` alone once
`axialDist_swapTableau_word_left` supplies `d_k(s_{k+1}s_k·T) = r`. -/
theorem genMat_braid_of_succ_fixed_three (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (k : ℕ) (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hl : 1 ≤ k + 1) (hln : k + 1 + 1 ≤ μ.cells.card)
    {T : StandardYoungTableau μ}
    (hka : SwapAdmissible T k) (hla : ¬ SwapAdmissible T (k + 1))
    (hAl : SwapAdmissible (swapTableau T k hk hkn hka) (k + 1))
    (hDk : ¬ SwapAdmissible
      (swapTableau (swapTableau T k hk hkn hka) (k + 1) hl hln hAl) k)
    (T' : StandardYoungTableau μ) :
    (genMat q k hk hkn * genMat q (k + 1) hl hln * genMat q k hk hkn) T' T
      = (genMat q (k + 1) hl hln * genMat q k hk hkn * genMat q (k + 1) hl hln) T' T := by
  classical
  have hkI : k ∈ Set.Icc 1 μ.cells.card := ⟨hk, by omega⟩
  have hkI' : k + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hkn⟩
  have hkI'' : k + 1 + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hln⟩
  set A := swapTableau T k hk hkn hka with hA
  set D := swapTableau A (k + 1) hl hln hAl with hD
  have hAk : SwapAdmissible A k := swapAdmissible_swapTableau T hk hkn hka
  have bAT : swapTableau A k hk hkn hAk = T := swapTableau_involutive T hk hkn hka
  have dAk : axialDist A k = -axialDist T k := axialDist_swapTableau T hk hkn hka
  have dAl : axialDist A (k + 1) = axialDist T k + axialDist T (k + 1) :=
    axialDist_succ_swapTableau T hk hkn (by omega) hka
  have dDk : axialDist D k = axialDist T (k + 1) :=
    axialDist_swapTableau_word_left T hk hkn (by omega) hka hAl
  -- distinctness, all at the first distinguished cell
  have eT1 : T.entry (cellOf T k).1 (cellOf T k).2 = k := entry_cellOf T hkI
  have eA1 : A.entry (cellOf T k).1 (cellOf T k).2 = k + 1 := (orbitEntries_sk T hk hkn hka).1
  have eD1 : D.entry (cellOf T k).1 (cellOf T k).2 = k + 2 :=
    (orbitEntries_sl_sk T hk hkn hln hka hAl).1
  have nTA : T ≠ A := ne_of_entry_ne (by rw [eT1, eA1]; omega)
  have nTD : T ≠ D := ne_of_entry_ne (by rw [eT1, eD1]; omega)
  have nAD : A ≠ D := ne_of_entry_ne (by rw [eA1, eD1]; omega)
  -- `σ_{k+1}` fixing `T` forces the scalar degeneracy at `r`
  have hscalar : axialDist T (k + 1) = 1 ∨ axialDist T (k + 1) = -1 := by
    rcases axialDist_trichotomy T hkI' hkI'' with h | h | h
    · exact Or.inl h
    · exact Or.inr h
    · exact absurd h hla
  have hdeg : 1 + seminormalParam q (axialDist T (k + 1))
      * seminormalParam q (-axialDist T (k + 1)) = 0 :=
    one_add_seminormalParam_mul_neg_of_scalar q hq0 hq2 hscalar
  have hp0 : axialDist T k ≠ 0 := axialDist_ne_zero T hkI hkI'
  have hr0 : axialDist T (k + 1) ≠ 0 := axialDist_ne_zero T hkI' hkI''
  have hpr0 : axialDist T k + axialDist T (k + 1) ≠ 0 := by
    rw [← dAl]; exact axialDist_ne_zero A hkI' hkI''
  have hprodp := offDiag_mul_neg q hp0
  have hsump := seminormalParam_add_neg q (axialDist T k) hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T k ≠ 0))
  have hsumr := seminormalParam_add_neg q (axialDist T (k + 1)) hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T (k + 1) ≠ 0))
  have hrel := seminormalParam_rel q (axialDist T k) (axialDist T (k + 1)) hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T k ≠ 0))
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T (k + 1) ≠ 0))
    (zpow_ne_one hq0 hq2 (by omega : -2 * (axialDist T k + axialDist T (k + 1)) ≠ 0))
  rw [genMat_mul_apply q k hk hkn (genMat q k hk hkn * genMat q (k + 1) hl hln) hka T',
    genMat_mul_apply_of_not_admissible q (k + 1) hl hln (genMat q k hk hkn) hla T',
    genMat_mul_apply q (k + 1) hl hln (genMat q k hk hkn) hAl T',
    genMat_mul_apply_of_not_admissible q (k + 1) hl hln
      (genMat q (k + 1) hl hln * genMat q k hk hkn) hla T',
    genMat_mul_apply q k hk hkn (genMat q (k + 1) hl hln) hka T', dAl]
  by_cases h1 : T' = T
  · subst h1
    simp only [← hA, ← hD]
    have entA : genMat q k hk hkn T' A = offDiag q (axialDist A k) := by
      have h := genMat_swap q k hk hkn hAk (by rw [bAT]; exact nTA)
      rwa [bAT] at h
    rw [genMat_diag, genMat_diag, entA, dAk,
      genMat_of_not_admissible q k hk hkn nTD hDk,
      genMat_apply_of_ne q (k + 1) hl hln nTA hAl (by rw [← hD]; exact nTD)]
    linear_combination
      (seminormalParam q (axialDist T' (k + 1)) - seminormalParam q (axialDist T' k)) * hrel
        + seminormalParam q (axialDist T' k + axialDist T' (k + 1))
            * seminormalParam q (axialDist T' k) * hsump
        - seminormalParam q (axialDist T' k + axialDist T' (k + 1))
            * seminormalParam q (axialDist T' (k + 1)) * hsumr
        + seminormalParam q (axialDist T' k + axialDist T' (k + 1)) * hdeg
        + seminormalParam q (axialDist T' k + axialDist T' (k + 1)) * hprodp
  by_cases h2 : T' = A
  · subst h2
    simp only [← hA, ← hD]
    have entT : genMat q k hk hkn A T = offDiag q (axialDist T k) :=
      genMat_swap q k hk hkn hka (by rw [← hA]; exact nTA.symm)
    rw [entT, genMat_diag, dAk, genMat_diag, dAl,
      genMat_of_not_admissible q k hk hkn nAD hDk,
      genMat_of_not_admissible q (k + 1) hl hln nTA.symm hla]
    linear_combination
      (-offDiag q (axialDist T k)) * hrel
        + seminormalParam q (axialDist T k + axialDist T (k + 1))
            * offDiag q (axialDist T k) * hsump
  by_cases h3 : T' = D
  · subst h3
    simp only [← hA, ← hD]
    have entA : genMat q (k + 1) hl hln D A = offDiag q (axialDist A (k + 1)) :=
      genMat_swap q (k + 1) hl hln hAl (by rw [← hD]; exact nAD.symm)
    rw [genMat_apply_of_ne q k hk hkn nTD.symm hka (by rw [← hA]; exact nAD.symm),
      genMat_apply_of_ne q k hk hkn nAD.symm hAk (by rw [bAT]; exact nTD.symm),
      genMat_diag, dDk, entA, dAl,
      genMat_of_not_admissible q (k + 1) hl hln nTD.symm hla]
    ring
  · rw [genMat_apply_of_ne q k hk hkn h1 hka (by rw [← hA]; exact h2),
      genMat_apply_of_ne q k hk hkn h2 hAk (by rw [bAT]; exact h1),
      genMat_of_not_admissible q k hk hkn h3 hDk,
      genMat_of_not_admissible q (k + 1) hl hln h1 hla,
      genMat_apply_of_ne q (k + 1) hl hln h2 hAl (by rw [← hD]; exact h3)]
    ring

/-- **Size-`3` orbit, `T` in the middle.**  Both generators move `T`, but neither `s_k·T` nor
`s_{k+1}·T` extends further, so the orbit is `{s_{k+1}·T, T, s_k·T}` and stops.

This is the position that shares its leading flags with a generic size-`6` orbit, and it is
also the one that needs **no deletion at all**: its three rows are `braid_diag_identity`,
`braid_rowA_identity` and `braid_rowB_identity` *unchanged*.

That is worth stating because it inverts the expectation set by the smaller orbits.  Sizes
`1` and `2` were the generic identity with terms removed, licensed by scalar degeneracy;
here nothing is removed and no degeneracy is used — neither generator fixes `T`, so no
distance is `±1`.  The orbit is smaller than generic purely because the two length-`2` words
fail to exist, and the rows that *do* exist are the generic ones. -/
theorem genMat_braid_of_middle (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (k : ℕ) (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hl : 1 ≤ k + 1) (hln : k + 1 + 1 ≤ μ.cells.card)
    {T : StandardYoungTableau μ}
    (hka : SwapAdmissible T k) (hla : SwapAdmissible T (k + 1))
    (hAl : ¬ SwapAdmissible (swapTableau T k hk hkn hka) (k + 1))
    (hBk : ¬ SwapAdmissible (swapTableau T (k + 1) hl hln hla) k)
    (T' : StandardYoungTableau μ) :
    (genMat q k hk hkn * genMat q (k + 1) hl hln * genMat q k hk hkn) T' T
      = (genMat q (k + 1) hl hln * genMat q k hk hkn * genMat q (k + 1) hl hln) T' T := by
  classical
  have hkI : k ∈ Set.Icc 1 μ.cells.card := ⟨hk, by omega⟩
  have hkI' : k + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hkn⟩
  have hkI'' : k + 1 + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hln⟩
  set A := swapTableau T k hk hkn hka with hA
  set B := swapTableau T (k + 1) hl hln hla with hB
  have hAk : SwapAdmissible A k := swapAdmissible_swapTableau T hk hkn hka
  have hBl : SwapAdmissible B (k + 1) := swapAdmissible_swapTableau T hl hln hla
  have bAT : swapTableau A k hk hkn hAk = T := swapTableau_involutive T hk hkn hka
  have bBT : swapTableau B (k + 1) hl hln hBl = T := swapTableau_involutive T hl hln hla
  have dAk : axialDist A k = -axialDist T k := axialDist_swapTableau T hk hkn hka
  have dBl : axialDist B (k + 1) = -axialDist T (k + 1) := axialDist_swapTableau T hl hln hla
  have dAl : axialDist A (k + 1) = axialDist T k + axialDist T (k + 1) :=
    axialDist_succ_swapTableau T hk hkn (by omega) hka
  have dBk : axialDist B k = axialDist T k + axialDist T (k + 1) :=
    axialDist_swapTableau_succ T hk (by omega) hla
  have eT1 : T.entry (cellOf T k).1 (cellOf T k).2 = k := entry_cellOf T hkI
  have eT2 : T.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 = k + 1 := entry_cellOf T hkI'
  have eA1 : A.entry (cellOf T k).1 (cellOf T k).2 = k + 1 := (orbitEntries_sk T hk hkn hka).1
  have eB1 : B.entry (cellOf T k).1 (cellOf T k).2 = k := (orbitEntries_sl T hk hln hla).1
  have eB2 : B.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 = k + 2 :=
    (orbitEntries_sl T hk hln hla).2
  have nTA : T ≠ A := ne_of_entry_ne (by rw [eT1, eA1]; omega)
  have nTB : T ≠ B := ne_of_entry_ne (by rw [eT2, eB2]; omega)
  have nAB : A ≠ B := ne_of_entry_ne (by rw [eA1, eB1]; omega)
  have hp0 : axialDist T k ≠ 0 := axialDist_ne_zero T hkI hkI'
  have hr0 : axialDist T (k + 1) ≠ 0 := axialDist_ne_zero T hkI' hkI''
  have hpr0 : axialDist T k + axialDist T (k + 1) ≠ 0 := by
    rw [← dAl]; exact axialDist_ne_zero A hkI' hkI''
  have hprodp := offDiag_mul_neg q hp0
  have hprodr := offDiag_mul_neg q hr0
  have hsump := seminormalParam_add_neg q (axialDist T k) hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T k ≠ 0))
  have hsumr := seminormalParam_add_neg q (axialDist T (k + 1)) hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T (k + 1) ≠ 0))
  have hrel := seminormalParam_rel q (axialDist T k) (axialDist T (k + 1)) hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T k ≠ 0))
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T (k + 1) ≠ 0))
    (zpow_ne_one hq0 hq2 (by omega : -2 * (axialDist T k + axialDist T (k + 1)) ≠ 0))
  rw [genMat_mul_apply q k hk hkn (genMat q k hk hkn * genMat q (k + 1) hl hln) hka T',
    genMat_mul_apply q (k + 1) hl hln (genMat q k hk hkn) hla T',
    genMat_mul_apply_of_not_admissible q (k + 1) hl hln (genMat q k hk hkn) hAl T',
    genMat_mul_apply q (k + 1) hl hln
      (genMat q (k + 1) hl hln * genMat q k hk hkn) hla T',
    genMat_mul_apply q k hk hkn (genMat q (k + 1) hl hln) hka T',
    genMat_mul_apply_of_not_admissible q k hk hkn (genMat q (k + 1) hl hln) hBk T',
    dAl, dBk]
  by_cases h1 : T' = T
  · subst h1
    simp only [← hA, ← hB]
    have entA : genMat q k hk hkn T' A = offDiag q (axialDist A k) := by
      have h := genMat_swap q k hk hkn hAk (by rw [bAT]; exact nTA)
      rwa [bAT] at h
    have entB : genMat q (k + 1) hl hln T' B = offDiag q (axialDist B (k + 1)) := by
      have h := genMat_swap q (k + 1) hl hln hBl (by rw [bBT]; exact nTB)
      rwa [bBT] at h
    rw [genMat_diag, genMat_diag, entA, entB, dAk, dBl,
      genMat_of_not_admissible q k hk hkn nTB hBk,
      genMat_of_not_admissible q (k + 1) hl hln nTA hAl]
    linear_combination
      (seminormalParam q (axialDist T' (k + 1)) - seminormalParam q (axialDist T' k)) * hrel
        + seminormalParam q (axialDist T' k + axialDist T' (k + 1))
            * seminormalParam q (axialDist T' k) * hsump
        - seminormalParam q (axialDist T' k + axialDist T' (k + 1))
            * seminormalParam q (axialDist T' (k + 1)) * hsumr
        + seminormalParam q (axialDist T' k + axialDist T' (k + 1)) * hprodp
        - seminormalParam q (axialDist T' k + axialDist T' (k + 1)) * hprodr
  by_cases h2 : T' = A
  · subst h2
    simp only [← hA, ← hB]
    have entT : genMat q k hk hkn A T = offDiag q (axialDist T k) :=
      genMat_swap q k hk hkn hka (by rw [← hA]; exact nTA.symm)
    rw [entT, genMat_diag, dAk, genMat_diag, dAl,
      genMat_of_not_admissible q k hk hkn nAB hBk,
      genMat_apply_of_ne q (k + 1) hl hln nTA.symm hla (by rw [← hB]; exact nAB),
      genMat_apply_of_ne q (k + 1) hl hln nAB hBl (by rw [bBT]; exact nTA.symm)]
    linear_combination
      (-offDiag q (axialDist T k)) * hrel
        + seminormalParam q (axialDist T k + axialDist T (k + 1))
            * offDiag q (axialDist T k) * hsump
  by_cases h3 : T' = B
  · subst h3
    simp only [← hA, ← hB]
    have entT : genMat q (k + 1) hl hln B T = offDiag q (axialDist T (k + 1)) :=
      genMat_swap q (k + 1) hl hln hla (by rw [← hB]; exact nTB.symm)
    rw [genMat_apply_of_ne q k hk hkn nTB.symm hka (by rw [← hA]; exact nAB.symm),
      genMat_diag, dBk,
      genMat_apply_of_ne q k hk hkn nAB.symm hAk (by rw [bAT]; exact nTB.symm),
      entT, genMat_of_not_admissible q (k + 1) hl hln nAB.symm hAl,
      genMat_diag, dBl]
    linear_combination
      offDiag q (axialDist T (k + 1)) * hrel
        - seminormalParam q (axialDist T k + axialDist T (k + 1))
            * offDiag q (axialDist T (k + 1)) * hsumr
  · rw [genMat_apply_of_ne q k hk hkn h1 hka (by rw [← hA]; exact h2),
      genMat_of_not_admissible q k hk hkn h3 hBk,
      genMat_apply_of_ne q k hk hkn h2 hAk (by rw [bAT]; exact h1),
      genMat_apply_of_ne q (k + 1) hl hln h1 hla (by rw [← hB]; exact h3),
      genMat_of_not_admissible q (k + 1) hl hln h2 hAl,
      genMat_apply_of_ne q (k + 1) hl hln h3 hBl (by rw [bBT]; exact h1)]
    ring

/-- **Size-`3` orbit, `T` at the `σ_k`-fixed end.**  `σ_{k+1}` moves `T`, `σ_k` fixes it, but
`s_{k+1}·T` *is* `k`-admissible, so the orbit runs `T → s_{k+1}·T → s_k s_{k+1}·T` and stops.

The mirror of `genMat_braid_of_succ_fixed_three`, and — consistent with the rule that
deletion tracks which columns are scalar — it deletes on the **left** where that one deleted
on the right, with the degeneracy at `p = ±1` rather than `r = ±1`.  The third row again
closes by `ring`, this time via `axialDist_swapTableau_word_right`. -/
theorem genMat_braid_of_fixed_succ_three (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (k : ℕ) (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hl : 1 ≤ k + 1) (hln : k + 1 + 1 ≤ μ.cells.card)
    {T : StandardYoungTableau μ}
    (hka : ¬ SwapAdmissible T k) (hla : SwapAdmissible T (k + 1))
    (hBk : SwapAdmissible (swapTableau T (k + 1) hl hln hla) k)
    (hEl : ¬ SwapAdmissible
      (swapTableau (swapTableau T (k + 1) hl hln hla) k hk hkn hBk) (k + 1))
    (T' : StandardYoungTableau μ) :
    (genMat q k hk hkn * genMat q (k + 1) hl hln * genMat q k hk hkn) T' T
      = (genMat q (k + 1) hl hln * genMat q k hk hkn * genMat q (k + 1) hl hln) T' T := by
  classical
  have hkI : k ∈ Set.Icc 1 μ.cells.card := ⟨hk, by omega⟩
  have hkI' : k + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hkn⟩
  have hkI'' : k + 1 + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hln⟩
  set B := swapTableau T (k + 1) hl hln hla with hB
  set E := swapTableau B k hk hkn hBk with hE
  have hBl : SwapAdmissible B (k + 1) := swapAdmissible_swapTableau T hl hln hla
  have hEk : SwapAdmissible E k := swapAdmissible_swapTableau B hk hkn hBk
  have bBT : swapTableau B (k + 1) hl hln hBl = T := swapTableau_involutive T hl hln hla
  have bEB : swapTableau E k hk hkn hEk = B := swapTableau_involutive B hk hkn hBk
  have dBl : axialDist B (k + 1) = -axialDist T (k + 1) := axialDist_swapTableau T hl hln hla
  have dBk : axialDist B k = axialDist T k + axialDist T (k + 1) :=
    axialDist_swapTableau_succ T hk (by omega) hla
  have dEl : axialDist E (k + 1) = axialDist T k :=
    axialDist_swapTableau_word_right T hk (by omega) hla hBk
  have eT1 : T.entry (cellOf T k).1 (cellOf T k).2 = k := entry_cellOf T hkI
  have eT2 : T.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 = k + 1 := entry_cellOf T hkI'
  have eB1 : B.entry (cellOf T k).1 (cellOf T k).2 = k := (orbitEntries_sl T hk hln hla).1
  have eB2 : B.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 = k + 2 :=
    (orbitEntries_sl T hk hln hla).2
  have eE1 : E.entry (cellOf T k).1 (cellOf T k).2 = k + 1 :=
    (orbitEntries_sk_sl T hk hkn hln hla hBk).1
  have nTB : T ≠ B := ne_of_entry_ne (by rw [eT2, eB2]; omega)
  have nTE : T ≠ E := ne_of_entry_ne (by rw [eT1, eE1]; omega)
  have nBE : B ≠ E := ne_of_entry_ne (by rw [eB1, eE1]; omega)
  -- `σ_k` fixes `T`, so the degeneracy is at `p`
  have hscalar : axialDist T k = 1 ∨ axialDist T k = -1 := by
    rcases axialDist_trichotomy T hkI hkI' with h | h | h
    · exact Or.inl h
    · exact Or.inr h
    · exact absurd h hka
  have hdegp : 1 + seminormalParam q (axialDist T k)
      * seminormalParam q (-axialDist T k) = 0 :=
    one_add_seminormalParam_mul_neg_of_scalar q hq0 hq2 hscalar
  have hp0 : axialDist T k ≠ 0 := axialDist_ne_zero T hkI hkI'
  have hr0 : axialDist T (k + 1) ≠ 0 := axialDist_ne_zero T hkI' hkI''
  have hpr0 : axialDist T k + axialDist T (k + 1) ≠ 0 := by
    rw [← dBk]; exact axialDist_ne_zero B hkI hkI'
  have hprodr := offDiag_mul_neg q hr0
  have hsump := seminormalParam_add_neg q (axialDist T k) hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T k ≠ 0))
  have hsumr := seminormalParam_add_neg q (axialDist T (k + 1)) hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T (k + 1) ≠ 0))
  have hrel := seminormalParam_rel q (axialDist T k) (axialDist T (k + 1)) hq0
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T k ≠ 0))
    (zpow_ne_one hq0 hq2 (by omega : -2 * axialDist T (k + 1) ≠ 0))
    (zpow_ne_one hq0 hq2 (by omega : -2 * (axialDist T k + axialDist T (k + 1)) ≠ 0))
  rw [genMat_mul_apply_of_not_admissible q k hk hkn
      (genMat q k hk hkn * genMat q (k + 1) hl hln) hka T',
    genMat_mul_apply q (k + 1) hl hln (genMat q k hk hkn) hla T',
    genMat_mul_apply q (k + 1) hl hln
      (genMat q (k + 1) hl hln * genMat q k hk hkn) hla T',
    genMat_mul_apply_of_not_admissible q k hk hkn (genMat q (k + 1) hl hln) hka T',
    genMat_mul_apply q k hk hkn (genMat q (k + 1) hl hln) hBk T', dBk]
  by_cases h1 : T' = T
  · subst h1
    simp only [← hB, ← hE]
    have entB : genMat q (k + 1) hl hln T' B = offDiag q (axialDist B (k + 1)) := by
      have h := genMat_swap q (k + 1) hl hln hBl (by rw [bBT]; exact nTB)
      rwa [bBT] at h
    rw [genMat_diag, genMat_diag, entB, dBl,
      genMat_apply_of_ne q k hk hkn nTB hBk (by rw [← hE]; exact nTE),
      genMat_of_not_admissible q (k + 1) hl hln nTE hEl]
    linear_combination
      (seminormalParam q (axialDist T' (k + 1)) - seminormalParam q (axialDist T' k)) * hrel
        + seminormalParam q (axialDist T' k + axialDist T' (k + 1))
            * seminormalParam q (axialDist T' k) * hsump
        - seminormalParam q (axialDist T' k + axialDist T' (k + 1))
            * seminormalParam q (axialDist T' (k + 1)) * hsumr
        - seminormalParam q (axialDist T' k + axialDist T' (k + 1)) * hdegp
        - seminormalParam q (axialDist T' k + axialDist T' (k + 1)) * hprodr
  by_cases h2 : T' = B
  · subst h2
    simp only [← hB, ← hE]
    have entT : genMat q (k + 1) hl hln B T = offDiag q (axialDist T (k + 1)) :=
      genMat_swap q (k + 1) hl hln hla (by rw [← hB]; exact nTB.symm)
    rw [genMat_of_not_admissible q k hk hkn nTB.symm hka,
      genMat_diag, dBk, entT, genMat_diag, dBl,
      genMat_of_not_admissible q (k + 1) hl hln nBE hEl]
    linear_combination
      offDiag q (axialDist T (k + 1)) * hrel
        - seminormalParam q (axialDist T k + axialDist T (k + 1))
            * offDiag q (axialDist T (k + 1)) * hsumr
  by_cases h3 : T' = E
  · subst h3
    simp only [← hB, ← hE]
    have entB : genMat q k hk hkn E B = offDiag q (axialDist B k) :=
      genMat_swap q k hk hkn hBk (by rw [← hE]; exact nBE.symm)
    rw [genMat_of_not_admissible q k hk hkn nTE.symm hka, entB, dBk,
      genMat_apply_of_ne q (k + 1) hl hln nTE.symm hla (by rw [← hB]; exact nBE.symm),
      genMat_apply_of_ne q (k + 1) hl hln nBE.symm hBl (by rw [bBT]; exact nTE.symm),
      genMat_diag, dEl]
    ring
  · rw [genMat_of_not_admissible q k hk hkn h1 hka,
      genMat_apply_of_ne q k hk hkn h2 hBk (by rw [← hE]; exact h3),
      genMat_apply_of_ne q (k + 1) hl hln h1 hla (by rw [← hB]; exact h2),
      genMat_apply_of_ne q (k + 1) hl hln h2 hBl (by rw [bBT]; exact h1),
      genMat_of_not_admissible q (k + 1) hl hln h3 hEl]
    ring

/-- **The braid relation, unconditionally.**

`ρ(σ_k)ρ(σ_{k+1})ρ(σ_k) = ρ(σ_{k+1})ρ(σ_k)ρ(σ_{k+1})` on all of `SYT μ`, arbitrary shape, no
hypothesis on the orbit.

The proof dispatches on three flags — does `σ_k` move `T`, does `σ_{k+1}`, does `σ_{k+1}`
move `s_k·T` — to the seven shape theorems.  Every remaining hypothesis those theorems ask
for is *derived* rather than assumed, via the classification iffs: `hBk` from `hAl`
(`swapAdmissible_cross_iff` — they are the same condition on the cells of `k` and `k+2`), and
the two length-`2` admissibilities from `T`'s own (`swapAdmissible_word_left_iff` /
`_right_iff`).

With `genMat_quadratic` and `genMat_far_comm`, this completes the three Hecke relations
unconditionally. -/
theorem genMat_braid (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (k : ℕ) (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hl : 1 ≤ k + 1) (hln : k + 1 + 1 ≤ μ.cells.card) :
    genMat q k hk hkn * genMat q (k + 1) hl hln * genMat q k hk hkn
      = genMat q (k + 1) hl hln * genMat q k hk hkn * genMat q (k + 1) hl hln := by
  classical
  ext T' T
  by_cases hka : SwapAdmissible T k
  · by_cases hla : SwapAdmissible T (k + 1)
    · by_cases hAl : SwapAdmissible (swapTableau T k hk hkn hka) (k + 1)
      · -- generic: the other three admissibilities are all derived
        have hBk := (swapAdmissible_cross_iff T hk hkn hln hka hla).mp hAl
        have hDk := (swapAdmissible_word_left_iff T hk hkn hln hka hAl).mpr hla
        have hEl := (swapAdmissible_word_right_iff T hk hkn hln hla hBk).mpr hka
        exact genMat_braid_generic q hq0 hq2 k hk hkn hl hln hka hla hAl hBk hDk hEl T'
      · -- `s_k·T` does not extend, hence neither does `s_{k+1}·T`: the middle position
        have hBk : ¬ SwapAdmissible (swapTableau T (k + 1) hl hln hla) k := fun h =>
          hAl ((swapAdmissible_cross_iff T hk hkn hln hka hla).mpr h)
        exact genMat_braid_of_middle q hq0 hq2 k hk hkn hl hln hka hla hAl hBk T'
    · by_cases hAl : SwapAdmissible (swapTableau T k hk hkn hka) (k + 1)
      · have hDk : ¬ SwapAdmissible
            (swapTableau (swapTableau T k hk hkn hka) (k + 1) hl hln hAl) k := fun h =>
          hla ((swapAdmissible_word_left_iff T hk hkn hln hka hAl).mp h)
        exact genMat_braid_of_succ_fixed_three q hq0 hq2 k hk hkn hl hln hka hla hAl hDk T'
      · exact genMat_braid_of_succ_fixed q hq0 hq2 k hk hkn hl hln hka hla hAl T'
  · by_cases hla : SwapAdmissible T (k + 1)
    · by_cases hBk : SwapAdmissible (swapTableau T (k + 1) hl hln hla) k
      · have hEl : ¬ SwapAdmissible
            (swapTableau (swapTableau T (k + 1) hl hln hla) k hk hkn hBk) (k + 1) := fun h =>
          hka ((swapAdmissible_word_right_iff T hk hkn hln hla hBk).mp h)
        exact genMat_braid_of_fixed_succ_three q hq0 hq2 k hk hkn hl hln hka hla hBk hEl T'
      · exact genMat_braid_of_fixed_succ q hq0 hq2 k hk hkn hl hln hka hla hBk T'
    · exact genMat_braid_of_both_fixed q k hk hkn hl hln hka hla T'

end Braid

/-! ## Packaging: the representation as an algebra map

The three relations are exactly `Hecke.lift`'s three obligations, so the seminormal
representation of `H_{n+1}(q)` on `SYT μ` follows once the indexing is translated: generators
here are `k : ℕ` with `1 ≤ k` and `k + 1 ≤ |μ|`, generators there are `i : Fin n`, and the
correspondence is `k = i + 1` with `|μ| = n + 1`.
-/

section Package

/-- The generator matrices re-indexed for `Hecke.lift`: `σ_i ↦ ρ(σ_{i+1})`. -/
noncomputable def seminormalGen (n : ℕ) (hN : μ.cells.card = n + 1) (i : Fin n) :
    Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ :=
  genMat q ((i : ℕ) + 1) (by omega) (by have := i.isLt; omega)

/-- **The general-`λ` Hoefsmit seminormal representation.**

`H_{n+1}(q) →ₐ[ℝ] M_{SYT μ}(ℝ)` for any shape `μ` with `|μ| = n + 1`, built from the three
relations proved above through the universal property `Hecke.lift`.  Its dimension is
`#SYT μ`, the Specht dimension of `μ`. -/
noncomputable def seminormalRep (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hN : μ.cells.card = n + 1) :
    Hecke ℝ q q⁻¹ n →ₐ[ℝ] Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ :=
  Hecke.lift ℝ q q⁻¹ n (seminormalGen q n hN)
    (fun i => by
      rw [mul_inv_cancel₀ hq0, one_smul]
      exact genMat_quadratic q hq0 hq2 _ _ _)
    (fun i hi => by
      have h : (seminormalGen q n hN ⟨(i : ℕ) + 1, hi⟩)
          = genMat q ((i : ℕ) + 1 + 1) (by omega) (by omega) := rfl
      rw [h]
      exact genMat_braid q hq0 hq2 _ _ _ _ _)
    (fun i j hij => by
      refine genMat_far_comm q _ _ _ _ ?_
      have := i.isLt; have := j.isLt
      omega)

/-- `seminormalRep` sends the generator `σ_i` to the matrix `ρ(σ_{i+1})`. -/
@[simp] theorem seminormalRep_σ (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hN : μ.cells.card = n + 1) (i : Fin n) :
    seminormalRep q hq0 hq2 n hN (Hecke.σ ℝ q q⁻¹ n i) = seminormalGen q n hN i :=
  Hecke.lift_σ ℝ q q⁻¹ n _ _ _ _ i

/-- **A generator that moves any tableau is not a scalar matrix.**

Needs no hypothesis on `q` whatever.  The reason is that `offDiag` takes the plain value `1`
on the non-negative branch, so of the two off-diagonal entries `(s_k·T, T)` and `(T, s_k·T)`
— which sit at distances `d` and `-d` — **at least one is exactly `1`**, whichever sign `d`
has.  A scalar matrix has both equal to `0`.

Note this does *not* go through `offDiag ≠ 0` at the moved entry: that can genuinely vanish,
since `offDiag q (-1) = 0`.  It is the *pair* that cannot both vanish. -/
theorem genMat_ne_scalar (k : ℕ) (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card)
    {T : StandardYoungTableau μ} (hadm : SwapAdmissible T k) (s : ℝ) :
    genMat q k hk hkn ≠ s • (1 : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ) := by
  classical
  intro hcon
  have hne : swapTableau T k hk hkn hadm ≠ T := swapTableau_ne T hk hkn hadm
  have hadm' : SwapAdmissible (swapTableau T k hk hkn hadm) k :=
    swapAdmissible_swapTableau T hk hkn hadm
  have hback : swapTableau (swapTableau T k hk hkn hadm) k hk hkn hadm' = T :=
    swapTableau_involutive T hk hkn hadm
  have hd : axialDist (swapTableau T k hk hkn hadm) k = -axialDist T k :=
    axialDist_swapTableau T hk hkn hadm
  -- both off-diagonal entries of a scalar matrix vanish
  have hz : ∀ {U V : StandardYoungTableau μ}, U ≠ V → genMat q k hk hkn U V = 0 := by
    intro U V huv
    rw [hcon]
    simp [Matrix.one_apply, huv]
  by_cases hsign : axialDist T k < 0
  · -- read the partner column instead: its distance is `-d > 0`
    have h1 : genMat q k hk hkn T (swapTableau T k hk hkn hadm)
        = offDiag q (axialDist (swapTableau T k hk hkn hadm) k) := by
      have h := genMat_swap q k hk hkn hadm' (by rw [hback]; exact hne.symm)
      rwa [hback] at h
    rw [hz hne.symm, hd, offDiag_of_not_neg q (by omega)] at h1
    exact one_ne_zero h1.symm
  · have h1 : genMat q k hk hkn (swapTableau T k hk hkn hadm) T
        = offDiag q (axialDist T k) := genMat_swap q k hk hkn hadm hne
    rw [hz hne, offDiag_of_not_neg q hsign] at h1
    exact one_ne_zero h1.symm

end Package

end SeminormalRep

end QOU.SchurWeyl
