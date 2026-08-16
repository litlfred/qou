import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum

/-!
# QOU.BraidKnot.TwoFiltrationBridge — conjectural class (§3b)

**§3b class axiomatisation** for content block
[`conj:two-filtration-bridge`](../../../quantum-observable-universe/mass-theory/two-filtration-bridge.md):
*Two-filtration bridge: iterated-integral depth $\leftrightarrow$
partition-cellular GB-depth via the central idempotents $e_\lambda$.*

This is a **conjecture**: the class carries the conjecture's actual
content as the `bridge` field (the depth-lift dichotomy); the
`noncomputable instance`'s `sorry` represents the open conjecture itself
(per AGENTS.md §3b), NOT a missing proof.

**Mathlib-infra pass (2026-06-25, Tier 1).** Both partition-side objects
are now *real*: the partition index is Mathlib `YoungDiagram` with the
genuine conjugate involution `YoungDiagram.transpose` (self-conjugacy =
`μ.transpose = μ`), and the **partition-cellular GB-depth is the concrete
definition** `gbDepth` = max hook length over cells (built here from the
real `rowLen`/`colLen`/`cells` API) — no longer an abstract `dGB` class
field. Only the QOU-specific iterated-integral depth-lift `dII` and the
chiral-pair predicate remain abstract (the open conjectural content). The
faithful conditional form is
`QOU.AlgebraicSubstrate.TwoFiltrationBridgeGeneral`.
-/

namespace QOU.BraidKnot

open YoungDiagram

/-- **Hook length** of cell `c = (i, j)` in a Young diagram `μ`:
    arm `(rowLen i - j)` + leg `(colLen j - i)` − 1. For a cell of `μ`
    this is `≥ 1` (truncated ℕ subtraction is exact there). -/
def TwoFiltrationBridge.hookLength (μ : YoungDiagram) (c : ℕ × ℕ) : ℕ :=
  (μ.rowLen c.1 - c.2) + (μ.colLen c.2 - c.1) - 1

/-- **Partition-cellular GB-depth** $\mathrm{depth}_{\mathrm{GB}}(\lambda)
    = \max_\square h(\square)$: the maximum hook length over all cells
    (the centre $Z(H_n(q))$ side of the bridge). The empty diagram has
    depth `0`. -/
def gbDepth (μ : YoungDiagram) : ℕ :=
  μ.cells.sup fun c => TwoFiltrationBridge.hookLength μ c

/-- **Two-filtration bridge** (iterated-integral depth $\leftrightarrow$
    partition-cellular GB-depth via $e_\lambda$).

    Conjectural class — see
    [`conj:two-filtration-bridge`](../../../quantum-observable-universe/mass-theory/two-filtration-bridge.md). -/
class TwoFiltrationBridge where
  /-- Iterated-integral depth-lift $d_{\mathrm{II}}(\lambda)$ of the
      central idempotent $e_\lambda$ (the grouplike side). -/
  dII : YoungDiagram → ℕ
  /-- Predicate selecting the depth-3 chiral-pair period family. -/
  isChiralPair : YoungDiagram → Prop
  /-- **The conjecture** (depth-lift dichotomy, from the manuscript):
      a self-conjugate cell ($\mu^\top = \mu$) lifts to depth $2$ (real /
      Bloch–Wigner period), a chiral pair to depth $3$ (Tate-twisted
      period), and every other cell's lift is bounded by its concrete
      GB-depth `gbDepth μ` (max hook length). -/
  bridge : ∀ μ : YoungDiagram,
    (μ.transpose = μ → dII μ = 2) ∧
    (isChiralPair μ → dII μ = 3) ∧
    (μ.transpose ≠ μ → ¬ isChiralPair μ → dII μ ≤ gbDepth μ)

-- The conjecture itself.  The `sorry` represents the **open
-- conjecture** per §3b — not a missing proof.
-- Ref: [manuscript] quantum-observable-universe/mass-theory/two-filtration-bridge.ts

