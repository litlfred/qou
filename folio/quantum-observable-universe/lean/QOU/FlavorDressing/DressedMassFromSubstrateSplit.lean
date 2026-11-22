import QOU.Basic
import QOU.FlavorDressing.FlavorDressingFunctor
import QOU.FlavorDressing.FlavorSplitSubstrateMass

/-!
# QOU.FlavorDressing.dressed_mass_from_substrate_split

The substrate-pure derivation of the down–up dressed-quark
mass splitting:

```
μ_d − μ_u = M_N · (q-1)²·(1 − q⁻⁴)/3 · (q^{1/2} + q⁻^{1/2})/(q + q⁻¹)
            + O((Δm/M_N)²)
```

This is the categorical lift of `conj:flavor-split-substrate-mass` to
the level of the flavor-dressing functor.

LaTeX: `\label{prop:flavor-dressed-mass-from-substrate-split}`
-/

namespace QOU.FlavorDressing

open Flavor

/-- The leading-order substrate factor

    `s(q) = (q − 1)² · (1 − q⁻⁴) / 3 · (√q + 1/√q) / (q + 1/q)`

    that multiplies `M_N` to give the dressed-quark splitting at
    substrate parameter `q ∈ ℝ`, `0 < q`.  Defined as a function on
    `ℝ` (we are at the archimedean / numerical layer here per
    AGENTS.md §7c). -/
noncomputable def substrate_split_factor (q : ℝ) : ℝ :=
  ((q - 1)^2 * (1 - q^(-4 : ℤ)) / 3) *
    ((Real.sqrt q + Real.sqrt q⁻¹) / (q + q⁻¹))

/-- **Classical limit at `q = 1` (proved):** the substrate splitting factor
    `substrate_split_factor q` vanishes identically at `q = 1` because of the
    `(q - 1)^2` prefactor. -/
theorem substrate_split_factor_at_one :
    substrate_split_factor 1 = 0 := by
  unfold substrate_split_factor
  norm_num

/-- The nucleon-level consequence of the pair Skein mass formula
    (`lem:pair-skein-mass-formula`) on the Borromean baryon braids of the
    proton and neutron:

      `(m_n − m_p) · (√q + √q⁻¹) = (q + q⁻¹) · (μ_d − μ_u)`.

    It is a hypothesis of the theorem below, not a lemma proved here. The
    Lean `QOU.HadronicMass.pair_skein_mass_formula` is a per-pair `Prop`
    and does not yet yield this nucleon form. The formula holds only in the
    convention-C frame. -/
def PairSkeinNucleonSplit (F : FlavorDressingFunctor) (m_p m_n q : ℝ) : Prop :=
  (m_n - m_p) * (Real.sqrt q + Real.sqrt q⁻¹)
    = (q + q⁻¹) * (F.μ Flavor.down - F.μ Flavor.up)

/-- **Dressed-quark mass splitting, conditional on
    `conj:flavor-split-substrate-mass`** (§3b-cond).

    From the conjecture `[FlavorSplitSubstrateMass m_p m_n q]` and the
    nucleon form of the pair Skein mass formula, the down–up dressed-mass
    splitting is `M_N · substrate_split_factor q` with
    `M_N = (m_p + m_n)/2`. The proof divides the Skein relation by
    `q + q⁻¹ > 0` and substitutes the conjecture's nucleon split.

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
        = (m_p + m_n) / 2 * substrate_split_factor q ∧
    F.μ Flavor.down
        = F.μ Flavor.up + (m_p + m_n) / 2 * substrate_split_factor q := by
  have hq0 : 0 < q := lt_trans one_pos h.q_gt_one
  have hB : 0 < q + q⁻¹ := add_pos hq0 (inv_pos.mpr hq0)
  have hdiff : F.μ Flavor.down - F.μ Flavor.up
      = (m_n - m_p) * (Real.sqrt q + Real.sqrt q⁻¹) / (q + q⁻¹) := by
    rw [eq_div_iff hB.ne', h_skein]; ring
  have hsplit : F.μ Flavor.down - F.μ Flavor.up
      = (m_p + m_n) / 2 * substrate_split_factor q := by
    rw [hdiff, h.nucleon_split]
    unfold substrate_split_factor flavorSplitClosedForm
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
