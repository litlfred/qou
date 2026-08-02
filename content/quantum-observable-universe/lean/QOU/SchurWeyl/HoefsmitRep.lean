import QOU.SchurWeyl.HeckeAlgebra
import QOU.SchurWeyl.YoungTableaux
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic

/-!
# `QOU.SchurWeyl.HoefsmitRep` — Hoefsmit seminormal representations of `H_n(q)` (bean SW-4)

The representations `ρ_λ : H_n(q) → M_{d_λ}(K)` of the Iwahori–Hecke algebra, built on the
universal property `Hecke.lift` (bean SW-1) and the Specht dimension `dLambda λ = #SYT(λ)`
(bean SW-2).

## What is delivered here (honest status)

* **The two 1-dimensional representations — fully sorry-free, generic `[CommRing K]`.**
  - `rhoTriv` (index/trivial rep): `σ_i ↦ q`;
  - `rhoSign` (sign rep): `σ_i ↦ -qi` (`= -q⁻¹` once `q·qi = 1`).
  Both are genuine `Hecke →ₐ[K] K` algebra maps produced through the `Hecke.lift` interface, with
  `lift_σ`-based computation lemmas.  Their quadratic relations hold **identically over any
  commutative ring** — no `q·qi = 1` hypothesis is needed (the `q·qi` cross-terms cancel; see
  `rhoTriv` / `rhoSign` proofs).

* **The `n = 3` (i.e. `Hecke K q qi 2`), shape `λ = (2,1)`, `d_λ = 2` seminormal representation —
  fully sorry-free over `ℝ`, including the braid relation.**  `seminormalRep21` is an honest
  `Hecke ℝ q q⁻¹ 2 →ₐ[ℝ] Matrix (Fin 2) (Fin 2) ℝ`; the two generator matrices `S0 = diag(q, -q⁻¹)`
  and the derived seminormal matrix `S1` satisfy the quadratic relation (both) and the single braid
  relation `S0 S1 S0 = S1 S0 S1` by explicit `2×2` matrix computation.  This is the first concrete
  genuinely-`2×2` seminormal braid identity of the program, verified for **all** real `q ≠ 0`.

* **Axial-distance infrastructure — sorry-free.**  `cellContent`, `axialDistance` on Young-diagram
  cells: the content difference that indexes Young's seminormal / orthogonal form.

* **General `λ` seminormal representation — GAP (honestly stated `sorry`).**
  `hoefsmit_seminormal_rep` states the *existence* of a `d_λ`-dimensional seminormal representation
  that is **non-scalar** for `d_λ ≥ 2` (ruling out the trivial `q·1` matrix rep — so the statement
  is non-vacuous and captures the *interesting* representation).  The general construction (the
  seminormal matrices indexed by SYT via axial distances, and the proof of the braid relation in
  full generality) is Hoefsmit's theorem; it is left as a cited `sorry` — see the `-- GAP:` note.

Refs:
- [hoefsmit1974] P. N. Hoefsmit, *Representations of Hecke algebras of finite groups with BN-pairs
  of classical type*, PhD thesis, UBC (1974) — the seminormal form.
- [ram1997] A. Ram, *Seminormal representations of Weyl groups and Iwahori–Hecke algebras*,
  Proc. LMS (1997), https://doi.org/10.1112/S0024611597000282 — the axial-distance formulas.
- [kassel1995] Ch. XII, https://doi.org/10.1007/978-1-4612-0783-2.
-/

namespace QOU.SchurWeyl

open scoped Matrix

/-! ## The two one-dimensional representations (generic `[CommRing K]`, sorry-free)

A one-dimensional representation is an algebra map `H_n(q) →ₐ[K] K` (the `1×1` matrices are `K`
itself).  Building one through `Hecke.lift` amounts to giving a single scalar `g` for every
generator and checking the three Hecke relations degenerate to ring identities. -/

section OneDim

variable (K : Type*) [CommRing K] (q qi : K) (n : ℕ)

/-- **Trivial / index representation** `ρ_triv : H_n(q) →ₐ[K] K`, `σ_i ↦ q`.

