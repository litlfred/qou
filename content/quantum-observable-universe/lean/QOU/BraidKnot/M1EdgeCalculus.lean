import QOU.BraidKnot.HookSumRegisterBridge

/-!
# The M₁ edge calculus: Fact A and the 1-Lipschitz diagonal lemma

Two pieces of the `M₁ > 0` reduction (bean `qou-k5r5`) that were established by
exact computation and flagged "Lean-formalizable", and are now proved.

`M₁ = Cov_Planch(Σ_h, ω₃)` is written on the Fulman up-down chain as `M₁ = P − N`
with

    P := Cov(Σ|c|, ω₃) ≥ 0        N := −Cov(ΣD², ω₃) ≥ 0

and the whole remaining gap is the finite-`n` domination `P > N`. This module
proves the **`P ≥ 0` half** at the per-edge level, and the structural lemma that
bounds the per-edge `N/P` ratio.

## Fact A is algebra, not combinatorics

An up-down move removes a box of content `c_r` and adds one of content `c_a`.
The increments were measured exactly:

    Δω₃ = c_r² − c_a²          ΔΣ|c| = |c_r| − |c_a|

Their product is `(|c_r| − |c_a|)²(|c_r| + |c_a|) ≥ 0` — and that identity is
true of *any* two integers, because `c² = |c|²`. So the per-edge sign of `P`
needs no property of Young diagrams at all: `factA_nonneg` below is stated for
arbitrary `cr ca : ℤ`, which is the honest strength. What the combinatorics
supplies is only the two increment formulas, and those are inputs here rather
than theorems (they are per-move facts about the chain, not about a single
diagram).

## The 1-Lipschitz lemma is where the diagrams enter

`D c`, the number of cells on diagonal `c`, satisfies `D (c+1) ≤ D c ≤ D (c+1) + 1`.
The right-hand inequality is what caps the per-edge ratio `N/P|ₑ` at 4, via
`d_a − d_r ≤ r − a`.

Its proof is short and worth stating, because it is the only place antitonicity
of the row lengths is used: the indices on diagonal `c` form a *downward-closed*
set, hence an initial segment `range (D c)`. If `D c` exceeded `D (c+1)` by two,
the two indices `k`, `k+1` in the gap would both satisfy `rowLen i = i + c + 1`,
forcing `rowLen (k+1) > rowLen k` and contradicting `rowLen_anti`.

Only the `c ≥ 0` side is proved. The `c < 0` side is the transpose statement, and
`YoungDiagram.rowLen_transpose` turns one into the other; it is not restated here
because nothing in the reduction needs both sides simultaneously.

## What this does NOT give

`P ≥ 0` per-edge does not give `P > N`. The parent bean records that the
per-edge ratio is *unbounded above by any bound that helps* — it reaches 4, so
no per-edge or FKG argument can close the gap — and that weight-suppression is
refuted, `N/P < 1` being an averaging phenomenon. These lemmas are the floor
under that analysis, not a route around it.

-- Ref: [bean] qou-k5r5, qou-t6hc
-/

namespace QOU.BraidKnot.M1EdgeCalculus

open Finset

/-! ## Fact A — the per-edge sign of `P` -/

/-- The product of the two measured increments, factored. True of any integers:
`c² = |c|²` is all it uses. -/
theorem factA_factor (cr ca : ℤ) :
    (|cr| - |ca|) * (cr ^ 2 - ca ^ 2) = (|cr| - |ca|) ^ 2 * (|cr| + |ca|) := by
  rw [← sq_abs cr, ← sq_abs ca]
  ring

/-- **Fact A.** `ΔΣ|c| · Δω₃ ≥ 0` on every edge, hence `P ≥ 0`. -/
theorem factA_nonneg (cr ca : ℤ) : 0 ≤ (|cr| - |ca|) * (cr ^ 2 - ca ^ 2) := by
  rw [factA_factor]
  exact mul_nonneg (sq_nonneg _) (by positivity)

/-- The product vanishes exactly when the two contents have equal absolute
value — i.e. the edge is `ω₃`-neutral. Recorded because it identifies which
edges contribute nothing to `P`, and those are exactly the ones a domination
argument may discard. -/
theorem factA_eq_zero_iff (cr ca : ℤ) :
    (|cr| - |ca|) * (cr ^ 2 - ca ^ 2) = 0 ↔ |cr| = |ca| := by
  rw [factA_factor]
  constructor
  · intro h
    rcases mul_eq_zero.mp h with h1 | h2
    · have := pow_eq_zero_iff (n := 2) (by norm_num) |>.mp h1
      linarith [this]
    · have hr : (0 : ℤ) ≤ |cr| := abs_nonneg cr
      have ha : (0 : ℤ) ≤ |ca| := abs_nonneg ca
      have : |cr| = 0 ∧ |ca| = 0 := by constructor <;> linarith
      rw [this.1, this.2]
  · intro h; rw [h]; ring

