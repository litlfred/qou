---
# qou-khue
title: m_n prediction moved 501 ppb in a drain commit on 2026-08-24, invisible because the canonical table had dropped its p/n rows
status: todo
type: bug
priority: normal
created_at: 2026-08-28T18:18:52Z
updated_at: 2026-09-14T19:42:26Z
---

## Found 2026-08-28, by restoring the p/n rows (qou-7e1t option 3)

The canonical mass table's `--method` default was `branching`, which is
inapplicable for A < 2, so p and n were dropped from every run. Putting them
back immediately surfaced this.

`canonical_mass.neutron_mass_mev()` returns **939.5658930679812**, i.e.
**+501 ppb** against CODATA 939.56542194. The proton, from the same facade, is
**-0.003 ppb**. Only the neutron leg moved.

## Traced to a single commit

`canonical_mass.py` itself has not changed since 2026-08-14, so this is import-
cone drift, not a code edit. The facade reads
`computations/m-p-substrate-identity-50dps.witness.json`, and that file was
rewritten by

    4f715fc970  2026-08-24  drain(tranche 1): 28 of 93 — and the population
                            rate is 30%, not the 45% I reported

Fields that moved in that commit:

    /data/predictions/m_n_MeV
       939.5654227645324356210258  ->  939.5658930679811464936213
    /data/codata_comparison/m_n_residual_ppm
       0.00238890489858            ->  0.501431800431          (2.39 ppb -> 501 ppb)
    /data/predictions/M_N_MeV
       938.9187560959283496741912  ->  938.918991247652705110489
    /data/neutron_diagnostics/m_n_flavor_split_residual_ppm
       -1.75778134226              ->  -1.75929267662

Note the CODATA REFERENCE also moved in the same commit
(`m_n_codata_MeV` 939.56542052 -> 939.56542194, ~1.5 ppb). That is a table
update and is far too small to explain the residual. The PREDICTION moved by
0.00047 MeV, which is the 501 ppb.

## WHICH VALUE IS CORRECT IS **NOT** ESTABLISHED HERE

Do not read this as "the drain broke m_n". Two readings are open and this bean
does not choose between them:

1. **Regression** — the drain changed a number it should not have, and the
   neutron prediction is now 210x worse.
2. **Unmasking** — the OLD 2.39 ppb was itself an artifact (float64 padding
   landing near CODATA is exactly the class that drain family targets), and the
   new value is the honest one. A 2.39 ppb agreement on a quantity AGENTS.md
   lists among the FAILING L2 observables deserves suspicion on its own.

Reading 2 is not idle: `m_n` is one of the five observables the precision-goals
table records as missing the 100x target, so a near-CODATA m_n was anomalous
BEFORE this commit, not after.

Deciding needs the drain's own rationale (what did tranche 1 change, and was
`m-p-substrate-identity-50dps` in its intended scope?) and a check of whether
the pre-drain value was reproducible at full precision.

## Why nothing caught it

The p/n rows had been absent from `canonical-mass-table-extended.witness.json`
since the `branching` default was introduced, so the artifact that would have
shown a 501 ppb neutron did not contain a neutron. The projection
`low-isotope-mass-table.witness.json` still carried a stale p/n pair from
2026-08-15 — it was pointing at a canonical witness that no longer existed
(that is this bean's sibling defect, qou-7e1t's "second, separate defect"), so
it displayed the OLD 0.88 ppb while main's facade returned 501.

Two artifacts disagreed about a headline observable by 570x, and neither was
wrong on its face: one had no neutron row at all, the other had a correct-
looking row computed from a vanished source.

## Next step

Read `4f715fc970`'s full diff and its bean, decide reading 1 vs 2, and either
restore the pre-drain value at the producer or record 501 ppb as the honest
m_n and update the L2 dashboard note accordingly.


--------

## RESOLVED, and I was wrong about the shape of it (2026-08-28, same day)

Both readings above are wrong, and so was the alarm I raised on the way. The
answer is neither "the drain broke m_n" nor "the drain unmasked m_n".

### Fact 1 — the value is reproducible; the drain did not corrupt anything

Re-ran `m_p_substrate_identity_50dps.py` on current main:

    m_p_MeV : REPRODUCES exactly
    m_n_MeV : REPRODUCES exactly   (939.5658930679811464936213)

So +501 ppb is what the code genuinely produces. Reading 1, in the sense of a
corrupted write, is refuted. The drain commit `4f715fc970` re-ran the producer
and kept the result, which is what it says it did.

### Fact 2 — I claimed the L2 dashboard was stale. It is NOT.

I found `per-observable-100x-status.witness.json` still reporting
`m_n err_ppb 0.9029 / miss_factor 176.7` and concluded the headline precision
artifact was carrying a pre-drain number. **Wrong.** Re-ran its producer:
every row is unchanged, m_n included. It reproduces 0.9029 on today's tree.

### Fact 3 — what is actually true: TWO LIVE ROUTES, disagreeing 555x

    canonical_mass.neutron_mass_mev()      939.5658930680   +501 ppb
      <- m-p-substrate-identity-50dps.witness.json (flavour-split identity)

    per_observable_100x_status.py "Path C" 939.565422788    +0.9029 ppb
      <- m_n = m_p + Q_beta + m_e  (categorical, no flavour split)

Both reproduce on current main. This is **deliberate and documented in the
source** — `per_observable_100x_status.py:533` introduces Path C, and its own
comment says it puts "m_n at 0.24 ppm (8x better than the substrate-identity's
2 ppm)". So the dashboard knowingly prefers the categorical route.

