import Mathlib.Algebra.Algebra.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum

/-!
# The order of an isospin projector and the γγ bond is a reading-orientation choice

Owner ask (2026-10-11, "explore all", item 1), follow-up to
`QOU/Mass/GammaGammaIsospinChannel.lean`. That file and its probe compute six compositions of
the isospin projector `P_T = a + b·σ₂` (of the interface generator) with the γγ-selected bond
`G = (σ₂σ₃⁻¹)³`; only C5 (`W·P·G` over `W·P`) has the physical sign pattern, and it differs
from the inverted C4 (`W·G·P` over `W·P`) only in the order of `P` and `G`. The question here
is whether anything **derives** that order. This file proves two structural facts; neither
selects a composition.

* **The order is not vacuous** (`isospinProj_comm_bond`, `s2_bond_comm_ne_zero`). Since
  `P_T = a + b·σ` with `b ≠ 0`, `P_T` commutes with `G` iff `σ₂` does, and in the generic
  two-dimensional `(2,1)` representation of the Hecke algebra on `σ₂, σ₃` the commutator
  `[σ₂, G]` has `(0,0)` entry `−(q² − 1)²(q⁴ + 1)/q⁵`, nonzero for `q² ≠ 1`, `q⁴ ≠ −1`.
  (The probe measures `tr(W·[σ₂, G]) ≠ 0` on the full `H₆` word for all four species.)
* **The order is the same choice as the reading orientation** (`trace_PG_eq_reversed_GP`,
  `channel_ratio_C5_eq_reversed_C4`). For any anti-automorphism `ι` fixing `σ` under which the
  trace is invariant — the Hecke word reversal `σ_i ↦ σ_i`, under which the Markov trace is
  invariant — cyclicity gives `tr(W·P·G) = tr(ιW·ιG·P)` and `tr(W·P) = tr(ιW·P)`. So the C5
  ratio of `(W, G)` **is** the C4 ratio of `(ιW, ιG)`. Choosing C5 over C4 is choosing to read
  every nucleon word and the vertex backwards. The bare functional is orientation-blind
  (`trace_bare_orientation_blind`); compositions symmetric in `P` (`P·G·P`) are orientation-
  covariant (`trace_PGP_covariant`).

What this does **not** do: it does not derive orientation-covariance as a requirement, and it
does not pick among the covariant forms (`P·G·P` over `W` or over `W·P`, the symmetrised
`(PG + GP)/2` over either), which give different numbers in
`computations/probes/gamma-gamma-isospin-composition-rule-probe.witness.json`.

Base ring: generic `CommRing R` / `Ring A` for the orientation section (§7c); the
representation section needs inverses and is over a generic `Field K`, never `ℝ`.
-/

namespace QOU.Mass.IsospinBondCompositionOrientation

section Orientation

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- An anti-automorphism `ι` that fixes `σ` fixes every element `a·1 + b·σ` of the interface
span, in particular both isospin projectors. -/
theorem iota_fix_interface (ι : A →ₗ[R] A) (hι1 : ι 1 = 1) (σ : A) (hσ : ι σ = σ)
    (a b : R) : ι (a • (1 : A) + b • σ) = a • (1 : A) + b • σ := by
  rw [map_add, map_smul, map_smul, hι1, hσ]

/-- `P = a + b·σ` commutes with `G` iff `b·[σ, G] = 0`: the commutator of a projector with the
bond is `b` times the commutator of the interface generator with it. -/
theorem isospinProj_comm_bond (σ G : A) (a b : R) :
    (a • (1 : A) + b • σ) * G - G * (a • (1 : A) + b • σ) = b • (σ * G - G * σ) := by
  simp only [add_mul, mul_add, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_sub]
  abel

variable (tr : A →ₗ[R] R) (ι : A → A)
  (hι : ∀ x y, ι (x * y) = ι y * ι x) (htrι : ∀ x, tr (ι x) = tr x)
  (hcyc : ∀ x y, tr (x * y) = tr (y * x))
include hι htrι hcyc

/-- **C5 read forwards is C4 read backwards.** `tr(W·P·G) = tr(ιW·ιG·P)` for `ι P = P`. -/
theorem trace_PG_eq_reversed_GP (W P G : A) (hP : ι P = P) :
    tr (W * P * G) = tr (ι W * ι G * P) := by
  rw [← htrι (W * P * G), hι, hι, hP, ← mul_assoc, hcyc, mul_assoc]

/-- And symmetrically `tr(W·G·P) = tr(ιW·P·ιG)` (C1 forwards is C2 backwards). -/
theorem trace_GP_eq_reversed_PG (W P G : A) (hP : ι P = P) :
    tr (W * G * P) = tr (ι W * P * ι G) := by
  rw [← htrι (W * G * P), hι, hι, hP, hcyc, mul_assoc, hcyc]

/-- The channel-relative normalisation is orientation-blind: `tr(W·P) = tr(ιW·P)`. -/
theorem trace_WP_reversed (W P : A) (hP : ι P = P) : tr (W * P) = tr (ι W * P) := by
  rw [← htrι (W * P), hι, hP, hcyc]

/-- The bare bond functional is orientation-blind: `tr(ιW·ιG) = tr(W·G)`. -/
theorem trace_bare_orientation_blind (W G : A) : tr (ι W * ι G) = tr (W * G) := by
  rw [← hι, htrι, hcyc]

/-- The compression `P·G·P` is orientation-covariant: `tr(W·(P·G·P)) = tr(ιW·(P·ιG·P))`. -/
theorem trace_PGP_covariant (W P G : A) (hP : ι P = P) :
    tr (W * (P * G * P)) = tr (ι W * (P * ι G * P)) := by
  rw [← htrι (W * (P * G * P)), hι, hι, hι, hP, hcyc]
  simp only [mul_assoc]

