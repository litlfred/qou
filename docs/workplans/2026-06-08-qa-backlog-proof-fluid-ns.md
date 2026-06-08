# QA backlog proof drain — fluid-dynamics NS slice (2026-06-08)

One slice = one PR (proven pattern from PR #1984 braids proof-drain).

## Blocks (all `proof-statement-integrity` = fail/critical, `True := trivial` stubs)
- `ns-obstruction-computation` (prop)
- `ns-obstruction-tower` (prop, conditional on 5 classes incl. conj:regularity-breakdown)
- `ns-singularity-descartes` (thm)
- `leray-profile` (prop)
- `q-bkm-criterion` (thm)

## Fix pattern
Replace `True := trivial` placeholder with a `class …Context` carrying the
load-bearing md claim(s) as Prop fields, then a `theorem` asserting the claim
from the context (provable, sorry-free, no wrong-proposition axiom). §3b-cond
honoured where md is explicitly conditional on a `conj:`.

## Verify
`_Scratch` harness build against restored `lake-cache/qou-v4-24-0`; remove
`_Scratch` before commit. Re-rate via `qa-agent-write --score`.
