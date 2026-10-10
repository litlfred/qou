/-
# S-map rigidity: the s-multiplication map fixes a moment sequence exactly when
  the sequence is log-quadratic (Stieltjes–Wigert)

Bean `qou-f6sm`; audit `docs/audits/2026-08-01-fvk-selection-framing.md`.
Probe: `computations/probes/fvk_selection_probe.py` (block V1).

## What this is about

For an indeterminate Stieltjes moment problem the **S-map**

  `S(μ) = (s ↦ s/c)_* (s·dμ / m₁)`

sends representing measures to representing measures whenever it preserves the
moments; on the Jacobi side it is `J ↦ c⁻¹ · LR(J)` with `LR` the Christoffel
step at shift `0`.  In the KSel-2-ID chain this map is exactly what relates the
two extremal self-adjoint extensions of the balanced Jacobi operator: for the
Stieltjes–Wigert core the Friedrichs measure IS the S-image of the Krein measure
(the `s` factor kills the Krein atom at `0` and shifts the support one `q̃`-step),
verified in the probe to `1.6e-116` at every truncation order.

That identity is not a coincidence of the SW core — it is a **rigidity**: the
S-map fixes a moment sequence precisely when the sequence is log-quadratic, i.e.
of Stieltjes–Wigert / log-normal type.  This file proves that rigidity, and the
division-free consequence that detects failure of S-fixedness in one line.

The point for the selection question: the balanced family fails `sFixed`
(its moment ratios carry the Jackson factor `1 − p^{k+1}`), so `F = S(K)` is
exact only on the SW core and asymptotic for the balanced family.

## What is NOT here

No analysis, no measure theory, no self-adjoint extension theory: this file
formalises only the algebraic rigidity, which is the load-bearing step.  The
identification of the truncation limits with the Friedrichs and Krein
extensions is literature (`[pedersen1995]`, `[simon1998]`) and is not formalised
here.  No conjecture carrier is declared and nothing is assumed.

Base ring: generic `CommRing` throughout (§7c) — the statement is purely
algebraic and no archimedean construct appears.

-- Ref: [christiansen2003sw] https://doi.org/10.1016/S0022-247X(02)00534-6
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic.Ring

namespace QOU.Archimedean.FvkSMapRigidity

variable {R : Type*} [CommRing R]

/-- **S-fixedness.** The moment sequence `m` is fixed by the `s`-multiplication
map with ratio `c`: each moment is the previous one times `c^k · m 1`.  This is
exactly the condition `c^{-k} · m (k+1) / m 1 = m k` written without division. -/
def SFixed (m : ℕ → R) (c : R) : Prop :=
  ∀ k : ℕ, m (k + 1) = c ^ k * m 1 * m k

/-- **Rigidity, forward direction.** An S-fixed normalised moment sequence is
log-quadratic: `m k = (m 1)^k · c^{k(k−1)/2}`, the Stieltjes–Wigert shape.

This is the sense in which `F = S(K)` is an SW-only phenomenon: the S-map has a
fixed point exactly at the log-quadratic sequences. -/
theorem sFixed_closed_form {m : ℕ → R} {c : R} (h1 : m 0 = 1) (h : SFixed m c) :
    ∀ k : ℕ, m k = m 1 ^ k * c ^ (k.choose 2) := by
  intro k
  induction k with
  | zero => simpa using h1
  | succ n ih =>
      have hchoose : (n + 1).choose 2 = n + n.choose 2 := by
        simpa [Nat.choose_one_right] using Nat.choose_succ_succ n 1
      rw [h n, ih, hchoose]
      ring

/-- **Rigidity, converse direction.** Every log-quadratic sequence is S-fixed.
Together with `sFixed_closed_form` this pins the fixed-point set of the S-map
exactly. -/
theorem closed_form_sFixed {m : ℕ → R} {c : R}
    (h : ∀ k : ℕ, m k = m 1 ^ k * c ^ (k.choose 2)) : SFixed m c := by
  intro k
  have hchoose : (k + 1).choose 2 = k + k.choose 2 := by
    simpa [Nat.choose_one_right] using Nat.choose_succ_succ k 1
  rw [h (k + 1), h k, hchoose]
  ring

/-- **The division-free detector.** S-fixedness forces the second-ratio identity
`c · m(k+1)² = m(k+2) · m k` — a constant-in-`k` relation.

This is what fails for the balanced family: its exact moment ratio
`m(k+1)/m(k) = q̃^k · E · (1 − p^{k+1})` makes the corresponding second ratio
`q̃ · (1 − p^{k+2})/(1 − p^{k+1})` depend on `k`.  So the balanced moment problem
admits no exact S-map, and `F = S(K)` holds for it only asymptotically. -/
theorem sFixed_second_ratio {m : ℕ → R} {c : R} (h : SFixed m c) (k : ℕ) :
    c * m (k + 1) ^ 2 = m (k + 2) * m k := by
  have h1 : m (k + 1) = c ^ k * m 1 * m k := h k
  have h2 : m (k + 2) = c ^ (k + 1) * m 1 * m (k + 1) := h (k + 1)
  rw [h2, h1]
  ring

/-- **Contrapositive form**, the shape actually used against the balanced family:
if the second-ratio identity fails at a single index, the sequence is not
S-fixed for that `c`. -/
theorem not_sFixed_of_second_ratio_ne {m : ℕ → R} {c : R} (k : ℕ)
    (hne : c * m (k + 1) ^ 2 ≠ m (k + 2) * m k) : ¬ SFixed m c :=
  fun h => hne (sFixed_second_ratio h k)

end QOU.Archimedean.FvkSMapRigidity
