import QOU.IwahoriHecke.BalancedGenerators
import Mathlib.Data.Matrix.Basic

/-!
# The `sl₂` R-matrix is a §7a Hecke generator

The braiding half of quantum Schur–Weyl. `QOU.MassTheory.WeightedPermutationCharacter`
supplied the *trace-weight* half of the `q ≠ 1` deformation — one `q`-factor per orbit,
with the fibre `κ = Fin 2` carrying `K = diag(1, q²)`. The other half is the **braiding**:
at `q ≠ 1` the symmetric group no longer acts by permuting tensor factors, and its
replacement is the Iwahori–Hecke algebra acting through Jimbo's R-matrix.

This file supplies the generator of that action for the fundamental of `U_q(sl₂)` and
proves the one fact that makes it a Hecke action:

    Ř² = (q − q⁻¹) Ř + 1,

i.e. `IsHeckeGenerator q qi Ř` in the sense of `QOU.MathlibExt.SkeinRelation`, which is the
symmetric normalisation AGENTS.md §7a mandates. So `Ř` has eigenvalues `q` (symmetric
channel) and `−q⁻¹` (antisymmetric channel) — the `q`-deformation of the `±1` eigenvalues of
the transposition it degenerates to.

## The degeneration is proved, not asserted

`rCheck_one` shows `Ř` at `q = qi = 1` is exactly the flip `e_i ⊗ e_j ↦ e_j ⊗ e_i` — the
permutation matrix of the transposition. That is the concrete link to the `q = 1` character
of `QOU.MassTheory.TensorPowerTrace`: the classical `2^{c(σ)}` trace is the `q → 1` limit of
this braiding, and the limit is checked here rather than assumed.

## Scope

