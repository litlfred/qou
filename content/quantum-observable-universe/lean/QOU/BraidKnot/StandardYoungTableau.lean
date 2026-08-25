import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.SetTheory.Cardinal.Finite
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Data.List.GetD

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
@[ext]
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

namespace StandardYoungTableau

variable {μ : YoungDiagram}

/-- Encode a standard tableau by its entries on the cells of `μ`: each on-cell entry lies in
`Fin μ.card` (by `lt_card`), and `zero_off` pins the off-cell entries to `0`, so a tableau is
fully determined by this finite data. This injection into a finite function type witnesses
finiteness of `StandardYoungTableau μ`. -/
def encode (T : StandardYoungTableau μ) : {c : ℕ × ℕ // c ∈ μ.cells} → Fin μ.card :=
  fun c => ⟨T.entry c.1.1 c.1.2, T.lt_card c.1.1 c.1.2 ((YoungDiagram.mem_cells c.1).mp c.2)⟩

theorem encode_injective : Function.Injective (encode : StandardYoungTableau μ → _) := by
  intro T1 T2 h
  ext i j
  by_cases hij : (i, j) ∈ μ
  · have hc : ((i, j) : ℕ × ℕ) ∈ μ.cells := (YoungDiagram.mem_cells (i, j)).mpr hij
    have := congrArg Fin.val (congrFun h ⟨(i, j), hc⟩)
    simpa [encode] using this
  · rw [T1.zero_off i j hij, T2.zero_off i j hij]

/-- `StandardYoungTableau μ` is **finite**: an SYT is determined by its finitely many on-cell
entries (`encode` is injective into `{c // c ∈ μ.cells} → Fin μ.card`). This makes `numSYT`
below (a `Nat.card`) a genuine count, rather than the `0` fallback that `Nat.card` returns on
an infinite type. -/
instance instFinite : Finite (StandardYoungTableau μ) :=
  Finite.of_injective _ encode_injective

end StandardYoungTableau

/-- `numSYT μ = #SYT(μ)`, the number of standard Young tableaux of shape `μ`.
This is the dimension `f^μ = dim V_μ` of the irreducible `S_{|μ|}`-representation
indexed by `μ` (program brick 1 / phase P2). Well-defined because
`StandardYoungTableau μ` is finite (the `zero_off` normalisation pins entries off
the diagram, so an SYT is determined by its finitely many on-cell values).
Noncomputable: it counts an unbundled structure via `Nat.card`, which is a genuine count
here because `StandardYoungTableau.instFinite` (above) proves the type finite.

The brick-1 FRT identity is **proved** downstream as
`QOU.BraidKnot.HookProductHLF.numSYT_mul_hookProduct` (see the note at the end of this
file for why it cannot be stated here). The `Finite` instance and the base case
`numSYT ⊥ = 1` — `numSYT_bot` — are proved here. -/
noncomputable def numSYT (μ : YoungDiagram) : ℕ := Nat.card (StandardYoungTableau μ)

/-- Base case: the empty diagram has a single standard tableau (the empty filling),
so `numSYT ⊥ = 1`. This also confirms the `zero_off` normalisation makes `numSYT`
count correctly — without it the type would be infinite and `Nat.card` would give
`0`, not `1`. -/
theorem numSYT_bot : numSYT (⊥ : YoungDiagram) = 1 := by
  have hempty : ∀ i j : ℕ, (i, j) ∉ (⊥ : YoungDiagram) := fun i j => by simp
  have huniq : Unique (StandardYoungTableau (⊥ : YoungDiagram)) :=
    { default :=
        { entry := fun _ _ => 0
          lt_card := fun i j h => absurd h (hempty i j)
          zero_off := fun _ _ _ => rfl
          inj_on := fun i j _ _ h _ _ => absurd h (hempty i j)
          row_strict := fun i j h => absurd h (hempty i (j + 1))
          col_strict := fun i j h => absurd h (hempty (i + 1) j) }
      uniq := fun t => by
        ext i j
        simp [t.zero_off i j (hempty i j)] }
  haveI := huniq
  rw [numSYT]
  exact Nat.card_unique

/-- The **hook length** of cell `(i, j)` in `μ`: arm (cells strictly to the right in
row `i`) + leg (cells strictly below in column `j`) + the cell itself. -/
def StandardYoungTableau.hookLength (μ : YoungDiagram) (i j : ℕ) : ℕ :=
  (μ.cells.filter (fun c => c.1 = i ∧ j < c.2)).card
    + (μ.cells.filter (fun c => c.2 = j ∧ i < c.1)).card
    + 1

/-- Every hook length is positive: besides its arm and leg it counts the cell itself (`+ 1`). -/
theorem hookLength_pos (μ : YoungDiagram) (i j : ℕ) : 0 < StandardYoungTableau.hookLength μ i j := by
  unfold StandardYoungTableau.hookLength; omega



/-- The **hook-length product** `∏_{c ∈ μ} h(c)` appearing in the FRT formula. -/
def hookProduct (μ : YoungDiagram) : ℕ :=
  ∏ c ∈ μ.cells, StandardYoungTableau.hookLength μ c.1 c.2

/-- The hook-length product is positive (a product of positive hook lengths). This makes the
FRT formula's division form `f^μ = |μ|! / ∏ h_c` well-posed and is what the multiplicative
statement `HookProductHLF.numSYT_mul_hookProduct` is divided through by. -/
theorem hookProduct_pos (μ : YoungDiagram) : 0 < hookProduct μ :=
  Finset.prod_induction _ (0 < ·) (fun _ _ ha hb => Nat.mul_pos ha hb) Nat.one_pos
    (fun c _ => hookLength_pos μ c.1 c.2)






/-! ### The FRT hook-length formula

The brick-1 target `#SYT(μ) · ∏_{c ∈ μ} h(c) = |μ|!` — i.e. `f^μ = |μ|! / ∏ h(c)` — is
**proved** (sorry-free) as `QOU.BraidKnot.HookProductHLF.numSYT_mul_hookProduct`.

It cannot be stated here: its proof needs `QOU.Mathlib.HookLengthFormula`, which
transitively imports *this* module (via `QOU.BraidKnot.SpechtClassification → Specht →
StandardYoungTableau`). The statement therefore lives one level downstream, in the leaf
module `QOU.BraidKnot.HookProductHLF`, where the import is legal. -/

end QOU.BraidKnot
