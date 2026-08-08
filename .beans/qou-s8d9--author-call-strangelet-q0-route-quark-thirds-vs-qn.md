---
# qou-s8d9
title: 'AUTHOR CALL: strangelet Q=0 route — quark thirds vs Q=(n+ - n-)/2'
status: todo
type: task
created_at: 2026-08-08T13:48:24Z
updated_at: 2026-08-08T13:48:24Z
---

`content/quantum-observable-universe/observations/strangelet-crossing-energy.md`
claim 1 derives the strangelet's electromagnetic neutrality as

    Q(B_3(u, d, s)) = +2/3 - 1/3 - 1/3 = 0

i.e. by summing quark *electric charges in thirds*. But `def:coulomb-charge`
defines `Q = (1/2)(n+ - n-)`, which lives in (1/2)Z — it has no thirds. Both
routes land on 0, so nothing is numerically wrong, but they are different
objects and only the author knows which one the claim intends.

This matters now because claim 2 was corrected to *depend* on which `Q` is
meant: with `Q = (1/2)(n+ - n-) = 0` you get `n+ = n-` and the bar-even channel
vanishes, which is what the corrected claim 2 uses. If claim 1's `Q` is instead
the quark-charge sum, that implication does not follow and claim 2 needs its own
`n+ = n-` input.

The Lean context field carries the same ambiguity:
`QOU.Observations.StrangeletCrossingEnergyContext.Q_uds` is an abstract real
whose docstring quotes the thirds sum, with no field relating it to
`n_plus`/`n_minus`.

Surfaced by `docs/audits/2026-08-08-coulomb-decomposition-downstream-propagation.md`.
