---
# qou-bvk7
title: Convention-C derived TRACE VALUES in live witnesses — invisible to both convention-C witness detectors
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T12:49:41Z
updated_at: 2026-11-17T11:39:37Z
parent: qou-cdx1
---

Parent: qou-cdx1. Surfaced while resolving qou-uabo; distinct from qou-pvem,
which is about the STRUCTURAL population (3+-row y_lambda, float64-noise
sub-class).

## The gap

`scripts/convention-c-witness-audit.py` has two tests:

  structural  a nonzero `y_lambda` on a 3-or-more-row partition
  symbolic    a half-integer power of q in a weight EXPRESSION

Both key on **weights**. Neither can see a witness that records a **derived
trace value** computed under convention C — `tr_M` is a number, with no
partition structure and no surviving square root.

## What turned it up

`qou-uabo`'s resolution cites `term6-full-pole-sum.witness.json` as "the
canonical one". It carries

    .data.atoms[2].tr_M_at_q0_polynomial = 0.3882864240747888
    .data.atoms[2].tr_M_polynomial.value_at_q0 = 0.38828642407478884856154551860407

`0.3883` is the **convention-C** deuteron `|tr_M|`; under D the same quantity is
`0.5751` (measured — docs/audits/2026-08-15-rho-k-co-casimir-stale-convention-c-
needs-d-refresh.md). The witness audit does **not** flag this file.

That caveat was written 2026-05-03, three months before the 2026-08-09 ruling, so
"canonical" there meant "canonical Markov trace as opposed to Schur-Weyl
weighted" — a distinction orthogonal to C-vs-D. It has since been read as
convention-canonical, which it never was.

## Measured, and DELIBERATELY NOT YET A COUNT

`grep -rl "0\.38828642" --include=*.witness.json` outside `_deprecated/` returns
**14 files**. That is a text match, not a verdict, and this campaign has three
published counts today that were wrong for exactly that reason. **Three sampled:**

| witness | field | reading |
|---|---|---|
| `deuteron-real-sdp` | `.data.tr_M_beta_D` | genuinely the deuteron trace |
| `applied-uniqueness-mass-table` | `.data.canonical_tr_M_q0_values.deuteron`, `.data.rows[2].tr_M_q0` | genuinely the trace — and **named `canonical`** |
| `cal4-disguise-hunt` | `.data.findings[33].value` | ambiguous; a hunt hit may legitimately quote a C value |

So the class is real and at least two live witnesses carry a convention-C trace
value, one asserting canonicity in its own field name. **The other eleven need
per-file reading before any number is published.**

## Why it matters more than the count

A block quoting `0.3883` and declaring one of these witnesses would pass the
witness-substitution axis (the value IS in the declared witness), pass the
convention-C witness audit (no 3-row weight, no sqrt), and pass R9/R10/R11 (those
read producers, not artifacts). Four gates, none of which can see it.

## Suggested approach

Do NOT add `0.38828642` as a fingerprint — that is the decimal-fingerprint
strategy this campaign already retired for being only as complete as someone's
memory. The general form is: a witness recording a `tr_M`-named field whose value
matches the C evaluation of that quantity at q0 and not the D one. That is
checkable against `closed_form_tau_M` without a list, the same way
`convention-c-producer-audit` moved from grep to AST.


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

Convention-C derived TRACE VALUES in live witnesses, invisible to both witness
detectors. Confirmed live by today's measurement: the two witness audits
disagree (0 structural vs 1 symbolic vs 1 fingerprint), which is exactly the
blind spot this bean names. Live.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

## 2026-10-10: the class drained 14 → 2, and BOTH survivors are now explained

Measured on `main` `fbc1f5f580`. This bean's own instruction — *"the other
eleven need per-file reading before any number is published"* — is now done.

    witness files containing 0.38828642, excl _deprecated :  2   (was 14)

**It is genuine drain, verified at the VALUE not the count.** All three files
this bean sampled still exist, and `deuteron-real-sdp.witness.json`'s
`.data.tr_M_beta_D` now reads **`0.5751722457697739`** — exactly the
convention-D deuteron `|tr_M|` ≈ 0.5751 this bean names as the D value. The
other two no longer carry the figure in any `tr_M`-named field.

### Survivor 1 — an ORPHAN DUPLICATE, and it is how the C value survived the drain

`computations/probes/option-e-deuteron-delta-lambda-probe.witness.json`:

| | `computedAt` | `results[0].B_pred_over_me` |
|---|---|---|
| the **orphan** (`computations/probes/…`) | **2026-07-19** | **`-0.3882864240747888767…`** |
| what the probe **writes** (`computations/…`) | 2026-10-10 (re-run) | **`-0.1519683392042316…`** |

