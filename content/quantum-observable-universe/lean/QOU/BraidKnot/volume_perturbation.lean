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
  concrete `q`-integer; it is unproved (`sorry` + manuscript citation per
  AGENTS.md §1a disposition 2 — the identity between the categorical
  vertex-volume perturbation `δΦ` and the closed form is the empirically
  verified content, not a Mathlib-derivable one).
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

/-- **Volume perturbation formula** ([`prop:volume-perturbation-formula`])
    — the real manuscript identity, stated over the class's data fields
    and the concrete balanced `q`-integer:

      `δΦ_k = z² · Vol(4_1) · [k − 3]_q`   for every level `k ≥ 4`.

    Unproved: the identity between the categorical vertex-volume
    perturbation `δΦ` (empirically verified for Ca, Fe at `k = 5,6,7`)
    and the closed form is a manuscript-level result, not derivable in
    Mathlib.  Stated with `sorry` + citation per AGENTS.md §1a
    disposition 2 — no conclusion field on the class hands this back. -/
-- Ref: [manuscript] quantum-observable-universe/mass-theory/volume-perturbation-formula.md
theorem volume_perturbation [ctx : VolumePerturbationContext] :
    ∀ k : ℕ, 4 ≤ k →
      ctx.δΦ k = ctx.z ^ 2 * ctx.Vol_41 * qIntSym ctx.q ((k : ℤ) - 3) := by
  -- Ref: [manuscript] quantum-observable-universe/mass-theory/volume-perturbation-formula.md
  sorry

/-- **The statement above is refutable as written** — the class never relates
    the fields its conclusion names, so `∀ instances` admits ones that simply
    disagree. Not an open gap: the `sorry` cannot be discharged. Fixing it
    means giving the class the hypotheses the derivation needs (bean qou-octr,
    criterion §10 `proof-unclosable-context-sorry`). This refutation is the
    evidence, not the fix. -/
theorem volume_perturbation_unconstrained_false :
    ¬ ∀ ctx : VolumePerturbationContext, ∀ k : ℕ, 4 ≤ k →
        ctx.δΦ k = ctx.z ^ 2 * ctx.Vol_41 * qIntSym ctx.q ((k : ℤ) - 3) := by
  intro h
  have := h { q := 1, z := 1 / (Real.sqrt 1 + 1 / Real.sqrt 1), Vol_41 := 0,
              δΦ := fun _ => 1, z_def := rfl } 4 (by norm_num)
  norm_num at this

end QOU.BraidKnot
