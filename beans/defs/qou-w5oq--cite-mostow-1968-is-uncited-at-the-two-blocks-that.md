---
# qou-w5oq
title: 'CITE: Mostow 1968 is uncited at the two blocks that make it load-bearing — M — approach-to-exceptional-divisor, swampland-island-of-consistency'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:05:25Z
updated_at: 2026-10-04T15:17:55Z
parent: qou-mub3
---

**Class M — the key exists and is bib-QA verified-clean; the two blocks that lean
hardest on it do not use it.**

`[mostow1968]` — Mostow, G. D., *Quasi-conformal mappings in n-space and the
rigidity of hyperbolic space forms*, Publ. Math. IHÉS **34** (1968) 53–104,
`references.ts:5036`, status `verified-clean` in `content/bib-qa-verifications.json`.
Companion `[gromov1982]` likewise. **Neither has a `library:` block**, and
`content/bib-qa-verifications.json` records `local_pdf: "uploads/mostow1968.pdf"` /
`"uploads/gromov1982.pdf"` — **both paths do not exist** (`uploads/` holds 22 PDFs
and neither is among them). So the ledger points at files that are gone.

**The two load-bearing, uncited sites.**

1. `folio/quantum-observable-universe/brings-surface/approach-to-exceptional-divisor.md:11`
   — *"Mostow rigidity (geometric confinement) makes the resulting topology—and
   hence the mass—discrete."* Its `.ts` has **no `cites` field at all**.
2. `folio/quantum-observable-universe/information-theory/swampland-island-of-consistency.md:11`
   — *"By Mostow rigidity, a finite-volume hyperbolic structure of dimension at
   least three admits no continuous deformation. Therefore, the topological data
   and the masses derived from it are discrete."* Its `.ts` cites
   `["vafa2005", "arkani-hamed2007"]` — the swampland literature, not Mostow.

Only `mass-theory/atom-knot-mass-derivation-proof` cites it
(`.md:81` `\cite{mostow1968}`, `.ts:15`).

**Credit where due:** `swampland-island-of-consistency.md:14` is *scrupulously*
honest about the limit of the claim — *"The stronger reading—that this geometric
rigidity selects the substrate parameter `q₀`—is motivational, not derived …
Mostow rigidity makes the hyperbolic geometry discrete. It does not, on its own,
determine the substrate modulus."* This bean is about the missing key, not about
an over-claim.

**Also (C):** `lean/QOU/Eightfold/HyperbolicVolumeFormType.lean:81,84,152` leans on
Mostow explicitly (*"Mostow rigidity, or that `Vol(4₁) = 2·Cl₂(π/3)`. Both cited."*)
and carries **zero `-- Ref:` lines**.

**Held sources that state it**, if a secondary is preferred to the primary:
`Mostow rigidity` matches 9 `library/*/sections/` dirs — `nrarith` (Neumann–Reid),
`zagier-the-dilogarithm-function`, `arxiv-2304.12545v1` (Garoufalidis–Zagier on
Walter Neumann's work), `symmetry-11-01298`, `arxiv-0903.2472v1`,
`arxiv-1511.00400v2`, `arxiv-1910.09966v1`, `hyperbolicandneumann`; the bare string
`Mostow` matches 27 dirs including `thurston` and
`milnor-1982-hyperbolic-geometry-the-first-150-years`.

**Fix:** add `mostow1968` to the two `.ts` `cites` lists and a `-- Ref:` at
`HyperbolicVolumeFormType.lean`. Optionally repair the two dangling `local_pdf`
paths in `bib-qa-verifications.json`, or ingest the two IHÉS papers (both free at
numdam.org, URLs already in `references.ts`).

Found by the citation-gap sweep, `docs/audits/2026-09-04-citation-gap-inventory.md`.
