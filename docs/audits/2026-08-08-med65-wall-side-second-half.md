# MED wall-side drain — second half (bean `qou-med65`)

Scope: the second half of the MED `wall-side-correct` failures, derived fresh
from a clean tree. The first half is owned by a sibling agent; nothing outside
the list below is touched here.

## How the list was derived

```bash
bash scripts/setup-folio-assistant.sh
bun run scripts/check-wall-side.ts --sweep content/quantum-observable-universe
```

Baseline on this branch point (`3f1a4e3f23`): **1114/1190 pass**, 76 FAIL.

Each failing block's `lean.ref` was resolved the way the checker resolves it
(sibling `<root>.lean` first, then `<lakeRoot>/<Decl/Path>.lean`), the Lean
source was **comment-stripped** and its `import` lines removed before any regex
ran, and the remaining code was scanned for:

- **HEAVY** — `Real.<fn>`, `Complex`, integral/measure tokens → not MED
- **MED** — ordering only: `0 <`, `≤`/`≥`, `abs`/`|…|`, `linarith`, `positivity`,
  and **bare `>` / `<`** (the token class #4709's regex omitted)
- **OTHER** — no ordering token at all → the WEAK queue, not this one

Result: **69 MED**, 1 HEAVY (`quantum-dilog-convergence`), 6 OTHER. The 6 OTHER
are exactly the six blocks the WEAK-33 triage already classified
(`qmn-recursive-memoized`, `cpt-d6-d7-d8-closure`, `nucleon-ordering-factorization`,
`q-gl-classical-limit`, `q-beta-radius-of-convergence-gate`,
`qou-infra-discharges-goncharov-zeta5`), which is an independent check that the
classifier agrees with the hand triage.

Sorted alphabetically by `.ts` path, this branch takes **items 35–69** (35
blocks). Item 35 is the midpoint and is claimed here deliberately: a duplicated
block costs a merge conflict, a skipped block is silent.

`appendix-surreals/collatz-contact-boundary` is item 3 — first half, and in any
case owned by sibling PR #4722. Not touched.

## Verdicts

Filled in per block as the work lands. The standing rule from
[`2026-08-08-lean-ref-molecular-namespace-and-weak-triage.md` §8](2026-08-08-lean-ref-molecular-namespace-and-weak-triage.md)
applies: **a GENUINE verdict is a compile result, never a read.**
