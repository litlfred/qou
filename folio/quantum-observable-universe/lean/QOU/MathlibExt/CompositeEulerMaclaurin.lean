/-
  Composite order-2 Euler–Maclaurin on a uniform grid — `qou-mlgp` (A).

  WHAT THIS IS.  `CorrectedTrapezoid.lean` gives the ONE-CELL rule

      ∫_c^{c+h} g = (h/2)(g c + g(c+h)) − (h²/12)(g′(c+h) − g′(c)) + R_c,
      |R_c| ≤ h⁵·sup|g⁗|/720.

  This file sums it over `k` cells.  Two things telescope, and that is the whole
  point:

    * the trapezoid halves collapse to the composite trapezoid sum
      `h·∑_{j=0}^{k} g(a+jh) − (h/2)(g a + g(a+kh))`;
    * the `B₂` corrections collapse to the SINGLE boundary term
      `−(h²/12)·(g′(a+kh) − g′(a))`.

  So `k` cells contribute `k` remainders but only ONE correction term.  That is
  exactly why the `qou-mlgp` (A) expansion carries a lone `−(π/12N)·cot θ` and
  nothing else below `O(1/N³)`: the interior `B₂` terms cancel in pairs and only
  the two endpoints survive.

  THE PROOF is induction on `k`.  The inductive step is the one-cell rule on
  `[a+kh, a+(k+1)h]` plus `integral_add_adjacent_intervals`; the residual at
  `k+1` splits as (inductive residual) + (cell residual), which is a `ring`
  identity once the integral is split.  Hypotheses on the big interval restrict
  to each cell by `Set.Icc` monotonicity.

  ON APPLYING THIS TO `logSinc` — SUPERSEDED, SEE `QOU/Knot/LogSincNearZero.lean`.
  An earlier version of this header said the remaining obstacle was exhibiting
  the analytic extension of `logSinc x = log(sin x) − log x` at `0`, since the
  rule was being applied on `[0, θ]` and `logSinc` is not differentiable at `0`
  as literally written.  That is true of `[0, θ]` but is an artefact of the
  choice of left endpoint: the Kashaev sum starts at `j = 1`, so `[h, θ]` is the
  natural interval, it never touches `0`, and the three left-endpoint terms it
  costs are all `O(h²) = O(1/N²)` — one order BELOW the `O(1/N)` term (A) is
  chasing.  No analytic extension is needed.  See that file for the elementary
  `O(x²)` bound that replaces it.

  -- Ref: [leitner2026] QOU/MathlibExt/CorrectedTrapezoid.lean   (the one-cell rule)
  -- Ref: [leitner2026] QOU/Knot/KashaevEndpointSplit.lean       (where logSinc enters)
-/
import QOU.MathlibExt.CorrectedTrapezoid

namespace QOU.MathlibExt

open Real MeasureTheory intervalIntegral

/-- **Composite order-2 Euler–Maclaurin on a uniform grid.**

    | ∫_a^{a+kh} g − [ h·∑_{j=0}^{k} g(a+jh) − (h/2)(g a + g(a+kh))
                       − (h²/12)(g′(a+kh) − g′ a) ] |   ≤   k·h⁵·M/720

