import QOU.QuantumObservableUniverse.SubstrateParameter
import QOU.AppendixSurreals.QCollatz

/-!
# The Skein-Collatz map descends from a QOU substrate parameter (Tier C, C8 brick 2)

Brick 1 (`SkeinCollatzArith`, in `QCollatz.lean`) showed the Skein-Collatz
`q`-arithmetic is determined by a single ring element `q`. This file closes
**brick 2**: that `q` is the **QOU substrate parameter** — the map's arithmetic
is *derived from an actual `SubstrateParameter`* of the framework, not posited.

`QOU.SubstrateParameter M` (`def:substrate-parameter`) furnishes, at each point
`p ∈ M`, the substrate field `q(p) : ℝ` with `q(p) ≥ 1 > 0` and never a root of
unity. Feeding `q(p)` to `SkeinCollatzArith` realises the whole map arithmetic —
`[2]_q`, `[3]_q`, the Skein divisibility identity, the contraction gap, the
Bézout coprimality and the fundamental `{q⁻¹, 1+q⁻¹}` cycle — over `ℝ`, from the
substrate value. The substrate's positivity axiom (`field_pos`) is exactly what
makes the fundamental cycle honest (`q(p)` invertible).

Honest scope: this links the Skein-Collatz `q` to the substrate parameter object
(where `q` genuinely lives — `QuantumUniverse` deliberately has no `q` field; it
"enters via the substrate parameter"). It derives the *arithmetic*; the dynamical
conjecture (`reaches_cycle`) and its `μ` remain the open walls. No axiomatisation.
-/

namespace QOU

open QOU.AppendixSurreals

/-- **C8 brick 2 — the Skein-Collatz arithmetic is the QOU substrate parameter.**
    A `SubstrateParameter M` at a point `p` furnishes the substrate field `q(p)`;
    this is the `q` of the induced `SkeinCollatzArith` over `ℝ`. Every brick-1
    identity (`skein_divisibility`, `contraction_gap`, `coprime`,
    `fundamental_odd_step`) therefore holds for the substrate value, by
    construction. -/
def SubstrateParameter.toSkeinCollatzArith {M : Type*}
    (sp : SubstrateParameter M) (p : M) : SkeinCollatzArith ℝ where
  q := sp.field p

@[simp] theorem SubstrateParameter.toSkeinCollatzArith_q {M : Type*}
    (sp : SubstrateParameter M) (p : M) :
    (sp.toSkeinCollatzArith p).q = sp.field p := rfl

/-- The Skein divisibility `[3]_q = q·[2]_q + 1` holds for the substrate value —
    a direct consequence of brick 1, now anchored at `q = q(p)`. -/
theorem SubstrateParameter.skein_divisibility_at {M : Type*}
    (sp : SubstrateParameter M) (p : M) :
    (sp.toSkeinCollatzArith p).qi3
      = sp.field p * (sp.toSkeinCollatzArith p).qi2 + 1 :=
  (sp.toSkeinCollatzArith p).skein_divisibility

/-- **The substrate makes the fundamental 2-cycle honest.** Because the substrate
    field is strictly positive (`field_pos`), `q(p)` is invertible, so the
    fundamental odd-step identity holds at `qinv = q(p)⁻¹`: the `{q⁻¹, 1+q⁻¹}`
    cycle of the Skein-Collatz map is realised by the substrate value itself. -/
theorem SubstrateParameter.fundamental_odd_step_at {M : Type*}
    (sp : SubstrateParameter M) (p : M) :
    (1 + (sp.field p)⁻¹) * (sp.toSkeinCollatzArith p).qi2
      = (sp.toSkeinCollatzArith p).qi3 * (sp.field p)⁻¹ + 1 :=
  (sp.toSkeinCollatzArith p).fundamental_odd_step (sp.field p)⁻¹
    (mul_inv_cancel₀ (sp.field_pos p).ne')

end QOU
