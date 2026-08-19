import QOU.SchurWeyl.SeminormalRange
import QOU.SchurWeyl.SytSwapTransport
import QOU.SchurWeyl.OffDiagNonvanishing

/-!
# QOU.SchurWeyl.SeminormalRangeTop — the seminormal representation is surjective

**SW-5 in the range form** (beans `qou-jfr8` / `qou-x10g`): for a shape `μ` with `|μ| = n+1` and a
real `q` that is not a root of unity,

    AlgHom.range (seminormalRep q hq0 hq2 n hN) = ⊤

i.e. `H_{n+1}(q)` surjects onto the full matrix algebra `M_{#SYT μ}(ℝ)`.  This is the form the
Wedderburn assembly (SW-7, `qou-0h5k`) consumes, and it is Burnside-equivalent to irreducibility
without needing a module-over-the-algebra structure to state.

The four inputs, each landed separately:

* **diagonal units** — `single_self_mem_range`: Ram 4.1 makes the `q`-Jucys–Murphy images diagonal,
  the content tuple makes them *separating*, and finite-set Lagrange interpolation
  (`DiagonalSeparation`) turns that into every `single T T 1`.
* **connectivity** — `syt_swapStep_connected`: any two SYT of one shape are joined by admissible
  swaps, transported from the Okounkov–Vershik stack.
* **nonvanishing** — `offDiag_ne_zero_of_two_le_abs` with `two_le_abs_axialDist_of_admissible`:
  *both* orientations of each edge carry a nonzero entry.  Without this the argument fails, and not
  for want of effort: `offDiag q (−1) = 0`, so one orientation per edge would be all one gets.
* **promotion** — `single_mem_range_of_entry_ne_zero`: a nonzero entry sandwiched between two
  diagonal units is a scaled matrix unit.

LaTeX label: `thm:seminormal-rep-surjective`
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)
open TableauCells SeminormalRep

variable {μ : YoungDiagram}

/-- **One admissible swap yields its off-diagonal matrix unit.**  The generator `σ_k` has entry
`offDiag q (axialDist T k)` at `(s_k·T, T)`, and that is nonzero because an admissible pair sits at
distance `|d| ≥ 2`. -/
theorem single_swapTableau_mem_range (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hN : μ.cells.card = n + 1) {T : StandardYoungTableau μ} {k : ℕ} (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hadm : SwapAdmissible T k) :
    Matrix.single (swapTableau T k hk hkn hadm) T (1 : ℝ)
      ∈ (seminormalRep q hq0 hq2 n hN).range := by
  have hkle : k - 1 < n := by omega
  have hgen : seminormalRep q hq0 hq2 n hN (Hecke.σ ℝ q q⁻¹ n ⟨k - 1, hkle⟩)
      = genMat q k hk hkn := by
    rw [seminormalRep_σ, seminormalGen]
    congr 1
    show k - 1 + 1 = k
    omega
  have hentry : genMat q k hk hkn (swapTableau T k hk hkn hadm) T
      = offDiag q (axialDist T k) :=
    genMat_swap q k hk hkn hadm (swapTableau_ne T hk hkn hadm)
  have hne : genMat q k hk hkn (swapTableau T k hk hkn hadm) T ≠ 0 := by
    rw [hentry]
    exact offDiag_ne_zero_of_two_le_abs q hq0 hq2
      (two_le_abs_axialDist_of_admissible T hk hkn hadm)
  refine single_mem_range_of_entry_ne_zero q hq0 hq2 n hN
    (x := Hecke.σ ℝ q q⁻¹ n ⟨k - 1, hkle⟩) ?_
  rw [hgen]
  exact hne

/-- **Every matrix unit lies in the image.**  Induct along the admissible-swap chain joining `T` to
`T'`, composing the one-step units with `single_mul_single_same`. -/
theorem single_mem_range (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hN : μ.cells.card = n + 1) (T T' : StandardYoungTableau μ) :
    Matrix.single T' T (1 : ℝ) ∈ (seminormalRep q hq0 hq2 n hN).range := by
  have hchain : Relation.ReflTransGen (SwapStep (μ := μ)) T T' := syt_swapStep_connected T T'
  induction hchain with
  | refl => exact single_self_mem_range q hq0 hq2 n hN T
  | tail _ hstep ih =>
      obtain ⟨k, hk, hkn, hadm, rfl⟩ := hstep
      have hone := single_swapTableau_mem_range q hq0 hq2 n hN hk hkn hadm
      have hcomp := mul_mem hone ih
      rwa [Matrix.single_mul_single_same, one_mul] at hcomp

/-- **The seminormal representation is surjective onto the full matrix algebra.**

`H_{n+1}(q) ↠ M_{#SYT μ}(ℝ)` for every shape `μ` of size `n+1`, at every real `q` that is not a
root of unity.  Equivalently: the `d_λ`-dimensional seminormal module is irreducible, in the form
the Wedderburn assembly can consume. -/
theorem seminormalRep_range_eq_top (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hN : μ.cells.card = n + 1) :
    (seminormalRep q hq0 hq2 n hN).range = ⊤ :=
  eq_top_of_single_mem _ (fun T' T => single_mem_range q hq0 hq2 n hN T T')

end QOU.SchurWeyl
