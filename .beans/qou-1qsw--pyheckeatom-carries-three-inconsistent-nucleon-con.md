---
# qou-1qsw
title: pyhecke.atom carries THREE inconsistent nucleon constructions (nets differ by 24%) and different consumers read different ones
status: todo
type: task
priority: normal
created_at: 2026-08-29T16:24:57Z
updated_at: 2026-08-29T18:21:39Z
---

Surfaced by the `qou-cds1` takeover work (`74a52d3486`), which recorded it as
**"New, and it is a defect in the tree, not in this bean: ... Not filed as its
own bean yet."** Filing it so it stops living inside another bean's history.

## The defect

`pyhecke.atom` carries three mutually inconsistent nucleon constructions, and
their Markov-trace nets disagree by up to ~24 %:

| constructor | crossings | net |
|---|---|---|
| `build_nucleon_nf` | 9 | `-0.1883216147` |
| `build_atom_nf_exact` | 11, interleaved | `-0.2272041420` |
| `nucleon_gen_chains` | 11, gen-grouped | `-0.2332458961` |

The two 11-crossing models carry the **same multiset of typed crossings** and
differ only in ORDER — `build_atom_nf_exact` interleaves gen-0/gen-1,
`nucleon_gen_chains` emits all gen-0 then all gen-1. `H_3(q)` is not commutative
across generators, so these are genuinely different elements; their nets differ
by 2.6 %.

## Why it bites — the consumers are split

Different call sites read different constructions, so "the nucleon" is not one
object in this codebase:

- the exact atom/mass path uses `build_atom_nf_exact`
- the module constants `PROTON_NF` / `NEUTRON_NF` are `build_nucleon_nf`
- the fork-pricing probe reads `_PROTON_G0` / `_G1`

A result quoted from one path is not comparable with a result quoted from
another, and nothing in the tree marks which is which.

## Prior art the fix must respect

`build_nucleon_nf` omits the 2-`sigma_0` gluon dressing **deliberately** — its
own docstring says *"No separate gluon dressing — B_3 IS the gluon structure"*.
So this is not simply "one is missing crossings"; the 9-crossing model is a
different physical convention, not a truncation bug. Any consolidation has to
decide which convention is canonical rather than assume the longest wins.

`qou-bg3w`'s `Delta_L` (`-0.233198`) is the **gen-grouped** one, which the first
version of the cds1 exclusion probe never touched — an example of the confusion
this causes reaching a real analysis.

## What is needed

1. Determine which construction is canonical (owner call if the gluon-dressing
   convention is genuinely open).
2. Make the non-canonical ones either aliases, or explicitly-named variants that
   a reader cannot pick up by accident.
3. Re-point the split consumers; check whether any committed witness carries a
   value from a now-non-canonical constructor.

Not started. Filed from the cds1 takeover record, not re-measured here — the
numbers above are quoted from that probe's output, and step 1 should re-verify
them before acting.


## 2026-08-29 — VERIFIED, and two corrections to the entry above

The entry above was written from the cds1 takeover's record and said so. Having
now re-measured, its verdict stands but **two of its statements were wrong**,
one of them mine.

### Correction 1 — those are n-minus-p DIFFERENCES, not per-nucleon nets

The table above presents the three numbers as each construction's "net",
which reads as a property of one nucleon. It is not. The probe computes
`net = sum(delta(neutron, proton))` — the **Delta_L difference** between the
neutron and proton NFs. A per-nucleon sum gives entirely different values
(`build_nucleon_nf(['u','u','d'])` sums to `+0.9991251242`), so anyone
checking the table against a single nucleon would find it irreproducible and
conclude the record was wrong.

### Correction 2 — the consumer split is far wider than "three call sites"

Measured across `computations/`, `tools/` and `qou-mass/`, excluding
`_deprecated/` and `pyhecke.atom` itself:

