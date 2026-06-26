import Mathlib.Combinatorics.Young.SemistandardTableau
import Mathlib.SetTheory.Cardinal.Finite

/-!
# QOU.Mathlib.StandardYoungTableau — the standard Young tableau type Mathlib lacks

Mathlib's `Combinatorics.Young` provides `YoungDiagram` and `SemistandardYoungTableau` (weakly
increasing along rows, strictly increasing down columns, zero off the diagram) but **no standard
Young tableau** type and **no `#SYT(λ)` count** — and no `Combinatorics.RSK` at the pinned
toolchain (recon 2026-06-26, see `docs/scope/2026-06-24-identity-i-plancherel-snrep-infra-program.md`).

Both the Identity I axiom (i) `∑_λ #SYT(λ)² = n!` (RSK / Burnside) and the hook-length formula
`dim(λ) = n!/∏h_c` need an honest `#SYT(λ)`.  This file builds the **minimal** standard-tableau
type those need, as a refinement of Mathlib's `SemistandardYoungTableau`:

> A **standard Young tableau** of shape `μ` (with `n = |μ|` cells) is a semistandard tableau whose
> entry map is a **bijection from the cells of `μ` onto `{1, …, n}`**.

Weak rows (SSYT) + the bijection's injectivity give the usual *strict* rows (`row_strict`).  The
count is `numStandardYoungTableaux μ := Nat.card (StandardYoungTableau μ)` (`Nat.card` is total —
no `Fintype` instance is needed to *define* the count; finiteness + the closed-form value are the
tracked next steps toward RSK/HLF).

**Scope (per the program's Decision 1).** This is a *minimal in-repo* SYT, deliberately built only
as far as the Identity I axioms need; Specht modules / RSK / HLF are natural Mathlib-upstream
contributions and are flagged as such. Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib

open YoungDiagram

/-- A **standard Young tableau** of shape `μ`: a semistandard tableau whose entry map restricted to
the cells of `μ` is a bijection onto `{1, …, |μ|}`.  (Strict rows follow from weak rows +
injectivity — see `StandardYoungTableau.row_strict`.) -/
structure StandardYoungTableau (μ : YoungDiagram) where
  /-- The underlying semistandard tableau. -/
  toSsyt : SemistandardYoungTableau μ
  /-- The entry map is a bijection from the cells onto `{1, …, |μ|}`. -/
  bijOn : Set.BijOn (fun c : ℕ × ℕ => toSsyt.entry c.1 c.2)
    (μ.cells : Set (ℕ × ℕ)) (Set.Icc 1 μ.cells.card)

namespace StandardYoungTableau

variable {μ : YoungDiagram}

/-- Entry `(i, j)` of a standard Young tableau. -/
def entry (T : StandardYoungTableau μ) (i j : ℕ) : ℕ := T.toSsyt.entry i j

/-- The entry map is injective on the cells of `μ` (the filling is a bijection). -/
theorem injOn_cells (T : StandardYoungTableau μ) :
    Set.InjOn (fun c : ℕ × ℕ => T.entry c.1 c.2) (μ.cells : Set (ℕ × ℕ)) :=
  T.bijOn.injOn

/-- The entry map sends the cells onto `{1, …, |μ|}`. -/
theorem mapsTo_cells (T : StandardYoungTableau μ) :
    Set.MapsTo (fun c : ℕ × ℕ => T.entry c.1 c.2)
      (μ.cells : Set (ℕ × ℕ)) (Set.Icc 1 μ.cells.card) :=
  T.bijOn.mapsTo

/-- Membership of a cell `(i, j) ∈ μ` as a `Set`-membership in `↑μ.cells` (the form `InjOn`
consumes). -/
theorem mem_coe_cells {i j : ℕ} (h : (i, j) ∈ μ) : ((i, j) : ℕ × ℕ) ∈ (μ.cells : Set (ℕ × ℕ)) := by
  rw [Finset.mem_coe, YoungDiagram.mem_cells]; exact h

/-- **Rows are strictly increasing** — not merely weakly, as for a general semistandard tableau.
On a row, the SSYT weak-row inequality together with injectivity of the (bijective) filling forces
strictness.  This certifies the type is the genuine standard-tableau notion, not a vacuous wrapper. -/
theorem row_strict (T : StandardYoungTableau μ) {i j1 j2 : ℕ}
    (hlt : j1 < j2) (hcell : (i, j2) ∈ μ) : T.entry i j1 < T.entry i j2 := by
  have hc1 : (i, j1) ∈ μ := μ.up_left_mem (le_refl i) (le_of_lt hlt) hcell
  have hle : T.entry i j1 ≤ T.entry i j2 := T.toSsyt.row_weak hlt hcell
  rcases lt_or_eq_of_le hle with h | h
  · exact h
  · exact absurd (congrArg Prod.snd
      (T.injOn_cells (mem_coe_cells hc1) (mem_coe_cells hcell) h)) (Nat.ne_of_lt hlt)

end StandardYoungTableau

/-- **`#SYT(μ)`** — the number of standard Young tableaux of shape `μ`, as `Nat.card` (total; no
`Fintype` instance required to define it).  This is the combinatorial dimension `dim(μ)` whose
square-sum is `n!` (RSK) and whose hook-length closed form is `n!/∏h_c` — both tracked as the
next infra steps. -/
noncomputable def numStandardYoungTableaux (μ : YoungDiagram) : ℕ :=
  Nat.card (StandardYoungTableau μ)

end QOU.Mathlib