for `|g⁗| ≤ M` on `[a, a+kh]`.  Note the `B₂` correction appears ONCE, not `k`
times: the interior terms telescope away. -/
theorem abs_integral_sub_composite_le
    {g g₁ g₂ g₃ g₄ : ℝ → ℝ} {a h M : ℝ} (hh : 0 < h) (k : ℕ)
    (hg : ∀ x ∈ Set.Icc a (a + k * h), HasDerivAt g (g₁ x) x)
    (hg1 : ∀ x ∈ Set.Icc a (a + k * h), HasDerivAt g₁ (g₂ x) x)
    (hg2 : ∀ x ∈ Set.Icc a (a + k * h), HasDerivAt g₂ (g₃ x) x)
    (hg3 : ∀ x ∈ Set.Icc a (a + k * h), HasDerivAt g₃ (g₄ x) x)
    (hcont : ContinuousOn g₄ (Set.Icc a (a + k * h)))
    (hM : ∀ x ∈ Set.Icc a (a + k * h), |g₄ x| ≤ M) :
    |(∫ x in a..(a + k * h), g x)
        - (h * (∑ j ∈ Finset.range (k + 1), g (a + j * h))
           - h / 2 * (g a + g (a + k * h))
           - h ^ 2 / 12 * (g₁ (a + k * h) - g₁ a))|
      ≤ (k : ℝ) * h ^ 5 * M / 720 := by
  induction k with
  | zero =>
      norm_num
      ring
  | succ n ih =>
      push_cast at hg hg1 hg2 hg3 hcont hM ⊢
      set A : ℝ := a + (n : ℝ) * h with hA
      set B : ℝ := a + ((n : ℝ) + 1) * h with hB
      have haA : a ≤ A := by rw [hA]; nlinarith [Nat.cast_nonneg (α := ℝ) n]
      have hAB : A ≤ B := by rw [hA, hB]; nlinarith
      have hBA : B - A = h := by rw [hA, hB]; ring
      have hsubA : Set.Icc a A ⊆ Set.Icc a B := Set.Icc_subset_Icc le_rfl hAB
      have hsubcell : Set.uIcc A B ⊆ Set.Icc a B := by
        rw [Set.uIcc_of_le hAB]
        exact Set.Icc_subset_Icc haA le_rfl
      have hsubuA : Set.uIcc a A ⊆ Set.Icc a B := by
        rw [Set.uIcc_of_le haA]
        exact Set.Icc_subset_Icc le_rfl hAB
      -- the inductive residual
      have ihb := ih (fun x hx => hg x (hsubA hx)) (fun x hx => hg1 x (hsubA hx))
        (fun x hx => hg2 x (hsubA hx)) (fun x hx => hg3 x (hsubA hx))
        (hcont.mono hsubA) (fun x hx => hM x (hsubA hx))
      -- the one-cell residual on `[A, B]`
      have hcellrule := abs_corrected_trapezoid_sub_integral_le (M := M) hAB
        (fun x hx => hg x (hsubcell hx)) (fun x hx => hg1 x (hsubcell hx))
        (fun x hx => hg2 x (hsubcell hx)) (fun x hx => hg3 x (hsubcell hx))
        (hcont.mono hsubcell) (fun x hx => hM x (hsubcell hx))
      rw [hBA] at hcellrule
      -- split the integral at the new grid point
      have hgcont : ContinuousOn g (Set.Icc a B) :=
        fun x hx => (hg x hx).continuousAt.continuousWithinAt
      have hsplit := integral_add_adjacent_intervals
        (μ := volume) (f := g) (hgcont.mono hsubuA).intervalIntegrable
        (hgcont.mono hsubcell).intervalIntegrable
      rw [Finset.sum_range_succ]
      push_cast
      rw [← hB]
      -- the residual at `n+1` splits as (inductive residual) + (cell residual)
      have hdecomp :
          (∫ x in a..B, g x)
            - (h * ((∑ j ∈ Finset.range (n + 1), g (a + (j : ℝ) * h)) + g B)
               - h / 2 * (g a + g B) - h ^ 2 / 12 * (g₁ B - g₁ a))
          = ((∫ x in a..A, g x)
              - (h * (∑ j ∈ Finset.range (n + 1), g (a + (j : ℝ) * h))
                 - h / 2 * (g a + g A) - h ^ 2 / 12 * (g₁ A - g₁ a)))
            + ((∫ x in A..B, g x)
               - (h / 2 * (g A + g B) - h ^ 2 / 12 * (g₁ B - g₁ A))) := by
        rw [← hsplit]; ring
      rw [hdecomp]
      have hcell2 : |(∫ x in A..B, g x)
          - (h / 2 * (g A + g B) - h ^ 2 / 12 * (g₁ B - g₁ A))|
            ≤ h ^ 5 * M / 720 := by
        rw [abs_sub_comm]
        convert hcellrule using 2
      -- triangle inequality, done by hand so no lemma name can drift
      rw [abs_le] at ihb hcell2
      rw [show ((n : ℝ) + 1) * h ^ 5 * M / 720
            = (n : ℝ) * h ^ 5 * M / 720 + h ^ 5 * M / 720 from by ring, abs_le]
      constructor <;> linarith [ihb.1, ihb.2, hcell2.1, hcell2.2]

