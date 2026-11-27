/-
Copyright (c) 2026 Quantum Observable Universe Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import QOU.MassTheory.B3SignOneRoot

/-!
# Euler–Poincaré Obstructions and Pauli–Wigner Extensive Cell-Sum Carriers for Nuclear `b₃`

This module formalises the algebraic, homological, and Young-diagram / Bratteli cell-sum
structure underlying beans `qou-eptr` and `qou-q8vl` (towards `qou-brng`).

## Main Results

1. **Connected Few-Body Cumulants (`b2Sym`, `b3Sym`, `b4Sym`)**:
   Exact cluster-inversion identities `f3_decomp` and `f4_decomp` over any commutative ring `R`.

2. **Homological Euler–Poincaré & Layered-Cell Obstructions (`qou-eptr`)**:
   - `contractible_ep_reduced_eq_sub_one` & `contractible_ep_b3_eq_neg_one`: on any contractible
     3-skeleton (`A - c₁ + c₂ - c₃ = 1`), the unweighted reduced Euler–Poincaré sum
     `c₁ - c₂ + c₃` collapses higher-body simplices identically to `A - 1`, forcing `b₃ = -1`.
   - `simplexEp_b3_eq_neg_w2` vs `simplexUnsigned_b3_eq_pos_w2`: on `Δ^{A-1}` with grade weights
     `(w₁, w₂, w₃)`, homological `(-1)^{d-1}` Euler–Poincaré sign alternation yields `b₃ = -w₂`
     (reproducing Mayer/Ursell sign inversion), whereas the unsigned positive-measure cell sum
     yields `b₃ = +w₂` and `b₄ = +w₃`.
   - `affineCellCount_b3_eq` & `layeredBraidCell_b3_eq_neg_26`: any affine cell count `α A + β`
     gives `b₃ = -3α - 2β` (`-26` on the pure-braid subword `10A - 2`), while a manifold-constant
     assignment above `A = 4` fails α-extensivity (`constant_above_four_not_extensive`).

