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

## Addendum 2 (13:41Z, before `both_rules.py` ran; owner: "explore both of the options")

For the nucleon rule (f = q/[2]⁴, K-allowed sector times ν̄) and the Markov rule (f = t(Δ)),
each in the one-sided and the shared placement, report without choosing:
(a) whether the rule respects K-weight conservation (sector restricted vs summed);
(b) the sign of F at q₀, i.e. whether the neutron comes out heavier;
(c) the q → 1 behaviour of Q_β (finite or ~E₀);
(d) the exact value with both E₀ forms (order-zero, tower) to show the E₀ spread;
(e) only then the comparison with CODATA Q_β and m_n − m_p.

## Addendum 3 (written before `reading_probe.py` ran; owner: "not yet, derive the reading")

Question: which energy is E₀·F for the one-sided nucleon-rule F = ε_n − ε_p·f? Test each reading
against the energy map it would have to use, with no comparison value used to decide:
(g) linear map E(X) = E₀·ε(X), multiplicative traces: the energies E(n), E(p), E(p e⁻ ν̄), the
    lepton-pair energy E(p e⁻ ν̄) − E(p), and E(n) − E(p). Pass for the Q_β reading iff the
    lepton-pair energy is > 0; pass for the m_n − m_p reading iff E(n) − E(p) = E₀·F.
(h) logarithmic map E(X) = ±E₀·ln ε(X), both signs: the same two quantities.
(i) only after (g) and (h): the lepton-pair energy against m_e, printed, not used to decide.
Lean twin: `QOU.QBeta.OneSidedReading` (signs proved on 1 < q ≤ 23/20).
