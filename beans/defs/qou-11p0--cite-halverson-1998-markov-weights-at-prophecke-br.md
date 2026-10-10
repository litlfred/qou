---
# qou-11p0
title: Cite [halverson-1998-markov-weights] at prop:hecke-branching-trace-decomposition
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:08Z
updated_at: 2026-10-10T07:37:08Z
parent: qou-mub3
---

Act on the registry's own standing FLAG: the branching / Murnaghan–Nakayama-type content asserted by the branching-trace block is in [ram1991]/[hoefsmit1974], not in this type-B/D weights paper.

Source: `library/arxiv-math-9806163v1/9806163v1.pdf` (`halverson-1998-markov-weights`)
Relevance: **tangential** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.


## 2026-10-10 — pointer

Tracked under carrier M14 (qou-9w2m) of epic `qou-d8c7` "Mass endomorphism" (issue litlfred/qou#7547). Parent and status unchanged; the epic body lists what is still open for this item and where it sits in the attack-vector catalogue.

## 2026-10-10 — half done (issue litlfred/qou#7552)

`hecke-branching-trace-decomposition.md` now cites `\cite{hoefsmit1974}, \cite[(2.3), Thm.~2.4]{halverson_ram_1998}` for the seminormal module; `halverson_ram_1998` added to the .ts cites. Note: `halverson-1998-markov-weights` was merged into `orellana1998` on 2026-08-16, which is the key the .ts actually carries. Left open: whether to drop `orellana1998` (type B/D Markov weights, tangential) from the .ts is the owner's call, and the LR restriction H_{n+m} -> H_n (x) H_m has no held source stating it directly (Goodman-Wenzl / Ram not ingested).

## 2026-10-10 — done (owner: "Drop")

`orellana1998` removed from `hecke-branching-trace-decomposition.ts` cites on the owner's call (issue litlfred/qou#7552, PR #7554). The block now cites `hoefsmit1974` and `halverson_ram_1998` (2.3), Thm 2.4. Still true and not this bean's to fix: no held source states the LR restriction H_{n+m} -> H_n (x) H_m directly.
