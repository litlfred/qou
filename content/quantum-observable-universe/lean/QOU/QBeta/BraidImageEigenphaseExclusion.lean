/-
# No braid-image transfer matrix carries the Q_β ladder phase — in ANY convention

Bean `qou-cds1` (tranche S1).  Companion to
`computations/qbeta/qbeta_braid_image_eigenphase_exclusion_probe.py` (11/11 exact).

## What this closes

`QOU.QBeta.EigenphaseCarrier` establishes that the class meant to carry the
spectral identification of the ladder phase `α = (z−1)h/2` is **vacuous**, and
leaves a trichotomy for a transfer matrix `M` with spectrum `{e^{±iα}}`:

1. `M` in the braid image — called *excluded there*, by transcendence of
   `2cos((z−1)h/2)` over `ℚ(q,z)`.  That is an assertion carried in a docstring,
   it is not proved anywhere in the corpus, and it is stated for convention C.
2. `M` arbitrary — circular (`rotationOfPhase` satisfies it for any `α`).
3. `M` a holonomy of an independently-defined connection (KZ / Kohno–Drinfeld) —
   the only contentful branch.

This file **proves branch 1**, by an elementary boundedness argument in place of
the transcendence assertion, and the argument never reads `z`'s formula.  So the
exclusion is not a fact about convention C: it holds for **every** Markov
parameter whose phase is non-constant, and in particular for the canonical
convention D of the 2026-08-15 owner ruling.

## The argument

Work in the substrate variable `s = √q`, in which both conventions are rational:

    z_C(s) = s/(s²+1)     z_D(s) = s⁶/(s⁴+1)     h(s) = s² − s⁻²
    α_X(s) = (z_X(s) − 1)·h(s)/2

A braid word's character in the 2-dimensional irrep `V_(2,1)` of `H₃(q)` is a
Laurent polynomial `P(s)/s^N` (verified exactly in the probe over every word of
length ≤ 5; the general statement is the standard `χ_λ(T_w) ∈ ℤ[q,q⁻¹]` of
Geck–Pfeiffer, imported here as the shape of the hypothesis, not proved).  If
such a character equals `2 cos α`, then `§1`'s `no_laurent_of_surjective_nonpos`
gives `False` as soon as `α` attains **every** non-positive real on `[1,∞)`:
`cos α` then takes the value `1` at infinitely many points, forcing
`P = C 2 * X^N`, and the value `−1` at infinitely many points, forcing
`P = C (−2) * X^N`.

`§2` supplies the hypothesis for both conventions from continuity plus a growth
bound, via the intermediate value theorem: `α_C` is unbounded **below**
(`alphaC_le`, exact) and `α_D` is unbounded **above** (`alphaD_ge`), and
`cos` is even, so `−α_D` serves for D.

## Scope

Scope-(b) — a structural exclusion citing a proved invariant, per AGENTS.md
§"Before declaring refuted".  It does **not** derive `α`, in either convention,
and it does **not** state a D-frame ladder.  Branch 3 is untouched and remains
the only place a derivation of `α` can live.

**Two limits of the exclusion, stated so nobody over-reads it.**

* It excludes a **functional identification** on the substrate branch — the
  hypothesis `heq` quantifies over all `s ≥ 1` — not a numerical coincidence at
  the single anchor `q₀`.  That is the right target (a ladder is a `q`-dependent
  formula, and a one-point agreement is what the corpus calls a *near-match*),
  but it is worth being explicit: nothing here says `2cos(α(q₀))` fails to equal
  some character *value*.
* The Laurent-polynomial shape of `tr ρ(w)` is **imported**, from the standard
  `χ_λ(T_w) ∈ ℤ[q,q⁻¹]` of Geck–Pfeiffer, and appears here as the shape of the
  hypothesis rather than as a proved lemma.  It is checked exactly, over every
  braid word of length ≤ 5, in the companion probe.
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Algebra.Polynomial.Roots
import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Tactic

namespace QOU.QBeta.BraidImageEigenphase

open Real Polynomial

/-! ## §1 — the abstract core

No Laurent polynomial in `s` agrees with `2 cos (α s)` on `[1,∞)` when `α`
attains every non-positive value there.  Nothing below mentions a Markov
parameter; this is the convention-independence. -/

