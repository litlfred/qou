---
# qou-cdh3
title: 'H3 (hygiene): regenerate the 14 convention-C witnesses — two hard gates first'
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-21T15:15:40Z
---

Parent: `qou-cdx1`. Successor to the `qou-eea0` cascade, which drained the bulk.

## Measured (`scripts/convention-c-witness-audit.py`, structural test, 2026-08-15)

**13 structural (825 dead-block entries) + 1 symbolic (14 expressions) = 14.**

```
computations/alpha/alpha-k-jones-markov-h12.witness.json              (70)
computations/chi-deuteron-h6-at-q0-50dps-matrix-m.witness.json         (7)  *rust
computations/chi-helium-3-h9-at-q0-50dps-matrix-m.witness.json        (25)  *rust
computations/chi-helium-4-h12-at-q0-50dps-matrix-m.witness.json       (70)  *rust
computations/chi-helium-4-h12-numeric.witness.json                    (70)
computations/chi-lithium-5-h15-at-q0-50dps-matrix-m.witness.json     (168)  *rust
computations/chi-lithium-6-h18-at-q0-50dps-matrix-m.witness.json     (375)  *rust
computations/chi-neutron-h3-at-q0-50dps-matrix-m.witness.json          (1)  *rust
computations/chi-proton-h3-at-q0-50dps-matrix-m.witness.json           (1)  *rust
computations/chi-tritium-h9-at-q0-50dps-matrix-m.witness.json         (25)  *rust
computations/derived-chi-catalogue.witness.json                        (2)
computations/probe-1b-li6-orthogonality.witness.json                   (9)
computations/tr-m-q-hecke-seminormal.witness.json                      (2)
computations/y-lambda-macdonald-telescope.witness.json         (symbolic, 14)
```

## The two gates — do not start a cascade without clearing these

1. **The `chi-*-matrix-m` family has no Python producer.** `qou-eea0` resolved
   them to `producer: "rust-chi-q-via-gp-lossless"` — a `hecke-engine` binary.
   That is exactly the layer where `qou-j6il` found a binary **silently
   returning convention C while its source read D**. Apply the convention gate
   to the binary *before* regenerating, or the regeneration launders C.
2. **`delta_lambda_2row_stratum_analysis.py` has never completed.** It consumed
   the full 2400 s timeout on every attempt and is first in topo order, so every
   cascade restart pays 40 minutes before producer 2. Diagnose or re-order.

## Standing constraints (from `qou-eea0`, all learned the hard way)

- **Never two producers concurrently in one checkout.** The harness has a
  `SerialLock` (`O_EXCL` + liveness) and process-group cleanup because killing a
  harness once left its producer child running, reparented to init, and a
  second harness started the same script — three concurrent writers on one
  witness.
- **Never hand-edit a witness number.** Every value comes from a producer run.
- **JSONL incrementally after every producer.** The container has died mid-task
  at ~1h more than once.
- **"C fingerprint cleared" is the wrong headline metric.** A witness can be
  fully migrated and still legitimately contain the string — an audit *of* C, a
  stored non-recomputed value, a preserved historical field. Count deltas by
  kind; treat surviving fingerprints as a triage queue.
- **Separate structural zeros from genuine shifts from q₀-refresh noise.**


---

## ⚠ Two constraints from #5209 (recorded 2026-08-16, `qou-2ixd` campaign)

**1. SIX of the tagged witnesses are CORRECTLY colour-blind and must NOT be
migrated.** Free words (`include_inter=False`), dineutron, diproton and single
nucleons have **no p–n bond to weight**, so colour-blind `χ` is the right answer
for them. A regeneration sweep that pattern-matches on filenames will migrate
them and be wrong.

The distinction is only visible from the WORD, not the filename: the sibling's
fix derives `convention_fingerprint` / `convention_label` in
`canonical_braid_crossings` from what a run actually builds
(`sigma:11+sigma_inv:7+averaged:4+averaged_weighted:1` for the deuteron) and
compares it on cache read. Use that, not a name pattern.

**2. The caches are the hazard, not the producers.** Nine committed witnesses
carry colour-blind `χ` for words that DO have a p–n interface, and no producer
is at fault — `atom_canonical_crossings` emits the right crossing every time.
`per_irrep_pole_deuteron_h6` returns on `CHI_CACHE.exists()`, and
`per_irrep_pole_atom` resumes keyed on **partition coverage alone**. Neither
knows which word produced the cached entries, so a pre-colour-weighting cache
looks complete forever. Recorded as **row 12** of the detector-blindness
taxonomy: the convention tag on those nine is *accurate about the bytes and
silent about the drift*.

