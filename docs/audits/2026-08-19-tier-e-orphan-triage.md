# Tier-E orphan triage (2026-08-19)

Owner instruction: *"move those without provenance put into a `_deprecated/`
directory."*

The derivation-gap categorizer reported **186 tier-E orphans** — witnesses with
"no producer on disk; provenance is gone". Taken at face value that reads as 186
retirements. It is not: **13** are genuinely dead, **4** were never orphaned, and
the remaining **169** have lost their producer while still being *consumed*.

## Verdict

| Class | Count | Disposition |
|---|---:|---|
| Dead — no producer, no consumer, no doc reference | **13** | **Deprecated** (`git mv` to `computations/_deprecated/`) |
| False orphan — producer on disk, tool could not see it | **4** | **Categorizer fixed** (no witness touched) |
| Live consumers, lost producer | 147 | **Keep** — see §3, needs its own workstream |
| Prose/doc reference only | 17 | **Keep / freeze** — historical evidence (precedent below) |
| Cited by an open audit objection | 1 | **Keep / freeze** — see §2 |

`computational-only` **1711 → 1698**; `E-orphan` **186 → 169**.

Precedent followed throughout:
[`2026-06-13-orphaned-legacy-witness-triage.md`](2026-06-13-orphaned-legacy-witness-triage.md)
— same criterion (0 code consumers **and** 0 doc references), same convention
(`git mv` to `_deprecated/`, never `git rm`), same owner directive of 2026-06-13:
**deprecate now, delete later** (git history preserves everything).

## 1. Deprecated (13)

All 13 have `scriptFile: null`, no producer under any name or suffix anywhere in
the tracked tree, and **zero** references outside the audit inventory witnesses
that enumerate every witness in the repo (`derivation-chain-audit`,
`witness-producer-executes-audit`, `q0-anchor-consistency-audit`,
`witness-provenance-audit`, `raw-float64-baseline`, `q0-value-drift-audit`).

`binding-damping-rate` · `binding-delta-derivable` ·
`bring-coordinate-linking-weight-probe` · `complete-mass-sweep-2026-05-28` ·
`geom-linking-weight-h7-probe` · `habiro-a0-universal-law` ·
`habiro-binding-linking-weight` · `hoefsmit-h3-std-matrices` ·
`interface-quadratic-structure` · `linking-weight-h4-correction` ·
`sigma3-eigenvalue-h6` · `spectral-borromean-figure-eight` ·
`spectral-phase-ladder-connection`

These are the 2026-05/06-era one-off analysis witnesses — descriptions opening
`STRUCTURAL DISCOVERY:`, `AUDIT:`, `DERIVABLE:`, and one literally titled
*"Complete mass sweep across all sectors after marathon session. 16 PRs
merged."* Session artifacts, not pipeline outputs.

## 2. Kept despite scoring "dead" (1)

`binding-lp-delta-audit.witness.json` has no producer and no code consumer, but
is **named in a live devil's-advocate objection** —
[`2026-06-24-devils-advocate-wave4.md`](2026-06-24-devils-advocate-wave4.md) §
`null-dual`, one of 11 LP/SDP witnesses emitting dual-certificate keys with
`null` values. Deprecating a witness an *open* objection points at would quietly
retire the evidence rather than answer it. Frozen, matching the prior triage's
"keep as historical evidence" disposition.

## 3. The finding that matters: 147 orphans are load-bearing

The tier name invites the wrong action. Of the 186, **147 are read by live
code** — including production consumers (`aK_via_lp_dual.py`,
`low_isotopes_binding_sweep.py`, `binding_depth_stratified_lr.py`), a **content
block** (`mba-step09b-per-isotope-binding.ts`), a **Lean file**
(`BraneGeometricResummation.lean`), and **`content/values/registry.ts`** — the
witnessed-values registry.

That is a worse state than either "dead" or "healthy": a value flows into the
paper from a file **nobody can regenerate**. If one of these is ever found
wrong, there is no producer to fix and re-run. Retiring them is not an option
and neither is leaving them unlabelled. This wants its own workstream —
reconstruct the producer, or freeze the witness explicitly as a declared
constant input. Not attempted here.

## 4. Categorizer fixes (4 false orphans recovered)

Three defects in `derivation_gap_categorize.py`, all in the same direction —
**over**-reporting orphans, i.e. recommending retirement for witnesses whose
producer was on disk the whole time:

| Defect | Recovered |
|---|---|
| `on_disk` scanned only `computations/`, so producers in `docs/audits/scripts/` were invisible | `keystone-step1-gate-wrt-vs-wlambda` |
| `on_disk` globbed only `*.py`, so a `scriptFile` naming a `.lean` never matched | `deltalambda/mu3-submodularity-vacuous-deuteron` |
| `_guess_producer` appended `.py` unconditionally, so `computations/substrate/*.sage` producers sitting **next to their own witness** did not match | `substrate/bring-jacobian-isogeny-factors`, `substrate/lever1-bring-period-trB` |

The widened scan excludes `.claude/worktrees/` — those are checkouts of other
branches, and a producer existing only there is not on disk for this checkout.
(Same blind spot fixed the same day in `mpf_context_dps_audit.py`, where it had
held `precision-gates.sh` red for every agent in the container.)

## 5. The `chi-*-at-qinv-*` class — not orphans, confirming the 2026-06-13 audit

Six of the twenty-two zero-reference candidates were `chi-{atom}(-free)-h{n}-at-qinv-50dps`
witnesses. They are **live**: `bar_pairing_binding_observable.py` both writes and
reads them via the template `chi-{atom}-{kind}-h{n}-at-{q_tag}-50dps.witness.json`
with `q_tag ∈ {q0, qinv}` (see its `_free_atom_chi_via_native(..., "qinv", 50)`
call). The categorizer missed them because a **programmatically constructed**
filename cannot be found by grepping for the literal basename, and the guessed
producer name (`chi_helium_3_free_h9_at_qinv_50dps.py`) does not exist.

This independently reproduces, on current code, the 2026-06-13 audit's finding
that the `chi-*` class self-heals and must not be retired. **A witness whose name
is built by an f-string is invisible to basename analysis** — the general lesson,
and the reason the 13 above were each checked against templates as well as
literals before moving.

## Method

For each of the 186: resolve `scriptFile`; search every **tracked** file for a
producer of that basename under any of `.py`/`.sage`/`.lean`/`.sh`; grep the
tree for the witness basename **and** its `computation` id; classify references
as enumerator (a file mentioning ≥ 20 of the orphans — i.e. an inventory) versus
real; then split real references into code (`.py`/`.ts`/`.lean`/`.sh`) and prose.
Only the intersection of *no producer*, *no code reference*, *no prose reference*
was moved.