/-! ### The composite rule driven by oscillation, for monotone `g″`

Same induction, but with `abs_corrected_trapezoid_sub_integral_le_osc` in place
of the `g⁗` bound.  When `g″` is ANTITONE the per-cell oscillation on
`[a+jh, a+(j+1)h]` is exactly `g″(a+jh) − g″(a+(j+1)h)`, and the bounds
TELESCOPE in the induction's arithmetic — no separate summation lemma is needed,
the `h³/12·(g″(a) − g″(A))` of the inductive step plus the
`h³/12·(g″(A) − g″(B))` of the new cell add to `h³/12·(g″(a) − g″(B))`.

Hypotheses are `C²` ONLY — no `g‴`, no `g⁗`.  That is because
`integral_eq_corrected_trapezoid_sub_deriv2` derives the order-2 identity from
the order-1 one by rewriting the kernel, rather than from the quartic kernel.

The payoff: `k` cells give a bound with NO factor of `k`.  Against the `g⁗`
version's `k·h⁵·sup|g⁗|/720`, this is `h³·TV(g″)/12` — and on the sum (divide by
`h`) that is `O(h²) = O(1/N²)`, below the `O(1/N)` term `qou-mlgp` (A) extracts,
while needing only `logSinc″` (bounded, and monotone by
`QOU.MathlibExt.mul_cube_cos_lt_sin_cube`) instead of `logSinc⁗`.
-/

/-- **Composite order-2 Euler–Maclaurin with an oscillation bound.**

    | ∫_a^{a+kh} g − [ h·∑_{j=0}^{k} g(a+jh) − (h/2)(g a + g(a+kh))
                       − (h²/12)(g₁(a+kh) − g₁ a) ] |
      ≤ (h³/12)·(g₂ a − g₂(a+kh))