It is therefore NOT a hidden inconsistency, and this bean should not be read as
one. (Note in passing: that comment's "2 ppm" matches neither the pre-drain
0.00239 ppm nor the post-drain 0.501 ppm, so it is stale in its own right and
worth a look, but it is a comment, not a computation.)

### The live consequence, which IS mine

Restoring the p/n rows (qou-7e1t option 3) made
`canonical-mass-table-extended.witness.json` carry an `n` row sourced from
`canonical_mass` -> **501 ppb**, while `per-observable-100x-status.witness.json`
reports the same observable at **0.9029 ppb**. Two committed production
artifacts now disagree about a scored observable by 555x, on their face, with
no note in either saying they use different routes.

Before my change the mass table had no `n` row at all, so the disagreement was
unstatable rather than absent.

I am NOT proposing to drop the row again — the row's `tr_M` is legitimate, and
its mass column is governed by the absolute-mass excision anyway (`qou-exam`:
absolute mass is not a claim, so `prediction_MeV` there is a rendering). But a
reader diffing the two artifacts will see a contradiction and deserves a
pointer.

### Next step (narrow, and no longer urgent)

Decide which route the canonical mass table's nucleon rows should cite, and say
so IN the witness — a `prediction_route` field naming "substrate-identity" vs
"path-C" would make the 555x self-explaining instead of alarming. That is a
labelling change, not a physics one, and it is the whole of what is left here.

The physics question — why the flavour-split identity sits 555x off the
categorical route — is real but is not this bean's, and is not new: it predates
the drain by however long the two routes have coexisted.

## 2026-09-08 — C4 of the programme audit (docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §2, §7.3): two m_n values are live on main — the facade witness m-p-substrate-identity-50dps (2026-08-29) carries Q_beta = 0.78280469 (+602 ppm, the N2 form at z_D) and m_n at +501 ppb, while per-observable-100x-status (2026-09-07) carries the c_k-cache Q_N2 (1279 ppb, convention C, z = 1 inadmissible) and m_n at 0.903 ppb / 176.7x — a factor ~550 apart, both Path C m_n = m_p + Q_beta + m_e. Owner decision 2026-09-08 (qou-99qc): epsilon := augmentation, base 0.8798906 MeV (+12.470 %). Both witnesses are therefore to be re-scored on the augmentation base and stamped with functional + frame; until then neither m_n is canonical. Not done in this session (producer re-run under D; ask-before-change).

## 2026-09-14 — the closing entry names the SUPERSEDED base, and the 555x has reversed

Two corrections, both measured on `main` `17003000fe`. Nothing re-run, nothing
regenerated.

### 1. 🛑 The 2026-09-08 entry records the owner's FIRST selection, not the ruling

It says: *'Owner decision 2026-09-08 (qou-99qc): epsilon := augmentation, base
0.8798906 MeV (+12.470 %). Both witnesses are therefore to be re-scored on the
augmentation base.'*

**The augmentation was superseded the same hour.** AGENTS.md (line ~2310) records
the sequence verbatim:

> 🟧 OWNER RULING 2026-09-08 (**final**, same day) — ε is the MARKOV TRACE AT
> `z_D = q³/(q²+1)`, i.e. option C … the owner first selected the augmentation on
> an option that carried the agent's recommendation; the same hour `13bb8243d8`
> showed the augmentation IS the Markov trace at `z = q`, so the choice is *which*
> Markov parameter, and under D7 the consistent point is `z_D` … **the owner chose
> `z_D`.**

Base **0.4447004 MeV, −43.157 %**, not 0.8798906 / +12.470 %. `qou-99qc` carries
both rows (lines 225-226).

**This matters because the entry is an instruction.** An agent acting on it would
re-score both witnesses onto a base the owner did not choose. Corrected here;
corpus-derived, so no gate.

### 2. The 555x is stale — and the comparison has REVERSED SIGN

Measured today:

| artifact | m_n | err | computedAt |
|---|---|---|---|
| `per-observable-100x-status.witness.json` | 939.434944688 | **1.389e+5 ppb** (2.718e+7x) | 2026-09-13 |
| `m-p-substrate-identity-50dps.witness.json` | 939.5658930678 | **501.43 ppb** | 2026-08-29 |

    bean's recorded pair:  501 ppb (subid)  vs 0.9029 ppb (dash)  -> 555x, dashboard BETTER
    today:                 501 ppb (subid)  vs 1.389e5 ppb (dash) -> 277x, dashboard WORSE

**The dashboard has been re-scored on the ruled `z_D` base; the substrate-identity
witness has not** (its `computedAt` predates the ruling by ten days). That is the
live asymmetry, and it is exactly the half-done state the 2026-09-08 entry
predicted — one of the two re-scored, the other not.

### What this does and does not change

- **The bean's structural finding stands**: two committed production artifacts
  report the same scored observable from different routes with no field saying
  so, and the `prediction_route` labelling proposal is still the right narrow
  fix. It is now *more* warranted, not less — the gap is 277x and the arithmetic
  reads the opposite way round from the last entry.
- **The old justification is gone.** The bean records the dashboard as
  *'knowingly preferring the categorical route'* because its own source comment
  cites a better residual. On today's tree that route is **277x worse**. Note
  separately that ranking routes by residual is the selection-against-the-target
  the anti-fit directive forbids, so that was never a licit reason — it is now
  not even a true one.
- **Do NOT read 501 ppb as the better answer.** Per the same directive, the
  substrate-identity route being closer to CODATA is a diagnostic, not evidence
  for it; and its witness is simply **un-re-scored**, which is why it sits where
  it does.

### Still open, unchanged

Re-scoring `m-p-substrate-identity-50dps` onto the ruled `z_D` base is
`qou-99qc`'s arc and a producer re-run — gated, not done here. The labelling fix
is still the whole of what is narrow.
