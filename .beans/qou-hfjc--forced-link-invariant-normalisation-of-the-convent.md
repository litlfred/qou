---
# qou-hfjc
title: 'Forced link-invariant normalisation of the convention-D Ocneanu trace (mu=[2]_q, nu=q^-2) equalises every single-crossing bond factor: the log law becomes pure bond counting, and the wrong-signed asymmetry is an artifact of the un-normalised trace'
status: completed
type: task
priority: normal
created_at: 2026-09-04T12:21:15Z
updated_at: 2026-09-04T12:31:38Z
---

Branch claude/forced-link-normalisation-bond-counting-2026-09-04. Answers avenue 4 of #6611's decision frame by derivation rather than scan.

LEAN (QOU/MathlibExt/ForcedLinkNormalisation.lean, sorry-free, 11 decls axiom-clean): the two Markov moves force nu² = z'/z and mu = 1/(nu z) (nu_sq_forced, mu_forced); then nu z = nu⁻¹ z' — a positive and a negative crossing have the SAME normalised weight (normalised_weights_equal) — so every branch mixture cp σ + cm σ⁻¹ with cp+cm = 1 weighs the same (normalised_mixture). Convention D: nu = q⁻², mu = [2]_q, common weight q/(q²+1) (convD_*). #6611 §3 scanned substrate constants for mu (which CANCELS under the log law, both words have 3A strands) and never solved for nu; objection (a) 'no single writhe' is answered by linearity per branch.

CONSEQUENCE: under B = E_0 ln(tr_free/tr_atom) + monotone factorization, every bond letter (pp = σ, nn = σ⁻¹, pn colour-weighted mixture) normalises to q/(q²+1), so B_norm = (A−1)·E_0·ln[2]_q with ε = 2.9242463 MeV derived. The un-normalised bond energies (0.490/0.677/0.907) and #6611's wrong-signed κ_derived = +0.22 are exactly the writhe factor nu^e; κ = 0 identically after normalisation.

PROBE (forced_link_normalisation_bond_counting_probe.py, 33/33, 50 dps, #6611's AME selection + percentile fn verbatim): all 9 production bonds normalise to q/(q²+1) to 50 dps; spread p5–p95 1.18085 (normalised) vs 1.22497 (un-normalised segregated chain) — identical to #6611's empirically-best 'bond COUNT only' 1.1809, which the normalisation PREDICTS; full range 10.2× → 8.2×; median AME/B_norm = 2.82 (ε would need 8.25 MeV — the qou-59j5 scale factor, a target not a criterion). 2H 0.76×, 3H 1.45×, 3He 1.32×, 4He 3.23×.

NOT established: that the normalised functional is the physics (it is the per-branch link invariant; that is an argument). Decision framed in docs/audits/2026-09-04-forced-link-normalisation-bond-counting.md §6; recommendation (judgement): re-measure the residual shape on the normalised law first. Nothing wired; E_0 untouched.
