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

/-! ## The area constraint

Every bound above uses only `D 0`, `λ₁` and 1-Lipschitz. The global constraint
`∑_c D c = n` was unused, and it is worth more than all of them: computed over
the limiting edge measure
(`wlambda_covariance_epic_M1_limit_closed_form.py`), adding it takes the
budget's margin from **0.047 %** to **7.54 %** — about 160× more room. The reason
is that `min (D 0) (λ₁ - a)` is nearly vacuous away from the origin: it permits
`D a = 0.637 √n` at `a = √n` where the truth is `0.218 √n`.

Two elementary facts do it, and each is one step from something already proved:

* **monotonicity** — `a * D a ≤ ∑_{c < a} D c`, since `D` is antitone;
* **1-Lipschitz tail** — `D a * (D a + 1) / 2 ≤ ∑_{c ∈ [a, a + D a)} D c`, since
  `D (a + k) ≥ D a - k`, which is `diagLen_le_add_sub`.

The two ranges are disjoint and abut, so together they give
`diagLen_area_bound` below. Solving that quadratic for `D a` gives the form the
quadrature uses, `D a ≤ √(a² + 2A) - a`; it is stated here in the equivalent
division-free way, which is both stronger as a Lean statement and free of
`Real.sqrt`.

**What is NOT proved here.** The bound is against the PARTIAL sum
`∑_{c < a + D a} D c`, which is what the argument needs and is stronger than
bounding by the full area. Identifying that sum with a count of boxes — hence
with `n`, and with `A_σ → n/2` in the limit — is a separate step, and the
`A_σ → n/2` half is a limit-shape input rather than a theorem. The 7.54 % figure
depends on it; with only `A_σ ≤ n` the margin is 0.094 %. -/

/-- Gauss, in the doubled form that stays inside `ℕ` (no division, no truncated
subtraction escaping). -/
private theorem two_mul_sum_range_sub (d : ℕ) :
    2 * ∑ i ∈ Finset.range d, (d - i) = d * (d + 1) := by
  -- Reflect `d - i` into `i + 1`, then use Gauss. Induction was the obvious
  -- route and fails: `omega` sees `∑ i ∈ range m, (m - i)` and its eta-reduced
  -- form as DIFFERENT atoms, so the inductive hypothesis never connects.
  have h1 : ∑ i ∈ Finset.range d, (d - i) = ∑ i ∈ Finset.range d, (i + 1) := by
    rw [← Finset.sum_range_reflect (fun j => j + 1) d]
    refine Finset.sum_congr rfl fun i hi => ?_
    have := Finset.mem_range.mp hi
    omega
  have h2 := Finset.sum_range_id_mul_two d
  -- omega is linear: `d * (d + 1)` and `d * (d - 1)` are unrelated atoms to it,
  -- so hand it the bridge. The `d = 0` case needs care -- truncated subtraction
  -- makes `d * (d - 1) = 0` there, which is still correct.
  have h3 : d * (d + 1) = d * (d - 1) + 2 * d := by
    cases d with
    | zero => rfl
    | succ m => simp only [Nat.add_sub_cancel]; ring
  rw [h1, Finset.sum_add_distrib, Finset.sum_const, Finset.card_range, smul_eq_mul]
  omega

/-- **Monotonicity piece.** The first `a` diagonals are each at least as long as
the `a`-th, so they sum to at least `a * D a`. -/
theorem mul_diagLen_le_sum (a : ℕ) :
    a * diagLen μ a ≤ ∑ c ∈ Finset.range a, diagLen μ c := by
  calc a * diagLen μ a = ∑ _c ∈ Finset.range a, diagLen μ a := by
        rw [Finset.sum_const, Finset.card_range, smul_eq_mul]
    _ ≤ ∑ c ∈ Finset.range a, diagLen μ c :=
        Finset.sum_le_sum fun c hc =>
          diagLen_antitone μ (le_of_lt (Finset.mem_range.mp hc))