/-! ## The diagonal profile and its 1-Lipschitz property -/

variable (μ : YoungDiagram)

/-- Row indices meeting diagonal `c ≥ 0`: those `i` with `(i, i + c) ∈ μ`.
Bounded by `μ.colLen 0`, which every nonempty row index satisfies. -/
def diagIdx (c : ℕ) : Finset ℕ :=
  (range (μ.colLen 0)).filter (fun i => i + c < μ.rowLen i)

/-- `D c` — the number of cells on diagonal `c ≥ 0`. -/
def diagLen (c : ℕ) : ℕ := (diagIdx μ c).card

/-- The indices on a diagonal are downward closed: `rowLen` is antitone, so a
smaller row reaches at least as far. -/
theorem diagIdx_downward_closed (c : ℕ) :
    ∀ a b, a ≤ b → b ∈ diagIdx μ c → a ∈ diagIdx μ c := by
  intro a b hab hb
  simp only [diagIdx, Finset.mem_filter, Finset.mem_range] at hb ⊢
  obtain ⟨hblt, hbc⟩ := hb
  refine ⟨lt_of_le_of_lt hab hblt, ?_⟩
  calc a + c ≤ b + c := by omega
    _ < μ.rowLen b := hbc
    _ ≤ μ.rowLen a := μ.rowLen_anti a b hab

/-- Hence the diagonal's index set is the initial segment `range (D c)`. -/
theorem diagIdx_eq_range (c : ℕ) : diagIdx μ c = range (diagLen μ c) :=
  QOU.HookSumComplete.downward_closed_eq_range (diagIdx_downward_closed μ c)

/-- Membership, in the form the Lipschitz proof uses. -/
theorem mem_diagIdx {c i : ℕ} :
    i ∈ diagIdx μ c ↔ i < μ.colLen 0 ∧ i + c < μ.rowLen i := by
  simp only [diagIdx, Finset.mem_filter, Finset.mem_range]

/-- Diagonals shrink outward: `D (c+1) ≤ D c`. -/
theorem diagLen_succ_le (c : ℕ) : diagLen μ (c + 1) ≤ diagLen μ c := by
  refine Finset.card_le_card ?_
  intro i hi
  rw [mem_diagIdx] at hi ⊢
  exact ⟨hi.1, by omega⟩

/-- **The 1-Lipschitz lemma.** `D c ≤ D (c+1) + 1`: a diagonal carries at most
one cell more than the next one out.

If it carried two more, the indices `k = D (c+1)` and `k+1` would both lie on
diagonal `c` and not on `c+1`, forcing `rowLen k = k + c + 1` and
`rowLen (k+1) = k + c + 2` — a strictly longer row below a shorter one. -/
theorem diagLen_le_succ_add_one (c : ℕ) : diagLen μ c ≤ diagLen μ (c + 1) + 1 := by
  by_contra hcon
  push_neg at hcon
  set k := diagLen μ (c + 1) with hk
  -- `k` and `k+1` are on diagonal `c` …
  have hmem : ∀ j, j < diagLen μ c → j ∈ diagIdx μ c := by
    intro j hj; rw [diagIdx_eq_range]; exact Finset.mem_range.mpr hj
  have hk0 : k ∈ diagIdx μ c := hmem k (by omega)
  have hk1 : k + 1 ∈ diagIdx μ c := hmem (k + 1) (by omega)
  -- … and neither is on diagonal `c+1`, that one being `range k`.
  have hnot : ∀ j, k ≤ j → j ∉ diagIdx μ (c + 1) := by
    intro j hj hmem'
    rw [diagIdx_eq_range, Finset.mem_range, ← hk] at hmem'
    omega
  have e0 : μ.rowLen k = k + c + 1 := by
    have h1 := (mem_diagIdx μ).mp hk0
    have h2 := hnot k le_rfl
    rw [mem_diagIdx] at h2
    push_neg at h2
    omega
  have e1 : μ.rowLen (k + 1) = k + c + 2 := by
    have h1 := (mem_diagIdx μ).mp hk1
    have h2 := hnot (k + 1) (by omega)
    rw [mem_diagIdx] at h2
    push_neg at h2
    omega
  have := μ.rowLen_anti k (k + 1) (by omega)
  omega

/-- The two halves together: `|D c − D (c+1)| ≤ 1`, stated over `ℤ`. -/
theorem diagLen_lipschitz (c : ℕ) :
    |(diagLen μ c : ℤ) - (diagLen μ (c + 1) : ℤ)| ≤ 1 := by
  have h1 := diagLen_succ_le μ c
  have h2 := diagLen_le_succ_add_one μ c
  rw [abs_le]
  omega

end QOU.BraidKnot.M1EdgeCalculus