**3. Cost, which may decide feasibility.** `δ(q) = (q−1)²(1−q⁻⁴)/3` turns a
scalar `−h/2` into a degree-8 rational function, so colour-weighted symbolic χ
is far more expensive: **~25 min at H₆** against ~155 s colour-blind, and
**tritium at H₉ reached 1 of 30 partitions in ~15 min**. At H₉ and above this
may not be feasible symbolically at all — which bears directly on this tranche's
existing gate about `delta_lambda_2row_stratum_analysis.py` never completing.


## A possible ~10× saving at H₁₂ — and the reason it may not apply (2026-08-16, from #5209/#5217)

#5217 proved, **all-`n` and sorry-free**, that at convention D
`y_λ = 0 ⟺ ℓ(λ) ≥ 3`, *identically in q*. For any consumer that only forms
`Σ_λ y_λ·χ^λ`, the three-or-more-row blocks cannot contribute at all:

```
  n=6    7 of 11 blocks dead
  n=9   25 of 30 dead
  n=12  70 of 77 dead      <- roughly a 10x saving
```

That would bear directly on the cost gate recorded above (colour-weighted
symbolic χ measured at **1525.9 s at H₆** against 0.5 s colour-blind, tritium at
H₉ at 1-of-30 in ~15 min, helium-4 at H₁₂ not attempted), and might make a
regeneration currently called likely-infeasible actually tractable.

**The catch, and it is decisive for these particular caches.** The two live
consumers are **per-irrep pole-order** analyses: they examine `χ^λ` block by
block *before* any weighting is applied, so a block with `y_λ = 0` is still a
block they read. `per_irrep_pole_deuteron_h6`'s own docstring singles out
**λ = (4,1,1) — three rows — as the unique pole maximiser**, which is exactly a
block the saving would discard.

So: **the saving is per-CONSUMER, not per-cache.** Anything downstream that
contracts to `Σ_λ y_λ·χ^λ` can skip the dead blocks; anything that inspects
blocks individually cannot, and the pole-order analyses are in the second class.
Do not apply it cache-wide on the strength of the n=12 ratio.


---

## WORKED 2026-08-21 — 14 → 5 → 2, and BOTH gates turned out not to apply

Claimed and worked today. Re-measured first (`scripts/convention-c-witness-audit.py`,
**unchanged since 2026-08-15** — verified, so none of the movement below is
detector drift).

### Starting position was already 14 → 5, not 14

| | this bean (2026-08-15) | on arrival (2026-08-21) |
|---|---|---|
| structural | 13 witnesses, 825 entries | **4 witnesses, 122 entries** |
| symbolic | 1 witness, 14 expressions | 1 witness, 14 expressions |

Of the 9 structural entries that had cleared before I started: **6 by
migration, 3 by deletion**, and the deletions are right — `chi-helium-4-h12-numeric`
was retired as the C orphan (`f933ce228`), and `chi-neutron-h3` / `chi-proton-h3`
were deprecated as A=1 leftovers (`6d5673374`). Per this bean's own constraint 1,
single nucleons have no p–n bond to weight, so **deprecating them beats migrating
them** — a sweep that pattern-matched filenames would have migrated them and been
wrong.

### Gate 1 is STALE — the hazard it names is not in the path

The gate says the `chi-*-matrix-m` family *"has no Python producer … a
`hecke-engine` binary … Apply the convention gate to the binary before
regenerating, or the regeneration launders C."* Resolved by reading the call
graph rather than the filenames:

- `computations/chi_at_q0_via_matrix_m_mpfr.py` **owns the family** and computes
  in `mpmath` at 50 dps (`NO f64 in compute path`).
- Rust appears **once**, at `:513`, as a *cross-check* —
  `abs(chi_mpf - chi_rust) < tol` — never as the compute path. So the
  `qou-j6il` binary-laundering hazard cannot reach these numbers.
- The real convention input is `_load_y_lambda` →
  `tr_m_wenzl_bridge_mpfr` → **`computations/y-lambda-mpfr-proton-witness.json`**,
  which the gate never names. Verified convention **D** *before* running
  anything: `z = 0.61268803714646525159…`, and every 3+-row weight is `≤1e-72`
  for n = 2…12.

