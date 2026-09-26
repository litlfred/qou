---
# qou-eea0
title: 'CAMPAIGN: regenerate all 84 convention-C witnesses under D and report total impact'
status: in-progress
type: task
priority: normal
created_at: 2026-08-10T01:15:27Z
updated_at: 2026-09-08T07:45:34Z
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

## "Ran OK but the C fingerprint survived" — three different reasons

Not a single failure mode, and worth separating before the impact report treats
them as one:

**1. An audit OF convention C.** `audits/weight-factor-audit.witness.json` holds

```json
"check": "C8",
"name": "Markov parameter z = 1/(q^0.5 + q^-0.5) at q_0",
"computed_z": "0.49932033418369445241344268025766630375194816404153194527617"
```

This is not a stale production number — it is a check that deliberately
evaluates the C formula. The *check itself* is now auditing the wrong
convention, which is a real defect, but a different one: the fix is to migrate
the audit's C8 criterion, not to regenerate a number. `changed=False`, as
expected, since the formula is written into the audit.

**2. A stored value the producer does not recompute.**
`bond-extensivity-equal-weight.witness.json` carries `f_bond.pp =
0.4993203341836944`. The producer ran clean and changed nothing
(`changed=False`, 0 deltas), so this value is stored rather than derived on each
run. That a *bond fraction* equals `z_C` to sixteen digits is not a coincidence
and wants explaining on its own terms — flagged, not assumed.

**3. A preserved historical field.**
`binding-k-enumerator.witness.json` has `stabilization_z: 0.4993203341836945`
sitting immediately beside `historical_markov_at_braid`. The producer did rewrite
the witness (41 deltas) but carries this section through deliberately.

**Consequence for the report:** "C fingerprint cleared" is the wrong headline
metric on its own. A witness can be fully migrated and still contain the string,
legitimately. The report must count *deltas by kind* and treat surviving
fingerprints as a triage queue rather than a failure count.

## Run notes

Producer runtimes are heavily skewed — `bond_extensivity_equal_weight` 0.8 s,
`binding_k_enumerator` 452 s, `delta_lambda_2row_stratum_analysis` hit the 600 s
timeout. Budgeting by average would have been wrong; the timeout is doing real
work and timed-out producers are recorded as such rather than silently skipped.

---

## REOPENED: the work list was built on the wrong test

The impact report published under this bean is **not total**. The work list
selected witnesses by grepping for known convention-C decimals —
`0.49932033418369`, `0.41539579536`, `0.2809296`, `0.02274491`. Those are the
`n = 3` values. A witness computed at `n = 6`, `9` or `12` contains none of them.

| | |
|---|---|
| fingerprint-detected | 46 |
| structurally convention C | 53 |
| overlap | **12** |
| **missed** | **41** |

The missed set is the nuclear layer: deuteron at `H₆`, helium-3 at `H₉`,
helium-4 at `H₁₂`, the `a_K` LP duals, the `binding-a3plus` assemblies.

It surfaced only by accident. Fixing the co-Casimir producer to use
`live_channels` made it print `live channels = 11 of 11 (dead: [])` — impossible
under convention D at `n = 6`, where 7 of 11 must be dead. The weights came from
an upstream witness (`rho-k-h3a-refinement.witness.json`) that is convention C
and carries **no fingerprint at all**.

Two lessons, and the second is the one worth keeping:

- **Producers read each other's witnesses.** A stale upstream witness
  propagates into a freshly-migrated downstream producer, and the downstream
  output looks clean. Migration order matters, and the dependency graph between
  producers and witnesses is not currently written down anywhere.
- **A detector built from a list of known values can only find what is already
  on the list.** The fingerprint test could not have found these no matter how
  carefully it was run, because the constants it looks for do not occur at
  `n > 3`. That is not a tuning problem.

### The replacement test is structural

> A witness recording a nonzero `y_λ` on a three-or-more-row partition is
> convention C — at any `n`, whatever numbers it contains.

