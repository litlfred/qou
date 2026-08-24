---
# qou-ny5l
title: Add reference for modular.qholonomic.modules.pdf at conj:stokes-dt-bps-bridge
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:37:00Z
updated_at: 2026-08-21T17:03:48Z
---

The corpus registers two companion papers on resurgence and Stokes data in complex Chern--Simons but not the one that supplies the effective solution method for the underlying q-difference equations.

**From the source**
- Def. 1.1 with Thm 1.2 (the slash operator), and Thm 1.4 — A q-difference equation is modular when the monodromy relation holds for all of SL(2,Z); it suffices to check the generators S and T, and the generalised q-hypergeometric equation is modular and self-dual with the two natural cocycles equal.
  Use here: A checkable criterion (two generators) for the modularity of the q-difference equations the corpus works with, and with it the effective solution method the Stokes-matrix work currently lacks.
- Sec. 1.5 (modular q-holonomic modules in Chern--Simons theory), Thm 1.5 — Three q-holonomic modules arising in complex Chern--Simons theory are modular, with explicitly computed monodromy and cocycles.
  Use here: Places the corpus's own state-integral and descendant equations inside a class with computable monodromy, which is the missing ingredient in the Stokes-matrix identification target for the figure-eight descendant equation.

Source: `library/modularqholonomicmodules/modular.qholonomic.modules.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/modularqholonomicmodules/  ->  [garoufalidis-wheeler-modular]
  Modular q-holonomic modules

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
