---
# qou-1pig
title: The pair layer is a LINEAR RAMP in neutron count, not an isospin structure — B_nn > B_pn > B_pp is backwards
status: todo
type: task
priority: normal
created_at: 2026-08-30T10:05:43Z
updated_at: 2026-08-30T10:06:29Z
---

## The question that provoked it

Owner, 2026-08-30: *"do we need to split in the model? where issue?"* — on the
27% b3 gap being the 3H-3He splitting with 'nowhere to live but b3'.

**The model already splits.** The issue is not a missing split; it is that the
split it has is the wrong SHAPE.

## Measured (convention D, proton pin, alpha = m_e/(q0(q0-1)) = 4.18598 MeV)

    h    = q0 - 1/q0                = 0.20906029879563931543
    f_pp = z                        = 0.6126880371464652516
    f_pn = z - h(1/2 - delta/4)     = 0.50822978937673896258
    f_nn = z - h                    = 0.40362773835082593616

Sec.10a log form, pair energies B = -alpha ln f:

    B_pp = 2.0507 MeV      B_pn = 2.8332 MeV      B_nn = 3.7978 MeV

## Defect 1 — the ordering is backwards

Charge symmetry says the two LIKE pairs are nearly degenerate (equal up to EM
and a small CSB residual) and the UNLIKE pair is the distinguished one: the
deuteron is bound, the diproton and dineutron are **not bound at all**. So the
physical ordering is `B_pn > B_pp ~ B_nn`.

The model gives a **monotone ladder** `B_pp < B_pn < B_nn`, with the two like
pairs **1.747 MeV apart** where charge symmetry wants them nearly equal, and
`B_nn` — the unbound one — as the MOST bound.

## Defect 2 — it is a linear ramp, and exactly so

    midpoint of f_pp and f_nn  =  z - h/2
    f_pn                       =  z - h/2 + h*delta/4

so `f_pn` is the ARITHMETIC MEAN of `f_pp` and `f_nn` up to `h*delta/4`,
measured at **7.19e-5**, i.e. **1.4e-4 relative**. The bond factor is therefore
linear in the neutron count of the pair (0, 1, 2 neutrons -> z, z-h/2, z-h).

A linear ramp in neutron count is **odd in T_z**. Charge symmetry demands the
strong part be **even** in T_z, with the asymmetry supplied by an EM term the
framework does not have (qou-9v7t: *"the framework has no EM term in any
per-bond factor"*). So the typing is not an isospin structure at all.

## Consequence — this is where the 27% goes

The model's pair-layer mirror asymmetry is

    B(3H) - B(3He) = alpha * ln(f_pp/f_nn) = 1.74707324276 MeV

against the observed 0.763755 MeV: **right sign, 2.287x too large**.

Re-typing the AME Ursell inversion with the model's own pair layer instead of
`3*B(2H)` therefore OVER-subtracts and eats the whole 3-body term:

    b3 untyped   3H  1.8081        3He  1.044345      split +0.763755
    b3 retyped   3H -0.98231       3He +0.00100816    split -0.98332

The split flips sign. So the answer to *"do we need to split in the model?"* is:
the model splits already, and the split is 2.3x too strong and of the wrong
parity — strong enough that using it destroys b3 rather than cleaning it.

**Why the AME inversion cannot type its pairs.** It subtracts `3*B(2H)` from
both nuclei, typing every pair as pn, because `B(pp)` and `B(nn)` are **not
measurable** — the diproton and dineutron are unbound. So the untyped inversion
charges the entire p/n asymmetry, strong AND EM, to b3 by construction. That is
correct bookkeeping given the data; it is not an error, and it is why b3 carries
the 27%.

## Flag — a suspicious near-zero, do NOT build on it

Retyped `b3(3He) = +0.00100816` MeV, i.e. the model's 3He pair layer 7.717035
against AME 7.718043 — a 0.013% match. With a 2.3x-wrong asymmetry elsewhere in
the same table this is almost certainly coincidence. Recorded so nobody
rediscovers it as a result.

## Next

Ask whether the corpus's own p/n convention (`bring_color_weighted`, canonical
per owner ruling R3 2026-08-15) gives an even-in-T_z typing, and if not, what
would. Cross-reference qou-9v7t, which found 9 of 10 chirality candidates get
the mirror asymmetry backwards and named the missing EM channel.
