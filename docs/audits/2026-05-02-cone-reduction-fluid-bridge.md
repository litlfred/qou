# Cone reduction: fluid-conjecture bridge via body-asymptotics-catalog

**Pair:** [`conjectural-propagation-audit.ts`](../../content/pipeline/conjectural-propagation-audit.ts)
+ witness [`2026-05-01-p3-1-conjectural-propagation.witness.json`](2026-05-01-p3-1-conjectural-propagation.witness.json).

The §3b conjectural-propagation audit reported 230/233 provable
blocks transitively touching the **fluid-dynamics conjectures**
(`conj:critical-exponent`, `conj:blowup-yekutieli`,
`conj:regularity-breakdown`, `conj:q-aubin-lions`,
`conj:ns-counterexample`). This memo identifies the single bridge
that caused the leak and lands the surgical fix.

## The bridge

Shortest path from `prop:per-braid-mass-tower` to a fluid
conjecture (10 hops):

```
prop:per-braid-mass-tower
  → prop:mass-endomorphism-tower            (provable, OK)
    → rem:kashaev-volume-density            (remark, OK)
      → rem:body-asymptotics-catalog        (remark, OK to interpret)
        → prop:ns-obstruction-computation   (provable! ← LEAK)
          → prop:ns-obstruction-tower
            → prop:core-levi-form
              → prop:vorticity-lower-bound
                → conj:q-aubin-lions
```

The leak is at step 4 → 5: `rem:body-asymptotics-catalog`
(a *catalog* of analytic bounds in surreal big-O form) listed
`prop:ns-obstruction-computation` as a `uses[]` entry. Per
AGENTS.md §3a, a catalog remark **may freely list interpretive
references**, but the §3b propagation audit treats every
`uses[]` edge as a structural dependency — making this catalog
entry a load-bearing path.

The NS-obstruction-computation entry is genuinely catalog-only:
it documents that NS singularity obstructions are *one of the
analytic bounds present in the body of the paper*, alongside
Hecke convergence, Hoefsmit scattering, jet-tower convergence,
etc. It does not contribute logical content to either the
catalog or to upstream callers (`rem:kashaev-volume-density`,
`prop:mass-endomorphism-tower`, `prop:per-braid-mass-tower`).

## Fix

Drop `prop:ns-obstruction-computation` from
`rem:body-asymptotics-catalog`'s `uses[]`. The other six entries
(Hecke convergence, Hoefsmit, jet-tower convergence, unified
iterative correction, Feynman classical limit, Möbius energy
proof) are kept — they are non-conjectural-cone catalog entries.

## Impact

| Conjecture | Before (provable blocks touching) | After |
|------------|----------------------------------:|------:|
| `conj:critical-exponent` | 230 | **13** |
| `conj:blowup-yekutieli` | 230 | 13 |
| `conj:regularity-breakdown` | 230 | 13 |
| `conj:q-aubin-lions` | 229 | 13 |
| `conj:ns-counterexample` | 229 | 13 |

For `prop:per-braid-mass-tower` specifically: cone of conjectures
shrinks from **20 → 14** (the 5 fluid conjectures + `levi-
degeneracy` removed).

The 13 remaining provable blocks that still touch fluid conjectures
all live in the fluid-dynamics chapter or its direct
neighbourhood (`prop:universality`, `prop:vorticity-lower-bound`,
NS obstruction tower, etc.). Their fluid dependence is structural
and correct — they really do depend on the NS conjectures.

## What the remaining cone looks like (per-braid-mass-tower)

After the fix, `prop:per-braid-mass-tower` transitively touches:

- Knot-theory conjectures: `conj:borromean-quark`,
  `conj:knot-factor-frobenius-pairing`,
  `conj:hyperbolic-volume-transcendence`,
  `conj:kashaev-volume-conjecture`,
  `conj:archimedean-remainder-exponential-decay`,
  `conj:dilogarithm-archimedean-limit`,
  `conj:shared-denominator-cusp-holonomy`,
  `conj:algebraic-geometric-dilog-equivalence`
- Mass-formula conjectures: `conj:q-integer-mass-formula`,
  `conj:palindromicity-orbital-type`,
  `conj:shell-closure-nf-term-count`,
  `conj:classical-limit-stpart`,
  `conj:shell-correction-term-seven`
- One observation: `conj:baryon-period-ratio`

These are all legitimate — the per-braid mass tower really does
depend on the knot-theory and mass-formula conjectures via its
derivation chain. None of them is a chain leak.

## Recommendation

The fluid-dynamics conjectures should be **structurally
quarantined** — only blocks within `fluid-dynamics/` or its
direct neighbourhood should depend on them. Any cross-chapter
`uses[]` edge into the fluid cone deserves scrutiny: is it
catalog-style (move to `cites[]` or drop) or genuinely
load-bearing (then the upstream block must be a `conjecture`
itself per §3b)?

This memo lands one such surgical fix; a fuller audit could
sweep all cross-chapter edges to enforce the quarantine.

## Status

Bridge identified, fix landed, cone reduction verified at the
audit level. The 217 provable blocks no longer falsely depend on
fluid-dynamics conjectures. `prop:per-braid-mass-tower`'s cone
shrinks from 20 → 14 conjectures (all of which are legitimate
upstream dependencies).
