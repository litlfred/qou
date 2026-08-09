---
# qou-w2d7
title: 'eigenbasis-structural-lemmas.qa.json: agent-judgement criteria (da-*, one-voice, q-usage, wall-side-correct) recorded needs-agent after the item-2 correction in PR #4826; supply verdicts'
status: completed
type: task
priority: normal
created_at: 2026-08-08T21:47:53Z
updated_at: 2026-08-09T00:11:43Z
---


## RESOLVED 2026-08-08 (PR #4834)

All 18 agent-judgement criteria now carry fresh verdicts against
`md=dff7d83acf96` / `ts=6bd2f97e8aa2`. `milnor-amalgamated-flow` had an
**empty** array (never reviewed at all) and is now covered too.

**Not a rubber stamp** — the review found three real defects, all fixed on
this PR rather than merely recorded:

1. **`da-reproducibility`** — the cited witness carried
   `contentBlock: "prop:eigenbasis-structural-lemmas"`, a label that does not
   exist (the block is `rem:`), and `scriptCommitSha: "unknown"`. The sibling
   probe from the same PR pointed at `obs:crossing-energy-decomposition`, and
   `obs:` is not a valid label prefix in this schema at all. Both producers
   fixed and re-run; witnesses regenerated with real commit SHAs.
2. **`da-lean-narrative-divergence`** — the title ended `"(Lean)"` but nothing
   formalises items 1–3; `CrossingEnergyBarParity` is about `E_cross`, not
   characters. Title corrected; formalisation tracked as `qou-lw3v`.
3. **`da-definitional-ambiguity`** — `c(λ)` carried the framing-pole claim
   while being defined nowhere in the corpus prose. Now defined as the content
   sum, tied to `QOU.MathlibExt.Partition.contentSum`.

Items 2 and 3 of the block were **re-derived independently** rather than taken
from the probe: the sign twist really is an algebra automorphism
(`(-s^{-1})^2 = h(-s^{-1}) + 1` follows from `s^{-1} = s - h`), and the signed
character form really does follow from the unsigned one plus item 1's parity.
The mathematics stands.

`da-referee-verdict`: **clean** (after the three fixes; `survivable-objection`
before them). `expo-milnor-clarity` moved warn → pass once the `c(λ)` gap and
the title were closed — the Milnor gate is strict 16/16.

Script criteria re-swept after the edits, so the whole sidecar is fresh.
