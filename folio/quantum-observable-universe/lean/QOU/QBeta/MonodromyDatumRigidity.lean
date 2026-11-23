import QOU.QBeta.CyclicDilogPentagon

/-!
# The A_ω monodromy datum is a pentagon-rigidity invariant

Continuation of the L4 Faddeev–Volkov rigidity lever
(`QOU.QBeta.CyclicDilogPentagon`): the keystone gap of the c₃ bar-odd `S`
program is **G3**, the *argument-identification / monodromy datum*
`z(q₀) → S` — no `FaddeevPhi` argument has yet been exhibited whose
archimedean evaluation reproduces the anchor targets
`S(muon) = +0.00968298`, `S(proton) = −0.03945936`
(`docs/audits/2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md`
§G3, "the load-bearing gap").

Two independent results sharpen *what kind of object* that datum is, and
together they say the datum is a **scale-invariant monodromy**, not a
resummation constant:

* **It is non-perturbative.** The deformed Ohtsuki tower at the substrate
  meridian obeys `arg κ̃_n = −n·arctan(t/π)` exactly (phase law, main
  commit `c821747763`): the perturbative tower carries **no intrinsic odd
  phase**, so any genuine odd monodromy phase — the bar-odd `S` seat — is
  non-perturbative. A non-perturbative jump across a Stokes line is a
  ratio of analytic continuations: intrinsically **scale-invariant** (the
  overall normalisation of `Φ_b` cancels in the monodromy).

* **It is rigidity-determined.** L4 (`CyclicDilogPentagon`) proved, modulo
  the honestly-carried open `PentagonRigidity` input (§3b-cond, the
  Liouville doubly-periodic-⇒-constant step absent from Mathlib), that any
  two nowhere-zero `FaddeevPhi` solutions are equal once normalised at a
  point.

This file composes the two into the structural statement the lane exists to
make: **every scale-invariant readout of a `FaddeevPhi` solution is the
same on all solutions** (`monodromy_datum_rigidity`). Hence the bar-odd
monodromy datum `A_ω` extracted from *any* `Φ_b` representative is one and
the same pentagon-forced invariant — it carries **no fitting freedom**,
which is precisely what "the datum is forced, not fitted" means for the G3
keystone.

## Honest scope

