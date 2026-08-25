import QOU.Machinery.MarkovTraceOnHecke
import QOU.Shared.DetFin
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Tactic

/-!
# QOU.Machinery.HeckeH3GramNondegeneracy — Gram nondegeneracy of the H₃(q) Markov trace

A3-s1 Schur-trace bridge at rank 3 (bean `qou-c7e3`, approach `qou-ulrx`,
milestone `qou-lv5t`).  The Gram matrix of the Markov-trace pairing
$\langle x, y\rangle = \mathrm{tr}_M(x\cdot y)$ on the GB normal-form basis
$[\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-]$ of $H_3(q)$, its determinant in
closed form, and the concrete nondegeneracy statement.

## Provenance (sympy, verified before formalization)

The 6×6 entry table and the factored determinant were derived symbolically in
`computations/h3_gram/hecke_h3_markov_gram_derive.py` and pinned in
`computations/h3_gram/hecke-h3-markov-gram.data.json`; every closed form below
was cross-checked numerically (e.g. at `z = 3, h = 2` both sides of
`gramMatrix_det` equal `-736`) before the Lean proofs were attempted.  Nothing
is trusted from the computation — `gramMatrix_eq` re-derives every entry from
the `trM`/`mulNF` substrate of `MarkovTraceOnHecke.lean` inside Lean.

## The determinant and its degeneracy locus

$$ \det G \;=\; -\bigl(z^2 - hz - 1\bigr)^5\,
   \bigl((h^2+4)z^2 - (h^3+4h)z - 1\bigr). $$

At the Hecke specialization $h = q - q^{-1}$ the two factors split:

* $z^2 - hz - 1 = (z - q)(z + q^{-1})$ — the quintic factor vanishes exactly at
  the **character weights** $z \in \{q, -q^{-1}\}$ (the two 1-dimensional
  Wedderburn blocks of $H_3(q)$ swallowing the trace);
* $(h^2+4)z^2 - (h^3+4h)z - 1
  = \bigl((q^2+1)z - q^3\bigr)\bigl((q^3+q)z + 1\bigr)/q^3$ — the quadratic
  factor vanishes at the two **$(2,1)$-block Markov-weight zeros**
  $z = q^3/(q^2+1)$ and $z = -1/(q(q^2+1))$.

Away from these four points the trace pairing is nondegenerate:
`exists_pairing_ne_zero` produces, for every nonzero `y`, a witness `w` with
$\mathrm{tr}_M(y\cdot w) \neq 0$.  This realizes the trace-nondegeneracy
hypothesis of `QOU.Machinery.HeckeTower.WenzlTowerStep` (`semisimple_ascend`)
**concretely at rank 3** — the hypothesis is no longer an abstract input but a
proved fact of the explicit H₃ Markov trace on its degeneracy-free locus.

Base ring (§7c): generic `[CommRing R]` throughout; `[Field K]` only where the
inverse Gram matrix is needed (`exists_pairing_ne_zero`,
`gramMatrix_det_ne_zero`).  No archimedean construct.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.Machinery.H3

variable {R : Type*} [CommRing R]

/-- The **Gram matrix** of the H₃(q) Markov-trace pairing
`⟨bᵢ, bⱼ⟩ = tr_M(bᵢ · bⱼ)` on the GB normal-form basis
`[γ, σ₀, σ₁, L₊, L₋, e⁻]`.  Entries are the polynomial-expanded forms of
`computations/h3_gram/hecke-h3-markov-gram.data.json` (`gram` field); the
identification with the trace pairing is `gramMatrix_eq`. -/
def gramMatrix (z h : R) : Matrix (Fin 6) (Fin 6) R :=
  Matrix.of
    ![![1, z, z, z ^ 2, z ^ 2, h * z ^ 2 + z],
      ![z, h * z + 1, z ^ 2, h * z ^ 2 + z, h * z ^ 2 + z,
        h ^ 2 * z ^ 2 + h * z + z ^ 2],
      ![z, z ^ 2, h * z + 1, h * z ^ 2 + z, h * z ^ 2 + z,
        h ^ 2 * z ^ 2 + h * z + z ^ 2],
      ![z ^ 2, h * z ^ 2 + z, h * z ^ 2 + z, h ^ 2 * z ^ 2 + h * z + z ^ 2,
        h ^ 2 * z ^ 2 + 2 * h * z + 1,
        h ^ 3 * z ^ 2 + h ^ 2 * z + 2 * h * z ^ 2 + z],
      ![z ^ 2, h * z ^ 2 + z, h * z ^ 2 + z, h ^ 2 * z ^ 2 + 2 * h * z + 1,
        h ^ 2 * z ^ 2 + h * z + z ^ 2,
        h ^ 3 * z ^ 2 + h ^ 2 * z + 2 * h * z ^ 2 + z],
      ![h * z ^ 2 + z, h ^ 2 * z ^ 2 + h * z + z ^ 2,
        h ^ 2 * z ^ 2 + h * z + z ^ 2,
        h ^ 3 * z ^ 2 + h ^ 2 * z + 2 * h * z ^ 2 + z,
        h ^ 3 * z ^ 2 + h ^ 2 * z + 2 * h * z ^ 2 + z,
        h ^ 4 * z ^ 2 + h ^ 3 * z + 3 * h ^ 2 * z ^ 2 + 3 * h * z + 1]]

