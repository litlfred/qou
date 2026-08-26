---
# qou-99qc
title: 'OWNER CALL: Delta prose vs epsNPq — one of the two is wrong (fork forced by qou-avt6)'
status: todo
type: task
priority: normal
created_at: 2026-08-26T07:35:22Z
updated_at: 2026-08-26T13:47:22Z
---

## Option (1) NARROWED, 2026-08-26 — the colour-weighted carve-out is closed

qou-avt6 fenced itself: "colour-weighted crossings fall outside the
q^m([2]/2)^c normal form, so do NOT quote the exclusion for words that do."
That carve-out was the last place the prose could still be right. It is gone.

`computations/qbeta/qbeta_epsnpq_colour_weighted_exclusion_probe.py` (15/15).
The fourth template `averaged_weighted` has counit
w(q) = q - h(1/2 - delta/4) with delta = (q-1)^2(1-q^-4)/3 exact
(flavor_split_leading), so eps of any word over ALL FOUR templates is
q^m ([2]/2)^c w^k. At the silver ratio h = 2 exactly, [2]/2 = sqrt2, and

    w(1+sqrt2) = 5*sqrt2 - 16/3,   |N(w)| = 194/9 = 2 * 97 / 3^2

so the vanishing condition gives 2^(C+K) * 97^K * 3^(-2K) = 1, and unique
factorisation reads off K = 0 from the 97, then C = 0, then M = 0. The
difference is identically zero; epsNPq is not.

The 97 is doing the work and nobody arranged it -- it is whatever prime the
flavour split contributes at that point. CHECK 4 TESTS that rather than
assuming it: had |N(w)| been a pure power of 2 the argument would fail, and
the probe would say so.

Control survives: chi_block_3 is found at (m,c,k) = (1,2,0) vs (3,2,0),
matching avt6's exponents.

ALSO DISPOSED OF, so it is not re-raised: "does ANY element have counit
epsNPq" is vacuous. eps is an algebra hom onto Q(q) hence surjective, and the
skein relation makes sigma - sigma^-1 = h a scalar outright, so epsNPq * 1
has counit epsNPq trivially. The content was always the CLASS.

## What is still open, and still yours

Two escapes remain from option (1), and neither is mine to pick:
  (a) Delta is not a difference of TWO words at all -- some other combination,
      which the prose would then have to name; or
  (b) epsNPq is simply wrong, and with it Q_A and the ladder phase.

Widening the crossing vocabulary is no longer among the options.
