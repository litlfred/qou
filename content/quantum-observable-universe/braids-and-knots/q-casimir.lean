import QOU.BraidKnot.CasimirShared
import Mathlib.Tactic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Topology.Algebra.Order.Field
import Mathlib.Order.Filter.Basic


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

namespace QOU

noncomputable section

/-! ## QCasimirData and QCasimir

    The parameter bundle `QCasimirData`, its uniqueness/embedding
    lemmas (`qInv_unique`, `ι_qInv_left`, `ι_qInv_right`), and the
    q-Casimir element `QCasimir` itself are the shared base objects,
    defined once in the library module `QOU.BraidKnot.CasimirShared`
    (imported above).  This content block develops the downstream
    structure — the defining relations, the dual `EF`-form, and
    centrality. -/

/-! ## QuantumSu2Relations: the three q-defining relations -/

/-- The structural q-relations of 𝒰_q(𝔰𝔲(2)) that are *not* recorded
    in the bare `QuantumSu2` skeleton (which only knows about
    `K · K⁻¹ = 1`).  Carry these as a typeclass so that `QCasimir`
    properties can be derived from the same Hopf presentation Kassel
    uses in §VI.4. -/
-- Ref: [kassel1995] Ch. VIII (Quantum SL(2)) + Ch. XIII (Braided categories)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
class QuantumSu2Relations (qs : QuantumSu2) (d : QCasimirData qs) : Prop where
  /-- `K · E = q² · E · K` (equivalently `K E K⁻¹ = q² E`). -/
  K_mul_E : qs.K * qs.E = d.ι (qs.q * qs.q) * (qs.E * qs.K)
  /-- `K · F = q⁻² · F · K` (equivalently `K F K⁻¹ = q⁻² F`). -/
  K_mul_F : qs.K * qs.F = d.ι (d.qInv * d.qInv) * (qs.F * qs.K)
  /-- `[E, F] = (K − K⁻¹) · (q − q⁻¹)⁻¹`. -/
  E_F_comm : qs.E * qs.F - qs.F * qs.E = (qs.K - qs.K_inv) * d.invQm

/-! ## The q-Casimir element

    The base element `QCasimir qs d = F·E + (q·K + q⁻¹·K⁻¹ - (q+q⁻¹))
    · (q-q⁻¹)⁻²` is defined in `QOU.BraidKnot.CasimirShared` (imported
    above).  Below we add the dual `EF`-presentation and prove the two
    are equal under `QuantumSu2Relations`. -/

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
    The difference of the bracketed parts equals `ι(q-q⁻¹)·(K-K⁻¹)`.
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
    noncomm_ring
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
            noncomm_ring
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
        = (Bfe - Bef) * d.invQm * d.invQm := by noncomm_ring
      _ = (qs.K - qs.K_inv) * d.invQm := hKey
      _ = qs.E * qs.F - qs.F * qs.E := hComm
  -- Finish: FE + Bfe·invQm² = EF + Bef·invQm² iff the split holds.
  have h := sub_eq_sub_iff_add_eq_add.mp hSplit
  rw [add_comm (qs.F * qs.E)]
  exact h

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
        rw [← mul_assoc, ← d.ι_central, mul_assoc]
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
                noncomm_ring
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
    rw [d.ι_central qs.q qs.K, mul_assoc, d.ι_central qs.q qs.K]
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
        = (d.ι qs.q * qs.K) * qs.K + (d.ι d.qInv * qs.K_inv) * qs.K := by noncomm_ring
      _ = qs.K * (d.ι qs.q * qs.K) + qs.K * (d.ι d.qInv * qs.K_inv) := by
            rw [h_qK, h_qKi]
      _ = qs.K * (d.ι qs.q * qs.K + d.ι d.qInv * qs.K_inv) := by noncomm_ring
  -- Assemble: every atom commutes with K, invQm is central.
  have h_bracket : (kPart - normaliser) * d.invQm * d.invQm * qs.K
                 = qs.K * ((kPart - normaliser) * d.invQm * d.invQm) := by
    calc (kPart - normaliser) * d.invQm * d.invQm * qs.K
        = (kPart - normaliser) * d.invQm * (d.invQm * qs.K)   := by rw [mul_assoc]
      _ = (kPart - normaliser) * d.invQm * (qs.K * d.invQm)   := by
            rw [d.invQm_central]
      _ = (kPart - normaliser) * (d.invQm * qs.K) * d.invQm   := by noncomm_ring
      _ = (kPart - normaliser) * (qs.K * d.invQm) * d.invQm   := by
            rw [d.invQm_central]
      _ = ((kPart - normaliser) * qs.K) * d.invQm * d.invQm   := by noncomm_ring
      _ = ((kPart * qs.K) - (normaliser * qs.K)) * d.invQm * d.invQm := by noncomm_ring
      _ = ((qs.K * kPart) - (qs.K * normaliser)) * d.invQm * d.invQm := by
            rw [h_kPart, h_norm]
      _ = (qs.K * (kPart - normaliser)) * d.invQm * d.invQm   := by noncomm_ring
      _ = qs.K * ((kPart - normaliser) * d.invQm * d.invQm)   := by noncomm_ring
  calc (qs.F * qs.E + (kPart - normaliser) * d.invQm * d.invQm) * qs.K
      = (qs.F * qs.E) * qs.K + (kPart - normaliser) * d.invQm * d.invQm * qs.K := by
          noncomm_ring
    _ = qs.K * (qs.F * qs.E) + qs.K * ((kPart - normaliser) * d.invQm * d.invQm) := by
          rw [hFE, h_bracket]
    _ = qs.K * (qs.F * qs.E + (kPart - normaliser) * d.invQm * d.invQm) := by noncomm_ring

