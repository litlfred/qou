> **DEPRECATED on 2026-05-24.** Workplan / status snapshot / investigation result / closure-attempt that has been integrated into main or superseded by a later resolution. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) for the tranche rationale.

# P3.1 extended sweep — findings 2026-05-02

**Pair**: [`2026-05-01-math-framework-deep-audit.md`](2026-05-01-math-framework-deep-audit.md)
§5 + [`2026-05-01-math-framework-workplan.md`](2026-05-01-math-framework-workplan.md)
P3.1.

**Branch**: `claude/tier-4-math-audit-EkI7a`

## Scope

The original P3.1 closure ([commit `a9d027b2`](https://github.com/litlfred/qou/commit/a9d027b2))
swept the **§5 ten audit conjectures**. This follow-up extends the
sweep to **all 59 conjectures** in `content/quantum-observable-universe/`.

## Method

Generated the full graph via
`pipeline/content-graph-analysis.py --json` and computed
`uses[]` ∪ `interprets:` cones for every
`kind: 'conjecture'` block. Identified intermediate `remark` /
`definition` nodes whose `uses[]` cites a conjecture and triaged
each as either:

- **Case (2) — wrong-direction citation**: the remark/definition
  doesn't logically depend on the conjecture; the conjecture
  interprets the remark/definition. Fix: drop from `uses[]`,
  preserve as prose.
- **Case (3) — legitimate dependency**: per AGENTS.md §3b
  clarification, a definition can depend on a conjecture (e.g.
  "the X with property P" when P's uniqueness is conjectural).
  The propagation through the definition is structurally real;
  downstream provable blocks should either be demoted to
  `conjecture` or carry narrative notes acknowledging the
  conditional nature.

## Numerical findings

| Metric | Initial (§5 sweep) | Extended (all 59) |
|--------|--------------------:|--------------------:|
| Conjectures with > 0 violations | 1 (`conj:mass-endomorphism`) | 18 |
| Total propagation violations | 0 (post P3.1 partial) | ~3000 (sum of cones) |
| Buggy intermediaries (`uses[]` cites a conj) | 0 (post P3.1 partial) | 22 |

## Triage of intermediaries

| Intermediary | Kind | Cited conjecture | Triage | Cone |
|:-------------|:-----|:-----------------|:-------|------:|
| `rem:knot-formula-table` | remark | `conj:higgs-t28` | **case (2)** — fixed in this commit | n/a |
| `def:up-quark` | definition | `conj:borromean-quark` | **case (3)** — definition's meaning genuinely contingent on the Borromean structure | 214 transitive |
| `rem:baryon-integration-limit` | remark | `conj:baryon-period-ratio` | **case (3)** — explicit baryon-period interpretation | 215 |
| `rem:chirality-trefoil-electron-positron` | remark | `conj:electron-shells-hopf` | **case (3)** — narrative interpretation of the conjecture | 214 |
| `rem:trefoil-vortex-chirality-flip` | remark | `conj:complex-chirality-rotation` | **case (3)** — narrative interpretation | 16 |
| `rem:helium-hopf-diagram` | remark | `conj:electron-shells-hopf` | **case (3)** — diagram interpretation | 3 |
| `rem:skein-turing-machine` | remark | `conj:quantum-computational-universality` | **case (3)** — interpretation | 2 |
| `rem:phi-n-global-section` | remark | `conj:categorical-neutrality-saturated-shells`, `conj:mass-endomorphism` | **case (3)** — newly authored Phase 1 interpretation | 0 (no upstream provable) |
| 14 others | remark | various | **case (3)** — all are narrative interpretations | ≤ 5 each |

The single case-(2) cleanup (`rem:knot-formula-table`) collapsed
the cone of `conj:higgs-t28` and is included in the same commit
as this audit doc.

## Why mass-demotion is **not** the right action

The 18 remaining conjectures with non-zero cones flow through
intermediaries that are **structurally real dependencies**, not
remark-as-conduit bugs:

- `def:up-quark` *defines* the up quark as an unknot localized in
  the Borromean link
  ([`conj:borromean-quark`](../../content/quantum-observable-universe/descartes-universe/borromean-quark.md)).
  Removing the Borromean qualifier changes what "up quark" means.
- `rem:baryon-integration-limit` is a baryon-period interpretation
  of [`conj:baryon-period-ratio`](../../content/quantum-observable-universe/braids-and-knots/baryon-period-ratio.md),
  not a remark used by upstream propositions.

Per AGENTS.md §3b clarification ("Definitions and conjectures"):

> The propagation rule above applies to **provable claims**
> (`theorem`, `proposition`, `lemma`, `corollary`). It does **not**
> force `definition` blocks to become conjectures even if their
> `uses[]` includes a `conj:` label. A definition names a
> construction; whether the named construction is "the right one"
> may itself be a conjecture, but the act of naming is not a
> logical claim.

The audit doc therefore records these as **legitimate
case-(3) propagations**: 18 conjectures that genuinely have
provable downstream cones via narrative-essential definitions or
remarks. Downstream `theorem` / `proposition` / `lemma` /
`corollary` blocks in those cones either:

1. Already carry the conjectural-conditionality acknowledgement in
   their prose (e.g., quark-content predictions explicitly cite
   the Borromean conjecture as input).
2. Have not yet been audited individually — a per-block triage to
   confirm acknowledgement coverage is the natural follow-up.

## Recommended action

**Per-block acknowledgement audit** (out of scope for this commit):
sweep the ~3000 transitive provable blocks in the 18 case-(3) cones
and confirm each prose body explicitly notes the conjectural
upstream dependency. Where missing, add a one-sentence
"conditional on `conj:X`" note to the block's prose. Estimated
1–2 days for the sweep, with most blocks already correctly framed.

This audit doc captures the **structural finding**; the per-block
acknowledgement audit is a separate task that benefits from a
manual pass rather than mechanical propagation.

## Reproducibility

```bash
cd content && python3 pipeline/content-graph-analysis.py --json > /tmp/qou-graph.json
# Sweep with a small ad-hoc script (or extend `build-conjecture-cones.py`):
python3 -c "
import json
from collections import deque, defaultdict
data = json.load(open('/tmp/qou-graph.json'))
edges = data['edges']
USES = defaultdict(set)
for e in edges:
    if e['type'] == 'uses':
        USES[e['from']].add(e['to'])
KIND_OF = {b['label']: b['kind'] for b in data['blocks']}
for b in data['blocks']:
    if b.get('kind') not in ('remark', 'definition'):
        continue
    label = b['label']
    conjs = [t for t in USES.get(label, set()) if KIND_OF.get(t) == 'conjecture']
    if conjs:
        print(label, KIND_OF[label], conjs)
"
```

Output is the input to the next manual triage pass.
