import Mathlib.Data.Nat.Choose.Basic
import Mathlib.LinearAlgebra.SymplecticGroup
import Mathlib.LinearAlgebra.Matrix.SpecialLinearGroup
import Mathlib.Tactic

/-!
# Atomicity from self-duality — deriving rank-one from the volume-form axiom (T0 + T2)

**Milestone `qou-atsd`.** The order-separation file
([`AtomicityRankOneOrderSeparation.lean`](AtomicityRankOneOrderSeparation.lean))
reduced atomicity to two premises — the categorical bridge `TensorGenerationFree`
and the jet-tower chain axiom. This file begins **deriving** them from the QOU
axioms rather than assuming them, via the chain

  `[ε : V⊗V→𝟙 symplectic, non-deg] + [dim V = 2]  ⟹  G ⊆ Sp(V) = Sp₂ = SL₂
     ⟹  rank G ≤ dim V / 2 = 1  ⟹  |fundamental objects| ≤ 1`.

**Key distinction kept explicit throughout:** `dim V = 2` is the *cohomological*
input (`H¹(Bring) = 2W` is rank 2 `= dim V`); it is **not** `rank G = 2`. It is
*self-duality* that collapses `dim V = 2 ⇝ rank G = 1` — the `Sp₂ = SL₂` dim-2
accident `rank Sp(2m) = m`.

Tiers realised here (attack plan:
`docs/workplans/2026-07-25-atomicity-from-self-duality-attack-plan.md`):

* **T0** — `Λ²V ≅ 𝟙` non-degenerate forces `dim V = 2`: the arithmetic crux
  `n.choose 2 = 1 → n = 2` (`dim_two_of_choose_two_eq_one`). Sorry-free.
* **T2** — the reduction skeleton at the level of the natural-number invariants
  (`dim V`, `rank G`, `rank Sp`): compose `[rank G ≤ rank Sp(dim V)]` (self-duality
  embedding) `+ [rank Sp(2m) = m]` (the classical residual, **T3**, an explicit
  hypothesis — *not* proved here, *not* an instance) `+ [dim V = 2]` to
  `rank G ≤ 1`, hence `Subsingleton (Fin (rank G))` (`rankG_le_one_of_self_dual`,
  `atomicity_subsingleton_of_self_dual`). Sorry-free.

The two hard classical facts — `rank Sp(2m) = m` (**T3**, symplectic root system)
and `G` connected reductive (**T4**, Tannakian reconstruction) — are named
residuals carried as hypotheses; they are the open content, honestly delimited,
and tracked in beans `qou-atsd-t3` / `qou-atsd-t4`. No axiom fabricates the
conclusion (AGENTS.md §"Axiomatization is NOT a Proof").

-- Ref: [leitner2026] quantum-universes/fundamental-object.ts (volume form ε = Λ²V→𝟙); def:tannaka-dual
-- Ref: [leitner2026] conj:binding-manybody-eq-jet-filtration (jet tower / atomicity)
-/

namespace QOU.Atomicity

/-! ## T0 — `dim V = 2` from `Λ²V ≅ 𝟙` (the categorical determinant is a bilinear form) -/

/-- **T0 — the dimension-two crux.** The categorical determinant
    `ε : Λ²V → 𝟙` being an isomorphism onto the tensor unit means `Λ²V` is
    1-dimensional, i.e. `binom(dim V, 2) = 1`; the only natural number with
    `binom(n, 2) = 1` is `n = 2`. So a non-degenerate volume form on `V` of the
    shape `V ⊗ V → 𝟙` (a *bilinear* determinant) forces `dim V = 2`. -/
theorem dim_two_of_choose_two_eq_one {n : ℕ} (h : n.choose 2 = 1) : n = 2 := by
  rcases n with _ | _ | _ | n
  · simp at h
  · simp at h
  · rfl
  · exfalso
    have hmono : Nat.choose 3 2 ≤ Nat.choose (n + 3) 2 := Nat.choose_le_choose 2 (by omega)
    rw [h] at hmono
    have h3 : Nat.choose 3 2 = 3 := by decide
    omega

/-! ## T2 — the reduction skeleton: rank G ≤ 1 from self-duality + dim 2 -/

/-- **Subsingleton from a rank bound.** `Fin (rank G)` — the set of fundamental
    objects, indexed by `rank G` fundamental weights — is a subsingleton (`≤ 1`
    element) exactly when `rank G ≤ 1`. -/
theorem subsingleton_fin_of_le_one {n : ℕ} (h : n ≤ 1) : Subsingleton (Fin n) := by
  interval_cases n <;> infer_instance

