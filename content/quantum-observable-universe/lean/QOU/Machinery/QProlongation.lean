import QOU.Machinery.QuantumTorusSymbol

/-!
# QOU.Machinery.QProlongation — the recurrence operator and its principal symbol

**Definitional sharpening of the LEFT-HAND SIDE of the keystone conjecture
`conj:qdifference-kernel-prolongation-symbol` — NOT a proof of the keystone.**

The proved confluent recurrence
(`QOU.Mass.QDifferenceConfluentObstruction.qlift_normalized_kernel_exists`,
`binding_carrier_satisfies_kernel`) is the exact depth-2 q-difference kernel
relation on the q-factorial carrier

    `[n+2]_q · b_{n+2} = b_{n+1} + b_n`.

This file re-encodes that relation as a single concrete element of the
`QOU.Machinery.QuantumTorus` q-Weyl ring — the **recurrence operator**

    `D_q = κ · L² − L − 1`  (`prolongationOp κ`),

where `L` is the forward-shift generator (`Lgen`, `(L·b)ₙ = b_{n+1}`) and
`κ : A` is the top-jet-order q-integer weight `[·]_q` living in the
coefficient ring `A = R[M^±]`.  Applying the QDM-1/QDM-2 principal-symbol
machinery (`QuantumTorusSymbol.symbol`, sorry-free) gives, for `κ ≠ 0`,

    `symbol D_q = L² · κ = monomial 2 κ`   (`symbol_prolongationOp`),

i.e. the principal (top-shift-order) symbol of the recurrence operator is the
leading kernel monomial read off the recurrence.  This makes the phrase "R is
the prolongation symbol" a **precise algebraic statement on the quantum torus**:
the principal symbol of `D_q` equals the leading kernel term `κ L²`.

## HONESTY — this is definitional sharpening, and the symbol-match is a
## TAUTOLOGICAL RE-ENCODING, not gap-closure.

Read `docs/audits/2026-07-20-qprolongation-definitional-sharpening.md`.  In
brief:

1. **This is NOT a proof of `conj:qdifference-kernel-prolongation-symbol`.**
   The conjecture stays a conjecture (`QOU.Mass.QDifferenceKernelIsProlongationSymbol`
   is untouched; this file introduces no instance of it).  We do not relabel it
   a theorem and wire nothing to production.

2. **The symbol-match is circular / tautological.**  `D_q` is defined *from* the
   recurrence — the C1 kernel — and `recurrenceKernelLead κ := monomial 2 κ` is
   *defined* as the leading term read off that same recurrence.  So
   `symbol D_q = recurrenceKernelLead κ` (`symbol_eq_recurrence_kernel`) holds
   **by construction**: it is the QDM `symbol` machinery correctly extracting a
   leading monomial, applied to an operator we wrote down *as* the recurrence.
   `D_q` is **NOT** defined independently from the jet / Seiberg–Witten period
   geometry.  It is the recurrence re-encoded in `QuantumTorus`.  Label:
   *tautological re-encoding of the recurrence's principal part, not
   gap-closure.*

3. **The genuine remaining wall is the GEOMETRIC ATTACHMENT** — that this
   algebraic symbol coincides with the symbol of the jet-prolongation operator
   `JⁿE → Jⁿ⁺¹E` of the SW connection (keystone steps D–E: the branch-point /
   Stokes monodromy of `λ_SW^{(n)}` on `𝒮_c ≅ ℙ¹`).  **This file does not touch
   that.**  Establishing the geometric side *independently* and then matching it
   to `symbol D_q` is what would actually close the keystone; that derivation is
   not attempted here.

## What is proved here (sorry-free)

* `prolongationOp_eq` — `D_q = emb κ · L² − L − 1 = monomial 2 κ − monomial 1 1
  − monomial 0 1` (the recurrence operator in the shift generator `L`).
* `coeffAt_prolongationOp`, `coeffAt_prolongationOp_two`,
  `coeffAt_prolongationOp_of_gt` — its L-graded coefficients.
* `topDeg_prolongationOp`, `leadDeg_prolongationOp`, `leadCoeff_prolongationOp`
  — top L-degree `2`, leading coefficient `κ`.