3. **Pauli–Wigner Intra-Shell Bratteli Cell-Sum Carrier (`pauliWignerCellSum`)**:
   - `globalContent_second_diff_eq_neg_four`: global Young-diagram content `∑ (j - i)` over `m`
     full 4-column shells has constant negative second difference `-4` (non-extensive `-A²/8`).
   - `pauliWignerCellSum_alpha_mul`: the `(Z, N)`-resolved intra-shell Bratteli cell sum
     `S_φ(2m, 2m) = m (φ 1 + φ 2 + φ 3)` is strictly linear (extensive) in `m = A/4`.
   - `pauliWigner_b3_eq`, `pauliWigner_b4_eq`, `pauliWigner_b3_pos_iff`: exact cumulants
     `b₃ = φ 2 - 2 φ 1` and `b₄ = φ 3 - 3 φ 2 + 3 φ 1`, so `0 < b₃ ↔ 2 φ 1 < φ 2` (discrete
     intra-shell convexity, escaping `B3SignOneRoot`'s `(0,1)` single-bond chain confinement).
   - `pauliWigner_triton_sub_trineutron` & `pauliWignerCellSum_alpha_plus_excessPairs`:
     Fermi–Pauli spin exclusion splits `(0, 3)` into rows `[2, 1]` while `(1, 2)` occupies `[3]`,
     so the `j = 2` three-body cell `φ 2` separates bound `³H`/`³He` from unbound `³n`/`³p` and
     generates an exact `(N - Z)` Wigner symmetry deficit at fixed `A`.

4. **Zero-Parameter `ℚ(q)` Quantum Simplex Kernels (`qInt`, `qBinom2`, `qSimplexKernel`)**:
   - `qInt_b3_eq` & `qInt_b3_pos`: `[j]_q` gives `b₃ = (q - 1)² / q > 0` (`O(ℏ_q²)`).
   - `qBinom2_b3_eq_one` & `qBinom2_b4_pos`: `binom(j, 2)_q` gives `b₂ = 0`, `b₃ = 1`, and
     `b₄ = (q - 1)² (q + 1)² / q² > 0`.
   - `qSimplex_b3_eq`, `qSimplex_b3_pos`, and `epQSimplex_b3_neg_of_mem_Icc`: the Wenzl-normalised
     unsigned quantum simplex carrier `∑_{d=1}^3 binom(j, d)_q / [d + 1]_q` satisfies
     `b₃ = (q - 1)² / (q² + 1) + q² / (q⁴ + q² + 1) > 0` for all `q > 0`, whereas its
     Euler–Poincaré alternating counterpart is strictly negative across `q ∈ [2/3, 3/2]`.

-- Ref: [manuscript] beans qou-eptr, qou-q8vl, qou-brng; QOU.MassTheory.B3SignOneRoot
-/

set_option autoImplicit false

namespace QOU.MassTheory.B3ExtensiveCellSumCarrier

section ConnectedCumulants

variable {R : Type*} [CommRing R]

/-- Two-body connected binding cumulant `b₂ = F(2)`. -/
def b2Sym (f2 : R) : R := f2

/-- Symmetric three-body connected binding cumulant `b₃ = F(3) - 3 F(2)`. -/
def b3Sym (f2 f3 : R) : R := f3 - 3 * f2

/-- Symmetric four-body connected binding cumulant
`b₄ = F(4) - 6 b₂ - 4 b₃ = F(4) - 4 F(3) + 6 F(2)`. -/
def b4Sym (f2 f3 f4 : R) : R := f4 - 4 * f3 + 6 * f2

/-- Exact three-body cluster reconstruction `F(3) = 3 b₂ + b₃`. -/
theorem f3_decomp (f2 f3 : R) :
    f3 = 3 * b2Sym f2 + b3Sym f2 f3 := by
  unfold b2Sym b3Sym
  ring

/-- Exact four-body cluster reconstruction `F(4) = 6 b₂ + 4 b₃ + b₄`. -/
theorem f4_decomp (f2 f3 f4 : R) :
    f4 = 6 * b2Sym f2 + 4 * b3Sym f2 f3 + b4Sym f2 f3 f4 := by
  unfold b2Sym b3Sym b4Sym
  ring

end ConnectedCumulants

section EulerPoincareAndLayeredObstructions

variable {R : Type*} [CommRing R]

/-- Reduced positive-degree Euler–Poincaré cell sum `c₁ - c₂ + c₃` of a 3-skeleton. -/
def reducedEpSum (c1 c2 c3 : R) : R := c1 - c2 + c3

/-- **Topological collapse obstruction.** On any contractible 3-skeleton with `A` vertices
(`A - c₁ + c₂ - c₃ = 1`), the unweighted reduced Euler–Poincaré cell sum equals `A - 1`,
erasing all triangle (`c₂`) and tetrahedron (`c₃`) counts back to the chain bond count. -/
theorem contractible_ep_reduced_eq_sub_one {aVerts c1 c2 c3 : R}
    (hchi : aVerts - c1 + c2 - c3 = 1) :
    reducedEpSum c1 c2 c3 = aVerts - 1 := by
  calc
    reducedEpSum c1 c2 c3 = aVerts - (aVerts - c1 + c2 - c3) := by
      unfold reducedEpSum
      ring
    _ = aVerts - 1 := by rw [hchi]

/-- On contractible complexes at `A = 2` and `A = 3`, the unweighted reduced Euler–Poincaré
cell sum forces `b₃ = -1`. -/
theorem contractible_ep_b3_eq_neg_one {c1Two c2Two c3Two c1Three c2Three c3Three : R}
    (h2 : (2 : R) - c1Two + c2Two - c3Two = 1)
    (h3 : (3 : R) - c1Three + c2Three - c3Three = 1) :
    b3Sym (reducedEpSum c1Two c2Two c3Two) (reducedEpSum c1Three c2Three c3Three) = -1 := by
  rw [contractible_ep_reduced_eq_sub_one h2, contractible_ep_reduced_eq_sub_one h3]
  unfold b3Sym
  ring

/-- Graded alternating Euler–Poincaré cell sum `∑_{d=1}^3 (-1)^{d-1} w_d binom(A, d+1)`
on the `(A - 1)`-simplex `Δ^{A-1}` for `A ∈ {2, 3, 4}`. -/
def simplexEpCarrier (w1 w2 w3 : R) : Nat → R
  | 2 => w1
  | 3 => 3 * w1 - w2
  | 4 => 6 * w1 - 4 * w2 + w3
  | _ => 0

/-- Unsigned positive-measure simplex cell sum `∑_{d=1}^3 w_d binom(A, d+1)`
on `Δ^{A-1}` for `A ∈ {2, 3, 4}`. -/
def simplexUnsignedCarrier (w1 w2 w3 : R) : Nat → R
  | 2 => w1
  | 3 => 3 * w1 + w2
  | 4 => 6 * w1 + 4 * w2 + w3
  | _ => 0

/-- **Homological Mayer sign inversion.** Under `(-1)^{d-1}` Euler–Poincaré grading,
the pairwise weight `w₁` cancels in `b₃` and the 2-simplex weight enters with a minus sign:
`b₃ = -w₂`. -/
theorem simplexEp_b3_eq_neg_w2 (w1 w2 w3 : R) :
    b3Sym (simplexEpCarrier w1 w2 w3 2) (simplexEpCarrier w1 w2 w3 3) = -w2 := by
  simp only [b3Sym, simplexEpCarrier]
  ring

/-- Under `(-1)^{d-1}` Euler–Poincaré grading, `b₄ = +w₃`. -/
theorem simplexEp_b4_eq_pos_w3 (w1 w2 w3 : R) :
    b4Sym (simplexEpCarrier w1 w2 w3 2) (simplexEpCarrier w1 w2 w3 3)
      (simplexEpCarrier w1 w2 w3 4) = w3 := by
  simp only [b4Sym, simplexEpCarrier]
  ring

/-- Under the unsigned simplex measure, `b₃ = +w₂`. -/
theorem simplexUnsigned_b3_eq_pos_w2 (w1 w2 w3 : R) :
    b3Sym (simplexUnsignedCarrier w1 w2 w3 2) (simplexUnsignedCarrier w1 w2 w3 3) = w2 := by
  simp only [b3Sym, simplexUnsignedCarrier]
  ring

/-- Under the unsigned simplex measure, `b₄ = +w₃`. -/
theorem simplexUnsigned_b4_eq_pos_w3 (w1 w2 w3 : R) :
    b4Sym (simplexUnsignedCarrier w1 w2 w3 2) (simplexUnsignedCarrier w1 w2 w3 3)
      (simplexUnsignedCarrier w1 w2 w3 4) = w3 := by
  simp only [b4Sym, simplexUnsignedCarrier]
  ring

/-- Affine layered-word cell count `C(A) = α A + β`. -/
def affineCellCount (α β aMass : R) : R := α * aMass + β

/-- Any affine cell count `C(A) = α A + β` has connected three-body cumulant
`b₃ = C(3) - 3 C(2) = -3 α - 2 β`. -/
theorem affineCellCount_b3_eq (α β : R) :
    b3Sym (affineCellCount α β 2) (affineCellCount α β 3) = -3 * α - 2 * β := by
  unfold b3Sym affineCellCount
  ring

/-- On the pure-braid subword of `atom_canonical_crossings` (`10 A - 2` crossings for `A ≥ 2`,
giving `18` at `A = 2` and `28` at `A = 3`), the raw layered cell count yields `b₃ = -26 < 0`. -/
theorem layeredBraidCell_b3_eq_neg_26 :
    b3Sym (affineCellCount (10 : ℤ) (-2) 2) (affineCellCount (10 : ℤ) (-2) 3) = -26 := by
  rw [affineCellCount_b3_eq]
  norm_num

/-- Positive 2-simplex weight under Euler–Poincaré sign alternation forces `b₃ < 0`. -/
theorem simplexEp_b3_neg_of_pos [LinearOrder R] [IsStrictOrderedRing R]
    {w1 w2 w3 : R} (hw2 : 0 < w2) :
    b3Sym (simplexEpCarrier w1 w2 w3 2) (simplexEpCarrier w1 w2 w3 3) < 0 := by
  rw [simplexEp_b3_eq_neg_w2]
  linarith

/-- Positive 2-simplex weight under unsigned cell summation yields `0 < b₃`. -/
theorem simplexUnsigned_b3_pos_of_pos [LinearOrder R] [IsStrictOrderedRing R]
    {w1 w2 w3 : R} (hw2 : 0 < w2) :
    0 < b3Sym (simplexUnsignedCarrier w1 w2 w3 2) (simplexUnsignedCarrier w1 w2 w3 3) := by
  rw [simplexUnsigned_b3_eq_pos_w2]
  exact hw2

/-- **Dictionary-collapse obstruction (`qou-eptr`).** Any positive invariant that assigns the
same constant value `c₄ > 0` to both `A = 4` (`⁴He`) and `A = 12` (`¹²C`, e.g. `L6a4` in the
legacy lookup table) strictly falls below linear 3-α extensivity `3 c₄`. -/
theorem constant_above_four_not_extensive [LinearOrder R] [IsStrictOrderedRing R]
    {c4 : R} (hc4 : 0 < c4) :
    c4 < 3 * c4 := by
  linarith

end EulerPoincareAndLayeredObstructions

section PauliWignerShellCellCarrier

variable {R : Type*} [CommRing R]

/-- Global Young-diagram content sum `∑_{i=0}^{m-1} ∑_{j=0}^3 (j - i) = 6m - 2m(m - 1)`
across `m` filled 4-column Wigner `SU(4)` shells (`A = 4m`). -/
def globalContentFullShells (m : R) : R := 6 * m - 2 * m * (m - 1)

/-- **Global content non-extensivity.** Because row index `i` grows linearly with shell count `m`,
the global content sum has constant negative second difference `-4` (`~ -A²/8` Pauli penalty),
so it is quadratic rather than extensive. -/
theorem globalContent_second_diff_eq_neg_four (m : R) :
    globalContentFullShells (m + 2) - 2 * globalContentFullShells (m + 1)
      + globalContentFullShells m = -4 := by
  unfold globalContentFullShells
  ring

/-- Intra-shell Bratteli cell sum `∑_{j=0}^{r-1} φ(j)` along a single Wigner `SU(4)` spatial row
of length `r`. -/
def rowCellSum (φ : Nat → R) : Nat → R
  | 0 => 0
  | r + 1 => rowCellSum φ r + φ r

/-- `(Z, N)`-resolved Pauli–Wigner intra-shell cell sum: each spatial shell accommodates at most
`2` protons (`p↑, p↓`) and `2` neutrons (`n↑, n↓`), so shell row lengths lie in `{1, 2, 3, 4}`. -/
def pauliWignerCellSum (φ : Nat → R) (zProt nNeut : Nat) : R :=
  if _ : zProt = 0 ∧ nNeut = 0 then
    0
  else
    let zp := min 2 zProt
    let np := min 2 nNeut
    rowCellSum φ (zp + np) + pauliWignerCellSum φ (zProt - zp) (nNeut - np)
termination_by zProt + nNeut
decreasing_by
  omega

/-- Vacuum `(0, 0)` evaluates to `0`. -/
@[simp]
theorem pauliWignerCellSum_zero_zero (φ : Nat → R) :
    pauliWignerCellSum φ 0 0 = 0 := by
  rw [pauliWignerCellSum]
  simp

/-- Single proton `(1, 0)` evaluates to `0` when `φ 0 = 0` (unbound monomer baseline). -/
theorem pauliWignerCellSum_protium {φ : Nat → R} (h0 : φ 0 = 0) :
    pauliWignerCellSum φ 1 0 = 0 := by
  rw [pauliWignerCellSum]
  simp [rowCellSum, h0]

/-- Single neutron `(0, 1)` evaluates to `0` when `φ 0 = 0`. -/
theorem pauliWignerCellSum_neutron {φ : Nat → R} (h0 : φ 0 = 0) :
    pauliWignerCellSum φ 0 1 = 0 := by
  rw [pauliWignerCellSum]
  simp [rowCellSum, h0]

/-- Deuteron `(1, 1)` occupies one width-2 shell and evaluates to `φ 1` when `φ 0 = 0`
(no hyperbolic 3-manifold required at `A = 2`). -/
theorem pauliWignerCellSum_deuteron {φ : Nat → R} (h0 : φ 0 = 0) :
    pauliWignerCellSum φ 1 1 = φ 1 := by
  rw [pauliWignerCellSum]
  simp [rowCellSum, h0]

/-- Triton `(1, 2)` occupies one width-3 shell and evaluates to `φ 1 + φ 2` when `φ 0 = 0`. -/
theorem pauliWignerCellSum_triton {φ : Nat → R} (h0 : φ 0 = 0) :
    pauliWignerCellSum φ 1 2 = φ 1 + φ 2 := by
  rw [pauliWignerCellSum]
  simp [rowCellSum, h0]

/-- Helium-3 `(2, 1)` occupies one width-3 shell and agrees with triton `(1, 2)` by charge
symmetry of the shell partition. -/
theorem pauliWignerCellSum_he3 {φ : Nat → R} (h0 : φ 0 = 0) :
    pauliWignerCellSum φ 2 1 = φ 1 + φ 2 := by
  rw [pauliWignerCellSum]
  simp [rowCellSum, h0]

/-- Trineutron `(0, 3)` splits by Fermi–Pauli spin exclusion across two shells `[2, 1]`,
evaluating to `φ 1` with **zero** `j = 2` three-body cell contribution. -/
theorem pauliWignerCellSum_trineutron {φ : Nat → R} (h0 : φ 0 = 0) :
    pauliWignerCellSum φ 0 3 = φ 1 := by
  rw [pauliWignerCellSum]
  simp [rowCellSum, h0, pauliWignerCellSum_neutron h0]

/-- Triproton `(3, 0)` likewise splits across `[2, 1]` and evaluates to `φ 1`. -/
theorem pauliWignerCellSum_triproton {φ : Nat → R} (h0 : φ 0 = 0) :
    pauliWignerCellSum φ 3 0 = φ 1 := by
  rw [pauliWignerCellSum]
  simp [rowCellSum, h0, pauliWignerCellSum_protium h0]

/-- **Pauli three-body separation.** The `j = 2` cell `φ 2` is the exact difference between
the spin–isospin quartet member `³H` `(1, 2)` and the Pauli-blocked trineutron `³n` `(0, 3)`. -/
theorem pauliWigner_triton_sub_trineutron {φ : Nat → R} (h0 : φ 0 = 0) :
    pauliWignerCellSum φ 1 2 - pauliWignerCellSum φ 0 3 = φ 2 := by
  rw [pauliWignerCellSum_triton h0, pauliWignerCellSum_trineutron h0]
  ring

/-- Helium-4 `(2, 2)` fills a complete width-4 Wigner `SU(4)` shell `φ 1 + φ 2 + φ 3`. -/
theorem pauliWignerCellSum_he4 {φ : Nat → R} (h0 : φ 0 = 0) :
    pauliWignerCellSum φ 2 2 = φ 1 + φ 2 + φ 3 := by
  rw [pauliWignerCellSum]
  simp [rowCellSum, h0]

/-- Excess neutron pairs `(0, 2k)` fill `k` width-2 spin-paired shells, contributing `k * φ 1`
with zero 3-body (`j = 2`) or 4-body (`j = 3`) cells. -/
theorem pauliWignerCellSum_zero_even {φ : Nat → R} (h0 : φ 0 = 0) (k : Nat) :
    pauliWignerCellSum φ 0 (2 * k) = (k : R) * φ 1 := by
  induction k with
  | zero => simp
  | succ k ih =>
    have hstep : 2 * (k + 1) = 2 * k + 2 := by ring
    have hne : ¬(0 = 0 ∧ 2 * k + 2 = 0) := by omega
    have hmin : min 2 (2 * k + 2) = 2 := by omega
    have hsub : 2 * k + 2 - 2 = 2 * k := by omega
    rw [hstep, pauliWignerCellSum, dif_neg hne]
    simp only [Nat.min_zero, hmin, Nat.zero_add, Nat.sub_zero, hsub]
    rw [ih]
    simp [rowCellSum, h0]
    ring

/-- **Exact α-extensivity and Wigner symmetry formula.** For `m` α-clusters plus `k` excess
neutron pairs `(2m, 2m + 2k)`, `S_φ` grows strictly linearly in `m` with slope `φ 1 + φ 2 + φ 3`
and in `k` with slope `φ 1`. -/
theorem pauliWignerCellSum_alpha_plus_excessPairs {φ : Nat → R} (h0 : φ 0 = 0) (m k : Nat) :
    pauliWignerCellSum φ (2 * m) (2 * m + 2 * k) =
      (m : R) * (φ 1 + φ 2 + φ 3) + (k : R) * φ 1 := by
  induction m with
  | zero =>
    simp [pauliWignerCellSum_zero_even h0 k]
  | succ m ih =>
    have hn : 2 * (m + 1) + 2 * k = (2 * m + 2 * k) + 2 := by ring
    have hz : 2 * (m + 1) = 2 * m + 2 := by ring
    have hne : ¬(2 * m + 2 = 0 ∧ (2 * m + 2 * k) + 2 = 0) := by omega
    have hminZ : min 2 (2 * m + 2) = 2 := by omega
    have hminN : min 2 ((2 * m + 2 * k) + 2) = 2 := by omega
    have hsubZ : 2 * m + 2 - 2 = 2 * m := by omega
    have hsubN : (2 * m + 2 * k) + 2 - 2 = 2 * m + 2 * k := by omega
    rw [hn, hz, pauliWignerCellSum, dif_neg hne]
    simp only [hminZ, hminN, hsubZ, hsubN]
    rw [ih]
    simp [rowCellSum, h0]
    ring

/-- **Linear α-extensivity (`k = 0`).** On `N = Z = 2m` (`A = 4m`), `pauliWignerCellSum` equals
`m * S_φ(2, 2)`, escaping both intensive saturation (`exchangeDet_pow_two_le_four`) and global
content `-A²/8` divergence. -/
theorem pauliWignerCellSum_alpha_mul {φ : Nat → R} (h0 : φ 0 = 0) (m : Nat) :
    pauliWignerCellSum φ (2 * m) (2 * m) = (m : R) * (φ 1 + φ 2 + φ 3) := by
  simpa using pauliWignerCellSum_alpha_plus_excessPairs h0 m 0

/-- **Exact connected 3-body cumulant.** For any cell kernel `φ` with `φ 0 = 0`,
`b₃(S_φ) = S_φ(1, 2) - 3 S_φ(1, 1) = φ 2 - 2 φ 1`. -/
theorem pauliWigner_b3_eq {φ : Nat → R} (h0 : φ 0 = 0) :
    b3Sym (pauliWignerCellSum φ 1 1) (pauliWignerCellSum φ 1 2) = φ 2 - 2 * φ 1 := by
  rw [pauliWignerCellSum_deuteron h0, pauliWignerCellSum_triton h0]
  unfold b3Sym
  ring

/-- **Exact connected 4-body cumulant.** For any cell kernel `φ` with `φ 0 = 0`,
`b₄(S_φ) = φ 3 - 3 φ 2 + 3 φ 1`. -/
theorem pauliWigner_b4_eq {φ : Nat → R} (h0 : φ 0 = 0) :
    b4Sym (pauliWignerCellSum φ 1 1) (pauliWignerCellSum φ 1 2) (pauliWignerCellSum φ 2 2) =
      φ 3 - 3 * φ 2 + 3 * φ 1 := by
  rw [pauliWignerCellSum_deuteron h0, pauliWignerCellSum_triton h0, pauliWignerCellSum_he4 h0]
  unfold b4Sym
  ring

/-- Classical linear content `φ_lin(j) = j` reproduces bounded-degree intra-shell pair counting
with `b₃ = 0` and `b₄ = 0`. -/
theorem linCell_b3_and_b4_eq_zero :
    b3Sym (pauliWignerCellSum (fun j : Nat => (j : R)) 1 1)
      (pauliWignerCellSum (fun j : Nat => (j : R)) 1 2) = 0 ∧
    b4Sym (pauliWignerCellSum (fun j : Nat => (j : R)) 1 1)
      (pauliWignerCellSum (fun j : Nat => (j : R)) 1 2)
      (pauliWignerCellSum (fun j : Nat => (j : R)) 2 2) = 0 := by
  have h0 : (fun j : Nat => (j : R)) 0 = 0 := by simp
  rw [pauliWigner_b3_eq h0, pauliWigner_b4_eq h0]
  constructor <;> norm_num

/-- **Discrete convexity criterion (`qou-q8vl` escape).** Over any strict ordered commutative
ring, `0 < b₃(S_φ)` holds if and only if `2 φ 1 < φ 2` (superlinear step from the 2nd to the 3rd
box in the Wigner `SU(4)` shell), requiring no multiplicative bond factor above `1`
(contrast `QOU.MassTheory.B3SignOneRoot.b3corpus_chain_neg_of_same_sign`). -/
theorem pauliWigner_b3_pos_iff [LinearOrder R] [IsStrictOrderedRing R]
    {φ : Nat → R} (h0 : φ 0 = 0) :
    0 < b3Sym (pauliWignerCellSum φ 1 1) (pauliWignerCellSum φ 1 2) ↔ 2 * φ 1 < φ 2 := by
  rw [pauliWigner_b3_eq h0]
  constructor <;> intro h <;> linarith

end PauliWignerShellCellCarrier

section QuantumSimplexCellKernels

variable {F : Type*} [Field F]

/-- Balanced Laurent quantum integer `[j]_q` on Wigner column indices `j ∈ {0, 1, 2, 3}`. -/
def qInt (q : F) : Nat → F
  | 0 => 0
  | 1 => 1
  | 2 => q + q⁻¹
  | 3 => q ^ 2 + 1 + q⁻¹ ^ 2
  | _ => 0

/-- Balanced quantum 2-simplex (triangle) cell kernel `binom(j, 2)_q = [j]_q [j-1]_q / [2]_q`
on `j ∈ {0, 1, 2, 3}`. -/
def qBinom2 (q : F) : Nat → F
  | 0 => 0
  | 1 => 0
  | 2 => 1
  | 3 => q ^ 2 + 1 + q⁻¹ ^ 2
  | _ => 0

/-- Balanced quantum 3-simplex (tetrahedron) cell kernel `binom(j, 3)_q` on `j ∈ {0, 1, 2, 3}`. -/
def qBinom3 : Nat → F
  | 3 => 1
  | _ => 0

/-- Verification that `qBinom2 q j * [2]_q = [j]_q * [j - 1]_q` for all `j ∈ {1, 2, 3}`. -/
theorem qBinom2_defining_rel (q : F) :
    qBinom2 q 1 * qInt q 2 = qInt q 1 * qInt q 0 ∧
    qBinom2 q 2 * qInt q 2 = qInt q 2 * qInt q 1 ∧
    qBinom2 q 3 * qInt q 2 = qInt q 3 * qInt q 2 := by
  simp only [qBinom2, qInt]
  refine ⟨by ring, by ring, by first | ring | trivial⟩

/-- Closed form in `ℚ(q)` for `b₃` of the `[j]_q` cell carrier: `(q - 1)² / q`. -/
theorem qInt_b3_eq {q : F} (hq : q ≠ 0) :
    b3Sym (pauliWignerCellSum (qInt q) 1 1) (pauliWignerCellSum (qInt q) 1 2) =
      (q - 1) ^ 2 / q := by
  have h0 : qInt q 0 = 0 := rfl
  rw [pauliWigner_b3_eq h0]
  simp only [qInt]
  field_simp [hq]
  ring

/-- Closed form in `ℚ(q)` for `b₄` of the `[j]_q` cell carrier:
`(q - 1)² (q² - q + 1) / q²`. -/
theorem qInt_b4_eq {q : F} (hq : q ≠ 0) :
    b4Sym (pauliWignerCellSum (qInt q) 1 1) (pauliWignerCellSum (qInt q) 1 2)
      (pauliWignerCellSum (qInt q) 2 2) =
      (q - 1) ^ 2 * (q ^ 2 - q + 1) / q ^ 2 := by
  have h0 : qInt q 0 = 0 := rfl
  rw [pauliWigner_b4_eq h0]
  simp only [qInt]
  field_simp [hq]
  ring

/-- The quantum 2-simplex kernel `qBinom2` vanishes on `²H` (`b₂ = 0`), equals `1` on `b₃`,
and equals `(q - 1)² (q + 1)² / q²` on `b₄`. -/
theorem qBinom2_cumulants_eq {q : F} (hq : q ≠ 0) :
    pauliWignerCellSum (qBinom2 q) 1 1 = 0 ∧
    b3Sym (pauliWignerCellSum (qBinom2 q) 1 1) (pauliWignerCellSum (qBinom2 q) 1 2) = 1 ∧
    b4Sym (pauliWignerCellSum (qBinom2 q) 1 1) (pauliWignerCellSum (qBinom2 q) 1 2)
      (pauliWignerCellSum (qBinom2 q) 2 2) = (q - 1) ^ 2 * (q + 1) ^ 2 / q ^ 2 := by
  have h0 : qBinom2 q 0 = 0 := rfl
  refine ⟨pauliWignerCellSum_deuteron h0, ?_, ?_⟩
  · rw [pauliWigner_b3_eq h0]
    simp only [qBinom2]
    ring
  · rw [pauliWigner_b4_eq h0]
    simp only [qBinom2]
    field_simp [hq]
    ring

/-- Wenzl-normalised unsigned quantum simplex cell kernel
`φ_qSimplex(j) = ∑_{d=1}^3 binom(j, d)_q / [d + 1]_q`. -/
def qSimplexKernel (q : F) (j : Nat) : F :=
  qInt q j / qInt q 2 + qBinom2 q j / qInt q 3 +
    qBinom3 j / (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3)

/-- Graded Euler–Poincaré alternating counterpart
`φ_epQSimplex(j) = ∑_{d=1}^3 (-1)^{d-1} binom(j, d)_q / [d + 1]_q`. -/
def epQSimplexKernel (q : F) (j : Nat) : F :=
  qInt q j / qInt q 2 - qBinom2 q j / qInt q 3 +
    qBinom3 j / (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3)

/-- Unconditional positivity of `[j]_q` cumulants `b₃ > 0` and `b₄ > 0` for all `q > 0, q ≠ 1`. -/
theorem qInt_b3_and_b4_pos [LinearOrder F] [IsStrictOrderedRing F]
    {q : F} (hq0 : 0 < q) (hq1 : q ≠ 1) :
    0 < b3Sym (pauliWignerCellSum (qInt q) 1 1) (pauliWignerCellSum (qInt q) 1 2) ∧
    0 < b4Sym (pauliWignerCellSum (qInt q) 1 1) (pauliWignerCellSum (qInt q) 1 2)
      (pauliWignerCellSum (qInt q) 2 2) := by
  have hqne : q ≠ 0 := ne_of_gt hq0
  have hsq : 0 < (q - 1) ^ 2 := sq_pos_of_ne_zero (sub_ne_zero.mpr hq1)
  have hcyc : 0 < q ^ 2 - q + 1 := by
    have hhalf : 0 ≤ (q - 1 / 2) ^ 2 := sq_nonneg (q - 1 / 2)
    linarith
  rw [qInt_b3_eq hqne, qInt_b4_eq hqne]
  exact ⟨div_pos hsq hq0, div_pos (mul_pos hsq hcyc) (sq_pos_of_pos hq0)⟩

/-- Exact closed form in `ℚ(q)` for `b₂` and `b₃` of the unsigned Wenzl-normalised quantum
simplex carrier `qSimplexKernel`. -/
theorem qSimplex_b2_and_b3_eq [LinearOrder F] [IsStrictOrderedRing F]
    {q : F} (hq0 : 0 < q) :
    pauliWignerCellSum (qSimplexKernel q) 1 1 = q / (q ^ 2 + 1) ∧
    b3Sym (pauliWignerCellSum (qSimplexKernel q) 1 1)
      (pauliWignerCellSum (qSimplexKernel q) 1 2) =
      (q - 1) ^ 2 / (q ^ 2 + 1) + q ^ 2 / (q ^ 4 + q ^ 2 + 1) := by
  have hqne : q ≠ 0 := ne_of_gt hq0
  have hq2pos : 0 < q ^ 2 + 1 := by nlinarith
  have hq4pos : 0 < q ^ 4 + q ^ 2 + 1 := by
    have h4 : 0 ≤ q ^ 4 := by positivity
    nlinarith
  have hq2ne : q ^ 2 + 1 ≠ 0 := ne_of_gt hq2pos
  have hq4ne : q ^ 4 + q ^ 2 + 1 ≠ 0 := ne_of_gt hq4pos
  have h0 : qSimplexKernel q 0 = 0 := by simp only [qSimplexKernel, qInt, qBinom2, qBinom3]; simp
  refine ⟨?_, ?_⟩
  · rw [pauliWignerCellSum_deuteron h0]
    simp only [qSimplexKernel, qInt, qBinom2, qBinom3]
    field_simp [hqne, hq2ne]
    ring
  · rw [pauliWigner_b3_eq h0]
    simp only [qSimplexKernel, qInt, qBinom2, qBinom3]
    field_simp [hqne, hq2ne, hq4ne]
    ring

/-- **Strict positivity of `qSimplexKernel` `b₃` for all `q > 0`.** Unlike `[j]_q` alone (whose
`b₃` vanishes at `q = 1`), the quantum 2-simplex term `q² / (q⁴ + q² + 1)` keeps `b₃ > 0`
strictly away from zero across all `q > 0`. -/
theorem qSimplex_b3_pos [LinearOrder F] [IsStrictOrderedRing F]
    {q : F} (hq0 : 0 < q) :
    0 < b3Sym (pauliWignerCellSum (qSimplexKernel q) 1 1)
      (pauliWignerCellSum (qSimplexKernel q) 1 2) := by
  rw [(qSimplex_b2_and_b3_eq hq0).2]
  have h1 : 0 ≤ (q - 1) ^ 2 / (q ^ 2 + 1) :=
    div_nonneg (sq_nonneg (q - 1)) (by nlinarith)
  have h2 : 0 < q ^ 2 / (q ^ 4 + q ^ 2 + 1) := by
    have h4 : 0 ≤ q ^ 4 := by positivity
    exact div_pos (sq_pos_of_pos hq0) (by nlinarith)
  linarith

/-- **Direct sign dichotomy against `B3SignOneRoot` (`qou-q8vl` + `qou-eptr`).** Whenever two
chain bond factors `f₀₁, f₁₂` lie on the same side of `1` (including `(0, 1)` confinement and
uniform `> 1` attraction), the multiplicative chain cumulant `b3corpus f₀₁ 1 f₁₂` is strictly
negative (`B3SignOneRoot.b3corpus_chain_neg_of_same_sign`), whereas the intra-shell quantum
simplex cell-sum cumulant is strictly positive for every `q > 0`. -/
theorem chain_vs_qSimplex_sign_dichotomy [LinearOrder F] [IsStrictOrderedRing F]
    {q f01 f12 : F} (hq0 : 0 < q)
    (hsame : (1 < f01 ∧ 1 < f12) ∨ (f01 < 1 ∧ f12 < 1)) :
    QOU.MassTheory.UrsellPartitionFunctionB3.b3corpus f01 1 f12 < 0 ∧
    0 < b3Sym (pauliWignerCellSum (qSimplexKernel q) 1 1)
      (pauliWignerCellSum (qSimplexKernel q) 1 2) :=
  ⟨QOU.MassTheory.B3SignOneRoot.b3corpus_chain_neg_of_same_sign hsame, qSimplex_b3_pos hq0⟩

/-- Closed form in `ℚ(q)` for `b₃` of the alternating Euler–Poincaré quantum simplex carrier. -/
theorem epQSimplex_b3_eq [LinearOrder F] [IsStrictOrderedRing F]
    {q : F} (hq0 : 0 < q) :
    b3Sym (pauliWignerCellSum (epQSimplexKernel q) 1 1)
      (pauliWignerCellSum (epQSimplexKernel q) 1 2) =
      (q - 1) ^ 2 / (q ^ 2 + 1) - q ^ 2 / (q ^ 4 + q ^ 2 + 1) := by
  have hqne : q ≠ 0 := ne_of_gt hq0
  have hq2ne : q ^ 2 + 1 ≠ 0 := ne_of_gt (by nlinarith)
  have h4 : 0 ≤ q ^ 4 := by positivity
  have hq4ne : q ^ 4 + q ^ 2 + 1 ≠ 0 := ne_of_gt (by nlinarith)
  have h0 : epQSimplexKernel q 0 = 0 := by simp only [epQSimplexKernel, qInt, qBinom2, qBinom3]; simp
  rw [pauliWigner_b3_eq h0]
  simp only [epQSimplexKernel, qInt, qBinom2, qBinom3]
  field_simp [hqne, hq2ne, hq4ne]
  ring

/-- **Euler–Poincaré sign obstruction on `[2/3, 3/2]`.** Across the entire interval
`2/3 ≤ q ≤ 3/2` (containing `q₀ ≈ 1.11`), the `(-1)^{d-1}` Euler–Poincaré sign flips the
2-simplex term negative and overwhelms the `(q - 1)²` curvature, forcing `b₃ < 0`. -/
theorem epQSimplex_b3_neg_of_mem_Icc [LinearOrder F] [IsStrictOrderedRing F]
    {q : F} (hq_lo : (2 : F) / 3 ≤ q) (hq_hi : q ≤ 3 / 2) :
    b3Sym (pauliWignerCellSum (epQSimplexKernel q) 1 1)
      (pauliWignerCellSum (epQSimplexKernel q) 1 2) < 0 := by
  have hq0 : 0 < q := by linarith
  have hqne : q ≠ 0 := ne_of_gt hq0
  rw [epQSimplex_b3_eq hq0]
  set u : F := q + q⁻¹
  have hu_lo : 2 ≤ u := by
    have hsq : 0 ≤ (q - 1) ^ 2 := sq_nonneg (q - 1)
    have hid : u - 2 = (q - 1) ^ 2 / q := by
      unfold u
      field_simp [hqne]
      ring
    linarith [div_nonneg hsq (le_of_lt hq0)]
  have hu_hi : u ≤ 13 / 6 := by
    have hquad : 0 ≤ (3 * q - 2) * (3 - 2 * q) :=
      mul_nonneg (by linarith) (by linarith)
    have hid : 13 / 6 - u = (3 * q - 2) * (3 - 2 * q) / (6 * q) := by
      unfold u
      field_simp [hqne]
      ring
    have hden : 0 ≤ 6 * q := by linarith
    linarith [div_nonneg hquad hden]
  have hpal : (u - 2) * (u ^ 2 - 1) - u < 0 := by
    have h1 : u - 2 ≤ 1 / 6 := by linarith
    have h2 : u ^ 2 - 1 ≤ 133 / 36 := by nlinarith
    have h3 : (u - 2) * (u ^ 2 - 1) ≤ (1 / 6) * (133 / 36) := by nlinarith
    linarith
  have hq2pos : 0 < q ^ 2 + 1 := by nlinarith
  have hq4pos : 0 < q ^ 4 + q ^ 2 + 1 := by
    have h4 : 0 ≤ q ^ 4 := by positivity
    nlinarith
  have hq2ne : q ^ 2 + 1 ≠ 0 := ne_of_gt hq2pos
  have hq4ne : q ^ 4 + q ^ 2 + 1 ≠ 0 := ne_of_gt hq4pos
  have hfrac : (q - 1) ^ 2 / (q ^ 2 + 1) - q ^ 2 / (q ^ 4 + q ^ 2 + 1) =
      q ^ 3 * ((u - 2) * (u ^ 2 - 1) - u) / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1)) := by
    unfold u
    field_simp [hqne, hq2ne, hq4ne]
    ring
  rw [hfrac]
  have hnum : q ^ 3 * ((u - 2) * (u ^ 2 - 1) - u) < 0 :=
    mul_neg_of_pos_of_neg (pow_pos hq0 3) hpal
  exact div_neg_of_neg_of_pos hnum (mul_pos hq2pos hq4pos)

