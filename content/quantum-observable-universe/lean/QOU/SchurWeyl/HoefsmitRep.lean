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

* **The generic axial-distance seminormal block — sorry-free, generic field.**  `seminormalBlock q a`
  is the `2×2` building block of *every* size-`2` SYT-orbit of the general construction (top-right
  `1`, trace `q - q⁻¹`, determinant `-1`, one free parameter `a`).  `seminormalBlock_quadratic` proves
  its Hecke quadratic relation for all `q ≠ 0` and all `a`; `seminormalBlock_ne_scalar` proves its
  non-degeneracy (off-diagonal `1 ≠ 0`); `S1_eq_seminormalBlock` recovers the concrete `(2,1)` matrix
  as `seminormalBlock q (-1/(q³+q))`.

* **The `λ = (2,2)`, `d_λ = 2`, `N = 4` seminormal representation — sorry-free over `ℝ`.**
  `seminormalRep22 : Hecke ℝ q q⁻¹ 3 →ₐ[ℝ] M_2(ℝ)`, generators `![S0, S1, S0]`.  The program's first
  4-strand rep and its first **non-vacuous far-commutation** (`σ_0 σ_2 = σ_2 σ_0`); every relation
  reduces to the `(2,1)` lemmas.  `seminormalRep22_nonScalar` is a concrete witness of the general
  non-degeneracy statement.

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

/-- **Axial distance is antisymmetric.**  Exchanging the two cells negates it — which is
what makes a seminormal pair carry the two parameters `a(d)` and `a(-d)`. -/
theorem axialDistance_antisymm (c d : ℕ × ℕ) :
    axialDistance c d = -axialDistance d c := by
  simp only [axialDistance]; ring

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

/-! ## The generic axial-distance seminormal block (sorry-free, generic field)

Every size-`2` orbit block of the general Hoefsmit matrices has one shape: a `2×2` matrix with
top-right entry `1`, trace `q - q⁻¹`, and determinant `-1` — hence spectrum `{q, -q⁻¹}` — carrying a
**single** free parameter, its top-left entry `a` (an axial-distance rational function of `q`), the
other two entries being forced by the trace and the determinant.  This is the reusable building block
from which every generator matrix `ρ_λ(σ_i)` of the general seminormal representation is assembled
block-diagonally over the `s_i`-orbits of `SYT λ`.  We isolate it here and prove its quadratic
relation once and for all, for **every** `q ≠ 0` and **every** parameter `a`, over a generic field
(§7c: no archimedean order is used).  The concrete `(2,1)` matrix `S1` is recovered as
`seminormalBlock q (-1/(q³+q))` (see `S1_eq_seminormalBlock`). -/

section SeminormalBlock

variable {K : Type*} [Field K] (q a : K)

/-- The **generic axial-distance seminormal block** `B(a)`: the unique `2×2` matrix with top-right
entry `1`, trace `q - q⁻¹`, and determinant `-1`, parametrised by its top-left entry `a`.  The
bottom-left entry `a·(q - q⁻¹) - a² + 1` and bottom-right entry `(q - q⁻¹) - a` are forced by the
trace and determinant.  Every size-`2` orbit block of the general Hoefsmit matrices is of this form
(with `a` an axial-distance function of `q`). -/
noncomputable def seminormalBlock : Matrix (Fin 2) (Fin 2) K :=
  !![a, 1; a * (q - q⁻¹) - a ^ 2 + 1, (q - q⁻¹) - a]