/-- **T2 — the rank collapse (PROVED, modulo the two named classical residuals).**
    Given
    * `hEmbed : rankG ≤ rankSp dimV` — the self-duality embedding `G ⊆ Sp(V)`
      (a symplectic-form-preserving subgroup has rank at most that of `Sp(V)`),
    * `hRankSp : ∀ m, rankSp (2*m) = m` — the classical fact `rank Sp(2m) = m`
      (**T3**; the `m = 1` case is the `Sp₂ = SL₂` dim-2 accident), and
    * `hDim : dimV = 2` — the cohomological input (`dim V = rank H¹(Bring) = 2`),

    the Tannaka dual has `rankG ≤ 1`. This is the arithmetic heart of the atomicity
    derivation; `hRankSp` is an explicit **hypothesis**, never an instance — the
    honest open residual. -/
theorem rankG_le_one_of_self_dual {dimV rankG : ℕ} {rankSp : ℕ → ℕ}
    (hEmbed : rankG ≤ rankSp dimV) (hRankSp : ∀ m, rankSp (2 * m) = m)
    (hDim : dimV = 2) : rankG ≤ 1 := by
  have h1 : rankSp dimV = 1 := by
    rw [hDim, show (2 : ℕ) = 2 * 1 by norm_num, hRankSp 1]
  omega

/-- **Atomicity (PROVED, modulo T3 + T4).** Under the self-duality embedding, the
    classical rank of the symplectic group, and the cohomological `dim V = 2`, the
    fundamental-object set `Fin (rank G)` is a subsingleton — **rank-one**. This is
    the categorical-side conclusion the order-separation file assumes as
    `TensorGenerationFree`/totality; here it is *derived* from the volume-form
    axiom plus the two named classical residuals (`hRankSp` = T3; the connected-
    reductive input T4 is what guarantees `rank G` is the honest torus rank rather
    than `0` for a finite subgroup — recorded, not needed for the `≤ 1` bound). -/
theorem atomicity_subsingleton_of_self_dual {dimV rankG : ℕ} {rankSp : ℕ → ℕ}
    (hEmbed : rankG ≤ rankSp dimV) (hRankSp : ∀ m, rankSp (2 * m) = m)
    (hDim : dimV = 2) : Subsingleton (Fin rankG) :=
  subsingleton_fin_of_le_one (rankG_le_one_of_self_dual hEmbed hRankSp hDim)

/-! ## T1 — the matrix-level self-duality constraint `det² = 1` (Mathlib-ext infra) -/

section SymplecticDet
open Matrix

/-- **T1 — symplectic ⟹ `(det A)² = 1` (matrix-group infra).** A symplectic matrix
    satisfies `A · J · Aᵀ = J`; taking determinants (`det J` is a unit,
    `isUnit_det_J`) gives `(det A)² = 1`. This is the matrix-group shadow of
    "self-duality constrains the determinant": in *every* dimension a
    symplectic-form-preserving map has `det = ±1`. The refinement `det A = +1`
    (excluding `−1`), and thereby the `Sp₂ = SL₂` dim-2 accident, is the deeper
    connectedness / Pfaffian fact — the base case of the classical residual T3,
    tracked in beans `qou-atsd-t1`/`t3`. Holds over any `CommRing`. -/
theorem symplectic_det_sq_eq_one {l : Type*} [DecidableEq l] [Fintype l]
    {R : Type*} [CommRing R] {A : Matrix (l ⊕ l) (l ⊕ l) R}
    (hA : A ∈ symplecticGroup l R) : det A ^ 2 = 1 := by
  have hmem : A * J l R * Aᵀ = J l R := (SymplecticGroup.mem_iff).mp hA
  have hdet : det A * det (J l R) * det A = det (J l R) := by
    have h := congrArg det hmem
    rwa [det_mul, det_mul, det_transpose] at h
  have key : det (J l R) * det A ^ 2 = det (J l R) * 1 := by
    rw [mul_one, sq]; linear_combination hdet
  exact (isUnit_det_J l R).mul_left_cancel key

end SymplecticDet

/-! ## T1′ — `Sp₂ = SL₂` at the matrix level (the dim-2 accident, `det = +1`) -/

section Sp2
open Matrix

/-- The standard 2×2 symplectic form `J₂ = [[0,-1],[1,0]]`. -/
def J2 (R : Type*) [Ring R] : Matrix (Fin 2) (Fin 2) R := !![0, -1; 1, 0]

/-- **The 2×2 symplectic identity.** For any 2×2 matrix, `A · J₂ · Aᵀ = det A • J₂`
    — the dimension-2 fact behind `Sp₂ = SL₂`: contracting a bilinear form with a
    2×2 map scales it by the determinant. Direct entrywise computation
    (`det A = a·d − b·c`). -/
theorem mul_J2_mul_transpose {R : Type*} [CommRing R] (A : Matrix (Fin 2) (Fin 2) R) :
    A * J2 R * Aᵀ = (A.det) • J2 R := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [J2, Matrix.mul_apply, Fin.sum_univ_two, Matrix.det_fin_two,
      Matrix.transpose_apply] <;> ring