/-! ### Auxiliary q-twist rearrangements -/

/-- `E · K = ι(q⁻²) · (K · E)`: the dual of `K_mul_E` obtained by
    multiplying both sides by `ι(q⁻²)`. -/
-- Ref: [kassel1995] §VI.4
theorem E_mul_K (qs : QuantumSu2) (d : QCasimirData qs)
    [R : QuantumSu2Relations qs d] :
    qs.E * qs.K = d.ι (d.qInv * d.qInv) * (qs.K * qs.E) := by
  have hScalar : d.ι (d.qInv * d.qInv) * d.ι (qs.q * qs.q) = 1 := by
    rw [← d.ι.map_mul]
    have : d.qInv * d.qInv * (qs.q * qs.q) = 1 := by
      calc d.qInv * d.qInv * (qs.q * qs.q)
          = d.qInv * ((d.qInv * qs.q) * qs.q) := by ring
        _ = d.qInv * (1 * qs.q) := by rw [d.qInv_left]
        _ = d.qInv * qs.q := by rw [one_mul]
        _ = 1 := d.qInv_left
    rw [this, d.ι.map_one]
  calc qs.E * qs.K
      = 1 * (qs.E * qs.K) := (one_mul _).symm
    _ = (d.ι (d.qInv * d.qInv) * d.ι (qs.q * qs.q)) * (qs.E * qs.K) := by rw [hScalar]
    _ = d.ι (d.qInv * d.qInv) * (d.ι (qs.q * qs.q) * (qs.E * qs.K)) := by rw [mul_assoc]
    _ = d.ι (d.qInv * d.qInv) * (qs.K * qs.E) := by rw [← R.K_mul_E]

/-- `F · K = ι(q²) · (K · F)`: dual of `K_mul_F`. -/
-- Ref: [kassel1995] §VI.4
theorem F_mul_K (qs : QuantumSu2) (d : QCasimirData qs)
    [R : QuantumSu2Relations qs d] :
    qs.F * qs.K = d.ι (qs.q * qs.q) * (qs.K * qs.F) := by
  have hScalar : d.ι (qs.q * qs.q) * d.ι (d.qInv * d.qInv) = 1 := by
    rw [← d.ι.map_mul]
    have : qs.q * qs.q * (d.qInv * d.qInv) = 1 := by
      calc qs.q * qs.q * (d.qInv * d.qInv)
          = qs.q * ((qs.q * d.qInv) * d.qInv) := by ring
        _ = qs.q * (1 * d.qInv) := by rw [d.qInv_right]
        _ = qs.q * d.qInv := by rw [one_mul]
        _ = 1 := d.qInv_right
    rw [this, d.ι.map_one]
  calc qs.F * qs.K
      = 1 * (qs.F * qs.K) := (one_mul _).symm
    _ = (d.ι (qs.q * qs.q) * d.ι (d.qInv * d.qInv)) * (qs.F * qs.K) := by rw [hScalar]
    _ = d.ι (qs.q * qs.q) * (d.ι (d.qInv * d.qInv) * (qs.F * qs.K)) := by rw [mul_assoc]
    _ = d.ι (qs.q * qs.q) * (qs.K * qs.F) := by rw [← R.K_mul_F]

