# T3g assessment: non-neutral Tannakian / gerbe as flavour SU(3) home

**Date:** 2026-08-04
**Bean:** `qou-y7vg` (T3g), epic `qou-8lxd`

## Status: ASSESSED — direction documented, not actionable near-term

## 1. The question

Can flavour SU(3) arise from the **inter-universe** structure (multiple
inequivalent fibre functors) rather than from a single fibre?

## 2. The Tannakian framework

A **neutral** Tannakian category (one with a fibre functor to Vect_k)
reconstructs a group G via Tannaka duality: G = Aut^⊗(ω).

A **non-neutral** Tannakian category (one where the fibre functor exists
only over a field extension or étale cover) reconstructs a **gerbe** —
a groupoid scheme with a band (lien). The band is the group G, but the
gerbe carries additional H¹ obstruction data.

## 3. QOU context

QOU's SU(2) theorem proves that a *single* QOU fibre has gauge group
exactly SU(2). Any SU(3) must therefore come from **multi-fibre** or
**inter-fibre** structure.

The Tannakian question: does QOU's braided category admit inequivalent
fibre functors? If H¹(base, Aut^⊗) ≠ 0, the reconstruction gives a
non-trivial gerbe whose band could be SU(3).

## 4. The Sym² gate obstruction

**WARNING:** Naively permuting 3 fibres gives the permutation group S₃,
whose natural 3-dim representation is the standard representation
ℂ³ = ℂ{1,2,3}. But permutation representations are **self-dual**
(Sym²(V) always contains a trivial summand for any permutation rep).
S₃ = W(A₂), the Weyl group — it gives the hexagonal symmetry of the
weight lattice, NOT the fundamental representation.

The Sym² gate (proved in Lean: `Sym2Gate`) says: for SU(3) to act on
a space V, we need Sym²(V) irreducible (no singlet). Permutation
representations fail this. So "permute 3 fibres → flavour SU(3)" is
FALSE.

## 5. What would work

A non-neutral Tannakian gerbe with band SU(3) would need a fibre
functor defined only over a **degree-3 extension** of the base. The
three fibres would then not be permuted (which gives S₃) but would
carry a *twisted* action where the Galois group acts by outer
automorphisms of SU(3).

The outer automorphism group of SU(3) is Z/2 (complex conjugation),
not Z/3. So a degree-3 extension alone doesn't naturally produce the
right twisting.

## 6. Connection to the S₄ bridge (T3h)

The S₄ bridge provides an alternative: the Fano point-stabilizer
S₄ ⊂ PSL(2,7) acts on 6 remaining Fano points = 3 + 3̄ under
SU(3). This is NOT a permutation of fibres but a stabilizer action
on the octonionic grading group. The Tannakian question becomes:
is there a gerbe whose band is PSL(2,7) (or its continuous
completion SU(3)) acting on the Fano plane structure?

## 7. Recommendation

This direction is theoretically interesting but:
- The naive "permute 3 fibres" route is DEAD (Sym² gate)
- The Tannakian gerbe route needs the specific degree-3 extension
  and outer automorphism structure, which doesn't naturally match
- The S₄ bridge / Fano route (T3h) is more concrete and testable

Mark as **documented** and lower priority. The Fano/S₄ route subsumes
the structural content of this bean.