* `symbol_prolongationOp` / `symbol_eq_recurrence_kernel` — the principal symbol
  is `monomial 2 κ`, the leading kernel monomial (the tautological re-encoding).

## Base ring (§7c)

Generic `{A : Type*} [CommRing A] [MulSemiringAction Ldeg A]` throughout — no
`ℝ`, no ordering, no archimedean construct.  `lean`-direct-verifies against the
package oleans.

-- Ref: [manuscript] mass-theory, conj:qdifference-kernel-prolongation-symbol;
--      docs/audits/2026-07-20-qprolongation-definitional-sharpening.md
-/

noncomputable section

namespace QOU.Machinery.QProlongation

open SkewMonoidAlgebra QOU.Machinery.QuantumTorus

variable {A : Type*} [CommRing A] [MulSemiringAction Ldeg A]

/-! ### L-graded coefficient additivity (thin wrappers over `coeff_add`/`coeff_sub`) -/

theorem coeffAt_add (f g : QuantumTorus A) (n : ℤ) :
    coeffAt (f + g) n = coeffAt f n + coeffAt g n := by
  simp only [coeffAt, coeff_add]

theorem coeffAt_neg (g : QuantumTorus A) (n : ℤ) : coeffAt (-g) n = - coeffAt g n := by
  simp only [coeffAt]; rw [coeff, coeff]; simp

theorem coeffAt_sub (f g : QuantumTorus A) (n : ℤ) :
    coeffAt (f - g) n = coeffAt f n - coeffAt g n := by
  rw [sub_eq_add_neg, coeffAt_add, coeffAt_neg, ← sub_eq_add_neg]

/-! ### The recurrence operator `D_q = κ·L² − L − 1` -/

/-- **The recurrence operator** encoding `[n+2]_q b_{n+2} = b_{n+1} + b_n` as a
    concrete quantum-torus element: `D_q = κ·L² − L − 1`, with `L = Lgen` the
    forward shift and `κ : A` the top-jet-order q-integer weight `[·]_q` in the
    coefficient ring. -/
def prolongationOp (κ : A) : QuantumTorus A := emb κ * Lgen ^ 2 - Lgen - 1

/-- `L² = monomial 2 1` (two shifts). -/
theorem Lgen_sq : (Lgen : QuantumTorus A) ^ 2 = monomial 2 1 := by
  rw [pow_two, Lgen_eq_monomial, monomial_mul_monomial]
  norm_num

/-- `emb κ · L² = monomial 2 κ` (the coefficient rides on the top shift). -/
theorem emb_mul_Lgen_sq (κ : A) :
    (emb κ * Lgen ^ 2 : QuantumTorus A) = monomial 2 κ := by
  rw [Lgen_sq, ← monomial_zero_left, monomial_mul_monomial]
  simp

/-- `(1 : QuantumTorus A) = monomial 0 1`. -/
theorem one_eq_monomial : (1 : QuantumTorus A) = monomial 0 1 := by
  rw [monomial]; exact one_def

/-- **The recurrence operator in monomial normal form.**
    `D_q = monomial 2 κ − monomial 1 1 − monomial 0 1`. -/
theorem prolongationOp_eq (κ : A) :
    prolongationOp κ = monomial 2 κ - monomial 1 1 - monomial 0 1 := by
  rw [prolongationOp, emb_mul_Lgen_sq, Lgen_eq_monomial, one_eq_monomial]

/-! ### The L-graded coefficients of `D_q` -/

/-- The `L^k`-coefficient of `D_q`. -/
theorem coeffAt_prolongationOp (κ : A) (k : ℤ) :
    coeffAt (prolongationOp κ) k
      = (if k = 2 then κ else 0)
        - (if k = 1 then (1 : A) else 0)
        - (if k = 0 then (1 : A) else 0) := by
  rw [prolongationOp_eq, coeffAt_sub, coeffAt_sub, coeffAt_monomial,
    coeffAt_monomial, coeffAt_monomial]

/-- The leading `L²`-coefficient of `D_q` is `κ`. -/
theorem coeffAt_prolongationOp_two (κ : A) : coeffAt (prolongationOp κ) 2 = κ := by
  rw [coeffAt_prolongationOp]; norm_num

