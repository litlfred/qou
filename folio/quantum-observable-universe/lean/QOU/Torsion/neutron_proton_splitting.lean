import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# QOU.Torsion.neutron_proton_splitting — neutron-proton mass splitting

**Proposition** ([`prop:neutron-proton-splitting`](../../../quantum-observable-universe/particle-interactions/neutron-proton-splitting.md)).

*The model neutron–proton splitting is*

```
  Δm := α · |Φ(udd) − Φ(uud)| = 3.7449 · 0.3476 = 1.30172724   (MeV units)
```

*where `Φ(uud)` and `Φ(udd)` are the quantum-dilogarithm volumes of the
proton and neutron quark orderings respectively, and `α = m_e · 8G` is the
same binding scale as the atomic mass formula.*

This file states only the model value.  Its comparison with the measured
CODATA splitting is an empirical claim and is recorded in the content block's
comparison paragraph, not in Lean (owner rule 2026-11-15).  The file is
**sorry-free**: the corpus values of `α`, `Φ(uud)`, `Φ(udd)` are pinned as
provenance-cited hypothesis fields (`NeutronProtonSplittingNumerics`) and the
value is derived from them by arithmetic.  Porting the exact closed forms of
the traced-volumes themselves stays open.

The two `Φ` volumes (`Φ(uud) ≈ -0.8785`, `Φ(udd) ≈ -1.2261`) **are derived**:
they are the canonical Hecke **traced-volume** of the quark orderings
(uud = `[1,1,0]`, udd = `[1,0,0]`), `Φ(K) = Σᵢ log|V̂ᵢ(K)|` with
`V̂ᵢ = z·M₁₀ + M₁₁` the transfer-matrix product over the quark crossings
(`computations/level1-qvalues.py`, `HeckeRational.traced_volume`).  This has an
exact closed form — `log` of a rational function of `q` — e.g.
`Φ(udd) = log|(q²+1)²(10000q² − 4993q − 10000) / (40000 q³)|` (with the
NF-basis constant `z = 4993/10000`).  Provenance + symbolic derivation:
`docs/audits/2026-07-11-quark-volume-provenance.md`.  (This transfer-matrix
`V̂ᵢ` is a *different* object from the `Φ_q` q-Pochhammer of
`QOU.MathlibExt.QuantumDilogarithm`.)  They remain opaque
`NeutronProtonSplittingContext` fields (§3b-cond) here only because the
`traced_volume` construction is not yet ported to Lean
(AGENTS.md anti-laundering rule).

-- Ref: [manuscript] quantum-observable-universe/particle-interactions/neutron-proton-splitting.md
-/

namespace QOU.Torsion

/-- Inputs for the neutron-proton splitting: the binding scale `α = m_e·8G`,
    the proton/neutron quantum-dilogarithm volumes `Φ(uud)`, `Φ(udd)`, and
    the physical masses `m_p`, `m_n`. -/
class NeutronProtonSplittingContext where
  /-- Binding scale `α = m_e · 8G`. -/
  α : ℝ
  /-- Quantum-dilogarithm volume of the proton (uud) braid. -/
  Φ_uud : ℝ
  /-- Quantum-dilogarithm volume of the neutron (udd) braid. -/
  Φ_udd : ℝ
  /-- Proton rest mass (MeV). -/
  m_p : ℝ
  /-- Neutron rest mass (MeV). -/
  m_n : ℝ

/-- The framework-predicted neutron-proton mass difference in MeV
    (`α · |Φ(udd) − Φ(uud)|` per the manuscript). -/
def predictedNeutronProtonSplitting [ctx : NeutronProtonSplittingContext] : ℝ :=
  ctx.α * |ctx.Φ_udd - ctx.Φ_uud|

/-- **Corpus-pinned numerics** for the splitting (the `qou-octr` fix: give
    the class the hypotheses the derivation needs).  Each pin is a genuine
    *input* with provenance, not the conclusion:

    - `α = 3.7449` — the binding scale `m_e·8G` (`m_e = 0.511 MeV`,
      `G` Catalan's constant, `8G ≈ 7.3286`); same scale as the atomic
      mass formula.
    - `Φ(uud) = −0.8785`, `Φ(udd) = −1.2261` — the canonical Hecke
      traced-volumes of the quark orderings; **derived** in the corpus
      with exact closed forms (`log` of a rational function of `q`), see
      `docs/audits/2026-07-11-quark-volume-provenance.md` and
      `computations/level1-qvalues.py`.  Decimal pins at manuscript
      precision (4 d.p.); porting the closed forms themselves to Lean is
      the remaining formalization item.

    From these three pins the value of the prediction below is *derived* by
    arithmetic — the class does not carry the conclusion. -/
class NeutronProtonSplittingNumerics extends NeutronProtonSplittingContext where
  /-- Binding-scale pin `α = m_e·8G ≈ 3.7449` (provenance above). -/
  α_val : α = 3.7449
  /-- Proton (uud) traced-volume pin (provenance above). -/
  Φ_uud_val : Φ_uud = -0.8785
  /-- Neutron (udd) traced-volume pin (provenance above). -/
  Φ_udd_val : Φ_udd = -1.2261

/-- **Neutron-proton mass splitting** ([`prop:neutron-proton-splitting`]),
    conditional on the corpus-pinned numerics — **sorry-free**.

    The framework *prediction* is `α · |Φ(udd) − Φ(uud)|`
    (`predictedNeutronProtonSplitting`); with the pinned values it equals
    exactly `3.7449 · 0.3476 = 1.30172724` (MeV units).

    This statement is model mathematics only.  The comparison with the
    measured (CODATA) splitting is an empirical claim and lives in the
    content block's comparison paragraph, not here (owner rule 2026-11-15:
    no empirical values in formal statements).  An earlier version carried
    a CODATA-tolerance conjunct, and before that an exact-equality conjunct
    `m_n − m_p = α·|Φ(udd) − Φ(uud)|` that was refutable as written
    (`neutron_proton_splitting_unconstrained_false` below). -/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/neutron-proton-splitting.md
theorem neutron_proton_splitting [cm : NeutronProtonSplittingNumerics] :
    (predictedNeutronProtonSplitting = cm.α * |cm.Φ_udd - cm.Φ_uud|) ∧
    (predictedNeutronProtonSplitting = (3.7449 : ℝ) * 0.3476) := by
  constructor
  · rfl
  · unfold predictedNeutronProtonSplitting
    rw [cm.α_val, cm.Φ_uud_val, cm.Φ_udd_val]
    have h1 : (-1.2261 : ℝ) - (-0.8785) = -0.3476 := by norm_num
    rw [h1, abs_neg, abs_of_pos (by norm_num : (0.3476 : ℝ) > 0)]

/-- **The exact-equality form is refutable as written** — the base class
    never relates the fields the conclusion names, so `∀ instances` admits
    ones that simply disagree (and per §7ab the manuscript never claimed
    exact equality of the measured splitting to the derived value in the
    first place).  Kept as the documented evidence for why the resolving
    theorem above states the prediction form instead
    (bean qou-octr, criterion §10 `proof-unclosable-context-sorry`). -/
theorem neutron_proton_splitting_unconstrained_false :
    ¬ ∀ ctx : NeutronProtonSplittingContext,
        ctx.m_n - ctx.m_p = ctx.α * |ctx.Φ_udd - ctx.Φ_uud| := by
  intro h
  have := h { α := 0, Φ_uud := 0, Φ_udd := 0, m_p := 0, m_n := 1 }
  norm_num at this

end QOU.Torsion
