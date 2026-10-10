/-
# Isospin-mirror invariance of the strong exchange determinant

The global proton↔neutron mirror flips every nucleon's isospin label
`s ↦ -s`.  For a strong exchange matrix whose off-diagonal bond entries
carry the isospin sign `s i * s j` on top of an isospin-independent
(geometry-only) magnitude `mag i j`, this mirror leaves **every** bond
entry fixed, since `(-s i)(-s j) = s i * s j`.  The determinant — and
hence any strong binding functional built from it — is therefore
mirror-invariant: a mirror pair such as ³H (pnn) and ³He (ppn) receives
the *same* strong value, so the strong ³H/³He binding split is exactly
zero.

Consequence for the Δ_λ magnitude front (2026-07-18): the observed
~1.10× ³H/³He mirror split cannot be of strong-exchange origin.  It must
come from a `Z`-dependent (isospin-odd) term — the Coulomb energy of the
proton pair — which is *not* invariant under `s ↦ -s` because it counts
protons, not bonds.  This is a scope-(b) structural exclusion (a proved
invariant), not a scope-(a) numerical miss.

This is distinct from `QOU.MassTheory.ReebPnMagnitude.pn_sign_det_invariant`,
which proves invariance of a `4×4` exchange matrix under conjugation by a
fixed parity matrix `parityD`.  Here the mirror acts on the isospin
*labelling function* `s` at the entry level, for any number of nucleons
`n` and any symmetric geometric magnitude `mag`, so the two statements
are independent (this one needs no `s i ^ 2 = 1` and no similarity
transform).
-/
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic

namespace QOU.MassTheory

open Matrix

variable {R : Type*} [CommRing R] {n : ℕ}

/-- Strong isospin-signed exchange matrix: diagonal `1`, off-diagonal
bond `mag i j * s i * s j`, where `s : Fin n → R` is the nucleon isospin
labelling (`+1` proton / `-1` neutron, kept generic) and `mag i j` is the
isospin-independent, geometry-only bond magnitude. -/
def isospinExchange (mag : Fin n → Fin n → R) (s : Fin n → R) :
    Matrix (Fin n) (Fin n) R :=
  Matrix.of fun i j => if i = j then 1 else mag i j * s i * s j

/-- The global isospin mirror `s ↦ -s` (proton ↔ neutron on every
nucleon) fixes every entry of the strong exchange matrix, since
`(-s i)(-s j) = s i * s j`. -/
theorem isospinExchange_mirror (mag : Fin n → Fin n → R) (s : Fin n → R) :
    isospinExchange mag (fun i => -s i) = isospinExchange mag s := by
  funext i j
  simp only [isospinExchange, Matrix.of_apply]
  by_cases h : i = j
  · simp [h]
  · simp only [if_neg h]; ring

/-- **Strong-sector mirror invariance.** The isospin-signed exchange
determinant is invariant under the global proton↔neutron mirror.  Hence
any strong binding functional of this determinant assigns a mirror pair
(³H and ³He) the same value: the strong ³H/³He split is exactly zero, so
the observed ~1.10× split is non-strong (the Coulomb term). -/
theorem isospinExchange_det_mirror_invariant
    (mag : Fin n → Fin n → R) (s : Fin n → R) :
    (isospinExchange mag (fun i => -s i)).det = (isospinExchange mag s).det := by
  rw [isospinExchange_mirror]

end QOU.MassTheory