set_option maxHeartbeats 6400000 in
/-- `gramMatrix` **is** the Gram matrix of the Markov-trace pairing: entry
`(i, j)` is `tr_M(bᵢ · bⱼ)` for the basis vectors `bᵢ = Pi.single i 1`.
Re-derives every entry of the sympy table from the `trM`/`mulNF` substrate. -/
theorem gramMatrix_eq (z h : R) (i j : Fin 6) :
    gramMatrix z h i j = trM z h (mulNF h (Pi.single i 1) (Pi.single j 1)) := by
  fin_cases i <;> fin_cases j <;>
    simp [gramMatrix, trM, TRM, mulNF, mulσ₀, mulσ₁, Fin.sum_univ_six,
      Pi.single_apply] <;> ring

/-- **Bilinearity in matrix form**: the trace pairing of arbitrary elements is
the Gram bilinear form, `tr_M(u · v) = ∑ⱼ (∑ᵢ uᵢ Gᵢⱼ) vⱼ` — the plain-sum
(`vecMul`-free) phrasing of `tr_M(u·v) = (u ᵥ* G) ⬝ᵥ v`. -/
theorem trM_mulNF_eq_dotProduct (z h : R) (u v : Fin 6 → R) :
    trM z h (mulNF h u v) = ∑ j, (∑ i, u i * gramMatrix z h i j) * v j := by
  simp only [trM, mulNF, mulσ₀, mulσ₁, TRM, gramMatrix, Matrix.of_apply,
    Fin.sum_univ_six, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val]
  ring

set_option maxHeartbeats 8000000 in
set_option maxRecDepth 8000 in
/-- **Closed-form determinant** of the H₃ Markov-trace Gram matrix:
`det G = -(z² - hz - 1)⁵ · ((h²+4)z² - (h³+4h)z - 1)`.
Matches `detG_zh` of the sympy witness
`computations/h3_gram/hecke-h3-markov-gram.data.json` (numerically
cross-checked, e.g. both sides `= -736` at `z = 3, h = 2`). -/
theorem gramMatrix_det (z h : R) :
    (gramMatrix z h).det =
      -(z ^ 2 - h * z - 1) ^ 5 *
        ((h ^ 2 + 4) * z ^ 2 - (h ^ 3 + 4 * h) * z - 1) := by
  rw [Matrix.det_fin_six]
  simp only [gramMatrix, Matrix.of_apply, Matrix.cons_val_zero,
    Matrix.cons_val_one, Matrix.cons_val]
  ring

/-- **Trace nondegeneracy from the determinant** — the Wenzl-hypothesis
realization at rank 3: whenever `det G ≠ 0`, every nonzero `y ∈ H₃(q)` pairs
nontrivially with some `w` under the Markov trace.  This exact shape is the
`semisimple_ascend` trace-nondegeneracy hypothesis of
`QOU.Machinery.HeckeTower.WenzlTowerStep`, here discharged concretely for the
explicit H₃ trace.  The witness is a basis vector: pick `j` with
`(y ᵥ* G) j ≠ 0` (possible since `G` is invertible) and take
`w = Pi.single j 1`. -/
theorem exists_pairing_ne_zero {K : Type*} [Field K] (z h : K)
    (hdet : (gramMatrix z h).det ≠ 0) (y : Fin 6 → K) (hy : y ≠ 0) :
    ∃ w : Fin 6 → K, trM z h (mulNF h y w) ≠ 0 := by
  have hGu : IsUnit (gramMatrix z h).det := isUnit_iff_ne_zero.mpr hdet
  have hvm : Matrix.vecMul y (gramMatrix z h) ≠ 0 := by
    intro hc
    apply hy
    have h2 := congrArg (fun w => Matrix.vecMul w (gramMatrix z h)⁻¹) hc
    simpa [Matrix.vecMul_vecMul, Matrix.mul_nonsing_inv _ hGu] using h2
  obtain ⟨j, hj⟩ : ∃ j, Matrix.vecMul y (gramMatrix z h) j ≠ 0 := by
    by_contra hall
    push_neg at hall
    exact hvm (funext fun j => hall j)
  refine ⟨Pi.single j 1, ?_⟩
  have hvj : Matrix.vecMul y (gramMatrix z h) j = ∑ i, y i * gramMatrix z h i j := by
    simp [Matrix.vecMul, dotProduct]
  rw [trM_mulNF_eq_dotProduct]
  have hsum : (∑ j' : Fin 6, (∑ i, y i * gramMatrix z h i j') * (Pi.single j 1 : Fin 6 → K) j')
      = ∑ i, y i * gramMatrix z h i j := by
    rw [Fintype.sum_eq_single j (fun b hb => by simp [Pi.single_eq_of_ne hb])]
    simp
  rw [hsum, ← hvj]
  exact hj

