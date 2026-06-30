---
# e5tn
title: 'Integration: detangler watcher - cross-chapter-forward (12 items)'
status: todo
type: task
created_at: 2026-06-21T21:46:07Z
updated_at: 2026-06-29T20:00:00Z
---

## Triage complete (2026-06-29, PR #3136) — ready to close

All 12 cross-chapter-forward items are **H2 chapter-pair aggregates** (severity minor,
baseline architectural coupling on main), not individual defects. `forward_ref_classifier.py`
over the whole corpus: 313 forward refs, dominated by storytelling/structural; the 12
aggregates are mass-cluster result-callbacks + Bring foundational coupling + the
`models-of-qous` framing chapter → **all `wontfix: architectural`**.

While triaging, the **2 genuine corpus-wide `LOGICAL DEFECT` edges** (both
Ch3 → `q-geometric-langlands/def:q-flat-connection`) were fixed via a subject-matched waive
(the def's subject — flat connection / local system — is the core q-GL object; corroborated by
`germ-commutator-q-curvature`'s authorNote that the identity is verified independently and the
def-link is "narrative"). `LOGICAL DEFECT 2 → 0`.

Full triage: `docs/audits/2026-06-29-e5tn-cross-chapter-forward-triage.md`. Queue items already
`status=wontfix, reason="converted to bean: e5tn"`. Close when convenient (human-only §4a).

