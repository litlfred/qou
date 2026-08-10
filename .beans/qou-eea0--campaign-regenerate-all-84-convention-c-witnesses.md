---
# qou-eea0
title: 'CAMPAIGN: regenerate all 84 convention-C witnesses under D and report total impact'
status: in-progress
type: task
created_at: 2026-08-10T01:15:27Z
updated_at: 2026-08-10T01:15:27Z
---


## Why this exists

The producer layer is fully convention D (`qou-9xla`, 178 actionable → 0), but
their committed outputs are not: **84 witness JSONs still carry convention-C
fingerprints**. Code and data disagree. Until this closes, the repo is in a state
where a reader cannot tell whether a given number is production or history.

Owner directive 2026-08-10: *"just do them all… I want to see total impact not
partial results"*, and *"work slowly diligently"*.

## Hard constraints

- **NEVER two producers concurrently in one checkout** (standing owner directive).
  The harness is strictly serial.
- **NEVER hand-edit a witness number.** Every value here comes from a producer run.
- The container is ephemeral and has already died mid-task twice in this arc, at
  ~1h each. The harness therefore writes **JSONL incrementally after every
  producer** and resumes by skipping what is already recorded. Losing an hour of
  runs to a restart is not acceptable when the fix is one append per producer.

## Method

For each producer, in order:

1. snapshot the witness (sha256 + extracted numeric fields)
2. run the producer with a per-producer timeout, capturing stdout/stderr
3. snapshot again
4. record: status, wall time, whether the C fingerprint cleared, per-field deltas
5. append one JSONL line — *then* move on

No commit until every producer has been attempted, so the impact is reported
whole rather than in fragments.

## What "total impact" means here

Not "84 files changed". The number that matters is how far each *physical*
quantity moves. The registry already records the expected order for migrated
channels — **195.8 ppm on β_Bor, −197 ppm on m_p** — so the report must give,
per witness, the largest relative change and what quantity it belongs to, and
must separate:

- **structural zeros** — `y_λ = 0` for `ℓ(λ) ≥ 3`. Not a "change", a collapse,
  and the thing convention D is *for*.
- **genuine shifts** — everything else, in ppm.
- **noise** — q₀-refresh at digit ~9 and timestamp churn, which must NOT be
  reported as convention impact. This bit me once already: a witness regenerated
  before its producer was migrated moved only at digit 9 and looked like a real
  result.

## Checklist

- [ ] harness written, resumable, serial
- [ ] dry-run on a known producer to confirm before/after capture works
- [ ] full run over all resolvable producers
- [ ] failures triaged: pre-existing breakage vs. breakage this migration caused
- [ ] 14 witnesses with no recorded `scriptFile` — find their producers or record why not
- [ ] impact report: per-quantity ppm, structural zeros separated from shifts
- [ ] commit witnesses + report together

## Orphan witnesses triaged (14 → 9 → 3 genuinely unowned)

The work list resolves a witness to its producer via `scriptFile`. 14 had none.
Two further resolution passes:

**Pass 1 — the `producer` key.** Five witnesses record their producer under
`producer` rather than `scriptFile`:

| witness | producer |
|---|---|
| `chi-neutron-h3-at-q0-50dps` | `chi_at_q0_via_hoefsmit_mpfr.py` |
| `chi-proton-h3-at-q0-50dps` | `chi_at_q0_via_hoefsmit_mpfr.py` |
| `binding-weight-markov-pinning` | `deltalambda/binding_weight_markov_pinning_probe.py` |
| `borromean-3body-cluster-sign` | `deltalambda/borromean_3body_cluster_sign_probe.py` |
| `mu4-rhoF-cluster-derivation` | `deltalambda/mu4_rhoF_cluster_derivation_probe.py` |

**Pass 2 — slug match on the basename.** Four more resolve to live producers:

| witness | producer |
|---|---|
| `alpha-k-jones-markov-h4` | `alpha/alpha_k_jones_markov_h4.py` (already in the run) |
| `e0-lambda-tryall` | `e0_lambda_tryall.py` |
| `ocneanu-param-from-fibre-dimension` | `ocneanu_param_from_fibre_dimension.py` |
| `y-lambda-wenzl` | `y_lambda_wenzl_bridge.py` |

**Genuinely unowned — 3, and each for a different reason:**

- `y-lambda-jones-markov`, `y-lambda-sdp`, `y-lambda-wenzl-bridge-numeric` —
  their producers are in `_deprecated/`. The witness outlived the script. These
  cannot be regenerated without un-deprecating, and probably should be **retired
  rather than regenerated**: a witness whose producer was deliberately retired is
  history, and history is allowed to be convention C provided it says so.
- `chi-*-h3-at-q0-50dps-matrix-m` (×2) — `producer: "rust-chi-q-via-gp-lossless"`,
  a **Rust binary**, not a Python script. Regenerating these needs the
  hecke-engine CLI, not this harness. Note the binary layer is exactly where
  `qou-j6il` found a stale artifact, so these want the convention gate applied
  before they are trusted.

So the harness's reach is 9 more producers than it first found, and 3 witnesses
are out of scope for it by nature rather than by oversight.

## Incident: three concurrent copies of one producer

Worth recording because the fix is now in the harness and the failure mode is
not obvious.

I launched the harness twice within a minute (the first launch appeared to have
failed because its log was missing; it had not). Both stepped through the
producer list. I killed both harnesses — **and that is where the real bug was**:
killing the harness left its producer child running, reparented to init. The
next harness then started the *same* script again.

Net effect: three concurrent `binding_k_enumerator.py` processes writing one
witness. Caught by looking at `ps` rather than by anything in the tooling.

No damage — every witness still parsed, the JSONL had no duplicate producer
records, and the 8 completed producers had all been run by a single harness
before the second launch. But that was luck, not design.

Two mechanisms added, because "I was careful" is not one:

- **`SerialLock`** — `O_EXCL` lockfile with a liveness check, so a second
  instance refuses to start and a lock left by a container death does not wedge
  the next run. Verified by launching a second instance and watching it refuse.
- **process-group cleanup** — producers now start with `start_new_session=True`
  and are killed via `killpg` on timeout, on error, and from `SIGTERM`/`SIGINT`/
  `SIGHUP` handlers. The harness can no longer abandon a running producer.

(The first attempt to *test* the signal path signalled the bash wrapper rather
than the python process and so proved nothing — noted so the test is not
mistaken for evidence.)