/-- Above L-degree `2` the coefficients of `D_q` vanish. -/
theorem coeffAt_prolongationOp_of_gt (κ : A) {k : ℤ} (hk : 2 < k) :
    coeffAt (prolongationOp κ) k = 0 := by
  rw [coeffAt_prolongationOp, if_neg (by omega), if_neg (by omega), if_neg (by omega)]
  ring

/-! ### Top degree and principal symbol of `D_q` -/

/-- **`D_q` has top L-degree `2`** (for a nonzero leading weight `κ`): the shift
    order of the recurrence operator is exactly `2`, matching the depth-2 kernel. -/
theorem topDeg_prolongationOp (κ : A) (hκ : κ ≠ 0) :
    topDeg (prolongationOp κ) = ((2 : ℤ) : WithBot ℤ) := by
  have h2mem : (2 : ℤ) ∈ expSupport (prolongationOp κ) := by
    rw [mem_expSupport_iff, coeffAt_prolongationOp_two]; exact hκ
  apply le_antisymm
  · rw [topDeg]
    apply Finset.max_le
    intro k hk
    by_contra hcon
    rw [not_le] at hcon
    have hkk : (2 : ℤ) < k := by exact_mod_cast hcon
    exact ((mem_expSupport_iff _ _).mp hk) (coeffAt_prolongationOp_of_gt κ hkk)
  · exact Finset.le_max h2mem

/-- The leading L-degree of `D_q` is `2`. -/
theorem leadDeg_prolongationOp (κ : A) (hκ : κ ≠ 0) :
    leadDeg (prolongationOp κ) = 2 :=
  leadDeg_of_topDeg (topDeg_prolongationOp κ hκ)

/-- The leading coefficient of `D_q` is the top-jet-order weight `κ`. -/
theorem leadCoeff_prolongationOp (κ : A) (hκ : κ ≠ 0) :
    leadCoeff (prolongationOp κ) = κ := by
  rw [leadCoeff, leadDeg_prolongationOp κ hκ, coeffAt_prolongationOp_two]

/-- **The principal symbol of the recurrence operator is `κ L²`.**  Applying the
    proved QDM-1 principal-symbol map to `D_q` extracts its leading `L`-monomial:
    `symbol D_q = monomial 2 κ`. -/
theorem symbol_prolongationOp (κ : A) (hκ : κ ≠ 0) :
    symbol (prolongationOp κ) = monomial 2 κ := by
  rw [symbol, leadDeg_prolongationOp κ hκ, leadCoeff_prolongationOp κ hκ]

/-! ### The tautological re-encoding: `symbol D_q = R_lead` -/

/-- **The leading kernel monomial read off the recurrence.**  From
    `[n+2]_q b_{n+2} = b_{n+1} + b_n`, the top-shift-order term is `κ L²`.  This
    is *defined* as the leading term of the SAME recurrence that defines `D_q`,
    so `symbol D_q = recurrenceKernelLead κ` below is true **by construction**
    (see the honesty note in the file header): a tautological re-encoding, not a
    geometric identification. -/
def recurrenceKernelLead (κ : A) : QuantumTorus A := monomial 2 κ

/-- **The principal symbol of `D_q` equals the leading recurrence-kernel term.**

    This is the precise algebraic form of the keystone's LEFT-HAND side "R is the
    prolongation symbol": the QDM principal-symbol machinery, applied to the
    recurrence operator, returns exactly the leading kernel monomial.

    **TAUTOLOGICAL RE-ENCODING, NOT KEYSTONE CLOSURE.**  Both sides are read off
    the same recurrence; `D_q` is not defined independently from jet / SW period
    geometry.  The genuine wall — matching this to the SW jet-prolongation
    operator's symbol — is untouched here.  See
    `docs/audits/2026-07-20-qprolongation-definitional-sharpening.md`. -/
theorem symbol_eq_recurrence_kernel (κ : A) (hκ : κ ≠ 0) :
    symbol (prolongationOp κ) = recurrenceKernelLead κ :=
  symbol_prolongationOp κ hκ

end QOU.Machinery.QProlongation
