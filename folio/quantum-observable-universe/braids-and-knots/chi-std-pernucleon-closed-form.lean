/-
  Closed-form theorem for χ_std(β_nucleon) in the 2-dim (2,1) irrep
  of the Iwahori-Hecke algebra H_3(q).

  For the per-nucleon braid words emitted by `proton_cross` and
  `neutron_cross` (in `mass_endomorphism.py`), the standard-irrep
  trace takes the closed form

    χ_std(β_nuc) = (H_A / 4) · Σ_{k ∈ S_nuc} [k]_q

  with S_proton = {11, 9, 7, 3}, S_neutron = {9, 7, 5, 1}, both
  sharing the ladder shape {m, m-2, m-4, m-8} (m_p = 11, m_n = 9).

  Ref: [leitner2026] docs/chi-std-pernucleon-theorem.md.
-/

import Mathlib.Algebra.Group.Defs
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Data.Real.Sqrt
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import QOU.MathlibExt.QIntegerCanonical

namespace QOU.ChiStdPerNucleon

/-! ## Self-contained 2×2 matrix algebra

    We define `M2` directly instead of pulling `Matrix (Fin 2) (Fin 2)`
    from Mathlib so that proofs reduce to `ring` over ℝ with no
    dependent-type bookkeeping. -/

/-- A real 2×2 matrix represented by its four entries. -/
structure M2 where
  a11 : ℝ
  a12 : ℝ
  a21 : ℝ
  a22 : ℝ

namespace M2

/-- 2×2 matrix product. -/
def mul (X Y : M2) : M2 :=
  ⟨X.a11 * Y.a11 + X.a12 * Y.a21, X.a11 * Y.a12 + X.a12 * Y.a22,
   X.a21 * Y.a11 + X.a22 * Y.a21, X.a21 * Y.a12 + X.a22 * Y.a22⟩

/-- 2×2 scalar multiplication. -/
def smul (c : ℝ) (X : M2) : M2 :=
  ⟨c * X.a11, c * X.a12, c * X.a21, c * X.a22⟩

/-- 2×2 matrix addition. -/
def add (X Y : M2) : M2 :=
  ⟨X.a11 + Y.a11, X.a12 + Y.a12, X.a21 + Y.a21, X.a22 + Y.a22⟩

/-- 2×2 identity matrix. -/
def one : M2 := ⟨1, 0, 0, 1⟩

/-- 2×2 trace. -/
def trace (X : M2) : ℝ := X.a11 + X.a22

instance : Mul M2 := ⟨mul⟩
instance : Add M2 := ⟨add⟩
instance : One M2 := ⟨one⟩
instance : HSMul ℝ M2 M2 := ⟨smul⟩

/-! The four instances above are anonymous, so a goal states `X * Y` as
`HMul.hMul X Y` rather than as `M2.mul X Y`.  Passing `M2.mul` to `simp` then
matches nothing — `simp` reports it as an *unused* argument — and because the
argument of a projection never becomes a constructor application, terms like
`(1 • {a11 := q, ..}).a11` are left unreduced and the closed-form proofs below
stall with a 24 kB goal.

These three `rfl` bridges are what let `simp` cross the instance boundary.  They
are deliberately **not** `@[simp]`: they are passed explicitly at the two call
sites, so nothing else in the file changes behaviour. -/

lemma mul_eq (X Y : M2) : X * Y = M2.mul X Y := rfl
lemma one_eq : (1 : M2) = M2.one := rfl
lemma smul_eq (c : ℝ) (X : M2) : c • X = M2.smul c X := rfl

@[simp] lemma trace_one : (1 : M2).trace = 2 := by
  show (M2.one.a11 + M2.one.a22) = 2
  norm_num [M2.one]

end M2

/-! ## Hoefsmit seminormal matrices for std = (2,1) at n = 3 -/

/-- σ_1 on std = (2,1): diagonal `diag(q, -q⁻¹)`. -/
noncomputable def hoefsmit_σ₁ (q : ℝ) : M2 :=
  ⟨q, 0, 0, -q⁻¹⟩

/-- σ_2 on std = (2,1): 2×2 mixing block with axial distance ρ = -2.
    Off-diagonal entries carry `√(q⁴+q²+1)/(q²+1)`. -/
noncomputable def hoefsmit_σ₂ (q : ℝ) : M2 :=
  let b := Real.sqrt (q^4 + q^2 + 1) / (q^2 + 1)
  ⟨-1 / (q^3 + q), b, b, q^3 / (q^2 + 1)⟩

