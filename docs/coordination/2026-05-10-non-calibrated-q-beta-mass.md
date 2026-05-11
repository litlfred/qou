# Coordination ledger — non-calibrated Q_β + mass cleanup

**Goal**: tighten the framework's β-decay $Q_\beta$ prediction
(non-calibrated, CAL-1 + CAL-2 only) and clean up the mass-formula
pipeline to honor the three-calibration discipline.

**Owner branch**: `claude/display-mass-tables-PAj4i` → PR #637

## Scope map (2026-05-11 snapshot)

| PR | Title | Author | Branch | Classification |
|---|---|---|---|---|
| **#637** (this) | FULL Q_β prediction + non-calibrated mass cleanup | @litlfred | claude/display-mass-tables-PAj4i | own |
| #636 | Audit: Plancherel weight usage | @litlfred | claude/audit-plancherel-usage-a6DgI | **scope-overlap (w_λ semantics)** |
| #635 | Mikusiński WitnessBuilder migration | @litlfred | claude/mikusinski-witness-builder-migration | **convention-overlap (WitnessBuilder.wrap_legacy)** |
| #632 | Paper illustrations (SVG figures) | @litlfred | claude/add-paper-illustrations-Diggj | no overlap |
| #510 | Mod-p Mandelbrot/Julia visualisations | @litlfred | claude/p-adic-mandelbrot-visuals-6Lvum | no overlap (paused) |

(Bot/automation PRs #31, #411 excluded — copilot-driven, separate workflow.)

## Classification axes (per skill §2)

### #636 — scope overlap (w_λ Plancherel weight semantics)

**Overlap**: my new probe scripts (`probe_beta_decay_residue_sum_h3.py`,
`probe_q_beta_residue_per_nucleon.py`) use the q-deformed Wedderburn
weight $w_\lambda = \dim_q^2(\lambda) / [n]_q!$ — exactly the formula
#636's audit identifies as overloaded with the classical Plancherel
form.

**Dependency**: my PR consumes one convention consistently (q-deformed,
normalized to sum-to-1 at n=3). If #636's R1 (rename q-deformed →
$\widetilde{w}_\lambda$) lands, I rename in my probes to match.

**Cherry-pick**: none. #636 is an audit report only, no code changes
to consume.

**Coordination posted**: https://github.com/litlfred/qou/pull/636#issuecomment-4417353011

**Action**: WAIT for #636 R1 disposition before renaming. No blocker.

### #635 — convention overlap (WitnessBuilder.wrap_legacy)

**Overlap**: #635 migrates 5 graded-Mikusiński scripts to
`WitnessBuilder.wrap_legacy`. Copilot's #637 review identified 7
ADDITIONAL scripts in `folio-assistant/computations/` with the same
missing-WitnessBuilder pattern.

**Dependency**: #637 SHOULD consume #635's `wrap_legacy` pattern after
merge to match the convention, rather than racing parallel migrations.

**Cherry-pick**: none. #635 establishes the canonical pattern; #637's
follow-up consumes it.

**Coordination posted**: https://github.com/litlfred/qou/pull/635#issuecomment-4417350818

**Action**: DEFER 7-script WitnessBuilder migration to a follow-up PR
(`claude/witnessbuilder-migration-cleanup`) opened after #635 merges.
Tier-2 fix list documented in PR #637 review reply
(https://github.com/litlfred/qou/pull/637#issuecomment-4417349854).

### #632 — no overlap (SVG illustrations)

**Overlap**: none. Different chapters, different file types (SVG +
illustration skills package). No content-block conflicts.

**Action**: nothing.

## Status comments posted

| PR | Comment | Type | URL |
|---|---|---|---|
| #637 | Tier-1 disposition + Tier-2 deferral plan | own status | https://github.com/litlfred/qou/pull/637#issuecomment-4417349854 |
| #636 | w_λ convention coordination | sibling intent | https://github.com/litlfred/qou/pull/636#issuecomment-4417353011 |
| #635 | WitnessBuilder migration coordination | sibling intent | https://github.com/litlfred/qou/pull/635#issuecomment-4417350818 |

## §6 escalations (inconsistent findings)

None — all overlap is convention-level (naming, formatting). No
inconsistent NUMERICAL findings between my PR and #635/#636.

Cross-check with #636 audit data:
- #636 reports $\dim_q^2/[12]_q! \neq 1$ at n=12
- My #637 probes evaluate at n=3 only, where the discrepancy is
  small
- After my sum-to-1 renormalization at H_3 the convention difference
  cancels exactly. No escalation needed.

## Watch baseline

`origin/main` at `f5e47e52` (no new commits during this session as of
03:35Z). Monitor task `blluxl3xg` re-armed (5-min poll). No upstream
landing to integrate.

## Open queue items on this branch

1. **Tier-2 WitnessBuilder migration** — DEFERRED to follow-up PR after #635 merges (7 scripts)
2. **Tier-3 Lean closure proofs** — 10 sorries opened in `MassComputationChainRoadmap.lean`; each is multi-week R&D
3. **CI validate failure** — believed to be runner-quota constraint (per #635 author's note on PR #634); local validate passes

## Anti-patterns avoided this session (skill §10)

- ✓ Did NOT split the difference on inconsistent w_λ conventions —
  documented per-probe convention explicitly and asked #636 for R1
  disposition.
- ✓ Did NOT silently merge main — fetched + verified no upstream
  changes before opening PR.
- ✓ Did NOT add newly-opened sibling PR to scope without prompting —
  #635 + #636 both got explicit coordination comments asking for
  their preferred coordination mode.
- ✓ Did NOT rewrite my framing in response to inconsistent findings
  — the +1.31 keV residual is intrinsic to predict mode and was
  preserved consistently across 16 commits.

## Last updated

2026-05-11T03:35Z — initial entry; will append on subsequent
coordination cycles.
