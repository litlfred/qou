---
# qou-pgdw
title: precision-gates.sh runs the raw-float64 audit twice and the advisory run overwrites the gating run's committed witness
status: todo
type: task
priority: high
created_at: 2026-08-15T21:10:00Z
updated_at: 2026-09-12T18:17:17Z
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

## SECOND INSTANCE of this class found 2026-09-12 — `qou-k1xe`

This bean is not an isolated script bug. The same shape — **two writes to one
`*.witness.json` path, the narrower silently replacing the richer** — was found
independently three weeks later in
`computations/deltalambda/he4-magnus-omega2-sign.witness.json`, written by both
`he4_magnus_omega2_sign_sparse_probe.py` (which emits both weight families and
declares `headline_pairing = "P_total_wenzl"`) and `he4_magnus_mpfr_probe.py`
(which mentions Wenzl **zero** times). A re-run of the second would delete 8
`results` keys and 10 top-level keys, among them the entire Wenzl column — the
A=4 weight-family result itself. Guarded in `99b305e60` (PR #7218); bean
`qou-k1xe`.

**This bean's own defect cost a session directly, which is evidence for its
priority.** A first read of `precision-gates.sh --changed` showed two
`RAW-FLOAT64 AUDIT` blocks, both `NEW 0 / REGRESSED 0`, and nearly got reported
as a clean ratchet. The unconditional run and a pristine `origin/main` baseline
both report **`REGRESSED: 3`** — byte-identical to the three named in
`docs/audits/2026-09-08-raw-float64-ratchet-is-regressed-on-pristine-main.md`.
The zeros were the **advisory** run's numbers standing in for the gating run's,
exactly as described above. So the clobber does not merely dirty a committed
file; it makes the gate's own console output misreport the corpus.

**Neither instance is a detector blind spot** — both detectors work. The gap is
that **nothing audits the write surface**. A cheap static scan would enumerate
every witness path written anywhere under `computations/`, flag any path with
more than one writer, and diff the key sets those writers emit. No compute, no
producer runs. Not built; scoped in `qou-k1xe` so it is not re-discovered a third
time.
