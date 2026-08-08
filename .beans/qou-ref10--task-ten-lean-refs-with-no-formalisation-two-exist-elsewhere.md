---
# qou-ref10
title: 'TASK: ten lean.refs with no formalisation — and two of them DO exist elsewhere'
status: todo
type: task
priority: medium
tags: [lean, lean-ref]
created_at: 2026-08-08T13:00:00Z
updated_at: 2026-08-08T13:00:00Z
---

Residue of the `lean.ref` drain (#4739). These blocks have **no sibling `.lean`
and no module at the mapped path**. A corpus-wide declaration grep run
2026-08-08 splits them:

## Exists elsewhere — repoint the ref, no formalisation needed (2)

| ref | actually declared in |
|---|---|
| `QOU.BraidsKnots.JSJ_volume_additivity` | `lean/QOU/BraidsKnots/LinearJSJVolume.lean` |
| `QOU.Archimedean.weierstrassProjection` | `lean/QOU/Archimedean/WeierstrassProjection.lean` |

Verify the declaration's namespace-qualified name against the file before
rewriting, and confirm the target carries the block's headline claim (not a
weaker lemma) — the rule from #4739 §2.

## Absent from the whole corpus (7)

`QOU.Eightfold.Sym2Gate`, `QOU.Eightfold.WeylInvarianceQDeformation`,
`QOU.Eightfold.RowCapObstruction`, `QOU.Eightfold.GellMannOkuboIdentity`,
`QOU.BraidKnot.chirality_frobenius_self_pairing`,
`QOU.BraidKnot.GBResidueSpectralSum.spectral_decomposition`,
`QOU.BraidsKnots.RamifiedDiscFusion`.

Four are `QOU.Eightfold.*` — check whether that chapter was ever formalised at
all before treating them as seven independent gaps.

Honest dispositions per §1a, per block: **formalise it**, **state it with
`sorry` + a `-- Ref:` citation** (the honest "stated, not yet proved" marker), or
**demote the block** if the claim is not one the corpus intends to prove. Do not
delete the ref to silence the checker.

## Related, do not conflate

Two further blocks have a resolvable ref pointing at a declaration **weaker than
the block claims** (#4739 §3): `recursive-atom-knot-atlas` (its only theorem is
`atomKnotAtlas.length ≥ 1`, a regression guard) and `q-momentum-properties` (one
of four stated properties formalised). Those need formalisation, not a repoint.
