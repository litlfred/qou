import Mathlib.Tactic

/-!
# QOU.Eightfold.Sym2GateParity — the `Sym²` gate is decided by PARITY, not self-duality

Companion to `QOU.Eightfold.Sym2Gate`, and the formal record of a correction.

## What this file is for

The `Sym²` gate is the requirement that `Sym²(W)` contain no singlet — the
condition an `SU(3)`-triplet candidate `W` must satisfy, since `Sym²(𝟑) = 𝟔` is
irreducible precisely because `𝟑̄ ≠ 𝟑`.

The compute probe `computations/state_space_natural_three_sym2_gate.py`
originally argued: *every `SU(2)` representation is self-dual, therefore no
summand of any `V^⊗n` can pass the gate.*  **That inference is invalid.**
Self-duality splits by the Frobenius–Schur indicator:

| dim `d = 2j+1` | spin | FS | invariant form | singlet lives in | gate |
|---|---|---|---|---|---|
| odd | integer | `+1` | symmetric (orthogonal) | `Sym²` | **fails** |
| even | half-integer | `−1` | antisymmetric (symplectic) | `Λ²` | **passes** |

so the 2-dimensional fundamental — self-dual, but *symplectically* — **passes**
the gate.  This file formalises the criterion that actually decides it.

## The combinatorial content

Clebsch–Gordan gives `V_j ⊗ V_j = ⨁_{k=0}^{2j} V_k`, and the summands split
between `Sym²` and `Λ²` by the parity of `2j − k`: `Sym²(V_j)` collects exactly
those `k ≤ 2j` with `k ≡ 2j (mod 2)`.  The gate therefore fails precisely when
the singlet index `k = 0` survives that filter, i.e. precisely when `2j` is
even, i.e. precisely when `d = 2j + 1` is **odd**.

Everything below is stated over `2j` (`twoJ`) rather than `d` to keep the
arithmetic subtraction-free.

## Why the correction leaves the physics conclusion intact

Colour needs `dim W = 3`, which is odd, hence orthogonal, hence fails the gate
(`adjoint_fails_gate`).  So a triplet still cannot be found among the summands
of `V^⊗n` for a 2-dimensional fibre, and the downstream collapse argument in
`docs/audits/2026-08-07-eightfold-live-surface-collapse.md` stands.  What was
wrong was only the stated *generality* — even-dimensional summands do pass, and
they are simply the wrong dimension.

`self_duality_does_not_decide_gate` records the counterexample pair formally, so
the invalid inference cannot be re-derived from this file.

-- Ref: [fulton-harris1991] §11 (Clebsch–Gordan for `sl₂`); Frobenius–Schur
-- indicator `(-1)^{2j}` for the spin-`j` irrep of `SU(2)`.
-/

namespace QOU.Eightfold.Sym2GateParity

open Finset

/-- Indices `k` of the `SU(2)` irreps `V_k` occurring in `Sym²(V_j)`, where
`twoJ = 2j`.  Clebsch–Gordan supplies `k ≤ 2j`; the symmetric square keeps
exactly those `k` congruent to `2j` mod 2. -/
def sym2Indices (twoJ : ℕ) : Finset ℕ :=
  (range (twoJ + 1)).filter (fun k => k % 2 = twoJ % 2)

/-- The dimension of the irrep `V_j` with `2j = twoJ`. -/
def dimOf (twoJ : ℕ) : ℕ := twoJ + 1

/-- **The gate criterion.** The singlet index `0` survives into `Sym²(V_j)`
exactly when `2j` is even. -/
theorem zero_mem_sym2Indices_iff (twoJ : ℕ) :
    0 ∈ sym2Indices twoJ ↔ Even twoJ := by
  unfold sym2Indices
  rw [mem_filter, mem_range]
  constructor
  · rintro ⟨-, h⟩
    rw [Nat.even_iff]
    omega
  · intro h
    rw [Nat.even_iff] at h
    exact ⟨Nat.succ_pos _, by omega⟩

/-- **Restated in terms of the dimension.** The gate fails exactly for
odd-dimensional irreps. -/
theorem gate_fails_iff_odd_dim (twoJ : ℕ) :
    0 ∈ sym2Indices twoJ ↔ Odd (dimOf twoJ) := by
  rw [zero_mem_sym2Indices_iff, dimOf, Nat.odd_add_one, Nat.not_odd_iff_even]

/-- The 2-dimensional fundamental (`2j = 1`, spin `1/2`) **passes** the gate:
its singlet sits in `Λ²`, not `Sym²`.  This is the counterexample to the
superseded self-duality argument. -/
theorem fundamental_passes_gate : 0 ∉ sym2Indices 1 := by decide

