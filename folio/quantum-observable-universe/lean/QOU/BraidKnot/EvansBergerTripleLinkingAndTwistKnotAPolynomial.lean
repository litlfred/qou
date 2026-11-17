/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Beans:
  - qou-0seq: Cross-check 1992EvansBerger.pdf [evans-berger1992] at mixed_multibond_mubar_integrality_probe
  - qou-dvqx: Cite 0401068v1 (1).pdf [takata2004] / [le2006] at prop:phi-q-aj-machinery-identification
  - qou-e1me: Cross-check 0401068v1.pdf [takata2004] at qbeta_nz_even_series_fourone_probe.py
-/

namespace QOU.BraidKnot

/-!
# Section 1: Evans-Berger Third-Order Winding Integral on 3-Braids (`qou-0seq`)

Ref: [evans-berger1992] M. A. Berger and N. W. Evans, "A Hierarchy of Linking Integrals",
J. Phys. A: Math. Gen. 25 (1992), 5849-5866, eqs. (21)-(22), p. 6:
The Arnol'd one-form
  `ψ_{123} = λ_{12} dλ_{23} + λ_{23} dλ_{31} + λ_{31} dλ_{12}`
is closed on the configuration space of 3-strand braids by the Arnol'd relation, so its cyclic
symmetrization defines a homotopy-invariant third-order winding integral `Ψ_{123}` on pure 3-braids
that remains well-defined even in the presence of a Hopf-linked spectator pair.
-/

/-- Discrete cyclic Arnol'd symplectic pairing step
`(λ_{12} Δλ_{23} - λ_{23} Δλ_{12}) + (λ_{23} Δλ_{31} - λ_{31} Δλ_{23}) + (λ_{31} Δλ_{12} - λ_{12} Δλ_{31})`
between the cumulative pairwise winding vector `(lam12, lam23, lam31)` and the increment
`(d12, d23, d31)`.
Ref: [evans-berger1992] eqs. (21)-(22). -/
def arnoldSymplecticStep (lam12 lam23 lam31 d12 d23 d31 : Int) : Int :=
  (lam12 * d23 - lam23 * d12) + (lam23 * d31 - lam31 * d23) + (lam31 * d12 - lam12 * d31)

/-- The discrete Arnol'd pairing step is skew-symmetric under exchanging the cumulative winding
vector `(lam12, lam23, lam31)` with the increment `(d12, d23, d31)`.
Ref: [evans-berger1992] eq. (21). -/
theorem arnoldSymplecticStep_skew
    (lam12 lam23 lam31 d12 d23 d31 : Int) :
    arnoldSymplecticStep d12 d23 d31 lam12 lam23 lam31 =
      -arnoldSymplecticStep lam12 lam23 lam31 d12 d23 d31 := by
  dsimp [arnoldSymplecticStep]
  have h1 : d12 * lam23 = lam23 * d12 := Int.mul_comm d12 lam23
  have h2 : d23 * lam12 = lam12 * d23 := Int.mul_comm d23 lam12
  have h3 : d23 * lam31 = lam31 * d23 := Int.mul_comm d23 lam31
  have h4 : d31 * lam23 = lam23 * d31 := Int.mul_comm d31 lam23
  have h5 : d31 * lam12 = lam12 * d31 := Int.mul_comm d31 lam12
  have h6 : d12 * lam31 = lam31 * d12 := Int.mul_comm d12 lam31
  omega

/-- Radial increments proportional to the cumulative winding vector contribute zero Arnol'd area
(`dλ_{ij} ∧ dλ_{ij} = 0`).
Ref: [evans-berger1992] eq. (21). -/
theorem arnoldSymplecticStep_self_zero (a b c : Int) :
    arnoldSymplecticStep a b c a b c = 0 := by
  dsimp [arnoldSymplecticStep]
  have h1 : b * a = a * b := Int.mul_comm b a
  have h2 : c * b = b * c := Int.mul_comm c b
  have h3 : a * c = c * a := Int.mul_comm a c
  omega

/-- Cyclic permutation `(12, 23, 31) ↦ (23, 31, 12)` of the three strand pairs preserves the
Arnol'd symplectic step identically.
Ref: [evans-berger1992] eq. (22). -/
theorem arnoldSymplecticStep_cyclic_invariant
    (lam12 lam23 lam31 d12 d23 d31 : Int) :
    arnoldSymplecticStep lam23 lam31 lam12 d23 d31 d12 =
      arnoldSymplecticStep lam12 lam23 lam31 d12 d23 d31 := by
  dsimp [arnoldSymplecticStep]
  omega

