---
# qcz9
title: 'Chip: scope contact-boundary to a QOU with 2|χ(A) (Descartes), map is χ-independent'
status: todo
type: task
priority: high
parent: qcz6
created_at: 2026-07-24T16:46:17Z
updated_at: 2026-07-24T16:46:17Z
---

Corpus-verified: χ(A)=-6 is NOT implied by a general QOU — it is the
Descartes universe (Bring Σ4, terminal object among QOUs with χ(A)=-6);
the substrate admits varying-χ QOUs (particle-interactions/varying-euler-intro.md).

Fix: the core Skein-Collatz results (map, no-cycles, 2-cycle, domain
non-invariance) are χ-INDEPENDENT — keep 'Given a QOU'. But
collatz-contact-boundary's Kummer step needs 2|χ(A) (2|-6). Re-scope its
banner: 'Given a QOU with 2|χ(A) (e.g. the Descartes universe χ(A)=-6)'.
Update collatz-contact-boundary.md + collatz_contact_boundary.lean
(the context class already has chi_A=-6 as a FIELD — good, that IS the
hypothesis; make the narrative banner match, don't imply general QOU).
Cheap, do first. Render-QA + lean-direct verify.