for `g₂ = g″` ANTITONE on `[a, a+kh]`.  Note the right-hand side does not grow
with `k`: the per-cell oscillations telescope. -/
theorem abs_integral_sub_composite_le_osc
    {g g₁ g₂ : ℝ → ℝ} {a h : ℝ} (hh : 0 < h) (k : ℕ)
    (hg : ∀ x ∈ Set.Icc a (a + k * h), HasDerivAt g (g₁ x) x)
    (hg1 : ∀ x ∈ Set.Icc a (a + k * h), HasDerivAt g₁ (g₂ x) x)
    (hc2 : ContinuousOn g₂ (Set.Icc a (a + k * h)))
    (hanti : AntitoneOn g₂ (Set.Icc a (a + k * h))) :
    |(∫ x in a..(a + k * h), g x)
        - (h * (∑ j ∈ Finset.range (k + 1), g (a + j * h))
           - h / 2 * (g a + g (a + k * h))
           - h ^ 2 / 12 * (g₁ (a + k * h) - g₁ a))|
      ≤ h ^ 3 / 12 * (g₂ a - g₂ (a + k * h)) := by
  induction k with
  | zero =>
      norm_num
      ring
  | succ n ih =>
      push_cast at hg hg1 hc2 hanti ⊢
      set A : ℝ := a + (n : ℝ) * h with hA
      set B : ℝ := a + ((n : ℝ) + 1) * h with hB
      have haA : a ≤ A := by rw [hA]; nlinarith [Nat.cast_nonneg (α := ℝ) n]
      have hAB : A ≤ B := by rw [hA, hB]; nlinarith
      have hBA : B - A = h := by rw [hA, hB]; ring
      have hsubA : Set.Icc a A ⊆ Set.Icc a B := Set.Icc_subset_Icc le_rfl hAB
      have hsubcell : Set.uIcc A B ⊆ Set.Icc a B := by
        rw [Set.uIcc_of_le hAB]
        exact Set.Icc_subset_Icc haA le_rfl
      have hsubuA : Set.uIcc a A ⊆ Set.Icc a B := by
        rw [Set.uIcc_of_le haA]
        exact Set.Icc_subset_Icc le_rfl hAB
      have ihb := ih (fun x hx => hg x (hsubA hx)) (fun x hx => hg1 x (hsubA hx))
        (hc2.mono hsubA) (hanti.mono hsubA)
      -- on the new cell the oscillation of an antitone `g₂` is `g₂ A − g₂ B`
      have hD : ∀ x ∈ Set.uIcc A B, |g₂ x - g₂ A| ≤ g₂ A - g₂ B := by
        intro x hx
        rw [Set.uIcc_of_le hAB, Set.mem_Icc] at hx
        have hxmem : x ∈ Set.Icc a B := ⟨le_trans haA hx.1, hx.2⟩
        have hAmem : A ∈ Set.Icc a B := ⟨haA, hAB⟩
        have hBmem : B ∈ Set.Icc a B := ⟨le_trans haA hAB, le_rfl⟩
        have h1 : g₂ x ≤ g₂ A := hanti hAmem hxmem hx.1
        have h2 : g₂ B ≤ g₂ x := hanti hxmem hBmem hx.2
        rw [abs_of_nonpos (by linarith)]
        linarith
      have hcellrule := abs_corrected_trapezoid_sub_integral_le_osc hAB
        (fun x hx => hg x (hsubcell hx)) (fun x hx => hg1 x (hsubcell hx))
        (hc2.mono hsubcell) hD
      rw [hBA] at hcellrule
      have hgcont : ContinuousOn g (Set.Icc a B) :=
        fun x hx => (hg x hx).continuousAt.continuousWithinAt
      have hsplit := integral_add_adjacent_intervals
        (μ := volume) (f := g) (hgcont.mono hsubuA).intervalIntegrable
        (hgcont.mono hsubcell).intervalIntegrable
      rw [Finset.sum_range_succ]
      push_cast
      rw [← hB]
      have hdecomp :
          (∫ x in a..B, g x)
            - (h * ((∑ j ∈ Finset.range (n + 1), g (a + (j : ℝ) * h)) + g B)
               - h / 2 * (g a + g B) - h ^ 2 / 12 * (g₁ B - g₁ a))
          = ((∫ x in a..A, g x)
              - (h * (∑ j ∈ Finset.range (n + 1), g (a + (j : ℝ) * h))
                 - h / 2 * (g a + g A) - h ^ 2 / 12 * (g₁ A - g₁ a)))
            + ((∫ x in A..B, g x)
               - (h / 2 * (g A + g B) - h ^ 2 / 12 * (g₁ B - g₁ A))) := by
        rw [← hsplit]; ring
      rw [hdecomp]
      have hcell2 : |(∫ x in A..B, g x)
          - (h / 2 * (g A + g B) - h ^ 2 / 12 * (g₁ B - g₁ A))|
            ≤ h ^ 3 / 12 * (g₂ A - g₂ B) := by
        rw [abs_sub_comm,
          show h ^ 3 / 12 * (g₂ A - g₂ B) = h ^ 3 * (g₂ A - g₂ B) / 12 from by ring]
        exact hcellrule
      -- the two bounds telescope: (g₂ a − g₂ A) + (g₂ A − g₂ B) = g₂ a − g₂ B
      rw [abs_le] at ihb hcell2
      rw [show h ^ 3 / 12 * (g₂ a - g₂ B)
            = h ^ 3 / 12 * (g₂ a - g₂ A) + h ^ 3 / 12 * (g₂ A - g₂ B) from by ring,
        abs_le]
      constructor <;> linarith [ihb.1, ihb.2, hcell2.1, hcell2.2]

end QOU.MathlibExt
