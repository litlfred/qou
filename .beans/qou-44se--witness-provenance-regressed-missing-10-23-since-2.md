---
# qou-44se
title: 'Witness provenance regressed: missing 10 -> 23 since 2026-08-01, completeness 0.9952 -> 0.9903'
status: todo
type: task
created_at: 2026-08-09T02:19:38Z
updated_at: 2026-08-09T02:19:38Z
---


Found 2026-08-09 while triaging stalled PR #4568 (bean `qou-x6as`).

#4568 refreshes the provenance-audit snapshot and claims *"missing 10 -> 9"*.
That was true on 2026-08-02. Re-running the producer
(`computations/audits/witness_provenance_audit.py`) against current main:

| snapshot | total_scanned | prov_missing | completeness_ratio |
|---|---|---|---|
| main (2026-08-01) | 2296 | 10 | 0.99521 |
| PR #4568 (2026-08-02) | 2351 | 9 | 0.99575 |
| **current main** | **2470** | **23** | **0.99028** |

**The backlog is moving the wrong way** — this is a live regression, not a
stale-snapshot artifact. 13 new witnesses landed without
`engine` / `scriptFile` / `commitSha`.

Several cluster around currently-open PRs, and are best fixed there, where
the producers are in hand:

- `whitehead-c-sigma-fig8-calib`, `whitehead-c-sigma-hiprec`,
  `whitehead-c0-mpmath`, `whitehead-volume-identification`
  -> open PRs **#4571** (c_sigma torsion) and **#4532** (VC squeeze)
- `qcollatz_cycle_census` -> open PR **#4435**
- `qbeta-5two-enhanced-dilog` -> open PR **#4588**
- `two-row-vs-higher-row-binding-split`, `qlift_kernel_candidate_crosscheck_probe`,
  `theta_jet_gb_grading_probe` -> unattributed so far

**Root-cause question worth answering before draining:** all 13 are missing
the *same three* fields, which is the signature of producers that build their
witness dict by hand instead of going through `WitnessBuilder`. If so the fix
is to route them through the builder, not to hand-patch 13 JSONs — and a
guard is wanted so the next 13 do not appear the same way.

Regenerate the number with:

```bash
python3 -u computations/audits/witness_provenance_audit.py
```

(then `git checkout --` the witness unless you intend to land the snapshot).

## Progress 2026-08-09 (PR #4834) — root cause fixed, one witness regenerated

**Root cause confirmed and fixed at the helper, not the JSONs.**
`WitnessBuilder.stamp_staleness_metadata` — the public helper whose stated job
is stamping provenance onto hand-built payloads — set `scriptHash`,
`scriptCommitSha`, `commitSha`, `engine`, `engineVersion`, `computedAt`,
`durationMs` but **not `scriptFile`**. So every witness stamped by it failed
the audit's `engine`/`scriptFile`/`commitSha` triple while looking fully
provenanced.

Corroboration that this was a known papercut: `m_tau_knot_prediction.py:343`
sets `witness["scriptFile"] = basename(__file__)` **by hand immediately after
calling the helper**. That workaround is now unnecessary.

Fixed in both mirrors:
- `tools/qou-substrate/python/qou_substrate/witness.py`
- `qou-mass/src/qou_mass/_internal/witness_base.py`

Four whitehead producers now stamp provenance (they hand-built the dict and
`json.dumps`'d it, bypassing the helper entirely):
`whitehead_c_sigma_hiprec.py`, `whitehead_c_sigma_fig8_calib.py`,
`whitehead_c0_mpmath.py`, `whitehead_c0_run.py`.

**Regenerated: 1** — `whitehead-c-sigma-fig8-calib.witness.json`
(verified additive-only: provenance + `q0Anchor`/`q0Value`, no science value
changed).

## THREE separate defects found while doing it — none of them the missing fields

1. **`whitehead-c-sigma-hiprec` is not reproducible from its default
   invocation.** The committed witness has `dps=100` and
   `Ns=[400,600,900,1300,1700,2100,2500,3000]`; the script defaults to
   `dps=60`, `Ns=[300,400,500,700,900,1100,1400]`. Re-running degrades
   `best_match_digits` **20 → 16** and shifts `c_sigma_extrapolated` in the
   17th digit. **Not regenerated** — a provenance stamp is not worth
   downgrading a 20-digit result. Faithful command (recovered from the
   witness's own recorded parameters, untested — it is an O(N²) mpf tower to
   N=3000 at dps=100):
   ```bash
   python3 computations/whitehead_c_sigma_hiprec.py 100 400,600,900,1300,1700,2100,2500,3000
   ```

2. **Two scripts write the same witness.** `whitehead_c0_mpmath.py` *and*
   `whitehead_c0_run.py` both write `whitehead-c0-mpmath.witness.json`. The
   committed one records `computation: "whitehead_c0_run"`, so `_run` is the
   real producer — running `_mpmath` silently overwrites it with a different
   script's output (it also rewords `description` and `precision`). A witness
   with two producers has no meaningful `scriptFile`. **Not regenerated**;
   the `_run` re-run exceeded a 10-minute budget and was killed, so nothing
   partial was committed.

3. **None of these producers use the canonical precision module** (owner
   observation). `computations/substrate/_precision.py` exposes
   `set_compute_dps()`, and `whitehead_c_sigma_hiprec.py`,
   `whitehead_c0_run.py`, `whitehead_c_sigma_fig8_calib.py` reference it
   **zero** times — they hardcode `mp.mp.dps` or read it from `sys.argv[1]`.
   That is *why* defect 1 exists: output precision is an unrecorded CLI
   argument instead of repo policy. **This is the deeper fix** and is the
   right next step: route these producers through `set_compute_dps()` and
   record the resolved dps + all tower parameters in the witness, so the
   invocation is recoverable from the artifact rather than from memory.

Deliberately not done here: changing precision semantics on a landed 20-digit
result is a behaviour change that wants its own scoped change, not a rider on
a provenance fix.