/-- **Quadratic relation for the generic block (sorry-free, every `q ≠ 0`, every `a`):**
`B(a)² = (q - q⁻¹)·B(a) + (q·q⁻¹)·1`.  Because the block's trace is `q - q⁻¹` and its determinant is
`-1` identically, Cayley–Hamilton gives `B(a)² = (q - q⁻¹)·B(a) + 1`; `q ≠ 0` is used only to
identify the constant `1 = q·q⁻¹` matching the Hecke normalisation `qi := q⁻¹`. -/
theorem seminormalBlock_quadratic (hq : q ≠ 0) :
    seminormalBlock q a * seminormalBlock q a
      = (q - q⁻¹) • seminormalBlock q a + (q * q⁻¹) • (1 : Matrix (Fin 2) (Fin 2) K) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [seminormalBlock, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- **The generic block is non-scalar (sorry-free):** `B(a) ≠ s·1` for every scalar `s`, because its
top-right entry is `1 ≠ 0` while every scalar matrix `s·1` has off-diagonal entries `0`.  This is the
crux of the non-degeneracy that distinguishes the seminormal representation from the trivial `q·1`
rep, isolated for the `2×2` building block. -/
theorem seminormalBlock_ne_scalar (s : K) :
    seminormalBlock q a ≠ s • (1 : Matrix (Fin 2) (Fin 2) K) := by
  intro h
  have h01 := congrFun (congrFun h 0) 1
  simp [seminormalBlock, Matrix.smul_apply] at h01

end SeminormalBlock

/-- The concrete `(2,1)` seminormal matrix `S1` is exactly the generic block at `a = -1/(q³+q)`
(sorry-free), tying the hand-verified `2×2` case to the general building block. -/
theorem S1_eq_seminormalBlock (q : ℝ) (hq : q ≠ 0) :
    S1 q = seminormalBlock q (-1 / (q ^ 3 + q)) := by
  have h1 : (q ^ 2 + 1) ≠ 0 := sq_add_one_ne q
  have h2 : (q ^ 3 + q) ≠ 0 := cube_add_ne q hq
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [S1, seminormalBlock] <;> field_simp <;> ring

/-- `S1` is non-scalar (sorry-free): its top-right entry is `1 ≠ 0`.  Follows from
`seminormalBlock_ne_scalar` via `S1_eq_seminormalBlock`. -/
theorem S1_ne_scalar (q : ℝ) (hq : q ≠ 0) (s : ℝ) :
    S1 q ≠ s • (1 : Matrix (Fin 2) (Fin 2) ℝ) := by
  rw [S1_eq_seminormalBlock q hq]
  exact seminormalBlock_ne_scalar q _ s

/-! ## The shape `λ = (2,2)`, `d_λ = 2` seminormal representation over `ℝ` (sorry-free)

`Hecke ℝ q q⁻¹ 3` is `H_4(q)` (three generators `σ_0, σ_1, σ_2`, two braid relations and **one
non-vacuous far-commutation** `σ_0 σ_2 = σ_2 σ_0`).  Its `2`-dimensional irreducible — the shape
`(2,2)` Specht module, with the two SYT `[[1,2],[3,4]]`, `[[1,3],[2,4]]` — is afforded by

* `σ_0 ↦ S0 = diag(q, -q⁻¹)` — entries `1,2` share a row in the first SYT (eigenvalue `q`), a column
  in the second (eigenvalue `-q⁻¹`);
* `σ_1 ↦ S1` — the axial-distance block (the same content difference `2` as the `(2,1)` case) that
  swaps the two SYT;
* `σ_2 ↦ S0 = diag(q, -q⁻¹)` — entries `3,4` share a row in the first SYT, a column in the second.

Every relation reduces to the already-proved `(2,1)` lemmas: both braid relations are `S0_S1_braid`
(one directly, one by symmetry), the two quadratics are `S0_quadratic` / `S1_quadratic`, and the
far-commutation `σ_0 σ_2 = σ_2 σ_0` is `S0 · S0 = S0 · S0` (`rfl`).  This is the program's first
4-strand seminormal representation and its first non-vacuous far-commutation verification. -/

section Seminormal22

variable (q : ℝ)

/-- **The shape `(2,2)` seminormal representation** `ρ_{(2,2)} : H_4(q) →ₐ[ℝ] M_2(ℝ)`, generators
`![S0, S1, S0]`.  Sorry-free for all `q ≠ 0`. -/
noncomputable def seminormalRep22 (hq : q ≠ 0) :
    Hecke ℝ q q⁻¹ 3 →ₐ[ℝ] Matrix (Fin 2) (Fin 2) ℝ :=
  Hecke.lift ℝ q q⁻¹ 3 ![S0 q, S1 q, S0 q]
    (by
      intro i
      fin_cases i
      · show S0 q * S0 q = (q - q⁻¹) • S0 q + (q * q⁻¹) • 1
        exact S0_quadratic q
      · show S1 q * S1 q = (q - q⁻¹) • S1 q + (q * q⁻¹) • 1
        exact S1_quadratic q hq
      · show S0 q * S0 q = (q - q⁻¹) • S0 q + (q * q⁻¹) • 1
        exact S0_quadratic q)
    (by
      intro i hi
      fin_cases i
      · show S0 q * S1 q * S0 q = S1 q * S0 q * S1 q
        exact S0_S1_braid q hq
      · show S1 q * S0 q * S1 q = S0 q * S1 q * S0 q
        exact (S0_S1_braid q hq).symm
      · exact absurd hi (by decide))
    (by
      intro i j h
      fin_cases i <;> fin_cases j <;>
        first
          | (exfalso; revert h; decide)
          | rfl)

/-- `ρ_{(2,2)} (σ_0) = S0`. -/
@[simp] theorem seminormalRep22_σ0 (hq : q ≠ 0) :
    seminormalRep22 q hq (Hecke.σ ℝ q q⁻¹ 3 0) = S0 q := by
  simp [seminormalRep22, Hecke.lift_σ]

/-- `ρ_{(2,2)} (σ_1) = S1`. -/
@[simp] theorem seminormalRep22_σ1 (hq : q ≠ 0) :
    seminormalRep22 q hq (Hecke.σ ℝ q q⁻¹ 3 1) = S1 q := by
  simp [seminormalRep22, Hecke.lift_σ]

/-- `ρ_{(2,2)} (σ_2) = S0`. -/
@[simp] theorem seminormalRep22_σ2 (hq : q ≠ 0) :
    seminormalRep22 q hq (Hecke.σ ℝ q q⁻¹ 3 2) = S0 q := by
  simp [seminormalRep22, Hecke.lift_σ]

/-- **`ρ_{(2,2)}` is non-scalar (sorry-free):** the generator `σ_1` is sent to `S1`, whose top-right
entry is `1 ≠ 0`, so it is not `s·1` for any scalar `s`.  This is the concrete `(2,2)` witness of the
non-degeneracy asserted in general by `hoefsmit_seminormal_rep`. -/
theorem seminormalRep22_nonScalar (hq : q ≠ 0) :
    ∃ i : Fin 3, ∀ s : ℝ,
      seminormalRep22 q hq (Hecke.σ ℝ q q⁻¹ 3 i) ≠ s • (1 : Matrix (Fin 2) (Fin 2) ℝ) := by
  refine ⟨1, fun s => ?_⟩
  rw [seminormalRep22_σ1 q hq]
  exact S1_ne_scalar q hq s

end Seminormal22

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
`rhoSign`); the smallest genuinely-`2×2` case `λ = (2,1)` (`N = 3`) is `seminormalRep21`; and the
first 4-strand case `λ = (2,2)` (`N = 4`, `d_λ = 2`, non-vacuous far-commutation) is
`seminormalRep22`, with `seminormalRep22_nonScalar` a concrete witness of the non-degeneracy
conclusion below.  The `2×2` building block of the general matrices — with its quadratic relation and
non-scalarity — is `seminormalBlock` / `seminormalBlock_quadratic` / `seminormalBlock_ne_scalar`.