/-- `cos` at a non-positive even multiple of `π` is `1`. -/
private theorem cos_neg_two_pi_mul (k : ℕ) : Real.cos (-((k : ℝ) * (2 * π))) = 1 := by
  rw [Real.cos_neg, Real.cos_nat_mul_two_pi]

/-- `cos` at an odd multiple of `π` is `−1`. -/
private theorem cos_pi_add_nat_two_pi (k : ℕ) :
    Real.cos (π + (k : ℝ) * (2 * π)) = -1 := by
  induction k with
  | zero => simp
  | succ n ih =>
      have e : π + ((n + 1 : ℕ) : ℝ) * (2 * π) = (π + (n : ℝ) * (2 * π)) + 2 * π := by
        push_cast; ring
      rw [e, Real.cos_add_two_pi, ih]

/-- `cos` at a non-positive odd multiple of `π` is `−1`. -/
private theorem cos_neg_two_pi_mul_add_pi (k : ℕ) :
    Real.cos (-((k : ℝ) * (2 * π) + π)) = -1 := by
  rw [Real.cos_neg, add_comm, cos_pi_add_nat_two_pi]

/-- **The core exclusion.**  If `α` attains every non-positive real on `[1,∞)`,
then `2 cos (α ·)` is not a Laurent polynomial `P(s)/s^N` there. -/
theorem no_laurent_of_surjective_nonpos
    (α : ℝ → ℝ)
    (hsurj : ∀ y : ℝ, y ≤ 0 → ∃ s : ℝ, 1 ≤ s ∧ α s = y)
    (P : ℝ[X]) (N : ℕ)
    (heq : ∀ s : ℝ, 1 ≤ s → 2 * Real.cos (α s) = P.eval s / s ^ N) :
    False := by
  -- A point of `[1,∞)` where `2 cos (α ·)` takes value `v` forces
  -- `(P - C v * X^N).IsRoot`.
  have root_of : ∀ (v s : ℝ), 1 ≤ s → 2 * Real.cos (α s) = v →
      (P - C v * X ^ N).IsRoot s := by
    intro v s hs hv
    have hs0 : (0 : ℝ) < s := lt_of_lt_of_le zero_lt_one hs
    have hpow : (s : ℝ) ^ N ≠ 0 := pow_ne_zero _ (ne_of_gt hs0)
    have : P.eval s / s ^ N = v := by rw [← heq s hs, hv]
    have hPv : P.eval s = v * s ^ N := by
      field_simp at this; linarith [this]
    simp [Polynomial.IsRoot, hPv]
  -- From a family of witnesses with pairwise distinct `α`-values we get an
  -- infinite root set, hence `P = C v * X^N`.
  have forced : ∀ (v : ℝ) (y : ℕ → ℝ), (∀ k, y k ≤ 0) → Function.Injective y →
      (∀ k, Real.cos (y k) = v / 2) → P = C v * X ^ N := by
    intro v y hnonpos hinj hcos
    choose f hf1 hf2 using fun k : ℕ => hsurj (y k) (hnonpos k)
    have hfinj : Function.Injective f := by
      intro a b hab
      exact hinj (by rw [← hf2 a, ← hf2 b, hab])
    have hmem : ∀ k : ℕ, f k ∈ {x : ℝ | (P - C v * X ^ N).IsRoot x} := by
      intro k
      refine root_of v (f k) (hf1 k) ?_
      rw [hf2 k, hcos k]; ring
    have hinf : {x : ℝ | (P - C v * X ^ N).IsRoot x}.Infinite :=
      Set.infinite_of_injective_forall_mem hfinj hmem
    have := Polynomial.eq_zero_of_infinite_isRoot (P - C v * X ^ N) hinf
    linear_combination (norm := ring_nf) this
  -- Even multiples of `2π`: `cos = 1`, so `P = C 2 * X^N`.
  have hEven : P = C 2 * X ^ N := by
    refine forced 2 (fun k => -((k : ℝ) * (2 * π))) (fun k => ?_) (fun a b hab => ?_)
      (fun k => by rw [cos_neg_two_pi_mul k]; norm_num)
    · have : (0 : ℝ) ≤ (k : ℝ) * (2 * π) := by positivity
      linarith
    · have hpi : (0 : ℝ) < 2 * π := by positivity
      have : (a : ℝ) * (2 * π) = (b : ℝ) * (2 * π) := by linarith [neg_injective hab]
      exact_mod_cast mul_right_cancel₀ (ne_of_gt hpi) this
  -- Odd multiples of `π`: `cos = -1`, so `P = C (-2) * X^N`.
  have hOdd : P = C (-2 : ℝ) * X ^ N := by
    refine forced (-2) (fun k => -((k : ℝ) * (2 * π) + π)) (fun k => ?_) (fun a b hab => ?_)
      (fun k => by rw [cos_neg_two_pi_mul_add_pi k]; norm_num)
    · have h1 : (0 : ℝ) ≤ (k : ℝ) * (2 * π) := by positivity
      have h2 : (0 : ℝ) < π := Real.pi_pos
      linarith
    · have hpi : (0 : ℝ) < 2 * π := by positivity
      have : (a : ℝ) * (2 * π) = (b : ℝ) * (2 * π) := by linarith [neg_injective hab]
      exact_mod_cast mul_right_cancel₀ (ne_of_gt hpi) this
  -- `C 2 * X^N = C (-2) * X^N` is false: compare the `N`-th coefficient.
  have : (2 : ℝ) = -2 := by
    have h := hEven.symm.trans hOdd
    have := congrArg (fun p : ℝ[X] => p.coeff N) h
    simpa using this
  norm_num at this