/-- **1-Lipschitz tail piece.** Past `a` the profile falls by at most one per
step, so the next `D a` diagonals sum to at least the triangle `D a (D a + 1)/2`
— stated doubled to stay in `ℕ`. -/
theorem triangle_le_sum_Ico (a : ℕ) :
    diagLen μ a * (diagLen μ a + 1)
      ≤ 2 * ∑ c ∈ Finset.Ico a (a + diagLen μ a), diagLen μ c := by
  set d := diagLen μ a with hd
  have hstep : ∀ i ∈ Finset.range d, d - i ≤ diagLen μ (a + i) := by
    intro i _
    have := diagLen_le_add_sub μ (Nat.le_add_right a i)
    simp only [Nat.add_sub_cancel_left] at this
    omega
  calc d * (d + 1) = 2 * ∑ i ∈ Finset.range d, (d - i) := (two_mul_sum_range_sub d).symm
    _ ≤ 2 * ∑ i ∈ Finset.range d, diagLen μ (a + i) := by
        exact Nat.mul_le_mul_left 2 (Finset.sum_le_sum hstep)
    _ = 2 * ∑ c ∈ Finset.Ico a (a + d), diagLen μ c := by
        rw [Finset.sum_Ico_eq_sum_range]
        simp

/-- **The area bound.** Combining the two, the diagonals up to `a + D a` already
account for `a * D a + D a (D a + 1)/2` cells. Since that sum is at most the
number of cells on that side of the diagonal — at most `n` — solving for `D a`
gives `D a ≤ √(a² + 2A) - a`, the form used in the quadrature. -/
theorem diagLen_area_bound (a : ℕ) :
    2 * (a * diagLen μ a) + diagLen μ a * (diagLen μ a + 1)
      ≤ 2 * ∑ c ∈ Finset.range (a + diagLen μ a), diagLen μ c := by
  have hsplit :
      (∑ c ∈ Finset.Ico 0 a, diagLen μ c) + (∑ c ∈ Finset.Ico a (a + diagLen μ a), diagLen μ c)
        = ∑ c ∈ Finset.Ico 0 (a + diagLen μ a), diagLen μ c :=
    Finset.sum_Ico_consecutive _ (Nat.zero_le a) (Nat.le_add_right a _)
  rw [← Finset.range_eq_Ico] at hsplit
  have h1 := mul_diagLen_le_sum μ a
  have h2 := triangle_le_sum_Ico μ a
  have h3 : ∑ c ∈ Finset.range (a + diagLen μ a), diagLen μ c
      = (∑ c ∈ Finset.range a, diagLen μ c)
        + ∑ c ∈ Finset.Ico a (a + diagLen μ a), diagLen μ c := by
    rw [← hsplit, Finset.range_eq_Ico]
  omega

/-! ## Refining the opposite-sign bound

`abs_diagLen_sub_transpose_le` bounds the opposite-sign slope by `D 0 / g`, and
that bound is SHARP per edge. But it is not sharp on AVERAGE, and the difference
decides the route: computed over the limiting edge measure
(`wlambda_covariance_epic_M1_limit_closed_form.py`), the crude bound puts the
budget at `1.005709` — a miss — while the refinement below puts it at `0.999534`.

Two facts do it, and both are one step from what is already proved here.

* `D 0 ≤ D c + c` (that is `diagLen_le_add_sub` at `u = 0`): the profile cannot
  have fallen by more than `c` after `c` steps, so at most `c` of the `D 0` drop
  sites lie in `[0, c)`.
* `D c + c ≤ λ₁` (`diagLen_add_le_rowLen_zero`, new below): the last box on
  diagonal `c` sits at row `D c - 1`, column `D c - 1 + c`, and that column is
  inside row `D c - 1`, hence inside row `0`.

The second is what bounds the drop sites from the *other* end: there are only
`λ₁ - D 0` non-drop sites in total on a side, so a long interval must contain
drops. Together they give `diagLen_sub_transpose_le_refined`.

**The guard on the second lemma is real, not decorative.** `D c + c ≤ λ₁` fails
when `D c = 0` and `c > λ₁` — the ℤ form would then assert `0 ≤` a negative. So
it is stated over ℕ unconditionally (truncated subtraction makes it true), and
over ℤ only under `0 < D c`. Every actual corner satisfies that, a corner being a
box on its own diagonal. -/

