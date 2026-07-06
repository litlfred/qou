import Mathlib.Tactic

/-!
# Lever-1 binding kernel — (b)-exclusion of the constant-coefficient depth-2 recurrence

The lever-1 binding generating function uses the selection-rule weights
`lw(c) = (1/(c+1)) · Σ_{λ ⊢ c+1} dim_q(λ)` (mean quantum dimension; `a_D^(n) = lw(n−1)`). A
natural hypothesis — the depth-2, `det = 1` kernel `R = x² − τx + 1` — would make the `lw`
sequence satisfy a **constant-coefficient depth-2 linear recurrence** `lw(c) = τ·lw(c−1) − lw(c−2)`
for a *single fixed* `τ`. The numerical probe (`lever1_lw_depth2_recurrence_test.py`, audit
`2026-06-24-lever1-lw-depth2-recurrence-falsified.md`) found this **fails beyond the 3-point seed**:
`τ` fit to `c = 2,3` (i.e. the `n = 3,4` checks) does not satisfy the next (`c = 4`) check.

This file is the **(b)-structural-exclusion** of that constant-coefficient depth-2 model, proved at
the **classical limit `q = 1`** (mean *classical* irrep dimension), where it is a pure-`ℚ` fact —
and it *implies* the `q`-general failure: the recurrence residual is a rational function of `q`
that is **already nonzero at `q = 1`** (value `−7/240`), hence not the zero function. The carried
invariant is the standard `S_n` irreducible dimension via the hook-length formula — **computed from
the partition structure, not tabulated** (dodge-proof), reusing the pattern of
`WLambdaDefectClosedForm`.

**Scope ((a)/(b) discipline, AGENTS.md).** This is the **(b)** exclusion of *the constant-coefficient
depth-2 model* (a window-independent `τ`). It does **not** exclude a `q`-family / variable-`τ`
monodromy `B` — that object (the abelianised `λ_SW` holonomy on the color `E_q`) is the open,
owner-gated keystone target and is untouched here. The file formalizes the audit's finding that
"`θ_binding = 0.7815` is a 3-point seed-fit artifact, not a derived constant-`τ` rate."
Ref: [manuscript] docs/audits/2026-06-24-lever1-lw-depth2-recurrence-falsified.md
-/

namespace QOU.Mass.Lever1Depth2

/-- Hook lengths of a partition `l` (descending rows): cell `(i,j)` has hook `arm + leg + 1`.
Same construction as `QOU.BraidKnot.WLambdaDefect.hookLengths`; kept local so this file is
self-contained. -/
def hookLengths (l : List ℕ) : List ℕ :=
  (List.range l.length).flatMap fun i =>
    let li := l.getD i 0
    (List.range li).map fun j =>
      (li - 1 - j) + ((l.drop (i + 1)).filter (fun p => decide (j < p))).length + 1

/-- `dim λ = (Σλ)! / ∏ h_c` (hook-length formula; exact `ℕ` division — the HLF guarantees
`∏ h_c ∣ (Σλ)!`). -/
def dimOf (l : List ℕ) : ℕ := Nat.factorial l.sum / (hookLengths l).prod

/-- Partitions of `m` for `m = 2..5`, as explicit descending lists (the dimensions are **computed**
from this structure, not tabulated). -/
def partitionsOf : ℕ → List (List ℕ)
  | 2 => [[2], [1, 1]]
  | 3 => [[3], [2, 1], [1, 1, 1]]
  | 4 => [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
  | 5 => [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]
  | _ => []

/-- `Σ_{λ ⊢ m} dim(λ)` — the classical dimension sum (computed via hooks). -/
def dimSum (m : ℕ) : ℕ := ((partitionsOf m).map dimOf).sum

/-- **Computed dimension sums** (dodge-proof, via hook-length `dim`): `Σ_{λ⊢m} dim(λ) = 2, 4, 10, 26`
for `m = 2,3,4,5`. -/
theorem dimSum_values : dimSum 2 = 2 ∧ dimSum 3 = 4 ∧ dimSum 4 = 10 ∧ dimSum 5 = 26 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> decide

/-- Classical lever-1 weight `lw(c) = (1/(c+1)) · Σ_{λ ⊢ c+1} dim(λ)` (the `q → 1` limit of the
mean quantum dimension). -/
noncomputable def lwCl (c : ℕ) : ℚ := (dimSum (c + 1) : ℚ) / ((c : ℚ) + 1)

/-- The classical lever-1 weights: `lw(1)=1`, `lw(2)=4/3`, `lw(3)=5/2`, `lw(4)=26/5`. -/
theorem lwCl_values : lwCl 1 = 1 ∧ lwCl 2 = 4 / 3 ∧ lwCl 3 = 5 / 2 ∧ lwCl 4 = 26 / 5 := by
  obtain ⟨h2, h3, h4, h5⟩ := dimSum_values
  refine ⟨?_, ?_, ?_, ?_⟩ <;> simp only [lwCl]
  · rw [show (1 : ℕ) + 1 = 2 from rfl, h2]; norm_num
  · rw [show (2 : ℕ) + 1 = 3 from rfl, h3]; norm_num
  · rw [show (3 : ℕ) + 1 = 4 from rfl, h4]; norm_num
  · rw [show (4 : ℕ) + 1 = 5 from rfl, h5]; norm_num

/-- **(b)-exclusion of the constant-coefficient depth-2 recurrence.** There is **no** fixed `τ : ℚ`
for which the `det = 1` depth-2 recurrence `lw(c) = τ·lw(c−1) − lw(c−2)` holds on the classical
lever-1 weights at both `c = 3` and `c = 4`: the `c = 3` (seed) equation forces `τ = 21/8`, and then
the `c = 4` equation requires `26/5 = 251/48`, false (residual `−7/240`). Hence the lever-1 `lw`
sequence is **not** the orbit `φ(Mⁿ v₀)` of any window-independent depth-2 kernel — `θ_binding` is a
seed-fit artifact, not a derived constant-`τ` rate. (`q`-deformation only worsens this: the residual
rational function is already nonzero at `q = 1`.) -/
theorem depth2_no_fixed_tau :
    ∀ τ : ℚ, ¬ (lwCl 3 = τ * lwCl 2 - lwCl 1 ∧ lwCl 4 = τ * lwCl 3 - lwCl 2) := by
  obtain ⟨e1, e2, e3, e4⟩ := lwCl_values
  rintro τ ⟨hseed, hnext⟩
  rw [e1, e2, e3] at hseed
  rw [e2, e3, e4] at hnext
  -- hseed : 5/2 = τ*(4/3) - 1  ⇒  τ = 21/8 ;  hnext : 26/5 = τ*(5/2) - 4/3
  have hτ : τ = 21 / 8 := by linarith
  rw [hτ] at hnext
  norm_num at hnext

end QOU.Mass.Lever1Depth2
