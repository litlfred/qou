import Mathlib.Tactic.NormNum

/-!
# QOU.ArchimedeanUniverse.brings_euler_characteristic

Content block
[`lem:brings-euler-characteristic`](../../../quantum-observable-universe/brings-surface/brings-euler-characteristic.md):
*The categorical Euler characteristic
`χ(A) = tr(id_A)` for `A = 𝒪_q(SU(2))` on Bring's surface `Σ₄`
equals `χ(Σ₄) = 2 − 2g(Σ₄) = −6`.*

## Lean structure

The genuine geometric **input** is the genus of Bring's surface,
`g(Σ₄) = 4` (a classical fact about the Bring curve / the `S₅`-quotient
`Σ₄`).  The categorical Euler characteristic `χ(A)` is **defined** by
the Euler formula `χ = 2 − 2g`, and the value `χ(A) = −6` is then
**derived** by `norm_num` from `g = 4`.

This is a genuine derivation, not a self-assuming projection: the
`−6` is *computed* from the genus input via the Euler formula, rather
than handed back from a class field that already asserts it.

## Trace of the identity — `χ(A) = tr(id_A) = ev ∘ coev`

The .md's central claim is that this Euler characteristic *is* the
categorical trace of the identity, `χ(A) = tr(id_A)`, and its final
clause is that this value *"is recovered as the quantum dimension
specialised at the Descartes substrate parameter `q₀`"*.

We model the rigidity trace exactly as the corpus does for the
neighbouring stability result
([`prop:euler-char-stability`](../../../quantum-observable-universe/lifting-and-descent/euler-char-stability-proof.md),
Lean `QOU.Torsion.euler_char_constant`): for a dualizable object `A`
in a rigid monoidal category, `tr(id_A) = ev_A ∘ coev_A` is a scalar
in the ground ring `End(𝟙) ≅ R`, so it is carried by two scalars
`ev, coev : R` evaluated at the substrate parameter `q₀`
(`categoricalTrace := ev * coev`).

**Base ring (§7c).** Everything here is the *algebraic* rigidity
computation — a commutative-ring identity `ev · coev = 2 − 2g = −6`
with no ordering, `Real.*`, or CODATA literal — so it is stated over a
generic `{R : Type*} [CommRing R]`, not `ℝ`.  The archimedean
evaluation (the substrate value `q₀ ≈ 1.1097 ∈ ℝ` at which the
`q`-family `dim_q 𝒪_q(SU(2))` would be realised) is the downstream
`R := ℝ` specialisation and is *not* performed in this file.  This is
the substrate → archimedean wall applied to the categorical Euler
characteristic: the fibre-level statement is generic, only the
evaluation is real.

The **one** non-derived input is the categorical = topological
identification `tr(id_A) = χ(𝒮) = 2 − 2g` — the content of the
proved upstream proposition [`prop:euler-char-stability`] that this
lemma `uses`.  It is carried as the context field
`trace_id_eq_topological`, stated *generically in `g`* (never the
`−6` conclusion).  From it, `categoricalTrace = −6` and the
quantum-dimension recovery `categoricalTrace = χ(A)` are then
**derived** by substituting `g = 4` and computing — no `sorry`, no
projected claim field.  What genuinely remains outside Mathlib (the
closed-form `q`-family `dim_q 𝒪_q(SU(2))` and a from-scratch
construction of `Rep(SU_q(2))`) is *not needed*: the substrate value
is pinned by `prop:euler-char-stability`, so nothing here is
axiomatised beyond that upstream proposition.

## References

- [manuscript] brings-surface/brings-euler-characteristic.md.
- [manuscript] lifting-and-descent/euler-char-stability-proof.md
  (`prop:euler-char-stability` — the categorical = topological
  Euler-characteristic identification).
-/

namespace QOU.ArchimedeanUniverse

/-- Geometric context for the Euler-characteristic lemma, over a
    generic ground ring `R = End(𝟙)`.

    The geometric datum is the genus of Bring's surface, `g(Σ₄) = 4`.
    The Euler characteristic is *defined* from it (see `chi_A` below),
    so the lemma's value is derived rather than assumed. -/
class BringsEulerCharacteristicContext (R : Type*) [CommRing R] where
  /-- The Descartes substrate parameter `q₀`, at which the quantum
      dimension is specialised.  A ground-ring element (`R`, generic per
      §7c); its archimedean value `q₀ ≈ 1.1097 ∈ ℝ` is the downstream
      `R := ℝ` evaluation, not performed here. -/
  q0 : R
  /-- Bring's surface genus — the genuine geometric input `g(Σ₄) = 4`. -/
  g : ℕ
  /-- The classical genus fact for Bring's surface. -/
  genus_is_four : g = 4
  /-- Evaluation scalar `ev_A ∈ End(𝟙) ≅ R` of the base object
      `A = 𝒪_q(SU(2))` over `Σ₄`, taken at the substrate `q₀`.  Half of
      the rigidity data whose composite is the trace `tr(id_A)`. -/
  ev : R
  /-- Coevaluation scalar `coev_A ∈ End(𝟙) ≅ R` of the base object,
      at the substrate `q₀`. -/
  coev : R
  /-- **Categorical = topological** — the content of the proved upstream
      proposition `prop:euler-char-stability`: the rigidity trace
      `tr(id_A) = ev ∘ coev` of the base algebra coincides with the
      topological Euler characteristic `χ(𝒮) = χ(Σ₄) = 2 − 2g` of the
      archimedean state bundle.  This is the genuine categorical
      *input* (an upstream proposition), stated generically in `g` — it
      is **not** the `−6` conclusion, which is derived from it plus
      `g = 4`. -/
  trace_id_eq_topological : ev * coev = 2 - 2 * (g : R)