So the caches held **stale pre-migration values, not laundered ones**, and the
right gate is "check the y_λ source witness", not "gate the binary".

### Gate 2 does not apply to this route

`delta_lambda_2row_stratum_analysis.py` is first in *cascade* topo order.
Invoking the producer directly does not enter the cascade, so the 40-minute
tax is not paid. Gate 2 stands for cascade restarts; it does not gate this work.

### Regenerated (`--fresh`, strictly one producer at a time, snapshotted first)

`--fresh` is **mandatory**, not hygiene: the q0 guard compares against the
**stored** q0, so a stale cache looks self-consistent and resumes its own values
forever.

| atom | H | time | partitions | cross-check | 3+row above `DEAD_TOL` |
|---|---|---|---|---|---|
| helium-3 | 9 | 67.7 s | 30/30 | 30/30 @ 1e-45 | 0 (max 5.274e-73) |
| tritium | 9 | 67.1 s | 30/30 | 30/30 @ 1e-45 | 0 (max 5.274e-73) |
| helium-4 | 12 | **in flight** | — | — | — |

Both cleared values match `y-lambda-mpfr-proton-witness.json` exactly, which is
the check that they came from the D source rather than being coincidentally small.

### ⚠ NEW COST DATUM — H₁₂ is far more expensive than H₉ on this path

helium-4 measured mid-run: **10 of 77 partitions in ~27 minutes**, and the
per-partition cost is climbing (the 10th landed at 15:36Z, the 11th was still
running 11 minutes later). H₉ did 30 partitions in 67 s. Naive extrapolation is
~3 h and that is optimistic, since the large-dim middle partitions are the
expensive ones.

This is a **different** cost axis from the one in the `#5209` note above (that
one is colour-weighted *symbolic* χ, measured at 1525.9 s at H₆). This is the
*numeric* matrix-M mpfr path, which was supposed to be the cheap one — and at H₁₂
it is not. Anyone planning an H₁₂-and-above regeneration should budget hours per
atom and run it detached, not inside a session.

### The symbolic hit is a FALSE POSITIVE — proved, not argued

All 14 flagged weights in `y-lambda-macdonald-telescope.witness.json` carry the
factor

```
1 - 1/((q**2 + 1)*(q**4/(q**2 + 1) - q**2 + 1))
```

and `(q**2 + 1)*(q**4/(q**2 + 1) - q**2 + 1) = q**4 - (q**4 - 1) = 1` **exactly**,
so the factor — and every weight carrying it — is identically `0`. Confirmed with
sympy: **14 of 14 algebraically zero, 0 nonzero**. The witness is *correctly
convention D*; its D-ness is simply spelled as an unsimplified vanishing factor.

**This is not a detector bug.** `scan_doc_symbolic`'s own docstring says a CAS
*"does not belong in a scan over a 7 MB witness, so the 3+-row test screens
syntactically and over-reports rather than under-reports"* — a deliberate,
documented choice, and the right default for a test whose failure mode was
silence. Added `--cas-verify` instead: an **opt-in** pass that runs the CAS only
over the handful already flagged, where the cost argument does not apply. Exit
code deliberately unchanged, so no gate flips on the flag. Selftest **16 → 22**,
including the negative cases that matter (the committed convention-C root's
`[1,1,1]` still flags; an unparseable expression returns `None`, never a verdict).

### The last structural hit is split out as `qou-j47t`

`derived-chi-catalogue.witness.json` (2 entries) is **not** a regeneration item.
Its builder now emits `y_lambda_at_zero="?"` for exactly those cells, but
`DerivedChiCatalogue.add` raises on duplicate keys and the builder *merges* into
the existing catalogue — verified read-only: both keys are already in `_index` of
the committed 342-cell witness, so a re-run raises on the first add, and a fresh
build would emit 12 cells against 342. There is no update path. Full analysis and
the unresolved `y_λ(0)` semantics question in `qou-j47t`.

### Where this leaves the tranche

- **cleared:** 11 of 13 structural (9 before today, 2 today), plus the symbolic
  hit shown to be a false positive.
- **in flight:** helium-4 (H₁₂).
- **split out:** `derived-chi-catalogue` → `qou-j47t`.

Not closing this bean while helium-4 is running.
