/-
# The Q_β eigenphase carrier asserts nothing — and a content-bearing replacement

Bean `qou-cds1`.  Tranche S1 needs a **derivation** of the ladder phase
`α = (z−1)h/2`, because `qbeta_ladder_required_phase_probe.py` prunes the whole
class "`α = (z−1)h/2` with `z` a convention parameter" for convention D: the
required phase is pinned to a window of half-width `≈1.1e-5` rad and `z_D` sits
`≈1.19e-2` rad away, so the *functional form* has to change, not the value of
`z` inside it.

Chasing where `α` is asserted leads to
`content/quantum-observable-universe/nuclear-interactions/q-beta-cos-resummation.lean`,
whose class `QOU.Interactions.TransferMatrixEigenphase` is documented as
axiomatising the spectral identification

  > `M_β` has spectrum `{e^{+iα}, e^{−iα}}` on the 2-d irrep `V_{(2,1)}` of
  > `H₃(q)`, where `α = (z−1)h/2`.

**Its two fields encode none of that.**  They are

  `-2 ≤ 2 cos(eigenphase q) ∧ 2 cos(eigenphase q) ≤ 2`
  `cos(eigenphase q) = cos(-eigenphase q)`

and both hold for *every real number* in place of the eigenphase
(`Real.neg_one_le_cos` / `Real.cos_le_one`, and `Real.cos_neg`).  So the class
is inhabited for every `q` by a proof that uses nothing about `eigenphase` at
all — it is equivalent to `True`, and a theorem stated
`[TransferMatrixEigenphase q] → P` is just `P`.

This is the `proof-claims-unencoded` failure mode of AGENTS.md §3b-tax: a
carrier whose docstring enumerates named properties that are not encoded as Prop
fields.  It is also the direct reason `α` is *asserted and derived nowhere* —
the carrier meant to hold the assertion holds nothing, so there is no
C-frame content to port to D.

§1 below demonstrates the vacuity.  §2 proposes the minimal honest repair: a
carrier that states the spectral identification with real content and has **no
instance**, which per §3b-tax is how a genuinely open input is represented.

**Scope.**  This does not derive `α`, in either convention, and does not claim
the cos-resummation is false — only that its Lean hypothesis is empty, so the
result is unconditional rather than conditional, and the physical content the
docstring describes is not carried anywhere.  Scope-(a).
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.Complex.Exponential
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic

namespace QOU.QBeta.EigenphaseCarrier

open Real

/-! ## §1 — the existing carrier is vacuous

Definitions reproduced verbatim from the content-block sibling so this file is
self-contained and does not depend on a block's `.lean` staying put. -/

/-- Convention-C Markov parameter, as spelled in the content block. -/
noncomputable def markovZ (q : ℝ) : ℝ := 1 / (Real.sqrt q + (Real.sqrt q)⁻¹)

/-- `h = q − q⁻¹`. -/
noncomputable def heckeH (q : ℝ) : ℝ := q - q⁻¹

/-- The asserted single-wrap eigenphase `α = (z−1)h/2`. -/
noncomputable def eigenphase (q : ℝ) : ℝ := (markovZ q - 1) * heckeH q / 2

/-- The existing carrier, fields reproduced verbatim. -/
class TransferMatrixEigenphase (q : ℝ) : Prop where
  symmetrized_character_in_unit_disc :
    -2 ≤ 2 * Real.cos (eigenphase q) ∧ 2 * Real.cos (eigenphase q) ≤ 2
  cos_eigenphase_bar_invariant :
    Real.cos (eigenphase q) = Real.cos (- eigenphase q)

/-- Field 1 holds for an **arbitrary** real, so it says nothing about the
eigenphase. -/
theorem field1_holds_for_any_real (x : ℝ) : -2 ≤ 2 * cos x ∧ 2 * cos x ≤ 2 := by
  constructor
  · nlinarith [neg_one_le_cos x]
  · nlinarith [cos_le_one x]

/-- Field 2 likewise: `cos` is even, for every real. -/
theorem field2_holds_for_any_real (x : ℝ) : cos x = cos (-x) := (cos_neg _).symm

/-- **The carrier is inhabited for every `q`**, by a proof using nothing about
`eigenphase`. -/
instance vacuousWitness (q : ℝ) : TransferMatrixEigenphase q where
  symmetrized_character_in_unit_disc := field1_holds_for_any_real _
  cos_eigenphase_bar_invariant := field2_holds_for_any_real _

/-- **The carrier is equivalent to `True`.**  Hence `[TransferMatrixEigenphase q] → P`
carries exactly the content of `P`; the hypothesis discharges itself. -/
theorem carrier_is_trivial (q : ℝ) : TransferMatrixEigenphase q ↔ True :=
  ⟨fun _ => trivial, fun _ => vacuousWitness q⟩

/-! ## §2 — a content-bearing replacement

A 2×2 real matrix has spectrum `{e^{+iα}, e^{−iα}}` exactly when its trace is
`2 cos α` and its determinant is `1` (the characteristic polynomial is then
`t² − 2cos(α)t + 1`, whose roots are `e^{±iα}`).  Stating *that* is what the
docstring of the existing class describes and its fields omit.

Unlike the original, this carrier is **falsifiable**: it constrains the matrix.
It is deliberately left with **no instance** — per AGENTS.md §3b-tax an unproved
primary is honestly represented by a content-bearing class with no instance, and
supplying a trivial one would reintroduce exactly the defect §1 documents. -/

/-- **Spectral identification of the β-decay transfer matrix** (content-bearing).

`M` is the transfer matrix restricted to the 2-d irrep `V_(2,1)` of `H₃(q)`.
The two fields pin its spectrum to `{e^{+iα}, e^{−iα}}` with `α = eigenphase q`.

Deliberately **uninstantiated**: this is the open input tranche S1 must supply,
and it is the statement a derivation of `α` would have to discharge. -/
class TransferMatrixSpectrum (q : ℝ) (M : Matrix (Fin 2) (Fin 2) ℝ) : Prop where
  /-- The Markov-symmetrised single-wrap character is `2 cos α`. -/
  trace_eq : M.trace = 2 * Real.cos (eigenphase q)
  /-- Unimodular spectrum: `e^{+iα}·e^{−iα} = 1`. -/
  det_eq : M.det = 1

/-- The replacement carrier is **not** vacuous: it pins the trace, so a matrix
whose trace differs from `2 cos α` cannot satisfy it.  Contrast
`carrier_is_trivial`. -/
theorem replacement_constrains_trace (q : ℝ) (M : Matrix (Fin 2) (Fin 2) ℝ)
    [h : TransferMatrixSpectrum q M] : M.trace = 2 * Real.cos (eigenphase q) :=
  h.trace_eq

/-- Concrete non-vacuity witness: a matrix violating the trace condition admits
no instance.  Since `2 cos α ≤ 2 < 3`, the matrix `!![3, 0; 0, 0]` (trace `3`)
is excluded for every `q` — so the class is not satisfied by everything. -/
theorem replacement_excludes_some_matrix (q : ℝ) :
    ¬ (Matrix.trace !![(3 : ℝ), 0; 0, 0] = 2 * Real.cos (eigenphase q)) := by
  have hle : Real.cos (eigenphase q) ≤ 1 := cos_le_one _
  have htr : Matrix.trace !![(3 : ℝ), 0; 0, 0] = 3 := by
    simp [Matrix.trace_fin_two_of]
  rw [htr]
  nlinarith [hle]

end QOU.QBeta.EigenphaseCarrier
