import QOU.QuantumObservableUniverse.SubstrateParameter
import QOU.AppendixSurreals.QCollatz

/-!
# The Skein-Collatz map descends from a QOU substrate parameter (Tier C, C8 brick 2)

Brick 1 (`SkeinCollatzArith`, in `QCollatz.lean`) showed the Skein-Collatz
`q`-arithmetic is determined by a single ring element `q`. This file closes
**brick 2**: that `q` is the **QOU substrate parameter** — the map's arithmetic
is *derived from an actual `ArchimedeanSubstrateField`* of the framework, not posited.

`QOU.ArchimedeanSubstrateField M` (`def:substrate-parameter`) furnishes, at each point
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
    A `ArchimedeanSubstrateField M` at a point `p` furnishes the substrate field `q(p)`;
    this is the `q` of the induced `SkeinCollatzArith` over `ℝ`. Every brick-1
    identity (`skein_divisibility`, `contraction_gap`, `coprime`,
    `fundamental_odd_step`) therefore holds for the substrate value, by
    construction. -/
def ArchimedeanSubstrateField.toSkeinCollatzArith {M : Type*}
    (sp : ArchimedeanSubstrateField M) (p : M) : SkeinCollatzArith ℝ where
  q := sp.field p

@[simp] theorem ArchimedeanSubstrateField.toSkeinCollatzArith_q {M : Type*}
    (sp : ArchimedeanSubstrateField M) (p : M) :
    (sp.toSkeinCollatzArith p).q = sp.field p := rfl

/-- The Skein divisibility `[3]_q = q·[2]_q + 1` holds for the substrate value —
    a direct consequence of brick 1, now anchored at `q = q(p)`. -/
theorem skein_divisibility_at {M : Type*}
    (sp : ArchimedeanSubstrateField M) (p : M) :
    (sp.toSkeinCollatzArith p).qi3
      = sp.field p * (sp.toSkeinCollatzArith p).qi2 + 1 :=
  (sp.toSkeinCollatzArith p).skein_divisibility

/-- **The substrate makes the fundamental 2-cycle honest.** Because the substrate
    field is strictly positive (`field_pos`), `q(p)` is invertible, so the
    fundamental odd-step identity holds at `qinv = q(p)⁻¹`: the `{q⁻¹, 1+q⁻¹}`
    cycle of the Skein-Collatz map is realised by the substrate value itself. -/
theorem fundamental_odd_step_at {M : Type*}
    (sp : ArchimedeanSubstrateField M) (p : M) :
    (1 + (sp.field p)⁻¹) * (sp.toSkeinCollatzArith p).qi2
      = (sp.toSkeinCollatzArith p).qi3 * (sp.field p)⁻¹ + 1 :=
  (sp.toSkeinCollatzArith p).fundamental_odd_step (sp.field p)⁻¹
    (mul_inv_cancel₀ (sp.field_pos p).ne')

/-! ### C8 brick 3 — the arithmetic on the Reeb-bundle Skein module `𝒮(q) ≅ ℤ[q^±1]`

The Reeb-bundle Skein module (`prop:skein-generation`) is
`𝒮(q) ≅ ℤ[q^{±1}] = LaurentPolynomial ℤ` — the ground ring `R_q` of the formal
chain (`GroundRingAnnotations`) — with `q` the module indeterminate `T`.
Instantiating `SkeinCollatzArith` there realises the map's whole `q`-arithmetic on
the **actual Skein module**, and `q = T` is a unit (inverse `T(-1)`,
`qcollatz_laurent_qunit`), so the fundamental cycle lives in `𝒮(q)`.

Together with brick 2 this exhibits the *two levels of `q`*: the **fibre** `q = T`
in `𝒮(q) = ℤ[q^{±1}]` (this brick) and its **archimedean evaluation**
`q = q(p) ∈ ℝ` at a substrate point (brick 2) — the substrate→fibre picture of
`AGENTS.md §"Im(q) at fibre vs observable level"`. -/

open LaurentPolynomial in
/-- **C8 brick 3 — the Skein-Collatz arithmetic on `𝒮(q) = ℤ[q^{±1}]`**, with `q`
    the module indeterminate `T`. -/
noncomputable def skeinModuleArith : SkeinCollatzArith (LaurentPolynomial ℤ) where
  q := T 1

open LaurentPolynomial in
/-- On the Skein module the q-integer is `[2]_q = T + 1` (`q + 1` with `q = T`). -/
theorem skeinModuleArith_qi2 : skeinModuleArith.qi2 = T 1 + 1 := rfl

open LaurentPolynomial in
/-- On the Skein module `𝒮(q) = ℤ[q^{±1}]`, `q = T` is a unit (inverse `T(-1)`),
    so the fundamental odd-step identity holds — the `{q⁻¹, 1+q⁻¹}` cycle is
    realised in the actual Skein module. -/
theorem skeinModuleArith_fundamental_odd_step :
    (1 + T (-1)) * skeinModuleArith.qi2 = skeinModuleArith.qi3 * T (-1) + 1 :=
  skeinModuleArith.fundamental_odd_step (T (-1)) qcollatz_laurent_qunit

end QOU
