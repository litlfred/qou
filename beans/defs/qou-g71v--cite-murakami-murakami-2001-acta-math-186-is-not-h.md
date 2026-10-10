---
# qou-g71v
title: 'CITE: Murakami-Murakami 2001 (Acta Math. 186) is not held — U — 63 citers, the volume conjecture''s founding statement'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:03:28Z
updated_at: 2026-10-04T15:14:44Z
parent: qou-1qhv
---

**Class U — registered, cited 63 times, and not in `library/`.**

**Work:** Murakami, Hitoshi & Murakami, Jun, *The colored Jones polynomials and
the simplicial volume of a knot*, Acta Mathematica **186** (2001) 85–104,
DOI `10.1007/BF02392716`. arXiv preprint `math/9905075`.

**Measured 2026-09-04.** `references.ts:5111` registers `murakami-murakami2001`
with **no `library:` block** (no `docId`). Confirmed absent four ways:
`library/INDEX.md` has **0** rows matching *"simplicial volume of a knot"*,
*"Kashaev's invariant"* or *"Yokota"*; there is no `library/*9905075*` and no
`library/*murakami*` directory; no `summary.json`/`structure.json` carries the
title; and `uploads/` (22 PDFs, the un-ingested queue that path 5 cannot see)
does not hold it either.

**Cited in 63 files** — `.ts` `cites`, `.md` `\cite{}` and Lean `-- Ref:` alike;
among them `mass-theory/dilog-saddle-regime.ts`,
`appendix-surreals/b1-figure-8-row-theorem.ts`,
`mass-theory/atom-knot-mass-derivation-proof.lean:102`. It is the statement L5 of
the hyperbolic-volume route rests on
(`docs/audits/2026-09-04-how-the-hyperbolic-volume-could-arise-from-qou.md` §2),
and the counterpart to `[kashaev1997]`, which **is** held
(`library/arxiv-q-alg-9601025v2/`) and cited 73 times.

**This is the single highest-leverage upload on the arc**: it is the most-cited
un-held work in the hyperbolic-volume layer, and its absence means every
`murakami-murakami2001` locator is uncheckable in-corpus.

**Partial mitigations that do not replace it.** ~16 held documents restate the
theorem (`arxiv-2604.16077v1`, `arxiv-math-0508100v6`, `arxiv-2111.06645`,
`ki52`, `ki6c`, `arxiv-math-0506456v1` = the held Andersen–Hansen, …), so the
*mathematics* is reachable. What is not reachable is the primary the corpus
names. See sibling bean on registering `library/0803219` (Murakami's
*Introduction to the volume conjecture*), which is held and would give the
survey-level locators a key.

**Fix:** fetch `math/9905075` (or the Acta version), run
`scripts/migrate-uploads-to-library.py`, and add the `library:` block to
`references.ts:5111`.

Found by the citation-gap sweep, `docs/audits/2026-09-04-citation-gap-inventory.md`.
