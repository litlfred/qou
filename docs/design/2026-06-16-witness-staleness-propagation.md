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

## Assertion gate (#4 — shipped as `witness_assertion_gate.py`)

The value complement to staleness. Scans every witness for
`allPassed == false`, separating **production** (actionable) from
**audit-only/exploratory** (failing assertions are expected — an honest
open gap). Current corpus: **47 production witnesses with failing
assertions**, 14 audit-only. On the regenerate path this blocks a refresh
whose `allPassed` flips false (so a regeneration can't launder a
regression or keep a retired fit). `--strict` exits 1 on production
failures.

## Minimal first step (shipped on this PR)

- Fixed + extended `witness_dependency_drift.py` (self-staleness +
  adoption %).
- `.github/workflows/witness-staleness.yml` — warn-mode CI step.
- This design doc + the hadron findings doc.

## Triage of the 694 self-stale (#1)

The 694 self-stale count **overcounts "wrong"**. Most of it is the recent
repo reorg (producers moved/reformatted, changing `scriptHash` without
changing compute output) — cosmetic for the *value*, real for the *hash*.
Precisely classifying each into genuine-wrong vs cosmetic requires
*regenerating* the producer and diffing the data (expensive; some
producers hang on SDP solves), so a per-witness 694-way classification is
not cheaply truthful.

**Better proxy for "actually wrong":** intersect self-staleness with the
**assertion gate** (#4). A witness that is self-stale *and* has
`allPassed == false` is the actionable set — its producer changed *and*
its own claims fail. The 47 production assertion-failures are the
high-signal list to drain first; pure self-staleness (no assertion
failure) is mostly reorg churn and is drained by a routine regenerate
pass, not investigation. Recommended: run
`witness_assertion_gate.py --strict` to get the 47, fix/regenerate those
(assertion-gated), then bulk-regenerate the cosmetic remainder.

## Adoption rollout (#2)

Edge adoption is 8.8%. A code-only `add_upstream` change does not populate
the edge until the witness is regenerated, so adoption advances one
*regenerated* producer at a time. Priority order (highest fan-in first):

1. The **mass/binding chain** consumers that read `proton-mass-codata-50dps`,
   `atomic-tr-m-mpfr-50dps`, `q-beta-predicted` (the 2026-05-16 audit
   already wired 3; ~50 remain).
2. Any producer that `json.load`s another `*.witness.json` — grep
   `read_text\|json.load` over `computations/**/*.py` for cross-witness
   reads, and add `builder.add_upstream(path)` for each.

A lint can enforce this going forward: warn when a producer reads a
`*.witness.json` it does not record as an upstream (the dual of the
q=111/100 ratchet). Deferred — not built here.

## Assertion-failure drain (#2 — triage of the production set)

After fixing the gate's classifier (a `set_audit_only(doc)` witness
serialises `auditOnly` as the doc-path *string*, not a bool — these were
mis-bucketed as production), the count is **39 production / 22
audit-only** (was 47/14). The 39 split three ways, and **most must NOT be
"fixed" to pass**:

1. **Genuinely-open-claim (~25)** — the assertion fails because the
   framework claim is genuinely open: m_p/m_n/Δ_pn residuals,
   `proton-mass-*`, `delta-lambda-*` (Δ_λ gate), `mmu-r9` (m_μ misses
   963×), `qbeta-*`, `level-k-binding`. These correctly record open
   problems; making them pass would be **fitting**. Drain = mark
   `auditOnly` / restate as a *conditional* assertion (banner per §3b-cond),
   NOT force a pass.
2. **Audit-meta caught a real violation (~10)** — `content-block-label-audit`
   (missing labels), `float64-leak-audit`, `hardcoded-literal-audit`,
   `fitted-labelled-canonical-audit`, `cal4-disguise-hunt`,
   `lean-ref-resolution-audit`, `onepb-status-dashboard`
   (all_witnesses_present). Each is a genuine discipline finding — its own
   investigation/PR.
3. **Stale / cache drift (~4)** — `hadron-knot-table` (known),
   `habiro-residue-a1` (cached_trM), `gram-h3-symbolic-regression`
   (4.4e-8, actually audit-only), `tr-m-atom-via-transfer`. Drain =
   regenerate (assertion-gated).

So "draining" is mostly **reclassification + per-audit investigation**,
not bulk passing — the gate's value is precisely separating honest-open
from regression. The classifier fix (this PR) is the first drain step.

1. Land the warn-mode CI step (visibility, no PR breakage).
2. Drain self-staleness: regenerate the genuinely-wrong witnesses
   (assertion-gated), starting with hadron-knot-table.
3. Drive `add_upstream` adoption on the mass/binding chain.
4. Add assertion-gating to the regenerate path.
5. Flip CI to `--self-strict`, then `--strict`.
6. (Optional) effectiveHash Merkle roots for single-pass transitive
   closure.

## Audit-suite scan-root rot (reorg silently disabled discipline audits)

Investigating the `float64-leak-audit` assertion failure surfaced a
*class* of bug: the discipline audits in `computations/audits/` scan
`HERE.glob("*.py")`. Pre-reorg they lived in the compute dir and scanned
their siblings (the whole compute tree); after the move into `audits/`,
`HERE.glob` saw only the audits dir — so each **passed vacuously** (false
green) and, for constant-policing audits, **false-flagged sibling audit
scripts** (which legitimately reference the constants they police). This
is the staleness-laundering pattern at the *audit* level: a stale
scan-root turns a discipline check green while it inspects almost nothing.

Fixed this PR (scan `HERE.parent.rglob`, skip `_deprecated` + `audits/`):

| Audit | scripts scanned | candidates surfaced |
|-------|----------------:|--------------------:|
| `float64_leak_audit` | 2 → 55 | 16 |
| `hardcoded_literal_audit` | 6 → 263 | 248 |
| `validation_as_input_audit` | 3 → 39 | 39 |

**Remaining candidates (same `HERE.glob`, need per-audit verification of
intent + exclusions — NOT a blind sed):** `canonical_script_input_audit`,
`guarded_off_audit`, `i2_probe_only_audit`, `incomplete_coverage_audit`,
`legacy_formula_audit`, `stale_probe_audit`, `witness_provenance_audit`.
(`fitted_labelled_canonical_audit` already uses `HERE.parent.rglob`;
`noncanonical_reentry_audit` uses `walk`.) Systematic follow-up.

The high post-fix counts (248, 39) reflect the audits' own broad matching
(a separate calibration concern); restoring SCOPE is the fix — an audit
scanning 6 files is worse than one honestly red.