/-! ## q-numbers -/

/-- q-number `[k]_q := (q^k - q^{-k}) / (q - q⁻¹)` for `k ∈ ℕ, k ≥ 0`. -/
noncomputable def qNum (q : ℝ) (k : ℕ) : ℝ :=
  (q^k - q^(-(k : ℤ))) / (q - q⁻¹)

/-- **Bridge to the canonical balanced bracket**, unconditional — the local body
differs from `qIntBal` only in writing the negative power as a `zpow`
(`q ^ (-(k : ℤ))` rather than `q⁻¹ ^ k`), which is `zpow_neg` + `inv_pow`.

This site was the one the `qou-qint` drain could not reach while the file was
red on `main`; it is migrated now that the two closed-form theorems above are
proved. -/
theorem qNum_eq_canonical (q : ℝ) (k : ℕ) :
    qNum q k = QOU.QInteger.qIntBal q k := by
  simp [qNum, QOU.QInteger.qIntBal, QOU.Mass.QHookDimensionBalanced.qIntBal,
    zpow_neg, zpow_natCast, inv_pow]

/-- Core closed-form: `(H_A / 4) · Σ_{k ∈ indices} [k]_q`. -/
noncomputable def chiStdClosedForm (q : ℝ) (indices : List ℕ) : ℝ :=
  (q - q⁻¹) / 4 * (indices.map (qNum q)).sum

/-- Proton index set (from Laurent-polynomial grouping). -/
def protonIndices : List ℕ := [11, 9, 7, 3]

/-- Neutron index set (ladder-shifted by 2). -/
def neutronIndices : List ℕ := [9, 7, 5, 1]

/-! ## Per-nucleon braid-word structure -/

/-- Hecke factor (c, d) ∈ ℝ² representing `c · σ + d · I`. -/
structure HeckeFactor where
  c : ℝ
  d : ℝ

/-- Which Hecke generator a factor acts on in H_3(q). -/
inductive Gen | g0 | g1
  deriving DecidableEq, Repr

/-- Per-nucleon braid word. -/
abbrev NucBraidWord := List (HeckeFactor × Gen)

/-- Build a 2×2 matrix from a single Hecke factor on a given generator:
    `c · σ + d · I`. -/
noncomputable def heckeFactorMat (q : ℝ) (f : HeckeFactor) (g : Gen) : M2 :=
  let sigma : M2 := match g with
    | .g0 => hoefsmit_σ₁ q
    | .g1 => hoefsmit_σ₂ q
  M2.add (f.c • sigma) (f.d • (1 : M2))

/-- Evaluate a nucleon braid word by matrix-product of its factor
    matrices in order. -/
noncomputable def evalWord (q : ℝ) : NucBraidWord → M2
  | [] => 1
  | (f, g) :: rest => (heckeFactorMat q f g) * (evalWord q rest)

/-- χ_std evaluator: word → scalar via matrix-product trace. -/
noncomputable def chiStdEval (q : ℝ) (w : NucBraidWord) : ℝ :=
  (evalWord q w).trace

/-! ## Per-nucleon braid words (as specified in mass_endomorphism.py) -/

/-- Proton per-nucleon braid word from `proton_cross`:

    - gen 0: six (1, 0) + one (1, -H_A/2)
    - gen 1: three (1, -H_A) + one (1, -H_A/2) -/
noncomputable def protonBraid (H_A : ℝ) : NucBraidWord :=
  (List.replicate 6 (⟨1, 0⟩, Gen.g0) : NucBraidWord) ++
  [(⟨1, -H_A / 2⟩, Gen.g0)] ++
  (List.replicate 3 (⟨1, -H_A⟩, Gen.g1) : NucBraidWord) ++
  [(⟨1, -H_A / 2⟩, Gen.g1)]

/-- Neutron per-nucleon braid word from `neutron_cross`:

    - gen 0: five (1, 0) + one (1, -H_A) + one (1, -H_A/2)
    - gen 1: three (1, -H_A) + one (1, -H_A/2) -/
noncomputable def neutronBraid (H_A : ℝ) : NucBraidWord :=
  (List.replicate 5 (⟨1, 0⟩, Gen.g0) : NucBraidWord) ++
  [(⟨1, -H_A⟩, Gen.g0), (⟨1, -H_A / 2⟩, Gen.g0)] ++
  (List.replicate 3 (⟨1, -H_A⟩, Gen.g1) : NucBraidWord) ++
  [(⟨1, -H_A / 2⟩, Gen.g1)]

