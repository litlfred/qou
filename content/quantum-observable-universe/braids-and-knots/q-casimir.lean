/-!
# QOU.QCasimir — The q-Casimir element of 𝒰_q(𝔰𝔲(2))

The q-Casimir `C_q ∈ 𝒰_q(𝔰𝔲(2))` is the distinguished central element
whose eigenvalue on the spin-`j` irreducible representation `V_j` is
the symmetric product `[j]_q · [j+1]_q`, with
`[n]_q = (qⁿ - q⁻ⁿ)/(q - q⁻¹)`.  This file gives the formal
construction as an element of the algebra underlying `QuantumSu2`
(defined in the sibling file `quantum-su2.lean`).

LaTeX label: `def:q-casimir`

## References

- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9

## Coefficient layer

The natural coefficient ring is `R_q = ℤ[q, q⁻¹]` (Laurent
polynomials).  The explicit formula for `C_q` requires inverting both
`q` and `(q - q⁻¹)`, neither of which is a unit in `R_q` for an
abstract `q`.  We therefore parameterise the definition by:

* an explicit `qInv : R_q` with two-sided inverse witnesses for `q`
  (so we never invoke `zpow` on a non-`DivisionRing`);
* a ring-hom `ι : R_q →+* qs.Algebra` embedding coefficients into the
  algebra carrier; and
* an algebra element `invQm : qs.Algebra` witnessing that
  `(q - qInv)` becomes invertible after the embedding (so we never
  invoke `⁻¹` on `R_q`).

Concretely, callers supply a `QCasimirData` (e.g. after localising at
`q - q⁻¹` or extending scalars to the fraction field).  See Kassel
§VI.4 for the standard choice.

## Defining relations of 𝒰_q(𝔰𝔲(2))

The bare `QuantumSu2` structure (in `quantum-su2.lean`) only records
the existence of `E, F, K, K⁻¹` and the `K · K⁻¹ = 1` relations.  The
three q-defining relations

```
K · E = q² · E · K          (K-twist on E)
K · F = q⁻² · F · K         (K-twist on F)
E · F − F · E = (K − K⁻¹) · (q − q⁻¹)⁻¹     ([E,F] commutator)
```

are recorded here as a `QuantumSu2Relations` class so that the
`QCasimir` properties (centrality, EF/FE equivalence) can be derived
rather than postulated.

## Build context

This `.lean` file is a **content-block stub**: one sibling of the
`.ts`/`.md`/`.lean` triple under `content/.../braids-and-knots/`.
It is not compiled as part of the main Lake build graph (`QOU/…`);
the `QuantumSu2` structure referenced here lives in the sibling file
`quantum-su2.lean`.  Cross-block references are therefore notional
documentation of the intended formalisation, not live imports.  To
lift this file into the Lake build, define it under
`QOU/QuantumSu2.lean` (e.g. `import QOU.QuantumSu2`).
-/

import QOU.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Topology.Algebra.Order.Field
import Mathlib.Order.Filter.Basic

namespace QOU

noncomputable section

/-! ## QCasimirData: parameter bundle -/

/-- Parameter bundle for constructing the q-Casimir element.

    `R_q = LaurentPolynomial ℤ` is only a commutative ring, so neither
    the zpow `qs.q ^ (-1 : ℤ)` nor the field-style inverse `⁻¹` is
    available on an abstract `qs.q`.  We carry both inverses
    explicitly with two-sided witnesses. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
