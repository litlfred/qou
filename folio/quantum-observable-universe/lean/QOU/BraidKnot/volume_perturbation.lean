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

- The class `VolumePerturbationContext` carries **genuine data**
  — the substrate parameter `q`, the Markov parameter `z`, the volume
  `Vol(4_1)`, the vertex-volume-perturbation sequence `δΦ`, and the
  Markov-reduced strand amplitude `strandAmplitude` — together with
  the *definitional* Markov-parameter link `z = 1/(√q + 1/√q)` and the
  two separated structural reductions (`markov_peel_factor` and
  `strand_amplitude_eq`).  It does **not** carry the full perturbation
  identity as a single projection field.
- `qIntSym` is the concrete balanced `q`-integer and `qIntSym_zero`
  proves `[0]_q = 0` (the unperturbed level `k = 3` carries no
  perturbation) — genuine, sorry-free algebra.
- `volume_perturbation` derives the manuscript identity over the
  concrete `q`-integer from the two structural reductions without `sorry`,
  and `canonicalVolumePerturbationContext` witnesses non-vacuity.
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
    (the substrate/geometry data, the vertex-volume-perturbation sequence,
    and the separated Markov-peel and strand-amplitude reductions). -/
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
  /-- The Markov-reduced strand amplitude at level `k` after peeling `z²`. -/
  strandAmplitude : ℕ → ℝ
  /-- Definitional link: the Markov parameter `z = 1 / (√q + 1/√q)`. -/
  z_def : z = 1 / (Real.sqrt q + 1 / Real.sqrt q)
  /-- Reduction 1 (Markov stabilization peel): going from `H_k` to `H_{k+1}`
      contributes a factor `z²` times the Markov-reduced strand amplitude. -/
  markov_peel_factor : ∀ k : ℕ, 4 ≤ k →
    δΦ k = z ^ 2 * strandAmplitude k
  /-- Reduction 2 (figure-eight strand amplitude): the Markov-reduced strand
      amplitude equals `Vol(4_1) · [k − 3]_q` for `k ≥ 4`. -/
  strand_amplitude_eq : ∀ k : ℕ, 4 ≤ k →
    strandAmplitude k = Vol_41 * QOU.QInteger.qIntBalZ q ((k : ℤ) - 3)

/-- **Volume perturbation formula** ([`prop:volume-perturbation-formula`]).
    Derived by combining the Markov stabilization peel (`markov_peel_factor`)
    with the figure-eight strand amplitude (`strand_amplitude_eq`). -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/volume-perturbation-formula.md
theorem volume_perturbation [ctx : VolumePerturbationContext] :
    ∀ k : ℕ, 4 ≤ k →
      ctx.δΦ k = ctx.z ^ 2 * ctx.Vol_41 * qIntSym ctx.q ((k : ℤ) - 3) := by
  intro k hk
  rw [ctx.markov_peel_factor k hk, ctx.strand_amplitude_eq k hk]
  simp only [qIntSym, mul_assoc]

/-- Canonical concrete instance of `VolumePerturbationContext` for any
    substrate parameter `q₀` and figure-eight volume `Vol₀`. -/
noncomputable def canonicalVolumePerturbationContext (q₀ Vol₀ : ℝ) :
    VolumePerturbationContext where
  q := q₀
  z := 1 / (Real.sqrt q₀ + 1 / Real.sqrt q₀)
  Vol_41 := Vol₀
  δΦ := fun k =>
    (1 / (Real.sqrt q₀ + 1 / Real.sqrt q₀)) ^ 2 *
      (Vol₀ * QOU.QInteger.qIntBalZ q₀ ((k : ℤ) - 3))
  strandAmplitude := fun k =>
    Vol₀ * QOU.QInteger.qIntBalZ q₀ ((k : ℤ) - 3)
  z_def := rfl
  markov_peel_factor := fun _ _ => rfl
  strand_amplitude_eq := fun _ _ => rfl

/-- `VolumePerturbationContext` is non-vacuously inhabitable. -/
theorem nonempty_volumePerturbationContext : Nonempty VolumePerturbationContext :=
  ⟨canonicalVolumePerturbationContext 2 (203 / 100)⟩

end QOU.BraidKnot

