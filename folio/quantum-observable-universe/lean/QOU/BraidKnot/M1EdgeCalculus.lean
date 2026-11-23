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

-- Ref: [leitner2026] qou-k5r5, qou-t6hc
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

/-- **Same-sign edge numerator bound (division-free, `qou-t6hc`).**
On any oriented same-sign Fulman edge (`a < r`), the `N`-term factor
`2(D(a) - D(r) + 1)` is bounded below by `2` and above by `4(r - a)`, i.e.
the per-edge ratio `2(D(a) - D(r) + 1)/(r - a)` is at most `4` on all
same-sign moves. -/
theorem same_sign_edge_num_bounds {a r : ℕ} (h : a < r) :
    2 ≤ 2 * ((diagLen μ a : ℤ) - (diagLen μ r : ℤ) + 1) ∧
      2 * ((diagLen μ a : ℤ) - (diagLen μ r : ℤ) + 1) ≤ 4 * ((r : ℤ) - (a : ℤ)) := by
  have hbounds := diagLen_sub_nonneg_le μ (Nat.le_of_lt h)
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

/-- The diagonals are disjoint and sit inside the diagram, so any initial run of
them accounts for at most all `n` cells. This is what turns
`diagLen_area_bound`'s partial sum into the area constraint `... ≤ n`. -/
theorem sum_diagLen_le_card (T : ℕ) :
    ∑ c ∈ Finset.range T, diagLen μ c ≤ μ.card := by
  classical
  have hcard : ∑ c ∈ Finset.range T, diagLen μ c
      = ((Finset.range T).sigma fun c => diagIdx μ c).card := (Finset.card_sigma _ _).symm
  rw [hcard]
  refine Finset.card_le_card_of_injOn (fun p => (p.2, p.2 + p.1)) ?_ ?_
  · rintro ⟨c, i⟩ hp
    simp only [Finset.mem_coe, Finset.mem_sigma] at hp
    simp only [Finset.mem_coe, YoungDiagram.mem_cells, YoungDiagram.mem_iff_lt_rowLen]
    have h2 := hp.2
    rw [mem_diagIdx] at h2
    exact h2.2
  · rintro ⟨c₁, i₁⟩ _ ⟨c₂, i₂⟩ _ h
    simp only [Prod.mk.injEq] at h
    obtain ⟨rfl, h2⟩ := h
    have : c₁ = c₂ := by omega
    subst this
    rfl

/-- **The area constraint, against `n`.** Chaining the two:

    2 a · D a + D a (D a + 1)  ≤  2 n.

Solving that quadratic for `D a` is exactly the bound the quadrature uses,
`D a ≤ √(a² + 2n) - a`, stated here without `Real.sqrt`. In the rescaled
variables of `wlambda_covariance_epic_M1_limit_closed_form.py` this is the
`A = 1` line — the fully deterministic one, needing no limit-shape input at all,
which on its own already takes the budget from failing to a 0.094 % margin. The
7.54 % figure quoted there uses `A_σ → n/2` instead, and that is a limit-shape
input, not this theorem. -/
theorem diagLen_area_bound_card (a : ℕ) :
    2 * (a * diagLen μ a) + diagLen μ a * (diagLen μ a + 1) ≤ 2 * μ.card :=
  le_trans (diagLen_area_bound μ a)
    (Nat.mul_le_mul_left 2 (sum_diagLen_le_card μ _))

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

/-! ## The diagonal decomposition — the area constraint as an EQUALITY

`sum_diagLen_le_card` bounds an initial run of diagonals by `n`. The bound is
lossy by exactly the cells it never reaches, and the loss is nameable: run the
diagonals *both* ways and every cell is hit exactly once.

Cell `(i, j)` has content `j - i`. Split `μ.cells` on `i ≤ j`:

* `i ≤ j` — the cell sits on diagonal `c = j - i ≥ 0` of `μ`, at row `i`;
* `j < i` — the cell sits on diagonal `r = i - j ≥ 1` of `μᵀ`, at row `j`.

Both maps are bijections onto their halves, so the two diagonal sums add to `n`
exactly. Since `diagLen μᵀ 0 = diagLen μ 0`, the symmetric form double-counts the
main diagonal and reads `∑ D + ∑ Dᵀ = n + D 0`.

Why this matters for the `M₁ > 0` budget: the route needs the two one-sided
areas `A₊`, `A₋`, and the *inequality* version can only ever give `A_σ ≤ n`.
The equality gives `A₊ + A₋ + D 0 = n`, which is the finite-`n` statement behind
the `A_σ → n/2` limit-shape input that takes the margin from 0.094 % to 7.54 %. -/

/-- The upper half — cells on or above the main diagonal — swept by diagonals of
`μ`. Any `T` past `λ₁` works, since `diagLen μ c = 0` there. -/
theorem sum_diagLen_eq_card_upper {T : ℕ} (hT : μ.rowLen 0 ≤ T) :
    ∑ c ∈ Finset.range T, diagLen μ c
      = (μ.cells.filter (fun p => p.1 ≤ p.2)).card := by
  classical
  have hcard : ∑ c ∈ Finset.range T, diagLen μ c
      = ((Finset.range T).sigma fun c => diagIdx μ c).card := (Finset.card_sigma _ _).symm
  rw [hcard]
  refine Finset.card_bij' (fun p _ => (p.2, p.2 + p.1)) (fun q _ => ⟨q.2 - q.1, q.1⟩) ?_ ?_ ?_ ?_
  · rintro ⟨c, i⟩ hp
    simp only [Finset.mem_sigma, Finset.mem_range] at hp
    have h2 := hp.2
    rw [mem_diagIdx] at h2
    simp only [Finset.mem_filter, YoungDiagram.mem_cells,
      YoungDiagram.mem_iff_lt_rowLen]
    exact ⟨h2.2, Nat.le_add_right _ _⟩
  · rintro ⟨i, j⟩ hq
    simp only [Finset.mem_filter, YoungDiagram.mem_cells] at hq
    obtain ⟨hmem, hle⟩ := hq
    have hj : j < μ.rowLen i := YoungDiagram.mem_iff_lt_rowLen.mp hmem
    have hi : i < μ.colLen 0 :=
      YoungDiagram.mem_iff_lt_colLen.mp (μ.up_left_mem (le_refl i) (Nat.zero_le j) hmem)
    have hrow : μ.rowLen i ≤ μ.rowLen 0 := μ.rowLen_anti 0 i (Nat.zero_le i)
    simp only [Finset.mem_sigma, Finset.mem_range, mem_diagIdx]
    exact ⟨by omega, hi, by omega⟩
  · rintro ⟨c, i⟩ _
    simp
  · rintro ⟨i, j⟩ hq
    simp only [Finset.mem_filter] at hq
    have hle := hq.2
    simp only [Prod.mk.injEq]
    exact ⟨trivial, by omega⟩