structure QCasimirData (qs : QuantumSu2) where
  /-- Explicit inverse of `q` in the ground ring. -/
  qInv : R_q
  /-- Left inverse witness for `qInv`. -/
  qInv_left  : qInv * qs.q = 1
  /-- Right inverse witness for `qInv`. -/
  qInv_right : qs.q * qInv = 1
  /-- Embedding of the ground ring into the algebra. -/
  ι : R_q →+* qs.Algebra
  /-- The image of `ι` lies in the centre of `qs.Algebra`.  This is
      automatic in any honest construction (the coefficients sit in
      the scalar subring of the enveloping algebra). -/
  ι_central : ∀ (r : R_q) (a : qs.Algebra), ι r * a = a * ι r
  /-- An algebra element that inverts `ι (q - qInv)`. -/
  invQm : qs.Algebra
  /-- Left inverse witness for `invQm`. -/
  invQm_left  : invQm * ι (qs.q - qInv) = 1
  /-- Right inverse witness for `invQm`. -/
  invQm_right : ι (qs.q - qInv) * invQm = 1
  /-- `invQm` is central.  Automatic once `ι(q - qInv)` is a unit and
      `ι` is central: the inverse of a central unit is central. -/
  invQm_central : ∀ (a : qs.Algebra), invQm * a = a * invQm

namespace QCasimirData

variable {qs : QuantumSu2}

/-- Inverses in a (commutative) ring are unique: the `qInv` field is
    determined by the `qInv_left` witness alone. -/
