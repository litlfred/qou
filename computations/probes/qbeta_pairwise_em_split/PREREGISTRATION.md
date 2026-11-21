# Pre-registration — does a pairwise charge energy escape the conserved-charge no-go for β?

Bean `qou-99qc`. Branch `claude/beta-em-self-energy-split-2026-11-21`. Written 2026-11-21, before any
number at q₀ was computed on this branch.

## Question

PR #8676 (`QOU.QuarkState.HyperchargeGradingNoGo`, branch `claude/beta-hypercharge-grading-2026-11-20`)
proves: for strands labelled (type ∈ {quark, lepton}) × (flavour ∈ {u, d}), an **additive per-strand**
charge `χ` has equal totals on `n⊗ν = (q u)(q d)(q d)(ℓ u)` and `p⊗e⁻ = (q u)(q u)(q d)(ℓ d)` iff
`χ(q,d) + χ(ℓ,u) = χ(q,u) + χ(ℓ,d)` (`total_eq_iff`); every **separable** charge `α(type)+β(flavour)`
satisfies this, so any function of a separable total gives zero split (`split_zero_of_total`).

Owner (2026-11-21): the EM self-energy enters through the two-term QED term; the two-term trace is
required in all β work. Does a **pairwise** charge energy `Σ_{i<j} w_ij Q_iQ_j (+ Σ s_i Q_i²)` escape?

## Arms (all exact; Lean over a generic field, charges as parameters, then SM charges)

* **A (uniform).** `E = w·Σ_{i<j}Q_iQ_j + s·ΣQ_i²`. Identity `2Σ_{i<j}Q_iQ_j = Q_tot² − ΣQ_i²`, so
  `E = (w/2)Q_tot² + (s − w/2)ΣQ_i²`. Predicted (algebra, not yet checked): split `n⊗ν − p⊗e⁻ =
  (s − w/2)(ΣQ²(nν) − ΣQ²(pe))`, non-zero unless `s = w/2`; `ΣQ²` is additive but not separable.
* **B (two weights).** intra-nucleon `w_N`, nucleon–lepton `w_L`, self `s_q`, `s_ℓ`. Report the split
  as a polynomial in the four weights and its zero locus.
* **C (corpus two-term term).** The covariant all-pairs insertion `Q₁₂+Q₂₃+Q₁₃` of
  `NucleonWeightSpaceTwoTerm` / `NucleonWeightSpaceQTrace`, with the derived quantum-trace weighting,
  extended by one lepton strand that the braid does not touch (spectator; premise E1) and the
  normalisation `[2]_q⁴` (premise E2). Raw and connected reported separately; the non-covariant
  adjacent `Q₁₂+Q₂₃+Q₃₄` as a labelled comparison.

## Reported, not chosen

* Which weights the corpus derives vs selects (issue #8524, `two_term_qed_pair_choice`).
* For each derived weighting: exact in q; value at the proton q₀ at 70 dps in MeV via `m_e·t` with
  BOTH overall signs (the sign is not fixed by the corpus: pre-registered `+`, compute `−`).
* CODATA comparison only: `m_n − m_p = 1.29333 MeV`, `Q_β = 0.78233 MeV`. No weight is solved for.
* No coupling is fitted. A result that only reproduces data by choosing a sign, raw-vs-connected or a
  normalisation is reported as a selection.
