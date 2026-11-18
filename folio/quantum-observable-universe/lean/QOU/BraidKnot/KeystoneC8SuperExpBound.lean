/-
# Keystone `W_λ` necessary-condition C8 — the super-exponential lower bound

The s5-so3 keystone's geometric `W_λ` realisation must satisfy necessary condition
**C8** (`docs/audits/2026-07-11-keystone-wlambda-superexp-necessary-condition.md`): the
Plancherel-weighted branched sum

    w_std(k) = (1/k!) Σ_{λ⊢k} (f^λ)² · f^{λ/(2,1)}  =  E_Planch[f^{λ/(2,1)}]

grows **super-exponentially**. This file proves the arithmetic core of the
super-exponential *lower bound*, discharging the Lean target the C8 audit flagged.
Compute: `computations/keystone_c8_superexp_proof.py` (witness verified `k = 3..12`).

## What is proved here vs carried (honest scope)

Everything **except** the two SYT-dimension identities is now *proved*, not assumed:

* **Cauchy–Schwarz (input B) — PROVED**, `weighted_cs`, from Mathlib's
  `sum_mul_sq_le_sq_mul_sq` (weighted via `Real.sqrt`). (An earlier draft carried
  this as a hypothesis; it is a general inequality and belongs proved.)
* **Involution numbers `I(k)` — CONCRETE**, `involutionNumber` (the recurrence
  `I(n+2)=I(n+1)+(n+1)I(n)`), with `involution_le_factorial : I n ≤ n!` proved.
  `I(k) = Σ_{λ⊢k} f^λ` is the `q=1` value of the QOU na-Stokes period `S(n)`.
* **The arithmetic reduction — PROVED**, `c8_lower_bound`:
  `(Σ f g = k!/3) ∧ (Σ g ≤ I(k)) ⇒ w_std ≥ k!/(9 I(k))`.

The **only** carried inputs are the two identities that genuinely need Standard-
Young-Tableau counting, which Mathlib does **not** have (it has `YoungDiagram` and
`SemistandardTableau`, but no `StandardYoungTableau`, hook-length formula, or `f^λ`):

  (A) `Σ_{λ⊢k} f^λ f^{λ/(2,1)} = k!/3`     (classical branching `Σ f^λ f^{λ/μ}=k! f^μ/|μ|!`),
  (C) `Σ_{λ⊢k} f^{λ/(2,1)} ≤ Σ f^λ = I(k)` (skew SYT ↪ straight SYT).

