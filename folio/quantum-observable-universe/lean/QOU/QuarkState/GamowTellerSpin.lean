/-
# The spin (Gamow–Teller) sector of the β vertex

Bean `qou-99qc`. Owner (Carl), 2026-11-20: derive the β-decay rate as a function of `q`, nothing chosen.
#8638 (`ChargedCurrentW.lean`) derived the charged current `h·(E⊗F)` on the isospin doublet; its β block is
Fermi-type only. This file asks where the spin factor `(1 + 3λ²)` can come from.
Pre-registered in `computations/probes/qbeta_gt_spin/PREREGISTRATION.md`.

## Part A — factorised strand space: no axial current at any `q`

If the strand space is `V_iso ⊗ V_spin` with the spin braided by the swap `P` (the only classical choice
compatible with `QuarkStrandConsequences.three_eigenvalues_no_quadratic`, which forbids a second
`q`-braided factor), every crossing is `X ⊗ₖ P`. `crossing_commutes_spin` : such a crossing commutes with
`1 ⊗ₖ B` for every `B` commuting with `P`, and `swap_commutes_sym` : `P` commutes with the total-spin
generator `X ⊗ₖ 1 + 1 ⊗ₖ X` for every `2 × 2` matrix `X`. So every braid word conserves total spin
strand by strand; the β block is `(isospin part) ⊗ 1_spin`, a pure vector (Fermi) current. **`λ ≡ 0`.**

## Part W — unfactorised `U_q(gl₄)` strand: the quark-level current is `h·P_spin`, `λ_q = 1`

Strand labels `Fin 4`, read as `u↑, u↓, d↑, d↓` (`0, 1, 2, 3`), ordered by a rank `r`. The strand-tracked
Jimbo crossing `P·Ř` has, for `a ≠ b`, coefficient `δ` (pass-through) plus `h` on the exchanged labels when
`r a > r b` (`jstrand`).

* `beta_block_isoMajor` : if both `u` labels rank below both `d` labels, the block
  `d_s ⊗ ν_{s'} → u_t ⊗ e_{t'}` equals `h · P_spin(t t' ; s s')`.
* `beta_block_zero_of_lt` : if `r (d_s) < r (u_{s'})` that entry is `0` (chirality of the exchange).
* `swap_fierz` : `P = ½(1 ⊗ 1 + σ_z ⊗ σ_z) + σ⁺ ⊗ σ⁻ + σ⁻ ⊗ σ⁺`, i.e. `P = ½(1 + σ⃗·σ⃗)` written without `i`.
  So the quark-level block has Fermi and Gamow–Teller parts of equal weight: `λ_q = 1`, independent of `q`.

## What is NOT proved here

The nucleon-level `λ_N(q)`: it needs a nucleon state in the `q`-symmetric 20, and no Hopf-compatible
`SU(2)_spin × SU(2)_iso` inside `U_q(gl₄)` separates `N` from `Δ`. The probe computes it under the labelled
classical-SU(6) choice (|λ| → 5/3 at `q → 1`). The ordering `r` is a choice: 4 of 24 orderings give the
full rotation-invariant current (`beta_block_isoMajor`), and within those the `u↑/u↓` order changes the
nucleon-level value at `q ≠ 1`. The lepton premise (fourth strand, `ν = u`, `e⁻ = d`) is inherited from #8638.

Base ring (§7c): generic `[Field K]`; `swap_fierz` needs `(2 : K) ≠ 0`. No `ℝ`, no `sorry`.

-- Ref: [jimbo1986] https://doi.org/10.1007/BF00400222
-- Ref: [kassel1995] Quantum Groups, Springer GTM 155, §VIII (Jimbo R-matrix of U_q(gl_N))
-/
import Mathlib.Data.Matrix.Mul
import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring

namespace QOU.QuarkState.GamowTellerSpin

open Matrix
open scoped Kronecker

variable {K : Type*} [Field K]

/-! ## Part A -/

/-- The spin swap `P` on `V_spin ⊗ V_spin`, indexed by `Fin 2 × Fin 2`. -/
def swapS : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) K := fun i j => if i = (j.2, j.1) then 1 else 0

/-- **A crossing that braids spin by the swap commutes with every spin operator that commutes with
the swap.** -/
theorem crossing_commutes_spin {ι : Type*} [Fintype ι] [DecidableEq ι] (X : Matrix ι ι K)
    (B : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) K) (hB : B * swapS = swapS * B) :
    (X ⊗ₖ swapS) * ((1 : Matrix ι ι K) ⊗ₖ B) = ((1 : Matrix ι ι K) ⊗ₖ B) * (X ⊗ₖ swapS) := by
  rw [← mul_kronecker_mul, ← mul_kronecker_mul, mul_one, one_mul, hB]