/-! ## §2 — the two conventions

`z_C` and `z_D` in the substrate variable `s = √q`, and the phase they induce. -/

/-- Convention C Markov parameter in `s = √q`:  `z_C = √q/(q+1) = s/(s²+1)`. -/
noncomputable def zC (s : ℝ) : ℝ := s / (s ^ 2 + 1)

/-- Convention D Markov parameter in `s = √q` (canonical, owner ruling
2026-08-15):  `z_D = q³/(q²+1) = s⁶/(s⁴+1)`. -/
noncomputable def zD (s : ℝ) : ℝ := s ^ 6 / (s ^ 4 + 1)

/-- `h = q − q⁻¹` in `s = √q`. -/
noncomputable def hS (s : ℝ) : ℝ := s ^ 2 - 1 / s ^ 2

/-- The asserted ladder eigenphase `α = (z − 1)·h/2`. -/
noncomputable def alphaOf (z : ℝ → ℝ) (s : ℝ) : ℝ := (z s - 1) * hS s / 2

/-- **Convention C is unbounded below**: `α_C(s) ≤ −(s−1)/4` for `s ≥ 1`. -/
theorem alphaC_le {s : ℝ} (hs : 1 ≤ s) : alphaOf zC s ≤ -(s - 1) / 4 := by
  have hs0 : (0 : ℝ) < s := lt_of_lt_of_le zero_lt_one hs
  have hden : (0 : ℝ) < 2 * s ^ 2 * (s ^ 2 + 1) := by positivity
  have key : alphaOf zC s = (s - s ^ 2 - 1) * (s ^ 4 - 1) / (2 * s ^ 2 * (s ^ 2 + 1)) := by
    unfold alphaOf zC hS
    field_simp
    ring
  rw [key, div_le_iff₀ hden]
  have hcube : (0 : ℝ) ≤ s ^ 3 + 1 - s ^ 2 / 2 := by nlinarith [sq_nonneg s, sq_nonneg (s - 1)]
  have hfac : (0 : ℝ) ≤ (s - 1) * (s ^ 2 + 1) * (s ^ 3 + 1 - s ^ 2 / 2) :=
    mul_nonneg (mul_nonneg (by linarith) (by positivity)) hcube
  nlinarith [hfac]

