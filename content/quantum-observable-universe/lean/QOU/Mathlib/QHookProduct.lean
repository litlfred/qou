import QOU.Mathlib.HookLengthFormula
import QOU.BraidKnot.wedderburn_trace_identity

/-!
# QOU.Mathlib.QHookProduct — the general-`n` q-hook product and its `q=1` specialization

The physical Wedderburn / Markov-trace dimension entering `tr_M = Σ_λ y_λ χ_λ` is the
**q-deformed** hook dimension `dim_q(λ) = [n]_q!/∏_c [hook(c)]_q`. This file gives the
general-`n` q-hook product `∏_c [hook(c)]_q` (q-analogue of
`HookLengthFormula.hookLengthProduct`, over the corpus Gaussian q-integer
`QOU.BraidKnot.qInt q k = ∑_{i<k} q^i`) and proves that at `q = 1` it recovers the classical
hook product — so the **machine-checked classical Frame–Robinson–Thrall HLF**
(`numStandardYoungTableaux_mul_hookLengthProduct`, #4041) is exactly the `q=1` specialization
of the q-hook identity.

This unifies the two threads: the concrete-cohort q-dimensions of
`QOU.Mathlib.WenzlBridgeConcrete` (physical `q > 1`, n ≤ 8/10) and the general-`n` classical
HLF (all `n`), via the shared q-integer convention. The general-`n` q-HLF as a
rep-theoretic identity (`dim_q(λ) = ` generic degree at every `q`) is a larger build tracked
separately; the cohort cases already cover the physical range.

Pure algebra over a generic `[Field R]`; the `q=1` evaluation is not archimedean.
-/

open YoungDiagram
open scoped BigOperators

namespace QOU.Mathlib

variable {R : Type*} [Field R]

/-- **The q-hook product** `∏_{c∈μ} [hook(c)]_q` — q-analogue of `hookLengthProduct`, over the
    corpus Gaussian q-integer `[k]_q = ∑_{i<k} q^i` (`QOU.BraidKnot.qInt`). -/
noncomputable def qHookLengthProduct (μ : YoungDiagram) (q : R) : R :=
  ∏ c ∈ μ.cells, QOU.BraidKnot.qInt q (μ.hookLength c.1 c.2)

/-- The Gaussian q-integer at `q = 1` is the plain integer: `[k]_1 = k`. -/
theorem qInt_one (k : ℕ) : QOU.BraidKnot.qInt (1 : R) k = (k : R) := by
  unfold QOU.BraidKnot.qInt
  simp

/-- **q-hook product at `q = 1` = classical hook product** (cast to `R`). -/
theorem qHookLengthProduct_one (μ : YoungDiagram) :
    qHookLengthProduct μ (1 : R) = (μ.hookLengthProduct : R) := by
  unfold qHookLengthProduct YoungDiagram.hookLengthProduct
  rw [Nat.cast_prod]
  exact Finset.prod_congr rfl (fun c _ => qInt_one _)

/-- **q-factorial at `q = 1` = `n!`** (cast to `R`). -/
theorem qFactorial_one (n : ℕ) :
    QOU.BraidKnot.qFactorial (1 : R) n = (n.factorial : R) := by
  unfold QOU.BraidKnot.qFactorial
  rw [show (∏ k ∈ Finset.range n, QOU.BraidKnot.qInt (1 : R) (k + 1))
        = ∏ k ∈ Finset.range n, ((k + 1 : ℕ) : R) from
      Finset.prod_congr rfl (fun k _ => qInt_one _),
    ← Nat.cast_prod, Finset.prod_range_add_one_eq_factorial]

/-- **The classical HLF is the `q = 1` specialization of the q-hook identity.** The general-`n`
    q-hook product at `q = 1`, times the genuine standard-tableau count `#SYT(μ)`, equals
    `[n]_q!|_{q=1} = n!` — i.e. the machine-checked classical Frame–Robinson–Thrall HLF
    (`numStandardYoungTableaux_mul_hookLengthProduct`, #4041) *is* the `q → 1` limit of the
    q-hook identity `dim_q(μ)·∏[hook]_q = [n]_q!`. Over any `[Field R]`. -/
theorem qHookLengthProduct_one_mul_num (μ : YoungDiagram) :
    qHookLengthProduct μ (1 : R) * (numStandardYoungTableaux μ : R)
      = QOU.BraidKnot.qFactorial (1 : R) μ.cells.card := by
  rw [qHookLengthProduct_one, qFactorial_one, mul_comm, ← Nat.cast_mul,
    numStandardYoungTableaux_mul_hookLengthProduct]

end QOU.Mathlib
