---
# qou-7ot6
title: 'GAP: drain the 443 source sites carrying a stale CODATA edition'
status: todo
type: task
created_at: 2026-08-19T13:05:24Z
updated_at: 2026-08-19T13:05:24Z
---


## Context

Found by [`codata_corpus_literal_scan.py`](../computations/codata_corpus_literal_scan.py)
(PR #5302). The full site list is in
`computations/codata-corpus-vintage-scan.witness.json`; the analysis is
[`docs/audits/2026-08-19-codata-edition-straddle-corpus-sweep.md`](../docs/audits/2026-08-19-codata-edition-straddle-corpus-sweep.md).

**447 SOURCE sites** (`.py`/`.lean`/`.ts`) hand-type a CODATA constant from an
earlier adjustment — full-length, not truncated, so `codata_truncation_audit`
cannot see them. Each is 3–4.5 σ from the committed 2022 table.

## What the drain is

Not a find-and-replace. For each site:

1. Replace the literal with an import from the canonical registry
   (`codata_2022_source` / `codata_constants`), which is already correct.
2. **Re-run the producer** and regenerate its witness.
3. Report which numbers moved.

## What it is NOT

- **Never edit a committed witness to match the table.** A witness records
  what a producer actually computed. `RECORD` sites (1526) are history; the
  fix is at the producer.
- Not an idle-pass sweep. Re-running 443 producers is a large announced
  tranche with its own scope.

## Two outliers to triage separately

- `3727.379378` (m_α, 18 sites) — 9.068 ppb, **28.2 σ**. Two editions back.
- `137.035944` (1/α, 18 sites) — 402.6 ppb, **2630 σ**. Not any CODATA
  edition; something else is happening at those sites.

## Scope

(a), scope-limited. No physical conclusion moves — offsets are ~1.3–1.5 ppb,
an order of magnitude under the μ–p tension. The value is that the corpus
stops disagreeing with itself.

## RE-SCOPED 2026-08-19 — split in two before starting

`producer_importability_audit` landed on main: of 2132 producers, **113 cannot
be imported at all**. The drain's method is *fix the literal → re-run the
producer → regenerate the witness*. For an unimportable producer that method
does not exist, so this is two tranches, not one:

- **7ot6-a** — source sites whose producer imports and runs. Mechanical.
  Start here.
- **7ot6-b** — sites inside the 113. **Blocked**: importability first. The
  stale CODATA literal is the lesser defect at those sites.

Make the split from the two witnesses before touching anything:
`codata-corpus-vintage-scan.witness.json` (the sites) ∩
`audits/producer-importability-audit.witness.json` (the 113).

**The forbidden shortcut, stated because 7ot6-b is where it tempts:** do NOT
edit a committed witness to match the table when its producer will not run. A
witness records what a producer actually computed.

## Upstream of this: qou-m9xp

`q-pinning-50-digit.witness.json` declares `q0Anchor: muon` with muon numbers
while `calibration_inputs.anchor` says `m_p/m_e`. Correcting a producer's
CODATA literal while it reads a self-contradicting pin file fixes the smaller
of its two errors. Prefer m9xp first for any site that reads that witness.

## Done, not part of the drain

The α_EM literal `137.035944` (2 producers) — a muon/proton **layer straddle**,
not a stale CODATA edition. Fixed on PR #5302. My "2630 σ outlier" triage of it
was wrong; see the audit note's addendum.

## Still open, small

~9 doc/content sites quote α⁻¹ "derived to 399 ppb"; the current proton-pinned
value is **468 ppb**. `DERIVATION-STATUS.md`, `observable-sector-tracker.md`,
`em-coupling-chern-simons.md`, `em-coupling-projection-table1-data.md`, three
audit docs. Content blocks need `qa-sweep`, so filed rather than half-done.

---

## RE-SCOPED AGAIN 2026-08-21 — measured, and my earlier split was wrong twice

The a/b split above was written from the *headline* numbers without
intersecting the two witnesses. Doing that intersection changes it materially.

### Correction 1 — sites vs files

"443/447 source sites" is **sites**, not files. The scan reports **447 sites
across 220 distinct files**. The drain's unit of work is a file (fix literal →
re-run producer → regenerate witness), so **220** is the number that matters.

### Correction 2 — the blocked tranche is 2 files, not 113

I wrote that 113 unimportable producers split the drain into a mechanical
tranche and a blocked one, implying the blocked half was large. Intersecting
`codata-corpus-vintage-scan.witness.json` (source files) with
`audits/producer-importability-audit.witness.json` (the 113):

    scan SOURCE files                : 220
    unimportable producers (audit)   : 113
    INTERSECTION                     :   7

Of those 7, five fail only on `PYTHONPATH` — `_precision` (×4) and
`q_parameter` (×1). Verified by importing each with
`PYTHONPATH=computations:computations/substrate:tools/qou-substrate/python:tools/pyhecke/python`:
**all five import cleanly.**

| file | cause | genuinely blocked? |
|---|---|---|
| `alpha_em_4pi_fixed_point_solve.py` | `_precision` | no — imports with PYTHONPATH |
| `alpha_em_4pi_q0_sensitivity.py` | `_precision` | no |
| `alpha_em_rt_phase3_schwinger_derivation.py` | `_precision` | no |
| `alpha_em_rt_shadow_world_symbolic_phase1.py` | `_precision` | no |
| `b_over_a_evaluator.py` | `q_parameter` | no |
| `compound_shift_nf.py` | `AttributeError` | **yes** — a real defect |
| `m_tau_complex_volume_search.py` | `snappy` missing | optional dep, installable |

### Revised split

- **7ot6-a — 218 files.** Producer imports (possibly needing `PYTHONPATH`).
  This is essentially the whole drain.
- **7ot6-b — 2 files.** `compound_shift_nf.py` (genuine `AttributeError`) and
  `m_tau_complex_volume_search.py` (needs `snappy`). Neither is a reason to
  stage the drain.

### What this means for sequencing

The importability finding does **not** gate this bean. It was worth checking —
the method genuinely does not exist for an unimportable producer — but the
overlap is two files, so the drain can proceed as one tranche with those two
carved out and handled separately.

**The forbidden shortcut still stands**, and now applies to exactly two files:
do NOT edit a committed witness to match the table because its producer will
not run. Fix the producer (or install the dep) and re-run it.

### Note on the 113 itself

It is largely an environment artifact rather than 113 broken producers: 72 are
`ModuleNotFoundError: pyhecke` and 9 are optional deps (matplotlib etc.).
That is a fact about the audit's run environment, not about the corpus. Worth
knowing before anyone cites "113 unimportable producers" as a corpus health
figure — including me, who did.