/-- `D c` cells on diagonal `c` reach column `D c - 1 + c`, which lies in row `0`.
Stated with truncated subtraction so it holds unconditionally: past the first row
both sides are `0`. -/
theorem diagLen_le_rowLen_zero_sub (c : ℕ) : diagLen μ c ≤ μ.rowLen 0 - c := by
  rcases Nat.eq_zero_or_pos (diagLen μ c) with h | h
  · simp [h]
  · have hmem : diagLen μ c - 1 ∈ diagIdx μ c := by
      rw [diagIdx_eq_range]
      exact Finset.mem_range.mpr (by omega)
    rw [mem_diagIdx] at hmem
    have := μ.rowLen_anti 0 (diagLen μ c - 1) (Nat.zero_le _)
    omega

/-- The same fact in the form the refined bound uses: for a NONEMPTY diagonal,
`D c + c ≤ λ₁`. The hypothesis cannot be dropped — see the section note. -/
theorem diagLen_add_le_rowLen_zero {c : ℕ} (h : 0 < diagLen μ c) :
    diagLen μ c + c ≤ μ.rowLen 0 := by
  have hmem : diagLen μ c - 1 ∈ diagIdx μ c := by
    rw [diagIdx_eq_range]
    exact Finset.mem_range.mpr (by omega)
  rw [mem_diagIdx] at hmem
  have := μ.rowLen_anti 0 (diagLen μ c - 1) (Nat.zero_le _)
  omega

/-- **The refined opposite-sign bound.** For an edge whose near corner sits at
distance `a` on `μ`'s side and whose far corner sits at distance `r` on `μᵀ`'s,

    D_μ a − D_μᵀ r  ≤  min (D 0) (λ₁ − a)  −  max 0 (D 0 − r).

The first term bounds the near diagonal both by the main diagonal and by how much
room is left in row `0`; the second says the far diagonal cannot have lost more
than `r` of its `D 0` cells. Dropping both refinements gives back
`abs_diagLen_sub_transpose_le`'s `D 0`. -/
theorem diagLen_sub_transpose_le_refined {a r : ℕ} (ha : 0 < diagLen μ a) :
    (diagLen μ a : ℤ) - (diagLen μ.transpose r : ℤ)
      ≤ min (diagLen μ 0 : ℤ) ((μ.rowLen 0 : ℤ) - (a : ℤ))
        - max 0 ((diagLen μ 0 : ℤ) - (r : ℤ)) := by
  have h1 : diagLen μ a ≤ diagLen μ 0 := diagLen_le_diagLen_zero μ a
  have h2 : diagLen μ a + a ≤ μ.rowLen 0 := diagLen_add_le_rowLen_zero μ ha
  have h3 : diagLen μ.transpose 0 ≤ diagLen μ.transpose r + r := by
    simpa using diagLen_le_add_sub μ.transpose (Nat.zero_le r)
  have h4 : diagLen μ.transpose 0 = diagLen μ 0 := diagLen_transpose_zero μ
  omega

/-! ## The site distribution `κ`, and what the "inflation factor" actually is

The `M₁ > 0` route needs `E_ω[slope]`, and by the telescoping lemmas above a
same-sign slope is the *density of drop sites* `δ t := D t − D (t+1) ∈ {0,1}`
in the edge's content interval. The measured quantity that governs the route is

    infl := E_ω[density] / E_ω[D 0 / λ₁]

— how much more the ω-chosen intervals drop than the diagram's own global
average. It is measured at 0.494 at `n = 46` and rising
(`wlambda_covariance_epic_M1_telescoping_route.py`).

This section says what that ratio *is*. Give each interval `e` weight `w e` and
let it spread that weight uniformly over the sites it covers:

    κ t := ∑_{e ∋ t} w e / (hi e − lo e).

Two facts, both elementary and both proved here:

* `kappa_sum` — `∑_t κ t = ∑_e w e`. Each interval contributes `g · (1/g) = 1`,
  so **κ is (after normalising) a probability distribution on SITES**.
* `weighted_density_eq_kappa_dot` — the weighted sum of interval densities
  equals `∑_t κ t · δ t`.