/-- The lower half — cells strictly below the main diagonal — swept by diagonals
`r ≥ 1` of the transpose. -/
theorem sum_diagLen_eq_card_lower {T : ℕ} (hT : μ.colLen 0 ≤ T) :
    ∑ r ∈ Finset.Ico 1 T, diagLen μ.transpose r
      = (μ.cells.filter (fun p => ¬ p.1 ≤ p.2)).card := by
  classical
  have hcard : ∑ r ∈ Finset.Ico 1 T, diagLen μ.transpose r
      = ((Finset.Ico 1 T).sigma fun r => diagIdx μ.transpose r).card :=
    (Finset.card_sigma _ _).symm
  rw [hcard]
  refine Finset.card_bij' (fun p _ => (p.2 + p.1, p.2)) (fun q _ => ⟨q.1 - q.2, q.2⟩) ?_ ?_ ?_ ?_
  · rintro ⟨r, j⟩ hp
    simp only [Finset.mem_sigma, Finset.mem_Ico] at hp
    obtain ⟨⟨hr1, _⟩, h2⟩ := hp
    rw [mem_diagIdx, YoungDiagram.rowLen_transpose] at h2
    simp only [Finset.mem_filter, YoungDiagram.mem_cells,
      YoungDiagram.mem_iff_lt_colLen, not_le]
    exact ⟨h2.2, by omega⟩
  · rintro ⟨i, j⟩ hq
    simp only [Finset.mem_filter, YoungDiagram.mem_cells, not_le] at hq
    obtain ⟨hmem, hlt⟩ := hq
    have hi : i < μ.colLen j := YoungDiagram.mem_iff_lt_colLen.mp hmem
    have hj : j < μ.transpose.colLen 0 := by
      rw [YoungDiagram.colLen_transpose]
      exact YoungDiagram.mem_iff_lt_rowLen.mp (μ.up_left_mem (Nat.zero_le i) (le_refl j) hmem)
    have hcol : μ.colLen j ≤ μ.colLen 0 := μ.colLen_anti 0 j (Nat.zero_le j)
    simp only [Finset.mem_sigma, Finset.mem_Ico, mem_diagIdx,
      YoungDiagram.rowLen_transpose]
    exact ⟨⟨by omega, by omega⟩, hj, by omega⟩
  · rintro ⟨r, j⟩ _
    simp
  · rintro ⟨i, j⟩ hq
    simp only [Finset.mem_filter, not_le] at hq
    have hlt := hq.2
    simp only [Prod.mk.injEq]
    exact ⟨by omega, trivial⟩