end Orientation

section Ratio

variable {K A : Type*} [Field K] [Ring A] [Algebra K A]
  (tr : A →ₗ[K] K) (ι : A → A)
  (hι : ∀ x y, ι (x * y) = ι y * ι x) (htrι : ∀ x, tr (ι x) = tr x)
  (hcyc : ∀ x y, tr (x * y) = tr (y * x))
include hι htrι hcyc

/-- **The C5 channel ratio of `(W, G)` equals the C4 channel ratio of `(ιW, ιG)`.** -/
theorem channel_ratio_C5_eq_reversed_C4 (W P G : A) (hP : ι P = P) :
    tr (W * P * G) / tr (W * P) = tr (ι W * ι G * P) / tr (ι W * P) := by
  rw [trace_PG_eq_reversed_GP tr ι hι htrι hcyc W P G hP,
    trace_WP_reversed tr ι hι htrι hcyc W P hP]

end Ratio

section Representation

variable {K : Type*} [Field K]

/-- `σ₂` in the generic `(2,1)` representation of the Hecke algebra on `σ₂, σ₃`. -/
def s2m (q : K) : Matrix (Fin 2) (Fin 2) K := !![q, 1; 0, -q⁻¹]
/-- `σ₃` in the same representation. -/
def s3m (q : K) : Matrix (Fin 2) (Fin 2) K := !![-q⁻¹, 0; 1, q]
/-- `σ₃⁻¹ = σ₃ − (q − q⁻¹)`. -/
def s3inv (q : K) : Matrix (Fin 2) (Fin 2) K := !![-q, 0; 1, q⁻¹]

theorem s3m_mul_s3inv (q : K) (hq : q ≠ 0) : s3m q * s3inv q = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [s3m, s3inv, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp

/-- Hecke quadratic `(σ₂ − q)(σ₂ + q⁻¹) = 0`. -/
theorem s2m_quadratic (q : K) :
    (s2m q - q • 1) * (s2m q + q⁻¹ • 1) = 0 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [s2m, Matrix.mul_apply, Fin.sum_univ_two]

/-- Hecke quadratic for `σ₃`. -/
theorem s3m_quadratic (q : K) :
    (s3m q - q • 1) * (s3m q + q⁻¹ • 1) = 0 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [s3m, Matrix.mul_apply, Fin.sum_univ_two]

/-- Braid relation `σ₂σ₃σ₂ = σ₃σ₂σ₃`. -/
theorem braid_rel (q : K) (hq : q ≠ 0) :
    s2m q * s3m q * s2m q = s3m q * s2m q * s3m q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [s2m, s3m, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

/-- The γγ vertex `V = σ₂σ₃⁻¹`, explicitly. -/
theorem vertex_eq (q : K) (hq : q ≠ 0) :
    s2m q * s3inv q = !![1 - q ^ 2, q⁻¹; -q⁻¹, -(q ^ 2)⁻¹] := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [s2m, s3inv, Matrix.mul_apply, Fin.sum_univ_two] <;> (field_simp; try ring)

/-- The bond `G = V³`, explicitly. -/
theorem bond_eq (q : K) (hq : q ≠ 0) :
    (s2m q * s3inv q) ^ 3 =
      !![-(q ^ 5 - q ^ 4 - q ^ 3 + q ^ 2 - 1) * (q ^ 5 + q ^ 4 - q ^ 3 - q ^ 2 + 1) / q ^ 4,
          (q - 1) ^ 2 * (q + 1) ^ 2 * (q ^ 4 + 1) / q ^ 5;
         -((q - 1) ^ 2 * (q + 1) ^ 2 * (q ^ 4 + 1)) / q ^ 5,
          (q ^ 3 - q ^ 2 + 1) * (q ^ 3 + q ^ 2 - 1) / q ^ 6] := by
  rw [vertex_eq q hq]
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [pow_succ, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

/-- **`σ₂` does not commute with the γγ bond.** The `(0,0)` entry of `[σ₂, G]`. -/
theorem s2_bond_comm_entry (q : K) (hq : q ≠ 0) :
    (s2m q * (s2m q * s3inv q) ^ 3 - (s2m q * s3inv q) ^ 3 * s2m q) 0 0 =
      -((q ^ 2 - 1) ^ 2 * (q ^ 4 + 1)) / q ^ 5 := by
  rw [bond_eq q hq]
  simp [s2m]
  field_simp
  ring

theorem s2_bond_comm_ne_zero (q : K) (hq : q ≠ 0) (h2 : q ^ 2 ≠ 1) (h4 : q ^ 4 + 1 ≠ 0) :
    s2m q * (s2m q * s3inv q) ^ 3 - (s2m q * s3inv q) ^ 3 * s2m q ≠ 0 := by
  intro h
  have := s2_bond_comm_entry q hq
  rw [h] at this
  have hq5 : q ^ 5 ≠ 0 := pow_ne_zero _ hq
  have hsub : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr h2
  have : (q ^ 2 - 1) ^ 2 * (q ^ 4 + 1) = 0 := by
    simp only [Matrix.zero_apply] at this
    field_simp at this
    linear_combination this
  rcases mul_eq_zero.mp this with h' | h'
  · exact hsub (pow_eq_zero_iff (by norm_num) |>.mp h')
  · exact h4 h'

end Representation

end QOU.Mass.IsospinBondCompositionOrientation

-- Axiom audit (run with `lean`-direct; not part of the build):
-- #print axioms QOU.Mass.IsospinBondCompositionOrientation.channel_ratio_C5_eq_reversed_C4
-- #print axioms QOU.Mass.IsospinBondCompositionOrientation.s2_bond_comm_ne_zero