Together: the ω-average interval density is exactly *the κ-mass sitting on drop
sites*. Since there are `D 0` drop sites among `T` (the telescoping identity),
uniform κ gives exactly the global density `D 0 / T`, i.e. `infl = 1`. So the
inflation factor is neither mysterious nor a fitted constant — it is precisely
the departure of κ from uniform, and `infl > 1` iff ω over-weights drop sites.

What this does NOT do is bound it. κ is determined by the Plancherel up-down
edge measure, not by any property of a Young diagram, so no theorem about
`diagLen` can constrain it; that is measurement's job. Recorded because the
identity is what makes the measured number mean something.

Two consequences worth stating, since one of them corrects a claim I made
before proving any of this:

* `E_ω[D 0 / λ₁] → 1/π`, so asymptotically `infl < π/2` is *the same statement*
  as `E_ω[density] < 1/2` — the pointwise limit-shape bound already known to be
  exactly critical. I had reported "infl = 0.494 against π/2" as comfortable
  headroom. It is the constraint restated, not headroom.
* `1/2` is the pointwise maximum of the VKLS local drop density, attained only
  at the main diagonal. So `infl → π/2` would require κ to concentrate at the
  ORIGIN. Measured over `n = 12..48`, κ's mean site moves *away* from it and
  then **plateaus** near `0.853·√n` — it is not heading for the origin, which
  is the failure mode that would sink the route. Evidence, not proof: the
  ceiling implied by that position has settled at ≈0.3545 (so `infl → ≈1.11`),
  but the measured density is still only ~54% of it and climbing.

`sum_drop_diagLen` below is the same telescoping identity instantiated at an
actual Young diagram: the profile falls from `D 0` to `0` across `[0, λ₁)`, so
the diagram's global drop density is exactly `D 0 / λ₁`. -/

section Kappa

variable {ι : Type*}

/-- `κ t` — the weight a finite family of intervals `[lo e, hi e)` puts on site
`t`, each interval spreading its weight `w e` uniformly over the sites it
covers. -/
noncomputable def kappa (E : Finset ι) (lo hi : ι → ℕ) (w : ι → ℚ) (t : ℕ) : ℚ :=
  ∑ e ∈ E, if t ∈ Finset.Ico (lo e) (hi e) then w e / ((hi e : ℚ) - (lo e : ℚ)) else 0

/-- **κ is a distribution on sites.** Each interval spreads exactly its own
weight, so the site weights sum to the total interval weight. -/
theorem kappa_sum (E : Finset ι) (lo hi : ι → ℕ) (w : ι → ℚ) (T : ℕ)
    (hsub : ∀ e ∈ E, Finset.Ico (lo e) (hi e) ⊆ Finset.range T)
    (hpos : ∀ e ∈ E, lo e < hi e) :
    ∑ t ∈ Finset.range T, kappa E lo hi w t = ∑ e ∈ E, w e := by
  unfold kappa
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun e he => ?_
  rw [Finset.sum_ite_mem, Finset.inter_eq_right.mpr (hsub e he), Finset.sum_const,
    Nat.card_Ico, nsmul_eq_mul]
  have h : ((hi e : ℚ) - (lo e : ℚ)) ≠ 0 := by
    have := hpos e he
    have : (lo e : ℚ) < (hi e : ℚ) := by exact_mod_cast this
    linarith
  rw [Nat.cast_sub (le_of_lt (hpos e he))]
  field_simp

/-- Telescoping over an interval: the total fall of `D` across `[lo, hi)` is
`D lo − D hi`, whatever `D` is. -/
theorem sum_drop_eq (D : ℕ → ℤ) {lo hi : ℕ} (h : lo ≤ hi) :
    ∑ t ∈ Finset.Ico lo hi, (D t - D (t + 1)) = D lo - D hi := by
  induction hi, h using Nat.le_induction with
  | base => simp
  | succ m hm ih =>
    rw [Finset.sum_Ico_succ_top hm, ih]
    ring

