/-
# GAP-A-3 ROUTE 4 (beyond-Hecke): can a Habiro-ring FIBRE element supply `r* ≈ 1.585`?

The A=3 (triton) Δ_λ 3-body **magnitude** factor `r* = μ₃ / c₃ ≈ 1.585` is the ratio
between the target additive-residual moment `μ₃ = +0.4708` (`AdditiveResidualSimplex`,
#4320) and the Hecke-level near-miss `c₃ = +0.297` (#4364 `BorromeanMagnitudeLift`, the
`H₉` joint-trace lift of the proved Borromean 3-body cluster). It is already bracketed out
of every Hecke-level ingredient (three-walls 2026-07-26: level / `W_λ` / coordination-edge)
AND out of the finite-type / Vassiliev filtration of the single Borromean deficit
(`VassilievMagnitudeA3.lean`, 2026-08-01, scope-(b): every finite-type weight is `≤` the
Hecke value, and the length-A Milnor weight is the integer `−2`).

This file tests the remaining candidate named by the Vassiliev audit ("structure genuinely
OUTSIDE the finite-type filtration"): a **fibre-level Habiro-ring element**
`F(q) = Σ_n a_n(q) · (q;q)_n` in the cyclotomic completion `ℤ[q]^` — parallel to the proved
α_EM element `[2]_q·(1 − h²α)` (PR #1511) and the Q_β Habiro element. Per the AGENTS.md
"Im(q) at fibre vs observable level" banner, the c_k / magnitude coefficients live in the
FIBRE (formal q-deformation); each q₀ anchor is a different archimedean evaluation of the
SAME fibre object. A REAL closed form `r* = f(q₀)` for smooth real f is already known to fail
(dc₃/dq impossible for smooth real f, PR #1821). The Habiro question is different: is there a
STRUCTURALLY-FORCED (0-fit) cyclotomic-completion element whose archimedean evaluation at the
substrate q₀ reproduces `r*`?

## The decisive obstruction (this file): the substrate anchor is `q₀ > 1`

The Habiro ring `ℤ[q]^ = lim_n ℤ[q]/((q;q)_n)` has canonical evaluations at ROOTS OF UNITY
(where `(q;q)_n` vanishes for `n ≥ ord`, truncating the sum to a finite polynomial) and, more
generally, INSIDE the unit disk `|q| < 1` (where `(q;q)_n → (q;q)_∞` and integer-coefficient
series can converge). The QOU substrate modulus is `q₀ ≈ 1.10998 > 1` — OUTSIDE both loci.

For real `q > 1` the cyclotomic basis magnitude `|(q;q)_n| = ∏_{k=1}^n (q^k − 1)` is
**unbounded** (`pochAbs_unbounded`): the successive factor `q^{n+1} − 1 → ∞`, so from some
index on the partial products at least double each step. Consequently a genuine (infinite)
integer-coefficient Habiro element `Σ a_n (q;q)_n` has terms that do NOT tend to `0`
(`habiro_terms_not_tendsto_zero`) — the series is **not summable at `q > 1`**. So a genuine
cyclotomic-completion element has *no canonical archimedean value at the substrate*; it cannot
supply a well-defined magnitude factor there.

The ONLY Habiro-shape elements with a well-defined evaluation at `q₀ > 1` are the FINITE
(Laurent-polynomial / rational) ones — exactly the α_EM shape `[k]_q·(1 − h²X)`. Those are
governed by the already-established finite-type bracketing (`VassilievMagnitudeA3`): their
value is a quantum integer `[k]_q` times a NEGLIGIBLE correction `(1 − h²X)` (`X` the
categorical deficit, `h²X ≈ 6·10⁻⁵`), and `r* ∈ (3/2, 2)` lies STRICTLY BETWEEN `[1]_{q₀} ≈ 1`
and `[2]_{q₀} ≈ 2.01`, so no integer `k` — and no 0-fit categorical `X` — lands on it. A
quantum-integer ratio near `r*` (best `[6]_q/[4]_q = 1.554`, −1.9%) is a fit-scan match, not a
forced value.

## Verdict — no DERIVED Habiro element reproduces `r*`; two-part honest negative

1. **REFUTE(scope-b)** of "an infinite cyclotomic-completion element evaluates to `r*` at the
   substrate": at `q₀ > 1` the basis magnitude is unbounded, so the series diverges — cited
   invariant `pochAbs_unbounded` (a proved growth/non-summability fact). No well-defined value
   exists, so none can equal `r*`.
2. **WALL(scope-a)** for the finite (Laurent) α_EM-shape sub-case: reduces to the quantum
   integers `[k]_q`; `r*` lies strictly between `[1]_{q₀}` and `[2]_{q₀}`, no derived (0-fit)
   element lands on it (`rStar_strictly_between_q1_q2`). A coefficient tuned to hit `1.585` is
   a FIT, declined.

Nothing is fit; nothing is wired. "No seventh fit-based ansatz" + PROBE-4 KL-prune stand.

-- Ref: [habiro2000] K. Habiro, On the colored Jones polynomials of some simple links,
--   Surikaisekikenkyusho Kokyuroku 1172 (2000) 34–43; [habiro2004] A unified Witten–Reshetikhin–
--   Turaev invariant for integral homology spheres, Invent. Math. 171 (2008) 1–81.
-- Ref: [leitner2026] deltalambda GAP-A-3 ROUTE 4 audit 2026-08-01; habiro_a3_probe.py.
-/
import Mathlib.Tactic
import QOU.MathlibExt.QIntegerCanonical

namespace QOU.MassTheory.HabiroMagnitudeA3

/-! ### 1. The Habiro cyclotomic basis magnitude `|(q;q)_n|` at real `q > 1`

For real `q > 1` we have `1 − q^k < 0`, so `|(q;q)_n| = ∏_{k=1}^n (q^k − 1)`. We work with
this magnitude directly. -/

/-- Magnitude of the cyclotomic Pochhammer `(q;q)_n = ∏_{k=1}^n (1 − q^k)` for real `q > 1`,
where each factor's magnitude is `q^k − 1`. -/
noncomputable def pochAbs (q : ℝ) : ℕ → ℝ
  | 0 => 1
  | n + 1 => pochAbs q n * (q ^ (n + 1) - 1)

@[simp] theorem pochAbs_zero (q : ℝ) : pochAbs q 0 = 1 := rfl

theorem pochAbs_succ (q : ℝ) (n : ℕ) :
    pochAbs q (n + 1) = pochAbs q n * (q ^ (n + 1) - 1) := rfl

/-- Each factor `q^(n+1) − 1` is strictly positive for `q > 1` (since `q^(n+1) ≥ q > 1`). -/
theorem factor_pos (q : ℝ) (hq : 1 < q) (n : ℕ) : 0 < q ^ (n + 1) - 1 := by
  have h1 : (1 : ℝ) < q ^ (n + 1) := one_lt_pow₀ hq (Nat.succ_ne_zero n)
  linarith

/-- The basis magnitude is strictly positive for `q > 1`. -/
theorem pochAbs_pos (q : ℝ) (hq : 1 < q) : ∀ n, 0 < pochAbs q n
  | 0 => by simp
  | n + 1 => by
      rw [pochAbs_succ]
      exact mul_pos (pochAbs_pos q hq n) (factor_pos q hq n)

/-! ### 2. The obstruction: the basis magnitude is UNBOUNDED for `q > 1` -/

/-- For `q > 1` the powers `q^n → ∞`, so eventually `q^n ≥ 3`; concretely there is an index
`N` beyond which every subsequent cyclotomic factor exceeds `2`. -/
theorem exists_factor_ge_two (q : ℝ) (hq : 1 < q) :
    ∃ N, ∀ n, N ≤ n → 2 ≤ q ^ (n + 1) - 1 := by
  have htend : Filter.Tendsto (fun n => q ^ n) Filter.atTop Filter.atTop :=
    tendsto_pow_atTop_atTop_of_one_lt hq
  have : ∀ᶠ n in Filter.atTop, (3 : ℝ) ≤ q ^ n :=
    htend.eventually_ge_atTop 3
  obtain ⟨N, hN⟩ := this.exists_forall_of_atTop
  refine ⟨N, fun n hn => ?_⟩
  have hge : (3 : ℝ) ≤ q ^ (n + 1) := by
    have := hN (n + 1) (le_trans hn (Nat.le_succ n))
    exact this
  linarith

/-- Geometric doubling: once every factor is `≥ 2` (from index `N`), the basis magnitude at
`N + m` is at least `2^m` times its value at `N`. -/
theorem pochAbs_ge_geometric (q : ℝ) (hq : 1 < q) {N : ℕ}
    (hN : ∀ n, N ≤ n → 2 ≤ q ^ (n + 1) - 1) :
    ∀ m, (2 : ℝ) ^ m * pochAbs q N ≤ pochAbs q (N + m)
  | 0 => by simp
  | m + 1 => by
      have ih := pochAbs_ge_geometric q hq hN m
      have hposN : 0 < pochAbs q N := pochAbs_pos q hq N
      have hfac : 2 ≤ q ^ (N + m + 1) - 1 := hN (N + m) (Nat.le_add_right N m)
      have hposNm : 0 < pochAbs q (N + m) := pochAbs_pos q hq (N + m)
      calc (2 : ℝ) ^ (m + 1) * pochAbs q N
            = 2 * (2 ^ m * pochAbs q N) := by ring
        _ ≤ 2 * pochAbs q (N + m) := by linarith
        _ ≤ pochAbs q (N + m) * (q ^ (N + m + 1) - 1) := by nlinarith
        _ = pochAbs q (N + (m + 1)) := by
              rw [show N + (m + 1) = (N + m) + 1 from rfl, pochAbs_succ]

/-- **OBSTRUCTION (the core structural fact).** For real `q > 1` the Habiro cyclotomic basis
magnitude `|(q;q)_n|` is UNBOUNDED: it exceeds any bound `B` at some index. Hence the
cyclotomic-completion series `Σ a_n (q;q)_n` cannot converge at `q > 1` with non-decaying
coefficients — the substrate anchor `q₀ > 1` lies outside the Habiro ring's evaluation locus. -/
theorem pochAbs_unbounded (q : ℝ) (hq : 1 < q) (B : ℝ) : ∃ n, B < pochAbs q n := by
  obtain ⟨N, hN⟩ := exists_factor_ge_two q hq
  have hposN : 0 < pochAbs q N := pochAbs_pos q hq N
  -- pick m with 2^m * pochAbs q N > B
  obtain ⟨m, hm⟩ := pow_unbounded_of_one_lt (max B 0 / pochAbs q N) (by norm_num : (1 : ℝ) < 2)
  refine ⟨N + m, ?_⟩
  have hgeo := pochAbs_ge_geometric q hq hN m
  have hstep : max B 0 / pochAbs q N < (2 : ℝ) ^ m := hm
  have : max B 0 < (2 : ℝ) ^ m * pochAbs q N := by
    rw [div_lt_iff₀ hposN] at hstep; linarith
  have hBle : B ≤ max B 0 := le_max_left _ _
  linarith [hgeo]

/-! ### 3. Divergence at the substrate: cyclotomic-completion terms do not tend to 0 -/

/-- **Term test / non-summability.** A genuine (infinite) integer-coefficient Habiro element
`F(q) = Σ a_n (q;q)_n` with `|a_n| ≥ 1` for all `n` has terms whose magnitude is unbounded at
`q > 1` (each `|a_n · (q;q)_n| ≥ |(q;q)_n|`), so the terms do NOT tend to `0` and the series
diverges. Therefore no well-defined archimedean value exists at the substrate `q₀ > 1`. -/
theorem habiro_terms_not_tendsto_zero (q : ℝ) (hq : 1 < q) (a : ℕ → ℝ)
    (ha : ∀ n, 1 ≤ |a n|) :
    ¬ Filter.Tendsto (fun n => a n * pochAbs q n) Filter.atTop (nhds 0) := by
  intro htend
  -- if it tends to 0 the sequence is bounded; but |a n · pochAbs q n| ≥ pochAbs q n is unbounded
  have habs : Filter.Tendsto (fun n => |a n * pochAbs q n|) Filter.atTop (nhds 0) := by
    simpa using htend.abs
  have hbdd : BddAbove (Set.range fun n => |a n * pochAbs q n|) := habs.bddAbove_range
  obtain ⟨C, hC⟩ := hbdd
  obtain ⟨n, hn⟩ := pochAbs_unbounded q hq C
  have hposn : 0 < pochAbs q n := pochAbs_pos q hq n
  have hge : pochAbs q n ≤ |a n * pochAbs q n| := by
    rw [abs_mul, abs_of_pos hposn]
    have : (1 : ℝ) * pochAbs q n ≤ |a n| * pochAbs q n :=
      mul_le_mul_of_nonneg_right (ha n) (le_of_lt hposn)
    simpa using this
  have hle : |a n * pochAbs q n| ≤ C := hC (Set.mem_range_self n)
  linarith

/-! ### 4. The finite (Laurent) α_EM-shape sub-case: bracketed by the quantum integers -/

/-- Hecke-level near-miss `c₃ = +0.297 MeV` (#4364). Mirrors `VassilievMagnitudeA3.c3bare`. -/
noncomputable def c3bare : ℝ := 297 / 1000

/-- Target additive-residual moment `μ₃ = +0.4708 MeV` (#4320). Mirrors `VassilievMagnitudeA3.mu3`. -/
noncomputable def mu3 : ℝ := 4708 / 10000

/-- The required A=3 magnitude factor `r* = μ₃ / c₃ ≈ 1.585`. -/
noncomputable def rStar : ℝ := mu3 / c3bare

theorem rStar_gt_three_halves : (3 / 2 : ℝ) < rStar := by
  unfold rStar mu3 c3bare; norm_num

theorem rStar_lt_two : rStar < 2 := by
  unfold rStar mu3 c3bare; norm_num

/-- The balanced quantum integer `[n]_q = (q^n − q^{-n})/(q − q^{-1})`, written with real
inverse powers `(q^n)⁻¹ = q^{-n}`. The α_EM-shape finite Habiro element `[k]_q·(1 − h²X)` has
this as its dominant factor (the correction `(1−h²X)` is `≈ 1` for the categorical `X`). -/
noncomputable def qInt (n : ℕ) (q : ℝ) : ℝ := (q ^ n - (q ^ n)⁻¹) / (q - q⁻¹)

/-- **Bridge to the canonical balanced bracket.** The alias was refused — a proof
below needs this literal body, with the inverse written `(q^n)⁻¹` rather than
`q⁻¹^n` — so the consolidation is this equation rather than a substitution. -/
theorem qInt_eq_canonical (n : ℕ) (q : ℝ) :
    qInt n q = QOU.QInteger.qIntBal q n := by
  simp [qInt, QOU.QInteger.qIntBal, QOU.Mass.QHookDimensionBalanced.qIntBal, inv_pow]

/-- `q − q⁻¹ ≠ 0` for `q > 1` (since `q⁻¹ < 1 < q`). -/
theorem denom_ne (q : ℝ) (hq : 1 < q) : q - q⁻¹ ≠ 0 := by
  have hq0 : (0:ℝ) < q := by linarith
  have h1 : q⁻¹ < 1 := by rw [inv_lt_one₀ hq0]; exact hq
  have : q⁻¹ < q := lt_trans h1 hq
  intro h; have := sub_eq_zero.mp h; linarith

/-- `[1]_q = 1` exactly. -/
theorem qInt_one (q : ℝ) (hq : 1 < q) : qInt 1 q = 1 := by
  unfold qInt
  simp only [pow_one]
  exact div_self (denom_ne q hq)

/-- `[2]_q = q + q⁻¹`. -/
theorem qInt_two (q : ℝ) (hq : 1 < q) : qInt 2 q = q + q⁻¹ := by
  unfold qInt
  have hq0 : (0:ℝ) < q := by linarith
  have hne : q - q⁻¹ ≠ 0 := denom_ne q hq
  have hnum : q ^ 2 - (q ^ 2)⁻¹ = (q + q⁻¹) * (q - q⁻¹) := by
    field_simp; ring
  rw [hnum, mul_div_assoc, div_self hne, mul_one]

/-- **MAIN (scope-(a) bracketing of the finite sub-case).** The required `r*` lies STRICTLY
between the quantum integers `[1]_q = 1` and `[2]_q = q + q⁻¹` for any `q` with
`q + q⁻¹ ≥ 2` — in particular for the substrate `q₀ > 1`, where `q₀ + q₀⁻¹ ≈ 2.01 ≥ 2`. Since
`r* ∈ (3/2, 2)` and the α_EM-shape finite Habiro element evaluates (to leading order) to a
quantum integer `[k]_q`, no integer `k` lands on `r*`: `[1]_q = 1 < 3/2 < r* < 2 ≤ [2]_q`. A
value hitting `r*` requires a NON-forced (fit) coefficient. -/
theorem rStar_strictly_between_q1_q2 (q : ℝ) (hq : 1 < q) (hqq : 2 ≤ q + q⁻¹) :
    qInt 1 q < rStar ∧ rStar < qInt 2 q := by
  constructor
  · rw [qInt_one q hq]; linarith [rStar_gt_three_halves]
  · rw [qInt_two q hq]; linarith [rStar_lt_two]

/-- Consequently no `[k]_q` for `k ∈ {1, 2}` — the two quantum integers bracketing `r*` — can
equal it; the α_EM-shape's leading factor cannot supply `r*` at any `q > 1` with
`q + q⁻¹ ≥ 2` (0-fit). -/
theorem no_bracketing_qInt_eq_rStar (q : ℝ) (hq : 1 < q) (hqq : 2 ≤ q + q⁻¹) :
    qInt 1 q ≠ rStar ∧ qInt 2 q ≠ rStar := by
  obtain ⟨h1, h2⟩ := rStar_strictly_between_q1_q2 q hq hqq
  exact ⟨ne_of_lt h1, (ne_of_lt h2).symm⟩

end QOU.MassTheory.HabiroMagnitudeA3
