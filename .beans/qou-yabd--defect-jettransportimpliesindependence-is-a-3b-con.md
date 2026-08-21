---
# qou-yabd
title: 'DEFECT: JetTransportImpliesIndependence is a §3b-cond item-5 self-assuming projection — its field IS the conclusion and both class binders are decorative (concrete instance of the qou-24m2 class-instance blind spot)'
status: todo
type: bug
priority: normal
created_at: 2026-08-21T19:50:30Z
updated_at: 2026-08-21T19:51:00Z
---

Found while doing archaeology on `qou-j4mn` (PR #5402, branch
`claude/jet-algebraic-dependence-2026-08-21`). Full analysis §4 of
[`docs/audits/2026-08-21-jet-algebraic-dependence-convention-d.md`](../docs/audits/2026-08-21-jet-algebraic-dependence-convention-d.md).

## The declaration

`content/quantum-observable-universe/lean/QOU/Archimedean/JetOrderIndependence.lean`:

```lean
class JetTransportImpliesIndependence (E : TransportErrorData)
    [JetOrderIndependence] [SurrealParallelTransportBound E] : Prop where
  nonempty_independence : Nonempty HyperbolicVolumeIndependence

noncomputable def hyperbolicVolumeIndependence_of_reduction
    (E : TransportErrorData)
    [JetOrderIndependence] [SurrealParallelTransportBound E]
    [R : JetTransportImpliesIndependence E] :
    HyperbolicVolumeIndependence :=
  R.nonempty_independence.some
```

## The defect

AGENTS.md §3b-cond item 5: a class that "carries the block's own conclusion as a
field, with a 'theorem' that merely projects it" is a **vacuous self-assuming
projection** — it satisfies the propagation audit while failing
`proof-statement-integrity`.

That is exactly this shape. The class's single field **is** the downstream
conclusion, and the consumer is a bare `.some` projection that uses **neither**
`[JetOrderIndependence]` **nor** `[SurrealParallelTransportBound E]`. Both class
binders are decorative: deleting them changes nothing that is proved.

This is a concrete instance of the pattern `qou-24m2` flags as a **detector blind
spot** — the CLASS-INSTANCE variant of self-assuming, which the
`lean-self-assuming-audit.py` scanner misses because there is no
`theorem (h : P) : P := h` to match on. Related: `qou-q407`, `qou-5p7n`.

## Note on the reason — do not inherit `qou-j4mn`'s

`qou-j4mn`'s title says this class "cannot be a transfer of independence" *because*
the tr_M jets are algebraically dependent. **That argument does not go through**,
and the defect should not be filed under it. The class never mentions the tr_M
jets: its conclusion is about `vol_4_1, vol_5_2, vol_B3` (three real numbers), and
the `q -> 1` jet of `tr_M` is not an expansion of `Vol(K)` — the volume lives in
the root-of-unity asymptotics, as the original probe's own scope warning states.

The verdict "this is not a transfer of independence" is correct; the supporting
reason is the self-assuming shape above, not the jet dependence.

## Honest fix

Restructure so the class carries the genuine sub-hypotheses of the Nesterenko-type
transfer (the finite-jet-data → infinite-order step) and the consumer **derives**
`HyperbolicVolumeIndependence` from them, rather than projecting it out. If no such
decomposition is available yet, the honest disposition is to keep it as an openly
labelled conjecture and add the §3b disclosure sentence (`qou-5p7n`), **not** to
leave a projection that reads as a reduction.
