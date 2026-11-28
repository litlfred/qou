import QOU.Core.Basic
import QOU.EightfoldWay.FlavorDressingFunctor
import QOU.EightfoldWay.FlavorSplitSubstrateMass
import QOU.MassTheory.PairSkeinMassConventionD

/-!
# QOU.FlavorDressing.dressed_mass_from_substrate_split

The substrate-pure derivation of the down–up dressed-quark
mass splitting:

```
μ_d − μ_u = M_N · (q-1)²·(1 − q⁻⁴)/3 · q(q² + 1)/(q⁴ + 1)
```

The last factor comes from the convention-D pair Skein mass formula,
derived in `QOU.MassTheory.PairSkeinD` (owner ruling 2026-11-27).

This is the categorical lift of `conj:flavor-split-aether-mass` to
the level of the flavor-dressing functor.

LaTeX: `\label{prop:flavor-dressed-mass-from-aether-split}`
-/

namespace QOU.FlavorDressing

open Flavor

/-- The leading-order substrate factor

    `s(q) = (q − 1)² · (1 − q⁻⁴) / 3 · q(q² + 1) / (q⁴ + 1)`

    that multiplies `M_N` to give the dressed-quark splitting. The factor
    `q(q² + 1)/(q⁴ + 1) = 1/κ` is the inverse of the convention-D nucleon
    splitting constant `κ = trace₂ z_D (σ + σ⁻¹)`
    (`QOU.MassTheory.PairSkeinD.kappaD_closed`). No square root appears.
    Convention D (owner ruling 2026-11-27); the convention-C factor
    `(√q + 1/√q)/(q + 1/q)` is retired. -/
noncomputable def aether_split_factor (q : ℝ) : ℝ :=
  ((q - 1)^2 * (1 - q^(-4 : ℤ)) / 3) *
    (q * (q^2 + 1) / (q^4 + 1))

@[deprecated (since := "2026-11-27")] alias substrate_split_factor := aether_split_factor

/-- **Classical limit at `q = 1` (proved):** the substrate splitting factor
    `aether_split_factor q` vanishes identically at `q = 1` because of the
    `(q - 1)^2` prefactor. -/
theorem aether_split_factor_at_one :
    aether_split_factor 1 = 0 := by
  unfold aether_split_factor
  norm_num

@[deprecated (since := "2026-11-27")] alias substrate_split_factor_at_one := aether_split_factor_at_one

/-- The nucleon-level form of the convention-D pair Skein mass formula:

      `(m_n − m_p) · q(q² + 1) = (q⁴ + 1) · (μ_d − μ_u)`.

    It follows from the derived pair formula when the proton and neutron
    masses are the sums of their pair masses
    (`pairSkeinNucleonSplit_of_nucleonMassD`). -/
def PairSkeinNucleonSplit (F : FlavorDressingFunctor) (m_p m_n q : ℝ) : Prop :=
  (m_n - m_p) * (q * (q^2 + 1))
    = (q^4 + 1) * (F.μ Flavor.down - F.μ Flavor.up)

/-- The nucleon form follows from the derived convention-D pair Skein mass
    formula (`QOU.MassTheory.PairSkeinD.neutron_sub_proton_cleared`) when the
    proton is the strand order `(u, u, d)` and the neutron `(u, d, d)`. -/
theorem pairSkeinNucleonSplit_of_nucleonMassD
    (F : FlavorDressingFunctor) (m_p m_n q : ℝ) (hq : 0 < q)
    (hp : m_p = QOU.MassTheory.PairSkeinD.nucleonMassD q
      (F.μ Flavor.up) (F.μ Flavor.up) (F.μ Flavor.down))
    (hn : m_n = QOU.MassTheory.PairSkeinD.nucleonMassD q
      (F.μ Flavor.up) (F.μ Flavor.down) (F.μ Flavor.down)) :
    PairSkeinNucleonSplit F m_p m_n q := by
  unfold PairSkeinNucleonSplit
  rw [hp, hn]
  exact QOU.MassTheory.PairSkeinD.neutron_sub_proton_cleared q _ _ hq.ne'
    (by positivity)

/-- **Dressed-quark mass splitting, conditional on
    `conj:flavor-split-aether-mass`** (§3b-cond).

    From the conjecture `[FlavorSplitSubstrateMass m_p m_n q]` and the
    nucleon form of the pair Skein mass formula, the down–up dressed-mass
    splitting is `M_N · aether_split_factor q` with
    `M_N = (m_p + m_n)/2`. The proof divides the Skein relation by
    `q⁴ + 1 > 0` and substitutes the conjecture's nucleon split.

    **History.** This file once stated the conclusion as an `axiom`
    quantified over unrelated `(F, M_N, q)`, which made the library
    inconsistent (until 2026-08-08: the constant dressing `μ ≡ 1` forced
    `√2 + (√2)⁻¹ = 0`). Its replacement was a hypothesis class whose
    `split` field *was* the conclusion, so the theorem was a projection of
    its own hypothesis (AGENTS.md §3b-cond item 5). The class now carries
    only the conjecture's input, the nucleon split, and the theorem derives
    the quark splitting from it. -/
-- Ref: [leitner2026] mass-theory/flavor-dressed-mass-from-substrate-split
theorem dressed_mass_from_substrate_split
    (F : FlavorDressingFunctor) (m_p m_n q : ℝ)
    [h : FlavorSplitSubstrateMass m_p m_n q]
    (h_skein : PairSkeinNucleonSplit F m_p m_n q) :
    F.μ Flavor.down - F.μ Flavor.up
        = (m_p + m_n) / 2 * aether_split_factor q ∧
    F.μ Flavor.down
        = F.μ Flavor.up + (m_p + m_n) / 2 * aether_split_factor q := by
  have hq0 : 0 < q := lt_trans one_pos h.q_gt_one
  have hB : 0 < q^4 + 1 := by positivity
  have hdiff : F.μ Flavor.down - F.μ Flavor.up
      = (m_n - m_p) * (q * (q^2 + 1)) / (q^4 + 1) := by
    rw [eq_div_iff hB.ne', h_skein]; ring
  have hsplit : F.μ Flavor.down - F.μ Flavor.up
      = (m_p + m_n) / 2 * aether_split_factor q := by
    rw [hdiff, h.nucleon_split]
    unfold aether_split_factor flavorSplitClosedForm
    ring
  exact ⟨hsplit, by linarith⟩


/-! ### Removed 2026-08-30 — self-assuming projections

- `dressed_mass_split_hypotheses` — body was `⟨h.M_N_pos, h.q_gt_one⟩`: the conclusion was the
  projected field verbatim, so the declaration restated its own hypothesis.

**Why removal.** The content stays in the class field each declaration
projected, asserting the same proposition under the same hypotheses; only the
restatement goes. That is the vacuity ledger's recorded disposition for this
category — *"drop the pseudo-theorem and project the field at use sites"* — and
there were no use sites: each had **zero references anywhere in the corpus**.
Bean `qou-z9ws`.

### Removed 2026-11-21 — the self-assuming class

- `DressedMassSubstrateSplit F M_N q` — its `split` field was the conclusion of
  `dressed_mass_from_substrate_split`, which projected it (§3b-cond item 5).
  Replaced by `FlavorSplitSubstrateMass`, which carries only the conjecture's
  nucleon split; the quark splitting is now derived (issue #8948).
- `dressed_mass_down_eq_up_add_split` — `linarith` on that field; its content
  is the second conjunct of `dressed_mass_from_substrate_split`. No use sites.
-/

end QOU.FlavorDressing
