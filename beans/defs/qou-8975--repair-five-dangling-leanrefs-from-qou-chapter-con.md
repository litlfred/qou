---
# qou-8975
title: Repair five dangling lean.refs from QOU chapter consolidation
status: completed
type: task
created_at: 2026-11-25T11:37:55Z
updated_at: 2026-11-25T11:37:55Z
---

PR litlfred/qou#9425. Refs 1,2,3,5 retargeted to <Library>.<Module>.<decl> locator form (true FQNs do not resolve under lean-coverage after 559a7210b); #4 sibling renamed t-beta-markov-collapse-general-lift.lean -> t-beta-markov-frobenius-collapse-general.lean. All 5 lean-direct exit 0, no sorryAx. Authors' note 721/726. Open owner question: should lean.ref carry true FQNs (needs folio-assistant resolver fix)?
