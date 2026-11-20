---
# qou-onte
title: 'Research doc: groupoid + derived-category attack routes on the binding gap, with lit requests'
status: todo
pr: 8359
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T17:47:03Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

2026-09-05: doc written — docs/audits/2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md (887 lines). Diagnosis: model b3=0 is a shadow of semisimplicity (HH^{>=1}(H_n(q))=0 => intrinsically formal => no higher operations); the n=4 interleaving cross term is the one degree-0 many-body signal (word topology). Routes A (categorified Markov trace / HH of Soergel cat), B (integralise: Z[q^±], Habiro, affine Hecke — Solleveld HELD), C (groupoidify: BHW spans), D (Yekutieli: degree>=2 descent data; 3-dim Stokes Thm 8.6.6 unexploited), E (factorization homology, no held source), F/G/H assessed. Two formalize-first prunes (F1 formality bridge; honest HH_1 example over Z[q^±]) + one exact test (q-adic order of the interleaving cross term) recommended before any construction.

2026-09-05: §7 item 3 (test T1) executed — see qou-212w and doc §7c. Answer NO: the interleaving cross term is order-zero (a closure component-count difference); route B weakened for b3. Items 4–9 of §7 remain open.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8359, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