/-- Twice the basepoint-symmetrized Evans-Berger / Magnus commutator invariant on a 3-period
two-generator braid word with block increments `(a1, b1), (a2, b2), (a3, b3)` on pairs `(12, 23)`:
`2 Ψ_{123} = ∑_{r < s} (a_r b_s - b_r a_s)`.
Ref: [evans-berger1992] §3, eq. (22). -/
def evansBergerThreeBlockCommutator2x
    (a1 b1 a2 b2 a3 b3 : Int) : Int :=
  (a1 * b2 - b1 * a2) + (a1 * b3 - b1 * a3) + (a2 * b3 - b2 * a3)

/-- A pure single-pair Hopf braid (`b1 = b2 = b3 = 0`) has identically zero Evans-Berger triple
winding (`qou-0seq`).
Ref: [evans-berger1992] §3. -/
theorem evansBergerThreeBlockCommutator2x_hopf_zero (a1 a2 a3 : Int) :
    evansBergerThreeBlockCommutator2x a1 0 a2 0 a3 0 = 0 := by
  dsimp [evansBergerThreeBlockCommutator2x]
  omega

/-- On the 3-period Borromean pure braid `B_3 = (σ_1 σ_2^{-1})^3`, the three pure-braid periods
carry increments `(1, 0), (-1, 1), (0, -1)` in the abelianized pair coordinates `(λ_{12}, λ_{23})`,
yielding total pairwise linking `(0, 0)` and non-zero Evans-Berger triple commutator
`evansBergerThreeBlockCommutator2x 1 0 (-1) 1 0 (-1) = 1` (`|μ̄(123)| = 1`).
Ref: [evans-berger1992] §4. -/
theorem borromeanPureBraid_evansBergerCommutator_eq_one :
    (1 + (-1) + 0 : Int) = 0 ∧
    (0 + 1 + (-1) : Int) = 0 ∧
    evansBergerThreeBlockCommutator2x 1 0 (-1) 1 0 (-1) = 1 := by
  dsimp [evansBergerThreeBlockCommutator2x]
  omega

/-- Prepending a full Hopf spectator twist `(h, 0)` at the start and `(-h, 0)` at the end of a
balanced pure braid with total `Δλ_{23} = b1 + b2 + b3 = 0` contributes `h * (b1 + b2 + b3) = 0`
to the commutator pairing, proving that a balanced Hopf spectator decouples from `Ψ_{123}`.
Ref: [evans-berger1992] eq. (22). -/
theorem evansBergerSpectatorDecoupling
    (h b1 b2 b3 : Int) (hbal : b1 + b2 + b3 = 0) :
    h * b1 + h * b2 + h * b3 = 0 := by
  have h1 : h * b1 + h * b2 = h * (b1 + b2) := (Int.mul_add h b1 b2).symm
  have h2 : h * (b1 + b2) + h * b3 = h * (b1 + b2 + b3) := (Int.mul_add h (b1 + b2) b3).symm
  rw [h1, h2, hbal, Int.mul_zero]

/-!
# Section 2: Takata / Hoste-Shanahan Twist-Knot A-Polynomial Recursion (`qou-dvqx`, `qou-e1me`)

Ref: [takata2004] T. Takata, "The colored Jones polynomial and the A-polynomial for twist knots",
arXiv:math/0401068v1 (2004), Theorem 2.2, Theorem 3.1 (quoting Hoste-Shanahan), & §4.
Ref: [le2006] T. T. Q. Le, "The colored Jones polynomial and the A-polynomial of knots",
Adv. Math. 207 (2006), 782-804 (proving the AJ conjecture for all twist knots).
-/

/-- Hoste-Shanahan / Takata transfer trace polynomial `c(l, m^2)` (with `m2 = m^2`):
`c(l, m) = -l + l^2 + 2 l m^2 + m^4 + 2 l m^4 + l^2 m^4 + 2 l m^6 + m^8 - l m^8`.
Ref: [takata2004] Theorem 3.1, eqs. after (6). -/
def takataTransferTrace (l m2 : Int) : Int :=
  -l + l * l + 2 * l * m2 + m2 * m2 + 2 * l * (m2 * m2) +
    (l * l) * (m2 * m2) + 2 * l * (m2 * m2 * m2) + (m2 * m2 * m2 * m2) - l * (m2 * m2 * m2 * m2)

/-- Hoste-Shanahan / Takata transfer determinant polynomial `d(l, m^2) = m^4 (l + m^2)^4`
(with `m2 = m^2`).
Ref: [takata2004] Theorem 3.1, eqs. after (6). -/
def takataTransferDet (l m2 : Int) : Int :=
  (m2 * m2) * ((l + m2) * (l + m2) * (l + m2) * (l + m2))

