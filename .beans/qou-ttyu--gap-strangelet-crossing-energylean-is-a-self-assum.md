---
# qou-ttyu
title: 'GAP: strangelet_crossing_energy.lean is a self-assuming projection — derive bar-odd form from Q=0'
status: todo
type: task
created_at: 2026-08-08T13:48:25Z
updated_at: 2026-08-08T13:48:25Z
---

`content/quantum-observable-universe/lean/QOU/Observations/strangelet_crossing_energy.lean`
is a **self-assuming projection** (AGENTS.md §3b-cond item 5): the class
`StrangeletCrossingEnergyConjecture` carries the block's own *conclusions* as
fields, and `theorem strangelet_crossing_energy` merely projects them
(`refine <hc.claim_i..., hc.claim_ii..., ?_>`). It satisfies the propagation
audit while deriving nothing.

This was NOT fixed when claim ii's inverted `(q + q^-1)` was corrected to
`(q - q^-1)` on branch `claude/coulomb-decomposition-downstream-2026-08-08` —
that change kept the projection shape.

**The honest restructure.** Carry the *hypotheses* and derive the conclusion:

    Q_def   : ctx.Q_uds = ((ctx.n_plus : R) - (ctx.n_minus : R)) / 2
    E_split : ctx.E_cross = N * ( ((n+ : R) - (n- : R))/2 * (q + q⁻¹)
                                + ((n+ : R) + (n- : R))/2 * (q - q⁻¹) )

then from `claim_i : Q_uds = 0` and `Q_def` get `((n+ : R) - n-)/2 = 0`, rewrite
in `E_split`, and the bar-odd form `N * ((n+ + n-)/2) * (q - q⁻¹)` follows by
`ring`. That turns the block from tautological into genuinely conditional, and
it encodes the `Q`-to-channel link that the corrected `.md` now relies on.

`E_split` should cite the sorry-free `QOU.Braiding.crossingEnergy_split` rather
than restate the decomposition as a fresh assumption.

**Cannot be done blind.** Verification needs a working toolchain. On the branch
above, `lean`-direct was unavailable: restoring `lake-cache/qou-v4-24-0`
exhausted the disk after extracting only `mathlib`, leaving `Batteries`/`aesop`
absent (`unknown module prefix 'Batteries'`). Do not attempt this restructure
without first confirming `lean`-direct exits 0 on the unmodified file.

Related author-call beans: qou-s8d9 (which `Q` claim 1 means — bears directly on
`Q_def` above), qou-h03q (binding-component sign convention).
Context: `docs/audits/2026-08-08-coulomb-decomposition-downstream-propagation.md`.