The quadratic relation `q·q = (q - qi)·q + (q·qi)·1` is an *identity* over any commutative ring
(the `q·qi` terms cancel: `(q-qi)q + q·qi = q² - qi·q + q·qi = q²`), so **no `q·qi = 1` hypothesis
is required**.  Braid and far-commutation are trivial because scalars commute. -/
noncomputable def rhoTriv : Hecke K q qi n →ₐ[K] K :=
  Hecke.lift K q qi n (fun _ => q)
    (fun _ => by simp only [smul_eq_mul]; ring)
    (fun _ _ => by ring)
    (fun _ _ _ => by ring)

/-- `ρ_triv (σ_i) = q`. -/
@[simp] theorem rhoTriv_σ (i : Fin n) :
    rhoTriv K q qi n (Hecke.σ K q qi n i) = q := by
  simp only [rhoTriv, Hecke.lift_σ]

/-- **Sign representation** `ρ_sign : H_n(q) →ₐ[K] K`, `σ_i ↦ -qi` (`= -q⁻¹` once `q·qi = 1`).

The quadratic relation `(-qi)·(-qi) = (q - qi)·(-qi) + (q·qi)·1` is again an identity over any
commutative ring (`(q-qi)(-qi) + q·qi = -q·qi + qi² + q·qi = qi²`); **no `q·qi = 1` needed**. -/
noncomputable def rhoSign : Hecke K q qi n →ₐ[K] K :=
  Hecke.lift K q qi n (fun _ => -qi)
    (fun _ => by simp only [smul_eq_mul]; ring)
    (fun _ _ => by ring)
    (fun _ _ _ => by ring)

/-- `ρ_sign (σ_i) = -qi`. -/
@[simp] theorem rhoSign_σ (i : Fin n) :
    rhoSign K q qi n (Hecke.σ K q qi n i) = -qi := by
  simp only [rhoSign, Hecke.lift_σ]

end OneDim

/-! ## Axial-distance infrastructure (sorry-free)

Young's seminormal / orthogonal form is indexed by the **content** `c(i,j) = j - i` of a cell and
the **axial distance** (content difference) between the cells carrying consecutive entries.  These
are the data the general Hoefsmit matrices are built from. -/

/-- **Content** of a cell `(i, j)` (row `i`, column `j`): `j - i`, as `ℤ`. -/
def cellContent (c : ℕ × ℕ) : ℤ := (c.2 : ℤ) - (c.1 : ℤ)

/-- **Axial distance** between two cells: the difference of their contents.  In a standard tableau,
`axialDistance (cell of i) (cell of i+1)` is the parameter that determines the `2×2` seminormal
block of the generator `σ_i`. -/
def axialDistance (c d : ℕ × ℕ) : ℤ := cellContent d - cellContent c

/-- Cells in the same row have axial distance equal to their column gap. -/
theorem axialDistance_same_row (i j₁ j₂ : ℕ) :
    axialDistance (i, j₁) (i, j₂) = (j₂ : ℤ) - (j₁ : ℤ) := by
  simp only [axialDistance, cellContent]; ring

/-- Cells in the same column have axial distance equal to the (negated) row gap. -/
theorem axialDistance_same_col (i₁ i₂ j : ℕ) :
    axialDistance (i₁, j) (i₂, j) = (i₁ : ℤ) - (i₂ : ℤ) := by
  simp only [axialDistance, cellContent]; ring

/-! ## The `λ = (2,1)`, `d_λ = 2` seminormal representation over `ℝ` (sorry-free)

`Hecke ℝ q q⁻¹ 2` is `H_3(q)` (two generators `σ_0, σ_1`, one braid relation
`σ_0 σ_1 σ_0 = σ_1 σ_0 σ_1`).  Its `2`-dimensional irreducible (the shape `(2,1)` Specht module)
is afforded by the seminormal matrices

* `S0 = diag(q, -q⁻¹)` — `σ_0` fixes the two SYT `[[1,2],[3]]`, `[[1,3],[2]]` (entries `1,2` share a
  row resp. a column), with eigenvalues `q` resp. `-q⁻¹`;
