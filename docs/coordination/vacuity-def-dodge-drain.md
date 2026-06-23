# Coordination ledger — vacuity `def:True` dodge drain

**Goal.** Surface and drain `def X : True := trivial` audit-dodges
(AGENTS.md §1a STRICT, 2026-06-23): detect them, forbid the
workaround, and delete the ones that are pure **shadow-stubs**
(§0a — a co-located sibling `.lean` shadowing a substantive real
library decl).

## Campaign PRs

| Date | PR | Phase | Status | Cherry-pick / artifact |
|------|----|-------|--------|------------------------|
| 2026-06-23 | #2636 | detector + §1a policy + sidecar marking | merged | `lean-vacuity-axiom-audit.ts` `def-disguised-true` flag |
| 2026-06-23 | #2646 | widen detector to **any** `: True` body (not just `:= trivial`) | merged `508cbd706` | `detectTrivialTrue` widening |
| 2026-06-23 | #2648 | delete the **4 safe** shadow-stubs | open | this ledger |

## Sibling branch — `claude/drain-def-disguised-true-2026-06-23`

A sibling session pushed a drain branch (no PR, last touched
2026-06-23 ~12:40Z) deleting **13** `def:True` files across two
commits:

- `8a45eb63d` "delete 4 shadow-stub def:True files" — **SAFE** (taken
  up by #2648).
- `7e0bd77b7` "delete 9 more shadow-stub def:True files" —
  **DESTRUCTIVE / STALE** (see below).

### ⚠️ DO NOT MERGE the drain branch as-is

Commit `7e0bd77b7` was built from a stale merge-base. Its 9 target
files have since been **resolved in place** by another sibling and
now carry **53 substantive declarations** on current `main`
(13 theorems/lemmas + 17 defs + 23 structures/classes; **0** vacuous
`: True`). Deleting them is destructive. This is the same hazard that
closed #2642.

| File | thm/lem | def | struct/class | Σ substantive |
|------|:---:|:---:|:---:|:---:|
| `predicted-spectra/shell-structure-eigenvalues.lean` | 8 | 6 | 1 | 15 |
| `appendix-surreals/collatz-contact-boundary.lean` | 0 | 1 | 5 | 6 |
| `appendix-surreals/collatz-no-cycles.lean` | 0 | 1 | 5 | 6 |
| `fluid-dynamics/root-of-unity-truncation.lean` | 0 | 1 | 5 | 6 |
| `fluid-dynamics/vorticity-lower-bound.lean` | 0 | 1 | 5 | 6 |
| `mass-endomorphism/hecke-baer-star-generic.lean` | 2 | 2 | 1 | 5 |
| `mass-theory/confinement-categorical.lean` | 1 | 2 | 1 | 4 |
| `mass-theory/eigenvalue-product-expansion.lean` | 2 | 2 | 0 | 4 |
| `particle-interactions/unstable-atom-decay-channel.lean` | 0 | 1 | 0 | 1 |
| **total** | **13** | **17** | **23** | **53** |

The drain branch's safe content is fully captured by #2648; its
remaining 9 deletions are obsolete. **Recommendation: close the drain
branch unmerged** (per AGENTS.md §9, do not delete it — leave the
branch as historical record).

## The 4 safe shadow-stubs (#2648)

Each is a pure `def *_stub : True := trivial` whose block `lean.ref`
points to a verified-present real library decl; deleting the sibling
stub lets the ref resolve to the real decl:

| Deleted stub (mass-theory/) | Resolves to |
|---|---|
| `q-reeb-flow-on-coral-coords.lean` | `qou:QOU.CategoricalReeb.QReebFlowOnCoralCoords` |
| `ramified-disc-fusion.lean` | `qou:QOU.BraidsKnots.RamifiedDiscFusion` |
| `reeb-bundle-complement-equals-volume.lean` | `qou:QOU.BraidsKnots.ReebBundleComplementEqualsVolume` |
| `six-canonical-knot-operators.lean` | `qou:QOU.CategoricalReeb.boundary_perm_realises_S3` |

The 4 `.qa.json` sidecars record `proof-no-trivial-true=fail`
(six-canonical also `statement-integrity` / `narrative-lean-equiv` /
`false-premise`); all resolved by deletion, refreshed on the next
qa-sweep (sidecars never hand-edited).

## Lesson

Drain/deletion branches must **re-validate against current `main`**
before merge — a stale merge-base turns "delete shadow-stubs" into
"delete real content." The vacuity audit flags a `: True` body; it
does **not** by itself prove the file is a shadow-stub. The §0a
shadow-stub test (does `lean.ref` resolve to a substantive decl
elsewhere?) plus a current-main substance count are both required.