/-- **The diagonal decomposition.** Every cell is on exactly one diagonal of `μ`
(content `≥ 0`) or one diagonal `r ≥ 1` of `μᵀ` (content `< 0`). -/
theorem card_eq_sum_diagLen_add {T T' : ℕ} (hT : μ.rowLen 0 ≤ T) (hT' : μ.colLen 0 ≤ T') :
    μ.card = (∑ c ∈ Finset.range T, diagLen μ c)
      + ∑ r ∈ Finset.Ico 1 T', diagLen μ.transpose r := by
  classical
  rw [sum_diagLen_eq_card_upper μ hT, sum_diagLen_eq_card_lower μ hT']
  exact (Finset.filter_card_add_filter_neg_card_eq_card (s := μ.cells) _).symm

/-- The symmetric form: sweeping both ways double-counts the main diagonal. -/
theorem sum_diagLen_add_transpose {T T' : ℕ} (hT : μ.rowLen 0 ≤ T) (hT' : μ.colLen 0 < T') :
    (∑ c ∈ Finset.range T, diagLen μ c) + ∑ r ∈ Finset.range T', diagLen μ.transpose r
      = μ.card + diagLen μ 0 := by
  classical
  have hsplit : ∑ r ∈ Finset.range T', diagLen μ.transpose r
      = diagLen μ.transpose 0 + ∑ r ∈ Finset.Ico 1 T', diagLen μ.transpose r := by
    rw [Finset.range_eq_Ico]
    exact Finset.sum_eq_sum_Ico_succ_bot (by omega) _
  rw [hsplit, diagLen_transpose_zero,
    card_eq_sum_diagLen_add μ hT (le_of_lt hT')]
  ring

/-! ## The two one-sided areas

`A₊` and `A₋` — the cell counts strictly above and strictly below the main
diagonal. These are the `A_σ` of the budget probes. In free-fermion language
(`library/arxiv-1909.06797v5`, `library/arxiv-2105.09342v1`) `A₊ - A₋` is the
first moment of the droplet density about the Fermi point — a **dipole moment**,
one of the conserved charges `Hₙ` — and `D 0` is the droplet's Durfee side. -/

/-- Area strictly above the main diagonal: cells of content `> 0`. -/
def areaUpper : ℕ := ∑ c ∈ Finset.Ico 1 (μ.rowLen 0), diagLen μ c

/-- Area strictly below the main diagonal: cells of content `< 0`. -/
def areaLower : ℕ := ∑ r ∈ Finset.Ico 1 (μ.colLen 0), diagLen μ.transpose r

/-- **The exact area split.** `A₊ + A₋ + D 0 = n`. -/
theorem areaUpper_add_areaLower_add_diagLen_zero :
    areaUpper μ + areaLower μ + diagLen μ 0 = μ.card := by
  classical
  have hup : ∑ c ∈ Finset.range (μ.rowLen 0), diagLen μ c = diagLen μ 0 + areaUpper μ := by
    rcases Nat.eq_zero_or_pos (μ.rowLen 0) with h | h
    · have h0 : diagLen μ 0 = 0 := by
        have := diagLen_le_rowLen_zero_sub μ 0
        omega
      simp [areaUpper, h, h0]
    · rw [Finset.range_eq_Ico]
      exact Finset.sum_eq_sum_Ico_succ_bot h _
  have := card_eq_sum_diagLen_add μ (T := μ.rowLen 0) (T' := μ.colLen 0)
    (le_refl _) (le_refl _)
  rw [hup] at this
  simp only [areaLower] at this ⊢
  omega

/-- Conjugation swaps the two areas. Under any conjugation-invariant measure —
Plancherel is one — this is what forces `E[A₊] = E[A₋]`, hence
`E[A_σ] = (n - E[D 0])/2 < n/2` unconditionally. -/
theorem areaUpper_transpose : areaUpper μ.transpose = areaLower μ := by
  simp only [areaUpper, areaLower, YoungDiagram.rowLen_transpose]

/-- The other direction, via `μᵀᵀ = μ`. -/
theorem areaLower_transpose : areaLower μ.transpose = areaUpper μ := by
  simp only [areaUpper, areaLower, YoungDiagram.colLen_transpose,
    YoungDiagram.transpose_transpose]

/-- **`2 A₊ ≤ n` is exactly "the dipole moment is bounded by the Durfee side".**

Stated as an `iff` deliberately: the left side is FALSE pointwise — the one-row
diagram `(n)` has `A₊ = n - 1`, `A₋ = 0`, `D 0 = 1` — so `A_σ ≤ n/2` can only
ever hold *in expectation*, and any route that needs it must average. This is
the reformulation that says what the average has to control: not an area, but
the imbalance between the two halves. -/
theorem two_mul_areaUpper_le_card_iff :
    2 * areaUpper μ ≤ μ.card
      ↔ (areaUpper μ : ℤ) - (areaLower μ : ℤ) ≤ (diagLen μ 0 : ℤ) := by
  have h := areaUpper_add_areaLower_add_diagLen_zero μ
  constructor
  · intro hle; omega
  · intro hle; push_cast at hle; omega

/-! ## Hook lengths, and where `Sum h` loses a half power of `n`

Measured in `computations/deltalambda/wlambda_covariance_epic_M1_kappa_structure.py`:
`sd(Sum_cells c^2) ~ n^(3/2)` but `sd(Sum_cells h) ~ n^1`. The leading
fluctuation term of the hook sum VANISHES — that is the "`Sum h` is not in the
Kerov–Olshanski algebra" wall of gap `qou-k5r5`, showing up as a scaling
exponent rather than as an algebraic obstruction.

This section proves *where it goes*, exactly and at every `n`:

    2 * Sum_cells h  =  Sum_i (rowLen i)^2  +  Sum_j (colLen j)^2

so `Sum h` is the conjugation-SYMMETRIC combination of two statistics that each
fluctuate at order `n` and are ~96 % ANTI-correlated (measured). The
symmetrisation is what costs the half power. Nothing here is asymptotic; this
identity is what the asymptotic statement is about. -/

/-- Summing over the diagram, grouped by rows. Any `C` past the last nonempty
row works. -/
theorem sum_cells_eq_sum_rows {M : Type*} [AddCommMonoid M] (f : ℕ → ℕ → M)
    {C : ℕ} (hC : μ.colLen 0 ≤ C) :
    ∑ p ∈ μ.cells, f p.1 p.2
      = ∑ i ∈ Finset.range C, ∑ j ∈ Finset.range (μ.rowLen i), f i j := by
  classical
  rw [Finset.sum_sigma']
  refine Finset.sum_nbij' (fun p => (⟨p.1, p.2⟩ : Σ _ : ℕ, ℕ))
    (fun q => (q.1, q.2)) ?_ ?_ (fun _ _ => rfl) (fun _ _ => rfl) (fun _ _ => rfl)
  · rintro ⟨i, j⟩ hp
    simp only [YoungDiagram.mem_cells] at hp
    have hj : j < μ.rowLen i := YoungDiagram.mem_iff_lt_rowLen.mp hp
    have hi : i < μ.colLen 0 :=
      YoungDiagram.mem_iff_lt_colLen.mp (μ.up_left_mem (le_refl i) (Nat.zero_le j) hp)
    simp only [Finset.mem_sigma, Finset.mem_range]
    exact ⟨by omega, hj⟩
  · rintro ⟨i, j⟩ hq
    simp only [Finset.mem_sigma, Finset.mem_range] at hq
    simp only [YoungDiagram.mem_cells, YoungDiagram.mem_iff_lt_rowLen]
    exact hq.2

/-- Transposing swaps the coordinates of every cell. -/
theorem sum_cells_transpose {M : Type*} [AddCommMonoid M] (f : ℕ → ℕ → M) :
    ∑ p ∈ μ.transpose.cells, f p.1 p.2 = ∑ p ∈ μ.cells, f p.2 p.1 := by
  classical
  refine Finset.sum_nbij' (fun p => (p.2, p.1)) (fun q => (q.2, q.1)) ?_ ?_
    (fun _ _ => rfl) (fun _ _ => rfl) (fun _ _ => rfl)
  · rintro ⟨i, j⟩ hp
    simpa only [YoungDiagram.mem_cells, YoungDiagram.mem_transpose] using hp
  · rintro ⟨i, j⟩ hq
    simpa only [YoungDiagram.mem_cells, YoungDiagram.mem_transpose] using hq

/-- Columns past `λ₁` are empty. -/
theorem colLen_eq_zero_of_le {j : ℕ} (h : μ.rowLen 0 ≤ j) : μ.colLen j = 0 := by
  by_contra hne
  have hpos : 0 < μ.colLen j := Nat.pos_of_ne_zero hne
  have : (0, j) ∈ μ := YoungDiagram.mem_iff_lt_colLen.mpr hpos
  have := YoungDiagram.mem_iff_lt_rowLen.mp this
  omega

/-- The hook length of a cell: arm + leg + 1, written so both `ℕ` subtractions
are valid on the diagram (`j < rowLen i` and `i < colLen j` there). -/
def hookLen (i j : ℕ) : ℕ := (μ.rowLen i - j) + (μ.colLen j - i - 1)

/-- `2 ∑_{j<L} (L - j) = L(L+1)` — the arm part of a row. -/
private theorem two_mul_row_arm (L : ℕ) :
    2 * ∑ j ∈ Finset.range L, (L - j) = L * L + L := by
  rw [two_mul_sum_range_sub L]; ring

/-- `2 ∑_{i<L} (L - i - 1) + L = L²` — the leg part of a column, stated without
a subtraction on the right so the aggregate step stays linear. -/
private theorem two_mul_col_leg (L : ℕ) :
    2 * ∑ i ∈ Finset.range L, (L - i - 1) + L = L * L := by
  have h : ∑ i ∈ Finset.range L, (L - i - 1) = ∑ i ∈ Finset.range L, i := by
    refine Finset.sum_nbij' (fun i => L - i - 1) (fun i => L - i - 1) ?_ ?_ ?_ ?_
      (fun _ _ => rfl) <;>
      · intro a ha
        simp only [Finset.mem_range] at ha ⊢
        omega
  rw [h, mul_comm, Finset.sum_range_id_mul_two L]
  cases L with
  | zero => simp
  | succ k => simp only [Nat.succ_sub_one]; ring

/-- **The hook sum is the conjugation-symmetric combination.**

    2 * Sum_cells h = Sum_i (rowLen i)² + Sum_j (colLen j)²

Row `i` contributes `rowLen i (rowLen i + 1)/2` of arm, column `j` contributes
`colLen j (colLen j - 1)/2` of leg; the two linear terms are each `n` and cancel.
Equivalently `Sum h = (Sum λᵢ² + Sum λ'ⱼ²)/2`, which is the statement measured
as ~96 % anti-correlated in the probe. -/
theorem two_mul_sum_hookLen {C R : ℕ} (hC : μ.colLen 0 ≤ C) (hR : μ.rowLen 0 ≤ R) :
    2 * ∑ p ∈ μ.cells, hookLen μ p.1 p.2
      = (∑ i ∈ Finset.range C, μ.rowLen i * μ.rowLen i)
        + ∑ j ∈ Finset.range R, μ.colLen j * μ.colLen j := by
  classical
  -- arm and leg totals, grouped by rows and by columns respectively
  have harm : ∑ p ∈ μ.cells, (μ.rowLen p.1 - p.2)
      = ∑ i ∈ Finset.range C, ∑ j ∈ Finset.range (μ.rowLen i), (μ.rowLen i - j) :=
    sum_cells_eq_sum_rows μ (fun i j => μ.rowLen i - j) hC
  have hlegR : ∑ p ∈ μ.cells, (μ.colLen p.2 - p.1 - 1)
      = ∑ j ∈ Finset.range (μ.rowLen 0),
          ∑ i ∈ Finset.range (μ.colLen j), (μ.colLen j - i - 1) := by
    have h1 := sum_cells_transpose μ (fun a b => μ.colLen a - b - 1)
    have h2 := sum_cells_eq_sum_rows μ.transpose (fun a b => μ.colLen a - b - 1)
      (le_of_eq (μ.colLen_transpose 0))
    simp only [YoungDiagram.rowLen_transpose] at h2
    rw [← h1, h2]
  -- widen the column range from λ₁ to R: those columns are empty
  have hwiden : ∀ (g : ℕ → ℕ), (∀ j, μ.rowLen 0 ≤ j → g j = 0) →
      ∑ j ∈ Finset.range (μ.rowLen 0), g j = ∑ j ∈ Finset.range R, g j := by
    intro g hg
    refine Finset.sum_subset
      (fun x hx => Finset.mem_range.mpr (lt_of_lt_of_le (Finset.mem_range.mp hx) hR)) ?_
    intro x hx hnx
    simp only [Finset.mem_range] at hx hnx
    exact hg x (by omega)
  have hleg : ∑ p ∈ μ.cells, (μ.colLen p.2 - p.1 - 1)
      = ∑ j ∈ Finset.range R, ∑ i ∈ Finset.range (μ.colLen j), (μ.colLen j - i - 1) := by
    rw [hlegR]
    exact hwiden _ (fun j hj => by simp [colLen_eq_zero_of_le μ hj])
  have hcol : ∑ j ∈ Finset.range (μ.rowLen 0), μ.colLen j
      = ∑ j ∈ Finset.range R, μ.colLen j :=
    hwiden _ (fun j hj => colLen_eq_zero_of_le μ hj)
  -- the two "n"s that cancel
  have hn : ∑ i ∈ Finset.range C, μ.rowLen i = μ.card := by
    have h := sum_cells_eq_sum_rows μ (fun _ _ => (1 : ℕ)) hC
    simp only [Finset.sum_const, Finset.card_range, smul_eq_mul, mul_one] at h
    rw [← h, YoungDiagram.card, Finset.card_eq_sum_ones]
  have hn' : ∑ j ∈ Finset.range R, μ.colLen j = μ.card := by
    have h1 := sum_cells_transpose μ (fun _ _ => (1 : ℕ))
    have h2 := sum_cells_eq_sum_rows μ.transpose (fun _ _ => (1 : ℕ))
      (le_of_eq (μ.colLen_transpose 0))
    simp only [YoungDiagram.rowLen_transpose, Finset.sum_const, Finset.card_range,
      smul_eq_mul, mul_one] at h1 h2
    rw [← hcol, ← h2, h1]
  -- per-row / per-column closed forms
  have e1 : ∑ i ∈ Finset.range C, (2 * ∑ j ∈ Finset.range (μ.rowLen i), (μ.rowLen i - j))
      = (∑ i ∈ Finset.range C, μ.rowLen i * μ.rowLen i) + μ.card := by
    simp only [two_mul_row_arm]
    rw [Finset.sum_add_distrib, hn]
  have e2 : ∑ j ∈ Finset.range R, (2 * ∑ i ∈ Finset.range (μ.colLen j), (μ.colLen j - i - 1))
        + μ.card
      = ∑ j ∈ Finset.range R, μ.colLen j * μ.colLen j := by
    rw [← hn', ← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun j _ => two_mul_col_leg (μ.colLen j)
  have hsplit : ∑ p ∈ μ.cells, hookLen μ p.1 p.2
      = (∑ p ∈ μ.cells, (μ.rowLen p.1 - p.2))
        + ∑ p ∈ μ.cells, (μ.colLen p.2 - p.1 - 1) := by
    rw [← Finset.sum_add_distrib]; rfl
  rw [← Finset.mul_sum] at e1 e2
  rw [hsplit, Nat.mul_add, harm, hleg]
  omega

/-- `2 ∑_cells j + n = ∑_i (rowLen i)²` — the column coordinate, summed. -/
private theorem two_mul_sum_snd {C : ℕ} (hC : μ.colLen 0 ≤ C) :
    2 * ∑ p ∈ μ.cells, p.2 + ∑ i ∈ Finset.range C, μ.rowLen i
      = ∑ i ∈ Finset.range C, μ.rowLen i * μ.rowLen i := by
  classical
  have h := sum_cells_eq_sum_rows μ (fun _ j => j) hC
  rw [h, Finset.mul_sum, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun i _ => ?_
  show 2 * ∑ j ∈ Finset.range (μ.rowLen i), j + μ.rowLen i
      = μ.rowLen i * μ.rowLen i
  have hg : (∑ j ∈ Finset.range (μ.rowLen i), j) * 2
      = μ.rowLen i * (μ.rowLen i - 1) := Finset.sum_range_id_mul_two _
  cases hL : μ.rowLen i with
  | zero => simp
  | succ k =>
    rw [hL] at hg
    simp only [Nat.succ_sub_one] at hg
    have hr : (k + 1) * (k + 1) = (k + 1) * k + (k + 1) := by ring
    omega

/-- **`∑_cells h = ∑_cells (i + j + 1)`.**

The hook sum equals the sum of the "anti-diagonal" coordinate. This is the
single-diagram form of the growth-chain step used in
`wlambda_covariance_epic_M1_kappa_structure.py`: adding a box at `(r, s)` raises
`∑ h` by exactly `1 + r + s`, because the new cell has hook `1` and every cell
left of it in its row and above it in its column gains exactly one. Summing that
over a standard Young tableau gives a path sum that must be path-INDEPENDENT —
and this is why: it is just `∑_cells (i + j + 1)` of the final shape.

It implies `two_mul_sum_hookLen`, since `∑ i = n(λ)` and `∑ j = n(λ')`. -/
theorem sum_hookLen_eq_sum_coords {C R : ℕ} (hC : μ.colLen 0 ≤ C) (hR : μ.rowLen 0 ≤ R) :
    ∑ p ∈ μ.cells, hookLen μ p.1 p.2 = ∑ p ∈ μ.cells, (p.1 + p.2 + 1) := by
  classical
  have hn : ∑ i ∈ Finset.range C, μ.rowLen i = μ.card := by
    have h := sum_cells_eq_sum_rows μ (fun _ _ => (1 : ℕ)) hC
    simp only [Finset.sum_const, Finset.card_range, smul_eq_mul, mul_one] at h
    rw [← h, YoungDiagram.card, Finset.card_eq_sum_ones]
  have hn' : ∑ j ∈ Finset.range R, μ.colLen j = μ.card := by
    have h1 := sum_cells_transpose μ (fun _ _ => (1 : ℕ))
    have h2 := sum_cells_eq_sum_rows μ.transpose (fun _ _ => (1 : ℕ))
      (le_of_eq (μ.colLen_transpose 0))
    simp only [YoungDiagram.rowLen_transpose, Finset.sum_const, Finset.card_range,
      smul_eq_mul, mul_one] at h1 h2
    have hw : ∑ j ∈ Finset.range (μ.rowLen 0), μ.colLen j
        = ∑ j ∈ Finset.range R, μ.colLen j := by
      refine Finset.sum_subset
        (fun x hx => Finset.mem_range.mpr (lt_of_lt_of_le (Finset.mem_range.mp hx) hR)) ?_
      intro x _ hnx
      simp only [Finset.mem_range] at hnx
      exact colLen_eq_zero_of_le μ (by omega)
    rw [← hw, ← h2, h1]
  -- the two coordinate sums
  have hsnd := two_mul_sum_snd μ hC
  have hfst : 2 * ∑ p ∈ μ.cells, p.1 + ∑ j ∈ Finset.range R, μ.colLen j
      = ∑ j ∈ Finset.range R, μ.colLen j * μ.colLen j := by
    have hsw := sum_cells_transpose μ (fun _ b => b)
    have ht := two_mul_sum_snd μ.transpose (C := R) (by rwa [YoungDiagram.colLen_transpose])
    simp only [YoungDiagram.rowLen_transpose] at ht
    rw [← hsw]
    exact ht
  have hcard : ∑ p ∈ μ.cells, (1 : ℕ) = μ.card := by
    rw [YoungDiagram.card, Finset.card_eq_sum_ones]
  have hsplit : ∑ p ∈ μ.cells, (p.1 + p.2 + 1)
      = (∑ p ∈ μ.cells, p.1) + (∑ p ∈ μ.cells, p.2) + ∑ p ∈ μ.cells, (1 : ℕ) := by
    rw [← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
  have hhook := two_mul_sum_hookLen μ hC hR
  rw [hn] at hsnd
  rw [hn'] at hfst
  rw [hsplit, hcard]
  omega

/-! ## The diagonal form of the hook sum — where the `|u|` cancellation lives

`sum_hookLen_eq_sum_coords` says `∑ h = ∑ (i + j + 1)`. Resolving that down each
diagonal is what makes the Kerov computation of `κ` work, so it is worth having
exactly rather than asymptotically.

A cell on diagonal `c ≥ 0` at depth `k` is `(k, k + c)`, so `i + j + 1 = 2k + c + 1`,
and summing over `k < D c` gives `D c ² + c · D c`. Hence

    ∑_cells h  =  ∑_c D(c)²  +  ∑_c |c| · D(c)

(both sums over all integer diagonals, the negative ones read off the transpose).

Why it matters. In the continuum `D(c) = (√n/2)(ν̂(u) − |u|)` with `u = c/√n`,
so the first sum is `(n^{3/2}/4) ∫ (ν̂ − |u|)²` and the second
`(n^{3/2}/2) ∫ |u| (ν̂ − |u|)`. Under Kerov's `ν̂ = Ω + (2/√n) Δ` the
FIRST-ORDER parts are `n ∫ (Ω − |u|) Δ` and `n ∫ |u| Δ`, and the `|u|` CANCELS:

    ∑ h − E[∑ h]  ≈  n ∫ Ω(u) Δ(u) du.

That cancellation is the whole reason `∑ h` fluctuates at order `n` rather than
`n^{3/2}`, and it is what reduces `κ`'s sign to the single Fourier coefficient
`f₃ = ∫₀^π (cos t (π/2 − t) + sin t) sin t sin 3t dt = 16/75 > 0`, giving
`κ = (8/3π²)(16/75) = 128/(225π²)`. See
`computations/deltalambda/wlambda_covariance_epic_M1_kappa_derivation.py`. -/

/-- Summing over the cells on or above the main diagonal, grouped by diagonal.
Cell `k` of diagonal `c` is `(k, k + c)`. -/
theorem sum_cells_upper_eq_sum_diag {M : Type*} [AddCommMonoid M] (f : ℕ → ℕ → M)
    {T : ℕ} (hT : μ.rowLen 0 ≤ T) :
    ∑ p ∈ μ.cells.filter (fun p => p.1 ≤ p.2), f p.1 p.2
      = ∑ c ∈ Finset.range T, ∑ k ∈ Finset.range (diagLen μ c), f k (k + c) := by
  classical
  rw [Finset.sum_sigma']
  refine Finset.sum_nbij' (fun p => (⟨p.2 - p.1, p.1⟩ : Σ _ : ℕ, ℕ))
    (fun q => (q.2, q.2 + q.1)) ?_ ?_ ?_ ?_ ?_
  · rintro ⟨i, j⟩ hq
    simp only [Finset.mem_filter, YoungDiagram.mem_cells] at hq
    obtain ⟨hmem, hle⟩ := hq
    have hj : j < μ.rowLen i := YoungDiagram.mem_iff_lt_rowLen.mp hmem
    have hi : i < μ.colLen 0 :=
      YoungDiagram.mem_iff_lt_colLen.mp (μ.up_left_mem (le_refl i) (Nat.zero_le j) hmem)
    have hrow : μ.rowLen i ≤ μ.rowLen 0 := μ.rowLen_anti 0 i (Nat.zero_le i)
    simp only [Finset.mem_sigma, Finset.mem_range, ← diagIdx_eq_range, mem_diagIdx]
    exact ⟨by omega, hi, by omega⟩
  · rintro ⟨c, k⟩ hp
    simp only [Finset.mem_sigma, Finset.mem_range, ← diagIdx_eq_range, mem_diagIdx] at hp
    simp only [Finset.mem_filter, YoungDiagram.mem_cells, YoungDiagram.mem_iff_lt_rowLen]
    exact ⟨hp.2.2, Nat.le_add_right _ _⟩
  · rintro ⟨i, j⟩ hq
    simp only [Finset.mem_filter] at hq
    have hle := hq.2
    simp only [Prod.mk.injEq]
    exact ⟨trivial, by omega⟩
  · rintro ⟨c, k⟩ _
    simp
  · rintro ⟨i, j⟩ hq
    simp only [Finset.mem_filter] at hq
    have hle := hq.2
    have he : i + (j - i) = j := by omega
    show f i j = f i (i + (j - i))
    rw [he]

/-- `∑_{k < d} (2k + c + 1) = d² + c·d` — one diagonal's contribution to
`∑ (i + j + 1)`. -/
private theorem sum_diag_coord (d c : ℕ) :
    ∑ k ∈ Finset.range d, (2 * k + c + 1) = d * d + c * d := by
  have hs : ∑ k ∈ Finset.range d, (2 * k + c + 1)
      = (∑ k ∈ Finset.range d, 2 * k) + ∑ k ∈ Finset.range d, (c + 1) := by
    rw [← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun k _ => by ring
  rw [hs, ← Finset.mul_sum, Finset.sum_const, Finset.card_range, smul_eq_mul]
  have hg : (∑ k ∈ Finset.range d, k) * 2 = d * (d - 1) := Finset.sum_range_id_mul_two d
  cases d with
  | zero => simp
  | succ k =>
    simp only [Nat.succ_sub_one] at hg
    have h1 : (k + 1) * (k + 1) = (k + 1) * k + (k + 1) := by ring
    have h2 : (k + 1) * (c + 1) = c * (k + 1) + (k + 1) := by ring
    omega

/-- The mirror of `sum_cells_upper_eq_sum_diag` below the main diagonal: cell
`k` of transpose-diagonal `r ≥ 1` is `(k + r, k)`. -/
theorem sum_cells_lower_eq_sum_diag {M : Type*} [AddCommMonoid M] (f : ℕ → ℕ → M)
    {T : ℕ} (hT : μ.colLen 0 ≤ T) :
    ∑ p ∈ μ.cells.filter (fun p => ¬ p.1 ≤ p.2), f p.1 p.2
      = ∑ r ∈ Finset.Ico 1 T, ∑ k ∈ Finset.range (diagLen μ.transpose r), f (k + r) k := by
  classical
  rw [Finset.sum_sigma']
  refine Finset.sum_nbij' (fun p => (⟨p.1 - p.2, p.2⟩ : Σ _ : ℕ, ℕ))
    (fun q => (q.2 + q.1, q.2)) ?_ ?_ ?_ ?_ ?_
  · rintro ⟨i, j⟩ hq
    simp only [Finset.mem_filter, YoungDiagram.mem_cells, not_le] at hq
    obtain ⟨hmem, hlt⟩ := hq
    have hi : i < μ.colLen j := YoungDiagram.mem_iff_lt_colLen.mp hmem
    have hj : j < μ.transpose.colLen 0 := by
      rw [YoungDiagram.colLen_transpose]
      exact YoungDiagram.mem_iff_lt_rowLen.mp (μ.up_left_mem (Nat.zero_le i) (le_refl j) hmem)
    have hcol : μ.colLen j ≤ μ.colLen 0 := μ.colLen_anti 0 j (Nat.zero_le j)
    simp only [Finset.mem_sigma, Finset.mem_Ico, ← diagIdx_eq_range, mem_diagIdx,
      YoungDiagram.rowLen_transpose]
    exact ⟨⟨by omega, by omega⟩, hj, by omega⟩
  · rintro ⟨r, k⟩ hp
    simp only [Finset.mem_sigma, Finset.mem_Ico, ← diagIdx_eq_range, mem_diagIdx,
      YoungDiagram.rowLen_transpose] at hp
    obtain ⟨⟨hr1, _⟩, h2⟩ := hp
    simp only [Finset.mem_filter, YoungDiagram.mem_cells,
      YoungDiagram.mem_iff_lt_colLen, not_le]
    exact ⟨h2.2, by omega⟩
  · rintro ⟨i, j⟩ hq
    simp only [Finset.mem_filter, not_le] at hq
    have hlt := hq.2
    simp only [Prod.mk.injEq]
    exact ⟨by omega, trivial⟩
  · rintro ⟨r, k⟩ _
    simp
  · rintro ⟨i, j⟩ hq
    simp only [Finset.mem_filter, not_le] at hq
    have hlt := hq.2
    have he : j + (i - j) = i := by omega
    show f i j = f (j + (i - j)) j
    rw [he]

/-- **The diagonal form of the hook sum.**

    ∑_cells h  =  ∑_{c ≥ 0} (D c² + c · D c)  +  ∑_{r ≥ 1} (Dᵀ r² + r · Dᵀ r)

i.e. `∑ h = ∑_c D(c)² + ∑_c |c| D(c)` over all integer diagonals. Combined with
`sum_hookLen_eq_sum_coords`, this is the exact statement behind the `|u|`
cancellation that makes `∑ h` fluctuate at order `n` rather than `n^{3/2}` —
see the section header. -/
theorem sum_hookLen_eq_diag {C R T T' : ℕ} (hC : μ.colLen 0 ≤ C) (hR : μ.rowLen 0 ≤ R)
    (hT : μ.rowLen 0 ≤ T) (hT' : μ.colLen 0 ≤ T') :
    ∑ p ∈ μ.cells, hookLen μ p.1 p.2
      = (∑ c ∈ Finset.range T, (diagLen μ c * diagLen μ c + c * diagLen μ c))
        + ∑ r ∈ Finset.Ico 1 T', (diagLen μ.transpose r * diagLen μ.transpose r
            + r * diagLen μ.transpose r) := by
  classical
  have hup : ∑ p ∈ μ.cells.filter (fun p => p.1 ≤ p.2), (p.1 + p.2 + 1)
      = ∑ c ∈ Finset.range T, (diagLen μ c * diagLen μ c + c * diagLen μ c) := by
    rw [sum_cells_upper_eq_sum_diag μ (fun i j => i + j + 1) hT]
    refine Finset.sum_congr rfl fun c _ => ?_
    rw [← sum_diag_coord (diagLen μ c) c]
    exact Finset.sum_congr rfl fun k _ => by omega
  have hlo : ∑ p ∈ μ.cells.filter (fun p => ¬ p.1 ≤ p.2), (p.1 + p.2 + 1)
      = ∑ r ∈ Finset.Ico 1 T', (diagLen μ.transpose r * diagLen μ.transpose r
          + r * diagLen μ.transpose r) := by
    rw [sum_cells_lower_eq_sum_diag μ (fun i j => i + j + 1) hT']
    refine Finset.sum_congr rfl fun r _ => ?_
    rw [← sum_diag_coord (diagLen μ.transpose r) r]
    exact Finset.sum_congr rfl fun k _ => by omega
  rw [sum_hookLen_eq_sum_coords μ hC hR, ← hup, ← hlo,
    Finset.sum_filter_add_sum_filter_not]

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

/-- **Pointwise slope-plus-gap decomposition of the edge ratio (`qou-t6hc`).**
Splits `2(d_a - d_r + 1) · g⁻¹` into the discrete diagonal slope term
`2(d_a - d_r) · g⁻¹` and the small-gap harmonic term `2 · g⁻¹`. -/
theorem edge_ratio_eq_slope_add_gap (da dr invGap : ℚ) :
    2 * (da - dr + 1) * invGap = 2 * (da - dr) * invGap + 2 * invGap := by
  ring

/-- **Weighted `S + Q` edge-ratio decomposition (`qou-t6hc` leg A).**
Summing `w_e · ratio_e` over the edge set `E` splits identically into the
weighted slope sum `S` plus the weighted inverse-gap sum `Q`, matching the exact
control identity `S(n) + Q(n) = N(n)/P(n)` of
`wlambda_covariance_epic_M1_edge_ratio_decomposition.py`. -/
theorem weighted_edge_ratio_eq_slope_add_gap (E : Finset ι) (w da dr invGap : ι → ℚ) :
    ∑ e ∈ E, w e * (2 * (da e - dr e + 1) * invGap e)
      = (∑ e ∈ E, w e * (2 * (da e - dr e) * invGap e))
        + (∑ e ∈ E, w e * (2 * invGap e)) := by
  rw [← Finset.sum_add_distrib]
  exact Finset.sum_congr rfl fun e _ => by ring

/-- **Domination `N < P` from separate `S` and `Q` bounds (`qou-t6hc`).**
If the weighted slope term is bounded by `S_bound` and the weighted small-gap
term is bounded by `Q_bound` with `S_bound + Q_bound < ∑_{e ∈ E} w_e`, then
`N < P` (`∑_{e ∈ E} w_e · ratio_e < ∑_{e ∈ E} w_e`). -/
theorem sum_edge_ratio_lt_of_slope_and_gap_bounds (E : Finset ι)
    (w da dr invGap : ι → ℚ) {S_bound Q_bound : ℚ}
    (hS : ∑ e ∈ E, w e * (2 * (da e - dr e) * invGap e) ≤ S_bound)
    (hQ : ∑ e ∈ E, w e * (2 * invGap e) ≤ Q_bound)
    (hsum : S_bound + Q_bound < ∑ e ∈ E, w e) :
    ∑ e ∈ E, w e * (2 * (da e - dr e + 1) * invGap e) < ∑ e ∈ E, w e := by
  have hdecomp := weighted_edge_ratio_eq_slope_add_gap E w da dr invGap
  linarith

end Reduction

/-! ## Covariance: the two steps the `kappa` argument actually needs

`computations/deltalambda/wlambda_covariance_epic_M1_kappa_structure.py` makes
two claims that are *logical*, not analytic, and so belong here rather than in a
probe. Neither is deep; both are load-bearing, and writing them down is what
separates them from the measured claims they sit next to.

FINDING 1 there uses the classical hook-content identity
`Sum_cells h^2 = Sum_cells c^2 + n^2` (verified on all 914 partitions of
`n <= 16`, with a control) to conclude

    M_1 = Cov(Sum h, Sum c^2) = Cov(Sum h, Sum h^2)   at every n.

The step from the identity to that conclusion is `cov_add_const`: `n^2` is
deterministic, so shifting one argument by a constant leaves the covariance
alone.

FINDING 5 concludes that `kappa > 0` is equivalent to a CORRELATION sign,
because `kappa = rho * sigma_h * sigma_c` and the two sigmas are standard
deviations, hence positive. That is `cov_pos_iff_corr_pos`. It is trivial
mathematically — and it is the whole reduction: what `qou-k5r5` needs for the
sign is not the value of `kappa`, and not Sniady's genus expansion, but that two
hook statistics are positively correlated. The measurement says the correlation
is asymptotically 1, not merely positive.

What is NOT here, and cannot be: `sigma_c = 1/sqrt(3)` needs Kerov's CLT, and
Mathlib has no Plancherel measure — its entire Young theory is two files. -/

section Covariance

variable {ι : Type*}

/-- Covariance of two observables under a finite weight. Stated for a weight
that sums to `1`, which is how the edge measure is normalised. -/
def cov (E : Finset ι) (w X Y : ι → ℚ) : ℚ :=
  (∑ i ∈ E, w i * X i * Y i) - (∑ i ∈ E, w i * X i) * (∑ i ∈ E, w i * Y i)

/-- **Covariance ignores a deterministic shift.** With `Sum h^2 = Sum c^2 + n^2`
and `n` deterministic, this is exactly the step
`Cov(Sum h, Sum c^2) = Cov(Sum h, Sum h^2)`. -/
theorem cov_add_const (E : Finset ι) (w X Y : ι → ℚ) (hw : ∑ i ∈ E, w i = 1) (k : ℚ) :
    cov E w X (fun i => Y i + k) = cov E w X Y := by
  have h1 : ∑ i ∈ E, w i * X i * (Y i + k)
      = (∑ i ∈ E, w i * X i * Y i) + k * ∑ i ∈ E, w i * X i := by
    rw [Finset.mul_sum, ← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun i _ => by ring
  have h2 : ∑ i ∈ E, w i * (Y i + k) = (∑ i ∈ E, w i * Y i) + k := by
    have h : ∑ i ∈ E, w i * (Y i + k)
        = (∑ i ∈ E, w i * Y i) + k * ∑ i ∈ E, w i := by
      rw [Finset.mul_sum, ← Finset.sum_add_distrib]
      exact Finset.sum_congr rfl fun i _ => by ring
    rw [h, hw]; ring
  simp only [cov, h1, h2]
  ring

/-- **The sign of a covariance is the sign of the correlation.** Trivial, and
it is the whole of the `kappa > 0` reduction: the two normalising factors are
standard deviations, so they cannot change the sign. -/
theorem cov_pos_iff_corr_pos {c sx sy : ℚ} (hx : 0 < sx) (hy : 0 < sy) :
    0 < c / (sx * sy) ↔ 0 < c := by
  have hd : 0 < sx * sy := mul_pos hx hy
  constructor
  · intro h
    have hc : c = c / (sx * sy) * (sx * sy) := (div_mul_cancel₀ c (ne_of_gt hd)).symm
    rw [hc]
    exact mul_pos h hd
  · intro h
    exact div_pos h hd

/-- **Only the `T`-symmetric part of `X` contributes.** If an involution `T`
preserves the weight and fixes `Y`, then `X` may be replaced by `X ∘ T`.

This is the step asserted in `wlambda_covariance_epic_M1_kappa_structure.py`:
Plancherel is conjugation-invariant and `∑ c²` is conjugation-fixed, so
`Cov(∑ λᵢ², ∑ c²) = Cov(∑ (λ'ⱼ)², ∑ c²)` and hence, by
`two_mul_sum_hookLen`, both equal `Cov(∑ h, ∑ c²)`. The antisymmetric part of
`∑ λᵢ²` — which is `∑ c`, by the companion identity — contributes nothing. -/
theorem cov_involution [DecidableEq ι] (E : Finset ι) (T : ι → ι) (w X Y : ι → ℚ)
    (hT : ∀ i ∈ E, T i ∈ E) (hTT : ∀ i ∈ E, T (T i) = i)
    (hw : ∀ i ∈ E, w (T i) = w i) (hY : ∀ i ∈ E, Y (T i) = Y i) :
    cov E w X Y = cov E w (fun i => X (T i)) Y := by
  have reindex : ∀ f : ι → ℚ, ∑ i ∈ E, f (T i) = ∑ i ∈ E, f i := fun f =>
    Finset.sum_nbij' T T hT hT hTT hTT (fun _ _ => rfl)
  have e1 : ∑ i ∈ E, w i * X (T i) * Y i = ∑ i ∈ E, w i * X i * Y i := by
    rw [← reindex (fun i => w i * X i * Y i)]
    exact Finset.sum_congr rfl fun i hi => by rw [hw i hi, hY i hi]
  have e2 : ∑ i ∈ E, w i * X (T i) = ∑ i ∈ E, w i * X i := by
    rw [← reindex (fun i => w i * X i)]
    exact Finset.sum_congr rfl fun i hi => by rw [hw i hi]
  simp only [cov, e1, e2]

/-- The symmetric-part form: averaging `X` with `X ∘ T` changes nothing. -/
theorem cov_eq_cov_symmetrised [DecidableEq ι] (E : Finset ι) (T : ι → ι)
    (w X Y : ι → ℚ) (hT : ∀ i ∈ E, T i ∈ E) (hTT : ∀ i ∈ E, T (T i) = i)
    (hw : ∀ i ∈ E, w (T i) = w i) (hY : ∀ i ∈ E, Y (T i) = Y i) :
    cov E w X Y = cov E w (fun i => (X i + X (T i)) / 2) Y := by
  have h := cov_involution E T w X Y hT hTT hw hY
  simp only [cov] at h ⊢
  have s1 : ∑ i ∈ E, w i * ((X i + X (T i)) / 2) * Y i
      = ((∑ i ∈ E, w i * X i * Y i) + ∑ i ∈ E, w i * X (T i) * Y i) / 2 := by
    rw [← Finset.sum_add_distrib, Finset.sum_div]
    exact Finset.sum_congr rfl fun i _ => by ring
  have s2 : ∑ i ∈ E, w i * ((X i + X (T i)) / 2)
      = ((∑ i ∈ E, w i * X i) + ∑ i ∈ E, w i * X (T i)) / 2 := by
    rw [← Finset.sum_add_distrib, Finset.sum_div]
    exact Finset.sum_congr rfl fun i _ => by ring
  rw [s1, s2]
  linarith [h]

/-! ## The two-regime shape of `qou-k5r5` claim (b), and why it can be weakened

The gap reduces `M₁ > 0` to (a) an exact check for small `n` and (b)
`κ_n ≥ κ` for `n ≥ 13`, with `κ_n = M₁(n)/n^(5/2)` and `κ = 128/(225π²)`.
Measured exactly in `wlambda_covariance_epic_M1_kappa_n_exact.py`: `κ_n` crosses
`κ` at exactly `n = 13`, peaks at `n = 32`, and decreases thereafter, rejoining
`κ` from above.

**Claim (b) is stronger than the goal needs.** `M₁(n) > 0` is equivalent to
`κ_n > 0`, because `n^(5/2) > 0`. So in the tail it is enough to know

    |κ_n − κ| < κ        (b′)

instead of `κ_n ≥ κ`. The difference in what an effective error bound must
deliver is large and measured: over the exactly-computed range `n = 32..42`,
`|κ_n − κ|/κ` runs `0.0270 → 0.0262`, so

* (b) needs the bound to resolve the SIGN of a quantity that is ~2.6 % of `κ`
  — relative accuracy better than 2.6 %;
* (b′) needs only `|κ_n − κ| < κ` — relative accuracy 100 %, a **37×** slacker
  demand.

`pos_of_check_and_tail` below is that argument, and nothing more: a finite exact
check up to `N` plus a crude tail bound past it. It is stated over `ℚ` and over
an arbitrary `f`, because the content is the SHAPE — which regime carries which
burden — not the analysis. The analysis (an effective Kerov error term) is what
remains open. -/

/-- **Positivity from a crude approximation.** If `x` is within `k` of `k` then
`x > 0`. No positivity hypothesis on `k` is needed — `|x - k| < k` already
forces `0 < k`, since the left side is non-negative. It is the whole of the
weakening: an effective bound need only be accurate to within the limit's own
size. -/
theorem pos_of_abs_sub_lt {x k : ℚ} (h : |x - k| < k) : 0 < x := by
  have h1 := (abs_lt.mp h).1
  linarith

/-- **A finite exact check plus a crude tail bound gives positivity throughout.**

This is the exact logical shape of `qou-k5r5` claim (b) once weakened to (b′).
`hfin` is the exactly-computable part (`n₀ ≤ n ≤ N`, done here to `N = 42`);
`htail` is the only analytic input, and it is the crude form. -/
theorem pos_of_check_and_tail {N n₀ : ℕ} {k : ℚ} (f : ℕ → ℚ)
    (hfin : ∀ n, n₀ ≤ n → n ≤ N → 0 < f n)
    (htail : ∀ n, N < n → |f n - k| < k) :
    ∀ n, n₀ ≤ n → 0 < f n := by
  intro n hn
  rcases le_or_gt n N with h | h
  · exact hfin n hn h
  · exact pos_of_abs_sub_lt (htail n h)

end Covariance

end QOU.BraidKnot.M1EdgeCalculus