* `S1` — the square-root-free seminormal (not orthogonal) matrix for `σ_1`, which exchanges the two
  SYT (it swaps `2 ↔ 3`), with the axial-distance–determined entries below.

Both have spectrum `{q, -q⁻¹}` (trace `q - q⁻¹`, determinant `-1`), so each satisfies the quadratic
relation by Cayley–Hamilton; the braid relation is the genuine `2×2` identity verified here for all
`q ≠ 0`.  This crosses the substrate→archimedean wall (§7c), so we specialise to `K := ℝ`. -/

section Seminormal21

variable (q : ℝ)

/-- `σ_0 ↦ diag(q, -q⁻¹)` — diagonal on the two SYT of shape `(2,1)`. -/
noncomputable def S0 : Matrix (Fin 2) (Fin 2) ℝ := !![q, 0; 0, -q⁻¹]

/-- `σ_1 ↦` the square-root-free seminormal matrix.  Entries are the axial-distance rational
functions of `q`: diagonal `-1/(q³+q)`, `q³/(q²+1)`; off-diagonal `1`, `(q⁴+q²+1)/(q²+1)²`.  Chosen
so that the trace is `q - q⁻¹`, the determinant `-1`, and the braid relation with `S0` holds. -/
noncomputable def S1 : Matrix (Fin 2) (Fin 2) ℝ :=
  !![-1 / (q ^ 3 + q), 1; (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2, q ^ 3 / (q ^ 2 + 1)]

private theorem sq_add_one_ne : (q ^ 2 + 1) ≠ 0 := by positivity

private theorem cube_add_ne (hq : q ≠ 0) : (q ^ 3 + q) ≠ 0 := by
  have h : q ^ 3 + q = q * (q ^ 2 + 1) := by ring
  rw [h]; exact mul_ne_zero hq (sq_add_one_ne q)

/-- **Quadratic relation for `S0`** (sorry-free): `S0² = (q - q⁻¹)·S0 + (q·q⁻¹)·1`.
The `q⁻¹` terms cancel symbolically (`ring` treats `q⁻¹` as an atom), so no `q ≠ 0` is needed. -/
theorem S0_quadratic :
    S0 q * S0 q = (q - q⁻¹) • S0 q + (q * q⁻¹) • (1 : Matrix (Fin 2) (Fin 2) ℝ) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [S0, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

/-- **Quadratic relation for `S1`** (sorry-free): `S1² = (q - q⁻¹)·S1 + (q·q⁻¹)·1`. -/
theorem S1_quadratic (hq : q ≠ 0) :
    S1 q * S1 q = (q - q⁻¹) • S1 q + (q * q⁻¹) • (1 : Matrix (Fin 2) (Fin 2) ℝ) := by
  have h1 : (q ^ 2 + 1) ≠ 0 := sq_add_one_ne q
  have h2 : (q ^ 3 + q) ≠ 0 := cube_add_ne q hq
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [S1, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- **Braid relation** (sorry-free): `S0 S1 S0 = S1 S0 S1`.  The genuine `2×2` seminormal braid
identity, verified for all `q ≠ 0`. -/
theorem S0_S1_braid (hq : q ≠ 0) : S0 q * S1 q * S0 q = S1 q * S0 q * S1 q := by
  have h1 : (q ^ 2 + 1) ≠ 0 := sq_add_one_ne q
  have h2 : (q ^ 3 + q) ≠ 0 := cube_add_ne q hq
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [S0, S1, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- **The shape `(2,1)` seminormal representation** `ρ_{(2,1)} : H_3(q) →ₐ[ℝ] M_2(ℝ)`.

Built through `Hecke.lift` from `![S0, S1]`; the three side conditions are `S0_quadratic`,
`S1_quadratic` (for `i = 0, 1`), `S0_S1_braid` (the one braid, `i = 0`), and vacuous
far-commutation (`n = 2` has no `|i-j| ≥ 2`). -/
noncomputable def seminormalRep21 (hq : q ≠ 0) :
    Hecke ℝ q q⁻¹ 2 →ₐ[ℝ] Matrix (Fin 2) (Fin 2) ℝ :=
  Hecke.lift ℝ q q⁻¹ 2 ![S0 q, S1 q]
    (by
      intro i
      fin_cases i
      · show S0 q * S0 q = (q - q⁻¹) • S0 q + (q * q⁻¹) • 1
        exact S0_quadratic q
      · show S1 q * S1 q = (q - q⁻¹) • S1 q + (q * q⁻¹) • 1
        exact S1_quadratic q hq)
    (by
      intro i hi
      fin_cases i
      · show S0 q * S1 q * S0 q = S1 q * S0 q * S1 q
        exact S0_S1_braid q hq
      · exact absurd hi (by decide))
    (by
      intro i j h
      have hi2 : (i : ℕ) < 2 := i.isLt
      exfalso; omega)

/-- `ρ_{(2,1)} (σ_0) = S0`. -/
@[simp] theorem seminormalRep21_σ0 (hq : q ≠ 0) :
    seminormalRep21 q hq (Hecke.σ ℝ q q⁻¹ 2 0) = S0 q := by
  simp [seminormalRep21, Hecke.lift_σ]

/-- `ρ_{(2,1)} (σ_1) = S1`. -/
@[simp] theorem seminormalRep21_σ1 (hq : q ≠ 0) :
    seminormalRep21 q hq (Hecke.σ ℝ q q⁻¹ 2 1) = S1 q := by
  simp [seminormalRep21, Hecke.lift_σ]

end Seminormal21

/-! ## General `λ` seminormal representation — GAP -/

/-- **Hoefsmit seminormal representation, general shape `λ` — GAP.**

For every partition `λ ⊢ N`, there is a `d_λ`-dimensional representation
`ρ_λ : H_N(q) →ₐ[ℝ] M_{d_λ}(ℝ)` (Young's seminormal / Hoefsmit form, built from the axial distances
`axialDistance` between the cells of consecutive entries in each SYT of shape `λ`).  The statement
records the **non-degeneracy** that distinguishes this representation from the trivial `q·1` matrix
rep: for `d_λ ≥ 2` at least one generator is sent to a **non-scalar** matrix.  (A scalar-only rep
`σ_i ↦ q·1` is reducible for `d_λ ≥ 2`; the seminormal rep affords the *irreducible* Specht module
`S^λ`, hence is non-scalar.)

The `1`-dimensional shapes (`d_λ = 1`) are realised concretely and sorry-free above (`rhoTriv`,
`rhoSign`), and the smallest genuinely-`2×2` case `λ = (2,1)` (`N = 3`) is `seminormalRep21`. -/
theorem hoefsmit_seminormal_rep {N : ℕ} (q : ℝ) (hq : q ≠ 0) (lam : Partition N) :
    ∃ ρ : Hecke ℝ q q⁻¹ (N - 1) →ₐ[ℝ] Matrix (Fin (dLambda lam)) (Fin (dLambda lam)) ℝ,
      2 ≤ dLambda lam →
        ∃ i : Fin (N - 1), ∀ s : ℝ,
          ρ (Hecke.σ ℝ q q⁻¹ (N - 1) i) ≠ s • (1 : Matrix (Fin (dLambda lam)) (Fin (dLambda lam)) ℝ) := by
  -- Ref: [hoefsmit1974] (PhD thesis, UBC 1974 — the seminormal form); [ram1997] axial-distance
  --   formulas.  Both keys resolve in `content/schema/references.ts`.
  -- GAP: the general seminormal construction indexes an orthonormal basis by `SYT lam` and defines,
  --   for each generator `σ_i`, the block-diagonal (over SYT orbits under `s_i`) seminormal matrix
  --   whose `2×2` blocks are the axial-distance rational functions realised concretely for `(2,1)`
  --   in `seminormalRep21`.  Proving the braid relation for arbitrary `λ` (the Yang–Baxter / axial-
  --   distance identity across three consecutive entries) is Hoefsmit's theorem and is not yet
  --   formalised here.  This is bean SW-4's residual; irreducibility (the `∃ i, non-scalar` witness
  --   in full strength) is bean SW-5.
  sorry

end QOU.SchurWeyl
