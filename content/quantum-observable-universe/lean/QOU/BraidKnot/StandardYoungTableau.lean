import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.SetTheory.Cardinal.Finite
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.BraidKnot.StandardYoungTableau — brick 1 of the Identity-I S_n rep-theory program

First brick of the multi-session program scoped in
[`docs/scope/2026-06-24-identity-i-plancherel-snrep-infra-program.md`]: the
standard-Young-tableau count `numSYT μ = #SYT(μ)` and its Frame–Robinson–Thrall
hook-length value — the "dimension side" `dim(λ) = f^λ` that program phase **P2**
needs for axiom (i) `Σ_λ dim(λ)² = n!`.

Pinned Mathlib (rev `f897ebcf`) ships `YoungDiagram` and a semistandard-tableau
type but **not** `StandardYoungTableau`, the SYT count, or the hook-length
dimension (verified against the cached oleans). This file supplies the missing
definitions over `ℕ` (nothing archimedean — §7c) and *states* the FRT identity.
Its proof is the genuine formalisation target (a textbook-famous theorem) and is
left as `sorry` + `-- Ref:` per AGENTS.md §1.

**Program seed.** This file is intentionally not yet imported by the
`QOU.BraidKnot` umbrella: the Identity-I program's integration phase (**P5**)
wires the tower once the rep-theory bricks (P1/P3, which need
`Mathlib.RepresentationTheory`) land in a build-capable environment. It is
verified to compile standalone via `lean`-direct against the cached v4.24.0
oleans.

## References
- [sagan2001] Sagan, *The Symmetric Group*, §3.10 (the hook-length formula).
-/

namespace QOU.BraidKnot

/-- A **standard Young tableau** of shape `μ`: a filling of the cells of `μ` by the
integers `0, …, |μ| − 1`, each used once, strictly increasing along rows
(left → right) and down columns (top → bottom). Entries are carried by
`entry : ℕ → ℕ → ℕ`, constrained on the cells `(i, j) ∈ μ` and pinned to `0` off the
diagram (`zero_off`) so the type is **finite** — an SYT is fully determined by its
values on the finitely many cells of `μ` — which is what makes `numSYT` via
`Nat.card` well-defined (without `zero_off` the entry field would be free off-cells,
the type infinite, and `Nat.card` would collapse to `0`). Surjectivity onto
`{0, …, |μ| − 1}` is *omitted*: it is forced by `inj_on` together with
`μ.cells.card = μ.card`, so stating it would be redundant. -/
structure StandardYoungTableau (μ : YoungDiagram) where
  /-- The entry at cell `(i, j)`. -/
  entry : ℕ → ℕ → ℕ
  /-- Entries lie in `{0, …, |μ| − 1}`. -/
  lt_card : ∀ i j, (i, j) ∈ μ → entry i j < μ.card
  /-- Off the diagram the filling is pinned to `0`, so the structure is finite (an
  SYT is determined by its values on the finitely many cells of `μ`). -/
  zero_off : ∀ i j, (i, j) ∉ μ → entry i j = 0
  /-- Distinct cells carry distinct entries. -/
  inj_on : ∀ i j i' j', (i, j) ∈ μ → (i', j') ∈ μ → entry i j = entry i' j' → i = i' ∧ j = j'
  /-- Entries strictly increase along each row. -/
  row_strict : ∀ i j, (i, j + 1) ∈ μ → entry i j < entry i (j + 1)
  /-- Entries strictly increase down each column. -/
  col_strict : ∀ i j, (i + 1, j) ∈ μ → entry i j < entry (i + 1) j

/-- `numSYT μ = #SYT(μ)`, the number of standard Young tableaux of shape `μ`.
This is the dimension `f^μ = dim V_μ` of the irreducible `S_{|μ|}`-representation
indexed by `μ` (program brick 1 / phase P2). Well-defined because
`StandardYoungTableau μ` is finite (the `zero_off` normalisation pins entries off
the diagram, so an SYT is determined by its finitely many on-cell values).
Noncomputable: it counts an unbundled structure via `Nat.card`.

Open brick-1 targets (next session, build-capable env): a `Finite`/`Fintype`
instance for `StandardYoungTableau`, the base case `numSYT ⊥ = 1`, and the FRT
identity `numSYT_mul_hookProduct` below. -/
noncomputable def numSYT (μ : YoungDiagram) : ℕ := Nat.card (StandardYoungTableau μ)

/-- The **hook length** of cell `(i, j)` in `μ`: arm (cells strictly to the right in
row `i`) + leg (cells strictly below in column `j`) + the cell itself. -/
def hookLength (μ : YoungDiagram) (i j : ℕ) : ℕ :=
  (μ.cells.filter (fun c => c.1 = i ∧ j < c.2)).card
    + (μ.cells.filter (fun c => c.2 = j ∧ i < c.1)).card
    + 1

/-- The **hook-length product** `∏_{c ∈ μ} h(c)` appearing in the FRT formula. -/
def hookProduct (μ : YoungDiagram) : ℕ :=
  ∏ c ∈ μ.cells, hookLength μ c.1 c.2

/-- **Frame–Robinson–Thrall hook-length formula** (the brick-1 target):
`#SYT(μ) · ∏_{c ∈ μ} h(c) = |μ|!`, i.e. `f^μ = |μ|! / ∏ h(c)`. Stated here as the
multiplicative (division-free) identity so it lives over `ℕ`; the proof is the
genuine formalisation target of this brick and is deferred. -/
theorem numSYT_mul_hookProduct (μ : YoungDiagram) :
    numSYT μ * hookProduct μ = (μ.card).factorial := by
  -- Ref: [sagan2001] §3.10 (hook-length formula); brick-1 target, see
  -- docs/scope/2026-06-24-identity-i-plancherel-snrep-infra-program.md (P2).
  sorry

end QOU.BraidKnot
