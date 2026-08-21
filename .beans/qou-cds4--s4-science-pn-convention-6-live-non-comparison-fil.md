---
# qou-cds4
title: 'S4 (SCIENCE): p/n convention — 6 live non-comparison files + 28 witnesses off bring_color_weighted'
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-19T21:20:52Z
---

Parent: `qou-cdx1`. Ruling R3: `pn_convention="bring_color_weighted"` is
canonical.

## Measured 2026-08-15 (live Python assignments, excluding `_deprecated/`)

| value | assignment sites |
|---|---|
| **`bring_color_weighted`** (canonical) | **16** |
| `chi_lambda_braid` | **9** |
| `strict_averaged` | **6** |

83 files mention `pn_convention` overall (`.py`+`.json`+`.md`).
**28 committed witnesses** record a non-colour-weighted `pn_convention`.

## R3 is largely already true

`bring_color_weighted` is already the default in the production path:
`closed_form_tau_M.py` (×4) and `mass_at_3A_proper.py`. R3 makes it canonical
and puts the alternatives on notice.

## The 8 live Python files off-canon

```
computations/_habiro_coefficient_extract.py
computations/atomic_tr_m_helium4_canonical.py
computations/binding_bring_enhancement_compare.py      <- name says comparison
computations/binding_canonical.py                      <- READ THIS FIRST
computations/binding_combiner_markov_peel_fallback.py  <- PN_CONVENTION = "strict_averaged"
computations/chi_monotone_transfer.py
computations/closed_form_tau_M_verification_phase5q.py
computations/iterative_knot_builder.py
```

**`binding_canonical.py` first.** A file with `canonical` in its name assigning a
non-canonical p/n convention is either a naming defect or a real one, and the
two need different fixes.

`*_compare` and `*_fallback` are plausibly legitimate under R3 — a **labelled**
comparison against a non-canonical convention is fine. Confirm the label exists;
do not assume it from the filename.

## Why SCIENCE and not hygiene

`chi_lambda_braid` vs `strict_averaged` vs `bring_color_weighted` is the p/n
interface factor — the Bring colour-weighted asymmetry. Switching it moves
binding numbers. This is not a rename.

## MEASURED 2026-08-19 — the two off-canon conventions are 1210x apart, and the bean lists them as one job

Claimed from `todo`. The bean above says *"switching it moves binding numbers.
This is not a rename"* — true, but with no magnitude the eight files read as one
queue. They are two populations, three orders of magnitude apart.

Per p-n interface factor at the proton-pinned q0 (50 dps, `closed_form_tau_M`
+ `_avg_color_delta`):

    chi_lambda_braid  -> positive  z              = 0.6126880371464652516
    strict_averaged   -> averaged  z - h/2        = 0.50815788774864559388
    bring_color_wtd   -> weighted  z - h(1/2-d/4) = 0.50822978937673896258

    chi_lambda_braid -> canonical :  -17.0492 %
    strict_averaged  -> canonical :   +0.0141 %

Ratio **1210x**. The `-17.05%` is the legacy marshalling drop that
`canonical_interface_kinds`' own docstring describes — *"maps (c=1, d=-h/2) to
(sign=+1, gen) and silently drops the -h/2 coefficient"* — and it independently
reproduces the ~21% figure Phase 5q recorded from the other direction.

**Do not order S4 by file count.** The 9 `chi_lambda_braid` assignments are the
whole tranche's weight; the 6 `strict_averaged` ones are the delta question this
arc has spent four PRs on, and are 1210x smaller than the convention sitting
next to them.

### The effect does not grow with A

`canonical_interface_kinds` models the atom as the block word `p^Z n^N`, so the
census is **Z-1 p-p, exactly 1 p-n, N-1 n-n** — verified D through 12C:

    5Li  Z=3 N=2  {positive: 2, averaged: 1, negative: 1}
    12C  Z=6 N=6  {positive: 5, averaged: 1, negative: 5}

One p-n boundary per atom, for every atom. So the per-bond figure IS the tr_M
figure, with no compounding, and every Z>=1,N>=1 atom in the table takes the same
single multiplicative hit. That is convenient for the migration and worth stating
plainly: this is a uniform rescale of the affected rows, not an A-dependent one.

### Blast radius of the `_habiro_coefficient_extract.py` site specifically