/-- **`Sp₂ = SL₂` (matrix level, `det = +1`).** A 2×2 matrix preserves the
    symplectic form `J₂` **iff** its determinant is `1`. This is the sharp dim-2
    accident that upgrades `symplectic_det_sq_eq_one` (`det² = 1`, all dimensions)
    to `det = +1` in dimension 2 — the base case (`m = 1`) of the classical
    `rank Sp(2m) = m` residual (T3): `Sp₂ = SL₂`, a rank-1 group.

    (Mathlib's `symplecticGroup (Fin 1) R` uses the `Fin 1 ⊕ Fin 1` index; the
    correspondence to this `Fin 2` form is a reindex — bean `qou-atsd-t1`.) -/
theorem sp2_mem_iff_det_one {R : Type*} [CommRing R] (A : Matrix (Fin 2) (Fin 2) R) :
    A * J2 R * Aᵀ = J2 R ↔ A.det = 1 := by
  rw [mul_J2_mul_transpose]
  constructor
  · intro h
    have hentry := congrFun (congrFun h 0) 1
    simp [J2] at hentry
    exact hentry
  · intro h; rw [h, one_smul]

end Sp2

/-! ## T3 (elementary, `m = 1`) — the SL₂ maximal torus is rank one (`≅ Rˣ = 𝔾ₘ`) -/

section SL2Torus
open Matrix

variable {R : Type*} [CommRing R]

/-- The diagonal matrix `diag(t, t⁻¹)` for a unit `t` — a point of the SL₂
    maximal torus. -/
def diagMat (t : Rˣ) : Matrix (Fin 2) (Fin 2) R := !![(t : R), 0; 0, (↑t⁻¹ : R)]

/-- `det diag(t, t⁻¹) = t · t⁻¹ = 1`, so the diagonal matrix lies in `SL₂`. -/
theorem diagMat_det (t : Rˣ) : (diagMat t).det = 1 := by
  simp [diagMat, Matrix.det_fin_two, Units.mul_inv]

theorem diagMat_one : diagMat (1 : Rˣ) = (1 : Matrix (Fin 2) (Fin 2) R) := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [diagMat]

theorem diagMat_mul (s t : Rˣ) : diagMat (s * t) = diagMat s * diagMat t := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [diagMat, Matrix.mul_apply, Fin.sum_univ_two, mul_comm]

/-- **The diagonal torus embedding** `Rˣ → SL₂(R)`, `t ↦ diag(t, t⁻¹)`, as a group
    homomorphism (`diag` is multiplicative and unital). -/
def diagEmbedHom : Rˣ →* SpecialLinearGroup (Fin 2) R where
  toFun t := ⟨diagMat t, diagMat_det t⟩
  map_one' := Subtype.ext diagMat_one
  map_mul' s t := Subtype.ext (diagMat_mul s t)

/-- **T3, `m = 1`, the LOWER bound (`rank SL₂ ≥ 1`).** The diagonal torus
    embedding `diagEmbedHom : Rˣ →* SL₂(R)`, `t ↦ diag(t, t⁻¹)`, is **injective**
    (read `s = t` off the `(0,0)` entry). So `SL₂(R)` contains a *faithful* copy of
    the unit group `Rˣ = 𝔾ₘ` as its diagonal torus — the maximal-torus *candidate*
    is realised, giving `rank SL₂ ≥ 1`.

    **Honest scope (critical-distance correction).** This is the **lower** bound.
    The atomicity chain needs `rank G ≤ rank Sp(V) ≤ 1`, i.e. the **upper** bound
    `rank SL₂ ≤ 1` — that this `𝔾ₘ` is *maximal*, that `SL₂` contains **no**
    two-parameter torus. That upper direction (the root-count / "no larger torus"
    fact) is the genuinely hard part and remains **open** (bean `qou-atsd-t3`,
    upper). This lemma builds the torus the maximality argument is *about*; it does
    **not** by itself establish the atomicity bound. Combined with `Sp₂ = SL₂`
    (`sp2_mem_iff_det_one`) it fixes the dimension-2 anchor's torus, one honest
    brick short of `rank G ≤ 1`. -/
theorem diagEmbedHom_injective : Function.Injective (diagEmbedHom (R := R)) := by
  intro s t h
  have hm : diagMat s = diagMat t := Subtype.ext_iff.mp h
  have h00 := congrFun (congrFun hm 0) 0
  simp [diagMat] at h00
  exact Units.ext h00