* **Fibre `Fin 2` only.** The general `gl_n` R-matrix
  `Ř = q Σ_i E_ii⊗E_ii + Σ_{i≠j} E_ji⊗E_ij + (q − q⁻¹) Σ_{i<j} E_ii⊗E_jj`
  has the same quadratic for any linearly ordered index type; only `Fin 2` is done here,
  because `Fin 2` is the fibre every consumer in this corpus uses (`weighted_character_two`,
  `trace_permMatrixOf_two`, `ClassicalTraceFloor`'s `2^{c(σ)}`).
* **`n = 3` only.** Both relations are proved — the quadratic (`isHeckeGenerator_rCheck`)
  and Yang–Baxter (`yangBaxter`) — and `heckeAction` feeds them to
  `QOU.IwahoriHecke.Balanced.liftBalanced` to produce an actual algebra map
  `H₃(q) → End(V^{⊗3})`. General `n` needs the embedding of a two-site operator at each
  position `i` of `V^{⊗n}`, which is not built here.
* **Nothing is claimed about the image.** `heckeAction` is an algebra map; that it is
  *surjective onto the commutant* of the quantum-group action — the Schur–Weyl statement
  proper — is not proved and does not follow from anything here.

-- Ref: [jimbo1986] Jimbo, "A q-difference analogue of U(g) and the Yang-Baxter equation"
-- Ref: [leitner2026] AGENTS.md §7a; bean qou-k4oq
-/

namespace QOU.IwahoriHecke.RMatrix

open QOU.MathlibExt.SkeinRelation

variable {R : Type*} [CommRing R]

/-- **Jimbo's `Ř`-matrix** for the fundamental of `U_q(sl₂)`, on `V ⊗ V` with
`V = Fin 2 → R`, indexed by `Fin 2 × Fin 2`.

On basis vectors:

* `Ř (eᵢ ⊗ eᵢ) = q · eᵢ ⊗ eᵢ` — the symmetric channel, eigenvalue `q`;
* `Ř (e₀ ⊗ e₁) = e₁ ⊗ e₀ + (q − qi) · e₀ ⊗ e₁`;
* `Ř (e₁ ⊗ e₀) = e₀ ⊗ e₁`.

At `q = qi = 1` the middle coefficient vanishes and this is the flip (`rCheck_one`). -/
def rCheck (q qi : R) : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R :=
  Matrix.of fun a b =>
    if a = b then (if b.1 = b.2 then q else if b.1 < b.2 then q - qi else 0)
    else if a = (b.2, b.1) then 1 else 0

variable (q qi : R)

@[simp] theorem rCheck_apply (a b : Fin 2 × Fin 2) :
    rCheck q qi a b
      = if a = b then (if b.1 = b.2 then q else if b.1 < b.2 then q - qi else 0)
        else if a = (b.2, b.1) then 1 else 0 := rfl

/-- **The R-matrix satisfies the §7a Hecke quadratic relation.**

`Ř² = (q − qi) Ř + 1`, so `Ř` has eigenvalues `q` and `−qi`. This is the statement that
makes the braiding a *Hecke* braiding rather than merely an invertible operator, and it is
where `q * qi = 1` is used: without it the diagonal entries give `q² ≠ (q − qi)q + 1`. -/
theorem rCheck_sq (hqi : q * qi = 1) :
    rCheck q qi * rCheck q qi = (q - qi) • rCheck q qi + 1 := by
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [rCheck, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
      Prod.ext_iff] <;>
    linear_combination hqi

/-- **`Ř` is a Hecke generator** in the sense of `QOU.MathlibExt.SkeinRelation` — the
symmetric normalisation of AGENTS.md §7a.

Everything that file proves therefore applies: `Ř` is a unit with explicit inverse
`Ř − (q − qi)`, it satisfies the skein relation `Ř − Ř⁻¹ = q − qi`, and it factors as
`(Ř − q)(Ř + qi) = 0`. -/
theorem isHeckeGenerator_rCheck (hqi : q * qi = 1) :
    IsHeckeGenerator q qi (rCheck q qi) := by
  show rCheck q qi * rCheck q qi
      = algebraMap R (Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R) (q - qi) * rCheck q qi + 1
  rw [Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul]
  exact rCheck_sq q qi hqi

/-- **The eigenvalue factorisation**, from the bridge: `(Ř − q)(Ř + qi) = 0`. The symmetric
and antisymmetric channels of the `q`-deformed braiding. -/
theorem rCheck_eigen (hqi : q * qi = 1) :
    (rCheck q qi - algebraMap R _ q) * (rCheck q qi + algebraMap R _ qi) = 0 :=
  (isHeckeGenerator_iff_factored hqi _).mp (isHeckeGenerator_rCheck q qi hqi)

/-- **`Ř` is invertible**, with the negative crossing `Ř − (q − qi)` as its explicit
two-sided inverse. -/
theorem isUnit_rCheck (hqi : q * qi = 1) : IsUnit (rCheck q qi) :=
  isUnit_of_isHeckeGenerator (isHeckeGenerator_rCheck q qi hqi)

/-- **The skein relation for the R-matrix**: `Ř − Ř⁻¹ = q − qi`. Stated against an
arbitrary right inverse — a right inverse of `Ř` has no choice but to be the negative
crossing. -/
theorem rCheck_sub_inv (hqi : q * qi = 1) {S : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R}
    (hS : rCheck q qi * S = 1) :
    rCheck q qi - S = algebraMap R _ (q - qi) :=
  sub_inv_eq (isHeckeGenerator_rCheck q qi hqi) hS

/-! ## The `q = 1` degeneration -/

/-- The flip `eᵢ ⊗ eⱼ ↦ eⱼ ⊗ eᵢ` on `V ⊗ V`, as a matrix. -/
def flip : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R :=
  Matrix.of fun a b => if a = (b.2, b.1) then 1 else 0

/-- **At `q = 1` the R-matrix IS the transposition.** The `q`-deformed braiding degenerates
to the symmetric-group action that `QOU.MassTheory.TensorPowerTrace` computes the character
of — so the `2^{c(σ)}` classical trace is this braiding's `q → 1` limit, checked rather
than assumed. -/
theorem rCheck_one : rCheck (1 : R) (1 : R) = flip := by
  ext a b
  fin_cases a <;> fin_cases b <;> simp [rCheck, flip, Prod.ext_iff]

/-- At `q = 1` the braiding is an involution: `Ř² = 1`, the transposition relation. -/
theorem rCheck_one_sq : rCheck (1 : R) (1 : R) * rCheck (1 : R) (1 : R) = 1 := by
  have h := rCheck_sq (1 : R) (1 : R) (by ring)
  simpa using h

/-! ## Yang-Baxter -/

/-- `Ř₁ = Ř ⊗ id` on `V ⊗ V ⊗ V`: the braiding acting on the first two factors. -/
def rc1 (q qi : R) : Matrix (Fin 2 × Fin 2 × Fin 2) (Fin 2 × Fin 2 × Fin 2) R :=
  Matrix.of fun a b => rCheck q qi (a.1, a.2.1) (b.1, b.2.1) * (if a.2.2 = b.2.2 then 1 else 0)

/-- `Ř₂ = id ⊗ Ř` on `V ⊗ V ⊗ V`: the braiding acting on the last two factors. -/
def rc2 (q qi : R) : Matrix (Fin 2 × Fin 2 × Fin 2) (Fin 2 × Fin 2 × Fin 2) R :=
  Matrix.of fun a b => (if a.1 = b.1 then 1 else 0) * rCheck q qi (a.2.1, a.2.2) (b.2.1, b.2.2)

set_option maxHeartbeats 2000000 in
/-- **The Yang-Baxter equation** `Ř₁Ř₂Ř₁ = Ř₂Ř₁Ř₂` on `V^{⊗3}` — the braid relation for
the `sl₂` R-matrix.

Together with `isHeckeGenerator_rCheck` this is exactly what
`QOU.IwahoriHecke.Balanced.liftBalanced` consumes, so the two of them are the whole input
to a Hecke action on a tensor power.

`q * qi = 1` is genuinely used, and only here: all 64 entries but two are ring identities
in `q` and `qi` separately, and the two survivors differ by `(q·qi − 1)(q − qi)`. So the
braid relation holds for the deformed braiding **because** `qi` is `q⁻¹`, not for formal
reasons. -/
theorem yangBaxter (hqi : q * qi = 1) :
    rc1 q qi * rc2 q qi * rc1 q qi = rc2 q qi * rc1 q qi * rc2 q qi := by
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [rc1, rc2, rCheck, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
      Prod.ext_iff]
  all_goals try ring
  all_goals first | linear_combination (q - qi) * hqi | linear_combination (qi - q) * hqi

/-! ## The Hecke action on `V^{⊗3}`

With both relations in hand, `QOU.IwahoriHecke.Balanced.liftBalanced` turns them into an
actual algebra map out of `H₃(q)`. This is the point of the whole file: `IsHeckeGenerator`
and `yangBaxter` are statements about operators; what quantum Schur-Weyl needs is an
*action*, and this is it. -/

set_option maxHeartbeats 1000000 in
/-- The embedded braiding `Ř₁` satisfies the §7a quadratic. -/
theorem rc1_sq (hqi : q * qi = 1) :
    rc1 q qi * rc1 q qi = (q - qi) • rc1 q qi + 1 := by
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [rc1, rCheck, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
      Prod.ext_iff]
  all_goals try ring
  all_goals linear_combination hqi

set_option maxHeartbeats 1000000 in
/-- The embedded braiding `Ř₂` satisfies the §7a quadratic. -/
theorem rc2_sq (hqi : q * qi = 1) :
    rc2 q qi * rc2 q qi = (q - qi) • rc2 q qi + 1 := by
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [rc2, rCheck, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
      Prod.ext_iff]
  all_goals try ring
  all_goals linear_combination hqi

theorem isHeckeGenerator_rc1 (hqi : q * qi = 1) : IsHeckeGenerator q qi (rc1 q qi) := by
  show rc1 q qi * rc1 q qi = algebraMap R _ (q - qi) * rc1 q qi + 1
  rw [Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul]
  exact rc1_sq q qi hqi

theorem isHeckeGenerator_rc2 (hqi : q * qi = 1) : IsHeckeGenerator q qi (rc2 q qi) := by
  show rc2 q qi * rc2 q qi = algebraMap R _ (q - qi) * rc2 q qi + 1
  rw [Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul]
  exact rc2_sq q qi hqi

/-- The type-`A₂` Coxeter matrix on the two generators of `H₃(q)`: the generators braid
(`m = 3`) and neither commutes with the other. -/
def coxA2 : Fin 2 → Fin 2 → ℕ := fun i j => if i = j then 1 else 3

theorem coxA2_symm : ∀ i j, coxA2 i j = coxA2 j i := by decide

/-- **The Hecke action of `H₃(q)` on `V^{⊗3}`.**

An honest algebra map, not a class: `σ₀ ↦ Ř₁`, `σ₁ ↦ Ř₂`, with the §7a quadratic and the
braid relation discharged by `isHeckeGenerator_rc1`/`rc2` and `yangBaxter`. This is the
braiding half of quantum Schur-Weyl at `n = 3`, realised. -/
noncomputable def heckeAction (hqi : q * qi = 1) :
    QOU.IwahoriHecke.Balanced.BalancedHecke coxA2 q →ₐ[R]
      Matrix (Fin 2 × Fin 2 × Fin 2) (Fin 2 × Fin 2 × Fin 2) R :=
  QOU.IwahoriHecke.Balanced.liftBalanced hqi ![rc1 q qi, rc2 q qi]
    (fun i => by fin_cases i
                 · simpa using isHeckeGenerator_rc1 q qi hqi
                 · simpa using isHeckeGenerator_rc2 q qi hqi)
    (fun i j => by
      have hy : rc1 q qi * (rc2 q qi * rc1 q qi) = rc2 q qi * (rc1 q qi * rc2 q qi) := by
        rw [← mul_assoc, ← mul_assoc]; exact yangBaxter q qi hqi
      fin_cases i <;> fin_cases j <;>
        simp [coxA2] <;>
        first
          | rfl
          | exact hy
          | exact hy.symm)
    coxA2_symm

@[simp] theorem heckeAction_sigma_zero (hqi : q * qi = 1) :
    heckeAction q qi hqi (QOU.IwahoriHecke.Balanced.sigma coxA2 q qi 0) = rc1 q qi := by
  simpa using QOU.IwahoriHecke.Balanced.liftBalanced_sigma (M := coxA2) hqi
    ![rc1 q qi, rc2 q qi] _ _ coxA2_symm 0

@[simp] theorem heckeAction_sigma_one (hqi : q * qi = 1) :
    heckeAction q qi hqi (QOU.IwahoriHecke.Balanced.sigma coxA2 q qi 1) = rc2 q qi := by
  simpa using QOU.IwahoriHecke.Balanced.liftBalanced_sigma (M := coxA2) hqi
    ![rc1 q qi, rc2 q qi] _ _ coxA2_symm 1

end QOU.IwahoriHecke.RMatrix
