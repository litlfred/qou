---
# qou-2r42
title: 'witness provenance COMPLETENESS audit: 55 missing engine/scriptFile/commitSha, and it is in no gate array'
status: todo
type: task
priority: normal
created_at: 2026-08-21T15:30:03Z
updated_at: 2026-08-21T15:30:37Z
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
