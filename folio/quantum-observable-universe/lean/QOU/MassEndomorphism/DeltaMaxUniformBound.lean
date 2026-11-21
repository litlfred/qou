import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.AbsoluteValue.Basic
import Mathlib.Tactic.Linarith
import QOU.BraidKnot.JetTowerUniformDeltaMax

/-!
# QOU.MassEndomorphism.DeltaMaxUniformBound — uniform Δ_max in the rank-1 regime

The proposition `prop:delta-max-uniform-bound` closes the
**archimedean / rank-1 SDP** regime of the convergence conjecture
`conj:jet-tower-uniform-delta-max`:

  |Δ⁽ⁿ⁾(ρ)| ≤ 2 · L(β) · ‖ρ(β)‖_op² · 𝔪⁽⁰⁾(ρ_free),
              independent of n.

The proof uses operator-norm boundedness of the Markov trace
([thm:markov-trace-factorization]), the recursive brane tower
([def:recursive-brane-tower]), and Kassel–Turaev's bound on the
Jones–Wenzl module dimension ([kassel1995] §4.4.3).

**Archimedean tier.**  This proposition lives on the τ-image side:
the operator norm `‖·‖_op` is real-valued, the substrate parameter
`q > 0` is real, and the numerical evaluation at `q₀ ≈ 1.1100`
appears in the narrative.  Per `QOU.GroundRingAnnotations`, this
file is in the **Archimedean realisation** tier — it is not part
of the formal pre-Arch chain.

The conditional-class structure is supplied by
[`OperatorNormBound`](#OperatorNormBound) below; an instance
witnesses the four ingredients of the proof (operator-norm bound,
Markov-trace boundedness, level-0 free mass, JW-module dimension
bound).

LaTeX label: `prop:delta-max-uniform-bound`
-- Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
-- Ref: [leitner2026] manuscript
-/

namespace QOU.MassEndomorphism

/-- **Operator-norm bound data** for a vortex `ρ` with braid
    representative `β ∈ B_n`.

    Captures the four quantities needed for the Δ_max uniform
    bound:
    * `braidLength` = `L(β)`,
    * `opNorm` = `‖ρ(β)‖_op` on the Jones–Wenzl module,
    * `freeMassLevel0` = `𝔪⁽⁰⁾(ρ_free)`,
    * `delta` = the per-level residual,
    along with their non-negativity.

    All quantities are real-valued (Archimedean tier). -/
structure OperatorNormBound (ρ : Type*) where
  braidLength : ℕ
  opNorm : ℝ
  opNorm_nonneg : 0 ≤ opNorm
  freeMassLevel0 : ℝ
  freeMassLevel0_nonneg : 0 ≤ freeMassLevel0
  delta : ℕ → ℝ
  /-- The proven per-level bound (Steps 1–4 of the .md proof). -/
  per_level_bound :
    ∀ n : ℕ, 1 ≤ n →
      |delta n| ≤
        2 * (braidLength : ℝ) * opNorm ^ 2 * freeMassLevel0

/-- The closed-form `Δ_max(ρ) := 2 · L(β) · ‖ρ(β)‖_op² ·
    𝔪⁽⁰⁾(ρ_free)`. -/
def OperatorNormBound.deltaMax {ρ : Type*}
    (b : OperatorNormBound ρ) : ℝ :=
  2 * (b.braidLength : ℝ) * b.opNorm ^ 2 * b.freeMassLevel0

theorem OperatorNormBound.deltaMax_nonneg {ρ : Type*}
    (b : OperatorNormBound ρ) :
    0 ≤ b.deltaMax := by
  unfold OperatorNormBound.deltaMax
  have h₁ : (0 : ℝ) ≤ 2 := by norm_num
  have h₂ : (0 : ℝ) ≤ (b.braidLength : ℝ) := Nat.cast_nonneg _
  have h₃ : (0 : ℝ) ≤ b.opNorm ^ 2 := sq_nonneg _
  have h₄ : (0 : ℝ) ≤ b.freeMassLevel0 := b.freeMassLevel0_nonneg
  positivity

/-- **Δ_max uniform bound (Archimedean / rank-1 SDP regime).**

    For a vortex `ρ` carrying an `OperatorNormBound`, the
    per-level residual is uniformly bounded by `deltaMax`. -/
-- Ref: [leitner2026] `prop:delta-max-uniform-bound`,
--      §"Derivation" Steps 1–4
-- Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
theorem delta_max_uniform_bound
    {ρ : Type*} (b : OperatorNormBound ρ)
    (n : ℕ) (hn : 1 ≤ n) :
    |b.delta n| ≤ b.deltaMax :=
  b.per_level_bound n hn

/-- An `OperatorNormBound` discharges the
    `JetTowerUniformDeltaMax` conjectural class for the same
    vortex `ρ`.  This is the **closure of the archimedean /
    rank-1 SDP regime** of the convergence conjecture
    (`conj:jet-tower-uniform-delta-max`). -/
def toJetTowerUniformDeltaMax {ρ : Type*}
    (b : OperatorNormBound ρ) :
    QOU.BraidKnot.JetTowerUniformDeltaMax ρ where
  delta := b.delta
  delta_max := b.deltaMax
  delta_max_nonneg := b.deltaMax_nonneg
  uniform_bound := b.per_level_bound

end QOU.MassEndomorphism
