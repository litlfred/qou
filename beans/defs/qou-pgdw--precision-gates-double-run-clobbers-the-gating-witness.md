---
# qou-pgdw
title: precision-gates.sh runs the raw-float64 audit twice and the advisory run overwrites the gating run's committed witness
status: completed
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T21:10:00Z
updated_at: 2026-11-22T21:33:07Z
parent: qou-9nnz
---

## What

`scripts/precision-gates.sh` invokes `computations/witness_raw_float64_audit.py`
at two places:

- **line 63** — the **gating** run: full corpus, `--strict`
- **line 89** — an **advisory** run: `--scan-root docs/audits/scripts --strict`

Both write the same output file,
`computations/witness-raw-float64-audit.witness.json`. The narrow advisory run
therefore **clobbers the full-corpus result**.

## Observed

After a normal `bash scripts/precision-gates.sh`, the committed witness is left
dirty with:

- `dirty_witnesses` 1561 → **5**
- `drained_files` 14 → **1572**
- every `lp_dual_carved_out_by_file` / `f64_integrator_carved_out_by_file`
  entry **dropped**

## Why this is dangerous, not cosmetic

It looks exactly like the case the script's own message tells you to act on —
*"a COUNT moved, so the committed witness was stale; commit the regenerated
one."* Committing it would **replace a corpus-wide audit with a 5-file one**
and silently drain the carve-out records.

That is the precise shape of the failure the NO-FLOAT64 discipline exists to
prevent: a red made green by shrinking what is measured. Worse, here the agent
does it *believing it is following instructions*, so the usual "never widen a
baseline" guard does not fire.

## How it was distinguished from a real change

Running the gating invocation **alone** —
`python3 computations/witness_raw_float64_audit.py --strict` — leaves the
committed witness **byte-identical**. That is the discriminator; use it before
ever committing a regenerated raw-float64 witness.

## Fix

Give the advisory invocation its own output path (or add a `--no-write` /
`--out` flag), so the two scans cannot share a witness.

## Provenance

Found during the `/prepare-merge-auto` pipeline for PR #5123. **Not fixed
there** because `precision-gates.sh` is shared and sibling PR #5124 was editing
gates in the same file — deliberately left to its own owner rather than
creating a cross-PR conflict. Detail:
https://github.com/litlfred/qou/pull/5123#issuecomment-5304213117

---

## Verification Update (2026-11-15 — Owner Ruling Q-9NNZ-2 = 1)

- **Status:** Kept `in-progress` per owner review policy.
- **Verified on `main`:**
  - `computations/witness_raw_float64_audit.py` derives both `_output_name(scan_root)` (line 131, landed in `7083509439` / `7668b998e9` on `2026-08-15`) and `_baseline_path(scan_root)` (line 76, landed in `8ba73cc915` on `2026-08-21`), emitting `witness-raw-float64--<slug>-audit.witness.json` and `raw-float64-baseline--<slug>.json` for non-default `--scan-root` values without clobbering `computations/witness-raw-float64-audit.witness.json`.

## 2026-11-22 — CLOSED: fixed on main, as the 2026-11-15 verification already found (bean-hygiene wave 2)

Session https://claude.ai/code/session_01Qmmkt95ogQs6aFq9zdMmwF. Checked against main `3c4c98fccf3`.

Re-checked: `computations/witness_raw_float64_audit.py:131` `_output_name(scan_root)` and `:76` `_baseline_path(scan_root)` give every non-default `--scan-root` its own witness and baseline, so the advisory runs at `scripts/precision-gates.sh:399` and `:430` no longer write the gating run's file (`:78`). The 2026-11-15 entry verified the same and kept the bean open only for owner review; nothing in the body names remaining work. Not one of the six reds PR #9105 is fixing.

## 2026-11-22 — Applicability review (owner instruction 2026-11-22, bean-hygiene wave 2)

Session https://claude.ai/code/session_01Qmmkt95ogQs6aFq9zdMmwF. Retroactive review of this pass's closure against `docs/coordination/owner-rulings.md` on main `3c4c98fccf3`.

**Verdict: ALREADY-DONE (closure stands).** The bean is about tooling or arithmetic precision (gates, audits, float64 paths, provenance, tracker structure). Its premises name no physics object, convention, anchor or particle assignment, so none of the retired premises (σ₀σ₁ photon, trefoil electron, convention C, the z = 1 Q_β base, census selection, absolute mass, muon pin A, virtual photons, adopted quark charges) or today's rulings (strand colour states, b = −qX, the fixed constant term 1 of the photon, the block U(1)_em charge) bear on it. What landed still answers its question.
