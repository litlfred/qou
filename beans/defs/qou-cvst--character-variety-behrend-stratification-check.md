---
# qou-cvst
title: Does the 4_1 character variety carry the odd-odd Behrend stratum the parity obstruction demands?
status: in-progress
pr: 8194
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T11:00:00Z
updated_at: 2026-10-04T15:18:53Z
parent: qou-frzo
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

## Progress (PR #8194)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/W1SpectralRigidityAndEllipticInvolution.lean` (`0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 advisory` across all 7 static vacuity/borrowed-name audits) and wired into `QOU.lean`.
- [x] Verified exact rational witness in `computations/probes/w1-spectral-rigidity-and-elliptic-involution.witness.json` (`scriptHash: 5e848ba624fe`, `scriptCommitSha: 62bd8cb179998d43808552b8955ff0b3857febae`, `allPassed: true`, `0` raw `float64` fields).
- [ ] Awaiting Merge Manager merge of PR #8194 (`b0ca85df1a1275572e6a829fccdff9eb4eff2fe0`).