A property of the physics (Schur–Weyl on a two-dimensional fibre), not of a
decimal expansion, so it needs no maintained list.
`scripts/convention-c-witness-audit.py`, selftest 7/7, including the
underscore-encoded partitions in `binding-a3plus-*` that a naive parse drops.

`work_list()` in the regeneration harness now applies both tests. Pass 2: 54
producers, 22 not previously run.

### Orphans after the structural pass — 14

| resolution | count | note |
|---|---|---|
| live producer, by slug | 3 | `alpha_k_jones_markov_h4`, `e0_lambda_tryall`, `ocneanu_param_from_fibre_dimension` |
| producer in `_deprecated/` | 2 | witness outlived the script — retire rather than regenerate |
| **Rust binary** | 4 | `rust-chi-q-via-gp-lossless`, `matrix-m-chi-q-via-gp` |
| genuinely unresolved | 5 | `chi-dineutron-h6`, `chi-diproton-h6`, `wenzl-y-lambda-h9`, `wenzl-y-lambda-h12`, `y-lambda-jones-markov` |

The four Rust-produced ones matter more than their count: that is the layer where
`qou-j6il` found a binary silently returning convention C while its source read
D. They should not be regenerated until the convention gate has been applied to
whatever binary produces them.

## Orphan drain complete (2026-08-11)

Orphan `y_λ` witnesses: **12 → 0**.

- **`chi-dineutron-h6` / `chi-diproton-h6`** re-derived in place (`14e8da5fd`).
  They have no producer — absent from `chi_at_q0_via_hoefsmit_mpfr`'s `ATOMS`,
  and nothing else writes them. Safe to redo from the file itself because
  `χ^λ_q(β)` is a **character**, independent of the Markov parameter `z`; so
  every `chi_lambda` survives the convention change and carries enough to redo
  `y_λ`, `contribution` and `tr_M_at_q0` consistently.
- **`y-lambda-sdp`** migrated (`240b5e3e8`) after *proving* the positional
  `y_ls` pairing rather than assuming it: `tr(1) = Σ dim_λ y_λ = 1` on the
  **stored** convention-C values is order-sensitive (dims differ per partition)
  and true of any Markov trace. Passes at every `n ∈ 2..6` to 1e-16.

**Result worth keeping:** that last witness's own question changes answer. It
exists to test whether the Frobenius system admits a *non-negative* solution.
Under C it does not — `n = 4, 5, 6` carry negatives, to `-8.4e-4`, and the file
records `positivity_holds: false`. Under D it does, exactly: every `ℓ(λ) ≤ 2`
weight is strictly positive (`n − 2k + 1 ≥ 1`) and every `ℓ(λ) ≥ 3` weight is
exactly zero — no slack, no tolerance. Support is `⌊n/2⌋+1` per table, the
two-row count. The C-era violators (n=6 indices 6, 8, 10 = `[3,1,1,1]`,
`[2,2,1,1]`, `[1⁶]`) are all partitions D sends to zero.

Remaining orphans: **4** Rust-produced `chi-*-matrix-m` files, which need the
`hecke-engine` CLI rather than a Python producer.

## Merged with main; cascade restarted on the merged tree (2026-08-11)

The branch was 1575 commits behind and un-mergeable. 37 conflicts: 32 witnesses,
`.gitignore`, `regenerate_y_lambda_mpfr.py`, the harness journal, `.work`.

**Both code conflicts went to main's side, and one of them is a genuine
independent-discovery case.** Main found the *same* bug this branch did in
`regenerate_y_lambda_mpfr.py` — the script `sympify`'d the convention-C symbolic
witness — and fixed it **better**: it changed the *source*, calling the module's
numeric entry point `y_lambda_wenzl_bridge_numeric` rather than opening the JSON
directly. That matters because the guard (`_cached_symbolic_agrees`, `qou-wgta`)
lives on that entry point and never ran for a caller that read the file itself.
Took main's evaluation path; kept this branch's `--anchor both` default (the
coverage defect: producer owns two caches, wrote one, exited 0) and re-applied
the `qou-u2jg` pointer for why `z_D` is forced.

