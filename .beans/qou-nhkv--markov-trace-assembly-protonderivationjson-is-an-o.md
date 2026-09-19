---
# qou-nhkv
title: markov-trace-assembly-proton.derivation.json is an orphan with no live builder
status: completed
type: task
priority: normal
created_at: 2026-09-13T12:45:55Z
updated_at: 2026-09-13T17:22:02Z
---


## The orphan

`computations/markov-trace-assembly-proton.derivation.json` is consumed by LIVE
code — `applied_uniqueness_mass_table.py` (which takes `tr_M[proton]` straight
from it) and `markov/assembly_chain_11_letter_recompute_probe.py` — but **no
live producer writes it.** Its only builder is
`computations/_deprecated/build_markov_trace_assembly_chain.py`.

Its neutron and deuteron siblings both have live builders
(`build_markov_trace_assembly_{neutron,deuteron}_chain.py`), and both were
migrated to `canonical_trm_reference` and regenerated canonical on 2026-09-13
(`ff7b290798d`). The proton did not move, so the cluster is now **mixed-frame**:

    atom      assembly chain target_value        frame
    proton    1.14575969245730086968…            GROUPED    <- orphan
    neutron   0.4751335171556822                 canonical
    deuteron  0.1519683392042316                 canonical

82 % disagreement against the reference, inside one table.

## Why un-deprecating the builder does NOT fix it

That builder computes a **different object**. Its own docstring says the proton
word is "6-crossing, all positive sigma" and reports `tr_M(p, q_0) ≈ 2.12258` —
which is the FIFTH claimant in `trm_proton_five_values_census` (bean
`qou-soj6`), listed there as UNEXPLAINED. The canonical proton element is
eleven letters with {6 σ, 3 σ⁻¹, 2 averaged}, and
`assembly_chain_11_letter_recompute_probe` already measures the correct value
from it: **0.62932840220292191817**.

So running the deprecated builder would replace a grouped-era value with a
wrong-word value. It is deprecated for a reason.

## What the work actually is

Write a live `build_markov_trace_assembly_proton_chain.py` against the
canonical 11-letter element, in the shape of its two siblings — they are the
template, and both now read `canonical_trm_reference` for their leaf. The
recompute probe already has the target value and the method, so this is
transcription of a known derivation into the chain format rather than new
mathematics.

Note the two siblings' own history when writing it: their steps 5–7 use a
legacy convention their builders document, and the proton chain's steps 4 and 6
assert the all-positive-sigma premise that is false. Do not carry that premise
across.

## Gated so it cannot be forgotten

`applied_uniqueness_mass_table.py` now carries
`all_chains_in_the_canonical_intra_ordering_frame` (computed 1, expected 0) and
prints a per-atom `⚠ FRAME MISMATCH` line. **Red on arrival, deliberately** —
a mixed-frame mass table is not a result to lock at its measured value, it is
something to fix, and a gate that tolerates it teaches the next reader it is
fine. It goes green when this bean lands.

Found under `qou-4383`. Related: `qou-soj6` (the five proton values),
`qou-y4gi` (the ordering guard on the reference).

---

## DONE 2026-09-13 — `851751ee7fe`

`computations/build_markov_trace_assembly_proton_chain.py`, written against the
canonical 11-letter element as this bean specified.

**It does not carry the siblings' premise across**, which this bean asked for
explicitly. The neutron and deuteron chains evaluate χ^λ from n₊/n₋ of a legacy
5-letter word and call their symbolic intermediate "illustrative-only"; this
chain runs its character steps on the canonical element via
`markov_weights_symbolic.tr_M_canonical`. `structural_check` OK, trust profile
{axiom 1, derived 4, script-cited **0**, computational 1} — the same
fully-trusted, zero-frontier profile the siblings claim, but earned rather than
asserted. The leaf is read from `canonical_trm_reference`, so it cannot inherit
a superseded frame the way theirs did.

### Three routes, one word

    atomic-braid-recipe-p-canonical.derivation.json   {σ: 6, σ⁻¹: 3, averaged: 2}
    trm_proton_five_values_census (canonical_word_for) {σ: 6, σ⁻¹: 3, averaged: 2}
    this builder, computed live                        {σ: 6, σ⁻¹: 3, averaged: 2}

### Downstream

    applied_uniqueness_mass_table        3/3, FRAME GATE CLEARED
    assembly_chain_11_letter_recompute   4/7 → 5/7
    grouped-era witness files            38 → 37
    downstream reflections               16 → 15

The recompute probe's two remaining failures are the muon-pin entries, for which
no muon-pinned assembly witness exists — a real gap, named in its source, and
not this bean's.

### A bug worth recording, because of how it was caught

The first run emitted `{σ: 4, σ⁻¹: 0, averaged: 7}`. I had read element `[0]` of
`atom_braid_word_3A_to_crossings` as a sign; it is the **generator index**, and
the type is element `[1]`. **Three tuple shapes exist for this one object within
one neighbourhood** — `(index, type)` there, `(c, d, g)` from
`atom_braid_word_3A` itself, `[sign, generator]` in the census — and I picked
the wrong reading of the wrong one.

What caught it was the docstring's own claim. The code contradicted a number I
had verified minutes before, so the disagreement was *visible* rather than
merely plausible. Stating the expected value next to the computation is what
turned a silent wrong count into an obvious one — worth doing deliberately, not
just when it happens to help.
