# Pre-registration: q = 1 coefficient of Q_β as an interaction (2026-11-21)

Owner choice (card, 2026-11-21 13:33Z): "Q_β as an interaction (q = 1 first)".
Written before `qbeta_interaction_q1_probe.py` was run.

Premise (corpus form, not new): Q_β = E₀^full · F, E₀^full = m_e/(q(q−1))/(1−ℏ_q²).
Since E₀^full ~ m_e/(q−1) as q → 1, the q = 1 coefficient of Q_β/m_e is
c(F) = lim_{q→1} F(q)/(q−1). If F vanishes to order k ≥ 2 at q = 1, c(F) = 0.

Questions:
1. Prove the reduction c(F) = F'(1) (Lean, any F = (q−1)·G with G continuous; here
   stated for rational F as an identity E₀^full·(q−1)G = m_e·G·q/(2q−1)).
2. For every exact interaction quantity on record in the pair-creation probes
   (`beta_pair_creation_word/*.witness.json`: cross terms C₁, charged-current block entries,
   character values, for A = V₁³, B = σ₀σ₁σ₂, B̄, C = σ₂, D-family, and the two-term
   connected term conn(β)): its order at q = 1 and its c(F).
3. For the electron Δ = σ₀σ₁σ₀ as a multiplicative factor: its Markov value at q = 1
   (from the eigenphase thread's t(Δ) = z(hz+1), z = z_D).
4. Only then: E₀^full·|F| at q₀ for the order-1 objects, and the comparison.

Nothing is selected. A finite c(F) is reported for every object; none is adopted as Q_β.

## Addendum (written before `lepton_factor_q1.py` was run, 13:45Z)

Lead from the eigenphase thread (#8836): a lepton factor on one side only makes the functional
order 0 at q = 1, so Q_β ≈ E₀·F(1) and F(1) is a counting number. Questions:
5. K-weight conservation n → p + e⁻ (+ ν̄): which electron weight sector b (number of d strands
   among the electron's three) is allowed, with and without a ν̄ strand of weight q^{±1}.
6. F(1) = ε_p(1)·(1 − f(1)) for the lepton factor f under each rule on record, none chosen:
   (i) the nucleon rule (K-weight × plain sector trace / [2]^n) on the K-allowed sector, with
   and without the ν̄ factor; (ii) the Markov value t(Δ); (iii) the plain per-sector trace.
The comparison column is printed last. None is adopted.