/-- **Nondegeneracy at the Hecke specialization** `h = q - q⁻¹`: the Gram
determinant is nonzero away from the four degeneracy points.

* **Quintic factor**, via `z² - hz - 1 = (z - q)(z + q⁻¹)`: the eigenvalue
  channels `z = q` and `z = -q⁻¹`.  Each is a **corank-5** collapse — the Gram
  drops to rank 1 there, not to rank 5.
* **Quadratic factor**, via
  `q³·((h²+4)z² - (h³+4h)z - 1) = ((q²+1)z - q³)((q³+q)z + 1)`: the Markov-weight
  zeros `z = q³/(q²+1)` and `z = -1/(q(q²+1))`.  Each is a **corank-1** collapse,
  and the block that drops out is **one-dimensional** in both cases:
  the sign representation `(1³)` at `z = q³/(q²+1)`, whose radical is the
  q-antisymmetriser `(-q³, q², q², -q, -q, 1)`, and the trivial representation
  `(3)` at `z = -1/(q(q²+1))`, whose radical is the q-symmetriser.

  This corrects an earlier reading of these two as `(2,1)`-block zeros.  `(2,1)`
  has dimension 2, and a block of dimension `d` leaving the trace costs the Gram
  `d²` dimensions — so `(2,1)` would give corank 4, where the measured corank is
  1.  The statement below is unaffected: all four hypotheses are exactly the
  vanishing locus and the proof never used the attribution.

  The `z = q³/(q²+1)` case is convention D, canonical since the owner ruling of
  2026-08-15, so this is the identity behind
  `QOU.Interactions.GramMatrixH3Symbolic.gramMatrixD_det_eq_zero`; its
  `gramRadicalD` is the same vector, reached independently.  Reading it as `(1³)`
  rather than `(2,1)` is what connects it to `y_λ = 0` for partitions with `≥ 3`
  rows (bean `qou-8iru`) — the same degeneracy seen from the weights.

  Corank and block identification measured exactly over `ℚ(q)` in
  `computations/probes/h3_gram_degeneracy_block_identification_probe.py`. -/
theorem gramMatrix_det_ne_zero {K : Type*} [Field K] (q z : K) (hq : q ≠ 0)
    (h1 : z ≠ q) (h2 : z ≠ -q⁻¹) (h3 : (q ^ 2 + 1) * z ≠ q ^ 3)
    (h4 : (q ^ 3 + q) * z ≠ -1) :
    (gramMatrix z (q - q⁻¹)).det ≠ 0 := by
  rw [gramMatrix_det]
  have e1 : z ^ 2 - (q - q⁻¹) * z - 1 = (z - q) * (z + q⁻¹) := by
    field_simp
    ring
  have hfac1 : z ^ 2 - (q - q⁻¹) * z - 1 ≠ 0 := by
    rw [e1]
    refine mul_ne_zero (sub_ne_zero.mpr h1) fun hc => h2 ?_
    exact eq_neg_of_add_eq_zero_left hc
  have hfac2 : ((q - q⁻¹) ^ 2 + 4) * z ^ 2
      - ((q - q⁻¹) ^ 3 + 4 * (q - q⁻¹)) * z - 1 ≠ 0 := by
    intro hB
    have e2 : q ^ 3 * (((q - q⁻¹) ^ 2 + 4) * z ^ 2
          - ((q - q⁻¹) ^ 3 + 4 * (q - q⁻¹)) * z - 1)
        = ((q ^ 2 + 1) * z - q ^ 3) * ((q ^ 3 + q) * z + 1) := by
      field_simp
      ring
    rw [hB, mul_zero] at e2
    have hf1 : (q ^ 2 + 1) * z - q ^ 3 ≠ 0 := sub_ne_zero.mpr h3
    have hf2 : (q ^ 3 + q) * z + 1 ≠ 0 := fun hc => h4 (eq_neg_of_add_eq_zero_left hc)
    exact mul_ne_zero hf1 hf2 e2.symm
  exact mul_ne_zero (neg_ne_zero.mpr (pow_ne_zero 5 hfac1)) hfac2

end QOU.Machinery.H3