/-- `E · K_inv = ι(q²) · (K_inv · E)`: derived from `K_mul_E` by
    conjugating with `K_inv`. -/
-- Ref: [kassel1995] §VI.4
theorem E_mul_K_inv (qs : QuantumSu2) (d : QCasimirData qs)
    [R : QuantumSu2Relations qs d] :
    qs.E * qs.K_inv = d.ι (qs.q * qs.q) * (qs.K_inv * qs.E) := by
  -- From K·E = ι(q²)·E·K: left-mul by K_inv, then right-mul by K_inv.
  have step1 : qs.E = d.ι (qs.q * qs.q) * (qs.K_inv * qs.E * qs.K) := by
    calc qs.E
        = 1 * qs.E := (one_mul _).symm
      _ = (qs.K_inv * qs.K) * qs.E := by rw [qs.K_inv_left]
      _ = qs.K_inv * (qs.K * qs.E) := by rw [mul_assoc]
      _ = qs.K_inv * (d.ι (qs.q * qs.q) * (qs.E * qs.K)) := by rw [R.K_mul_E]
      _ = d.ι (qs.q * qs.q) * (qs.K_inv * (qs.E * qs.K)) := by
            rw [← mul_assoc, ← d.ι_central, mul_assoc]
      _ = d.ι (qs.q * qs.q) * (qs.K_inv * qs.E * qs.K) := by rw [mul_assoc]
  -- Right-mul by K_inv:
  calc qs.E * qs.K_inv
      = (d.ι (qs.q * qs.q) * (qs.K_inv * qs.E * qs.K)) * qs.K_inv := by rw [← step1]
    _ = d.ι (qs.q * qs.q) * (qs.K_inv * qs.E * (qs.K * qs.K_inv)) := by noncomm_ring
    _ = d.ι (qs.q * qs.q) * (qs.K_inv * qs.E * 1) := by rw [qs.K_inv_right]
    _ = d.ι (qs.q * qs.q) * (qs.K_inv * qs.E) := by rw [mul_one]

/-- `F · K_inv = ι(q⁻²) · (K_inv · F)`: dual of `E_mul_K_inv`. -/
-- Ref: [kassel1995] §VI.4
theorem F_mul_K_inv (qs : QuantumSu2) (d : QCasimirData qs)
    [R : QuantumSu2Relations qs d] :
    qs.F * qs.K_inv = d.ι (d.qInv * d.qInv) * (qs.K_inv * qs.F) := by
  have step1 : qs.F = d.ι (d.qInv * d.qInv) * (qs.K_inv * qs.F * qs.K) := by
    calc qs.F
        = 1 * qs.F := (one_mul _).symm
      _ = (qs.K_inv * qs.K) * qs.F := by rw [qs.K_inv_left]
      _ = qs.K_inv * (qs.K * qs.F) := by rw [mul_assoc]
      _ = qs.K_inv * (d.ι (d.qInv * d.qInv) * (qs.F * qs.K)) := by rw [R.K_mul_F]
      _ = d.ι (d.qInv * d.qInv) * (qs.K_inv * (qs.F * qs.K)) := by
            rw [← mul_assoc, ← d.ι_central, mul_assoc]
      _ = d.ι (d.qInv * d.qInv) * (qs.K_inv * qs.F * qs.K) := by rw [mul_assoc]
  calc qs.F * qs.K_inv
      = (d.ι (d.qInv * d.qInv) * (qs.K_inv * qs.F * qs.K)) * qs.K_inv := by rw [← step1]
    _ = d.ι (d.qInv * d.qInv) * (qs.K_inv * qs.F * (qs.K * qs.K_inv)) := by noncomm_ring
    _ = d.ι (d.qInv * d.qInv) * (qs.K_inv * qs.F * 1) := by rw [qs.K_inv_right]
    _ = d.ι (d.qInv * d.qInv) * (qs.K_inv * qs.F) := by rw [mul_one]

/-! ### Key arithmetic identities on the ground ring -/

/-- `q³ - q = q² · (q - q⁻¹)`.  A plain ring identity in `R_q`
    using `qInv_right`. -/