/-- **The weighted average of interval densities is the κ-average of `δ`.**
Each interval's density `(D lo − D hi)/(hi − lo)` is the mean of the one-step
drops over its sites; weighting and exchanging the two sums replaces the
intervals by κ. -/
theorem weighted_density_eq_kappa_dot (E : Finset ι) (lo hi : ι → ℕ) (w : ι → ℚ)
    (D : ℕ → ℤ) (T : ℕ)
    (hsub : ∀ e ∈ E, Finset.Ico (lo e) (hi e) ⊆ Finset.range T)
    (hpos : ∀ e ∈ E, lo e < hi e) :
    ∑ e ∈ E, w e * (((D (lo e) - D (hi e) : ℤ) : ℚ) / ((hi e : ℚ) - (lo e : ℚ)))
      = ∑ t ∈ Finset.range T, kappa E lo hi w t * ((D t - D (t + 1) : ℤ) : ℚ) := by
  have key : ∀ e ∈ E,
      w e * (((D (lo e) - D (hi e) : ℤ) : ℚ) / ((hi e : ℚ) - (lo e : ℚ)))
        = ∑ t ∈ Finset.range T,
            (if t ∈ Finset.Ico (lo e) (hi e)
              then w e / ((hi e : ℚ) - (lo e : ℚ)) else 0) * ((D t - D (t + 1) : ℤ) : ℚ) := by
    intro e he
    have hle : lo e ≤ hi e := le_of_lt (hpos e he)
    have hs : ∑ t ∈ Finset.Ico (lo e) (hi e), ((D t - D (t + 1) : ℤ) : ℚ)
        = ((D (lo e) - D (hi e) : ℤ) : ℚ) := by
      rw [← sum_drop_eq D hle]
      push_cast
      rfl
    simp only [ite_mul, zero_mul]
    rw [Finset.sum_ite_mem, Finset.inter_eq_right.mpr (hsub e he), ← Finset.mul_sum, hs]
    ring
  rw [Finset.sum_congr rfl key, Finset.sum_comm]
  refine Finset.sum_congr rfl fun t _ => ?_
  unfold kappa
  rw [Finset.sum_mul]

/-- **Uniform κ gives exactly the global density.** If every site carries the
same weight, the ω-average of the interval densities collapses to the total fall
of `D` spread over all `T` sites. So `infl = 1` is precisely the uniform case,
and the inflation factor measures nothing but κ's departure from uniform. -/
theorem kappa_uniform_dot (D : ℕ → ℤ) (T : ℕ) (c : ℚ) :
    ∑ t ∈ Finset.range T, c * ((D t - D (t + 1) : ℤ) : ℚ)
      = c * ((D 0 - D T : ℤ) : ℚ) := by
  rw [← Finset.mul_sum]
  congr 1
  rw [Finset.range_eq_Ico, ← sum_drop_eq D (Nat.zero_le T)]
  push_cast
  rfl

end Kappa

/-- Past the first row every diagonal is empty: `i + λ₁ < rowLen i ≤ λ₁` is
impossible. -/
theorem diagLen_rowLen_zero : diagLen μ (μ.rowLen 0) = 0 := by
  rw [diagLen, Finset.card_eq_zero, Finset.eq_empty_iff_forall_notMem]
  intro i hi
  rw [mem_diagIdx] at hi
  have := μ.rowLen_anti 0 i (Nat.zero_le i)
  omega

/-- **The telescoping total for a Young diagram.** The profile falls from `D 0`
to `0` across `[0, λ₁)`, so the sum of the one-step drops is exactly `D 0` — the
Durfee side — and the diagram's global drop density is exactly `D 0 / λ₁`. This
is the quantity the `M₁ > 0` route trades the effective CLT for: it is an
identity, not an estimate. -/
theorem sum_drop_diagLen :
    ∑ t ∈ Finset.range (μ.rowLen 0), ((diagLen μ t : ℤ) - (diagLen μ (t + 1) : ℤ))
      = (diagLen μ 0 : ℤ) := by
  rw [Finset.range_eq_Ico, sum_drop_eq _ (Nat.zero_le _), diagLen_rowLen_zero]
  simp

/-! ## The reduction skeleton: what a Lean proof of `M₁ > 0` would still need

Asked directly: can the finite-`n` crossover be closed in Lean? On the current
route, **no**, and the obstruction is worth writing down precisely so nobody
re-derives it.