-- **No instance is provided — the honest open state** (AGENTS.md §3b-tax).
-- Previously: `axiom twoFiltrationBridge_conjecture` plus a global instance discharging `TwoFiltrationBridge` with it.
-- Consumers already declare `[TwoFiltrationBridge]`, so the global instance was silently
-- satisfying a hypothesis they had correctly written down.  Removed.

/-! ### What `gbDepth` actually grades — bean `wpdb`

`prf:phi-q-categorical-truncation` Step 3 and two sibling blocks use
`Z^(k)(A) = span{eλ : gbDepth λ = k}` as the centre's depth grading, citing
`prop:curvature-rank-gb-stratification` — which stratifies by the curvature
rank of **words** and mentions no partition. That bridge is stated nowhere
(audit: `docs/audits/2026-08-16-word-depth-vs-partition-depth-bridge-is-unstated.md`).

This section does not close it. It measures the **partition side**, and what
it finds bears directly on the downstream use: the grading is far coarser than
its notation suggests, and at the strand count where the framework actually
consumes it, it is trivial.
-/

/-- **The GB-depth is the corner hook**, `λ₁ + λ'₁ - 1`.

The maximum over all cells is attained at `(0,0)`: rows and columns are
antitone, so every cell's arm and leg are dominated by the corner's. -/
theorem gbDepth_eq_corner (μ : YoungDiagram) (h : μ.cells.Nonempty) :
    gbDepth μ = μ.rowLen 0 + μ.colLen 0 - 1 := by
  apply le_antisymm
  · refine Finset.sup_le fun c _ => ?_
    unfold TwoFiltrationBridge.hookLength
    have h1 : μ.rowLen c.1 - c.2 ≤ μ.rowLen 0 :=
      (Nat.sub_le _ _).trans (rowLen_anti μ 0 c.1 (Nat.zero_le _))
    have h2 : μ.colLen c.2 - c.1 ≤ μ.colLen 0 :=
      (Nat.sub_le _ _).trans (colLen_anti μ 0 c.2 (Nat.zero_le _))
    omega
  · obtain ⟨c, hc⟩ := h
    have hmem : ((0 : ℕ), (0 : ℕ)) ∈ μ.cells :=
      μ.up_left_mem (Nat.zero_le _) (Nat.zero_le _) hc
    simpa [TwoFiltrationBridge.hookLength] using
      Finset.le_sup (f := fun c => TwoFiltrationBridge.hookLength μ c) hmem

/-- **The grading is blind to the interior.** Two diagrams sharing a first row
and a first column have the same GB-depth however differently they are shaped
below and to the right of the corner — an immediate consequence of
`gbDepth_eq_corner`, and the reason the stratification is coarse. -/
theorem gbDepth_eq_of_border_eq (μ ν : YoungDiagram)
    (hμ : μ.cells.Nonempty) (hν : ν.cells.Nonempty)
    (hrow : μ.rowLen 0 = ν.rowLen 0) (hcol : μ.colLen 0 = ν.colLen 0) :
    gbDepth μ = gbDepth ν := by
  rw [gbDepth_eq_corner μ hμ, gbDepth_eq_corner ν hν, hrow, hcol]

/-- A diagram that is not a hook — one containing `(1,1)` — has at least four
cells. So every partition of `n ≤ 3` is a hook, which is what makes the
`H₃` computation below come out constant. -/
theorem four_le_card_of_mem_one_one (μ : YoungDiagram) (h : (1, 1) ∈ μ) :
    4 ≤ μ.cells.card := by
  have h00 : ((0 : ℕ), (0 : ℕ)) ∈ μ.cells := μ.up_left_mem (by omega) (by omega) h
  have h01 : ((0 : ℕ), (1 : ℕ)) ∈ μ.cells := μ.up_left_mem (by omega) (by omega) h
  have h10 : ((1 : ℕ), (0 : ℕ)) ∈ μ.cells := μ.up_left_mem (by omega) (by omega) h
  have hsub : ({(0,0), (0,1), (1,0), (1,1)} : Finset (ℕ × ℕ)) ⊆ μ.cells := by
    intro x hx
    fin_cases hx <;> assumption
  calc (4 : ℕ) = ({(0,0), (0,1), (1,0), (1,1)} : Finset (ℕ × ℕ)).card := by decide
    _ ≤ μ.cells.card := Finset.card_le_card hsub