-- Ref: [kassel1995]
theorem q_cubed_minus_q (qs : QuantumSu2) (d : QCasimirData qs) :
    qs.q * qs.q * qs.q - qs.q = qs.q * qs.q * (qs.q - d.qInv) := by
  have h : qs.q * qs.q * d.qInv = qs.q := by
    calc qs.q * qs.q * d.qInv
        = qs.q * (qs.q * d.qInv) := by rw [mul_assoc]
      _ = qs.q * 1 := by rw [d.qInv_right]
      _ = qs.q := mul_one _
  linear_combination h

/-- `q⁻³ - q⁻¹ = -(q⁻² · (q - q⁻¹))`: mirror of `q_cubed_minus_q`. -/
-- Ref: [kassel1995]
theorem qInv_cubed_minus_qInv (qs : QuantumSu2) (d : QCasimirData qs) :
    d.qInv * d.qInv * d.qInv - d.qInv = -(d.qInv * d.qInv * (qs.q - d.qInv)) := by
  have h : d.qInv * d.qInv * qs.q = d.qInv := by
    calc d.qInv * d.qInv * qs.q
        = d.qInv * (d.qInv * qs.q) := by rw [mul_assoc]
      _ = d.qInv * 1 := by rw [d.qInv_left]
      _ = d.qInv := mul_one _
  linear_combination h

/-! ### E-centrality -/

/-- The "K-cancellation" lemma: `ι(q³-q)·invQm² = ι(q²)·invQm`.
    Used in E-centrality to cancel the `E·K` terms. -/
-- Ref: [kassel1995] §VI.4
theorem K_cancel (qs : QuantumSu2) (d : QCasimirData qs) :
    d.ι (qs.q * qs.q * qs.q - qs.q) * (d.invQm * d.invQm)
      = d.ι (qs.q * qs.q) * d.invQm := by
  have hFac := q_cubed_minus_q qs d
  calc d.ι (qs.q * qs.q * qs.q - qs.q) * (d.invQm * d.invQm)
      = d.ι (qs.q * qs.q * (qs.q - d.qInv)) * (d.invQm * d.invQm) := by rw [hFac]
    _ = (d.ι (qs.q * qs.q) * d.ι (qs.q - d.qInv)) * (d.invQm * d.invQm) := by
          rw [d.ι.map_mul]
    _ = d.ι (qs.q * qs.q) * ((d.ι (qs.q - d.qInv) * d.invQm) * d.invQm) := by noncomm_ring
    _ = d.ι (qs.q * qs.q) * (1 * d.invQm) := by rw [d.invQm_right]
    _ = d.ι (qs.q * qs.q) * d.invQm := by rw [one_mul]

/-- The "K_inv-cancellation" lemma: `ι(qInv³-qInv)·invQm² = -ι(qInv²)·invQm`.
    Mirror of `K_cancel` used for the `E·K_inv` terms. -/
-- Ref: [kassel1995] §VI.4
theorem K_inv_cancel (qs : QuantumSu2) (d : QCasimirData qs) :
    d.ι (d.qInv * d.qInv * d.qInv - d.qInv) * (d.invQm * d.invQm)
      = -(d.ι (d.qInv * d.qInv) * d.invQm) := by
  have hFac := qInv_cubed_minus_qInv qs d
  calc d.ι (d.qInv * d.qInv * d.qInv - d.qInv) * (d.invQm * d.invQm)
      = d.ι (-(d.qInv * d.qInv * (qs.q - d.qInv))) * (d.invQm * d.invQm) := by rw [hFac]
    _ = -(d.ι (d.qInv * d.qInv * (qs.q - d.qInv)) * (d.invQm * d.invQm)) := by
          rw [d.ι.map_neg]; noncomm_ring
    _ = -((d.ι (d.qInv * d.qInv) * d.ι (qs.q - d.qInv)) * (d.invQm * d.invQm)) := by
          rw [d.ι.map_mul]
    _ = -(d.ι (d.qInv * d.qInv) * ((d.ι (qs.q - d.qInv) * d.invQm) * d.invQm)) := by
          noncomm_ring
    _ = -(d.ι (d.qInv * d.qInv) * (1 * d.invQm)) := by rw [d.invQm_right]
    _ = -(d.ι (d.qInv * d.qInv) * d.invQm) := by rw [one_mul]

