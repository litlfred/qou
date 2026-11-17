---
# qou-dhsn
title: The level-3 EM term already exists and is mirror-blind; crossing counts are affine so no Coulomb term can be built from them
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T12:35:18Z
updated_at: 2026-11-17T07:28:00Z
parent: qou-v2om
---

## The ask, and why it inverts

Owner, 2026-08-30: *"next qou-vudb's open item -- add an explicit EM term at
level 3. It's the first thing with a clear falsifiable target (Coulomb's
A-scaling, exponent ~0.78 on this grid), and unlike the previous candidates it
isn't competing with the strong channel for the same job."*

**The EM term is already there. And it IS competing with the strong channel --
they have each other's parity.**

## What the corpus's own decomposition gives

`qou-toul` (2026-08-29, completed) derived the split from
`def:crossing-energy`'s weights `E = n+ q - n- q^-1`, solving
`E = A(q + q^-1) + B(q - q^-1)`:

    A  (symmetric / STRONG)      = (n+ - n-)/2    the WRITHE
    B  (antisymmetric / COULOMB) = (n+ + n-)/2    the crossing COUNT

Measured against `mass_at_3A_proper.atom_braid_word_3A` on 12 nuclei to A = 39
(`computations/probes/level3_em_channel_parity_probe.py`, 7/7), reproducing
`mba-sidecar-mirror-cancellation` exactly:

    n+ = 5A - 1 + 2Z        n- = 5A - 1 - 2Z
    COULOMB channel = 5A - 1      A-ONLY  -> mirror-INVARIANT
    STRONG  channel = 2Z          carries ALL the charge dependence

Every mirror pair confirms it: 3He/3H Coulomb [14,14], 7Be/7Li [34,34],
11C/11B [54,54], 15O/15N [74,74], 39Ca/39K [194,194] -- equal in all five, while
the strong multiplicities differ in all five.

## Finding 1 — the existing EM term contributes EXACTLY ZERO to any mirror splitting

No coefficient times a mirror-invariant multiplicity produces a mirror
splitting. So the EM term cannot be *tuned* into the Coulomb displacement
energy; the question is not its size.

This is the same parity inversion `qou-1pig` found in the bond layer, now
confirmed one level up in the corpus's POST-CORRECTION decomposition -- and it
is why `qou-vudb` measured the model's mirror asymmetry as a *strong*-channel
constant with A^0 scaling against an observed A^0.87.

## Finding 2 — scope (b), invariant: DEGREE

Coulomb needs the number of proton PAIRS, `Z(Z-1)` -- quadratic in Z. But `n+`
and `n-` are each **affine** in (A,Z), so every `a*n+ + b*n- + c` is affine, and
no affine function equals a quadratic one. Second difference in Z: `Z(Z-1)`
gives constant 2, every crossing-count combination gives identically 0.

Lean, sorry-free, generic CommRing:
`QOU/MassTheory/CrossingCountAffine.lean` --
`no_crossing_combination_is_protonPairs` quantifies over the coefficients
FIRST, so it excludes the whole family at once rather than one fit at a time.
Also `coulomb_channel_mirror_invariant` and
`strong_channel_mirror_difference = 4(Z - W)`.

## A counting trap that nearly made me call a corpus block wrong

`atom_braid_word_3A` returns `(c, d, gen)` triples denoting the HECKE ELEMENT
`c*sigma_g + d*1`, **not** braid letters. Classifying by `c` -- which is 1 on
every letter -- reports every braid as POSITIVE, gives `n- = 0` and
`n+ + n- = n+ - n- = 12A - 1`, and makes `mba-sidecar-mirror-cancellation` look
wrong. Classify by `d`, per that function's own docstring: `d == 0` is sigma,
`d == -h` is sigma^-1 (this module has `sigma^-1 = sigma - h`), anything else
is an averaged letter and not a braid generator at all. Then `n- = 7` for 2H,
156 for 39K, and every sidecar figure matches including the `2A+1` averaged
count. **The braids are NOT positive.**

## What survives

Not "add an EM term" -- that is done and is inert. The target is to get a
`Z(Z-1)` multiplicity from somewhere the crossing counts do not reach, OR to
move the charge dependence out of the strong channel. Both are structural
changes to the crossing-energy decomposition, not new coefficients.

Nothing refuted; `qou-toul`'s correction stands and this builds on it. Nothing
wired.

Parents: qou-vudb, qou-toul, qou-1pig.

## Round 62 Update (PR #8255)
- Formalized in PR https://github.com/litlfred/qou/pull/8255 (head `b4ec4b15ca43f486c66d8f53b0eeb216293fc6aa`, Commit 1 `c715790dad2efe16f1713c8a17825e912524e641`, `scriptHash: e2eb499467fc`).
