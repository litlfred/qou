---
# qou-20yf
title: 'The Phi_q margin is a chain-length fact: n=4 is the last even sigma-inverse chain inside the pole'
status: completed
type: task
priority: high
created_at: 2026-08-29T09:45:01Z
updated_at: 2026-08-29T10:48:57Z
---

Measured 2026-08-29, branch claude/tower-gap-lean-and-infra-2026-08-29 (PR
#5978). Probe computations/probes/tower_vhat_chain_length_pole_margin_probe.py,
witness computations/tower-vhat-chain-length-pole-margin.witness.json.
8 checks, all passing; mpmath 50 dps; 0 raw float64 in the witness.

Follows qou-zloi (Z pinned at h/2) and qou-lbgh (the 6.04 % headroom on the
OTHER producer). This one is about mass_at_3A_proper.per_generator_V_hat_3A.

THE WORRY IT SETTLES. per_generator_V_hat_3A runs V_hat to 98 % of the Phi_q
pole (qou-2tuv). If that margin DEGRADED with nucleon count, the tower would be
undefined past some atom. It does not.

  * max |V_hat| SATURATES: 1.0883675333971881278 (98.053 % of q) for EVERY
    neutron-containing atom, already at A = 1, unchanged through A = 16.
  * A proton-only system sits strictly further out, 1.0551103188317245612 --
    the neutron's dd pair contributes a further sigma^-1 where the proton's uu
    pair contributes a sigma.
  * The number of distinct per-generator (alpha, beta) saturates at SEVEN from
    A = 4 on. Adding nucleons only repeats a finite alphabet of local
    environments.

Cheap to establish because markov_param_eq_half_h pins Z = h/2 with no
computation and prod_eq_linear reduces each generator to (alpha, beta): no
seminormal matrices, no character sums, A = 16 costs what A = 1 costs.

THE ALPHABET, using sigma - h = sigma^-1 (skein; QOU.BraidsAndKnots.
sigma_mul_sub_h) and sigma - h/2 = (sigma + sigma^-1)/2 = avg:

    |V|/q     word
    0.98053   sigma^-4                    <- the max
    0.95057   sigma^-3 * avg              <- proton; its BETA equals the max
    0.60486   sigma^4 * avg * sigma^2
    0.49700   sigma^3 * avg^2 * sigma^2
    0.09417   sigma^-1        (V = -h/2)
    0.09417   sigma           (V = +h/2)
    0.0000648 colour-weighted avg

THE SHARP PART. At z = h/2 the Markov trace is the AVERAGE of the two Hecke
eigenvalue evaluations sigma -> q and sigma -> -1/q (QOU.BraidsAndKnots.
vHat_half_h_eq_avg_evals -- and that is also WHY transpose-pairing forced h/2 in
markov_param_eq_half_h: transposition swaps the two eigenvalues). Each
evaluation is multiplicative (prod_eq_linear), so the chain has a closed form
(QOU.BraidsAndKnots.vHat_invChain, sorry-free):

    V_n = ((1/q)^n + (-q)^n) / 2

verified against the recursion to 5.3e-51 over n = 1..12. Since |-q| > 1,
|V_n| -> infinity: only finitely many chain lengths keep Phi_q finite.

    n = 4   |V|/q = 0.98053   <- the length the word uses
    n = 5   |V|/q = 0.49163
    n = 6   |V|/q = 1.08331   <- PAST THE POLE

n = 4 is the LAST EVEN chain length inside the pole. One further same-sign
crossing pair diverges the tower.

WHAT THIS DOES NOT SAY. It does NOT say the 4 is tuned. It is 3 + 1 -- three
crossings from the B_3 closure, one from the quark pair -- both fixed upstream
by the construction and not chosen against this margin. What it does say is that
the 1.95 % headroom is the whole of it, and that it is a fact about chain length
rather than about robustness. Anyone extending the braid word (heavier quark
content, extra gluon modes, a longer intra-nucleon chain) should check the
chain length against this before assuming the tower stays finite.

SCOPE-(a). Measures the construction as built; excludes no ingredient.

A CORRECTION MADE IN PASSING, kept in the probe. The saturation check first
asserted ONE maximum across all atoms and FAILED: proton-only is 1.05511,
neutron-containing is 1.08837. The data was right and my claim was wrong. Fixed
by splitting the statement, not by loosening the check -- and the split is the
better finding, since it says the neutron sets the margin.