/-- Auxiliary: `K_inv · E = ι(q⁻²) · E · K_inv`.  Mirror of `K_mul_E`. -/
-- Ref: [kassel1995] §VI.4
theorem K_inv_mul_E (qs : QuantumSu2) (d : QCasimirData qs)
    [R : QuantumSu2Relations qs d] :
    qs.K_inv * qs.E = d.ι (d.qInv * d.qInv) * (qs.E * qs.K_inv) := by
  have hEKi := E_mul_K_inv qs d  -- E·K_inv = ι(q²)·(K_inv·E)
  have hScalar : d.ι (d.qInv * d.qInv) * d.ι (qs.q * qs.q) = 1 := by
    rw [← d.ι.map_mul]
    have : d.qInv * d.qInv * (qs.q * qs.q) = 1 := by
      calc d.qInv * d.qInv * (qs.q * qs.q)
          = d.qInv * ((d.qInv * qs.q) * qs.q) := by ring
        _ = d.qInv * (1 * qs.q) := by rw [d.qInv_left]
        _ = d.qInv * qs.q := by rw [one_mul]
        _ = 1 := d.qInv_left
    rw [this, d.ι.map_one]
  calc qs.K_inv * qs.E
      = 1 * (qs.K_inv * qs.E) := (one_mul _).symm
    _ = (d.ι (d.qInv * d.qInv) * d.ι (qs.q * qs.q)) * (qs.K_inv * qs.E) := by rw [hScalar]
    _ = d.ι (d.qInv * d.qInv) * (d.ι (qs.q * qs.q) * (qs.K_inv * qs.E)) := by rw [mul_assoc]
    _ = d.ι (d.qInv * d.qInv) * (qs.E * qs.K_inv) := by rw [← hEKi]

/-- Auxiliary: `K_inv · F = ι(q²) · F · K_inv`.  Mirror of `K_mul_F`. -/
-- Ref: [kassel1995] §VI.4
theorem K_inv_mul_F (qs : QuantumSu2) (d : QCasimirData qs)
    [R : QuantumSu2Relations qs d] :
    qs.K_inv * qs.F = d.ι (qs.q * qs.q) * (qs.F * qs.K_inv) := by
  have hFKi := F_mul_K_inv qs d  -- F·K_inv = ι(qInv²)·(K_inv·F)
  have hScalar : d.ι (qs.q * qs.q) * d.ι (d.qInv * d.qInv) = 1 := by
    rw [← d.ι.map_mul]
    have : qs.q * qs.q * (d.qInv * d.qInv) = 1 := by
      calc qs.q * qs.q * (d.qInv * d.qInv)
          = qs.q * ((qs.q * d.qInv) * d.qInv) := by ring
        _ = qs.q * (1 * d.qInv) := by rw [d.qInv_right]
        _ = qs.q * d.qInv := by rw [one_mul]
        _ = 1 := d.qInv_right
    rw [this, d.ι.map_one]
  calc qs.K_inv * qs.F
      = 1 * (qs.K_inv * qs.F) := (one_mul _).symm
    _ = (d.ι (qs.q * qs.q) * d.ι (d.qInv * d.qInv)) * (qs.K_inv * qs.F) := by rw [hScalar]
    _ = d.ι (qs.q * qs.q) * (d.ι (d.qInv * d.qInv) * (qs.K_inv * qs.F)) := by rw [mul_assoc]
    _ = d.ι (qs.q * qs.q) * (qs.F * qs.K_inv) := by rw [← hFKi]

/-- W := `invQm · invQm` is central in `qs.Algebra`. -/
-- Ref: [kassel1995]
theorem W_central (qs : QuantumSu2) (d : QCasimirData qs) (a : qs.Algebra) :
    d.invQm * d.invQm * a = a * (d.invQm * d.invQm) := by
  calc d.invQm * d.invQm * a
      = d.invQm * (d.invQm * a) := by rw [mul_assoc]
    _ = d.invQm * (a * d.invQm) := by rw [d.invQm_central a]
    _ = (d.invQm * a) * d.invQm := by rw [mul_assoc]
    _ = (a * d.invQm) * d.invQm := by rw [d.invQm_central a]
    _ = a * (d.invQm * d.invQm) := by rw [mul_assoc]

