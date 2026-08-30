---
# qou-2r42
title: 'witness provenance COMPLETENESS audit: 55 missing engine/scriptFile/commitSha, and it is in no gate array'
status: todo
type: task
priority: normal
created_at: 2026-08-21T15:30:03Z
updated_at: 2026-08-30T13:40:18Z
---

Found 2026-08-21 while sweeping duplicate witness stems (qou-kcii).

## Two DIFFERENT audits share the name witness_provenance_audit.py

  computations/witness_provenance_audit.py         529 lines  exit 0
  computations/audits/witness_provenance_audit.py  292 lines  exit 1

Not a fork of one script -- they check different things:
  computations/  -> provenance CORRECTNESS: does a witness's scriptFile
                    actually WRITE that witness? (wired blocking in
                    precision-gates.sh 2026-08-16, bean qou-w9s3)
  audits/        -> provenance COMPLETENESS: does a witness carry the
                    required engine / scriptFile / commitSha at all? (I14)

precision-gates.sh runs the computations/ one by full path, so the gate is
unaffected. But anyone 'resolving the duplicate' by keeping the audits/ copy
-- the more natural home for an audit -- would silently swap one check for
another and flip the gate red for an unrelated reason.

## The completeness audit is RED and RUN BY NOTHING

  PROV_MISSING        : 55
  completeness ratio  : 0.979

Grepped every .sh / .yml / .json / .py: it appears in no gate array and no
workflow. Only references are a watcher-queue entry and its own script-qa
sidecar. That is a THIRD instance of the qou-j6gb pattern precision-gates.sh
warns about at the top of the file ('A GATE OUTSIDE THIS ARRAY IS A GATE
NOBODY RUNS') -- after mpf_import_time_dps_audit and
witness_provenance_audit(correctness) itself.

## The queue note about it is STALE and should not be trusted

.beans/compute-integration-watcher-queue.json:1085 says, verified
2026-06-13: 'the local audits/witness_provenance_audit.py scans only 32
files (PROV_MISSING=0, completeness 1.000); it CANNOT reproduce the
dashboard 26 of 707'. Kept queued pending re-scope.

Today it scans far wider and reports 55 missing. So the scope question that
entry parked on has resolved itself -- the finding is real and larger than
the 26 the dashboard claimed. The queue entry should be re-opened with
today's number rather than left as UNSURE/STALE.

## Not fixed here

Draining 55 witnesses is a migration (WitnessBuilder adoption or removal per
the audit's own wording), not a bystander's sweep. Wiring it as a gate is
also premature: this repo's own rule is that a gate red on arrival gets
skipped, so it wants draining first, or wiring advisory the way the
audits-tree raw-float64 entry was.

Also note the audit itself trips the raw-float64 ratchet on its own output
(.data.counts.completeness_ratio is a bare float) -- a small producer-side
fix for whoever takes it.


## RE-MEASURED 2026-08-30 — the count nearly doubled, and two claims above are now stale

Measured by running `scripts/precision-gates.sh --changed` on a tree synced to
`main` and diffing the regenerated `computations/audits/witness-provenance-audit.witness.json`
against its committed copy (ephemeral fields masked).

| field | committed | fresh |
|---|---|---|
| `total_scanned` | 2907 | **2940** |
| `prov_ok` | 2491 | 2516 |
| **`prov_missing`** | **78** | **101** |
| `prov_exempt_no_reader` | 258 | 241 |
| `prov_audit_exempt` | 80 | 81 |
| `prov_exempt_acknowledged` | 0 | 1 |
| `completeness_ratio` | 0.97317 | **0.96565** |

So `prov_missing` is **101**, not the 55 in this bean's title — and **+23 in
the 172 commits** between the committed copy and today. The ratio is falling,
which is the part that matters: this is an active regression, not a static
backlog.

**Attribution, since a committed-vs-fresh diff invites the wrong one.** The
branch that measured this (`claude/bn8e-lit-search-2026-08-30`) adds exactly
**one** witness, and that witness is `PROV_OK` with `missing_fields: []`. All
33 of the `total_scanned` increase bar one, and all 23 of the `prov_missing`
increase, are **main's**.

### Two claims above are now stale

1. **"The completeness audit is RED and RUN BY NOTHING" — it IS run.**
   `precision-gates.sh` reports it as *"witness provenance completeness
   (advisory)"* under `ADVISORY (not gating)`. That is exactly what this
   bean's own closing paragraph recommended (*"wiring it advisory the way the
   audits-tree raw-float64 entry was"*), so the recommendation was taken and
   the bean was not updated. Note the separate `RED: ... witness scriptFile
   provenance` line is the **other** script — the `computations/` CORRECTNESS
   audit, wired blocking — so the two-scripts-one-name hazard this bean opens
   with is live in the gate output itself, one line apart.
2. **"`.data.counts.completeness_ratio` is a bare float" — fixed.** It
   serialises as a string in both the committed and the fresh witness
   (`'0.973168214654282765737874097007223942208462332301341589267286'`), so
   the producer-side raw-float64 trip is gone.

### Still not fixed here, and now with a reason

Draining 101 is still a migration, not a bystander's sweep. But the advisory
wiring plus a **rising** count means the drain is losing to the inflow: any
plan that only drains the backlog leaves the regression. Whatever takes this
should first find out *why* 23 new witnesses landed without provenance in one
172-commit window — a producer template, a copied script, or WitnessBuilder
not being reachable from some subdirectory — because that is cheaper to fix
than 101 files.