27 committed `habiro-coefficients-*.witness.json`. The module declares its
convention in its own docstring (*"the production `chi_lambda_braid`
convention"*), so it is not an accident — it is a file that was correct before
the migration and was never revisited. `atomic_tr_m_helium4_canonical.py` and
`closed_form_tau_M_verification_phase5q.py` are the same shape.

Note on Phase 5q: its witness validates the closed form against the empirical
slow path to 1e-49 **under `chi_lambda_braid`**. That is a self-consistency check
*within* the legacy frame. It is not evidence for the frame, and it will need
re-running rather than re-reading once S4 lands.

### Next step

`binding_canonical.py` first, per the bean and the ruling. But the ordering
inside the tranche should be by convention, not by filename: settle the 9
`chi_lambda_braid` sites as one decision, then the 6 `strict_averaged` ones as a
separate and much smaller one.

## ROOT CAUSE 2026-08-21 — the mass table's p-n interface comes from caches built before the weighting existed

Owner authorised picking the frame for `canonical_mass_table_extended.py` (the
producer of both `canonical-mass-table-extended` and, via a thin wrapper,
`low-isotope-mass-table`). Traced it rather than flipped it, and the answer is
not a convention flag anywhere in that producer — it has none. `grep
pn_convention canonical_mass_table_extended.py` returns **zero**.

### Measured

    branching combiner, deuteron   0.575090872290275361250124   <- COLOUR-BLIND
    closed form, strict_averaged   0.575090871629810316751633      (agrees, 6.6e-10)
    bridge / fixed symbolic path   0.575172243917771870826535   <- weighted
                                                                   gap 1.4e-4

The producer routes A ≥ 2 through `canonical_tr_m_via_branching`, whose
docstring says it applies `σ − h(½ − δ/4)·𝟙`. It does not, and the reason is
structural rather than a wrong line:

- `intra_block_word()` builds its word from `atom_canonical_crossings(1,0)` and
  `(0,1)` — **free nucleons**, which have no p-n bond. So the `d_for_ctype` call
  there (correct, and fixed for exactly this reason in an earlier pass) never
  sees `averaged_weighted`. The comment above it — *"the if/elif this replaces
  raised on averaged_weighted, i.e. on every Z≥1,N≥1 atom"* — is true of a
  different call path and reads, in place, as though it covered this one.
- The **interface** between blocks is not computed at all. It is loaded from
  precomputed A-operator extract witnesses, keyed `(n_strands, iface)`:

      (6,  "pn") -> sublemma-2-1-A-operator-extract.witness.json     computedAt 2026-05-05
      (9,  "pn") -> A-operator-extract-h9-pn.witness.json            computedAt 2026-05-18
      (12, "pn") -> A-operator-extract-h12-pn.witness.json
      (15, "pn") -> A-operator-extract-h15-pn.witness.json
      (18, "pn") -> A-operator-extract-h18-pn.witness.json

Both checked extracts predate the colour weighting by ~three months, and
**neither carries `convention_fingerprint`, `convention_label`, or
`pn_convention`** — so nothing downstream can tell which interface they encode,
and nothing invalidates them when the convention moves.

### This is `45789ddfa0`'s finding, one cache family over

That commit fixed exactly this shape for the **chi** caches — resume logic keyed
on partition coverage or q₀ alone, "no notion of which word produced the cached
entries, so a cache written before the colour-weighting landed looks complete
forever" — and introduced `convention_fingerprint` in `canonical_braid_crossings`
as the derived guard. The **A-operator** extracts have the same defect and were
not covered.

So the answer to "which frame is the mass table in" is: **it is in whatever
frame its A-operator caches were built in, which is pre-weighting, and no code
in the producer expresses a choice at all.** Flipping a `pn_convention` argument
would fix nothing, because there is none to flip.

### Fix path (NOT executed here — this is a compute job, not an edit)

1. Apply the `convention_fingerprint` guard to the A-operator extracts, so a
   pre-weighting cache is DISCARDED rather than resumed. Same mechanism, same
   module, already written.
2. Regenerate the five `(n, "pn")` extracts with the weighted interface. H₆ is
   cheap; H₁₅/H₁₈ are long-compute and need the `-u … | tee` discipline.
3. Re-run `canonical_mass_table_extended.py` and expect every Z≥1,N≥1 row to
   move by ~1.4e-4 relative — the same migration the low-isotope witness took.
4. Only then is `recomputed-low-isotope-mass-table.md`'s "three paths agree to
   machine epsilon" true of all three; two of them now agree at 3.4e-25 after
   the `qou-4e5k` fixes, and this producer is the third.

### Also found, unrelated to the frame

`canonical_mass_table_extended.py:310` passes `q_val=float(Q_FLOAT)` — a float64
q₀ into a 50-dps pipeline. Caps the branching path at ~1e-16 regardless of
`target_dps`. Precision defect, not a convention one; worth its own fix.
