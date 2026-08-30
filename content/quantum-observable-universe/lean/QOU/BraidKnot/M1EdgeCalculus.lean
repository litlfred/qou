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

/-! ## Telescoping: the two-case per-edge bound

`diagLen_lipschitz` bounds ONE step. What the `M₁ > 0` route needs is the SUM,
and the sum telescopes exactly:

    ∑_{t=0}^{λ₁-1} (D t − D (t+1))  =  D 0 − D λ₁  =  D 0.

So the profile's total fall is `D 0` — no limit shape, no error term, no
Berry–Esseen. Two consequences, one per edge type of the up-down chain, and
between them they cover every edge:

* **Same-sign contents** (`u ≤ v` on one side): `D u − D v` is the number of
  drop sites in `[u, v)`, so it lies in `[0, v − u]` and the per-edge slope
  `(D u − D v)/(v − u)` is a **density** in `[0, 1]`.
* **Opposite-sign contents**: the two sides telescope to the *same* total
  `D 0`, which cancels, leaving a difference of two counts each in `[0, D 0]`
  — hence `|D_μ u − D_μᵀ v| ≤ D 0`. This is the case the slope is unbounded on
  (it grows like `√(2n)`; see `..._edge_ratio_monotonicity.py`), so a bound
  covering it at all is the point.

Measured in `computations/deltalambda/wlambda_covariance_epic_M1_telescoping_route.py`:
0 violations of either bound over every edge at every `n ≤ 46`, and the second
is **sharp** — `max |slope| · g / D 0 = 1` exactly, attained. Neither closes
`M₁ > 0`: the two bounds together still exceed 1, so averaging is still
required. What they replace is an appeal to effective limit-shape asymptotics
with elementary, deterministic, finite statements. -/

/-- Diagonals only shrink outward. -/
theorem diagLen_antitone : Antitone (diagLen μ) :=
  antitone_nat_of_succ_le (diagLen_succ_le μ)

/-- **The main diagonal is the longest.** `D c ≤ D 0` for every `c`. -/
theorem diagLen_le_diagLen_zero (c : ℕ) : diagLen μ c ≤ diagLen μ 0 :=
  diagLen_antitone μ (Nat.zero_le c)

/-- **Telescoped Lipschitz.** Over `v − u` steps the profile falls by at most
`v − u`, since each single step falls by at most one. -/
theorem diagLen_le_add_sub {u v : ℕ} (h : u ≤ v) :
    diagLen μ u ≤ diagLen μ v + (v - u) := by
  induction v, h using Nat.le_induction with
  | base => simp
  | succ v hv ih =>
    have := diagLen_le_succ_add_one μ v
    omega

/-- **Same-sign edges: the slope is a density.** For `u ≤ v` on one side of the
main diagonal, `D u − D v` counts the drop sites in `[u, v)`, so it lies between
`0` and `v − u`; equivalently `(D u − D v)/(v − u) ∈ [0, 1]`. -/
theorem diagLen_sub_nonneg_le {u v : ℕ} (h : u ≤ v) :
    0 ≤ (diagLen μ u : ℤ) - (diagLen μ v : ℤ) ∧
      (diagLen μ u : ℤ) - (diagLen μ v : ℤ) ≤ (v : ℤ) - (u : ℤ) := by
  have h1 : diagLen μ v ≤ diagLen μ u := diagLen_antitone μ h
  have h2 := diagLen_le_add_sub μ h
  omega

/-- The main diagonal is transpose-invariant — it is cut out by `(i, i) ∈ μ`,
and the range bounds are implied by membership rather than extra conditions. -/
theorem diagLen_transpose_zero : diagLen μ.transpose 0 = diagLen μ 0 := by
  unfold diagLen
  congr 1
  ext i
  simp only [mem_diagIdx, Nat.add_zero, YoungDiagram.rowLen_transpose,
    YoungDiagram.colLen_transpose]
  constructor
  · rintro ⟨-, h⟩
    have hii : (i, i) ∈ μ := YoungDiagram.mem_iff_lt_colLen.mpr h
    exact ⟨YoungDiagram.mem_iff_lt_colLen.mp
             (μ.up_left_mem (le_refl i) (Nat.zero_le i) hii),
           YoungDiagram.mem_iff_lt_rowLen.mp hii⟩
  · rintro ⟨-, h⟩
    have hii : (i, i) ∈ μ := YoungDiagram.mem_iff_lt_rowLen.mpr h
    exact ⟨YoungDiagram.mem_iff_lt_rowLen.mp
             (μ.up_left_mem (Nat.zero_le i) (le_refl i) hii),
           YoungDiagram.mem_iff_lt_colLen.mp hii⟩

/-- **Opposite-sign edges.** The two sides of the diagonal telescope to the same
total `D 0`, which cancels; what is left is a difference of two drop-site
counts, each in `[0, D 0]`. So `|D_μ u − D_μᵀ v| ≤ D 0`, hence the slope is at
most `D 0 / g` where `g` is the content gap. This bound is sharp. -/
theorem abs_diagLen_sub_transpose_le (u v : ℕ) :
    |(diagLen μ u : ℤ) - (diagLen μ.transpose v : ℤ)| ≤ (diagLen μ 0 : ℤ) := by
  have h1 := diagLen_le_diagLen_zero μ u
  have h2 := diagLen_le_diagLen_zero μ.transpose v
  have h3 := diagLen_transpose_zero μ
  rw [abs_le]
  omega

end QOU.BraidKnot.M1EdgeCalculus
