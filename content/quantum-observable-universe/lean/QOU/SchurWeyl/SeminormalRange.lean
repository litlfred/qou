import QOU.SchurWeyl.SeminormalSimpleSpectrum
import QOU.SchurWeyl.DiagonalSeparation

/-!
# QOU.SchurWeyl.SeminormalRange — matrix units inside the seminormal image

Toward SW-5 in the **range form** `AlgHom.range (seminormalRep …) = ⊤`, which is what the
Wedderburn assembly (SW-7, `qou-0h5k`) actually consumes: it needs surjectivity onto the matrix
block, not an abstract "no proper submodule" statement, and it avoids standing up a
module-over-the-algebra structure just to say so.

Two of the three steps are here, and neither needs connectivity:

* **Diagonal units** (`single_self_mem_range`).  Each `ρ(L_k)` *is* its own diagonal
  (`diagonal_seminormalRep_qJM`), the tuples separate the tableaux
  (`seminormalRep_qJM_spectrum_injective`), so `DiagonalSeparation` interpolates every
  `single T T 1` out of the family.
* **Off-diagonal units from a nonzero entry** (`single_mem_range_of_entry_ne_zero`).  Sandwiching
  any element of the image between two diagonal units extracts a single scaled matrix unit
  (`Matrix.single_mul_mul_single`), and the scalar is invertible exactly when the entry is
  nonzero.

What is **not** here is the step that supplies those nonzero entries for *every* pair: an
invariant-subspace-free way of saying that the SYT of one shape are connected by admissible swaps,
along each of which `genMat`'s off-diagonal entry `offDiag` is nonzero.  `syt_adjacentSwap_connected`
proves exactly that on the `BraidKnot` side, sorry-free; transporting it is the remaining work
(bean `qou-jfr8`), and it is a strictly larger translation than `SytContentTuple` was, because the
*swap* notions have to be matched, not just the label conventions.

LaTeX label: `lem:seminormal-matrix-units`
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)
open TableauCells SeminormalRep

variable {μ : YoungDiagram}

/-- `ρ(L_k)` equals the diagonal matrix read off its own diagonal — the form
`DiagonalSeparation` consumes. -/
theorem diagonal_seminormalRep_qJM (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hN : μ.cells.card = n + 1) (k : ℕ) (hk : k ≤ n) :
    Matrix.diagonal (fun T : StandardYoungTableau μ =>
        seminormalRep q hq0 hq2 n hN (qJM ℝ q q⁻¹ n k) T T)
      = seminormalRep q hq0 hq2 n hN (qJM ℝ q q⁻¹ n k) := by
  rw [seminormalRep_qJM q hq0 hq2 n hN k hk, jmDiagVal]
  ext T U
  by_cases h : T = U
  · subst h; simp
  · simp [Matrix.diagonal_apply_ne _ h]

/-- **Every diagonal matrix unit lies in the image of the seminormal representation.**

The `q`-Jucys–Murphy images are diagonal *and* separating, which is exactly the hypothesis pair of
`single_self_mem_of_separating`; the interpolation there does the rest. -/
theorem single_self_mem_range (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hN : μ.cells.card = n + 1) (T : StandardYoungTableau μ) :
    Matrix.single T T (1 : ℝ) ∈ (seminormalRep q hq0 hq2 n hN).range := by
  refine single_self_mem_of_separating (V := Fin (n + 1)) _
    (fun (T : StandardYoungTableau μ) (k : Fin (n + 1)) =>
      seminormalRep q hq0 hq2 n hN (qJM ℝ q q⁻¹ n k.val) T T) (fun k => ?_) (fun T1 T2 hne => ?_) T
  · rw [diagonal_seminormalRep_qJM q hq0 hq2 n hN k.val (by omega)]
    exact ⟨qJM ℝ q q⁻¹ n k.val, rfl⟩
  · by_contra hcon
    push_neg at hcon
    exact hne (seminormalRep_qJM_spectrum_injective q hq0 hq2 n hN (funext hcon))

/-- **A nonzero matrix entry promotes to an off-diagonal matrix unit.**  If some element of the
image has a nonzero `(T', T)` entry, then `single T' T 1` is itself in the image: sandwich between
the two diagonal units and divide by the entry. -/
theorem single_mem_range_of_entry_ne_zero (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hN : μ.cells.card = n + 1) {x : Hecke ℝ q q⁻¹ n} {T T' : StandardYoungTableau μ}
    (hx : seminormalRep q hq0 hq2 n hN x T' T ≠ 0) :
    Matrix.single T' T (1 : ℝ) ∈ (seminormalRep q hq0 hq2 n hN).range := by
  set A := (seminormalRep q hq0 hq2 n hN).range with hA
  have hsandwich : Matrix.single T' T' (1 : ℝ) * seminormalRep q hq0 hq2 n hN x
      * Matrix.single T T (1 : ℝ)
      = Matrix.single T' T (seminormalRep q hq0 hq2 n hN x T' T) := by
    rw [Matrix.single_mul_mul_single]
    congr 1
    ring
  have hmem : Matrix.single T' T (seminormalRep q hq0 hq2 n hN x T' T) ∈ A := by
    rw [← hsandwich]
    exact mul_mem (mul_mem (single_self_mem_range q hq0 hq2 n hN T') ⟨x, rfl⟩)
      (single_self_mem_range q hq0 hq2 n hN T)
  have hscale : Matrix.single T' T (1 : ℝ)
      = (seminormalRep q hq0 hq2 n hN x T' T)⁻¹
          • Matrix.single T' T (seminormalRep q hq0 hq2 n hN x T' T) := by
    rw [Matrix.smul_single, smul_eq_mul, inv_mul_cancel₀ hx]
  rw [hscale]
  exact Subalgebra.smul_mem _ hmem _

end QOU.SchurWeyl
