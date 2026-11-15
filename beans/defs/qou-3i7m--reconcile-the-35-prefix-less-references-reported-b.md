---
# qou-3i7m
title: Reconcile the 35 prefix-less references reported by gen-block-jsonld
status: completed
type: task
priority: normal
created_at: 2026-09-05T09:58:09Z
updated_at: 2026-09-05T09:58:34Z
---

Done on `claude/prefixless-refs-2026-09-05`, PR #6819. **Zero content defects; no content block changed.**

**The finding.** All 35 prefix-less references reported by
`gen-block-jsonld --paper quantum-observable-universe` name a block that
EXISTS, and all 7 distinct targets are `prose` — a kind the AGENTS.md
Type-system table gives no required label prefix. 0 dangling references in
the paper. Every inbound reference to a bare-labelled block is *itself*
written bare, so referrer and target agree in all 35 cases and there is no
rename-left-behind anywhere. The generator line is a convention report, not
a defect list.

**This is a re-derivation** — `qou-uhzk` (completed 2026-09-03) established
it when `parseReference` was changed to stop refusing prefix-less refs
("deleted 35 real edges"). Recorded because a negative that has to be
re-derived each time the line is read is not yet a result.

**37 vs 35: the generator is right.** The two extra are `//` line comments
INSIDE a `uses:` array, not entries — a line-based extraction reads them as
elements, the module import does not.
`mba-sidecar-delta-lambda-closure.ts:24` ("algorithms are downstream of
math") and `p3-blowup-yekutieli.ts:10` ("NS blowup <=> obstruction level
n*"). Both arrays are well-formed and fully prefixed; both comments record
why a citation is or is not there, so deleting them would be audit-dodging.

**New measurement the prior bean does not carry.** `prose` needs no prefix,
but the corpus convention is near-uniform prefixing: of 324 prose blocks
**315 are prefixed** (`sec`/`prose`/`ssec`/`subsec`) and **9 are bare** —
and those 9 are the ONLY bare labels among all 3526 blocks in the paper.
8 are `appendix-transfer-matrices` bodies (its 5 intro prose blocks are
`sec:`-prefixed, so prose splits by role inside one directory), the 9th is
`braids-and-knots/fundamental-knots-operator-basis`. `tm-general-form` and
`tm-inductive-construction` have 0 inbound refs and contribute nothing to
the 35.

**Correction to `qou-uhzk`:** it says the 35 point at "seven `prose`/`example`
blocks". All seven are `prose`; none is an `example`. The kind is the field
that decides legitimacy, so exactness matters here.

**Shipped:** `content/pipeline/prefixless-ref-audit.ts` (print-only; per bare
ref reports target existence + kind, exits non-zero only on a missing target)
plus `prefixless-ref-audit.test.ts` (7 tests — the audit's dangling and
convention-break branches never fire on this corpus, the `qou-t0wm` trap).

**Open editorial call for the owner, NOT a defect.** Whether the 9 bare prose
labels should be normalised to `prose:`/`sec:`. Cost: rename 9 blocks + 35
referrers + 3526 regenerated `.jsonld`. Buys: a zero on a counter that is not
reporting a problem. Default (do nothing) is safe — the edges are correct.
My judgement: leave them.

**Verified** against folio-assistant `5618350` (fast-forwarded from `e7f5f55`
first): validate exit 0, 3 issues before AND after (identical, all
pre-existing); `gen-block-jsonld --check` unchanged, 0 dangling, 3526
siblings up to date; 7/7 tests pass.