end QuantumSimplexCellKernels

section ExtensiveShellCarrierHypothesis

/-- `§3b-cond` hypothesis bundle packaging the exact discrete-convexity and positivity conditions
under which an intra-shell Pauli–Wigner cell carrier simultaneously achieves linear α-extensivity,
strictly positive `b₃`, and Pauli triton–trineutron separation (`0` global instances). -/
class ExtensiveShellCarrierHypotheses (R : Type*)
    [CommRing R] [LinearOrder R] [IsStrictOrderedRing R] where
  /-- Intra-shell Bratteli column kernel `φ : Nat → R`. -/
  cellKernel : Nat → R
  /-- Positive energy scale `E_scale > 0`. -/
  energyScale : R
  /-- Positivity of the energy scale. -/
  scale_pos : 0 < energyScale
  /-- Unbound monomer normalisation `φ 0 = 0`. -/
  kernel_zero : cellKernel 0 = 0
  /-- Strict discrete convexity between the 2nd and 3rd box in a Wigner `SU(4)` shell. -/
  kernel_strict_convex_two : 2 * cellKernel 1 < cellKernel 2
  /-- Strict positivity of the `j = 2` three-body cell weight. -/
  kernel_two_pos : 0 < cellKernel 2

/-- Conditional binding functional `B_cell(Z, N) = E_scale * pauliWignerCellSum φ Z N`. -/
def shellBinding
    {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    [h : ExtensiveShellCarrierHypotheses R] (zProt nNeut : Nat) : R :=
  h.energyScale * pauliWignerCellSum h.cellKernel zProt nNeut

/-- Under `ExtensiveShellCarrierHypotheses`, α-conjugate nuclei `(2m, 2m)` scale strictly
linearly in `m = A / 4`. -/
theorem shellBinding_alpha_linear
    {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    [h : ExtensiveShellCarrierHypotheses R] (m : Nat) :
    shellBinding (R := R) (2 * m) (2 * m) = (m : R) * shellBinding (R := R) 2 2 := by
  unfold shellBinding
  rw [pauliWignerCellSum_alpha_mul h.kernel_zero, pauliWignerCellSum_he4 h.kernel_zero]
  ring

/-- Under `ExtensiveShellCarrierHypotheses`, the connected 3-body cumulant `b₃` is strictly
positive (`0 < b₃`). -/
theorem shellBinding_b3_pos
    {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    [h : ExtensiveShellCarrierHypotheses R] :
    0 < b3Sym (shellBinding (R := R) 1 1) (shellBinding (R := R) 1 2) := by
  have heq : b3Sym (shellBinding (R := R) 1 1) (shellBinding (R := R) 1 2) =
      h.energyScale * b3Sym (pauliWignerCellSum h.cellKernel 1 1)
        (pauliWignerCellSum h.cellKernel 1 2) := by
    unfold shellBinding b3Sym
    ring
  rw [heq]
  have hb3 : 0 < b3Sym (pauliWignerCellSum h.cellKernel 1 1)
      (pauliWignerCellSum h.cellKernel 1 2) :=
    (pauliWigner_b3_pos_iff h.kernel_zero).mpr h.kernel_strict_convex_two
  exact mul_pos h.scale_pos hb3

/-- Under `ExtensiveShellCarrierHypotheses`, `³H` `(1, 2)` is strictly more strongly bound than
the Pauli-split trineutron `(0, 3)` by `E_scale * φ 2 > 0`. -/
theorem shellBinding_triton_gt_trineutron
    {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    [h : ExtensiveShellCarrierHypotheses R] :
    shellBinding (R := R) 0 3 < shellBinding (R := R) 1 2 := by
  have hdiff : shellBinding (R := R) 1 2 - shellBinding (R := R) 0 3 =
      h.energyScale * h.cellKernel 2 := by
    calc
      shellBinding (R := R) 1 2 - shellBinding (R := R) 0 3 =
          h.energyScale * (pauliWignerCellSum h.cellKernel 1 2 -
            pauliWignerCellSum h.cellKernel 0 3) := by
        unfold shellBinding
        ring
      _ = h.energyScale * h.cellKernel 2 := by
        rw [pauliWigner_triton_sub_trineutron h.kernel_zero]
  have hpos : 0 < h.energyScale * h.cellKernel 2 := mul_pos h.scale_pos h.kernel_two_pos
  linarith

/-- Explicit anti-vacuity inhabitation over `ℚ` instantiated at `qSimplexKernel (111 / 100)`. -/
theorem exists_extensiveShellCarrierHypotheses_rat :
    Nonempty (ExtensiveShellCarrierHypotheses ℚ) := by
  refine ⟨{
    cellKernel := qSimplexKernel (111 / 100 : ℚ)
    energyScale := 4227 / 1000
    scale_pos := by norm_num
    kernel_zero := by unfold qSimplexKernel qInt qBinom2 qBinom3; norm_num
    kernel_strict_convex_two := by
      have hpos := qSimplex_b3_pos (F := ℚ) (q := 111 / 100) (by norm_num)
      have h0 : qSimplexKernel (111 / 100 : ℚ) 0 = 0 := by
        unfold qSimplexKernel qInt qBinom2 qBinom3; norm_num
      exact (pauliWigner_b3_pos_iff h0).mp hpos
    kernel_two_pos := by
      unfold qSimplexKernel qInt qBinom2 qBinom3
      norm_num
  }⟩

end ExtensiveShellCarrierHypothesis

end QOU.MassTheory.B3ExtensiveCellSumCarrier