1. **Mathlib has none of the analytic input.** Its entire Young theory is two
   files — `Combinatorics.Young.YoungDiagram` and `.SemistandardTableau`. There
   is no RSK/Schensted correspondence, no Plancherel measure, no semicircle law,
   no VKLS limit shape, no hook-length formula. Every analytic ingredient this
   route uses would have to be built first.

2. **The margin shrinks exactly where the error terms grow.** Measured, the
   finite-`n` budget rises monotonically toward its limit:

       n         100      200      400      800     limit
       total   0.8799   0.9181   0.9413   0.9597   0.99953
       margin   12 %     8.2 %    5.9 %    4.0 %    0.047 %

   So `M₁ > 0` has comfortable room at every `n` reached, and the route is
   *tightest in the limit*. An effective limit-shape estimate would have to be
   accurate to better than `5·10⁻⁴` relative — in the asymptotic regime, which is
   where such estimates are weakest.

3. **The finite range is not kernel-checkable.** Exact verification reaches
   `n = 60`; the next level has `p(61) = 1121505` partitions carrying ~40-digit
   dimensions.

What IS possible, and is done below, is to formalise the REDUCTION, so that the
missing analytic input is a single named hypothesis rather than prose spread
across a dozen probes. `sum_lt_of_weighted_bound` says: per-edge bounds plus one
aggregate inequality give `N < P`, hence `M₁ > 0`. Every per-edge bound it needs
is already proved in this file — `diagLen_sub_nonneg_le` for same-sign edges and
`diagLen_sub_transpose_le_refined` for opposite-sign ones. What is NOT proved,
and is exactly hypothesis `hagg`, is that the bounds' own weighted average stays
below the total weight. That is the whole remaining gap, in one line. -/

section Reduction

variable {ι : Type*}

/-- **The reduction, with the analytic input isolated.** If every edge's ratio is
bounded by `b e`, and the weights are nonnegative, and the BOUNDS' weighted total
falls short of the total weight, then so does the ratio's — i.e. `N < P`, i.e.
`M₁ > 0`. Everything except `hagg` is per-edge and already proved. -/
theorem sum_lt_of_weighted_bound (E : Finset ι) (w r b : ι → ℚ)
    (hw : ∀ e ∈ E, 0 ≤ w e)
    (hrb : ∀ e ∈ E, r e ≤ b e)
    (hagg : ∑ e ∈ E, w e * b e < ∑ e ∈ E, w e) :
    ∑ e ∈ E, w e * r e < ∑ e ∈ E, w e :=
  lt_of_le_of_lt
    (Finset.sum_le_sum fun e he => mul_le_mul_of_nonneg_left (hrb e he) (hw e he))
    hagg

/-- The same reduction with the two edge classes separated, which is the shape
the route actually has: same-sign edges are bounded by the DENSITY reading, and
opposite-sign ones by the refined telescoping bound. `S` is the same-sign class. -/
theorem sum_lt_of_split_bound [DecidableEq ι] (E S : Finset ι) (w r bs bo : ι → ℚ)
    (hS : S ⊆ E) (hw : ∀ e ∈ E, 0 ≤ w e)
    (hsame : ∀ e ∈ S, r e ≤ bs e)
    (hopp : ∀ e ∈ E \ S, r e ≤ bo e)
    (hagg : (∑ e ∈ S, w e * bs e) + (∑ e ∈ E \ S, w e * bo e) < ∑ e ∈ E, w e) :
    ∑ e ∈ E, w e * r e < ∑ e ∈ E, w e := by
  refine lt_of_le_of_lt ?_ hagg
  rw [← Finset.sum_sdiff hS (f := fun e => w e * r e), add_comm]
  exact add_le_add
    (Finset.sum_le_sum fun e he =>
      mul_le_mul_of_nonneg_left (hsame e he) (hw e (hS he)))
    (Finset.sum_le_sum fun e he =>
      mul_le_mul_of_nonneg_left (hopp e he) (hw e (Finset.mem_sdiff.mp he).1))

end Reduction

end QOU.BraidKnot.M1EdgeCalculus
