---
# qou-khue
title: m_n prediction moved 501 ppb in a drain commit on 2026-08-24, invisible because the canonical table had dropped its p/n rows
status: todo
type: bug
priority: normal
created_at: 2026-08-28T18:18:52Z
updated_at: 2026-08-28T18:19:47Z
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