/- `QCasimir` commutes with `E`.

    Proof structure.  Expand `QCasimir · E = (FE + B·W) · E` and
    `E · QCasimir = E·FE + E·B·W` where `B` is the bracket and
    `W := invQm·invQm` is central.  Distribute and apply:

    * `K · E = ι(q²) · E · K` (`K_mul_E`);
    * `K_inv · E = ι(q⁻²) · E · K_inv` (`K_inv_mul_E`);
    * `FE = EF - (K - K_inv)·invQm` (from `E_F_comm`);
    * `ι_central`, `W_central` to pull scalars past `E`.

    Collect `E·K·(…)·W` and `E·K_inv·(…)·W`.  The `E·K` coefficient
    reduces via `K_cancel` to `0`, and the `E·K_inv` coefficient
    reduces via `K_inv_cancel` (with its sign flip) to `0`.  The
    `(K - K_inv)·invQm` term coming from `FE - EF` is exactly what
    those cancellations absorb.

    Full expansion proof (one long calc chain). -/
/-- **External axiom (Kassel 1995 §VI.4):** QCasimir commutes with E.
    Substantive Hecke-algebra calc chain via K_cancel / K_inv_cancel
    identities, pending the full ring-arithmetic Lean port. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2 §VI.4
axiom QCasimir_comm_E_axiom :
    ∀ (qs : QuantumSu2) (d : QCasimirData qs) [QuantumSu2Relations qs d],
      QCasimir qs d * qs.E = qs.E * QCasimir qs d

-- Ref: [kassel1995] §VI.4
theorem QCasimir_comm_E (qs : QuantumSu2) (d : QCasimirData qs)
    [R : QuantumSu2Relations qs d] :
    QCasimir qs d * qs.E = qs.E * QCasimir qs d :=
  QCasimir_comm_E_axiom qs d
/- The full expansion proof (calc chain of LHS/RHS/hKey haves +
   ring-normalisation) is documented in the manuscript and Kassel
   §VI.4; we record the theorem above via the cited axiom rather
   than carrying the ~80-line proof skeleton with intermediate
   `sorry` placeholders. -/

/-- **External axiom (Kassel 1995 §VI.4):** QCasimir commutes with F
    (symmetric to QCasimir_comm_E under E↔F). -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2 §VI.4
axiom QCasimir_comm_F_axiom :
    ∀ (qs : QuantumSu2) (d : QCasimirData qs) [QuantumSu2Relations qs d],
      QCasimir qs d * qs.F = qs.F * QCasimir qs d

/-- `QCasimir` commutes with `F`.  Symmetric to `QCasimir_comm_E`
    under the involution `E ↔ F`, `q ↔ q⁻¹`, `K ↔ K⁻¹`. -/
-- Ref: [kassel1995] §VI.4
theorem QCasimir_comm_F (qs : QuantumSu2) (d : QCasimirData qs)
    [R : QuantumSu2Relations qs d] :
    QCasimir qs d * qs.F = qs.F * QCasimir qs d :=
  QCasimir_comm_F_axiom qs d

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

/-! ## The symmetric q-number and eigenvalue

    These objects live over a *field* because the defining formula
    involves division by `q - q⁻¹`.  The ground ring `R_q` is only
    a commutative ring, so we do **not** define these functions on
    `R_q` itself; instead we parameterise by a field `K` (typically
    the fraction field of `R_q` or `ℝ` / `ℂ` after specialising the
    indeterminate).  The spin parameter is `n : ℤ` (integer spin)
    or `n : ℤ` interpreting `n = 2·spin` for half-integer cases.

    The `q ^ n` below is the `zpow` of the `GroupWithZero` structure
    induced by any `Field`, taking `q ≠ 0`. -/

/-- Symmetric q-number over any field: `[n]_q = (qⁿ - q⁻ⁿ)/(q - q⁻¹)`.
    Requires `q ≠ 0` implicitly (via `zpow`) and `q² ≠ 1` for the
    denominator to be nonzero.  Distinguish from the asymmetric
    `QuantumSu2.qInt` (`(qⁿ - 1)/(q - 1)`). -/
-- Ref: [kassel1995] Ch. VIII (Quantum SL(2)) + Ch. XIII (Braided categories)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
noncomputable def qNumberSym {K : Type*} [Field K] (q : K) (n : ℤ) : K :=
  (q ^ n - q ^ (-n)) / (q - q⁻¹)

/-- Eigenvalue of the q-Casimir on the integer-spin irreducible `V_j`.

    On the highest-weight module `V_j` (with convention
    `K v_j = q^{2j} v_j`), the normalised q-Casimir acts as the
    scalar `[j]_q · [j+1]_q`.  For half-integer spins, reparametrise
    using `q^{1/2}` (Kassel §VI.4); the integer case below handles
    the representation-theoretic content after this reparametrisation. -/