/-- **Convention D is unbounded above**: `α_D(s) ≥ s − 3` for `s ≥ 3`. -/
theorem alphaD_ge {s : ℝ} (hs : 3 ≤ s) : s - 3 ≤ alphaOf zD s := by
  have hs0 : (0 : ℝ) < s := by linarith
  have hden : (0 : ℝ) < 2 * s ^ 2 * (s ^ 4 + 1) := by positivity
  have key : alphaOf zD s = (s ^ 6 - s ^ 4 - 1) * (s ^ 4 - 1) / (2 * s ^ 2 * (s ^ 4 + 1)) := by
    unfold alphaOf zD hS
    field_simp
    ring
  rw [key, le_div_iff₀ hden]
  -- `s ≥ 3`:  LHS ≥ s^10/4  and  RHS ≤ 4 s^7 ≤ s^10/4.
  have hs2 : (9 : ℝ) ≤ s ^ 2 := by nlinarith
  have hs3 : (27 : ℝ) ≤ s ^ 3 := by nlinarith [sq_nonneg (s - 3), sq_nonneg (s + 3)]
  have hs4 : (81 : ℝ) ≤ s ^ 4 := by nlinarith [sq_nonneg (s ^ 2 - 9)]
  have hkey1 : (9 : ℝ) * s ^ 4 ≤ s ^ 6 := by
    have := mul_le_mul_of_nonneg_left hs2 (le_of_lt (pow_pos hs0 4))
    nlinarith [this]
  have h1 : s ^ 6 / 2 ≤ s ^ 6 - s ^ 4 - 1 := by linarith
  have h2 : s ^ 4 / 2 ≤ s ^ 4 - 1 := by linarith
  have h1' : (0 : ℝ) ≤ s ^ 6 / 2 := by positivity
  have h2' : (0 : ℝ) ≤ s ^ 4 / 2 := by positivity
  have hprod : s ^ 10 / 4 ≤ (s ^ 6 - s ^ 4 - 1) * (s ^ 4 - 1) := by
    calc s ^ 10 / 4 = (s ^ 6 / 2) * (s ^ 4 / 2) := by ring
      _ ≤ (s ^ 6 - s ^ 4 - 1) * (s ^ 4 - 1) := by
          apply mul_le_mul h1 h2 h2' (by linarith)
  have hrhs : (s - 3) * (2 * s ^ 2 * (s ^ 4 + 1)) ≤ 4 * s ^ 7 := by
    nlinarith [pow_pos hs0 2, pow_pos hs0 4, pow_pos hs0 6, pow_pos hs0 7]
  have hkey2 : (27 : ℝ) * s ^ 7 ≤ s ^ 10 := by
    have := mul_le_mul_of_nonneg_left hs3 (le_of_lt (pow_pos hs0 7))
    nlinarith [this]
  have hlast : 4 * s ^ 7 ≤ s ^ 10 / 4 := by nlinarith [pow_pos hs0 7]
  linarith

/-- Continuity of `α_z` on `[1,b]` for a `z` continuous there. -/
theorem alphaOf_continuousOn {z : ℝ → ℝ} {b : ℝ}
    (hz : ContinuousOn z (Set.Icc 1 b)) : ContinuousOn (alphaOf z) (Set.Icc 1 b) := by
  have hne : ∀ x ∈ Set.Icc (1 : ℝ) b, x ^ 2 ≠ 0 := by
    intro x hx
    have : (0 : ℝ) < x := lt_of_lt_of_le zero_lt_one hx.1
    positivity
  have hh : ContinuousOn hS (Set.Icc 1 b) := by
    unfold hS
    exact (continuousOn_pow 2).sub (continuousOn_const.div (continuousOn_pow 2) hne)
  exact ((hz.sub continuousOn_const).mul hh).div_const 2

theorem zC_continuousOn {b : ℝ} : ContinuousOn zC (Set.Icc 1 b) := by
  unfold zC
  refine continuousOn_id.div (by fun_prop) ?_
  intro x _; positivity

theorem zD_continuousOn {b : ℝ} : ContinuousOn zD (Set.Icc 1 b) := by
  unfold zD
  refine (continuousOn_pow 6).div (by fun_prop) ?_
  intro x hx
  have : (0 : ℝ) < x := lt_of_lt_of_le zero_lt_one hx.1
  positivity

/-- `α_z(1) = 0` for any `z` — the phase vanishes at the classical point,
because `h(1) = 0`. -/
theorem alphaOf_one (z : ℝ → ℝ) : alphaOf z 1 = 0 := by
  unfold alphaOf hS; norm_num