/-! ## Main theorems

    The proofs reduce to polynomial identities in q after:
      1. Expanding the matrix products W_g0 · W_g1 (14 factors each).
      2. Noting that W_g0 is diagonal (σ_1 is), so only the diagonal
         of W_g1 contributes to tr(W_g0 · W_g1).
      3. Applying the algebraic simplification σ² = H_A · σ + 1 on
         σ_2, which reduces the trace to a Laurent polynomial in q.
      4. Regrouping Laurent-polynomial terms into (q^k - q^{-k}) pairs
         at odd k, which yields the q-number sum.

    The polynomial identity (step 4) is established by direct sympy
    computation and recorded in
    `computations/chi-std-pernucleon.witness.json`.

    In Lean, the full matrix expansion produces expressions of degree
    up to 30 in q that ring-normalise to the claimed Laurent form.
    **Both closed-form theorems below are now proved outright** — no
    `sorry`, and the sympy run is corroboration rather than the
    warrant.  What the proofs need beyond `simp`/`field_simp`/`ring`
    is three ingredients, none of which the tactic block can find on
    its own:

      1. `M2.{mul,one,smul}_eq` — the anonymous `Mul`/`One`/`HSMul`
         instances mean the goal says `HMul.hMul`, so passing `M2.mul`
         to `simp` matches nothing and the structure projections never
         reduce.  See the note beside those lemmas.
      2. `Real.sq_sqrt` at the radicand `1 + q² + q⁴`, supplied at both
         `√²` and `√⁴`.  Step 3's claim that the off-diagonal
         `√(q⁴+q²+1)` contributions cancel is what this discharges;
         the surviving even powers are polynomial.
      3. `q ≠ 0` and `q² − 1 ≠ 0` for `field_simp`, the latter coming
         from the `q − q⁻¹` in `qNum`. -/

/- **Main theorem (proton)**: the per-nucleon χ_std closed form.

    Proof structure (see `docs/chi-std-pernucleon-theorem.md` §Proof):

    **Step 1** (diagonal block reduction). Since `hoefsmit_σ₁` is
    diagonal, all factors on gen 0 commute and reduce to
    `W_g0 = σ_1^6 · (σ_1 - H_A/2)`.  Explicit:
      `W_g0 = ([2]_q/2) · diag(q^6, -q^{-6})`.

    **Step 2** (mixing block). On gen 1, `σ_2 - H_A · I = σ_2^{-1}`
    from the Hecke relation, so
      `W_g1 = σ_2^{-3} · (σ_2 - H_A/2)`.
    This is an explicit 2×2 matrix with entries polynomial in q.

    **Step 3** (trace). Since `W_g0` is diagonal, the trace of
    `W_g0 · W_g1` picks out the diagonal of `W_g1` only, cancelling
    the off-diagonal `√(q⁴+q²+1)` contributions.

    **Step 4** (Laurent grouping). The resulting Laurent polynomial
    in q has terms at powers {±11, ±9, ±7, ±3}, which regroup into
    `(H_A / 4) · ([11]_q + [9]_q + [7]_q + [3]_q)`.

    The matrix expansion in steps 1-3 is also verified symbolically by
    sympy (see `chi_std_pernucleon_derivation.py`).  Steps 1-4 are now
    discharged in Lean as a single `simp`/`ring_nf`/`field_simp`/`ring`
    computation, so the sympy run is a cross-check rather than the
    citation standing in for a proof.
    -- Ref: [leitner2026] docs/chi-std-pernucleon-theorem.md §Proof.

    Ref: [leitner2026] docs/chi-std-pernucleon-theorem.md §Proof,
         computations/chi-std-pernucleon.witness.json.
-/
/-- **Theorem (manuscript chi-std-pernucleon-theorem §Proof):
    closed-form χ_std for proton braid.**  Verified externally via
    sympy (chi_std_pernucleon_derivation.py). -/
