---
# qou-oppb
title: 'Two inequivalent canonical-He4 braid words: he4_braid_canonical vs atom_braid_word_3A'
status: completed
type: task
priority: normal
created_at: 2026-08-26T16:40:21Z
updated_at: 2026-08-26T18:15:32Z
---

Two functions in `computations/` each construct "the canonical ⁴He braid word at
H_12", both 47 crossings with interfaces pp@gen2 / pn@gen5 / nn@gen8, and they
are **not the same word**:

- `sublemma_2_1_h12_he4_branching.he4_braid_canonical()`
- `chi_sym_alt_closed_form.atom_braid_word_3A(2, 2)`

They differ in **36 of 47 positions**, yet carry the **identical multiset of
(c, d) letters** (max pairwise difference 5.0e-17, pure float64 rounding) and
the **identical multiset of generators**. Same letters, different strands,
different order.

Diagnostic:
[`computations/probes/he4_canonical_braid_word_disagreement_probe.py`](../computations/probes/he4_canonical_braid_word_disagreement_probe.py)
(mpmath, 40 dps).

### Why this went unnoticed

The two words give the same answer wherever the answer cannot distinguish them.
On a one-dimensional irrep the character is a product of scalars, and scalars
commute, so any reordering agrees. Measured:

| | dim | max/min rel difference |
|---|---|---|
| (12,) and (1¹²) | 1 | **1.06e-15** |
| the other six λ ⊢ 12 | 11–55 | **2.34 to 30.8** |

Fifteen orders of magnitude, split exactly on dimension. Any check that only
exercises 1-dim blocks — or that reports a summed `tr_M` where the two-row
stratum dominates — sees agreement.

### What it already broke

`sublemma_2_1_h12_he4_phase25` reports 0/8 and was recorded as a defect in
`path_b_chi_h12` (`qou-matm`, now retracted). It is not: Path B reproduces
`tr(ρ_λ(β))` with defect **0.0**, and the branching decomposition is complete
(dimensions sum exactly, per-η class sizes match, no SYT skipped). The producer
was comparing the characters of two different words.

Everything downstream of `he4-canonical-tr-m-block-fingerprint` inherits
`atom_braid_word_3A`; everything downstream of the H_12 branching cone inherits
`he4_braid_canonical`. Neither says which it used at the point of use.

### Open — and this is a judgement call, not a measurement

Which is canonical? Not established here. Both are plausible readings of
"p₁ · I_pp · p₂ · I_pn · n₁ · I_nn · n₂", differing in where the interface
offset attaches relative to the nucleon body. Note that `atom_braid_word_3A` is
also the subject of `qou-b4xn` (its u-d factor count is `2A`, not the `2A+1`
that `chi_sym_alt_closed_form` asserts of it), which is weak evidence against
it — weak because that bean has not been bisected either.

### Next step

Decide the convention, then make it un-choosable: one constructor, imported by
both cones, with the other deleted or made an explicit alias. A convention that
two functions can disagree about will be disagreed about again.

Secondary, and independent of which word wins: **both constructors emit float64
offsets** (`atom_braid_word_3A` wraps one in `mpf`, the `mpf(<float>)` pattern
`scripts/precision-gates.sh` flags). That caps every character built from either
at ~1e-15 regardless of the dps used downstream.


## RESOLVED 2026-08-26 (PR #5833, commit `d003e06c4`)

The bean framed the choice as "a judgement call, not a measurement". It turned
out to be a measurement, and one-sided:

| constructor | consumers |
|---|---|
| `atom_braid_word_3A` (defined `mass_at_3A_proper.py:433`) | **~220** corpus-wide |
| `he4_braid_canonical` | **3**, all inside the H_12 branching cone |

And the corpus word makes the divergent cone verify. Substituting it takes
phase25's residuals from six at O(1) to:

| λ | rel | λ | rel |
|---|---|---|---|
| (12,) | 1.25e-08 | (3,1⁹) | 1.02e-08 |
| (11,1) | 6.64e-09 | (2,2,1⁸) | 4.97e-09 |
| (10,2) | 4.75e-08 | (2,1¹⁰) | 1.77e-08 |
| (10,1,1) | 1.43e-08 | (1¹²) | 1.07e-08 |

That band is F1's **8-significant-figure storage floor**, not a residual. A
third independent confirmation that `path_b_chi_h12` was always correct, after
the completeness identity and the defect-0.0 projector check.

