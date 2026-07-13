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

-- Ref: [manuscript] docs/audits/2026-07-11-keystone-c8-superexp-proof.md
-/
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Data.Real.Sqrt
import Mathlib.Tactic

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

/-! ## Involution numbers (concrete; `I(k) = Σ_{λ⊢k} f^λ` at q=1) -/

/-- The involution / telephone numbers `I(0)=I(1)=1`, `I(n+2)=I(n+1)+(n+1)I(n)`
(OEIS A000085). `I(k) = Σ_{λ⊢k} f^λ` — the `q=1` value of the QOU na-Stokes
period `S(n) = Σ_λ dim_q(λ)`. -/
def involutionNumber : ℕ → ℕ
  | 0 => 1
  | 1 => 1
  | (n + 2) => involutionNumber (n + 1) + (n + 1) * involutionNumber n

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

end QOU.BraidKnot.KeystoneC8SuperExpBound