These are supplied as `f g : ι → ℝ` sum hypotheses — the minimal irreducible fill
(the same StandardYoungTableau infrastructure the keystone's Identity I needs,
`s5-so3-keystone.md` line 40 / #2634). Building `StandardYoungTableau` + the
hook-length formula in Mathlib would discharge (A)/(C) too; that is the open fill.

Base ring `ℝ`: the statement uses `Real.sqrt` (Cauchy–Schwarz) and division/order
(AGENTS.md §7c: archimedean ordered field is the correct home).

-- Ref: [leitner2026] docs/audits/2026-07-11-keystone-c8-superexp-proof.md
-/
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Data.Real.Sqrt
import Mathlib.Tactic
import QOU.Mass.InvolutionNumbers

namespace QOU.BraidKnot.KeystoneC8SuperExpBound

open Finset

/-! ## Cauchy–Schwarz, weighted form (proved from Mathlib) -/

/-- **Weighted Cauchy–Schwarz.** For nonnegative weights `g`,
`(Σ f g)² ≤ (Σ f² g)(Σ g)`. Proved from `sum_mul_sq_le_sq_mul_sq` applied to
`f·√g` and `√g`. -/
theorem weighted_cs {ι : Type*} (s : Finset ι) (f g : ι → ℝ)
    (hg : ∀ i ∈ s, 0 ≤ g i) :
    (∑ i ∈ s, f i * g i) ^ 2 ≤ (∑ i ∈ s, f i ^ 2 * g i) * (∑ i ∈ s, g i) := by
  have h := sum_mul_sq_le_sq_mul_sq s (fun i => f i * Real.sqrt (g i))
    (fun i => Real.sqrt (g i))
  have e1 : ∑ i ∈ s, (f i * Real.sqrt (g i)) * Real.sqrt (g i) = ∑ i ∈ s, f i * g i :=
    sum_congr rfl fun i hi => by rw [mul_assoc, Real.mul_self_sqrt (hg i hi)]
  have e2 : ∑ i ∈ s, (f i * Real.sqrt (g i)) ^ 2 = ∑ i ∈ s, f i ^ 2 * g i :=
    sum_congr rfl fun i hi => by rw [mul_pow, Real.sq_sqrt (hg i hi)]
  have e3 : ∑ i ∈ s, Real.sqrt (g i) ^ 2 = ∑ i ∈ s, g i :=
    sum_congr rfl fun i hi => Real.sq_sqrt (hg i hi)
  simpa only [e1, e2, e3] using h

/-! ## The C8 lower bound (arithmetic core, proved) -/

/-- **C8 super-exponential lower bound.** With `w_std := (Σ f² g)/kfac`, the
identity `Σ f g = kfac/3` (input A), and `Σ g ≤ Ik` (input C, `Ik = I(k)`),
the Plancherel-weighted branched sum obeys `w_std ≥ kfac/(9·Ik)`. Cauchy–Schwarz is
`weighted_cs` (proved); only (A)/(C) are SYT-supplied. -/
theorem c8_lower_bound {ι : Type*} (s : Finset ι) (f g : ι → ℝ) (kfac Ik : ℝ)
    (hg : ∀ i ∈ s, 0 ≤ g i) (hkfac : 0 < kfac) (hIk : 0 < Ik)
    (hA : ∑ i ∈ s, f i * g i = kfac / 3)      -- (A) Σ f^λ f^{λ/(2,1)} = k!/3
    (hC : ∑ i ∈ s, g i ≤ Ik) :                 -- (C) Σ f^{λ/(2,1)} ≤ I(k)
    kfac / (9 * Ik) ≤ (∑ i ∈ s, f i ^ 2 * g i) / kfac := by
  set W := ∑ i ∈ s, f i ^ 2 * g i with hWdef
  have hWnn : 0 ≤ W :=
    sum_nonneg fun i hi => mul_nonneg (sq_nonneg _) (hg i hi)
  have hcs : (∑ i ∈ s, f i * g i) ^ 2 ≤ W * (∑ i ∈ s, g i) := weighted_cs s f g hg
  rw [hA] at hcs
  have h2 : (kfac / 3) ^ 2 ≤ W * Ik :=
    le_trans hcs (mul_le_mul_of_nonneg_left hC hWnn)
  have key : kfac ^ 2 ≤ 9 * Ik * W := by nlinarith [h2]
  rw [div_le_div_iff₀ (by positivity) hkfac]
  nlinarith [key]

/-! ## Involution numbers (concrete; `I(k) = Σ_{λ⊢k} f^λ` at q=1)

**This file used to define its own `involutionNumber`.** It was a second, independent
definition of the sequence `QOU.Mass.involutionNumber` already carried — same two base cases,
same recurrence, no shared code. The duplication was harmless only by luck: the two constants
were distinct, so a lemma proved about one said nothing about the other, and bridging them
needed an explicit induction (`involutionNumber_eq_keystone`, now deleted as redundant).

The single definition now lives in `QOU/Mass/InvolutionNumbers.lean`, where the substantive
content also sits — `card_involutions_eq_involutionNumber`, that `I(n)` counts the involutions
in `S_n`. The `export` below keeps `KeystoneC8SuperExpBound.involutionNumber` resolving, so
every existing reference and the fully-qualified name both still work.

`I(k) = Σ_{λ⊢k} f^λ` — the `q=1` value of the QOU na-Stokes period `S(n) = Σ_λ dim_q(λ)` — is
proved in `QOU.Mass.sum_numSYT_eq_involutionNumber`. -/

export QOU.Mass (involutionNumber involutionNumber_zero involutionNumber_one
  involutionNumber_succ_succ)

/-- `I(n) ≤ n!` — the involution numbers are dominated by the factorial (so the C8
denominator `I(k)` keeps `k!/(9·I(k))` at least bounded below, and the super-
exponential class of `k!/I(k)` is grounded on a concrete sequence). -/
theorem involution_le_factorial : ∀ n, involutionNumber n ≤ n.factorial := by
  intro n
  induction n using Nat.twoStepInduction with
  | zero => decide
  | one => decide
  | more n ih1 ih2 =>
    -- I(n+2) = I(n+1) + (n+1)·I(n) ≤ (n+1)! + (n+1)·n! = 2·(n+1)! ≤ (n+2)!
    have e : (n + 2).factorial = (n + 2) * (n + 1).factorial := Nat.factorial_succ _
    have e2 : (n + 1).factorial = (n + 1) * n.factorial := Nat.factorial_succ _
    have hstep : involutionNumber (n + 2)
        = involutionNumber (n + 1) + (n + 1) * involutionNumber n := rfl
    calc involutionNumber (n + 2)
        = involutionNumber (n + 1) + (n + 1) * involutionNumber n := hstep
      _ ≤ (n + 1).factorial + (n + 1) * n.factorial :=
          Nat.add_le_add ih2 (Nat.mul_le_mul_left _ ih1)
      _ = 2 * (n + 1).factorial := by rw [e2]; ring
      _ ≤ (n + 2) * (n + 1).factorial := by
          exact Nat.mul_le_mul_right _ (by omega)
      _ = (n + 2).factorial := e.symm

/-! ## Genuinely super-exponential lower bound (square form, no `√`) -/

/-- **C8 super-exponential lower bound — square form.** The bare `c8_lower_bound`
combined with the crude `Ik ≤ kfac` (`involution_le_factorial`) only yields the
**constant** `w_std ≥ 1/9`. Feeding the *sharper* Gevrey-1/2 involution bound
`Ik² ≤ 2^K·kfac` instead gives a genuinely **super-exponential** lower bound on the
square:

  `w_std² ≥ kfac / (81 · 2^K)`   ( `= k!/(81·2^k)` at `kfac = k!`, `K = k` ),

and `k!/2^k → ∞` super-exponentially — so `w_std` itself leaves every geometric class.
Squaring sidesteps `Real.sqrt` entirely: pure algebra over the two proved inputs. This
is the arithmetic core the C8 audit's "super-exponential" claim actually needs (the
`1/9` constant did not deliver it). -/
theorem c8_superexp_sq_lower_bound {ι : Type*} (s : Finset ι) (f g : ι → ℝ)
    (kfac Ik : ℝ) (K : ℕ)
    (hg : ∀ i ∈ s, 0 ≤ g i) (hkfac : 0 < kfac) (hIk : 0 < Ik)
    (hA : ∑ i ∈ s, f i * g i = kfac / 3) (hC : ∑ i ∈ s, g i ≤ Ik)
    (hIsq : Ik ^ 2 ≤ 2 ^ K * kfac) :
    kfac / (81 * 2 ^ K) ≤ ((∑ i ∈ s, f i ^ 2 * g i) / kfac) ^ 2 := by
  set w := (∑ i ∈ s, f i ^ 2 * g i) / kfac with hw
  have hlb : kfac / (9 * Ik) ≤ w := c8_lower_bound s f g kfac Ik hg hkfac hIk hA hC
  have hpos : 0 < kfac / (9 * Ik) := by positivity
  -- w ≥ kfac/(9·Ik) > 0 ⇒ w² ≥ (kfac/(9·Ik))²
  have hsq : (kfac / (9 * Ik)) ^ 2 ≤ w ^ 2 := by
    have hwpos : 0 ≤ w := le_trans (le_of_lt hpos) hlb
    nlinarith [hlb, hpos, hwpos]
  -- (kfac/(9·Ik))² = kfac²/(81·Ik²) ≥ kfac²/(81·2^K·kfac) = kfac/(81·2^K)
  have h2K : (0:ℝ) < 2 ^ K := by positivity
  have hstep : kfac / (81 * 2 ^ K) ≤ (kfac / (9 * Ik)) ^ 2 := by
    rw [div_pow, div_le_div_iff₀ (by positivity) (by positivity)]
    nlinarith [hIsq, hkfac, mul_pos hkfac h2K, sq_nonneg Ik]
  linarith [hsq, hstep]

/-- The difference between the squared normalised sum and the super-exponential ratio is non-negative. -/
theorem c8_superexp_sq_sub_nonneg {ι : Type*} (s : Finset ι) (f g : ι → ℝ)
    (kfac Ik : ℝ) (K : ℕ)
    (hg : ∀ i ∈ s, 0 ≤ g i) (hkfac : 0 < kfac) (hIk : 0 < Ik)
    (hA : ∑ i ∈ s, f i * g i = kfac / 3) (hC : ∑ i ∈ s, g i ≤ Ik)
    (hIsq : Ik ^ 2 ≤ 2 ^ K * kfac) :
    0 ≤ ((∑ i ∈ s, f i ^ 2 * g i) / kfac) ^ 2 - kfac / (81 * 2 ^ K) :=
  sub_nonneg.mpr (c8_superexp_sq_lower_bound s f g kfac Ik K hg hkfac hIk hA hC hIsq)

end QOU.BraidKnot.KeystoneC8SuperExpBound