**What is now scaffolded sorry-free (see above):** the reusable size-`2` orbit block and its
quadratic + non-scalarity, and two fully-worked instances (`(2,1)`, `(2,2)`) exercising the braid and
far-commutation relations.  **What remains for the general `∀ λ` statement** is: (i) enumerate the
`s_i`-orbits of `SYT λ` (each of size `1` — scalar `q` / `-q⁻¹` — or `2` — a `seminormalBlock`);
(ii) assemble the block-diagonal generator matrices from those orbits; (iii) prove the **braid
relation for arbitrary `λ`** — the Yang–Baxter / axial-distance identity across the `S₃`-orbit of
three consecutive entries `i, i+1, i+2`, whose generic (size-`6`) case is a genuine `6`-dimensional
identity, not reducible to the `2×2` blocks above.  Step (iii) is Hoefsmit's thesis theorem and is
not yet formalised.  Tracked as bean `qou-im9l` (SW-4-gen) and its child GAP bean; irreducibility (the
`∃ i, non-scalar` witness in full strength) is bean SW-5. -/
theorem hoefsmit_seminormal_rep {N : ℕ} (q : ℝ) (hq : q ≠ 0) (lam : Partition N) :
    ∃ ρ : Hecke ℝ q q⁻¹ (N - 1) →ₐ[ℝ] Matrix (Fin (dLambda lam)) (Fin (dLambda lam)) ℝ,
      2 ≤ dLambda lam →
        ∃ i : Fin (N - 1), ∀ s : ℝ,
          ρ (Hecke.σ ℝ q q⁻¹ (N - 1) i) ≠ s • (1 : Matrix (Fin (dLambda lam)) (Fin (dLambda lam)) ℝ) := by
  -- Ref: [hoefsmit1974] (PhD thesis, UBC 1974 — the seminormal form); [ram1997] axial-distance
  --   formulas.  Both keys resolve in `content/schema/references.ts`.
  -- GAP (bean qou-im9l / SW-4-gen residual): the general seminormal construction indexes a basis by
  --   `SYT lam` and, for each generator `σ_i`, forms the block-diagonal matrix over the `s_i`-orbits
  --   of SYT — size-1 orbits scalar (`q` or `-q⁻¹`), size-2 orbits a `seminormalBlock` (proved
  --   quadratic + non-scalar above).  The residual is the BRAID relation for arbitrary `λ`: the
  --   Yang–Baxter / axial-distance identity across the S₃-orbit of `i, i+1, i+2`, whose generic
  --   size-6 case is a genuine 6-dim identity (the size-1/2 cases reduce to `S0_S1_braid`, as in
  --   `seminormalRep22`).  This is Hoefsmit's thesis theorem; not yet formalised.  Irreducibility in
  --   full strength is bean SW-5.
  sorry

end QOU.SchurWeyl