/-- Takata trefoil seed `A_{K_1}(l, m) = l + m^6` (with `m2 = m^2`).
Ref: [takata2004] Theorem 3.1. -/
def takataTrefoilSeed (l m2 : Int) : Int :=
  l + m2 * m2 * m2

/-- Takata figure-eight (`4_1 = K_{-1}`) seed:
`A_{K_{-1}}(l, m) = -l + l m^2 + m^4 + 2 l m^4 + l^2 m^4 + l m^6 - l m^8` (with `m2 = m^2`).
Ref: [takata2004] Theorem 3.1. -/
def takataFigureEightSeed (l m2 : Int) : Int :=
  -l + l * m2 + m2 * m2 + 2 * l * (m2 * m2) + (l * l) * (m2 * m2) +
    l * (m2 * m2 * m2) - l * (m2 * m2 * m2 * m2)

/-- Two-term Hoste-Shanahan recursion step `A_{K_p} = c(l, m^2) A_{K_{p-1}} - d(l, m^2) A_{K_{p-2}}`.
Ref: [takata2004] Theorem 3.1; [le2006]. -/
def takataHosteShanahanStep (aPrev aPrev2 l m2 : Int) : Int :=
  takataTransferTrace l m2 * aPrev - takataTransferDet l m2 * aPrev2

/-- Exact specialization of `takataFigureEightSeed` at the trivial meridian `m^2 = 1`:
`A_{K_{-1}}(l, 1) = (l + 1)^2 = l^2 + 2 l + 1`, exhibiting the double root at `l = -1` (`qou-e1me`).
Ref: [takata2004] Theorem 3.1. -/
theorem takataFigureEightSeed_at_m2_one (l : Int) :
    takataFigureEightSeed l 1 = l * l + 2 * l + 1 ∧
    takataFigureEightSeed (-1) 1 = 0 := by
  dsimp [takataFigureEightSeed]
  omega

/-- Exact coefficient comparison (`qou-e1me`) between Takata's `A_{K_{-1}}(-L, M)` and the balanced
CCGLS figure-eight A-polynomial numerator
`L^2 M^4 + (L M^8 - L M^6 - 2 L M^4 - L M^2 + L) + M^4`:
under `l = -L` and `m2 = M^2`, the two polynomials are identically equal.
Ref: [takata2004] Theorem 3.1. -/
theorem takataFigureEightSeed_eq_ccgls_balanced (L m2 : Int) :
    takataFigureEightSeed (-L) m2 =
      (L * L) * (m2 * m2) +
        (L * (m2 * m2 * m2 * m2) - L * (m2 * m2 * m2) -
          2 * L * (m2 * m2) - L * m2 + L) +
        m2 * m2 := by
  dsimp [takataFigureEightSeed]
  have h1 : (-L) * (-L) = L * L := Int.neg_mul_neg L L
  have h2 : (-L) * m2 = -(L * m2) := Int.neg_mul L m2
  have h3 : 2 * (-L) * (m2 * m2) = -(2 * L * (m2 * m2)) := by
    have h3a : 2 * (-L) = -(2 * L) := Int.mul_neg 2 L
    rw [h3a, Int.neg_mul]
  have h4 : (-L) * (m2 * m2 * m2) = -(L * (m2 * m2 * m2)) := Int.neg_mul L (m2 * m2 * m2)
  have h5 : (-L) * (m2 * m2 * m2 * m2) = -(L * (m2 * m2 * m2 * m2)) :=
    Int.neg_mul L (m2 * m2 * m2 * m2)
  rw [h1, h2, h3, h4, h5]
  omega

/-- Classical `q → 1` specialization of `takataTransferTrace`, `takataTransferDet`, and
`takataTrefoilSeed` at `m^2 = 1`:
`c(l, 1) = 2 (l + 1)^2 = 2 l^2 + 4 l + 2`, `d(l, 1) = (l + 1)^4`, and `A_{K_1}(l, 1) = l + 1`
(`qou-dvqx`).
Ref: [takata2004] Theorem 2.2 & Theorem 3.1; [le2006]. -/
theorem takataTransfer_at_m2_one (l : Int) :
    takataTransferTrace l 1 = 2 * (l * l) + 4 * l + 2 ∧
    takataTransferDet l 1 = (l + 1) * (l + 1) * (l + 1) * (l + 1) ∧
    takataTrefoilSeed l 1 = l + 1 := by
  dsimp [takataTransferTrace, takataTransferDet, takataTrefoilSeed]
  refine ⟨?_, ?_, ?_⟩
  · omega
  · omega
  · omega

end QOU.BraidKnot
