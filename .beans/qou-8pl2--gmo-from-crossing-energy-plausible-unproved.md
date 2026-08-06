---
# qou-8pl2
title: 'PLAUSIBLE-NOT-PROVED: Gell-Mann–Okubo from the crossing-energy splitting'
status: todo
type: task
created_at: 2026-08-06T00:00:00Z
updated_at: 2026-08-06T00:00:00Z
---

## Claim (plausible, not proved)

The meson mass relation `4 m_K² = 3 m_η² + m_π²` should follow from the
crossing-energy splitting pattern on the `A_2` weight lattice, the kaon
involving a strange-quark braid word of different writhe than the pion.

## Status

**Asserted, never derived.** The chapter previously said the relation "is a
consequence of" the crossing-energy pattern and then, one sentence later, called
the numerical agreement "an open cross-check" — a claim and its own retraction
in the same paragraph. Rewritten (see the `content(eightfold)` honesty pass).

## The one numerical datum

`computations/gmo_meson_crosscheck.py`:
* experimental GMO deviation: `≈ 6%`
* `q`-deformation of the adjoint quantum dimension at `q_0 ≈ 1.11`: `≈ 3.3%`

Same order of magnitude, factor `≈ 2` apart, **no mechanism connecting them**.
This is currently recorded as an unexplained coincidence of scale and must not
be cited as agreement.

## What would settle it

1. Derive the mass operator from the crossing energy
   `E_×(q) = ½(q − q⁻¹)` acting on the octet braid words, and show the GMO
   combination is the eigenvalue relation it induces. Note GMO is conventionally
   an SU(3)-breaking statement about the *linear* mass operator (squared masses
   for mesons); the derivation must reproduce that structure, not just a number.
2. Or show the factor-2 discrepancy is a genuine prediction of the framework
   (i.e. QOU predicts GMO should be violated at ~3.3%, contradicting the ~6%
   observed) — that is a **falsification test**, and running it is more valuable
   than continuing to describe the two numbers as close.

## Blocked on

Both routes are gated on `N = 3` (item 1 of the chapter's open problems) and on
hypercharge `Y` (item 2), since inter-multiplet splittings depend on `Y`. Within
an isospin multiplet the splitting is electromagnetic and comes from the writhe
difference, which IS derived — that sub-case is the honest place to start.