/-- **The swap commutes with the two-strand total of any one-strand spin operator.** -/
theorem swap_commutes_sym (X : Matrix (Fin 2) (Fin 2) K) :
    (X ⊗ₖ (1 : Matrix (Fin 2) (Fin 2) K) + (1 : Matrix (Fin 2) (Fin 2) K) ⊗ₖ X) * swapS
      = swapS * (X ⊗ₖ (1 : Matrix (Fin 2) (Fin 2) K) + (1 : Matrix (Fin 2) (Fin 2) K) ⊗ₖ X) := by
  ext ⟨a, b⟩ ⟨c, d⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp [swapS, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two, Matrix.kroneckerMap_apply,
      Matrix.one_apply, Matrix.add_apply] <;> ring

/-! ## Part W -/

/-- Label of a strand: `isospin` (`0 = u`, `1 = d`) and `spin` (`0 = ↑`, `1 = ↓`), index `2·iso + spin`. -/
def lab (iso s : Fin 2) : Fin 4 := ⟨2 * iso.val + s.val, by omega⟩

/-- Coefficient of strand-tracked output `(c, d)` from input `(a, b)` in `P·Ř` (Jimbo, `U_q(gl₄)`),
ordering given by a rank `r`. -/
def jstrand (r : Fin 4 → ℕ) (q : K) (a b c d : Fin 4) : K :=
  if a = b then (if c = a ∧ d = b then q else 0)
  else (if c = a ∧ d = b then 1 else 0)
    + (if r b < r a ∧ c = b ∧ d = a then q - q⁻¹ else 0)

/-- The `2 × 2`-spin β block: quark `d_s` and lepton `ν_{s'} = u_{s'}` in, quark `u_t` and lepton
`e_{t'} = d_{t'}` out. -/
def betaBlock (r : Fin 4 → ℕ) (q : K) (t t' s s' : Fin 2) : K :=
  jstrand r q (lab 1 s) (lab 0 s') (lab 0 t) (lab 1 t')

/-- The spin swap, entrywise. -/
def swapE (t t' s s' : Fin 2) : K := if t = s' ∧ t' = s then 1 else 0

/-- **Iso-major ordering: the quark-level β block is `h · P_spin`.** -/
theorem beta_block_isoMajor (r : Fin 4 → ℕ) (q : K)
    (hr : ∀ s s' : Fin 2, r (lab 0 s') < r (lab 1 s)) (t t' s s' : Fin 2) :
    betaBlock r q t t' s s' = (q - q⁻¹) * swapE t t' s s' := by
  have h := hr s s'
  fin_cases t <;> fin_cases t' <;> fin_cases s <;> fin_cases s' <;>
    simp_all [betaBlock, jstrand, swapE, lab, Fin.ext_iff]

/-- **Chirality:** an exchange whose `d` label ranks below the `u` label is absent from `σ`. -/
theorem beta_block_zero_of_lt (r : Fin 4 → ℕ) (q : K) (t t' s s' : Fin 2)
    (h : r (lab 1 s) < r (lab 0 s')) : betaBlock r q t t' s s' = 0 := by
  have h' : ¬ r (lab 0 s') < r (lab 1 s) := by omega
  fin_cases t <;> fin_cases t' <;> fin_cases s <;> fin_cases s' <;>
    simp_all [betaBlock, jstrand, lab, Fin.ext_iff]

/-- `σ_z`, `σ⁺`, `σ⁻` on one spin. -/
def sz : Matrix (Fin 2) (Fin 2) K := !![1, 0; 0, -1]
def sp' : Matrix (Fin 2) (Fin 2) K := !![0, 1; 0, 0]
def sm : Matrix (Fin 2) (Fin 2) K := !![0, 0; 1, 0]

/-- **Fierz:** `P = ½(1 ⊗ 1 + σ_z ⊗ σ_z) + σ⁺ ⊗ σ⁻ + σ⁻ ⊗ σ⁺`, i.e. `P = ½(1 + σ⃗·σ⃗)`, so a block
proportional to `P` carries Fermi and Gamow–Teller parts with equal coefficient: `λ = 1`. -/
theorem swap_fierz (h2 : (2 : K) ≠ 0) :
    (swapS : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) K)
      = (2 : K)⁻¹ • ((1 : Matrix (Fin 2) (Fin 2) K) ⊗ₖ (1 : Matrix (Fin 2) (Fin 2) K) + sz ⊗ₖ sz)
        + sp' ⊗ₖ sm + sm ⊗ₖ sp' := by
  ext ⟨a, b⟩ ⟨c, d⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp [swapS, sz, sp', sm, Matrix.kroneckerMap_apply, Matrix.add_apply,
      Matrix.smul_apply] <;> field_simp <;> ring

end QOU.QuarkState.GamowTellerSpin
