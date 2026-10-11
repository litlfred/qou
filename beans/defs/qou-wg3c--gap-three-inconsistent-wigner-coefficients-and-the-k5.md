---
# qou-wg3c
title: 'GAP: three inconsistent Wigner coefficients, and the [5]_q! block conflicts with the k=5 row cap'
status: todo
type: task
priority: normal
created_at: 2026-10-11T07:35:00Z
updated_at: 2026-10-11T07:35:00Z
parent: qou-8lxd
---

Found 2026-10-11 while testing whether the Wigner term derives `a_asym`
(bean `qou-nxvg`; it does not). Opened on owner instruction.

## The three coefficients (proton q0, mp.dps 30)

    prop:wigner-np-pairing             Delta_(2,2) = m_e [3]_q [2]_q^2      6.2893 MeV
    prop:wigner-coefficient-derivation [5]_q! m_e                           67.1008 MeV
    prop:wigner-2-coefficient          C_(2,2) = w h/2, w = dim_q^2/[4]_q!  0.017357 (dimensionless)

`dim_q(2,2) = 2.04371`, `w_(2,2) = 0.166049`, `h = q - 1/q`. All three are
named "the Wigner coefficient" for `-Delta_W T(T+1)/A`. They differ in value
and in q-form, so at most one can be the coefficient of that term, unless
they are proven to be different objects (e.g. a dimensionless shadow price
vs its MeV realisation) with a stated map between them.

## The k = 5 conflict

`prop:wigner-coefficient-derivation` sets the scale at Hecke level k = 5
(`[5]_q!`). Under convention D the row cap `l(lambda) <= 2` admits no
self-conjugate shape at k >= 5 (`qou-a5jk`, `no_selfConj_two_row_of_five_le`,
sorry-free), and `w = 0 -> C = 0 -> u* = 0` (`qou-w06d`). So a level-5
self-conjugate Wigner shadow price is zero. The block's proof asserts the
k = 5 scale ("set by the Hecke-level scale at k = 5") and supports it by
agreement with a fitted 68.9 MeV, which is not a derivation.

## Open (owner decision before any edit)

1. Which, if any, of the three is the canonical Wigner coefficient.
2. Whether the [5]_q! block should be scoped as superseded by the k=4 cap.

Nothing edited. Status stays todo: this tracks an open identification.
