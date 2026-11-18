---
# qou-b5ly
title: 'CITE: Riemann-Hurwitz has no reference key anywhere in references.ts — M — brings-is-qou-verification.md:15 (no cites at all), CoveringDegreeRamification.lean:88-91'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:06:49Z
updated_at: 2026-10-04T15:17:56Z
parent: qou-1qhv
---

**Class M/U — the corpus uses Riemann–Hurwitz as arithmetic and has no key for it
at all, while holding ten sources that state it.**

**`references.ts` has no Riemann–Hurwitz entry, and no Riemann-surface textbook.**
Measured over all 828 ids: no `riemann`, `hurwitz`, `forster`, `miranda`,
`farkas`, `kra`, `griffiths` entry. (`ClassicalRiemannHypothesis` in `.beans/` is a
different subject.)

**Two sites use it, both unsourced.**

1. `folio/quantum-observable-universe/brings-surface/brings-is-qou-verification.md:15`
   — *"The degree-4 covering `π` has 6 branch points with total ramification
   `R_tot = 14` (Riemann–Hurwitz)."* Its `.ts` has **no `cites` field at all** —
   and the same block also asserts *"The differential calculus `Ω¹(A)` is the
   Woronowicz 3-dimensional calculus"* uncited, though its sibling
   `brings-is-qou-proof` **does** cite `woronowicz1987-twisted-su2`
   (`.md:11,15`, `.ts:12`). Fold that half in while editing this block.
2. `folio/quantum-observable-universe/lean/QOU/BringsSurface/CoveringDegreeRamification.lean:88-91`
   — the file is explicit that `ramification` is *"a **definition** encoding
   Riemann–Hurwitz for a `ℙ¹` target, not a proof"*, and lists *"the
   Riemann–Hurwitz theorem itself"* under what is **not** proved (`:73`). The file
   carries **zero `-- Ref:` lines**.

**Ten held sources state it** — `Riemann-Hurwitz` (hyphen) 7 section dirs
(`2018sorus020`, `210811825v1`, `arxiv-1204.4824v2`, `arxiv-2208.13692v1`,
**`arxiv-2402.08782v1`**, `arxiv-2502.02662v1`, `disssubmission`);
`Riemann–Hurwitz` (en dash) 3 more (`ant-v14-n7-s`, `ant-v14-n7-s-p07`,
**`s40879-023-00706-0`**). Note the spelling split: **neither list is a superset of
the other**, the same trap as `Bloch-Wigner` 135 vs `Bloch–Wigner` 19.

**The cheapest fix uses a source already held AND registered.**
`s40879-023-00706-0` = **Braden & Disney-Hogg, *Bring's curve: old and new*** —
about Bring's curve specifically, holds the en-dash Riemann–Hurwitz, and is already
in `references.ts` (bean `qou-1twx` cross-checks it elsewhere). `arxiv-2402.08782v1`
(*Hecke–Farey coordinates for Bring's surface*) holds the hyphen spelling and is
the second Fuchsian route to the same curve.

**Fix:** cite the held Bring paper at both sites; optionally register a textbook
(**Miranda, *Algebraic Curves and Riemann Surfaces*, GSM 5, 1995, §III.4** or
**Forster, *Lectures on Riemann Surfaces*, GTM 81**) for the general statement.
No ingest is required for the minimal fix.

Found by the citation-gap sweep, `docs/audits/2026-09-04-citation-gap-inventory.md`.
