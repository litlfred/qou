/-
Copyright (c) 2026 litlfred. All rights reserved.

# The `b₃` exhaustion is CONDITIONAL on a uniform bond weight — and the corpus now derives that the weight is NOT uniform

`QOU.Mass.BrunnianTripleExhaustion` closes the count-channel route to the measured
three-body cumulant: `bRatioOfTriple m₁ m₂ m₃ = m₁ + m₂ + m₃ − 3` is an **integer**
for integer per-pair crossing counts, while `rMeasured = 950815/1483044` sits
strictly inside `(1/2, 3/4)`.  Hence `no_carrier_reproduces_b3`, a miss of at
least 55.98 %, and `gap_increases_beyond_four` covering every crossing number.

**That exhaustion is honest about its own premise**, and says so: the integrality
is *"not a fact about crossings — it is the uniformity of `def:crossing-energy`,
and it is the one ingredient of the excluded conjunction that is a definitional
choice rather than a proved constraint."*  `pairDependent_weight_not_a_count` is
the escape it names.

**The corpus has since taken that escape, on a different front, and nobody
connected the two.**  Bean `qou-qqm4` (#7000, #6992, and the order-4
discriminator) establishes that the atom word's inter-nucleon interface factor is
`z + d_kind` and that the **kind matters**: `d_averaged` and `d_averaged_weighted`
first separate at `ε⁴`, and the measured `pn` bond matches
`z + d_averaged_weighted` — `(1/2, 0, 3/4, −3/4, 31/24)` — decisively.  So the
bond weight **depends on which kind of pair the interface joins**, and that
dependence is *derived from the two Markov parameters*, not fitted.

A light nucleus has mixed pair kinds: the deuteron is `pn`; `³He = ppn` has pairs
`pp, pn, pn`; `⁴He = ppnn` has `pp, nn` and four `pn`.  So the uniformity premise
fails for exactly the nuclei whose `b₃` is measured.

**Consequence, stated precisely.**  `no_carrier_reproduces_b3` is not refuted and
nothing in `BrunnianTripleExhaustion` is wrong.  What changes is its **scope**:
it is a scope-(a) negative about *uniform-weight* carriers, not a scope-(b)
exclusion of the count channel, because the invariant it rests on (integrality)
is derived-false on the physical carrier.  This file supplies the generalisation
and the resulting target.

## 🛑 THE DIRECTION OF USE — this is a DERIVATION TARGET, not a fit

`kindRatio_forced_at_minimal_carrier` says what `ρ_pp` **would have to be** to
reproduce the measurement.  Reading that equation left-to-right — computing
`ρ_pp` from `rMeasured` and declaring the channel closed — is a **one-parameter
fit**, and under AGENTS.md's anti-fit rule it ranks *below* the honest 55.98 %
miss it would replace.

The only admissible use is right-to-left: compute `ρ_pp` **independently**, from
`qou-qqm4`'s derived `z + d_kind` at the `pp` interface, and compare it to the
number below.  Agreement would be a parameter-free prediction; disagreement is a
real negative about the bond model.  Either is a result; inverting is not.

§7c: everything here is `ℚ` arithmetic on ratios and counts — no archimedean
construct, no `ℝ`.  Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md
-/
import QOU.Mass.BrunnianTripleExhaustion

namespace QOU.Mass.KindDependentBondBreaksIntegrality

open QOU.Mass.BrunnianTripleExhaustion QOU.Mass.CarrierCrossingQuantisation

/-- `b₃/b₂` when the bond weight may depend on the **kind** of pair the interface
joins.  `ρᵢ` is pair `i`'s weight in units of the reference pair's — and the
reference is the `pn` pair, because `b₂` is measured on the deuteron, which is
`pn`.  Setting every `ρᵢ = 1` recovers the uniform case. -/
def bRatioKind (ρ₁ ρ₂ ρ₃ m₁ m₂ m₃ : ℚ) : ℚ :=
  m₁ * ρ₁ + m₂ * ρ₂ + m₃ * ρ₃ - 3

/-- **It is a genuine generalisation**: at uniform weights it is exactly the
exhaustion's ratio, so nothing here contradicts that file — it extends it. -/
theorem bRatioKind_uniform (m₁ m₂ m₃ : ℚ) :
    bRatioKind 1 1 1 m₁ m₂ m₃ = bRatioOfTriple m₁ m₂ m₃ := by
  unfold bRatioKind bRatioOfTriple; ring

/-- **And it is not the same function** — the generalisation has content.  A
single kind whose weight differs moves the ratio by exactly that difference, so
`bRatioKind` is not constant in `ρ`.  Without this the extension could be
vacuous. -/
theorem bRatioKind_shifts (ρ m₁ m₂ m₃ : ℚ) :
    bRatioKind ρ 1 1 m₁ m₂ m₃ - bRatioOfTriple m₁ m₂ m₃ = m₁ * (ρ - 1) := by
  unfold bRatioKind bRatioOfTriple; ring

/-- **The forced kind-ratio for the minimal `³He` carrier.**

`³He` is `ppn`: one `pp` pair and two `pn` pairs.  With the minimal Brunnian
counts `mᵢ = 1` and the `pn` weight as the reference, the measured ratio is
reproduced **iff**

    ρ_pp  =  1 + rMeasured  =  2433859 / 1483044  ≈  1.64112 .

Read RIGHT-TO-LEFT only: this is the number `qou-qqm4`'s derived `z + d_kind` at
the `pp` interface must independently produce.  Computing `ρ_pp` from the left is
a one-parameter fit — see the banner above. -/
theorem kindRatio_forced_at_minimal_carrier (ρ : ℚ) :
    bRatioKind ρ 1 1 1 1 1 = rMeasured ↔ ρ = 2433859 / 1483044 := by
  unfold bRatioKind rMeasured
  constructor <;> intro h <;> linarith

/-- **Why the exhaustion cannot see this.**  Its ratio depends only on the *sum*
of the counts (`bRatio_depends_only_on_sum`); the kind-dependent ratio does not,
because two carriers with the same total can distribute their crossings over
pairs of different kinds.  So the collapse that makes the exhaustion exhaustive
is exactly what a kind-dependent weight breaks. -/
theorem kind_ratio_not_determined_by_sum :
    ∃ ρ m₁ m₂ m₃ m₁' m₂' m₃' : ℚ,
      m₁ + m₂ + m₃ = m₁' + m₂' + m₃' ∧
      bRatioKind ρ 1 1 m₁ m₂ m₃ ≠ bRatioKind ρ 1 1 m₁' m₂' m₃' := by
  refine ⟨2, 1, 1, 1, 2, 1, 0, by norm_num, ?_⟩
  unfold bRatioKind; norm_num

end QOU.Mass.KindDependentBondBreaksIntegrality
