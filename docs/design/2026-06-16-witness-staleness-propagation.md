# Witness-staleness propagation — design + closure plan

**Date:** 2026-06-16
**Branch:** `claude/youthful-faraday-5snwms` (PR #2355)
**Question (owner):** "How do we best ensure staleness of children is
propagated up the witness chain, as CI infra / QA?"

## TL;DR

Most of the mechanism **already exists** (2026-05-16) but is
**under-adopted, partly broken, and not CI-enforced**. The fix is *not* a
new system — it is: (1) fix + extend the existing validator (done here:
added self-staleness), (2) wire it into CI (warn → strict), (3) drive
adoption of the dependency edges, (4) pair refresh with assertion-gating
so a regeneration can't launder a regression.

## What exists today

| Primitive | Where | Status |
|-----------|-------|--------|
| Record upstream edges | `WitnessBuilder.add_upstream()` / `load_and_hash_upstream()` → `upstream_witness_hashes` | exists; **8.8% adoption** (144/1640 witnesses) |
| Self-identity | every witness carries `scriptHash` + `scriptCommitSha` | recorded, but **nothing checks it post-hoc** |
| Drift validator | `computations/witness_dependency_drift.py` | existed but **crashed** on the corpus + checked **upstream only** — both fixed here |
| Value gate | witness `assertions` + `allPassed` | exists; **not consulted on refresh** |
| Prior analysis | `docs/audits/2026-05-16-stale-witness-infra-gap.md` | identified the DAG gap; left CI-wiring + adoption "to operators" |

## Quantified state (enhanced validator, 2026-06-16)

Running `witness_dependency_drift.py` over 1640 witnesses:

- **8.8%** declare upstream edges (144/1640).
- **624 upstream drift records** among those that do.
- **694 self-stale (42%)** — `scriptHash` ≠ current producer hash — that
  no CI check flags. (Caveat: some are cosmetic producer edits or
  regenerable caches; the point is *detectability*, not that all 694 are
  numerically wrong. The hadron-knot-table witness — which advertises a
  retired empirical-fit ⁴He binding the current categorical producer no
  longer reproduces — is one of the 694.)

## The mechanism (build-system invalidation, two directions)

A witness is **stale** iff either:

- **SELF:** its recorded `scriptHash` ≠ the current hash of its producer
  (`scriptFile`). The producer changed; the witness wasn't re-run.
- **UPSTREAM (transitive):** any recorded `upstream_witness_hashes[i].sha256`
  ≠ the current bytes-hash of that upstream witness.

These compose into full upward propagation: a leaf producer edit flips
SELF on the leaf; regenerating the leaf changes its bytes; that flips
UPSTREAM on every parent that recorded the leaf's hash; and so on up the
chain. Staleness is **derived, never stored** — the same principle the
repo already uses for proof-object status.

**Stricter (optional) — Merkle effectiveHash.** Define
`effectiveHash = H(scriptHash ‖ params ‖ sorted(input effectiveHashes))`.
Then a single root-hash comparison detects transitive staleness in *one*
pass without needing each parent to be regenerated first (closes the
"stale-but-unchanged-file upstream" corner the byte-hash check misses
until the child is rebuilt). Deferred — the two-direction byte check is
enough to start.

## The six gaps (and the closure plan)

1. **Validator was broken** → *fixed here* (guarded non-dict
   `data`/`derivation_inputs`/top-level-list witnesses).
2. **Self-staleness unchecked** → *fixed here* (`check_self_staleness`
   resolves `scriptFile` → producer, compares `scriptHash`; warn-only by
   default, `--self-strict` to gate).
3. **Not CI-enforced** → add a workflow running the validator. Start
   **warn-mode** (`--no-self`-strict, non-failing) to surface the backlog
   without red-walling every PR; escalate to **`--strict`** once the
   backlog drains. A starter workflow ships here as
   `.github/workflows/witness-staleness.yml` (warn-mode). NOTE: this
   branch predates the CI reorg on `main` (only `build.yml` present);
   at merge, reconcile with `main`'s `witness-pipeline.yml` rather than
   duplicating.
4. **8.8% edge adoption** → spread `add_upstream()` one producer per PR
   (the 2026-05-16 adoption pattern). Prioritise the mass/binding chain
   consumers. A lint can warn when a producer reads another
   `*.witness.json` without recording it as an upstream.
5. **Stale witnesses can launder retired fits** → on regenerate, **run
   the witness's `assertions`**; block the refresh (and the PR) if
   `allPassed` flips to false. This is the QA crux: staleness detection
   alone is insufficient. The hadron ⁴He `B_MeV` is committed as 28.19
   (≈ experiment, a *retired* empirical fit) but the current categorical
   producer gives 0.72 (binding is the open Δ_λ problem). A stale witness
   thus retroactively violates the no-fit discipline — assertions tied to
   the framework's *actual* claim (what the categorical path produces, and
   its distance from `B_AME`) keep a disavowed fit from sitting unflagged.
6. **Runlist problem** (from 2026-05-16): the witness pipeline only
   re-runs a hardcoded script list, so most witnesses are never
   regenerated in CI. The DAG validator sidesteps this — it checks
   recorded-vs-current hashes *without* re-running producers, so it
   covers every witness, on every PR, cheaply.

## Minimal first step (shipped on this PR)

- Fixed + extended `witness_dependency_drift.py` (self-staleness +
  adoption %).
- `.github/workflows/witness-staleness.yml` — warn-mode CI step.
- This design doc + the hadron findings doc.

## Recommended escalation order

1. Land the warn-mode CI step (visibility, no PR breakage).
2. Drain self-staleness: regenerate the genuinely-wrong witnesses
   (assertion-gated), starting with hadron-knot-table.
3. Drive `add_upstream` adoption on the mass/binding chain.
4. Add assertion-gating to the regenerate path.
5. Flip CI to `--self-strict`, then `--strict`.
6. (Optional) effectiveHash Merkle roots for single-pass transitive
   closure.