`he4_braid_canonical` now delegates. Kept as a named function rather than
deleted: it is the name this cone documents itself with, so a reader looking for
"the canonical ⁴He word" lands there and is told where it comes from.

### Deliberately not done

**The pass threshold was not widened.** phase25 still prints 0/8, because
`rel < 1e-9` is unmeetable against an upstream storing 8 significant figures.
Relaxing it to make the run green is the baseline-widening anti-pattern; the
honest report is that the mathematics agrees and the threshold is measuring F1's
serialization. Whether `he4-canonical-tr-m-block-fingerprint` should store more
digits belongs to whoever owns that producer.

### What was NOT established

That `he4_braid_canonical`'s local build was never deliberate. Established: it
disagrees with ~220 files, nothing else consumes it, and the corpus word makes
its own cone verify. Reversible in one line if someone knows otherwise.

### The probe is now a regression pin

The fix would have made
[`he4_canonical_braid_word_disagreement_probe.py`](../computations/probes/he4_canonical_braid_word_disagreement_probe.py)
compare the corpus word to itself and quietly stop demonstrating anything, so it
reconstructs the old local word inline (verbatim, from `b2028fc3b`) and **exits
non-zero if the delegation is ever undone**.

### Still open, and separate

Both constructors emit **float64 offsets** — `atom_braid_word_3A` wraps one in
`mpf`, the `mpf(<float>)` pattern `scripts/precision-gates.sh` flags. That caps
every character built from either at ~1e-15 regardless of downstream dps. Not
fixed here: it touches the corpus-wide constructor and moves numbers in ~220
consumers, which is its own tranche. Related: `qou-b4xn`, whose subject is the
same constructor.


## RETRACTED 2026-08-26, same day — the float64 claim was mine and it is false

This bean's "Still open" / "Secondary" item said:

> both constructors emit **float64 offsets** (`atom_braid_word_3A` wraps one in
> `mpf`, the `mpf(<float>)` pattern `scripts/precision-gates.sh` flags). That
> caps every character built from either at ~1e-15 ... A ~220-consumer tranche.

**There is no tranche.** `atom_braid_word_3A` is exact. It builds `h` and `delta`
inside `workdps(max(mp.dps, 60))` from `Q_50_DIGIT_STR` and
`flavor_split_leading`, and measured against the closed form at 60 dps its `ud`
and p-n offsets have relative error **exactly 0.0**:

```
ud:  got   -0.104530149397819657715423106565
     exact -0.104530149397819657715423106565
pn:  got   -0.10445824776972628901783406629
     exact -0.10445824776972628901783406629
```

`mass_at_3A_proper.py` even carries a long comment naming the exact two leaks I
"found" — `pyhecke.gram.h` being a Python float, and `_avg_color_delta()`
reaching only ~5e-16 — as **already fixed at the source**, with the measured
improvement (deuteron 1.024e-16 → 3.476e-20 → 3.229e-50). I did not read it.

### How the error was made

The probe compared `he4_braid_canonical`'s word against `atom_braid_word_3A`'s
and found the letters differing by ~5e-17. That difference is real. I attributed
it to **both** words rather than to the one that moved. `he4_braid_canonical`
used `pyhecke.gram.H` directly, which is a float; the other side was exact all
along, so the 5e-17 was a one-sided error being read as a shared floor.

The same mistake explains the "~1e-15 agreement" on the two one-dimensional
irreps: that is the old local word's float64 error against an exact reference,
not a cap on both.

And it is doubly stale now: `he4_braid_canonical` **delegates** to
`atom_braid_word_3A` as of this same bean's fix, so there is exactly ONE
constructor and it is exact.

### Where it propagated before being caught

The probe docstring, this bean, `qou-cdqu`, the `authorNotes` of
`prop:chi-sym-alt-closed-form`, and the bodies of PRs #5833 and #5847 — all
corrected. Nothing downstream consumed the claim; it was described as a future
tranche and never acted on.

### The lesson, which is the corpus-grep rule again

A measured difference between two implementations tells you they disagree. It
does not tell you **which** is wrong. I had the exact closed form available the
whole time (`flavor_split_leading`, the same function the constructor uses) and
did not check either side against it — the check that would have settled it took
one script and found rel error 0.0 immediately.