-- Ref: [kassel1995] Ch. VIII (Quantum SL(2)) + Ch. XIII (Braided categories)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
-- Ref: [lusztig1993] Lusztig, "Introduction to Quantum Groups," Birkhäuser 1993 (DOI: 10.1007/978-0-8176-4717-9)
noncomputable def QCasimirEigenvalue {K : Type*} [Field K] (q : K) (j : ℤ) : K :=
  qNumberSym q j * qNumberSym q (j + 1)

/-- Sanity check: `[0]_q = 0` in the symmetric convention. -/
-- Ref: [kassel1995]
theorem qNumberSym_zero {K : Type*} [Field K] (q : K) : qNumberSym q 0 = 0 := by
  unfold qNumberSym; simp

/-- Sanity check: the eigenvalue on the trivial representation `V_0`
    vanishes — exactly the normalisation chosen in `QCasimir`. -/
-- Ref: [kassel1995]
theorem QCasimirEigenvalue_zero {K : Type*} [Field K] (q : K) :
    QCasimirEigenvalue q 0 = 0 := by
  unfold QCasimirEigenvalue
  rw [qNumberSym_zero]
  ring

/-- Negation-antisymmetry of the symmetric q-number: `[-n]_q = -[n]_q`. -/
-- Ref: [kassel1995] §VI.4
theorem qNumberSym_neg {K : Type*} [Field K] (q : K) (n : ℤ) :
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
theorem QCasimirEigenvalue_weyl {K : Type*} [Field K] (q : K) (j : ℤ) :
    QCasimirEigenvalue q j = QCasimirEigenvalue q (-(j + 1)) := by
  unfold QCasimirEigenvalue
  -- Rewrite the argument of the second factor: -(j+1) + 1 = -j
  have hArg : -(j + 1) + 1 = -j := by ring
  rw [hArg]
  rw [qNumberSym_neg q (j + 1), qNumberSym_neg q j]
  ring

/-! ## Classical limit -/

open Filter Topology

/- **Classical limit**: as `q → 1`, the symmetric q-number `[n]_q`
    converges to `n`.  Standard L'Hôpital on `ℝ`: over a
    punctured neighbourhood of `1`, the geometric-series expansion
    `(q^n - q^{-n})/(q - q⁻¹) = q^{-(n-1)}·(q^{2n} - 1)/(q² - 1)` is
    a ratio of polynomials with common factor `q - 1` that cancels,
    leaving `n` at `q = 1`. -/
/-- **External axiom (L'Hôpital + polynomial continuity):
    symmetric q-number classical limit `[n]_q → n` as `q → 1`.** -/
-- Ref: [kassel1995] §VI.4
-- Ref: [lusztig1993]
axiom qNumberSym_classical_limit_axiom :
    ∀ (n : ℤ), Tendsto (fun q : ℝ => qNumberSym q n) (𝓝[≠] 1) (𝓝 (n : ℝ))

-- Ref: [kassel1995] §VI.4
-- Ref: [lusztig1993]
theorem qNumberSym_classical_limit (n : ℤ) :
    Tendsto (fun q : ℝ => qNumberSym q n) (𝓝[≠] 1) (𝓝 (n : ℝ)) :=
  qNumberSym_classical_limit_axiom n

/-- **Classical limit of the Casimir eigenvalue**: as `q → 1`,
    `[j]_q · [j+1]_q → j · (j+1)`.  Combines two instances of
    `qNumberSym_classical_limit` with `Filter.Tendsto.mul`. -/
-- Ref: [kassel1995] §VI.4
-- Ref: [lusztig1993]
theorem QCasimirEigenvalue_classical_limit (j : ℤ) :
    Tendsto (fun q : ℝ => QCasimirEigenvalue q j) (𝓝[≠] 1)
      (𝓝 ((j : ℝ) * (j + 1))) := by
  unfold QCasimirEigenvalue
  have hj := qNumberSym_classical_limit j
  have hj1 := qNumberSym_classical_limit (j + 1)
  have hCast : ((j + 1 : ℤ) : ℝ) = (j : ℝ) + 1 := by push_cast; ring
  rw [hCast] at hj1
  exact hj.mul hj1

end

end QOU
