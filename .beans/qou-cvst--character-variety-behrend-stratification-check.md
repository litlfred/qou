---
# qou-cvst
title: 'Does the 4_1 character variety carry the odd-odd Behrend stratum the parity obstruction demands?'
status: todo
type: task
priority: normal
created_at: 2026-08-11T11:00:00Z
updated_at: 2026-08-11T11:00:00Z
---

Deferred follow-up to qou-dt14 (PR #4998, DTBehrendParityObstruction.lean). That result proved a
NECESSARY condition on any supplier of the knot DT count A_omega(4_1)=3:
  - the Behrend weighting cannot be constant (parity: every even total is blocked, chiEu_even_blocks_three),
  - so the moduli has >= 2 Behrend strata (at_least_two_strata),
  - and at least one stratum carries BOTH an odd Behrend value and an odd Euler characteristic
    (odd_count_needs_odd_stratum).

THE QUESTION: does the actual object — the SL_2(C) character variety of the figure-eight complement,
A_{4_1}(L,M)=0, whose Behrend-weighted DT invariant is the 3 — actually exhibit such a stratification?
This is checkable against the literature (character-variety singularity structure of 4_1; the
Garoufalidis-Kashaev / GGM exponential-network description), and would upgrade the result from a
NECESSARY CONDITION to an IDENTIFICATION of where the odd contribution comes from.

Discipline: this is characterization, not closure. Per the lever map (#4601, derive-then-check) even a
full identification of the DT count would NOT close binding (deuteron B(D)=0.380 MeV, -82.9%), and the
count remains irreducibly external to the 13 QOU drivers (#4599/#4601). Formalize-first: state what the
stratification must satisfy before searching the literature. Do NOT wire anything to production.
Parent: qou-dt14. Owner deferred it 2026-08-11 ("2 bean for later").
