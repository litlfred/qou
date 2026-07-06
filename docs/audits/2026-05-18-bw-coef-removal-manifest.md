# BW-coefficient-shadow-price removal manifest

**Date:** 2026-05-18
**Branch:** `claude/canonical-chi-rust` (PR #683)
**Status:** Draft for owner review — execute on approval.
**Predecessor:**
- [`2026-05-18-m-p-item-b-t5-categorical-attribution.md`](2026-05-18-m-p-item-b-t5-categorical-attribution.md) §7f course-correction
- [`2026-05-11-plancherel-usage-audit.md`](2026-05-11-plancherel-usage-audit.md) — original deprecation of compute scripts

## Why remove

Per §7f of the Item B audit: `prop:mass-coefficient-shadow-price`'s
**computational scaffolding was deprecated in the 2026-05-11
plancherel-usage audit** (moved to `_deprecated/`), but the
narrative block remained in the paper. Production six-term mass
formula does not cite it. The live framework is
`prop:wedderburn-weight-canonical` + `prop:plancherel-weight-
boundedness` + Wenzl bridge. Keeping the BW-shadow-price block
maintains a dead-end structural framing the codebase has moved
past.

## Three categories of action

### Category A — full block removal (5 blocks, 15 files)

These blocks are **structurally tied** to the BW-shadow-price
program — either as its foundation, its main consequence, or
its corollaries. They cannot survive the BW-shadow-price block's
removal without losing essential coupling.

| Block label | .ts | .md | .lean | Reason |
|-------------|-----|-----|-------|--------|
| `prop:mass-coefficient-shadow-price` | ✅ | ✅ | ✅ | the Tier-1 target |
| `prop:frobenius-self-duality-forces-lp-dual-extraction` | ✅ | ✅ | ✅ | foundation — "structural justification for the LP-dual formulation of mass" |
| `prop:mass-formula-iterative-lp-dual` | ✅ | ✅ | ✅ | "REPLACES the seven ad-hoc mass-formula terms with one iterative recursion" — superseded by the actual six-term-mass-formula-complete in production |
| `prop:unified-iterative-correction` | ✅ | ✅ | ✅ | "per-step Wedderburn projection over all partitions" — uses bw-coef as primary backing, becomes orphaned without it |
| `prop:wigner-2-coefficient` | ✅ | ✅ | ✅ | "Wigner-2 coefficient at k=6 derived from the LP dual" — derivation framing collapses without bw-coef |

**Subtotal: 15 sibling files (5 blocks × 3 files).**

### Category B — keep block, scrub bw-coef references (4 blocks)

These blocks have **independent structural content**; they merely
cited mass-coefficient-shadow-price as supporting infrastructure.
Scrub the `uses[]` entry + narrative cite; leave the block
intact.

| Block label | Action |
|-------------|--------|
| `conj:knot-factor-frobenius-pairing` | Drop `prop:mass-coefficient-shadow-price` from `uses[]`. Item B's canonical T5 lives here; rewrite is straightforward. |
| `prop:magic-numbers-from-q` | Drop `prop:mass-coefficient-shadow-price` from `uses[]` (uses[] keeps `conj:shell-closure-nf-term-count`, `prop:nuclear-knot-classification`). |
| `rem:sdp-as-thimble-flow` | Drop `prop:mass-coefficient-shadow-price` from `uses[]` (encounter remark; keeps Picard–Lefschetz cites). |
| `prop:confinement-frobenius-reciprocity` | Drop `prop:mass-coefficient-shadow-price` from `uses[]`. |

**Subtotal: 4 .ts files modified.**

### Category C — soft cite scrubbing in .md narrative (~19 files)

These .md files cite `mass-coefficient-shadow-price` (or one of the
Category-A removed blocks) in prose. For each:

1. If the cite is just supporting context → remove the parenthetical
   reference.
2. If the cite carries a structural claim → replace with the
   canonical replacement (`prop:wedderburn-weight-canonical` or
   `prop:plancherel-weight-boundedness`).
3. If the cite is load-bearing for a paragraph that no longer
   stands without it → flag for owner re-write, do not silently
   delete content.

**Files to scrub (estimated; computed after Category-A removal):**

- `knot-operator-energy.md`
- `knot-operator-energy-exists.md`
- `wedderburn-weight-canonical.md` (ironic — the live replacement
  cites the deprecated block)
- `stable-atom.md`
- `unstable-atom-decay-channel.md`
- `alpha-5-jm-central-empirical-findings.md`
- `per-partition-k-lambda-rule.md`
- `markov-trace-axiomatic-closed-form.md`
- `y-lambda-sign-pattern.md`
- `wigner-2-coefficient.md` *(only if Category A is not adopted; see ✱)*
- `shell-schur-weyl-self-duality.md`
- `shell-correction-term-seven.md`
- `encounter-intro.md`
- `confinement-frobenius-reciprocity.md`
- `index-of-definitions/definition-index.md`
- `observations/sdp-regime-switch.md`

✱ Files belonging to Category-A-deleted blocks are removed wholesale.

**Subtotal: ~16 .md files modified after Category A.**

### Category D — chapter manifest + Lean references

- `content/quantum-observable-universe/braids-and-knots/braids-and-knots.ts` — remove `"mass-coefficient-shadow-price"` (and the four Category-A block labels) from the chapter section list.
- `content/quantum-observable-universe/index-of-definitions/definition-index.md` — remove the `MassCoefficientShadowPrice` row.
- `content/quantum-observable-universe/braids-and-knots/knot-operator-energy-unique.lean` — currently cites `MassCoefficientShadowPrice`; update or remove.
- `content/quantum-observable-universe/braids-and-knots/knot-factor-frobenius-pairing.lean` — citation cleanup.
- `content/quantum-observable-universe/braids-and-knots/unified-iterative-correction.lean` — removed wholesale with the block (Category A).

## Total file impact

| Category | Block-removals (×3 files) | Manifest edits | Narrative edits | Total files affected |
|----------|---------------------------|-----------------|-----------------|----------------------|
| **A — full delete** | 5 × 3 = 15 | — | — | 15 deletes |
| **B — uses[] scrub** | — | 4 .ts | — | 4 edits |
| **C — narrative scrub** | — | — | ~16 .md | ~16 edits |
| **D — chapter / index / Lean cross-refs** | — | 2 (chapter ts, def-index md) + ≥2 .lean | — | ~4 edits |
| **Total** | | | | **~39 files** |

## Cited-from-deprecated-folder check

After Category A executes, also clean up:
- `computations/_deprecated/bw_wenzl_shadow_equivalence.py` — purge or leave (already deprecated; harmless to keep as historical artefact).
- Other `_deprecated/` scripts with BW references: same call.

Recommendation: **leave `_deprecated/` alone** — it is already
gitignored from the active compute pipeline and serves as an
archaeological record.

## Conjectural-propagation audit re-run

After execution, run:

```bash
cd content && bun run pipeline/conjectural-propagation-audit.ts
```

to ensure no Category-A block left orphaned dependents. If any
block's `uses[]` still references a removed Category-A label,
either:
- the dependent block belongs in Category A too (extend scope), or
- the cite should be rewritten / removed.

## Sibling-PR coordination

- **PR #682** does not touch the BW-coef block; no conflict.
- **PR #686** does not touch the BW-coef block; no conflict.
- **PR #679** does not touch the BW-coef block; no conflict.
- **PR #671** is m_p closure analysis; will be affected if it cites bw-coef.
  Quick check needed before execution.

## Execution sequence

Single atomic commit recommended (39 files moves together):

1. Delete Category A files (15 deletes via `git rm`).
2. Edit Category B `.ts` files (4 manifest edits — drop one `uses[]` entry each).
3. Edit Category C `.md` files (~16 narrative scrubs).
4. Edit Category D infrastructure (~4 cross-ref cleanups).
5. Run `cd content && bun run validate` → must pass.
6. Run `cd content && bun run pipeline/conjectural-propagation-audit.ts` → no new orphans.
7. Single commit: `paper: remove mass-coefficient-shadow-price + 4 deprecated LP-dual siblings (per Item B audit §7f)`.

## Open questions

1. **Wigner-2 coefficient block** — is its CONTENT (Wigner-2 = `[2][4][6]h/(2[3]²[5])`) still relevant if the LP-dual derivation framing is dropped? If yes, the block could be rewritten to derive Wigner-2 via a non-LP path (e.g. directly from seminormal trace pairing) instead of deleted. **Owner call.**

2. **`prop:unified-iterative-correction`** — is its "iterative correction" concept still in use anywhere else (e.g. m_p chain closure)? If the iterative-LP framing is gone but the iteration concept survives, this block could be rewritten. **Owner call.**

3. **`braids-and-knots.ts` chapter manifest** — does removing 5 propositions from this chapter leave a structural gap in the narrative flow? **Owner call** on whether to insert replacement section headers / transitional remarks.

## Approval

Owner approval needed on:
- Scope (Category A list — particularly Wigner-2 and unified-iterative-correction)
- Single-commit vs split commits (recommended single)
- Whether to coordinate with PR #671 first
