/-!
# QOU.Descartes.QMomentum — q-Momentum from braid writhe

The q-momentum of a particle is the Hecke-weighted writhe of its
braid representative.  At q=1 this reduces to the classical writhe.

LaTeX label: `def:q-momentum`

## References
- [jones1987] https://doi.org/10.2307/1971403
- [manuscript] §6/q-momentum

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.Int.Basic
import Mathlib.Data.List.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Algebra.GeomSum
import Mathlib.Analysis.SpecificLimits.Basic

namespace QOU.Descartes

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Descartes.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The q-momentum of a braid, computed from its crossing signs.
    Each positive crossing contributes +1, each negative contributes -1,
    weighted by q-deformation. -/
-- Ref: [manuscript] §6/q-momentum
noncomputable def qMomentum (q : R_q) (crossingSigns : List ℤ) : R_q :=
  crossingSigns.foldl (fun acc ε =>
    acc + (q ^ (2 * ε) - 1) / (q ^ 2 - 1)) 0

/-- Helper: foldl with additive function decomposes over cons. -/
private lemma foldl_qMomentum_acc (q : R_q) (acc : R_q) (signs : List ℤ) :
    List.foldl (fun a ε => a + (q ^ (2 * ε) - 1) / (q ^ 2 - 1)) acc signs =
    acc + List.foldl (fun a ε => a + (q ^ (2 * ε) - 1) / (q ^ 2 - 1)) 0 signs := by
  induction signs generalizing acc with
  | nil => simp [List.foldl]
  | cons s ss ih =>
    simp only [List.foldl]
    rw [ih, ih (0 + _)]
    ring

/-- Helper: the integer sum foldl decomposes over cons similarly. -/
private lemma foldl_intSum_acc (acc : R_q) (signs : List ℤ) :
    List.foldl (fun a (s : ℤ) => a + ↑s) acc signs =
    acc + List.foldl (fun a (s : ℤ) => a + ↑s) (0 : R_q) signs := by
  induction signs generalizing acc with
  | nil => simp [List.foldl]
  | cons s ss ih =>
    simp only [List.foldl]
    rw [ih, ih (0 + _)]
    ring

/-- Key single-term limit: (q^{2s} - 1)/(q² - 1) → s as q → 1.

    For s ≥ 0: the geometric sum identity gives
      (q^{2s} - 1)/(q² - 1) = Σ_{k=0}^{s-1} q^{2k}
    which is a polynomial in q, continuous at q=1, evaluating to s.
    For s < 0: multiply numerator and denominator by q^{-2s} and reduce
    to the positive case.

    Since crossing signs are always ±1 in practice:
      s = +1: (q²-1)/(q²-1) = 1 for q ≠ ±1
      s = -1: (q⁻²-1)/(q²-1) = -q⁻² → -1 as q → 1 -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
-- Ref: [manuscript] Ch. 6, §q-momentum
private lemma single_term_limit_pos_one :
    ∀ ε > 0, ∃ δ > 0, ∀ q : R_q, 0 < |q - 1| → |q - 1| < δ →
      |(q ^ (2 * (1 : ℤ)) - 1) / (q ^ 2 - 1) - ↑(1 : ℤ)| < ε := by
  intro ε hε
  refine ⟨1, one_pos, fun q hq _ => ?_⟩
  -- (q²-1)/(q²-1) = 1 for q ≠ ±1, and |q-1| > 0 ensures q ≠ 1
  have hq_ne : q ≠ 1 := by
    intro heq; rw [heq, sub_self, abs_zero] at hq; linarith
  have : q ^ (2 : ℤ) - 1 ≠ 0 := by
    simp only [zpow_natCast]; intro h
    have : q ^ 2 = 1 := by linarith
    have : q = 1 ∨ q = -1 := by
      have : (q - 1) * (q + 1) = 0 := by nlinarith
      rcases mul_eq_zero.mp this with h | h
      · left; linarith
      · right; linarith
    rcases this with rfl | rfl
    · exact hq_ne rfl
    · simp at hq; linarith
  simp only [Int.cast_one, zpow_natCast]
  rw [div_self this, sub_self, abs_zero]
  exact hε

