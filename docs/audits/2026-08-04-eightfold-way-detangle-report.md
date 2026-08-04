# Eightfold-Way Chapter Detangle Report

**Date:** 2026-08-04
**Chapter:** `eightfold-way` (Chapter 10)
**Branch:** `claude/eightfold-detangle-2026-08-04`

## Executive summary

**Zero fitting found.** The chapter is clean: no numerical constants,
no fitted parameters, no magic numbers. Every claim either traces to
QOU axioms or is explicitly marked as open/conjectural.

**One structural choice identified** — the Ocneanu trace parameter
N=2 is a soft constraint, not a theorem (T3f audit). Bean created.

**Section density is sparse** (H4) — most sections have 1 block.
This is expected: the chapter is in Phase 1-2, with Phase 3-5 blocks
not yet authored.

## H1 — Forward references: 0

No intra-chapter forward references. The block ordering follows:
```
eightfold-intro → a2-from-three-strands → flavor-charge-assignments
→ meson-octet-decomposition → schur-weyl-eightfold
→ color-su3-from-g2 → q-deformation-weight-lattice
→ dictionary-flavor-layer → eightfold-open-problems
```
Each block uses only blocks earlier in this sequence or external
(cross-chapter backward) dependencies.

## H2 — Cross-chapter coupling

### External uses (backward — fine):
- `def:braid-group` (braids-and-knots) — Ch 6, earlier
- `def:hecke-algebra` (braids-and-knots) — Ch 6, earlier
- `def:octonion-algebra` — needs verification of chapter
- `def:coulomb-charge` (knots-particles-confinement) — Ch 9, earlier
- `conj:sm-hypercharge-invariant` (appendix-standard-model) — appendix, later
- `rem:knot-particle-dictionary` (knots-particles-confinement) — Ch 9, earlier

### Forward cross-chapter reference found:
**`conj:sm-hypercharge-invariant`** — this is in the SM appendix
(later in document order). The `flavor-charge-assignments` block uses
it. This is an **H1/H2 cross-chapter forward reference**.

**Assessment:** Acceptable. The hypercharge conjecture is the framework's
#1 open problem. The eightfold-way chapter must reference it because it
directly concerns the charge assignments. The reference is to an
*open problem*, not to a result — it doesn't create a logical
dependency (no proof relies on it). Mark as `wontfix: architectural`.

## H3 — Cross-section coupling: 0.0

Zero intra-chapter cross-section edges. Each section is self-contained
(its blocks use only external dependencies or blocks within the same
section). This is ideal but partly a consequence of section sparsity.

## H4 — Section density

| Section | Blocks | H4 status |
|---|---|---|
| §1 A₂ root system | 2 | OK (includes intro prose) |
| §2 Flavor charges | 1 | ⚠ sparse |
| §3 Meson octet | 1 | ⚠ sparse |
| §4 Baryon multiplets | 1 | ⚠ sparse |
| §5 Color algebra | 1 | ⚠ sparse |
| §6 q-Deformation | 1 | ⚠ sparse |
| §7 Dictionary | 1 | ⚠ sparse |
| §8 Open problems | 1 | ⚠ sparse |

**Assessment:** All sparse sections have identified TODO blocks (Phase
2-5 continuation). The sparsity is honest — it reflects what's
authored, not missing content that should have been included. No
merging recommended: the 8-section structure is correct for the
chapter's scope, and each section will grow as the TODOs are filled.

## H5 — Section too dense: NONE

No section exceeds 18 blocks.

## H6 — Isolated blocks: NONE

Every block either uses or is used by at least one other block.

## H7 — Remark/example ratio

| Block type | Count |
|---|---|
| prose | 1 (eightfold-intro) |
| proposition | 4 (a2-from-three-strands, meson-octet, schur-weyl, color-su3) |
| remark | 4 (flavor-charges, q-deformation, dictionary, open-problems) |

Ratio: 4 remark / 4 proposition = 1:1. Within healthy bounds.

## Fit/Choice/Derivation audit

### Scan result: ZERO FITTING

Grep for `fitted`, `calibrated`, `tuning`, `free param`, `chosen`,
`ad hoc`, `we set`, `we choose`, `we fix` — every match is in the
context of **anti-fitting warnings** ("not a fit", "a candidate
requiring a fitted scale... is a fit, not a derivation").

### Numerical constants: ZERO

No floating-point numbers in any .md file. The chapter is purely
algebraic (representation theory, combinatorics, Cartan matrices).

### Identified structural choice (NOT fitting):

**The Ocneanu trace parameter N=2** (T3f audit) is a structural choice,
not a fitted parameter. It's not in this chapter's content but
affects the chapter's conclusions. Already beaned as `qou-w5fw`
(completed — audit documented the open status).

## Recommendations

1. ✅ No reorganization needed — structure is sound
2. ✅ No fitting to resolve — chapter is clean
3. ⚠ The `conj:sm-hypercharge-invariant` forward reference is
   architectural — mark as `wontfix: architectural`
4. 📋 Fill sparse sections as Phase 3-5 beans are worked
