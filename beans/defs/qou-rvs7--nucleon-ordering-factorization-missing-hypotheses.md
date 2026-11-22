---
# qou-rvs7
title: nucleon ordering factorization missing hypotheses
status: completed
pr: 8218
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:00:00Z
updated_at: 2026-11-22T21:55:07Z
parent: qou-uot9
---

File: `folio/quantum-observable-universe/lean/QOU/Interactions/nucleon_ordering_factorization.lean`
The `nucleon_ordering_factorization` theorem is unprovable. The context class `NucleonOrderingFactorizationContext` just provides variables without asserting the complex Wedderburn decomposition or Markov-trace engine hypotheses that would make the factorisation hold.



Also known as `nofa` (its former front-matter header id; the beans CLI uses the filename id `nucleon_ordering_factorization`). Recorded 2026-10-04.


## Progress (Round 52 — PR #8218)
- Resolved in PR `litlfred/qou#8218` (`claude/round52-devacuify-6qbv-uot9`, HEAD `31f749976663905d17c11fe898c73116da2e8d1b`) with 80-dps mpmath witness `computations/probes/round52-devacuify-6qbv-uot9.witness.json` (`scriptCommitSha = 5355a18ce7a60c5cabb79019663bff82e103d505`).

## 2026-11-22 — wave-2 drain (lean-devacuify), closed on main evidence
Session https://claude.ai/code/session_01Qmmkt5vgAD2YAm4VcqJgrF, main 3c4c98fcc.

The self-assuming class is gone. `QOU/Interactions/nucleon_ordering_factorization.lean` now has `def nucleon_ordering_factorization` (line 142) as the honest carrier, two proved ordering-independence lemmas (lines 128, 159), and a no-go theorem `not_nucleonOrderingFactorization_of_free_data` (line 180). PR #8218 is superseded.

## 2026-11-22 — applicability review (owner instruction 2026-11-22, retroactive)
Session https://claude.ai/code/session_01Qmmkt5vgAD2YAm4VcqJgrF. Checked against docs/coordination/owner-rulings.md on origin/main.

Verdict: ALREADY-DONE for the vacuity defect. The proved lemmas (ordering independence of commuting scalar products, and the no-go theorem) are generic and stand. Critical note: the content block's model, S(π) = ∏(q + d_k) over interface letters d_k, rests on the single-crossing interface letters that the owner superseded on 2026-11-15 (γγ rule; docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md). The block itself needs RESCOPE onto a γγ-selected word, which belongs to the A=2/3 binding lane (#7876, #9120), not this drain.

## 2026-11-22 — id renamed `nucleon_ordering_factorization` → `qou-rvs7` (bean-hygiene, owner-approved)

Session https://claude.ai/code/session_01Qmmkt95ogQs6aFq9zdMmwF. The old id contained underscores, which the tracker's id pattern `[A-Za-z0-9-]+` rejects, so `scripts/check-beans.sh` reported this file as having no id and every `beans` query missed it. Renamed on the owner's approval of qou-w3yy (project-chat card, 2026-11-22 21:53Z). Content unchanged; the old id stays greppable here.
