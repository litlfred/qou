import QOU.Basic
import Mathlib.FieldTheory.RatFunc.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.List.Basic
import Mathlib.Tactic


/-!
# QOU.BraidKnot.CasimirShared — promoted shared types for the braid/knot content blocks

Content-block `.lean` siblings cannot import one another, yet several blocks in
`content/.../braids-and-knots/` share a handful of carrier structures.  This
library module promotes those shared types into the `QOU` library so the
deferred sibling files (`q-casimir`, `q-casimir-exists`, `q-casimir-unique`,
`knot-eigenbasis-complete-proof`) can `import QOU.BraidKnot.CasimirShared`
instead of re-declaring them.

Two independent clusters live here, each over the ground ring its originating
sibling used:

* **Casimir cluster** (`namespace QOU`, ground ring `R_q = ℚ(q) = RatFunc ℚ`):
  `QuantumSu2`, `QCasimirData`, `QCasimir`.  The quantum-group relation
  `[E,F] = (K − K⁻¹)/(q − q⁻¹)` divides by `(q − q⁻¹)`, so the ground ring is
  the fraction field `ℚ(q)` (matching the canonical `quantum-su2.lean`).

* **Eigenbasis cluster** (`namespace QOU.Braiding`, ground ring
  `R_q = ℤ[q, q⁻¹] = LaurentPolynomial ℤ`): `HeckeAlgebra`, `BoundedPartition`,
  `SchurWeylDecomposition`, `AlexanderSurjectivity`, `MarkovTrace`.  These carry
  explicit `q⁻¹` data fields (the Laurent ring has no native `Inv`).

## References

