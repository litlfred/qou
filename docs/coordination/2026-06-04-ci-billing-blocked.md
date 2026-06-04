# CI status: GitHub Actions is billing-blocked (2026-06-04)

**Confirmed by repo owner: `ci=billing`.**

## Symptom

Every GitHub Actions workflow on `litlfred/qou` fails 0–4 seconds
after start, across **all** workflows and **all** commits:

- Witness pipeline, release-please, Build Paper Assistant Image,
  paper-builder-image, witness-refresh, qa-sweep — 30/30 recent
  runs failed.
- Each run dies at runner provisioning, before any step executes.
- Job logs return HTTP 404 (no runner ever produced output).

## Root cause

**Account-level GitHub Actions wall** — minutes quota / spending
limit on the private repo, not a code defect. The runner never
executes a single script, so the failure is independent of the
diff.

## Discipline implication (IMPORTANT for all agents)

Until billing is restored:

1. **Do NOT attribute red CI to code.** A failing `validate` /
   witness-pipeline check is the billing wall, not a numerical
   drift, float64 issue, or witness staleness. Diagnosing it as
   code wastes cycles (this cost ~a full session of
   misattribution: "float64 flaky" → "numpy in pipeline" →
   "thimble drift", all wrong — the runner never ran).

2. **Local validation is the merge gate.** Run the witness
   validators + `bun run validate` locally; if they pass, the PR
   is mergeable. The GitHub `validate` check will show red
   regardless and can be disregarded for merge decisions.

3. **Don't add per-PR CI workarounds** (drift exclusions, witness
   refreshes purely to "make CI pass") — they cannot help while
   the runner is down, and they accrete cruft.

## Restore steps (owner-only)

1. GitHub → Settings → Billing & plans → Actions minutes /
   spending limit. Raise limit / confirm payment method.
2. If billing is fine: repo → Settings → Actions → General →
   confirm Actions are enabled.
3. Re-run one failed workflow to confirm green; then this note
   can be removed.