Running `computations/probes/option_e_deuteron_delta_lambda_probe.py` writes the
**`computations/`** path, not the `computations/probes/` one. So the
`probes/` copy is written by nothing and has been frozen since 19 July, while the
live value moved **2.55×** away. And the frozen figure is the convention-C
deuteron trace to **rel 7.25e-17** — it is not a coincidental digit match.

My re-run changed the live copy by **provenance only**, so that artifact is
current and was reverted unmodified.

**Not a cwd-relative write.**
`computations/audits/cwd_relative_witness_write_audit.py` reports **0**
producers writing a CWD-relative witness (5370 `.py` scanned, selftest passes),
so that cause is excluded. The shallow clone shows **one** commit on each path,
so *when* the write target moved is **undetermined** — I am not guessing it.

### Survivor 2 — a C value frozen behind a CORRECT refusal, under a name that reads backwards

`computations/qbeta/qbeta-habiro-phase5q-dn-refactorize.witness.json`,
`.data.numerical_q0_cross_check.tr_M_D_q0_witness = 0.3882864240747888`, with
`allPassed: true`. Three things, all now written into the producer's docstring:

- **The `D` is DEUTERON, not convention D** — the producer's own lines 3/10/15
  say so (*"Phase 5q canonical (D − n)"*, *"the deuteron is…"*,
  `Σ_m Δa_m(D − n)`). A reader scanning field names for convention-D artifacts
  reads this one backwards.
- **"Convention" in this file means which braid/identity**, not C-vs-D — and on
  the C/D axis the Phase 5q side binds `z(q) = 1/(q^{1/2} + q^{-1/2})`, which is
  `z_C` exactly. So *"Phase 5q canonical"* is canonical about the identity route
  and **not** convention-canonical. That spelling is a detector-blind C form,
  which is why `convention-c-producer-audit.py` does not flag the file.
- 🛑 **The witness cannot be refreshed, so its `allPassed: true` is
  unfalsifiable.** The probe **refuses to run**: `_qou_lnog_preflight` raises
  `AmDifferenceInvalid` because the two witnesses' denominators differ, so `a_m`
  subtraction would build `d_X·t_X − d_Y·t_Y` instead of the pair difference
  (beans `qou-0ndb` / `qou-lnog`). **That refusal is correct and is not a
  crash.** It is the `qou-2cof` lesson in its stronger form: a producer that
  cannot run cannot report drift — and here the producer is *right* not to run,
  so the C-frame value is frozen until `qou-lnog` lands.

### A new detector blind spot — taxonomy row 55

This bean's title says the class is *"invisible to both convention-C witness
detectors"*. True, and there is a third: **`witness_producer_resolution_audit.py`
keys on CITATION, not on WRITE TARGET.** Its test is *"does the witness cite a
`.py` that exists"* — 3175 of 3510 `RESOLVED`, 0 `NAMED_BUT_MISSING` on `main`
— so an orphan whose cited producer exists but writes a *different* path reads
`RESOLVED`. Survivor 1 is exactly that, and it is why a 19 July C-frame copy
survived a drain that cleared the other twelve. `scriptFile` / `computation`
says who *claims* a witness, never who *writes* it.

### 🟡 One decision, not taken

**Survivor 1 is a duplicate at a path nothing writes.** Deleting it is not
labelling, so it asks (§🟥 ASK THE OWNER), and nothing in the corpus decides it:
`witness_producer_resolution_audit` calls it RESOLVED and there is no
orphan-witness policy I could find. Framed for the owner in the session report.
**Default if nothing is done:** the file stays, still frozen at the C-frame
value, still reading `RESOLVED` to the one audit that looks at it — and the live
artifact beside it is correct, so no published number is wrong today.

**Status: staying `todo`** on the deletion decision and on survivor 2, which is
blocked behind `qou-lnog`. The per-file reading this bean asked for is complete.

**2026-10-10 — survivor 1 moved (owner picked "move to fsh-guts").** The orphan `computations/probes/option-e-deuteron-delta-lambda-probe.witness.json` is now at `fsh-guts/deprecated/computations/probes/` on branch `cat/cat-harness/fsh-guts` (commit `8a0b888de8`), with a README saying why it is frozen. It is removed from main. The live copy at `computations/option-e-deuteron-delta-lambda-probe.witness.json` is untouched. Survivor 2 stays blocked behind `qou-lnog`, so this bean stays `todo`.
