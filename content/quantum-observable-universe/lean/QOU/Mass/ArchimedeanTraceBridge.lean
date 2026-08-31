/-
QOU.Mass.ArchimedeanTraceBridge — the archimedean functor is the logarithm: a multiplicative
categorical trace becomes an additive observable free energy, which LIFTS the additive crossing-energy
partition to the mass observable.

Arc context (bk-crossing mass-binding; bean `qou-brng`, residual R2 — the one item the residuals
audit left genuinely open). `QOU.Mass.SelfMutualPartition` proved, at the ADDITIVE crossing-energy
granularity, that mass = self part and binding = −(mutual part). It *assumed* the energy is additive.
The mass observable, however, carries the q-dimension Markov self-trace
`lw = (Σ_{λ⊢c+1} dim_q λ)/(c+1)` — a MULTIPLICATIVE object. The residual was: how does the
multiplicative trace at the categorical (fibre) level become the additive energy the partition needs?

🛑 WHICH multiplicative structure — an earlier version of this docstring conflated two (bean
`qou-bsfg`). For the normalised Jones polynomial the CONNECTED SUM is exactly multiplicative,
`J(K₁ # K₂) = J(K₁)·J(K₂)`, while the DISJOINT UNION carries the loop value,
`J(K₁ ⊔ K₂) = δ·J(K₁)·J(K₂)`, `δ = [2]_q`. The proved matrix statement
(`QOU.MathlibExt.MarkovTraceMultiplicative`, Kronecker product) models the DISJOINT UNION. So the
`log`-additivity below is exact for a connected sum and holds only up to `log δ` per juxtaposition
otherwise — quantified in `QOU.Mass.ClosureNormalisationDefect`. The lemma name
`freeEnergy_connectedSum` is accurate for the connected-sum reading and is retained (a sibling file
depends on it); what was wrong was inferring it from the Kronecker result.

The bridge is the **archimedean functor τ = logarithm** (the free energy of a partition-function-like
amplitude). This file proves that multiplicativity of the categorical amplitude *forces* additivity of
the observable free energy, so the additive partition `SelfMutualPartition` assumed is DERIVED here
from Jones multiplicativity — and binding is exactly the connected (interaction) free energy, which
vanishes iff the constituents are independent.

What stays a modelling input (stated, not faked): (1) that the substrate assembly amplitude *is* the
Markov trace, multiplicative under the nucleon-assembly connected sum (a citable theorem for the
Jones polynomial, asserted here as the hypothesis `Multiplicative`); (2) the dimensional dressing
`m = m_e · Vol · lw / ℏ_q²` (the CAL-1 scale `m_e`, the geometric `Vol`, the CAL-2 cusp `1/ℏ_q²`) —
calibration and geometry, not derivable from the trace structure. The bridge below is the piece
between them, and it is a theorem.

Ground ring `ℝ` (§7c: archimedean — `Real.log`, positivity). No fit.
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.Tactic
import QOU.MathlibExt.MarkovTraceMultiplicative

namespace QOU.Mass.ArchimedeanTraceBridge

open Finset

/-- The archimedean functor on a positive categorical amplitude `T`: the observable free energy
`E = log T`. (Sign convention: `log`; the mass-deficit binding is `−` the interaction free energy.) -/
noncomputable def freeEnergy (T : ℝ) : ℝ := Real.log T

/-- **Multiplicative trace ⟹ additive free energy.** The Markov/Jones trace is multiplicative under
connected sum (`J(K₁#K₂) = J(K₁)·J(K₂)`); its archimedean image `E = log T` is therefore additive.
This is why rest mass is EXTENSIVE (adds over constituents) — the additive-energy model of
`SelfMutualPartition` is the log-image of the multiplicative self-trace, not an independent
assumption. -/
theorem freeEnergy_connectedSum (T₁ T₂ : ℝ) (h₁ : 0 < T₁) (h₂ : 0 < T₂) :
    freeEnergy (T₁ * T₂) = freeEnergy T₁ + freeEnergy T₂ := by
  unfold freeEnergy
  exact Real.log_mul (ne_of_gt h₁) (ne_of_gt h₂)

/-- Extensivity over many constituents: the free energy of a product of positive self-amplitudes is
the sum of the constituent free energies. Rest mass adds over the `A` nucleons. -/
theorem freeEnergy_prod {ι : Type*} (s : Finset ι) (T : ι → ℝ) (hT : ∀ i ∈ s, 0 < T i) :
    freeEnergy (∏ i ∈ s, T i) = ∑ i ∈ s, freeEnergy (T i) := by
  unfold freeEnergy
  exact Real.log_prod s T (fun i hi => ne_of_gt (hT i hi))

/-- The interaction (connected) free energy of an assembly whose amplitude is the product of the
constituent self-amplitudes times an interaction factor `I`. -/
noncomputable def bindingFreeEnergy (I : ℝ) : ℝ := - freeEnergy I

