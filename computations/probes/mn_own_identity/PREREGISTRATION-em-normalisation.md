# Pre-registration: which insertion normalisation does the corpus force for α·S? (2026-11-22)

Owner, 2026-11-22: *"1"* (derive the normalisation, per-block relative versus sector share, from the
Lagrangian). §44 left two values: per-block relative −2.3008 MeV, sector share −0.7633 MeV. This is
an argument from corpus artefacts plus one exact check; both values are already known, so it is an
adjudication, not a blind prediction. Written before the check script exists.

## The argument (each link cites the artefact that fixes it)
1. The canonical absolute nucleon mass is the full Markov trace, m_p = 2m_μ|tr_M(β_Bor)|[3]_q!/q³
   − 12m_e, routed through `computations/canonical_mass.py` (AGENTS.md STRICT: every absolute
   nucleon mass goes through that facade). It is not a weight-block share. Both nucleons carry
   the same word V³ (§44 C1), so in this functional p and n differ only by the strand charges.
2. A degree-0, charge-symmetric quadratic k₁ΣQ_a² + k₂Σ_{a<b}Q_aQ_b takes k₁ on the proton and
   (2/3)k₁ − (1/3)k₂ on the neutron (`QEDHigherOrderCovariance.degreeZero_values`, sorry-free).
3. Owner ruling A (2026-11-22): S = QPair·hol enters with coefficient α, energy ⊃ +α·S. QPair is
   the pair sum, so k₂ = α, k₁ = 0.
4. A degree-0 term acts as a scalar insertion (1 + a) on the F_Bor term, and shifts the mass by
   a·M_QCD (`scalar_insertion_shift`, sorry-free; the reading "rescales the whole F_Bor term" is
   the file's §S).
5. Hence a_p = 0, a_n = −α/3, and E_n − E_p = −(α/3)·M_QCD.
6. The sector share τ_W = q^{±1}tr_W/[2]³ is the §35 muon map, which is not the canonical facade,
   so step 1 excludes it. This exclusion is made by a corpus rule. It is not made by closeness: the
   excluded value (−0.763) is the closer of the two to the lattice −1.00.

## Predictions
- P1. The strand-charge reading (steps 2–5) and the weight-block reading (§44 C3) give the same
  a_n, a_p exactly, because QPair is constant on each weight block (−1/3 on W_n, 0 on W_p). So
  E_n − E_p = −2.3008 MeV at q₀ under either labelling.
- P2. α(1) = 1/90 ≠ 0, so E/M_QCD → −1/270 at q = 1. This term breaks m_p = m_n at q = 1 (bean
  `qou-az9l`) in ratio as well as in MeV. Reported as a tension with that working assumption.

## Links NOT forced (stated now, reported unchanged)
- Step 4's reading: no theorem derives "ℒ ⊃ −αS ⇒ scalar insertion on F_Bor" from the Lagrangian.
- k₁ = 0 comes from the ruling's S, which has no self-energy ΣQ². The lattice −1.00 MeV includes
  self-energy, so the comparison is between different objects.
- The central U(1) colouring of V³ gives k₁ = k₂ = 0 (`u1Trace_borromean`). So the α·S term is not
  produced by that invariant; its coefficient rests on ruling A.
- The neutron's F_Bor multiplier is taken equal to the proton's (same word); the difference is
  second order in α.
**Pre-registration completed: 2026-11-22T10:51:16 (UTC), before the check script exists.**
