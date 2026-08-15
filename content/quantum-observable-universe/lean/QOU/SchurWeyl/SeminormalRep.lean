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

## Scope

This is the **definition** and its entry rules.  The Hecke relations for `genMat` — the
quadratic, far commutation, and the braid — are *not* proved here; they are what route (c)
buys the chance to prove globally, and they remain open under bean `qou-gjg6`.
`hoefsmit_seminormal_rep` keeps its `-- Ref:`-cited `sorry`.

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

end SeminormalRep

end QOU.SchurWeyl