`.gitignore`: main anchors every pattern with a leading slash, because an
unanchored `_deprecated/` matches at **every** depth and was silently capturing
`computations/_deprecated/` (1,449 tracked files). Directly relevant — this
branch deprecated `binding_k_enumerator` there. **Checked rather than assumed:**
both files are tracked (`626f332b`); `git mv` preserves tracking and ignore
rules never untrack, so nothing was lost.

32 witnesses took ours then re-derive. Every one declares a producer, so none is
a hand-resolution — they are this campaign's D outputs against main's
independent C regeneration, which the standing directive says to ignore.

**The float64 red was stale tooling, not a regression.** `a-K-via-lp-dual-full`
measured 395 → 862 here. Main has since landed an owner-approved LP-dual
carve-out (`0c1917b72`) naming that exact file: 801 of its 867 floats are solver
output, f64 by construction, excused **and counted**. The ~66 the carve-out
deliberately does NOT hide — the probe's own results — are the real residue and
are still open.

Post-merge: Lean re-verified (both files exit 0, six declarations sorry-free);
cascade restarted, 36 producers / 30 to run / 4 orphans.

**Persistent time sink:** `delta_lambda_2row_stratum_analysis.py` has consumed
the full 2400 s timeout on every attempt and has never completed. It is first in
topo order among the remaining, so every cascade restart pays 40 minutes before
producer 2. Undiagnosed.

## `--impact-vs-main` — the gate, run 2026-08-15

12 witness files differ from `origin/main`. `delta kinds: q0_refresh=2, shift=166`.
`convention-D collapse: 0` — expected, since none of the 12 is a `y_λ` table;
the weights that collapse to exactly zero already landed via #4928.

**Provenance caveat, stated by the tool itself:** 0 of 12 declare a
`markov_convention` field, so the work-list count is a LOWER BOUND. A trace or a
derived scalar looks identical under either convention; only the producer knows.

### The result worth keeping — and it is not mine

`log-delta-categorical-derivation` compares three weight forms in the unified
curvature-rank mass formula across {D, T, ³He, ⁴He}. Convention D collapses one
of them to near-constant:

| form | max/min C → D | mean log abs ratio C → D | |
|---|---|---|---|
| `y_lambda` | 207.61 → 85.89 | −4.4093 → −3.7645 | improved, still bad |
| `w_lambda` | **43.46 → 1.557** | **−0.8700 → +0.0568** | **near-constant** |
| `identity` | 4.64 → 5.513 | 2.8291 → 3.3562 | WORSE |

The probe's own verdict now reads *"PROMISING — w_lambda gives max/min = 1.56
(close to constant)"*.

**Why this is more than menu-picking.** The improvement is *within* the `w_λ`
form (43× → 1.56× under the same form), not a switch between forms, and the
shift is **discriminating rather than uniform**: `identity` got worse, `y_lambda`
improved but stays two orders out. Only `w_λ` collapses.

**Why it is still only "promising".** A 1.56× spread is not 1.00; the formula
predicts a constant. Three forms are on the table, and one landing near unity
deserves the fitted-shape question even when the mechanism is not a fit. This is
a probe verdict, not a derivation.

**Provenance: this did not come from my edits.** My only change to that producer
is line 166, the *recorded* `z_mark` parameter; its compute (line 90) was already
convention D on `main`. The 46 deltas came from the upstream tables moving. So
it is an independent signal from a probe that was not designed to test
conventions.

## 2026-09-08: canonical ledger for the convention-C excision family is qou-wgta (the P0 excision tracker; owner-ruling milestone qou-cdx1, S2 science blocker qou-cds2); see docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 2 / §7.3 C3. Nine trackers, previously linked only cds2↔8iru and htsi→t9r1, now all point there.