- [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [chari1994guide] Chari–Pressley, *A Guide to Quantum Groups*, Ch. 10
- [alexander1923] J.W. Alexander, Proc. Natl. Acad. Sci. USA 9 (1923)
- [jones1987] V.F.R. Jones, Annals of Mathematics 126 (1987)
-/

namespace QOU

/-! ## Casimir cluster — ground ring `R_q = ℚ(q) = RatFunc ℚ` -/

-- Ground ring `R_q = ℚ(q) = RatFunc ℚ` (rational functions over ℚ).
abbrev R_q := RatFunc ℚ

/-- The canonical indeterminate `q` of `R_q = ℚ(q)`. -/
noncomputable def q_param : R_q := RatFunc.X

/-- The formal inverse `q⁻¹` of the indeterminate in `R_q = ℚ(q)`. -/
noncomputable def q_inv_param : R_q := RatFunc.X⁻¹

/-- **Quantum group 𝒰_q(𝔰𝔲(2))** generator data. -/
-- Ref: [lusztig1993] Lusztig, "Introduction to Quantum Groups," Birkhäuser 1993 (DOI: 10.1007/978-0-8176-4717-9)
structure QuantumSu2 where
  /-- The deformation parameter q > 0, q ≠ 1. -/
  q : R_q
  q_ne_one : q ≠ 1
  /-- The algebra carrier type. -/
  Algebra : Type*
  [instRing : Ring Algebra]
  /-- Generators E, F, K, K⁻¹. -/
  E : Algebra
  F : Algebra
  K : Algebra
  K_inv : Algebra
  /-- K · K⁻¹ = 1. -/
  K_inv_left : K_inv * K = 1
  K_inv_right : K * K_inv = 1

attribute [instance] QuantumSu2.instRing

/-- The q-integer [n]_q = (qⁿ - 1)/(q - 1). -/
-- Ref: [lusztig1993]
noncomputable def QuantumSu2.qInt (qs : QuantumSu2) (n : ℕ) : R_q :=
  (qs.q ^ n - 1) / (qs.q - 1)

/-- [1]_q = 1 for all q ≠ 1. -/
-- Ref: [lusztig1993]
theorem qInt_one (qs : QuantumSu2) : qs.qInt 1 = 1 := by
  unfold QuantumSu2.qInt; simp [pow_one, div_self (sub_ne_zero.mpr qs.q_ne_one)]

/-- [2]_q = q + 1. -/
-- Ref: [lusztig1993]
theorem qInt_two (qs : QuantumSu2) : qs.qInt 2 = qs.q + 1 := by
  unfold QuantumSu2.qInt
  have h : qs.q - 1 ≠ 0 := sub_ne_zero.mpr qs.q_ne_one
  field_simp; ring

/-- **Step recurrence for classical q-integers (`xbz0`).** For any `qs : QuantumSu2`
and `n : ℕ`, `[n + 1]_q = q · [n]_q + 1`. -/
theorem qInt_succ (qs : QuantumSu2) (n : ℕ) :
    qs.qInt (n + 1) = qs.q * qs.qInt n + 1 := by
  dsimp [QuantumSu2.qInt]
  have h : qs.q - 1 ≠ 0 := sub_ne_zero.mpr qs.q_ne_one
  rw [pow_add, pow_one]
  field_simp
  ring

/-! ## Casimir cluster — the parameter bundle and the q-Casimir element -/

/-- Parameter bundle for constructing the q-Casimir element.

    We carry explicit inverses of `q` and of `(q − qInv)` with two-sided
    witnesses, plus a central embedding `ι : R_q →+* qs.Algebra`, so that the
    construction never invokes a field-style `⁻¹` on an abstract coefficient. -/
-- Ref: [kassel1995] Ch. VIII (Quantum SL(2)) + Ch. XIII (Braided categories)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
structure QCasimirData (qs : QuantumSu2) where
  /-- Explicit inverse of `q` in the ground ring. -/
  qInv : R_q
  /-- Left inverse witness for `qInv`. -/
  qInv_left  : qInv * qs.q = 1
  /-- Witness that `qInv` is a right inverse. -/
  qInv_right : qs.q * qInv = 1
  /-- Embedding of the ground ring into the algebra. -/
  ι : R_q →+* qs.Algebra
  /-- The image of `ι` lies in the centre of `qs.Algebra`. -/
  ι_central : ∀ (r : R_q) (a : qs.Algebra), ι r * a = a * ι r
  /-- An algebra element that inverts `ι (q - qInv)`. -/
  invQm : qs.Algebra
  /-- Left inverse witness for `invQm`. -/
  invQm_left  : invQm * ι (qs.q - qInv) = 1
  /-- Witness that `invQm` is a right inverse. -/
  invQm_right : ι (qs.q - qInv) * invQm = 1
  /-- `invQm` is central. -/
  invQm_central : ∀ (a : qs.Algebra), invQm * a = a * invQm

namespace QCasimirData

variable {qs : QuantumSu2}

/-- Inverses in a (commutative) ring are unique: the `qInv` field is
    determined by the `qInv_left` witness alone. -/
-- Ref: [kassel1995]
theorem qInv_unique (d d' : QCasimirData qs) : d.qInv = d'.qInv := by
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

/-- The (normalised) q-Casimir element inside `qs.Algebra`:

    `C_q = F·E + (q·K + q⁻¹·K⁻¹ - (q + q⁻¹)) · (q - q⁻¹)⁻²`. -/
-- Ref: [kassel1995] Ch. VIII (Quantum SL(2)) + Ch. XIII (Braided categories)
--      DOI: 10.1007/978-1-4612-0783-2
-- Ref: [lusztig1993] Lusztig, "Introduction to Quantum Groups," Birkhäuser 1993 (DOI: 10.1007/978-0-8176-4717-9)
noncomputable def QCasimir (qs : QuantumSu2) (d : QCasimirData qs) : qs.Algebra :=
  let kPart      := d.ι qs.q * qs.K + d.ι d.qInv * qs.K_inv
  let normaliser := d.ι (qs.q + d.qInv)
  qs.F * qs.E + (kPart - normaliser) * d.invQm * d.invQm

end QOU

/-! ## Eigenbasis cluster — ground ring `R_q = ℤ[q, q⁻¹] = LaurentPolynomial ℤ` -/

namespace QOU.Braiding

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ). -/
abbrev R_q := LaurentPolynomial ℤ
noncomputable def q_param : R_q := LaurentPolynomial.T 1
noncomputable def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Hecke algebra H_n(q)**: the quotient of the group algebra k[B_n]
    by the quadratic relation (σ_i − q)(σ_i + q⁻¹) = 0. -/
-- Ref: [chari1994guide] Chari–Pressley, Ch. 10
structure HeckeAlgebra where
  /-- Number of strands. -/
  n : ℕ
  /-- Carrier type. -/
  carrier : Type*
  /-- Deformation parameter q. -/
  q : R_q
  /-- q ≠ 0. -/
  q_ne_zero : q ≠ 0
  /-- Inverse parameter q⁻¹ carried as data. -/
  q_inv : R_q
  /-- Defining relation `q · q⁻¹ = 1`. -/
  q_mul_inv : q * q_inv = 1
  /-- Multiplication. -/
  mul : carrier → carrier → carrier
  /-- Unit element. -/
  one : carrier
  /-- Zero element. -/
  zero : carrier
  /-- Subtraction. -/
  sub : carrier → carrier → carrier
  /-- Scalar multiplication by `R_q`. -/
  smul : R_q → carrier → carrier
  /-- Generators T₁, …, T_{n-1}. -/
  T : Fin (n - 1) → carrier
  /-- Braid relation: T_i T_{i+1} T_i = T_{i+1} T_i T_{i+1}. -/
  braid_relation : ∀ (i : Fin (n - 2)),
    let i' : Fin (n - 1) := ⟨i.val, by omega⟩
    let j : Fin (n - 1) := ⟨i.val + 1, by omega⟩
    mul (mul (T i') (T j)) (T i') = mul (mul (T j) (T i')) (T j)
  /-- Quadratic relation: T_i² − (q − q⁻¹)·T_i − 1 = 0. -/
  quadratic : ∀ (i : Fin (n - 1)),
    sub (sub (mul (T i) (T i)) (smul (q - q_inv) (T i))) one = zero

/-- A partition of n with at most r parts, a non-increasing list of row lengths. -/
structure BoundedPartition where
  /-- Row lengths in non-increasing order. -/
  rows : List ℕ
  /-- Size n (sum of row lengths). -/
  n : ℕ
  /-- Maximum number of parts (rows). -/
  maxParts : ℕ
  /-- The rows sum to n. -/
  size_eq : rows.sum = n
  /-- At most maxParts rows. -/
  parts_bound : rows.length ≤ maxParts
  /-- Non-increasing (valid Young diagram). -/
  sorted : rows.Pairwise (· ≥ ·)

/-- The spin label j = (λ₁ − λ₂)/2 for a two-part partition. -/
def spin (bp : BoundedPartition) : ℚ :=
  match bp.rows with
  | [] => 0
  | [a] => (a : ℚ) / 2
  | a :: b :: _ => ((a : ℚ) - (b : ℚ)) / 2

/-- **q-Schur–Weyl decomposition** of V^⊗n under the joint action
    of SU_q(2) and the Hecke algebra H_n(q). -/
-- Ref: [chari1994guide] Chari–Pressley, Ch. 10
structure SchurWeylDecomposition where
  /-- Number of tensor factors. -/
  n : ℕ
  /-- The Hecke algebra. -/
  hecke : HeckeAlgebra
  /-- Consistency: same n. -/
  n_eq : hecke.n = n
  /-- Type of the tensor power V^⊗n. -/
  tensorPower : Type*
  /-- The set of partitions indexing the decomposition. -/
  partitions : List BoundedPartition
  /-- Each partition has size n with at most 2 parts. -/
  partitions_valid : ∀ μ ∈ partitions, μ.n = n ∧ μ.maxParts = 2
  /-- The number of partitions equals ⌊n/2⌋ + 1. -/
  partitions_count : partitions.length = n / 2 + 1
  /-- Irreducible SU_q(2)-module for partition μ. -/
  V_irrep : BoundedPartition → Type*
  /-- Irreducible H_n(q)-module for partition μ. -/
  S_irrep : BoundedPartition → Type*
  /-- Embedding of each summand V_μ ⊗ S_μ into V^⊗n. -/
  summand_embed : ∀ μ ∈ partitions,
    V_irrep μ → S_irrep μ → tensorPower
  /-- **Completeness**: every element of V^⊗n lies in the image of some
      summand embedding. -/
  -- Ref: [chari1994guide] Chari–Pressley, Ch. 10 (Jimbo's theorem)
  complete : ∀ (v : tensorPower), ∃ μ, ∃ (hμ : μ ∈ partitions),
    ∃ (w : V_irrep μ) (s : S_irrep μ), summand_embed μ hμ w s = v

/-- **Alexander's theorem**: every oriented link in S³ is the closure
    β̂ of some braid β ∈ B_n for some n. -/
-- Ref: [alexander1923] J.W. Alexander, Proc. Natl. Acad. Sci. USA 9 (1923), 93–95
structure AlexanderSurjectivity where
  /-- Type of oriented links in S³. -/
  Link : Type*
  /-- Type of braids (union over all B_n). -/
  Braid : Type*
  /-- Braid closure map β ↦ β̂. -/
  closure : Braid → Link
  /-- **Surjectivity**: every link is the closure of some braid. -/
  -- Ref: [alexander1923] https://doi.org/10.1073/pnas.9.3.93
  surjective : Function.Surjective closure

/-- **Markov trace** on the Hecke algebra tower ⋃_n H_n(q).

    Carries its own Hecke algebra as the `hecke` field (so a decomposition and
    its trace can be checked for consistency by `markov.hecke = decomp.hecke`),
    matching the presentation in `knot-eigenbasis-complete-proof.lean`. -/
-- Ref: [jones1987] V.F.R. Jones, Annals of Mathematics 126 (1987), 335–388
structure MarkovTrace where
  /-- The Hecke algebra this trace lives on. -/
  hecke : HeckeAlgebra
  /-- The trace functional tr : H_n(q) → R_q. -/
  tr : hecke.carrier → R_q
  /-- Trace property (cyclicity / Markov I): tr(ab) = tr(ba). -/
  trace_comm : ∀ (a b : hecke.carrier), tr (hecke.mul a b) = tr (hecke.mul b a)
  /-- Markov parameter z determined by q. -/
  z : R_q
  /-- z ≠ 0. -/
  z_ne_zero : z ≠ 0
  /-- Non-degeneracy: the trace of the unit is non-zero. -/
  tr_one_ne_zero : tr hecke.one ≠ 0
  /-- **Markov property** (Markov II / stabilisation). -/
  markov_stab : ∀ (hn : hecke.n ≥ 2) (x : hecke.carrier),
    let last : Fin (hecke.n - 1) := ⟨hecke.n - 2, by omega⟩
    tr (hecke.mul x (hecke.T last)) = z * tr x

end QOU.Braiding
