---
# qou-y2np
title: 'SHAPE-1: the symmetry-energy sign is a BAR BRANCH (exactly +/- 2 ln q), the corpus took the branch that fits nuclear binding worse, and beta-decay does NOT pin it (Q_beta uses |Delta net|)'
status: in-progress
type: task
created_at: 2026-09-05T06:49:20Z
updated_at: 2026-09-05T06:49:20Z
---

`computations/qbeta/qbeta_asymmetry_sign_is_a_bar_branch_probe.py` (6/6).

## The asymmetry is exactly `+/- 2 ln q`

From `qou-xf14`'s pinning, `b_pp = q^2/[2]_q` and `b_nn = q^-2/[2]_q`, so the
bond energies are `ln[2]_q -/+ 2 ln q` identically and

    S(Z,N) = (A-2) ln[2]_q + (-ln b_pn) + 2 ln(q) . (N - Z)

The coefficient is **exactly `2 ln q_0 = 0.2086814`**, positive for one reason:
`q_0 > 1`. (Supersedes `qou-q7ga`'s first-order `2(q_0-1) = 0.21996`.)

## Its sign is one bit — a bar branch

Under `q -> 1/q`: `[2]_q` is INVARIANT and `b_pp <-> b_nn` swap. So the two
branches are `+2 ln q` (as built, `p-p = sigma`) and `-2 ln q` (swapped), and the
bit traces to the Hecke eigenvalue assignment `u <-> +q`, `d <-> -q^-1`
(`meson-to-proton-via-borromean.md`).

## The swapped branch fits substantially better

2548 measured AME nuclides, tower-summed `E_0`, 3 strands/nucleon:

    law                            p5-p95    full    corr (N-Z)^2/A^2
    as built    p-p = sigma        1.22497  10.18       -0.804
    BAR-SWAPPED p-p = sigma^-1     1.16633   7.37       -0.493
    no asymmetry (count only)      1.18054   8.21       -0.697

It nearly halves the symmetry-energy correlation and is the **first isospin
structure in this arc to beat layout-free bond counting** — which reverses
`qou-q7ga`.

## And beta-decay does NOT pin the branch

The obvious objection is that the same letters build the nucleons, so `Q_beta`
fixes the bit. It does not, for a specific reason: `derived_masses.py` computes
`Q_beta = |Delta(net)| . E_0` with an **absolute value**, so the magnitude is
sign-blind; and the ordering is imposed separately as `m_n = m_p + Q_beta + m_e`,
not read off `Delta(net)`'s sign. Neither half constrains the bit.

## NOT adopted — and what would settle it

Choosing the branch that fits IS a fit. What is established is that the choice is
currently **free** and the evidence points away from the corpus's convention, so
something must pin it. Candidates, none evaluated here: electric charge
(`u = +2/3`, `d = -1/3` is not bar-symmetric — the most promising), the Borromean
proton construction, or the `net` values' own derivation.

**Caveat that cuts against this:** the swap is one bit out of two, so "it fits
better" is a single bit of evidence, not a derivation. And it REDUCES the symmetry
residual without supplying it — `corr = -0.493` is still the dominant residual
shape, so the term is still missing, just less badly.

Successor to the shape agenda in
`docs/audits/2026-09-05-binding-law-arc-synthesis.md` §6 item 1-2.
