import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import QOU.GroundRingCore

/-!
# §3  Substrate Parameter, Gauge Group, Planck Constant

The substrate parameter, the quantum gauge group family `{SU_{q(p)}(2)}`, and
the quantum Planck constant `ℏ_q = 1 − q⁻¹`.

## Two layers, either side of the §7c wall (bean `qou-6ome`)

`SubstrateParameter` used to be a single archimedean structure — `field : M → ℝ`
carrying `field_pos`, `field_ge_one` and `not_root_of_unity` — and that
disagreed with both the block and the co-located siblings:

* `def:substrate-parameter` defines the substrate parameter as
  **`q ∈ End(𝟙)`** — categorical, no ordering, no `q ≥ 1`, no `ℝ`.
* the siblings (`quantum-observable-universes/substrate-parameter.lean`,
  `quantum-gauge-group.lean`) had already migrated to the two-layer shape,
  recording that "the archimedean properties … live on
  `ArchimedeanSubstrateField` … **after the substrate→archimedean wall
  (AGENTS.md §7c)**".

So the migration had reached the block and the siblings and never reached the
library. Now:

| layer | what it is |
|---|---|
| `SubstrateParameter M` | categorical: `field : M → R_q`, matching the block |
| `ArchimedeanSubstrateField M` | the former structure, renamed — `M → ℝ` with the order axioms |

The rename is *not* a demotion of the archimedean layer: it keeps all four
fields, so every one of the 87 references across 22 library modules kept
working unchanged. What it fixes is the **name**: `SubstrateParameter` now
means what `def:substrate-parameter` says it means, and the real-valued
specialisation is honestly labelled as living past the wall.

Neither gate caught this, and the reason is worth remembering:
`check-wall-side` and `check-base-ring` both **PASS** on a file that is
*wholly* archimedean, because they fire on files that *mix* regimes. Passing
the wall gate means "not mixed", not "on the right side of the wall".
-/


namespace QOU

/-! ## §3  Substrate Parameter, Gauge Group, Planck Constant -/

/-- **Substrate parameter** (categorical), the block's own definition: the
    fibre coordinate `q ∈ End(𝟙)`, recorded pointwise as a field over the
    formal ground ring `R_q = ℤ[q, q⁻¹]`.

    Un-ordered by construction. `q(p) > 0`, `q(p) ≥ 1` and "not a root of
    unity" are **archimedean** facts and live on `ArchimedeanSubstrateField`
    below, past the §7c wall.

    LaTeX: `\label{def:substrate-parameter}` -/
structure SubstrateParameter (M : Type*) where
  /-- The categorical substrate field `q : M → R_q`. Records the local value
      of the `End(𝟙) ≅ R_q`-element at each point `p`. -/
  field : M → QOU.GroundRing.R_q

/-- **Archimedean substrate field**: the substrate parameter as a genuine real
    field `q : M → ℝ`.

    This is the structure that used to be called `SubstrateParameter`; the
    rename is about which side of the §7c wall the name advertises, not about
    weakening what is assumed. `field_pos` is the one field that did not
    survive as a field — it is derivable, and is a theorem below.

    **`field` here is independent by construction.** This docstring used to say
    the structure was "obtained by specialising the categorical field through
    `ι : R_q → ℝ, q ↦ q₀`" — prose asserting a tie the type did not carry.
    Nothing related `field` to `SubstrateParameter.field`, so an instance could
    pair a real field with an entirely unrelated categorical one.

    To get the specialisation that prose described, build a
    `QOU.Archimedean.ArchimedeanRealisation` and take
    `toArchimedeanSubstrateField`. There `ι` is **constructed**, not assumed
    (`QOU/Archimedean/GroundRingEval.lean`, bean `qou-d8m1`): `R_q` is
    `LaurentPolynomial ℤ`, so evaluation at a real unit is an ordinary ring
    hom. This bare structure is kept for call sites that need only the
    archimedean data. -/
structure ArchimedeanSubstrateField (M : Type*) where
  /-- The substrate field `q : M → ℝ` with `q(p) ≥ 1`. -/
  field : M → ℝ
  /-- **Classicality bound**: `q(p) ≥ 1` at every point.

      `q(p) = 1` is the classical limit (`ℏ_q = 0`); `q(p) > 1` is the quantum
      regime, where the physical substrate sits. -/
  field_ge_one : ∀ (p : M), 1 ≤ field p
  /-- `q₀(p)` is never a root of unity.

      Independent of `field_ge_one` and so genuinely a field: `q = 1` satisfies
      `1 ≤ q` and *is* a root of unity, so the bound alone does not exclude it.
      Note this is a library-side assumption — `substrate-parameter.md` states
      the substrate parameter as `q ∈ End(𝟙)` and says nothing about roots of
      unity. Recorded rather than quietly relied on (bean `qou-6ome`). -/
  not_root_of_unity : ∀ (p : M) (k : ℕ), k ≥ 1 → field p ^ k ≠ 1

/-- **Positivity is derived, not assumed.**

    This was a fourth field, `field_pos`, sitting beside `field_ge_one` — and
    `0 < q` follows from `1 ≤ q` by transitivity with `0 < 1`. Positing both
    made the structure carry a redundant axiom, which is exactly what the
    co-located sibling avoided: its docstring says the classicality bound is
    the *single* archimedean axiom, "from which positivity, invertibility, and
    the non-negativity of the quantum Planck displacement are derived".

    Kept under the same name, so every existing `sp.field_pos p` call site
    reads identically — dot notation resolves to this theorem exactly as it
    resolved to the field. -/
theorem ArchimedeanSubstrateField.field_pos {M : Type*}
    (sp : ArchimedeanSubstrateField M) (p : M) : 0 < sp.field p :=
  lt_of_lt_of_le zero_lt_one (sp.field_ge_one p)

/-- **Quantum gauge group**: the family `{SU_{q(p)}(2)}_{p ∈ M}`.
    LaTeX: `\label{def:quantum-gauge-group}` -/
structure QuantumGaugeGroup (M : Type*) extends ArchimedeanSubstrateField M where
  /-- The quantum group at each point. -/
  groupAt : M → Type*

/-- **Quantum Planck constant**: `ℏ_q(p) = 1 − q(p)⁻¹`.
    LaTeX: `\label{def:quantum-planck-constant}` -/
noncomputable def quantumPlanckConstant {M : Type*} (sp : ArchimedeanSubstrateField M)
    (p : M) : ℝ :=
  1 - (sp.field p)⁻¹

/-- The quantum Planck constant takes values in `[0, 1)`. -/
theorem quantumPlanckConstant_nonneg {M : Type*} (sp : ArchimedeanSubstrateField M)
    (p : M) : 0 ≤ quantumPlanckConstant sp p := by
  unfold quantumPlanckConstant
  have hq := sp.field_ge_one p
  have hpos := sp.field_pos p
  have hne : sp.field p ≠ 0 := hpos.ne'
  -- (sp.field p)⁻¹ ≤ 1 follows from 1 ≤ sp.field p via multiplication
  nlinarith [mul_le_mul_of_nonneg_right hq (le_of_lt (inv_pos.mpr hpos)),
             mul_inv_cancel₀ hne]

theorem quantumPlanckConstant_lt_one {M : Type*} (sp : ArchimedeanSubstrateField M)
    (p : M) : quantumPlanckConstant sp p < 1 := by
  unfold quantumPlanckConstant
  have hpos := sp.field_pos p
  have hinv : 0 < (sp.field p)⁻¹ := inv_pos.mpr hpos
  linarith

end QOU