section H3

private theorem colLen_ofRowLens {w : List ℕ} (hw : List.Sorted (· ≥ ·) w)
    (hpos : ∀ x ∈ w, 0 < x) : (ofRowLens w hw).colLen 0 = w.length := by
  rw [← length_rowLens, rowLens_ofRowLens_eq_self hpos]

private theorem rowLen_ofRowLens {w : List ℕ} (hw : List.Sorted (· ≥ ·) w)
    (hpos : ∀ x ∈ w, 0 < x) (h : 0 < w.length) :
    (ofRowLens w hw).rowLen 0 = w[0]'h := by
  have hl : (0 : ℕ) < (ofRowLens w hw).rowLens.length := by
    rw [rowLens_ofRowLens_eq_self hpos]; exact h
  have := @get_rowLens (ofRowLens w hw) 0 hl
  rw [← this]
  simp [rowLens_ofRowLens_eq_self hpos]

private theorem cells_ne {w : List ℕ} (hw : List.Sorted (· ≥ ·) w)
    (hpos : ∀ x ∈ w, 0 < x) (h : 0 < w.length) :
    (ofRowLens w hw).cells.Nonempty := by
  refine ⟨(0, 0), ?_⟩
  have : (ofRowLens w hw).colLen 0 = w.length := colLen_ofRowLens hw hpos
  have hcol : 0 < (ofRowLens w hw).colLen 0 := by omega
  simpa using (mem_iff_lt_colLen).mpr hcol

/-- The three partitions of `3` — the `H₃` Wedderburn blocks of a single
nucleon (`schur-weyl-mass-decomposition`: symmetric, standard, antisymmetric). -/
def p3 : YoungDiagram := ofRowLens [3] (by decide)
def p21 : YoungDiagram := ofRowLens [2, 1] (by decide)
def p111 : YoungDiagram := ofRowLens [1, 1, 1] (by decide)

theorem gbDepth_p3 : gbDepth p3 = 3 := by
  rw [p3, gbDepth_eq_corner _ (cells_ne _ (by decide) (by decide)),
      rowLen_ofRowLens _ (by decide) (by decide), colLen_ofRowLens _ (by decide)]
  decide

theorem gbDepth_p21 : gbDepth p21 = 3 := by
  rw [p21, gbDepth_eq_corner _ (cells_ne _ (by decide) (by decide)),
      rowLen_ofRowLens _ (by decide) (by decide), colLen_ofRowLens _ (by decide)]
  decide

theorem gbDepth_p111 : gbDepth p111 = 3 := by
  rw [p111, gbDepth_eq_corner _ (cells_ne _ (by decide) (by decide)),
      rowLen_ofRowLens _ (by decide) (by decide), colLen_ofRowLens _ (by decide)]
  decide

/-- **At `n = 3` the partition grading has exactly one stratum.**

All three `H₃` blocks have GB-depth `3`, so `Z(H₃) = Z^(3)` and every other
stratum is zero.

The downstream consequence is the point. `prop:phi-q-categorical-truncation`
sets `k⋆(T_w) := max {gbDepth λ : λ ∈ supp(T_w)}` and states that the
truncation depth is *"structurally locked to the NF support of `T_w`"*. At
`n = 3` that maximum is `3` for **every** `T_w` with nonempty support — it is
constant, so it locks onto nothing. Whatever the truncation claim is worth at
the single-nucleon level, it is not carried by the support.

Scope-(a): this says the grading is degenerate here, not that the truncation
is false. It becomes non-trivial from `n = 4`, where `(2,2)` has depth `3`
against `4` for the four hooks. -/
theorem gbDepth_const_on_H3 :
    gbDepth p3 = gbDepth p21 ∧ gbDepth p21 = gbDepth p111 :=
  ⟨by rw [gbDepth_p3, gbDepth_p21], by rw [gbDepth_p21, gbDepth_p111]⟩

end H3

end QOU.BraidKnot
