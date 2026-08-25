---
# qou-xy5f
title: 'canonical-ordering-dof Part 6: eight C-era readings blocked on qou-eea0 pass 2'
status: todo
type: task
priority: normal
created_at: 2026-08-10T09:13:33Z
updated_at: 2026-08-10T09:14:17Z
---


Blocked on qou-eea0 pass 2; closes with it.

`canonical_ordering_dof_probe.py` Part 6 asserts `closed_form_matches_full_trace`.
It passes 22/22 on main and fails 1/22 on #4899, deliberately.

Part 6 checks `interface_factors()` against eight decimals hardcoded from two
independent full-trace pipelines. The closed form migrated to
z = q^3/(q^2+1) with the rest of the producer layer; the eight readings did not.

    T_npn_over_pnn     measured 1.36013 / 1.36037   closed 1.25898   rel 8.0%
    He3_pnp_over_ppn   measured 0.79066 / 0.79080   closed 0.82939   rel 4.7%

The two sources agree with EACH OTHER to ~1e-4 while both differ from the
closed form by the same 8.0% / 4.7%. That is a convention shift in the closed
form, not an error in either pipeline.

**Why it cannot be fixed in place.** The readings come from the nuclear layer
— n = 9 H_3A words and He-3 — which is exactly the set the fingerprint work
list missed and pass 2 has not regenerated. Only a re-run produces the number;
there is no closed form to substitute, which is what made the sibling case
(`markov_trace_recursive`'s expected column) fixable and this one not.

Left RED and annotated in place with the numbers and the diagnosis. Retuning
the constants would fabricate a measurement; muting the assertion would hide
it. A convention migration that silences its own cross-check is the failure
this arc exists to unpick.

**To close:** after pass 2 regenerates the H_3A / He-3 witnesses, retake the
eight readings from them and replace the literals. The assertion should go
green on its own; if it does not, the disagreement is real and is a finding.
