---
# qou-zloi
title: Phi_q pole in per_generator_V_hat_3A is set by alpha_i, not by the Markov convention
status: completed
type: task
priority: normal
created_at: 2026-08-29T08:27:35Z
updated_at: 2026-08-29T10:48:57Z
---

Measured 2026-08-29 on branch claude/tower-gap-lean-and-infra-2026-08-29
(PR #5978), probe computations/probes/tower_vhat_markov_parameter_probe.py,
witness computations/tower-vhat-markov-parameter.witness.json.

THE FINDING. `mass_at_3A_proper.per_generator_V_hat_3A` runs V_hat up against
the Phi_q pole (bean qou-2tuv; the function's own docstring records 1.08837
against a cap of 1.087779, and that number is the NEUTRON's gen 1, not the
proton's). It is tempting to read this as an instance of the convention C -> D
cascade on bean qou-dchz item 1, since z_D = 0.6127 is 22.70 % closer to the
pole than z_C = 0.4993. It is not, and re-pinning the convention cannot move it.

Factoring the one-generator collapse out (QOU.BraidsAndKnots.prod_eq_linear,
proved this branch) gives V_hat_i = alpha_i * Z + beta_i * W with

    Z = Sum_lambda omega_lambda tr(sigma^lambda) / dim lambda

the effective Markov parameter -- the only place a convention can enter.
Measured at 50 dps under the production normalized_plancherel scheme:

    Z = 0.10453014939781965772   IDENTICALLY at n = 3, 6 and 9
      = (q - 1/q)/2 = h/2        to 3.3e-52

(the unnormalised Plancherel scheme, by contrast, gives a visibly n-dependent
Z: 0.10321727 at n=3, 0.10359769 at n=6.)

WHY, PROVED. QOU.BraidsAndKnots.markov_param_eq_half_h: normalised
(Sum omega = 1) plus transpose-symmetric (omega_{lambda'} = omega_lambda)
weights force Z = h/2 for any n. The proof uses nothing about Plancherel
weights, Hecke algebras or partitions -- only those two facts plus the
eigenvalue exchange (transposing a shape swaps the multiplicities of q and
-1/q, so the two normalised traces sum to h). All three hypotheses are verified
against the production weight table in the probe, not assumed.

CONSEQUENCES.

1. Z is pinned by symmetry at 0.1045 -- 79 % below convention C, 83 % below D.
   The convention question does not reach this producer.
2. The pole distance is set by alpha_i (QOU.BraidsAndKnots.vHat_margin: the
   margin measured in z is the margin measured in V_hat DIVIDED BY alpha), so
   the braid word is what to look at.
3. markov_param_indep_of_weights: EVERY normalised transpose-symmetric scheme
   gives the same Z. Searching that family for one that moves the pole is
   futile. This is the formalize-first prune: the search was killed before it
   was coded.

SCOPE-(a). Measures the construction as built. Says nothing about what the
right V_hat is; per_generator_V_hat_3A's own verdict that both its weight
schemes are wrong for the tower stands, and no ingredient is excluded.

ALSO RECORDED. The corpus carries two inequivalent V_hat for the proton and
they are not roundings of each other:
  canonical_tower.per_gen_V_hat_canonical    [0.6629533727, 1.0646262154]  95.91 % of q
  mass_at_3A_proper.per_generator_V_hat_3A   [0.6713858244, 1.0551103188]  95.06 % of q
The first is a Plancherel-averaged JM eigenvalue, the second the H_{3A}
character sum. Different objects, by their own docstrings.