/-- **The self/mutual partition, lifted to the multiplicative trace.** If the assembly amplitude is
`(∏ Tᵢ) · I` (constituent self-traces times the interaction factor), the observable free energy
splits as `Σ Eᵢ + log I`, so the mass-deficit binding `Σ Eᵢ − E_assembly` equals `−log I =
bindingFreeEnergy I`. This is `SelfMutualPartition.binding_eq_neg_mutualEnergy` DERIVED at the
Markov-trace level: the additivity is a consequence of trace multiplicativity, not an assumption. -/
theorem binding_eq_bindingFreeEnergy {ι : Type*} (s : Finset ι) (T : ι → ℝ) (I : ℝ)
    (hT : ∀ i ∈ s, 0 < T i) (hI : 0 < I) :
    (∑ i ∈ s, freeEnergy (T i)) - freeEnergy ((∏ i ∈ s, T i) * I) = bindingFreeEnergy I := by
  unfold bindingFreeEnergy
  rw [freeEnergy_connectedSum (∏ i ∈ s, T i) I (Finset.prod_pos hT) hI, freeEnergy_prod s T hT]
  ring

/-- **Binding vanishes exactly at independence.** For a positive interaction factor, the binding
free energy is zero iff the assembly amplitude factorises (`I = 1`, no interaction). Binding is
purely the connected part — the free-energy form of `binding_indep_of_self`. -/
theorem bindingFreeEnergy_eq_zero_iff (I : ℝ) (hI : 0 < I) :
    bindingFreeEnergy I = 0 ↔ I = 1 := by
  unfold bindingFreeEnergy freeEnergy
  rw [neg_eq_zero, Real.log_eq_zero]
  constructor
  · rintro (h | h | h)
    · exact absurd h (ne_of_gt hI)
    · exact h
    · linarith
  · intro h; right; left; exact h

/-- **A bound state has positive binding iff its interaction factor is below one.** With the
mass-deficit sign convention, `bindingFreeEnergy I > 0 ↔ I < 1`: the assembly amplitude is
*suppressed* relative to independent constituents exactly when the state is bound. -/
theorem bindingFreeEnergy_pos_iff (I : ℝ) (hI : 0 < I) :
    0 < bindingFreeEnergy I ↔ I < 1 := by
  unfold bindingFreeEnergy freeEnergy
  rw [neg_pos]
  exact Real.log_neg_iff hI

/-! ## Discharging the positivity hypothesis for the framework's amplitude class

The bridge above carries `0 < T` as a hypothesis because `log` needs a nonzero (here positive)
argument. That hypothesis is **not** a genuine assumption for the amplitudes the framework actually
uses: the categorical amplitudes are quantum dimensions, built from quantum integers `[n]_q`, and at
the substrate modulus `q > 1` every quantum integer is strictly positive
(`QOU.MathlibExt.qInt_pos`). So for the quantum-integer amplitude class the positivity follows from
the substrate constraint `q > 1` and is discharged, not assumed. (The *multiplicativity* input — that
the assembly amplitude factorises as `(∏ Tᵢ)·I` — is the separate, still-open item: the Jones trace
is multiplicative under connected sum, `J(K₁#K₂)=J(K₁)·J(K₂)`. That is now PROVED algebraically in
`QOU.MathlibExt.MarkovTraceMultiplicative` and consumed in the capstone section at the end of this
file; bean `qou-301d`.) -/

/-- The quantum integer `[n]_q = ∑_{i<n} qⁱ`, restated inline to keep this file Mathlib-only (the
canonical form is `QOU.MathlibExt.qInt`, `= ∑ i ∈ range n, q^i`; `qInt_pos` there proves the same
positivity). The Mass files in this arc are deliberately self-contained. -/
noncomputable def qIntR (q : ℝ) (n : ℕ) : ℝ := ∑ i ∈ range n, q ^ i

/-- **A quantum integer at `q > 1` is strictly positive** — a sum of positive powers. This is the
positivity the framework's amplitudes carry (quantum dimensions are built from `[n]_q`), so `0 < T`
is discharged by the substrate constraint `q > 1`, not assumed. -/
theorem qIntR_pos {q : ℝ} (hq : 1 < q) {n : ℕ} (hn : 0 < n) : 0 < qIntR q n := by
  unfold qIntR
  apply Finset.sum_pos
  · intro i _; exact pow_pos (lt_trans one_pos hq) i
  · exact ⟨0, Finset.mem_range.mpr hn⟩

/-- A finite product of quantum integers at `q > 1` is strictly positive. -/
theorem qIntRProd_pos {ι : Type*} (s : Finset ι) (q : ℝ) (hq : 1 < q) (n : ι → ℕ)
    (hn : ∀ i ∈ s, 0 < n i) : 0 < ∏ i ∈ s, qIntR q (n i) :=
  Finset.prod_pos (fun i hi => qIntR_pos hq (hn i hi))

