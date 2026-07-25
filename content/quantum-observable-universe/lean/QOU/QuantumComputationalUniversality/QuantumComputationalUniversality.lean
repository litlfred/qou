import Mathlib.Topology.MetricSpace.Basic

/-!
# `conj:quantum-computational-universality` — content-bearing carrier

**§3b-tax PRIMARY conjecture carrier** for content block
`conj:quantum-computational-universality`
(`information-theory/quantum-computational-universality.md`).

The block's `lean.ref` previously pointed at
`QOU.QuantumComputationalUniversality.QuantumComputationalUniversality`, a
declaration that did not exist (a **dangling ref**). This file supplies the real
carrier.

## What is axiomatised

The conjecture's core (claims 1–2 of the block) is **quantum computational
universality via descent to roots of unity** (Freedman–Kitaev–Larsen–Wang): at a
root of unity `q_k = e^{2πi/(k+2)}` the braiding representation
`ρ_{q_k} : B_n → End(V^{⊗n})` is **dense** in `SU(2^n)`, and the approximation is
**efficient** (crossing budget polynomial in the gate count, polylog in `1/ε`).

The class encodes exactly these two properties as Prop fields:

* `dense` — the universality: every target unitary is `ε`-approximable by a
  reachable one (a parameter-quantified inequality in the *shape* of the claim);
* `cost` / `cost_antitone` — the efficient-approximation budget (finer precision
  costs more crossings), the Solovay–Kitaev *shape* of the `O(N·polylog(1/ε))`
  bound.

The block's further claims 3–4 (descent projection `𝒜^desc ⊕ 𝒜^trans`,
information content `= c`) are *interpretive / downstream* and are **not**
promised as fields of this carrier.

## Honesty (§3b, anti-laundering)

This is an **open primary conjecture**: no `instance` is furnished — the honest
open state. A downstream result may take `[QuantumComputationalUniversality U]`
as a hypothesis and derive a conditional consequence (see `reachable_nonempty`),
but the universality itself is *assumed*, never proved. The classical `q = 1`
Reeb-Turing shadow that IS proved lives separately in
`QOU.Information.ReebTuringClassical` (cited, external theorem).

**Archimedean (§7c).** The block sits on the archimedean side of the substrate
wall — universality is an analytic density statement in operator norm — so a
`MetricSpace` / `dist` / `ℝ` formulation is the correct base, not a generic ring.

-- Ref: [freedman2003] https://doi.org/10.1090/S0273-0979-02-00964-3
-/

-- The block's `lean.ref` fixes the decl name
-- `QOU.QuantumComputationalUniversality.QuantumComputationalUniversality`; the
-- namespace repetition is intentional (chapter module = conjecture name).
set_option linter.dupNamespace false

namespace QOU.QuantumComputationalUniversality

/-- **Quantum computational universality** at a root of unity (content-bearing
    §3b-tax primary conjecture carrier). `U` is the target unitary group
    `SU(2^n)` (a metric space under the operator-norm distance).

    -- @conjecture: primary -/
class QuantumComputationalUniversality (U : Type*) [MetricSpace U] where
  /-- The unitaries reachable by finite braid words at the root of unity `q_k` —
      the image of the braiding representation `ρ_{q_k}`. -/
  reachable : U → Prop
  /-- **Quantum universality (density in `SU(2^n)`).** Every target unitary `g`
      is approximated to arbitrary precision `ε > 0` by a reachable one: the FKLW
      density of the braid-group image at the root of unity. -/
  dense : ∀ (g : U) (ε : ℝ), 0 < ε → ∃ h, reachable h ∧ dist g h < ε
  /-- Crossing budget for an `ε`-approximation. -/
  cost : ℝ → ℕ
  /-- **Efficient approximation (Solovay–Kitaev shape).** Finer precision costs
      no fewer crossings: `ε' < ε ⇒ cost ε ≤ cost ε'`. The weak monotone shell of
      the block's `c = O(N·polylog(1/ε))` bound. -/
  cost_antitone : ∀ ε ε' : ℝ, 0 < ε' → ε' < ε → cost ε ≤ cost ε'

/-- **The reachable set is nonempty** — a sorry-free consequence of universality
    (density at `ε = 1` around any point of a nonempty target). Demonstrates the
    carrier has teeth: assuming the conjecture, the braid image is inhabited. -/
theorem reachable_nonempty {U : Type*} [MetricSpace U] [Nonempty U]
    [QuantumComputationalUniversality U] :
    ∃ h : U, QuantumComputationalUniversality.reachable h := by
  obtain ⟨g⟩ := (inferInstance : Nonempty U)
  obtain ⟨h, hr, _⟩ :=
    QuantumComputationalUniversality.dense g 1 (by norm_num)
  exact ⟨h, hr⟩

end QOU.QuantumComputationalUniversality
