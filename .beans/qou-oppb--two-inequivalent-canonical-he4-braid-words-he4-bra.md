---
# qou-oppb
title: 'Two inequivalent canonical-He4 braid words: he4_braid_canonical vs atom_braid_word_3A'
status: todo
type: task
created_at: 2026-08-26T16:40:21Z
updated_at: 2026-08-26T16:40:21Z
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