| model | crossings | Delta_L (n - p) | in-repo readers |
|---|---|---|---|
| `build_nucleon_nf` | 9 | `-0.1883216147` | 10 direct, + 8 via `PROTON_NF`/`NEUTRON_NF` |
| `build_atom_nf_exact` | 11, interleaved | `-0.2272041420` | 6 |
| `nucleon_gen_chains` / `_PROTON_G0` | 11, gen-grouped | `-0.2332458961` | **53** |

Not "the fork-pricing probe" — **53 files**, and they include canonical
mass/binding producers: `binding_canonical.py`, `closed_form_tau_M.py`,
`pn_alpha_lp_dual.py`, `tau_M_proton_closed_form_phase5l1.py`,
`binding_multibond_wenzl.py`, `terms_2_3_atom_per_gen_mpfr_50dps.py`. The
gen-grouped model is not a probe-local choice; it is what most of the compute
surface actually reads.

Spreads: **23.85 %** between the extremes, **2.66 %** between the two
11-crossing models (which differ only in generator ORDER, `H_3(q)` being
non-commutative across generators).

All three values reproduced exactly by re-running
`computations/qbeta/qbeta_d1_eleven_crossing_exclusion_probe.py` on `main`.

### New, and separable — `pyhecke.atom` computes in float64

Measured on import:

    pyhecke.atom.h      -> float   0.20906029879563937
    PROTON_NF[0]        -> float  -0.0996576539713873   (all six coords float)

`build_nucleon_nf` seeds `nf = [1.0, 0, 0, 0, 0, 0]` and the module-level `h` is
a Python float, so `PROTON_NF` / `NEUTRON_NF` — module constants that 8 files
read — are float64 objects. Under AGENTS.md §"PROBES ARE NOT EXEMPT" that is a
defect on its own, independent of which construction is canonical, and it is
worth fixing first: it is mechanical, it does not require the convention ruling,
and it makes the comparison between the three models trustworthy at more than
~15 digits.

### Still not patched, deliberately

Which construction is canonical is a convention question — the 9-crossing model
omits gluon dressing **by design** — and re-pointing 53 readers on my own
judgement would be exactly the kind of unilateral move the anti-laundering rules
exist to prevent. The measurement is the deliverable here; the ruling is the
owner's.


## 2026-08-29 — the float64 half is DONE; the convention half is what remains

`build_nucleon_nf_mp` added to `pyhecke.atom` (float-free, at the true 50-dps
`q_0`), additive, no consumer moved.

**The trap worth recording, because the one-line fix is the wrong one.** The
module already has a float-free path — `hm_exact` over `Fraction` — and routing
this builder through it is a two-character change. It would have been a
regression of about eleven orders of magnitude:

    float64 builder vs mp at true q_0    1.4e-16 relative  (proton)
    Fraction path  vs mp at true q_0     1.66e-5 relative  = 16.6 ppm

because `_Q_FRAC = Fraction(111, 100)`, i.e. the Fraction path is exact
arithmetic at `q = 1.11`, not at `q_0 = 1.1099785827513808`. gram.py documents
the 1.93e-5 gap on `q` itself at `_Z_FRAC`; the 1.66e-5 above is what that
propagates to on this builder's output, measured. **Float-free and correct are
different properties**, and a NO-FLOAT64 sweep that reaches for the nearest
Fraction path will silently trade 1e-16 for 1e-5. The docstring says this at
the site where the next person will reach for `hm_exact`.

Also checked rather than assumed: `_hm_mp` tests `nf[si] == 0` where the float
`hm` tests `abs(nf[si]) < 1e-15`. Had the mp twin inherited that cutoff the
whole mp path would have been capped at float64 no matter the dps.

**Nothing moved.** The float builder was already correct to its own precision,
so this extends precision rather than fixing a value; `PROTON_NF`/`NEUTRON_NF`
and all 53 readers are untouched.

### What is left on this bean

Only the convention question, and it is unchanged: which of the three nucleon
constructions is canonical, given that the 9-crossing model omits gluon
dressing by design. That needs the owner. When it is settled, the mp builder is
the precision-correct base to re-point onto — and the same warning applies to
whatever is done for the two 11-crossing models: build them on `hm_mp`, not on
`hm_exact`.
