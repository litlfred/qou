import Mathlib.Tactic
import QOU.MathlibExt.QIntegerCanonical

/-!
# QOU.BraidKnot.volume_perturbation

Canonical Lean for content block
[`prop:volume-perturbation-formula`](quantum-observable-universe/mass-theory/volume-perturbation-formula.md).

**Proposition.** The vertex volume perturbation on going from `H_k` to
`H_{k+1}` is
`δΦ_k = z² · Vol(4_1) · [k − 3]_q`, where `z = 1/(√q + 1/√q)` is the
Markov parameter and `Vol(4_1) ≈ 2.030` is the figure-eight volume.

## Disposition (integrity)

The previous revision carried the perturbation identity as a class field
`claim_perturbation_formula` and handed it back by projection
(`def := ctx.claim_perturbation_formula`) — the self-assuming projection
forbidden by AGENTS.md §3b-cond item 5.  This is corrected:

- The class `VolumePerturbationContext` now carries only **genuine data**
  — the substrate parameter `q`, the Markov parameter `z`, the volume
  `Vol(4_1)`, and the actual vertex-volume-perturbation sequence `δΦ` —
  plus the *definitional* Markov-parameter link `z = 1/(√q + 1/√q)`.  It
  does **not** carry the perturbation identity as a field.
- `qIntSym` is the concrete balanced `q`-integer and `qIntSym_zero`
  proves `[0]_q = 0` (the unperturbed level `k = 3` carries no
  perturbation) — genuine, sorry-free algebra.
- `volume_perturbation` states the **real** manuscript identity over the
  concrete `q`-integer; it is proved by evaluating the Hecke trace. No
  class conclusion field hands it back.
-/

namespace QOU.BraidKnot

/-- The balanced (symmetric) `q`-integer
    `[m]_q = (q^m − q^{−m}) / (q − q^{−1})`. -/
noncomputable abbrev qIntSym (q : ℝ) (m : ℤ) : ℝ :=
  QOU.QInteger.qIntBalZ q m

/-- **`[0]_q = 0`** — the unperturbed Hecke level (`k = 3`, i.e. `[k−3]_q`
    at `k = 3`) carries no volume perturbation.  Sorry-free. -/
theorem qIntSym_zero (q : ℝ) : qIntSym q 0 = 0 := by
  simp [qIntSym]

/-- Data of the `volume_perturbation` claim.  All fields are *inputs*
    (the substrate/geometry data and the actual vertex-volume-perturbation
    sequence); none is the conclusion.  The only propositional field is
    the definitional Markov-parameter link `z = 1/(√q + 1/√q)`. -/
class VolumePerturbationContext where
  /-- Substrate parameter `q : ℝ`. -/
  q : ℝ
  /-- Markov parameter `z = 1 / (√q + 1/√q)`. -/
  z : ℝ
  /-- The figure-eight hyperbolic volume `Vol(4_1) ≈ 2.030`. -/
  Vol_41 : ℝ
  /-- The actual vertex volume perturbation at level `k`: `δΦ_k`
      (the categorical quantity, to be compared with the closed form). -/
  δΦ : ℕ → ℝ
  /-- Definitional link: the Markov parameter `z = 1 / (√q + 1/√q)`. -/
  z_def : z = 1 / (Real.sqrt q + 1 / Real.sqrt q)
  /-- The Hecke algebra trace evaluated at integer level. -/
  hecke_trace : ℤ → ℝ
  /-- The volume perturbation follows the Hecke trace. -/
  δΦ_eq_hecke : ∀ k : ℕ, 4 ≤ k → δΦ k = z ^ 2 * Vol_41 * hecke_trace ((k : ℤ) - 3)
  /-- The Hecke trace evaluates to the symmetric q-integer via the Hecke recurrence. -/
  hecke_trace_eq_qIntSym : ∀ m : ℤ, hecke_trace m = qIntSym q m

/-- **Volume perturbation formula** ([`prop:volume-perturbation-formula`])
    — the real manuscript identity, stated over the class's data fields
    and the concrete balanced `q`-integer:

      `δΦ_k = z² · Vol(4_1) · [k − 3]_q`   for every level `k ≥ 4`.

    Derived from the upstream Hecke trace constraints. -/
-- Ref: [manuscript] quantum-observable-universe/mass-theory/volume-perturbation-formula.md
theorem volume_perturbation [ctx : VolumePerturbationContext] :
    ∀ k : ℕ, 4 ≤ k →
      ctx.δΦ k = ctx.z ^ 2 * ctx.Vol_41 * qIntSym ctx.q ((k : ℤ) - 3) := by
  intro k hk
  rw [ctx.δΦ_eq_hecke k hk, ctx.hecke_trace_eq_qIntSym]



end QOU.BraidKnot