-- Ref: [leitner2026] docs/chi-std-pernucleon-theorem.md §Proof
theorem chi_std_proton_closed_form (q : ℝ) (hq : 1 < q) :
    chiStdEval q (protonBraid (q - q⁻¹)) =
      chiStdClosedForm q protonIndices := by
  simp [chiStdEval, evalWord, protonBraid, heckeFactorMat, hoefsmit_σ₁, hoefsmit_σ₂, M2.mul_eq, M2.one_eq, M2.smul_eq,
    M2.add, M2.mul, M2.smul, M2.one, M2.trace, chiStdClosedForm, protonIndices, qNum]
  have hs : Real.sqrt (1 + q ^ 2 + q ^ 4) ^ 2 = 1 + q ^ 2 + q ^ 4 :=
    Real.sq_sqrt (by positivity)
  have hs4 : Real.sqrt (1 + q ^ 2 + q ^ 4) ^ 4 = (1 + q ^ 2 + q ^ 4) ^ 2 := by
    rw [show (4 : ℕ) = 2 * 2 from rfl, pow_mul, hs]
  have hq0 : q ≠ 0 := by positivity
  have hne : (-1 : ℝ) + q ^ 2 ≠ 0 := by nlinarith
  have hne' : q ^ 2 - 1 ≠ 0 := by nlinarith
  ring_nf
  simp only [hs, hs4]
  field_simp
  ring

/-- **Theorem (manuscript): closed-form χ_std for neutron.** -/
-- Ref: [leitner2026] docs/chi-std-pernucleon-theorem.md §Proof
theorem chi_std_neutron_closed_form (q : ℝ) (hq : 1 < q) :
    chiStdEval q (neutronBraid (q - q⁻¹)) =
      chiStdClosedForm q neutronIndices := by
  simp [chiStdEval, evalWord, neutronBraid, heckeFactorMat, hoefsmit_σ₁, hoefsmit_σ₂, M2.mul_eq, M2.one_eq, M2.smul_eq,
    M2.add, M2.mul, M2.smul, M2.one, M2.trace, chiStdClosedForm, neutronIndices, qNum]
  have hs : Real.sqrt (1 + q ^ 2 + q ^ 4) ^ 2 = 1 + q ^ 2 + q ^ 4 :=
    Real.sq_sqrt (by positivity)
  have hs4 : Real.sqrt (1 + q ^ 2 + q ^ 4) ^ 4 = (1 + q ^ 2 + q ^ 4) ^ 2 := by
    rw [show (4 : ℕ) = 2 * 2 from rfl, pow_mul, hs]
  have hq0 : q ≠ 0 := by positivity
  have hne : (-1 : ℝ) + q ^ 2 ≠ 0 := by nlinarith
  have hne' : q ^ 2 - 1 ≠ 0 := by nlinarith
  ring_nf
  simp only [hs, hs4]
  field_simp
  ring

/-- Both nucleon characters share the unified ladder shape
    `{m, m-2, m-4, m-8}`, with `m_proton = 11`, `m_neutron = 9`.
    This is established purely by unfolding the closed-form
    definitions and the index-set lists — no matrix manipulation. -/
theorem chi_std_ladder_shape (q : ℝ) :
    chiStdClosedForm q protonIndices =
      (q - q⁻¹) / 4 *
        (qNum q 11 + qNum q 9 + qNum q 7 + qNum q 3) ∧
    chiStdClosedForm q neutronIndices =
      (q - q⁻¹) / 4 *
        (qNum q 9 + qNum q 7 + qNum q 5 + qNum q 1) := by
  refine ⟨?_, ?_⟩
  · show (q - q⁻¹) / 4 *
        ((protonIndices.map (qNum q)).sum) =
        (q - q⁻¹) / 4 *
        (qNum q 11 + qNum q 9 + qNum q 7 + qNum q 3)
    simp [protonIndices, List.map, List.sum_cons, List.sum_nil]
    exact Or.inl (by ring)
  · show (q - q⁻¹) / 4 *
        ((neutronIndices.map (qNum q)).sum) =
        (q - q⁻¹) / 4 *
        (qNum q 9 + qNum q 7 + qNum q 5 + qNum q 1)
    simp [neutronIndices, List.map, List.sum_cons, List.sum_nil]
    exact Or.inl (by ring)

/-- Cardinality of each index set: 4 indices per nucleon. -/
theorem protonIndices_length : protonIndices.length = 4 := rfl

theorem neutronIndices_length : neutronIndices.length = 4 := rfl

/-- Ladder gap pattern `{Δ=2, 2, 4}` from largest to smallest:
    both sequences drop by 2, 2, 4. -/
theorem ladder_gaps_proton :
    ∃ m, protonIndices = [m, m - 2, m - 4, m - 8] := ⟨11, rfl⟩

theorem ladder_gaps_neutron :
    ∃ m, neutronIndices = [m, m - 2, m - 4, m - 8] := ⟨9, rfl⟩

end QOU.ChiStdPerNucleon