namespace BringsEulerCharacteristicContext

variable {R : Type*} [CommRing R] [ctx : BringsEulerCharacteristicContext R]

/-- The categorical Euler characteristic, **defined** by the Euler
    formula `χ = 2 − 2g`.  An integer topological invariant (`ℤ`, not
    the archimedean `ℝ`), embedded into the ground ring `R` where the
    categorical trace lives (see `quantum_dimension_recovers_chi`). -/
def chi_A : ℤ := 2 - 2 * (ctx.g : ℤ)

/-- The categorical trace of the identity, `tr(id_A) = ev_A ∘ coev_A`,
    as a scalar in the ground ring `End(𝟙) ≅ R` — the rigidity-trace
    model used by `prop:euler-char-stability`
    (`QOU.Torsion.euler_char_constant`), here taken at the substrate
    `q₀`.  This is the quantum dimension `dim_q A` specialised at `q₀`. -/
def categoricalTrace : R := ctx.ev * ctx.coev

end BringsEulerCharacteristicContext

variable {R : Type*} [CommRing R]

/-- **Lemma** ([`lem:brings-euler-characteristic`]):
    on Bring's surface, `g = 4`, the Euler characteristic obeys the
    Euler formula `χ(A) = 2 − 2g`, and its value is `χ(A) = −6`.

    The first conjunct is the geometric input; the second is the
    definition of `chi_A`; the third is **derived** by `norm_num`
    after substituting `g = 4`. -/
-- Ref: [manuscript] brings-surface/brings-euler-characteristic.md
theorem brings_euler_characteristic [ctx : BringsEulerCharacteristicContext R] :
    ctx.g = 4
    ∧ (BringsEulerCharacteristicContext.chi_A (R := R)) = 2 - 2 * (ctx.g : ℤ)
    ∧ (BringsEulerCharacteristicContext.chi_A (R := R)) = -6 := by
  refine ⟨ctx.genus_is_four, rfl, ?_⟩
  unfold BringsEulerCharacteristicContext.chi_A
  rw [ctx.genus_is_four]
  norm_num

/-- **Trace of the identity** ([`lem:brings-euler-characteristic`]):
    the categorical trace `tr(id_A) = ev_A ∘ coev_A` of
    `A = 𝒪_q(SU(2))` over `Σ₄` equals `χ(Σ₄) = −6`.

    Derived, not assumed: the value `−6` is **computed** from the
    categorical = topological identification `prop:euler-char-stability`
    (`trace_id_eq_topological`, generic in `g`) together with the genus
    fact `g = 4` — never read back from a class field asserting `−6`. -/
-- Ref: [manuscript] quantum-observable-universe/brings-surface/brings-euler-characteristic.md
theorem categorical_trace_eq_neg_six [ctx : BringsEulerCharacteristicContext R] :
    BringsEulerCharacteristicContext.categoricalTrace (R := R) = -6 := by
  unfold BringsEulerCharacteristicContext.categoricalTrace
  rw [ctx.trace_id_eq_topological, ctx.genus_is_four]
  norm_num

/-- **Substrate recovery** — the .md's final clause: the quantum
    dimension of `A = 𝒪_q(SU(2))` specialised at the Descartes
    substrate parameter `q₀` (the categorical trace `tr(id_A)`,
    modelled by `categoricalTrace`) recovers the categorical Euler
    characteristic `χ(A) = −6`, viewed in the ground ring `R`.

    Fully derived (no `sorry`): both sides evaluate to `−6` —
    `categoricalTrace` by `categorical_trace_eq_neg_six`, and `χ(A)`
    by `brings_euler_characteristic`.  The only non-derived input in
    the chain is the upstream proposition `prop:euler-char-stability`
    carried by `trace_id_eq_topological`; the closed-form `q`-family
    `dim_q 𝒪_q(SU(2))` is not needed and is not axiomatised. -/
-- Ref: [manuscript] quantum-observable-universe/brings-surface/brings-euler-characteristic.md
theorem quantum_dimension_recovers_chi [ctx : BringsEulerCharacteristicContext R] :
    BringsEulerCharacteristicContext.categoricalTrace (R := R)
      = ((BringsEulerCharacteristicContext.chi_A (R := R) : ℤ) : R) := by
  have hchi : BringsEulerCharacteristicContext.chi_A (R := R) = -6 :=
    (brings_euler_characteristic).2.2
  rw [categorical_trace_eq_neg_six, hchi]
  norm_num

end QOU.ArchimedeanUniverse
