> **DEPRECATED on 2026-05-24.** Workplan executed / point-in-time status snapshot / PR-specific note that has been superseded by subsequent integration into main. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T1 for the deprecation rationale.

# Cone-reduction sweep — status after body-asymptotics fix

## Headline

The body-asymptotics-catalog fix
([2026-05-02-cone-reduction-fluid-bridge.md](2026-05-02-cone-reduction-fluid-bridge.md))
cleared the fluid-conjecture leak from 230 → 13 provable blocks.

**Searching for more catalog-style leaks: none found.** The
remaining 233 violators each touch their conjectures via
**structural derivation chains**, not catalog references.

## The remaining cone — direct bridges

After fluid leak removal, the top 9 conjectures (touched by
~221–224 provable blocks each) are reached directly from these
provable blocks:

| Conjecture | Direct provable users |
|------------|----------------------|
| `conj:baryon-period-ratio` | reached only via `conj:hyperbolic-volume-transcendence` |
| `conj:borromean-quark` | `def:up-quark` (definition, exempt) |
| `conj:classical-limit-stpart` | `prop:feynman-classical-limit` |
| `conj:hyperbolic-volume-transcendence` | `prop:geom-yekutieli-alignment` |
| `conj:knot-factor-frobenius-pairing` | `prop:knot-factor-spectral-form`, `thm:knot-mass-formula-unified` |
| `conj:palindromicity-orbital-type` | only via `conj:q-integer-mass-formula` |
| `conj:q-integer-mass-formula` | `prop:wigner-coefficient-derivation`, `prop:six-term-mass-formula-complete` |
| `conj:shell-closure-nf-term-count` | `prop:magic-numbers-from-q` |
| `conj:shell-correction-term-seven` | `prop:derived-mass-formula-light-isotopes`, `prop:plancherel-term-7-formulation` |

These ~9 provable blocks are the **structural bridges**.
They legitimately derive content from open conjectures (their
proofs use the conjectural results). Per AGENTS.md §3b, each
must be `conjecture` (or remarks with `interprets:`), not
`proposition`/`theorem`.

## Why this isn't a catalog-style fix

The body-asymptotics-catalog edge was special:
`rem:body-asymptotics-catalog` listed
`prop:ns-obstruction-computation` as a **catalog entry** —
documenting that NS singularity bounds exist, not depending
on them logically. Dropping that single edge cut the chain.

The remaining bridges are different. For example,
`prop:feynman-classical-limit` actually uses
`conj:classical-limit-stpart` in its proof body
(the classical limit is conditional on the conjecture). You
can't drop the `uses[]` entry without breaking the proof.

## What's left — §3b policy territory

The 233 remaining violators split into:

- **9 structural bridges** (above) — provable blocks whose proofs
  genuinely cite open conjectures. Per §3b STRICT, they must
  be demoted to `conjecture`.
- **~224 transitively-downstream blocks** — they `uses[]` the
  bridge blocks (or reach them via 2-3 hops). Per §3b STRICT,
  they too must be demoted.

The cone reduction can't cut these structurally — it can only
inform the §3b policy decision: Option A (demote all 260),
Option B (substrate-axiom classification: keep provable kind
but axiomatize the conjecture upstream), Option C (split
provable-vs-conditional reading per block).

This is the P3.1 audit memo's open question
([2026-05-01-p3-1-conjectural-propagation-audit.md](2026-05-01-p3-1-conjectural-propagation-audit.md)).

## Lookout for future catalog-style edges

When new content lands on main, audit edges of the form:

- A `remark` listing many `uses[]` entries (catalog pattern).
- A `prose` block with `uses[]` (prose shouldn't have logical
  dependencies).
- A `definition` with conjectural backing in `uses[]` (prefer
  narrative note).

Run `bun run content/pipeline/conjectural-propagation-audit.ts`
periodically; spot-check any conjecture whose direct-user count
is 0 but transitive-user count is high (indicates a remark/prose
bridge rather than a structural one).

## Status

**Catalog-style cone leaks: cleared.** The framework's remaining
conjectural-cone size is structurally minimal given the open
conjectures present. Further reduction requires either:

1. Proving one of the 9 bridge conjectures (closes its cone
   entirely), or
2. The §3b policy decision (P3.1) to demote-or-axiomatize.