/-- **IVT packaging.**  A continuous phase vanishing at `s = 1` and taking
arbitrarily negative values on `[1,∞)` attains *every* non-positive real. -/
theorem surjective_nonpos_of_growth (z : ℝ → ℝ)
    (hz : ∀ b : ℝ, ContinuousOn z (Set.Icc 1 b))
    (hgrow : ∀ y : ℝ, y ≤ 0 → ∃ s : ℝ, 1 ≤ s ∧ alphaOf z s ≤ y) :
    ∀ y : ℝ, y ≤ 0 → ∃ s : ℝ, 1 ≤ s ∧ alphaOf z s = y := by
  intro y hy
  obtain ⟨b, hb1, hb2⟩ := hgrow y hy
  have hcont : ContinuousOn (alphaOf z) (Set.Icc 1 b) := alphaOf_continuousOn (hz b)
  have hsub := intermediate_value_Icc' hb1 hcont
  have hmem : y ∈ Set.Icc (alphaOf z b) (alphaOf z 1) := by
    rw [alphaOf_one]; exact ⟨hb2, hy⟩
  obtain ⟨s, hs, hval⟩ := hsub hmem
  exact ⟨s, hs.1, hval⟩

/-! ### The two instantiations -/

/-- Convention C attains every non-positive phase on `[1,∞)`. -/
theorem alphaC_surjective_nonpos :
    ∀ y : ℝ, y ≤ 0 → ∃ s : ℝ, 1 ≤ s ∧ alphaOf zC s = y := by
  refine surjective_nonpos_of_growth zC (fun _ => zC_continuousOn) ?_
  intro y hy
  refine ⟨1 - 4 * y, by linarith, ?_⟩
  have := alphaC_le (s := 1 - 4 * y) (by linarith)
  linarith

/-- Convention D attains every non-positive phase on `[1,∞)` **after negation**
— `α_D` is unbounded above, and `cos` is even, so `−α_D` is the relevant
function. -/
theorem alphaD_neg_surjective_nonpos :
    ∀ y : ℝ, y ≤ 0 → ∃ s : ℝ, 1 ≤ s ∧ (fun t => -(alphaOf zD t)) s = y := by
  intro y hy
  have hgrow : ∀ w : ℝ, w ≤ 0 → ∃ s : ℝ, 1 ≤ s ∧ -(alphaOf zD s) ≤ w := by
    intro w hw
    refine ⟨3 - w, by linarith, ?_⟩
    have := alphaD_ge (s := 3 - w) (by linarith)
    linarith
  -- Same IVT packaging, applied to `-(α_D ·)`.
  obtain ⟨b, hb1, hb2⟩ := hgrow y hy
  have hcont : ContinuousOn (fun t => -(alphaOf zD t)) (Set.Icc 1 b) :=
    (alphaOf_continuousOn (zD_continuousOn (b := b))).neg
  have hsub := intermediate_value_Icc' hb1 hcont
  have hmem : y ∈ Set.Icc (-(alphaOf zD b)) (-(alphaOf zD 1)) := by
    rw [alphaOf_one]; exact ⟨hb2, by simpa using hy⟩
  obtain ⟨s, hs, hval⟩ := hsub hmem
  exact ⟨s, hs.1, hval⟩

/-! ## §3 — the exclusion, in each convention

The hypothesis `heq` is the branch-1 assumption of the
`EigenphaseCarrierVacuity` trichotomy, written out: the transfer matrix lies in
the braid image, so its character is a Laurent polynomial `P(s)/s^N` in the
substrate variable, and it equals `2 cos α` because the spectrum is
`{e^{±iα}}`.  Laurent polynomials **in `√q`** are allowed, so this covers
`ℤ[q^{±1}]` and `ℤ[q^{±1/2}]` alike. -/

/-- **Branch 1 is closed for convention C.** -/
theorem no_braid_character_C (P : ℝ[X]) (N : ℕ)
    (heq : ∀ s : ℝ, 1 ≤ s → 2 * Real.cos (alphaOf zC s) = P.eval s / s ^ N) :
    False :=
  no_laurent_of_surjective_nonpos (alphaOf zC) alphaC_surjective_nonpos P N heq

/-- **Branch 1 is closed for convention D** — the canonical one. -/
theorem no_braid_character_D (P : ℝ[X]) (N : ℕ)
    (heq : ∀ s : ℝ, 1 ≤ s → 2 * Real.cos (alphaOf zD s) = P.eval s / s ^ N) :
    False := by
  refine no_laurent_of_surjective_nonpos (fun t => -(alphaOf zD t))
    alphaD_neg_surjective_nonpos P N ?_
  intro s hs
  rw [Real.cos_neg]
  exact heq s hs

end QOU.QBeta.BraidImageEigenphase
