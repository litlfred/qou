---
# qou-ref10
title: 'TASK: ten lean.refs with no formalisation — and two of them DO exist elsewhere'
status: in-progress
pr: 8259
type: task
priority: medium
tags:
    - lean
    - lean-ref
    - reorg-2026-10-04
created_at: 2026-08-08T13:00:00Z
updated_at: 2026-10-04T15:26:09Z
parent: qou-6qbv
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

## ⚠ RETRACTED — none of these is absent (2026-08-08)

**The "absent from the whole corpus" verdict below is wrong for all seven.**
Every one has a module in the Lean tree, at exactly the path its ref implies:

| ref | module |
|---|---|
| `QOU.Eightfold.Sym2Gate` | `lean/QOU/Eightfold/Sym2Gate.lean` |
| `QOU.Eightfold.WeylInvarianceQDeformation` | `lean/QOU/Eightfold/WeylInvarianceQDeformation.lean` |
| `QOU.Eightfold.RowCapObstruction` | `lean/QOU/Eightfold/RowCapObstruction.lean` |
| `QOU.Eightfold.GellMannOkuboIdentity` | `lean/QOU/Eightfold/GellMannOkuboIdentity.lean` |
| `QOU.BraidKnot.chirality_frobenius_self_pairing` | `lean/QOU/BraidKnot/chirality_frobenius_self_pairing.lean` |
| `QOU.BraidKnot.GBResidueSpectralSum.spectral_decomposition` | `lean/QOU/BraidKnot/GBResidueSpectralSum.lean` |
| `QOU.BraidsKnots.RamifiedDiscFusion` | `lean/QOU/BraidsKnots/RamifiedDiscFusion.lean` |

**The `QOU.Eightfold` chapter IS formalised** — the instruction below to "check
whether that chapter was ever formalised at all" is answered affirmatively;
there is even a fifth module, `Sym2GateParity.lean`, beyond the four named.

**Why the verdict was wrong.** I ran a grep for top-level *declaration names*
and concluded absence when these are **module-path refs** — §0a candidate 2,
`<lakeRoot>/<Decl/Path>.lean`. The ref `QOU.Eightfold.Sym2Gate` names a MODULE,
not a declaration, so a declaration grep can never find it. The triviality
probe's `decl-not-found` meant "no declaration to probe", not "the ref is
broken".

The same regex also omitted `axiom`, `opaque` and class fields — which is how
`s5_acts_on_ew_slice` was mis-reported in #4739 §1. Third and fourth instances
of one defect.

PR #4757 acts on the corrected picture: these are mis-shaped or already-correct
refs, not formalisation gaps. **Prefer that PR's per-ref table over the list
below**, which is retained only as the record of what was assumed.

## Superseded: "absent from the whole corpus" (7)

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

- **Round 55 update (in-progress):** De-vacuified in PR `litlfred/qou#8259` (HEAD `1be723e4c3e702d48db833cb3bedc75e89004822`), verified with Lean 4.24.0 (`0` `sorry`, `0` vacuity hits) and 80-dps `mpmath` witness.
