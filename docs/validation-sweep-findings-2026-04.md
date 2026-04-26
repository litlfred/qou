# Validation sweep findings — Track 5 of post-#430 follow-ups

**Date:** 2026-04-26
**Branch:** `claude/post-pr430-followups` (PR #436)
**Scope:** survey of `bun run validate quantum-observable-universe` output
on `origin/main` HEAD, with mechanical fixes applied.

## Headline numbers

| Stage | Hard errors (`✗`) | "no Lean declaration" warnings | "undefined cross-reference" warnings | Total issues |
|---|---:|---:|---:|---:|
| Pre-sweep (post-#430 main) | 26 | 65 | 114 | 203 |
| After Track 5 sweep | 14 | 65 | 110 | 188 |

15 issues resolved by purely mechanical fixes; 188 remain and require
substantive content/Lean work.

## What Track 5 fixed (15 issues)

### Label-prefix renames (12 issues)

The `uses[]` array on a referring block names the dependency by full
label including its kind prefix (`prop:`, `def:`, `rem:`, etc.).
Several blocks named the wrong prefix for an existing label.  Five
mechanical renames applied via `find content/ -name "*.ts" -exec sed`:

| Wrong reference | Correct reference | Block kind change |
|---|---|---|
| `prop:knot-factor-frobenius-pairing` | `conj:knot-factor-frobenius-pairing` | proposition → conjecture |
| `prop:fibre-functor-rigidity` | `rem:fibre-functor-rigidity` | proposition → remark |
| `def:adjoint-trace` | `rem:adjoint-trace` | definition → remark |
| `def:quantum-bloch-group` | `rem:quantum-bloch-group` | definition → remark |
| `prop:borromean-baryon-interpretation` | `rem:borromean-baryon-interpretation` | proposition → remark |
| `cor:topological-decomposition-mass` | `conj:topological-decomposition-mass` | corollary → conjecture |

These are **mechanical fixes**: only the reference prefix changes;
the referring block's kind is unchanged.  Where these expose
**propagation violations** (CLAUDE.md §3b — provable kinds depending
on conjectures or remarks must themselves be demoted), the deeper
fix is documented in the "Propagation violations exposed" section
below.

### Manifest additions (3 issues)

Three blocks have `.ts` files but were not listed in their chapter
manifest, so the validator treated them as missing labels:

- `eigenvalue-product-expansion` → added to `braids-and-knots/braids-and-knots.ts`
- `nuclear-knot-classification` → added to `braids-and-knots/braids-and-knots.ts`
- (The third is included via the cascade as the unblocked
  `b-over-a-spectral-decomposition` could finally resolve `eigenvalue-product-expansion`.)

## What remains (188 issues, by category)

### Hard errors (`✗`, 14 remaining)

#### Missing labels — block needs to be authored

| Missing label | Cited from | Notes |
|---|---|---|
| `def:hecke-algebra` | `hoefsmit-seminormal-form`, `universal-braid-branching` | The base Hecke-algebra definition is missing a top-level block.  Currently only `rem:hecke-algebra-from-braiding` exists. |
| `prop:geom-yekutieli-alignment` | `hoefsmit-scattering-pipeline` | Block exists at `braids-and-knots/geom-yekutieli-alignment.ts` but not in the chapter manifest. (Manifest fix possible — try adding.) |
| `rem:yekutieli-stokes-remark` | `knot-factor-frobenius-pairing` | No block with this label exists; either author it or rename the reference. |
| `prop:content-scaling-correspondence` | `shell-correction-term-seven` | Same as above — block exists, manifest membership needs verification. |
| `prop:information-speed-of-light` | `regime-table` | Similar — needs author or rename. |
| `prop:hausdorff-dimension` | `regime-table` | Same. |
| `prop:atomic-braid-mass` | `tower-binding-energy` | Same. |
| `def:molecular-hopf-ring` | `shell-threading-conjecture` | Same. |
| `prop:shell-closure-nf-term-count` | `magic-numbers-from-q` | Same. |
| `rem:cmb-torsion-data` | `ns-blowup-physical-evidence` | Same. |
| `prop:cp-violation-spectral-form` | `physics-names-knot-operations` | Same. |

#### Missing Lean siblings — `.lean` file required for definitions

Per CLAUDE.md §3, every `definition` block requires a `.lean`
sibling.  Two definitions are missing them:

- `def:reeb-epsilon` → `algebraic-substrate/reeb-epsilon.lean` (missing)
- `def:q-from-epsilon` → `algebraic-substrate/q-from-epsilon.lean` (missing)

These need genuine formalisation, not just a stub — `reeb-epsilon`
is the substrate parameter generator and `q-from-epsilon` is the
chapter-2 mapping that derives `q` from `ε`.

### Warnings (174 remaining)

- **65 "no Lean declaration"** — provable blocks (`thm`, `prop`,
  `lem`, `cor`) without a Lean sibling.  Each needs a stub `.lean`
  with at least the statement, even if the proof is `sorry`.

- **110 "undefined cross-reference"** — internal `[text](#label)`
  links in `.md` whose `#label` doesn't resolve to a block.  These
  are individually small fixes (rename or remove the link) but
  collectively the largest category.  No structural risk; just
  cleanup.

## Propagation violations exposed by Track 5

The label-prefix renames *uncovered* (but did not fix) several
violations of CLAUDE.md §3b — "a statement that depends on (is
downstream of) a conjecture cannot be a `theorem`, `proposition`,
`lemma`, or `corollary`":

| Dependent block (kind) | Now uses | Should be demoted to | Rationale |
|---|---|---|---|
| `prop:chirality-residue-mass-term` | `conj:knot-factor-frobenius-pairing` | conjecture | propagation violation |
| `thm:knot-mass-formula-unified` | `conj:knot-factor-frobenius-pairing` | conjecture | propagation violation |
| `prop:exterior-square-borromean` | `rem:borromean-baryon-interpretation` | remark or recast | provable kind cannot rely on a remark for content |
| `prop:hoefsmit-seminormal-form` | `def:hecke-algebra` (still missing) | — | blocked on missing definition |
| `prop:mass-endomorphism-tower` | `rem:quantum-bloch-group` | remark or recast | provable kind cannot rely on a remark |
| `prop:mass-endomorphism-jet-tower` | `rem:quantum-bloch-group` | remark or recast | same |
| `conj:mass-endomorphism-conjecture` | `conj:topological-decomposition-mass` | (already conjecture) | OK — chains conjectures |

The demotion work is **substantive** — each renamed block changes
its label kind and possibly its lean ref; downstream blocks may
need their references updated.  This is the right next step for a
deeper sweep, but is out of scope for the mechanical Track 5.

## Recommendation for follow-up sweeps

**Sweep 2 (manifest membership):** verify every `.ts` file in
`content/quantum-observable-universe/<chapter>/` is listed in
that chapter's `<chapter>.ts` manifest.  Several of the
"missing label" hard errors above appear to be missed manifest
entries, not missing files.

**Sweep 3 (Lean stubs):** auto-generate `.lean` stubs for every
provable block missing one, with `sorry  -- Ref: [manuscript]
<label>` placeholders.  Resolves 65 warnings mechanically.

**Sweep 4 (cross-refs):** scan `.md` files for `](#label)` links;
for each, verify `label` exists or remove the link.  Resolves 110
warnings mechanically.

**Sweep 5 (propagation demotions):** apply CLAUDE.md §3b
systematically — every `prop`/`thm`/`lem`/`cor` whose `uses[]`
transitively touches a `conj:` must be demoted to `conjecture` or
its proof must be reworked to remove the conjectural dependency.

## Files affected by this sweep

```
content/quantum-observable-universe/braids-and-knots/braids-and-knots.ts        (+2 manifest entries)
content/quantum-observable-universe/braids-and-knots/chirality-residue-mass-term.ts (1 ref rename)
content/quantum-observable-universe/braids-and-knots/exterior-square-borromean.ts   (1 ref rename)
content/quantum-observable-universe/braids-and-knots/gram-matrix-spectral-connection.ts (1 ref rename)
content/quantum-observable-universe/braids-and-knots/knot-factor-frobenius-pairing.ts (2 ref renames)
content/quantum-observable-universe/braids-and-knots/knot-mass-formula-unified.ts   (1 ref rename)
content/quantum-observable-universe/braids-and-knots/mass-endomorphism-conjecture.ts (1 ref rename)
content/quantum-observable-universe/braids-and-knots/mass-endomorphism-jet-tower.ts (1 ref rename)
content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.ts    (1 ref rename)
content/quantum-observable-universe/observations/physics-names-knot-operations.ts  (1 ref rename)
```

## Validation invocation

```bash
bun run validate quantum-observable-universe
```

Output truncates at `✗ Invalid — N issue(s)`.  N is the total of
hard errors + warnings.  Hard errors block CI; warnings do not.
