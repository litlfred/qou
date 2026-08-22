---
# qou-7ot6
title: 'GAP: drain the 443 source sites carrying a stale CODATA edition'
status: in-progress
type: task
priority: normal
created_at: 2026-08-19T13:05:24Z
updated_at: 2026-08-22T09:53:42Z
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

## PROGRESS 2026-08-21 — PR #5423, two tranches

### Tranche 1: the constants modules (done)

`substrate/experimental_constants.py` and `qou_substrate/constants.py` now
read the registry instead of hardcoding. Five stale values removed, including
`M_N_MINUS_P_MEV` at 320 ppb under a *"direct CODATA 2022 value"* label.
`codata_2022_source` gained `M_N_MINUS_P_MEV`; the vintage audit is at
**9/9**.

**The catch worth remembering:** the registry's `M_N_MEV` is **AME-derived**,
not CODATA-direct, and that is load-bearing. `Q_β = m_n − m_p − m_e`, and AME
pins the *difference*. Both edition shifts are exactly `1.27e-6`, so it
cancels and Q_β is **invariant**. A first pass mixed the table's CODATA-direct
neutron with the 2022 proton and shifted Q_β by **+0.15 eV** — an artifact,
not a result.

**So: the drain's target is the REGISTRY, not the table.** The table is what
the registry is checked against. This is the single most important thing to
carry into the remaining work.

### Tranche 2: 12 consumer literals in 7 files (done)

Bare duplicates, several in files already importing `codata_constants` for
other symbols.

### Remaining, and the four exclusion classes

The bulk is `.md`/`.lean`/witness sites plus ~170 `.py` files whose literal is
in a **string or comment**. Before touching any of them, note that four
classes look identical to a grep and must NOT be drained:

1. **Window bounds** — `codata_masses.py:55-56`,
   `float(M_P_MEV) > 938.27200 and < 938.27220`. Not constants.
2. **Framework-derived look-alikes** — `rho_f_vol_binding_dashboard.py:27`,
   `M_P = 938.2720894273`, the *muon-anchored Hecke energy*. Resembles m_p;
   is not m_p.
3. **`# noqa: P31` with a written justification** — six sites. Someone
   adjudicated those; silently re-draining discards the adjudication.
4. **Test expectations** — `test_p2_integration.py:21` is 252 ppb off, which
   is not an edition shift. Changing it would falsify the test.

Plus one open identification: the deuteron / He-3 / He-4 masses in
`b_over_m_order_probe.py` and `knot-particle-generation.py` differ from the
CODATA table by 9–100 ppb, too large for an edition. Probably **AME** values
under a CODATA-shaped name. That needs identifying, not replacing.

## 2026-08-21 22:50 UTC — tranche a on PR #5423, rebased and clean

PR #5423 (`claude/codata-drain-7ot6a-2026-08-21`) carries tranche **a**:
the constants modules routed at the registry, 12 consumer literals in 7
files, and the light-nuclide identification. Rebased onto main (+170);
`mergeable_state: clean`; all blocking precision gates green.

Two witness conflicts during the rebase, both resolved by taking main's
copy and regenerating (never merging witness text). Both counts that
moved are main-side, verified by running the producer in a pristine
`origin/main` worktree rather than argued:

  mpf-import-time-dps-audit   literal_findings 1 -> 0 (main drained it)
  q0-anchor-consistency-audit Q0_ANCHOR_MISSING 1918 -> 1919
  q0-value-drift-audit        unchanged vs main

The PR body's older accounting said `literal_findings 0 -> 1`; corrected
in a comment on the PR rather than by a silent body edit.

One finding filed rather than fixed: `qou-r8zo` — the
`rho_f_vol_binding_dashboard` M_meas column is irreproducible from any
standard route (+-240 eV, 100-240 sigma). Values deliberately left
alone: the correct ones are computable but the intended provenance is
not establishable, and guessing would launder it.

Remaining: tranche **b** — the string/comment-resident sites, plus the
188 consumers minus the three exclusion classes (window bounds, test
expectations, deliberate determination choices).

## 2026-08-21 23:05 UTC — tranche b: the count itself was the defect

Re-measured before draining anything, and the first finding was in the
detector this bean is built on.

**The actionable queue is ~61, not 447.** Classified by whether the
literal is executable, the 448 `.py/.lean/.ts` sites split:

    CODE          61   executable -- can compute a wrong number
    PROSE        381   inside a comment or a string; inert
    ADJUDICATED    6   executable, carrying `noqa: P31`

So this bean's title ("drain the 443 source sites") over-states its own
scope by ~7x, and the scan's headline label was wrong for 87% of what it
counted.

**The direction matters more than the size.** Tranche a moved the count
447 -> 448 -- not a regression: a drain that replaces a stale literal
with a registry read and records the superseded value beside it lands in
PROSE. Counting prose as defects makes the number rise when the corpus
improves and rewards deleting provenance to bring it down. Only CODE
gates under `--strict` now.

Two defects in my own classifier, both recorded rather than quietly
fixed: a line-keyed first attempt under-counted code 53 vs 61 (a
trailing comment tarred the executable line), and an untracked-string
`.lean/.ts` path over-counted it (registry.ts:647 is a CODATA value
inside a `description:` string, reported as executable) -- the opposite
of the direction I had argued the crude path could err in.

Landed on #5423: `2e348e57e5`. `--self-test` covers 11 classifier
shapes + 4 marker cases; precision gates green.

**Remaining for the drain proper: the 61 code sites.** Dominant classes
are `938.27208816` / `939.56542052` (CODATA-2018 masses, mostly in
mass-theory `.lean`), `0.51099895` (truncated m_e) and
`137.035999084` (CODATA-2018 alpha-inverse). The alpha-inverse sites
are a deliberate determination choice per the tranche-a adjudication and
should be marked `noqa: P31` rather than changed.

## 2026-08-22 — tranche c on PR #5439: 61 -> 36 code sites

Drained the m_e (5 of 8), m_p/m_n (6) and alpha^-1 (3 of 6) groups.
Counts: CODE 61 -> 36, PROSE 381 -> 388 (rising, correctly), ADJUDICATED
6 -> 12.

**The `:leanval{precision=N}` rule added in tranche b was too permissive
and this drain caught it.** `precision=N` declares a deliberate
truncation; it says nothing about which EDITION the digits came from. As
written it would have excused `partition-sum-proton-residual.lean:59`,
where `precision=11` sits on the CODATA-2018 `938.27208816`. The
declaration is now CHECKED against the table value truncated to N digits.

Left deliberately, each with a reason in the commit: the three .lean
alpha^-1 sites (inside the conjecture machinery #5361 just re-scoped --
the live gap there is 468 ppb structural, not 1e-9 editions), the
`m_AME_MeV` field-name mismatch in recursive-atom-knot-atlas (renaming
has blast radius), and the two `electronMass_witness` proof-body mirrors
(correct declared truncations).

**Remaining: 36 code sites.** Not yet grouped -- next step is to re-run
`--strict` and classify them the way tranche c did, one literal-group per
commit with a per-site disposition.