/-- **T3, `m = 1`, the diagonal torus is EXACTLY `𝔾ₘ` (the torus-level upper
    bound).** A *diagonal* matrix in `SL₂(R)` (off-diagonal entries zero) is
    `diag(t, t⁻¹)` for a unit `t`: from `det = a·d = 1`, `a` is a unit with inverse
    `d`. So the diagonal torus is *precisely* the range of `diagEmbedHom` — a single
    `𝔾ₘ`, **rank exactly 1** (both bounds, for this torus): it cannot be larger.

    This closes the torus-level upper bound. The remaining atomicity gap is
    strictly the *maximality* step — that no larger torus lives elsewhere in `SL₂`
    (all maximal tori conjugate) — which is the root-count fact (bean
    `qou-atsd-t3`, upper). -/
theorem sl2_diagonal_eq_diagEmbed (g : SpecialLinearGroup (Fin 2) R)
    (h01 : (g : Matrix (Fin 2) (Fin 2) R) 0 1 = 0)
    (h10 : (g : Matrix (Fin 2) (Fin 2) R) 1 0 = 0) :
    ∃ t : Rˣ, g = diagEmbedHom t := by
  have hdet : (g : Matrix (Fin 2) (Fin 2) R) 0 0 * (g : Matrix (Fin 2) (Fin 2) R) 1 1 = 1 := by
    have hg := SpecialLinearGroup.det_coe g
    rw [Matrix.det_fin_two, h01, h10] at hg
    simpa using hg
  refine ⟨Units.mkOfMulEqOne _ _ hdet, ?_⟩
  apply Subtype.ext
  ext i j
  have hinv : (↑(Units.mkOfMulEqOne ((g : Matrix (Fin 2) (Fin 2) R) 0 0)
      ((g : Matrix (Fin 2) (Fin 2) R) 1 1) hdet)⁻¹ : R) = (g : Matrix (Fin 2) (Fin 2) R) 1 1 := rfl
  fin_cases i <;> fin_cases j <;>
    simp [diagEmbedHom, diagMat, h01, h10, hinv]

end SL2Torus

/-! ## T3 (`m = 1`) — maximality ingredient: the diagonal torus is self-centralizing -/

section SL2TorusMaximal
open Matrix

variable {R : Type*} [Field R]

/-- **Maximality ingredient — a regular torus element centralizes only diagonals.**
    If a `2×2` matrix `M` commutes with `diag(t, t⁻¹)` for a **regular** unit `t`
    (`t² ≠ 1` — which needs the base ring to carry a unit of order `> 2`, true for
    the archimedean substrate `ℝ`/`ℂ`, false over `𝔽₂`/`𝔽₃`), then `M` is
    **diagonal** (`M 0 1 = M 1 0 = 0`). Proof: the `(0,1)`/`(1,0)` entries of
    `M·diag = diag·M` force `M 0 1·(1 − t²) = 0` and likewise for `M 1 0`, and
    `1 − t² ≠ 0` in a field.

    Consequence: the centralizer of a regular element of the diagonal torus is
    contained in the diagonals, so (with `sl2_diagonal_eq_diagEmbed`) the diagonal
    `𝔾ₘ` is **self-centralizing** — the standard criterion for a *maximal* torus in
    a connected reductive group. This is a genuine ingredient of the maximality
    step (rank ≤ 1); concluding rank ≤ 1 from it still needs the connected-reductive
    structure theory, so it does **not** by itself close the atomicity upper bound
    (bean `qou-atsd-t3`). The `t² ≠ 1` hypothesis honestly records that maximality
    requires the substrate's ring-richness. -/
theorem commute_diagMat_imp_diagonal (M : Matrix (Fin 2) (Fin 2) R) (t : Rˣ)
    (ht : (t : R) ^ 2 ≠ 1) (hcomm : M * diagMat t = diagMat t * M) :
    M 0 1 = 0 ∧ M 1 0 = 0 := by
  have hne : (1 : R) - (t : R) ^ 2 ≠ 0 := sub_ne_zero.mpr (Ne.symm ht)
  have hit : ((t : R))⁻¹ * ↑t = 1 := inv_mul_cancel₀ t.ne_zero
  have e01 := congrFun (congrFun hcomm 0) 1
  have e10 := congrFun (congrFun hcomm 1) 0
  simp [Matrix.mul_apply, Fin.sum_univ_two, diagMat] at e01 e10
  refine ⟨?_, ?_⟩
  · have key : M 0 1 * (1 - (t : R) ^ 2) = 0 := by
      linear_combination (t : R) * e01 - M 0 1 * hit
    exact (mul_eq_zero.mp key).resolve_right hne
  · have key : M 1 0 * (1 - (t : R) ^ 2) = 0 := by
      linear_combination (-(t : R)) * e10 - M 1 0 * hit
    exact (mul_eq_zero.mp key).resolve_right hne

end SL2TorusMaximal

end QOU.Atomicity
