---
# qou-klr1
title: 'GAP: three fluid-dynamics propositions are formalised twice and the LIBRARY copy is the vacuous one (§0a inverted)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T07:59:14Z
updated_at: 2026-11-16T20:00:34Z
parent: qou-6qbv
---

Found while adjudicating the 13 of `qou-vh1o` (2026-09-13/14). **Author call,
not an agent call** — deliberately not acted on.

## The finding

Three propositions each have a content-block **sibling** `.lean` *and* a
**library** module under `lean/QOU/FluidDynamics/`:

| proposition | sibling (block resolves here) | library twin |
|---|---|---|
| acoustic horizon conditions | `fluid-dynamics/acoustic-horizon-conditions.lean` | `lean/QOU/FluidDynamics/acoustic_horizon_conditions.lean:43` |
| discrete vortex spectrum | `fluid-dynamics/discrete-vortex-spectrum.lean` | `lean/QOU/FluidDynamics/discrete_vortex_spectrum.lean:70` |
| root-of-unity truncation | `fluid-dynamics/root-of-unity-truncation.lean` | `lean/QOU/FluidDynamics/root_of_unity_truncation.lean:69` |

Per AGENTS.md §0a a `lean.ref` resolves **sibling first**, and in all three the
sibling is the BETTER formalisation — `acoustic_horizon_criterion_iff` is
genuinely proved
(`rw [ctx.mach_def, div_eq_one_iff_eq (ne_of_gt ctx.cs_pos)]`) and
`acoustic_horizon_hawking_temperature` closes by `field_simp` — while each
library twin is the **antecedent-asserting-context** shape: a free `Prop` field,
a field asserting it, `impl_* : P → conclusion`, and a theorem doing modus
ponens on the class's own two fields. All three library twins are now ledgered
**`genuine`** (`docs/audits/lean-vacuity-review-ledger.json`, disposition
`restate-to-derive-or-demote`).

## Why this is the INVERSE of §0a's stated hazard, and of `qou-enyo`

§0a's "no shadowing stubs" rule, and `qou-enyo`'s residual-shadow-stub drain,
both assume the **sibling** is the stub and the **library** decl is real. Here
it runs the other way: the sibling carries the real proof and the library twin
is the vacuous one. A sweep written against the documented direction would
delete exactly the wrong file of each pair.

## Measured containment — this is NOT urgent

- the library modules ARE inside the Lake glob (`globs = ["QOU", "QOU.+"]`,
  `srcDir = "."` at `lean/`), so they **do** compile under `lake build QOU`;
- the siblings are outside `lean/` and not in the library, so there is **no name
  collision** even though `acoustic_horizon_conditions` and
  `discrete_vortex_spectrum` exist under the same name in both trees;
- **importers of the three library modules: 0.**

So nothing consumes the bad copy today. The hazard is prospective: a future
library file that `import QOU.FluidDynamics.acoustic_horizon_conditions` gets
the shape-(A) version, not the proved one.

## The decision (author's)

1. **Delete the library twins** — cheapest, zero importers, and the blocks
   already resolve to the siblings. Risks nothing measured; forecloses having a
   library-tier version of these three.
2. **Promote the siblings into the library** (replace each twin with the
   sibling's content, keep the sibling per §0a's definition-block rule) — more
   work, and makes the proved form importable.
3. **Do nothing** — the default. The twins stay, ledgered `genuine`, counted as
   3 of the 76 defects; the audit keeps reporting them and no consumer is
   affected.

**Agent recommendation (judgement, not a finding):** option 1. Zero importers
plus a strictly-better sibling makes deletion the honest cleanup, and option 2's
extra work buys an importable copy nobody has asked for. But deleting Lean that
compiles is the owner's call, and option 3 is safe.

## Round 49 Progress (`litlfred/qou#8180`, `75360a145951a3e9bdb50b79e4a7ca2a9c94a813`)

- Replaced the three decoy-hypothesis library twins in `folio/quantum-observable-universe/lean/QOU/FluidDynamics/` (`acoustic_horizon_conditions.lean`, `discrete_vortex_spectrum.lean`, `root_of_unity_truncation.lean`) with the non-decoy context classes from their `fluid-dynamics/` chapter siblings plus proved consumer theorems (`acoustic_horizon_criterion_iff`, `acoustic_horizon_conditions`, `acoustic_horizon_hawking_temperature`, `discrete_vortex_transition_energy`, `discrete_vortex_ladder_rule`, `discrete_vortex_classical_energy`, `root_of_unity_truncation_core_at_one`).
- Verified `lean-decoy-hypothesis-audit.py` reports `0` hits on all three files and `lean -DautoImplicit=false -s 65536` exits `0` with `0` warnings.
