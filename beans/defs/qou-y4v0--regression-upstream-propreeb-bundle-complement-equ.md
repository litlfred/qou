---
# qou-y4v0
title: 'REGRESSION (upstream): prop:reeb-bundle-complement-equals-volume dropped out of the §3b-cond item-2 satisfied bucket'
status: completed
type: task
priority: normal
created_at: 2026-09-04T11:02:10Z
updated_at: 2026-09-04T13:37:49Z
---

Measured 2026-09-04 on `claude/q-riemann-hypothesis-gaps-zgxd8m` after merging
`origin/main` `d0d473550a` (21 commits since `7297f2f6d5`).

## What moved

`scripts/conditional-on-class-hypothesis-audit.ts` measures AGENTS.md §3b-cond
item 2 — does a block reported `conditional_on_class` actually bind a class
from its own conjectural cone as a Lean `[Instance]` hypothesis. Its committed
witness (`docs/audits/2026-09-03-conditional-on-class-hypothesis.witness.json`,
generated before the merge) records:

    binds_cone_class 9 | binds_other_carrier 72 | binds_no_carrier 45

Re-run on the post-merge tree with this branch's own changes stashed out:

    binds_cone_class 8 | binds_other_carrier 69 | binds_no_carrier 49

The one that left `binds_cone_class` is **`prop:reeb-bundle-complement-equals-volume`**
(`content/quantum-observable-universe/mass-theory/reeb-bundle-complement-equals-volume.ts`,
`lean.ref` = `qou:QOU.BraidsKnots.ReebBundleComplementEqualsVolume`). It is now
in `binds_no_carrier` — the bucket for blocks whose Lean binds no class at all.

## Why it is upstream, and what is NOT established

`git log 7297f2f6d5..d0d473550a` touches **neither** the block's `.ts` nor its
`.lean`. So the block did not change; what changed is the set of class names in
its conjectural cone, i.e. one of the *carriers* upstream. Two upstream commits
are the obvious candidates — `f4587317d7` ("12 `axiom`s declared SYMBOLS, not
claims: convert to `opaque`") and `63df086c63` ("close two more axioms by
construction") — but **that is a hypothesis, not a measurement**: this bean did
not identify which carrier changed or how.

**`binds_no_carrier` is a candidate set, not a violation count** — the audit's
own header says so, and this PR hand-checked two members that are correctly
unconditional. So do not read this as "a block regressed to unsound". Three
readings are consistent with the move and it does not separate them:

1. the carrier the block used to bind was removed or renamed, and the block now
   silently states something conditional with no hypothesis (a real defect);
2. the carrier became derivable and the block is now legitimately
   unconditional (an improvement, mis-read by the detector);
3. the carrier is still there but under a name the cone no longer collects
   (a detector-blindness instance, the fourteenth-plus of its family).

## Next honest step

Diff `QOU/BraidsKnots/ReebBundleComplementEqualsVolume` and its cone's carriers
across `7297f2f6d5..d0d473550a`, and read the block's Lean signature. One
`git log -p` on the carrier files settles which of the three it is. Do NOT
"fix" the block until that is known — under reading 2 there is nothing to fix,
and under reading 3 the fix belongs in the audit script.

Not fixed here because it is not this branch's change and the diagnosis is
cheap but not free.


---

## RESOLVED 2026-09-04 — NOT a regression. Reading 1 is excluded; it is readings 2 and 3 together.

**This bean's own title is wrong.** `prop:reeb-bundle-complement-equals-volume`
did not regress. The detector correctly stopped counting a **false positive**,
and the block's former "item 2 satisfied" status was resting on a class that
should never have existed.

## Mechanism, established

The block's `lean.ref` is `qou:QOU.BraidsKnots.ReebBundleComplementEqualsVolume`,
resolving to `content/quantum-observable-universe/lean/QOU/BraidsKnots/ReebBundleComplementEqualsVolume.lean`.

At `6f8d8510de` — the commit that generated the committed witness — that file
declared **`class MassVolumeFactorization`**. It now declares only `def`s and
theorems. The conversion is commit **`be967ae9f9`**, whose own message says it:

> This file declared `QOU.BraidsKnots.MassVolumeFactorization` with three
> fields — `markov_trace : ℝ`, `jsj_volume_sum : ℝ`, and
> `factorization_identity : markov_trace = jsj_volume_sum` … It **cited
> AGENTS.md §3b-cond** for the pattern while being the case §3b-cond **item 5**
> forbids: both reals are chosen by the instance, so the "conditional theorem"
> derives [its own conclusion].

So the class the block was binding was a **self-assuming projection**. Removing
it is right, and the block dropping out of `binds_cone_class` is the correct
consequence. Nothing about the block needs fixing.

## The finding worth keeping: the item-2 audit is BLIND TO ITEM 5

`scripts/conditional-on-class-hypothesis-audit.ts` measures §3b-cond **item 2**
— does the block bind a class from its own conjectural cone. It says nothing
about **item 5**, which forbids that class from carrying the block's own
conclusion. A block can therefore sit in `binds_cone_class` — the bucket that
reads as "item 2 not refuted" — while being an item-5 violation, and at least
one of the original 9 demonstrably was.

**So `binds_cone_class` is an upper bound too**, in the same way the script's
header already says `binds_no_carrier` is. Both ends of the split over-count in
their own direction. Worth folding an item-5 check in; not done here.

## Corrections to what this bean originally said

- **"REGRESSION (upstream)"** — no. A correct upstream fix.
- **"a carrier in its cone changed [in the 21 commits `7297f2f6d5..d0d473550a`]"**
  — the carrier did change, but **not in that window**. `be967ae9f9` is dated
  2026-09-03 and is an ancestor of *both* ends; it reached this branch through
  an earlier merge. The window framing was inferred from when I happened to
  re-measure, not established. Checking `git merge-base --is-ancestor` against
  both ends of the window is what settles this, and it is two commands.
- **Reading 1 ("the block now silently states something conditional with no
  hypothesis — a real defect")** is excluded.

## Not diagnosed

The other three moves in the same re-measurement (`binds_other_carrier`
72 → 69, i.e. three blocks going to `binds_no_carrier`) were **not**
investigated. Do not assume the same cause; `MassVolumeFactorization` still
exists as a class in `mass-theory/mass-volume-factorization.lean`, so the name
has not left the corpus.