This does **not** close G3: it does not *compute* `A_ω`, and it inherits the
open `PentagonRigidity` hypothesis (the pentagon's Liouville content). What
it removes is the "which solution / which normalisation" degree of freedom —
proving that the readout is well-posed as an invariant of `b` alone. The
concrete `qpRatio` readout is proved scale-invariant unconditionally as a
non-vacuous witness; by `phi_b_quasiperiod` it is even solution-independent
*without* the pentagon (it equals the fixed quasi-period factor), so the
pentagon input is the load-bearing ingredient only for the *dual /
large-argument* monodromy that the local `ib`-quasi-period does not pin.
No `c_k` is produced or wired; registry untouched; scope-(a) throughout.

-- Ref: [faddeev_kashaev1994] Faddeev–Kashaev, "Quantum dilogarithm",
--        Mod. Phys. Lett. A 9 (1994) 427. https://doi.org/10.1142/S0217732394000447
-- Ref: [leitner2026] docs/audits/2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md (G3)
-/

namespace QOU.QBeta.MonodromyDatumRigidity

open Complex
open QOU.MathlibExt.FaddeevQuantumDilogarithm
open QOU.QBeta.CyclicDilogPentagon

/-- **Scale-invariant readout.** A functional `D` of a candidate solution that
is unchanged when the solution is rescaled by a nonzero constant. A monodromy /
Stokes datum — a ratio of analytic continuations — is of this form: the overall
normalisation of `Φ_b` cancels. -/
def ScaleInvariant {X : Type*} (D : (ℂ → ℂ) → X) : Prop :=
  ∀ c : ℂ, c ≠ 0 → ∀ Ψ : ℂ → ℂ, D (fun z => c * Ψ z) = D Ψ

/-- **The monodromy datum is a pentagon-rigidity invariant.** Assuming pentagon
rigidity (`PentagonRigidity b Φ`, the L4 open input) and given two nowhere-zero
`FaddeevPhi` solutions at `b`, **every** scale-invariant readout `D` takes the
*same value* on both. The bar-odd datum `A_ω` read off any `Φ_b` representative
is therefore one pentagon-forced invariant — no fitting freedom.

Derivation: rigidity gives `Φᵢ = cᵢ·Φ` pointwise; nowhere-vanishing forces
`cᵢ ≠ 0`; scale-invariance collapses both readouts to `D Φ`. -/
theorem monodromy_datum_rigidity {b : ℂ} {Φ Φ₁ Φ₂ : ℂ → ℂ} {X : Type*}
    (hR : PentagonRigidity b Φ)
    (h₁ : FaddeevPhi b Φ₁) (h₂ : FaddeevPhi b Φ₂)
    (hn₁ : ∀ z, Φ₁ z ≠ 0) (hn₂ : ∀ z, Φ₂ z ≠ 0)
    {D : (ℂ → ℂ) → X} (hD : ScaleInvariant D) :
    D Φ₁ = D Φ₂ := by
  obtain ⟨c₁, hc₁⟩ := hR.uniqueUpToScalar Φ₁ h₁ hn₁
  obtain ⟨c₂, hc₂⟩ := hR.uniqueUpToScalar Φ₂ h₂ hn₂
  have hc₁0 : c₁ ≠ 0 := fun h => hn₁ 0 (by rw [hc₁ 0, h, zero_mul])
  have hc₂0 : c₂ ≠ 0 := fun h => hn₂ 0 (by rw [hc₂ 0, h, zero_mul])
  have e₁ : Φ₁ = fun z => c₁ * Φ z := funext hc₁
  have e₂ : Φ₂ = fun z => c₂ * Φ z := funext hc₂
  rw [e₁, e₂, hD c₁ hc₁0 Φ, hD c₂ hc₂0 Φ]

/-- **Concrete scale-invariant readout — the quasi-period ratio.** The functional
`Ψ ↦ (z ↦ Ψ(z + ib)/Ψ(z))` is scale-invariant: a nonzero constant cancels in the
quotient. A non-vacuous witness that `ScaleInvariant` functionals exist. -/
theorem qpRatio_scaleInvariant {b : ℂ} :
    ScaleInvariant (fun (Ψ : ℂ → ℂ) => fun z => Ψ (z + I * b) / Ψ z) := by
  intro c hc Ψ
  funext z
  exact mul_div_mul_left _ _ hc

/-- **The quasi-period readout is already solution-independent** (no pentagon
needed): for two `FaddeevPhi` solutions at `b`, wherever both are nonzero the
ratio `z ↦ Φ(z + ib)/Φ(z)` agrees, because `phi_b_quasiperiod` fixes it to the
common quasi-period factor `1 + q_b·e^{2πbz}`. This is the *local* half; the
pentagon input of `monodromy_datum_rigidity` is what extends invariance to the
*dual / large-argument* monodromy the local quasi-period does not pin. -/
theorem qpRatio_solution_independent {b : ℂ} {Φ₁ Φ₂ : ℂ → ℂ}
    [FaddeevPhi b Φ₁] [FaddeevPhi b Φ₂] (z : ℂ)
    (hz₁ : Φ₁ z ≠ 0) (hz₂ : Φ₂ z ≠ 0) :
    Φ₁ (z + I * b) / Φ₁ z = Φ₂ (z + I * b) / Φ₂ z := by
  have q1 := phi_b_quasiperiod (b := b) (Φ := Φ₁) z
  have q2 := phi_b_quasiperiod (b := b) (Φ := Φ₂) z
  -- Φᵢ z = P · Φᵢ (z+ib) with a common factor P; solve each for the ratio.
  set P : ℂ := 1 + Complex.exp (I * (Real.pi : ℂ) * (b : ℂ) ^ 2)
      * Complex.exp (2 * (Real.pi : ℂ) * b * z) with hP
  have hz1b : Φ₁ (z + I * b) ≠ 0 := fun h => hz₁ (by rw [q1, h, mul_zero])
  have hz2b : Φ₂ (z + I * b) ≠ 0 := fun h => hz₂ (by rw [q2, h, mul_zero])
  rw [q1, q2]
  rw [mul_comm P (Φ₁ (z + I * b)), mul_comm P (Φ₂ (z + I * b)),
    ← div_div, ← div_div, div_self hz1b, div_self hz2b]

end QOU.QBeta.MonodromyDatumRigidity