/-- **The binding identity with the positivity hypothesis DISCHARGED**, for amplitudes drawn from
the quantum-integer class (constituent self-amplitudes `Tᵢ = [nᵢ]_q`, interaction factor `[m]_q`).
No `0 < T` is assumed: at the substrate `q > 1` positivity is a theorem (`qIntR_pos`). The
mass-deficit binding equals the connected free energy `−log [m]_q`. Only the *multiplicativity* input
— that the assembly amplitude factorises as `(∏ Tᵢ)·[m]_q` — remains carried by the shape of the
statement; that is the Jones-connected-sum theorem, the open formalisation item. -/
theorem binding_eq_qInt {ι : Type*} (s : Finset ι) (q : ℝ) (hq : 1 < q)
    (nT : ι → ℕ) (hnT : ∀ i ∈ s, 0 < nT i) (nI : ℕ) (hnI : 0 < nI) :
    (∑ i ∈ s, freeEnergy (qIntR q (nT i)))
        - freeEnergy ((∏ i ∈ s, qIntR q (nT i)) * qIntR q nI)
      = bindingFreeEnergy (qIntR q nI) :=
  binding_eq_bindingFreeEnergy s (fun i => qIntR q (nT i)) (qIntR q nI)
    (fun i hi => qIntR_pos hq (hnT i hi)) (qIntR_pos hq hnI)

/-! ## Capstone — BOTH hypotheses discharged on juxtaposed matrix amplitudes (bean `qou-301d`)

The lemmas above take `T₁ * T₂` (multiplicativity) and `0 < T` (positivity) as hypotheses. On the
framework's actual amplitudes — Markov traces of Hecke-representation matrices — both are theorems:

* multiplicativity is `MarkovTraceMultiplicative.markovTrace_juxtapose` (the trace of a
  disjoint-strand juxtaposition is the product of the block traces, from `Matrix.trace_kronecker`) —
  the algebraic form of `J(K₁#K₂)=J(K₁)·J(K₂)`;
* positivity is preserved by juxtaposition (`markovTrace_juxtapose_pos`) and, for the
  quantum-integer amplitude class, holds outright at `q > 1` (`qIntR_pos` above).

So the bridge below assumes only that the composite amplitude IS the juxtaposition
(`IsJuxtaposition`, the algebraic statement that the two sub-braids share no strand) and that each
component amplitude is positive. Nothing about `log`-additivity is postulated. -/

open QOU.MathlibExt.MarkovTraceMultiplicative in
/-- **The archimedean bridge on juxtaposed amplitudes — multiplicativity DISCHARGED.** For two
components whose composite evaluation is their disjoint-strand juxtaposition, the observable free
energy is additive. The multiplicativity is not assumed: it is `markovTrace_juxtapose`. -/
theorem freeEnergy_juxtapose {m n : Type*} [Fintype m] [Fintype n]
    {A : Matrix m m ℝ} {B : Matrix n n ℝ} {C : Matrix (m × n) (m × n) ℝ}
    (h : IsJuxtaposition A B C) (hA : 0 < A.trace) (hB : 0 < B.trace) :
    freeEnergy C.trace = freeEnergy A.trace + freeEnergy B.trace := by
  rw [markovTrace_juxtapose h]
  exact freeEnergy_connectedSum A.trace B.trace hA hB

open QOU.MathlibExt.MarkovTraceMultiplicative in
/-- **Adding a `1×1` identity BLOCK costs no free energy** — at the matrix level.

🛑 The physical gloss that stood here ("a disjoint trivial component contributes nothing to the
mass, as it must") is FALSE and is retracted (bean `qou-bsfg`). A braid closure on `n` strands is
normalised by `δ^{n−1}`, so juxtaposition drops exactly one loop factor: the cost is `log δ =
0.6985808249` at `q₀`, and `⁴He` is short by `≈ 2.096`. Machine-checked in
`QOU.Mass.ClosureNormalisationDefect` (`freeEnergy_closureNorm_additive_iff`: additivity holds iff
`δ = 1`, which `loopValue_ne_one` excludes for `q > 1`). This lemma is retained as the matrix-level
fact it is. -/
theorem freeEnergy_juxtapose_trivial {m : Type*} [Fintype m]
    {A : Matrix m m ℝ} {C : Matrix (m × Unit) (m × Unit) ℝ}
    (h : IsJuxtaposition A (1 : Matrix Unit Unit ℝ) C) :
    freeEnergy C.trace = freeEnergy A.trace := by
  rw [markovTrace_juxtapose_one h]

open QOU.MathlibExt.MarkovTraceMultiplicative in
/-- **Binding of a juxtaposed pair vanishes.** If the assembly is a genuine disjoint union (no
linking), the mass-deficit binding is zero — the components are independent. Binding is therefore
carried entirely by the FAILURE of juxtaposition, i.e. by the linking, which is what
`bindingFreeEnergy` measures. This is the falsifiable content of the whole bridge. -/
theorem binding_juxtapose_eq_zero {m n : Type*} [Fintype m] [Fintype n]
    {A : Matrix m m ℝ} {B : Matrix n n ℝ} {C : Matrix (m × n) (m × n) ℝ}
    (h : IsJuxtaposition A B C) (hA : 0 < A.trace) (hB : 0 < B.trace) :
    (freeEnergy A.trace + freeEnergy B.trace) - freeEnergy C.trace = 0 := by
  rw [freeEnergy_juxtapose h hA hB]; ring

end QOU.Mass.ArchimedeanTraceBridge