/-- The 3-dimensional adjoint (`2j = 2`, spin `1`) **fails** the gate — the case
the colour question actually needs. -/
theorem adjoint_fails_gate : 0 ∈ sym2Indices 2 := by decide

/-- **Self-duality does not decide the gate.**  Both irreps below are self-dual
(every `SU(2)` representation is), yet one passes and one fails.  Formal record
of the corrected inference: no predicate that holds of *all* `SU(2)` irreps can
imply gate-failure. -/
theorem self_duality_does_not_decide_gate :
    (0 ∉ sym2Indices 1) ∧ (0 ∈ sym2Indices 2) :=
  ⟨fundamental_passes_gate, adjoint_fails_gate⟩

/-- Dimension bookkeeping at `2j = 1`: `Sym²` of the 2-dimensional fundamental
has dimension `3 = 2·3/2`, and the surviving index is `k = 1` (the spin-1
triplet), with the singlet absent. -/
theorem sym2_dim_twoJ_one : (sym2Indices 1).sum (fun k => 2 * k + 1) = 3 := by decide

/-- Dimension bookkeeping at `2j = 2`: `Sym²` of the 3-dimensional adjoint has
dimension `6 = 3·4/2`, decomposing as `5 + 1` — the singlet is present, which is
the gate failure. -/
theorem sym2_dim_twoJ_two : (sym2Indices 2).sum (fun k => 2 * k + 1) = 6 := by decide

/-- The top spin `2j` always survives in `Sym²(V_j)` (`V_{2j}` is the highest-weight
Clebsch–Gordan summand of `V_j ⊗ V_j`, which is symmetric). -/
theorem twoJ_mem_sym2Indices (twoJ : ℕ) : twoJ ∈ sym2Indices twoJ := by
  unfold sym2Indices
  rw [mem_filter, mem_range]
  exact ⟨Nat.lt_succ_self twoJ, rfl⟩

/-- Every surviving spin index `k ∈ sym2Indices twoJ` differs from `twoJ` by an
even integer (`Even (twoJ - k)`). -/
theorem even_sub_of_mem_sym2Indices {twoJ k : ℕ} (hk : k ∈ sym2Indices twoJ) :
    Even (twoJ - k) := by
  unfold sym2Indices at hk
  rw [mem_filter, mem_range] at hk
  rcases hk with ⟨hlt, hmod⟩
  rw [Nat.even_iff]
  omega

/-- Twice the group order times the singlet multiplicity `⟨χ_{Sym²(V)}, 1⟩` for a
finite-group character over `n` conjugacy classes with class sizes `classSize`
and character sums `sym2CharSum i = χ(g_i)² + χ(g_i²)`. -/
def twoGroupOrderMulSym2Singlet (n : ℕ) (classSize : Fin n → ℕ)
    (sym2CharSum : Fin n → ℤ) : ℤ :=
  ∑ i : Fin n, (classSize i : ℤ) * sym2CharSum i

/-- Concrete conjugacy class sizes of the icosahedral group `A₅` (`|A₅| = 60`):
`1` (identity), `15` (double transpositions), `20` (3-cycles), and `12, 12`
(the two 5-cycle conjugacy classes). -/
def icosahedralClassSize : Fin 5 → ℕ := ![1, 15, 20, 12, 12]

/-- On the 3-dimensional icosahedral representation `T₁` of `A₅`, the quantity
`χ(g)² + χ(g²)` on the five conjugacy classes takes the integer values
`![3² + 3, (-1)² + 3, 0² + 0, 2, 2] = ![12, 4, 0, 2, 2]` (since on the two
5-cycle classes `(φ² - φ⁻¹) + (φ⁻² - φ) = (φ + φ⁻¹)² - 2 - (φ + φ⁻¹) = 1 - (-1) = 2`,
or class-averaged `2` per 12-element class). -/
def icosahedralT1Sym2CharSum : Fin 5 → ℤ := ![12, 4, 0, 2, 2]

/-- **Icosahedral `T₁` fails the `Sym²` gate (character inner product proof).**
The class-weighted sum `∑ |C_i| (χ(g_i)² + χ(g_i²))` equals `120 = 2 · |A₅| · 1`,
proving `⟨χ_{Sym²(T₁)}, 1⟩ = 1` (`Sym²(T₁) ≅ 1 ⊕ 5` contains a singlet). -/
theorem icosahedral_T1_sym2_singlet_inner_product :
    twoGroupOrderMulSym2Singlet 5 icosahedralClassSize icosahedralT1Sym2CharSum
      = 2 * (∑ i : Fin 5, (icosahedralClassSize i : ℤ)) * 1 := by
  decide

end QOU.Eightfold.Sym2GateParity
