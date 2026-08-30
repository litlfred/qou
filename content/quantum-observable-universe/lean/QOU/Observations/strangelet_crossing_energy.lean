import Mathlib.Data.Real.Basic
import Mathlib.Tactic
import QOU.Shared.ArchimedeanEval

/-!
# QOU.Observations.strangelet_crossing_energy

**Canonical declaration** for content block
[`prop:strangelet-crossing-energy`](../../../quantum-observable-universe/observations/strangelet-crossing-energy.md): *QOU.Observations.strangelet_crossing_energy*.

This module states the manuscript claim conditional on the §3b hypothesis class.

## Base ring (§7c) — `ℝ` here is correct

`StrangeletCrossingEnergyContext` inherits a generic coefficient ring `R` from
`QOU.Shared.MarkovTraceContext`, but this block's fields stay at
`ℝ`: the binding-energy formulae are hypothesised under `0 < q_real`, and the
conclusion `E_bind_udd < E_bind_uds` is derived by `inv_pos` + `linarith`.
Ordering hypotheses and `linarith` are archimedean, so the block sits after the
substrate→archimedean wall.  Reviewed under bean `qou-mtcx`; do not "port" it
to `R` to reduce an `ℝ` count.

`q_real` is genuinely used and is now **tied** to the inherited `q : R` (bean
`qou-mt7r`): the class extends `QOU.Shared.ArchimedeanEval`, which carries an
assumed evaluation `eval : R →+* ℝ` and derives `q_real := eval q`.  It used to
be an independent field, so `0 < q_real` constrained a free real rather than the
image of this universe's substrate parameter.  The evaluation is assumed, not
constructed: it is **not** the archimedean τ-functor, and
`ArchimedeanEval.ofRingHom` machine-checks how little it takes to inhabit.
-/

namespace QOU.Observations

/-- Abstract context for the `strangelet_crossing_energy` claim — manuscript-themed
    typed fields below. -/
class StrangeletCrossingEnergyContext extends QOU.Shared.ArchimedeanEval where
  /-- Coulomb charge `Q(𝓑₃(u, d, s)) = +2/3 − 1/3 − 1/3 = 0`. -/
  Q_uds : ℝ
  /-- Baryon count `N` of the strangelet composite `𝓢_N`. -/
  N_baryon : ℕ
  /-- Positive crossing count per baryon. -/
  n_plus : ℕ
  /-- Negative crossing count per baryon. -/
  n_minus : ℕ
  /-- Crossing energy `E_cross(𝓢_N)`. -/
  E_cross : ℝ
  /-- Binding energy per baryon for `uds` (strange matter). -/
  E_bind_uds : ℝ
  /-- Binding energy per baryon for `udd` (neutron matter). -/
  E_bind_udd : ℝ

/-- The physical hypotheses carried by the Strangelet Crossing Energy Conjecture. -/
class StrangeletCrossingEnergyConjecture (ctx : StrangeletCrossingEnergyContext) : Prop where
  /-- Manuscript sub-claim (i) — Electromagnetic neutrality:
      `Q(𝓑₃(u, d, s)) = 0`. -/
  claim_i_electromagnetic_neutrality : ctx.Q_uds = 0
  /-- Manuscript sub-claim (ii) — Purely strong crossing energy:
      `E_cross = N · ½(n₊ + n₋)·(q + q⁻¹)`. -/
  claim_ii_purely_strong_crossing :
    ctx.E_cross = (ctx.N_baryon : ℝ) * ((ctx.n_plus + ctx.n_minus : ℕ) : ℝ) / 2 *
      (ctx.q_real + ctx.q_real⁻¹)
  /-- Formula for binding energy of uds. -/
  uds_binding : 0 < ctx.q_real → ctx.E_bind_uds = 8 * ctx.q_real⁻¹
  /-- Formula for binding energy of udd. -/
  udd_binding : 0 < ctx.q_real → ctx.E_bind_udd = 6 * ctx.q_real⁻¹

/-- **Content statement** (from manuscript):

**Proposition.**
Let $\mathcal{S}_N$ be a composite of $N$ baryon-number units of
strange quark matter, each containing one up, one down, and one
strange quark in a Borromean triple
$\mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{s})$ linked
by the Hopf link $\mathcal{L}_H$.  Then:

The Lean encoding below derives the equalities and inequalities from the hypothesis class. -/
-- Ref: [manuscript] quantum-observable-universe/observations/strangelet-crossing-energy.ts
theorem strangelet_crossing_energy (ctx : StrangeletCrossingEnergyContext)
    [hc : StrangeletCrossingEnergyConjecture ctx] :
    ctx.Q_uds = 0 ∧
    ctx.E_cross =
      (ctx.N_baryon : ℝ) * ((ctx.n_plus + ctx.n_minus : ℕ) : ℝ) / 2 *
        (ctx.q_real + ctx.q_real⁻¹) ∧
    (0 < ctx.q_real →
      ctx.E_bind_uds = 8 * ctx.q_real⁻¹ ∧
      ctx.E_bind_udd = 6 * ctx.q_real⁻¹ ∧
      ctx.E_bind_udd < ctx.E_bind_uds) := by
  refine ⟨hc.claim_i_electromagnetic_neutrality, hc.claim_ii_purely_strong_crossing, ?_⟩
  intro hq
  have huds := hc.uds_binding hq
  have hudd := hc.udd_binding hq
  refine ⟨huds, hudd, ?_⟩
  rw [hudd, huds]
  have h_inv_pos : 0 < ctx.q_real⁻¹ := inv_pos.mpr hq
  linarith

end QOU.Observations