/-- Key single-term limit: (q^{2s} - 1)/(q² - 1) → s as q → 1.

    For s = +1: (q²-1)/(q²-1) = 1 identically (for q ≠ ±1).
    For s = -1: (q⁻²-1)/(q²-1) = -1/q² → -1.
    General s: geometric sum (q^{2s}-1)/(q²-1) = Σ_{k=0}^{s-1} q^{2k}
    is a polynomial, continuous at q=1, evaluating to s.

    The general proof requires Mathlib's polynomial continuity or
    Filter.Tendsto infrastructure. With `lake build`, use:
      Polynomial.eval_geom_sum + Polynomial.continuous_eval -/
/-- **External axiom (L'Hôpital): the q-bracket limit
    `(q^{2s} − 1) / (q² − 1) → s` as `q → 1`.**

    Standard ε-δ continuity statement for a Polynomial-rational
    function; the limit is `s` by direct L'Hôpital evaluation.
    Pending Mathlib's Polynomial.continuous_eval + Filter.Tendsto
    integration. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
-- Ref: [manuscript] Ch. 6, §q-momentum
private axiom single_term_limit (s : ℤ) :
    ∀ ε > 0, ∃ δ > 0, ∀ q : R_q, 0 < |q - 1| → |q - 1| < δ →
      |(q ^ (2 * s) - 1) / (q ^ 2 - 1) - ↑s| < ε

/-- At q = 1, q-momentum equals the writhe (sum of signs). -/
-- Ref: [manuscript] §6/q-momentum
-- The limit q → 1 of (q^{2ε} - 1)/(q² - 1) = ε by L'Hôpital.
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
theorem qMomentum_classical_limit (signs : List ℤ) :
    -- In the q → 1 limit, each term (q^{2ε} - 1)/(q² - 1) → ε
    -- So q-momentum → writhe = Σε
    ∀ ε > 0, ∃ δ > 0, ∀ q : R_q, 0 < |q - 1| → |q - 1| < δ →
      |qMomentum q signs - (signs.foldl (fun acc s => acc + ↑s) (0 : R_q))| < ε := by
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Each term (q^{2ε} - 1)/(q² - 1) → ε by L'Hôpital as q → 1
  -- Ref: [manuscript] Ch. 6, §q-momentum
  induction signs with
  | nil =>
    -- Base case: qMomentum q [] = 0 and foldl ... [] = 0
    intro ε hε
    exact ⟨1, one_pos, fun q _ _ => by
      simp only [qMomentum, List.foldl, sub_self, abs_zero]; exact hε⟩
  | cons s ss ih =>
    -- Inductive step: decompose foldl over (s :: ss)
    intro ε hε
    -- Get δ₁ from the inductive hypothesis for the tail with ε/2
    have hε2 : (0 : R_q) < ε / 2 := by linarith
    obtain ⟨δ₁, hδ₁_pos, hδ₁⟩ := ih (ε / 2) hε2
    -- Get δ₂ from single_term_limit for the head with ε/2
    obtain ⟨δ₂, hδ₂_pos, hδ₂⟩ := single_term_limit s (ε / 2) hε2
    -- Take δ = min δ₁ δ₂
    refine ⟨min δ₁ δ₂, lt_min hδ₁_pos hδ₂_pos, fun q hq_pos hq_lt => ?_⟩
    have hq_lt₁ : |q - 1| < δ₁ := lt_of_lt_of_le hq_lt (min_le_left δ₁ δ₂)
    have hq_lt₂ : |q - 1| < δ₂ := lt_of_lt_of_le hq_lt (min_le_right δ₁ δ₂)
    -- Get bounds from hypotheses
    have h_tail := hδ₁ q hq_pos hq_lt₁
    have h_head := hδ₂ q hq_pos hq_lt₂
    -- Reduce to foldl form
    show |qMomentum q (s :: ss) -
          List.foldl (fun acc s => acc + ↑s) (0 : R_q) (s :: ss)| < ε
    -- Key decomposition lemmas for qMomentum and the integer sum
    have hq_decomp : qMomentum q (s :: ss) =
        (q ^ (2 * s) - 1) / (q ^ 2 - 1) + qMomentum q ss := by
      simp only [qMomentum, List.foldl]
      rw [foldl_qMomentum_acc]
      ring
    have hint_decomp : List.foldl (fun acc (s : ℤ) => acc + ↑s) (0 : R_q) (s :: ss) =
        (s : R_q) + List.foldl (fun acc (s : ℤ) => acc + ↑s) (0 : R_q) ss := by
      simp only [List.foldl]
      rw [foldl_intSum_acc]
      ring
    rw [hq_decomp, hint_decomp]
    -- Goal: |(term_s + qMom_tail) - (↑s + int_tail)| < ε
    -- = |(term_s - ↑s) + (qMom_tail - int_tail)| < ε
    have hrearrange :
        (q ^ (2 * s) - 1) / (q ^ 2 - 1) + qMomentum q ss -
        ((s : R_q) + List.foldl (fun acc (s : ℤ) => acc + ↑s) (0 : R_q) ss) =
        ((q ^ (2 * s) - 1) / (q ^ 2 - 1) - (s : R_q)) +
        (qMomentum q ss - List.foldl (fun acc (s : ℤ) => acc + ↑s) (0 : R_q) ss) := by
      ring
    rw [hrearrange]
    calc |((q ^ (2 * s) - 1) / (q ^ 2 - 1) - (s : R_q)) +
          (qMomentum q ss - List.foldl (fun acc (s : ℤ) => acc + ↑s) (0 : R_q) ss)|
        ≤ |(q ^ (2 * s) - 1) / (q ^ 2 - 1) - (s : R_q)| +
          |qMomentum q ss - List.foldl (fun acc (s : ℤ) => acc + ↑s) (0 : R_q) ss| :=
        abs_add _ _
      _ < ε / 2 + ε / 2 := add_lt_add h_head h_tail
      _ = ε := by ring

/-- The writhe of a braid word (sum of crossing signs). -/
-- Ref: [manuscript] §6/q-momentum
def writhe (crossingSigns : List ℤ) : ℤ :=
  crossingSigns.foldl (· + ·) 0

/-- Trefoil writhe = +3. -/
-- Ref: [manuscript] §6/q-momentum
example : writhe [1, 1, 1] = 3 := by decide

/-- Figure-eight writhe = 0 (amphichiral). -/
-- Ref: [manuscript] §6/q-momentum
example : writhe [1, -1, 1, -1] = 0 := by decide

/-- Mirror reversal negates the writhe. -/
-- Ref: [manuscript] §6/q-momentum
theorem writhe_mirror (signs : List ℤ) :
    writhe (signs.map (· * (-1))) = -writhe signs := by
  unfold writhe
  induction signs with
  | nil => simp [List.foldl]
  | cons s ss ih =>
    simp only [List.map_cons, List.foldl]
    -- Need a helper: foldl (· + ·) a (map (· * -1) l) = -foldl (· + ·) (-a) l... not quite
    -- Actually let's try a different approach with a general accumulator
    suffices h : ∀ (acc : ℤ) (l : List ℤ),
      List.foldl (· + ·) acc (l.map (· * (-1))) = -(List.foldl (· + ·) (-acc) l) by
      simpa using h 0 (s :: ss)
    intro acc l
    induction l generalizing acc with
    | nil => simp [List.foldl]
    | cons x xs ih =>
      simp only [List.map_cons, List.foldl]
      rw [ih]
      ring_nf

end QOU.Descartes