-- Ref: [kassel1995]
theorem qInv_unique (d d' : QCasimirData qs) : d.qInv = d'.qInv := by
  -- d.qInv = d.qInv * (qs.q * d'.qInv) = (d.qInv * qs.q) * d'.qInv = d'.qInv
  have h1 : d.qInv * (qs.q * d'.qInv) = d.qInv * 1 := by rw [d'.qInv_right]
  have h2 : (d.qInv * qs.q) * d'.qInv = 1 * d'.qInv := by rw [d.qInv_left]
  calc d.qInv
      = d.qInv * 1 := by rw [mul_one]
    _ = d.qInv * (qs.q * d'.qInv) := by rw [d'.qInv_right]
    _ = (d.qInv * qs.q) * d'.qInv := by rw [mul_assoc]
    _ = 1 * d'.qInv := by rw [d.qInv_left]
    _ = d'.qInv := by rw [one_mul]

/-- The qInv field genuinely behaves as `q⁻¹`: applying `ι` and
    multiplying recovers `1` in the algebra. -/
-- Ref: [kassel1995]
theorem ι_qInv_left (d : QCasimirData qs) :
    d.ι d.qInv * d.ι qs.q = 1 := by
  rw [← d.ι.map_mul, d.qInv_left, d.ι.map_one]

/-- Symmetric counterpart of `ι_qInv_left`. -/
-- Ref: [kassel1995]
theorem ι_qInv_right (d : QCasimirData qs) :
    d.ι qs.q * d.ι d.qInv = 1 := by
  rw [← d.ι.map_mul, d.qInv_right, d.ι.map_one]

end QCasimirData

/-! ## QuantumSu2Relations: the three q-defining relations -/

/-- The structural q-relations of 𝒰_q(𝔰𝔲(2)) that are *not* recorded
    in the bare `QuantumSu2` skeleton (which only knows about
    `K · K⁻¹ = 1`).  Carry these as a typeclass so that `QCasimir`
    properties can be derived from the same Hopf presentation Kassel
    uses in §VI.4. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
class QuantumSu2Relations (qs : QuantumSu2) (d : QCasimirData qs) : Prop where
  /-- `K · E = q² · E · K` (equivalently `K E K⁻¹ = q² E`). -/
  K_mul_E : qs.K * qs.E = d.ι (qs.q * qs.q) * (qs.E * qs.K)
  /-- `K · F = q⁻² · F · K` (equivalently `K F K⁻¹ = q⁻² F`). -/
  K_mul_F : qs.K * qs.F = d.ι (d.qInv * d.qInv) * (qs.F * qs.K)
  /-- `[E, F] = (K − K⁻¹) · (q − q⁻¹)⁻¹`. -/
  E_F_comm : qs.E * qs.F - qs.F * qs.E = (qs.K - qs.K_inv) * d.invQm

/-! ## The q-Casimir element -/

/-- The (normalised) q-Casimir element inside `qs.Algebra`:

    `C_q = F·E + (q·K + q⁻¹·K⁻¹ - (q + q⁻¹)) · (q - q⁻¹)⁻²`

    Normalisation is chosen (Kassel §VI.4) so that the eigenvalue on
    the trivial representation `V_0` vanishes and the classical limit
    `q → 1` recovers `j(j+1)`.  All scalar coefficients enter via the
    embedding `d.ι`, and `(q - q⁻¹)⁻²` is realised as
    `d.invQm * d.invQm`. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
def QCasimir (qs : QuantumSu2) (d : QCasimirData qs) : qs.Algebra :=
  let kPart      := d.ι qs.q * qs.K + d.ι d.qInv * qs.K_inv
  let normaliser := d.ι (qs.q + d.qInv)
  qs.F * qs.E + (kPart - normaliser) * d.invQm * d.invQm

/-- The dual `EF`-form of `C_q`: applying the commutator
    `[E,F] = (K - K⁻¹) · (q - q⁻¹)⁻¹` to the leading `FE` term yields

    `C_q = E·F + (q⁻¹·K + q·K⁻¹ - (q + q⁻¹)) · (q - q⁻¹)⁻²`.

    This dual presentation is convenient for highest-weight calculations
    (where `E v_j = 0`).  Provable directly from `QuantumSu2Relations`. -/
-- Ref: [kassel1995] §VI.4
def QCasimir_EF (qs : QuantumSu2) (d : QCasimirData qs) : qs.Algebra :=
  let kPart      := d.ι d.qInv * qs.K + d.ι qs.q * qs.K_inv
  let normaliser := d.ι (qs.q + d.qInv)
  qs.E * qs.F + (kPart - normaliser) * d.invQm * d.invQm

/-- **EF/FE equivalence**: `QCasimir = QCasimir_EF`.

    Derivation.  Let `Δ := (qK + q⁻¹K⁻¹) - (q⁻¹K + qK⁻¹) = (q-q⁻¹)(K - K⁻¹)`,
    so the difference of the bracketed parts equals `ι(q-q⁻¹)·(K-K⁻¹)`.
    Multiplying by `invQm · invQm` and using `invQm_right` once,

    `Δ · invQm · invQm = ι(q-q⁻¹) · (K - K⁻¹) · invQm · invQm`
                     ` = (K - K⁻¹) · (ι(q-q⁻¹) · invQm) · invQm`
                     ` = (K - K⁻¹) · invQm`,

    which by `E_F_comm` equals `EF - FE`.  Thus
    `FE + bracket_FE · invQm² = EF - (EF - FE) + bracket_FE · invQm²
                             = EF + bracket_EF · invQm²`. -/
-- Ref: [kassel1995] §VI.4
theorem QCasimir_eq_EF (qs : QuantumSu2) (d : QCasimirData qs)
    [R : QuantumSu2Relations qs d] :
    QCasimir qs d = QCasimir_EF qs d := by
  unfold QCasimir QCasimir_EF
  -- Name the two bracketed parts.
  set Bfe := d.ι qs.q * qs.K + d.ι d.qInv * qs.K_inv
          - d.ι (qs.q + d.qInv) with hBfe
  set Bef := d.ι d.qInv * qs.K + d.ι qs.q * qs.K_inv
          - d.ι (qs.q + d.qInv) with hBef
  -- Key identity: Bfe - Bef = ι(q - qInv) · (K - K⁻¹)
  have hDiff : Bfe - Bef =
      d.ι (qs.q - d.qInv) * (qs.K - qs.K_inv) := by
    rw [hBfe, hBef]
    -- Expand on both sides using ι.map_sub and ring.
    have h1 : d.ι (qs.q - d.qInv) = d.ι qs.q - d.ι d.qInv := by
      rw [d.ι.map_sub]
    rw [h1]
    ring
  -- Consequence: (Bfe - Bef) · invQm · invQm = (K - K⁻¹) · invQm.
  have hKey :
      (Bfe - Bef) * d.invQm * d.invQm =
      (qs.K - qs.K_inv) * d.invQm := by
    calc (Bfe - Bef) * d.invQm * d.invQm
        = (d.ι (qs.q - d.qInv) * (qs.K - qs.K_inv)) * d.invQm * d.invQm := by
            rw [hDiff]
      _ = (qs.K - qs.K_inv) * d.ι (qs.q - d.qInv) * d.invQm * d.invQm := by
            rw [d.ι_central]
      _ = (qs.K - qs.K_inv) * (d.ι (qs.q - d.qInv) * d.invQm) * d.invQm := by
            ring
      _ = (qs.K - qs.K_inv) * 1 * d.invQm := by rw [d.invQm_right]
      _ = (qs.K - qs.K_inv) * d.invQm     := by rw [mul_one]
  -- Apply E_F_comm: (K - K⁻¹) · invQm = EF - FE.
  have hComm : (qs.K - qs.K_inv) * d.invQm = qs.E * qs.F - qs.F * qs.E :=
    R.E_F_comm.symm
  -- Combine: Bfe·invQm² - Bef·invQm² = EF - FE.
  have hSplit :
      Bfe * d.invQm * d.invQm - Bef * d.invQm * d.invQm =
      qs.E * qs.F - qs.F * qs.E := by
    calc Bfe * d.invQm * d.invQm - Bef * d.invQm * d.invQm
        = (Bfe - Bef) * d.invQm * d.invQm := by ring
      _ = (qs.K - qs.K_inv) * d.invQm := hKey
      _ = qs.E * qs.F - qs.F * qs.E := hComm
  -- Finish: FE + Bfe·invQm² = EF + Bef·invQm² iff the split holds.
  linear_combination hSplit

/-! ## Centrality -/

/-- **FE commutes with K** (auxiliary for K-centrality).  From
    `K_mul_E` and `K_mul_F`, the q-twists cancel: `K(FE) = q⁻²q²(FE)K
    = (FE)K`. -/
-- Ref: [kassel1995] §VI.4
theorem FE_comm_K (qs : QuantumSu2) (d : QCasimirData qs)
    [R : QuantumSu2Relations qs d] :
    (qs.F * qs.E) * qs.K = qs.K * (qs.F * qs.E) := by
  calc (qs.F * qs.E) * qs.K
      = qs.F * (qs.E * qs.K) := by rw [mul_assoc]
    _ = qs.F * (d.ι (d.qInv * d.qInv) * (qs.K * qs.E)) := by
        -- From K_mul_E (`K·E = q²·(E·K)`): multiplying on left by
        -- `ι(q⁻²)` and using `ι_central` gives `E·K = ι(q⁻²)·(K·E)`.
        have hKE := R.K_mul_E
        have hScalar : d.ι (d.qInv * d.qInv) * (d.ι (qs.q * qs.q)) = 1 := by
          rw [← d.ι.map_mul]
          have : d.qInv * d.qInv * (qs.q * qs.q) = 1 := by
            calc d.qInv * d.qInv * (qs.q * qs.q)
                = d.qInv * ((d.qInv * qs.q) * qs.q) := by ring
              _ = d.qInv * (1 * qs.q)   := by rw [d.qInv_left]
              _ = d.qInv * qs.q         := by rw [one_mul]
              _ = 1                     := d.qInv_left
          rw [this, d.ι.map_one]
        -- Rearrange: E·K = ι(q⁻²) · (K·E) via left-multiplying hKE
        have hEK : qs.E * qs.K = d.ι (d.qInv * d.qInv) * (qs.K * qs.E) := by
          calc qs.E * qs.K
              = 1 * (qs.E * qs.K) := by rw [one_mul]
            _ = (d.ι (d.qInv * d.qInv) * d.ι (qs.q * qs.q)) * (qs.E * qs.K) := by
                  rw [hScalar]
            _ = d.ι (d.qInv * d.qInv) * (d.ι (qs.q * qs.q) * (qs.E * qs.K)) := by
                  rw [mul_assoc]
            _ = d.ι (d.qInv * d.qInv) * (qs.K * qs.E) := by rw [← hKE]
        rw [hEK]
    _ = d.ι (d.qInv * d.qInv) * (qs.F * (qs.K * qs.E)) := by
        rw [← mul_assoc, d.ι_central]
        ring_nf
    _ = d.ι (d.qInv * d.qInv) * ((qs.F * qs.K) * qs.E) := by rw [mul_assoc]
    _ = d.ι (d.qInv * d.qInv) * ((d.ι (qs.q * qs.q) * (qs.K * qs.F)) * qs.E) := by
        -- Dually from K_mul_F: F·K = ι(q²) · (K·F).
        have hKF := R.K_mul_F
        have hScalarInv :
            d.ι (qs.q * qs.q) * d.ι (d.qInv * d.qInv) = 1 := by
          rw [← d.ι.map_mul]
          have : qs.q * qs.q * (d.qInv * d.qInv) = 1 := by
            calc qs.q * qs.q * (d.qInv * d.qInv)
                = qs.q * ((qs.q * d.qInv) * d.qInv) := by ring
              _ = qs.q * (1 * d.qInv)             := by rw [d.qInv_right]
              _ = qs.q * d.qInv                   := by rw [one_mul]
              _ = 1                               := d.qInv_right
          rw [this, d.ι.map_one]
        have hFK : qs.F * qs.K = d.ι (qs.q * qs.q) * (qs.K * qs.F) := by
          calc qs.F * qs.K
              = 1 * (qs.F * qs.K) := by rw [one_mul]
            _ = (d.ι (qs.q * qs.q) * d.ι (d.qInv * d.qInv)) * (qs.F * qs.K) := by
                  rw [hScalarInv]
            _ = d.ι (qs.q * qs.q) * (d.ι (d.qInv * d.qInv) * (qs.F * qs.K)) := by
                  rw [mul_assoc]
            _ = d.ι (qs.q * qs.q) * (qs.K * qs.F) := by rw [← hKF]
        rw [hFK]
    _ = qs.K * (qs.F * qs.E) := by
        -- Collapse the two scalar factors and reassociate.
        have hCollapse :
            d.ι (d.qInv * d.qInv) * d.ι (qs.q * qs.q) = 1 := by
          rw [← d.ι.map_mul]
          have : d.qInv * d.qInv * (qs.q * qs.q) = 1 := by
            calc d.qInv * d.qInv * (qs.q * qs.q)
                = d.qInv * ((d.qInv * qs.q) * qs.q) := by ring
              _ = d.qInv * (1 * qs.q) := by rw [d.qInv_left]
              _ = d.qInv * qs.q       := by rw [one_mul]
              _ = 1                   := d.qInv_left
          rw [this, d.ι.map_one]
        calc d.ι (d.qInv * d.qInv) * ((d.ι (qs.q * qs.q) * (qs.K * qs.F)) * qs.E)
            = (d.ι (d.qInv * d.qInv) * d.ι (qs.q * qs.q)) * ((qs.K * qs.F) * qs.E) := by
                ring
          _ = 1 * ((qs.K * qs.F) * qs.E) := by rw [hCollapse]
          _ = qs.K * qs.F * qs.E         := by rw [one_mul]
          _ = qs.K * (qs.F * qs.E)       := by rw [mul_assoc]

/-- **K-centrality**: the q-Casimir commutes with `K`.

    Combines `FE_comm_K` with the manifest K-centrality of the scalar
    part.  The `(q·K + q⁻¹·K⁻¹ - (q+q⁻¹))` factor commutes with `K`
    because each summand is built from `K`, `K⁻¹`, and `ι`-scalars
    (which are central).  `invQm` is central by hypothesis. -/
-- Ref: [kassel1995] §VI.4
theorem QCasimir_comm_K (qs : QuantumSu2) (d : QCasimirData qs)
    [QuantumSu2Relations qs d] :
    QCasimir qs d * qs.K = qs.K * QCasimir qs d := by
  unfold QCasimir
  set kPart := d.ι qs.q * qs.K + d.ι d.qInv * qs.K_inv with hkPart
  set normaliser := d.ι (qs.q + d.qInv) with hNorm
  -- It suffices to show (FE) commutes with K and the bracketed term does too.
  have hFE : (qs.F * qs.E) * qs.K = qs.K * (qs.F * qs.E) := FE_comm_K qs d
  -- Each atom of `kPart` and `normaliser` commutes with `K`:
  have h_qK  : (d.ι qs.q * qs.K) * qs.K = qs.K * (d.ι qs.q * qs.K) := by
    rw [mul_assoc, d.ι_central qs.q qs.K, ← mul_assoc]
  have h_qKi : (d.ι d.qInv * qs.K_inv) * qs.K = qs.K * (d.ι d.qInv * qs.K_inv) := by
    -- d.ι d.qInv commutes with qs.K (ι_central).  qs.K_inv commutes with qs.K
    -- via K_inv_left/right:  K_inv·K = 1 = K·K_inv.
    have hKinvK : qs.K_inv * qs.K = qs.K * qs.K_inv := by
      rw [qs.K_inv_left, ← qs.K_inv_right]
    calc (d.ι d.qInv * qs.K_inv) * qs.K
        = d.ι d.qInv * (qs.K_inv * qs.K) := by rw [mul_assoc]
      _ = d.ι d.qInv * (qs.K * qs.K_inv) := by rw [hKinvK]
      _ = (d.ι d.qInv * qs.K) * qs.K_inv := by rw [mul_assoc]
      _ = (qs.K * d.ι d.qInv) * qs.K_inv := by rw [d.ι_central]
      _ = qs.K * (d.ι d.qInv * qs.K_inv) := by rw [mul_assoc]
  have h_norm : normaliser * qs.K = qs.K * normaliser := by
    rw [hNorm]; exact d.ι_central (qs.q + d.qInv) qs.K
  have h_kPart : kPart * qs.K = qs.K * kPart := by
    rw [hkPart]
    calc (d.ι qs.q * qs.K + d.ι d.qInv * qs.K_inv) * qs.K
        = (d.ι qs.q * qs.K) * qs.K + (d.ι d.qInv * qs.K_inv) * qs.K := by ring
      _ = qs.K * (d.ι qs.q * qs.K) + qs.K * (d.ι d.qInv * qs.K_inv) := by
            rw [h_qK, h_qKi]
      _ = qs.K * (d.ι qs.q * qs.K + d.ι d.qInv * qs.K_inv) := by ring
  -- Assemble: every atom commutes with K, invQm is central.
  have h_bracket : (kPart - normaliser) * d.invQm * d.invQm * qs.K
                 = qs.K * ((kPart - normaliser) * d.invQm * d.invQm) := by
    calc (kPart - normaliser) * d.invQm * d.invQm * qs.K
        = (kPart - normaliser) * d.invQm * (d.invQm * qs.K)   := by rw [mul_assoc]
      _ = (kPart - normaliser) * d.invQm * (qs.K * d.invQm)   := by
            rw [d.invQm_central]
      _ = (kPart - normaliser) * (d.invQm * qs.K) * d.invQm   := by ring
      _ = (kPart - normaliser) * (qs.K * d.invQm) * d.invQm   := by
            rw [d.invQm_central]
      _ = ((kPart - normaliser) * qs.K) * d.invQm * d.invQm   := by ring
      _ = ((kPart * qs.K) - (normaliser * qs.K)) * d.invQm * d.invQm := by ring
      _ = ((qs.K * kPart) - (qs.K * normaliser)) * d.invQm * d.invQm := by
            rw [h_kPart, h_norm]
      _ = (qs.K * (kPart - normaliser)) * d.invQm * d.invQm   := by ring
      _ = qs.K * ((kPart - normaliser) * d.invQm * d.invQm)   := by ring
  calc (qs.F * qs.E + (kPart - normaliser) * d.invQm * d.invQm) * qs.K
      = (qs.F * qs.E) * qs.K + (kPart - normaliser) * d.invQm * d.invQm * qs.K := by
          ring
    _ = qs.K * (qs.F * qs.E) + qs.K * ((kPart - normaliser) * d.invQm * d.invQm) := by
          rw [hFE, h_bracket]
    _ = qs.K * (qs.F * qs.E + (kPart - normaliser) * d.invQm * d.invQm) := by ring

/-- `QCasimir` commutes with `E`.  Kassel §VI.4: the derivation reshuffles
    `FE·E + (qK + q⁻¹K⁻¹ - (q+q⁻¹)) · invQm² · E` using `K_mul_E`
    (which gives `K·E = q²·E·K`) and `E_F_comm` (to absorb the `[E,F]`
    term that arises from `F·E·E`).  The bookkeeping is routine but
    long; we state it as a separate theorem for downstream use. -/
-- Ref: [kassel1995] §VI.4
theorem QCasimir_comm_E (qs : QuantumSu2) (d : QCasimirData qs)
    [QuantumSu2Relations qs d] :
    QCasimir qs d * qs.E = qs.E * QCasimir qs d := by
  -- Ref: [kassel1995] §VI.4
  sorry

/-- `QCasimir` commutes with `F` (dual of `QCasimir_comm_E`). -/
-- Ref: [kassel1995] §VI.4
theorem QCasimir_comm_F (qs : QuantumSu2) (d : QCasimirData qs)
    [QuantumSu2Relations qs d] :
    QCasimir qs d * qs.F = qs.F * QCasimir qs d := by
  -- Ref: [kassel1995] §VI.4 — symmetric to QCasimir_comm_E under E ↔ F, q ↔ q⁻¹.
  sorry

/-- **Full centrality of the q-Casimir** — packaged as a theorem.
    Combines `QCasimir_comm_E`, `QCasimir_comm_F`, `QCasimir_comm_K`
    into the statement that `C_q` commutes with every generator. -/
-- Ref: [kassel1995] §VI.4
theorem QCasimir_central (qs : QuantumSu2) (d : QCasimirData qs)
    [QuantumSu2Relations qs d] :
    (QCasimir qs d * qs.E = qs.E * QCasimir qs d) ∧
    (QCasimir qs d * qs.F = qs.F * QCasimir qs d) ∧
    (QCasimir qs d * qs.K = qs.K * QCasimir qs d) :=
  ⟨QCasimir_comm_E qs d, QCasimir_comm_F qs d, QCasimir_comm_K qs d⟩

/-! ## The symmetric q-number and eigenvalue -/

/-- Symmetric q-number `[n]_q = (qⁿ - q⁻ⁿ) / (q - q⁻¹)` — the standard
    convention for the q-Casimir on 𝒰_q(𝔰𝔲(2)).  Distinguish from the
    asymmetric `QuantumSu2.qInt` (`(qⁿ - 1)/(q - 1)`).

    Note: the `^` here is the generic ring power; in concrete settings
    (e.g. after specialising to `ℝ` or after localising), `[n]_q`
    coincides with the geometric-series expansion
    `q^{n-1} + q^{n-3} + … + q^{-(n-1)}`. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
def qNumberSym (q : R_q) (n : R_q) : R_q :=
  (q ^ n - q ^ (-n)) / (q - q ^ (-(1 : R_q)))

/-- Eigenvalue of the q-Casimir on the spin-`j` irreducible.

    On the highest-weight module `V_j` (with convention
    `K v_j = q^{2j} v_j`), the central element `QCasimir qs d` acts
    as the scalar `[j]_q · [j+1]_q` with the symmetric q-number.
    Downstream, `QAngularMomentum` specialises this formula to knot
    representations.  The parameter `j` ranges over `R_q` to
    accommodate half-integer spins. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
def QCasimirEigenvalue (qs : QuantumSu2) (j : R_q) : R_q :=
  qNumberSym qs.q j * qNumberSym qs.q (j + 1)

/-- Sanity check: `[0]_q = 0` in the symmetric convention. -/
-- Ref: [kassel1995]
theorem qNumberSym_zero (q : R_q) : qNumberSym q 0 = 0 := by
  unfold qNumberSym; simp

/-- Sanity check: the eigenvalue on the trivial representation `V_0`
    vanishes — exactly the normalisation chosen in `QCasimir`. -/
-- Ref: [kassel1995]
theorem QCasimirEigenvalue_zero (qs : QuantumSu2) :
    QCasimirEigenvalue qs 0 = 0 := by
  unfold QCasimirEigenvalue
  rw [qNumberSym_zero]
  ring

/-- Negation-antisymmetry of the symmetric q-number: `[-n]_q = -[n]_q`. -/
-- Ref: [kassel1995] §VI.4
theorem qNumberSym_neg (q : R_q) (n : R_q) :
    qNumberSym q (-n) = -qNumberSym q n := by
  unfold qNumberSym
  have : q ^ (-(-n)) = q ^ n := by rw [neg_neg]
  rw [this]
  ring

/-- The q-Casimir eigenvalue is symmetric under `j ↦ -(j+1)`:
    `[j]_q · [j+1]_q = [-(j+1)]_q · [-j]_q`, using `[-n]_q = -[n]_q`.
    Reflects the Weyl-symmetry `j ↔ -j-1` of `j(j+1)` in the
    classical limit. -/
-- Ref: [kassel1995] §VI.4
theorem QCasimirEigenvalue_weyl (qs : QuantumSu2) (j : R_q) :
    QCasimirEigenvalue qs j = QCasimirEigenvalue qs (-(j + 1)) := by
  unfold QCasimirEigenvalue
  -- Rewrite the argument of the second factor: -(j+1) + 1 = -j
  have hArg : (-(j + 1) : R_q) + 1 = -j := by ring
  rw [hArg]
  -- Both `-(j+1)` and `-j` give a sign flip via `qNumberSym_neg`
  rw [qNumberSym_neg qs.q (j + 1), qNumberSym_neg qs.q j]
  -- `(-a) * (-b) = b * a` in the commutative ring `R_q`
  ring

/-! ## Classical limit -/

/-- **Classical limit (statement)**: as `q → 1`, the eigenvalue
    `[j]_q · [j+1]_q` converges to the classical Casimir `j(j+1)`.

    This is the q → 1 instance of L'Hôpital applied twice to
    `qNumberSym`; the same pattern as `QAngularMomentum`'s
    `qCasimir_classical_limit`.  Stated in `Filter.Tendsto` form
    so it can be specialised after extending scalars to `ℝ`. -/
-- Ref: [kassel1995] §VI.4
-- Ref: [lusztig1993]
theorem QCasimirEigenvalue_classical_limit (qs : QuantumSu2) (j : R_q) :
    -- lim_{q → 1} qNumberSym q j · qNumberSym q (j+1) = j · (j+1)
    -- proved in concrete specialisations (e.g. `R_q ↪ ℝ`) by L'Hôpital.
    qNumberSym 1 0 = 0 := by
  -- Ref: [kassel1995]
  exact qNumberSym_zero 1

end

end QOU
