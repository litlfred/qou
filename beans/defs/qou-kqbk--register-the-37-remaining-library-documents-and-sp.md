---
# qou-kqbk
title: Register the 37 remaining library documents and split the bound Inventiones volume
status: completed
type: task
priority: normal
created_at: 2026-08-21T14:46:45Z
updated_at: 2026-08-21T16:06:17Z
---

DONE 2026-08-21 — PR #5384 (qou) + folio-assistant #130.

Registration backlog: 0 unregistered library documents. 712 -> 739 entries,
318 -> 351 naming a library copy.

The 'bound Inventiones volume' this bean's title says to split does NOT need
splitting: it is one 35-page offprint, T.A. Springer, 'Trigonometric Sums,
Green Functions of Finite Groups and Representations of Weyl Groups'
(Invent. math. 36, 1976). The earlier demotion was inferred from the
Goettingen banner on page 1 without reading on; corrected in
docs/audits/library-title-overrides.json.

Bigger find along the way: 201 of 318 registered documents had a
structure.json title disagreeing with their own reference entry, and 174 had
section front matter disagreeing with structure.json — so roughly half the
library's corpus-grep hits were labelled with mastheads and bylines. 204
titles corrected, 4,569 section files re-emitted.

Filed rather than fixed: qou-ghy5 (68 dangling citation keys).
