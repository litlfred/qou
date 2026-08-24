import QOU.MathlibExt.QPartitionCombinatorics
import QOU.Mathlib.SYTEnumerationFintype

/-!
# QOU.MathlibExt.MolienFakeDegree — the correct q-analogue of `Σ_λ (f^λ)² = n!`

Lean side of `docs/audits/2026-08-21-molien-mining-the-correct-q-analogue-of-rsk.md`,
and the companion to `QOU.MathlibExt.QPlancherel`.

## What this establishes

For `n = 2, 3, 4`, in the **balanced** convention this corpus already uses
(`qBracket q m = (q^m − q^{-m})/(q − q^{-1})`):

```text
  Σ_{λ ⊢ n}  f^λ · q^{−κ_λ} · qDim q λ  =  qFactorial q n
```

`f^λ` is the **classical** number of standard Young tableaux, `κ_λ = Σ_x c(x)` is the
content statistic, and `qDim` is the corpus's own q-hook-length dimension. In the
standard convention this is the textbook identity `Σ_λ f^λ R_λ(q) = [n]_q!` with
`R_λ(q) = q^{n(λ)} d_q(λ)` the **fake degree** — the graded multiplicity of `V_λ` in
the coinvariant algebra, whose Poincaré polynomial is `[n]_q!` for `S_n`.

**The contrast is proved too.** `sum_qDim_sq_ne_qFactorial_n3_at_two` shows
`Σ_λ qDim q λ ² ≠ qFactorial q n`, which is the whole of the `Z(n)` defect measured
in `docs/audits/2026-06-20-keystone-wlambda-Z-defect-n-scaling.md`. The classical
identity has TWO factors of `f^λ`; the graded identity deforms exactly ONE of them
into the graded multiplicity and leaves the other classical, whereas `Σ qDim²`
deforms both and squares. They agree only at `q = 1`. Having both proved here — same
`n`, same convention, same hook data — is what makes the identities non-vacuous.

## Deliberately reusing the corpus's definitions

Everything is stated in terms of `QPartitionCombinatorics.qDim`, `qFactorial`,
`qBracket` and `Partition.hookLength`. An earlier draft of this file introduced its
own `balQInt`/`balQFact`; that was discarded on finding `qBracket` is *definitionally
the same object*. A second q-bracket in the corpus would be exactly the divergence
surface bean `qou-m7py` removed from the Rust engine.

The `qDim_*` bridge lemmas hold by `rfl`: `qDim` on a concrete partition reduces
definitionally to `qFactorial / ∏_cells qBracket (hookLength …)`.

## Scope — read before extending

These are the **concrete cases `n ≤ 4`**, kernel-checked. The general-`n` statement is
not here. Mathlib as of `v4.24.0` has `YoungDiagram` and `Nat.Partition` but no hook lengths,
tableaux, or hook-length formula (probed by name, all absent). **The corpus supplies
all three of the combinatorial ingredients**, which an earlier draft of this note
wrongly listed as missing: `Partition.hookLength` and `qDim` in
`QPartitionCombinatorics`, and `#SYT` in `QOU.Mathlib.SYTEnum` — `numSYTenum` is
kernel-computable (the `numSYT_*` lemmas below are `by decide`) and is bridged to the
structure-level count by `numSYTenum_eq_numStandardYoungTableaux`.

So the genuinely missing piece for a general-`n` proof is narrower than "hook-length
theory": it is the **graded decomposition of the coinvariant algebra**
(Chevalley/Steinberg) plus an induction over `Finset`-many partitions. Tracked as
bean `qou-3quc` rather than faked with a `sorry`.

The identity is standard (Chevalley/Steinberg + fake degrees); what is corpus-new is
the diagnosis that `Σ qDim²` is the wrong q-analogue.

Note `qDim` is `ℝ`-specialised upstream although it is purely algebraic (AGENTS.md
§7c); these statements inherit that and are over `ℝ` for that reason alone.
-/

namespace QOU.MathlibExt.MolienFakeDegree
open QOU.MathlibExt.QPartitionCombinatorics
open QOU.Mathlib.SYTEnum

/-! ### Bridge lemmas: `qDim` on concrete partitions, by `rfl` -/

@[simp] theorem qDim_2 (q : ℝ) :
    qDim q [2] = qFactorial q 2 / (1 * (1 * qBracket q 2 * qBracket q 1)) := rfl

@[simp] theorem qDim_1_1 (q : ℝ) :
    qDim q [1, 1] = qFactorial q 2 / (1 * (1 * qBracket q 2) * (1 * qBracket q 1)) := rfl

@[simp] theorem qDim_3 (q : ℝ) :
    qDim q [3] = qFactorial q 3 / (1 * (1 * qBracket q 3 * qBracket q 2 * qBracket q 1)) := rfl

@[simp] theorem qDim_2_1 (q : ℝ) :
    qDim q [2, 1] = qFactorial q 3 / (1 * (1 * qBracket q 3 * qBracket q 1) * (1 * qBracket q 1)) := rfl

@[simp] theorem qDim_1_1_1 (q : ℝ) :
    qDim q [1, 1, 1] = qFactorial q 3 / (1 * (1 * qBracket q 3) * (1 * qBracket q 2) * (1 * qBracket q 1)) := rfl

@[simp] theorem qDim_4 (q : ℝ) :
    qDim q [4] = qFactorial q 4 / (1 * (1 * qBracket q 4 * qBracket q 3 * qBracket q 2 * qBracket q 1)) := rfl

@[simp] theorem qDim_3_1 (q : ℝ) :
    qDim q [3, 1] = qFactorial q 4 / (1 * (1 * qBracket q 4 * qBracket q 2 * qBracket q 1) * (1 * qBracket q 1)) := rfl

@[simp] theorem qDim_2_2 (q : ℝ) :
    qDim q [2, 2] = qFactorial q 4 / (1 * (1 * qBracket q 3 * qBracket q 2) * (1 * qBracket q 2 * qBracket q 1)) := rfl

@[simp] theorem qDim_2_1_1 (q : ℝ) :
    qDim q [2, 1, 1] = qFactorial q 4 / (1 * (1 * qBracket q 4 * qBracket q 1) * (1 * qBracket q 2) * (1 * qBracket q 1)) := rfl

@[simp] theorem qDim_1_1_1_1 (q : ℝ) :
    qDim q [1, 1, 1, 1] = qFactorial q 4 / (1 * (1 * qBracket q 4) * (1 * qBracket q 3) * (1 * qBracket q 2) * (1 * qBracket q 1)) := rfl

/-! ### The SYT counts, COMPUTED by the kernel

`f^lam` is not typed in as a literal below: `numSYTenum` enumerates the standard
Young tableaux and `decide` evaluates it, so a mis-counted `f^lam` cannot silently
produce a true theorem about a wrong coefficient. `numSYTenum` is bridged to the
structure-level count by `numSYTenum_eq_numStandardYoungTableaux` upstream. -/

@[simp] theorem numSYT_2 : numSYTenum [2] = 1 := by decide

@[simp] theorem numSYT_1_1 : numSYTenum [1, 1] = 1 := by decide

@[simp] theorem numSYT_3 : numSYTenum [3] = 1 := by decide

@[simp] theorem numSYT_2_1 : numSYTenum [2, 1] = 2 := by decide

@[simp] theorem numSYT_1_1_1 : numSYTenum [1, 1, 1] = 1 := by decide

@[simp] theorem numSYT_4 : numSYTenum [4] = 1 := by decide

@[simp] theorem numSYT_3_1 : numSYTenum [3, 1] = 3 := by decide

@[simp] theorem numSYT_2_2 : numSYTenum [2, 2] = 2 := by decide

@[simp] theorem numSYT_2_1_1 : numSYTenum [2, 1, 1] = 3 := by decide

@[simp] theorem numSYT_1_1_1_1 : numSYTenum [1, 1, 1, 1] = 1 := by decide

/-! ### The identity -/

/-- **Molien / fake-degree q-analogue at `n = 2`** (2 partitions).

    `f^lam` is the kernel-computed `numSYTenum`, not a typed literal. -/
theorem molien_qanalogue_n2 (q : ℝ) (hq : q ≠ 0) (h2 : q ^ 2 - 1 ≠ (0:ℝ)) (h4 : q ^ 4 - 1 ≠ (0:ℝ)) :

      (numSYTenum [2] : ℝ) * (q⁻¹ ^ 1) * qDim q [2] +
      (numSYTenum [1, 1] : ℝ) * (q ^ 1) * qDim q [1, 1]
      = qFactorial q 2 := by
  simp only [qDim_2, qDim_1_1, numSYT_2, numSYT_1_1, qFactorial]
  norm_num [qBracket]
  field_simp
  ring

/-- **Molien / fake-degree q-analogue at `n = 3`** (3 partitions).

    `f^lam` is the kernel-computed `numSYTenum`, not a typed literal. -/
theorem molien_qanalogue_n3 (q : ℝ) (hq : q ≠ 0) (h2 : q ^ 2 - 1 ≠ (0:ℝ)) (h4 : q ^ 4 - 1 ≠ (0:ℝ)) (h6 : q ^ 6 - 1 ≠ (0:ℝ)) :

      (numSYTenum [3] : ℝ) * (q⁻¹ ^ 3) * qDim q [3] +
      (numSYTenum [2, 1] : ℝ) * (1) * qDim q [2, 1] +
      (numSYTenum [1, 1, 1] : ℝ) * (q ^ 3) * qDim q [1, 1, 1]
      = qFactorial q 3 := by
  simp only [qDim_3, qDim_2_1, qDim_1_1_1, numSYT_3, numSYT_2_1, numSYT_1_1_1, qFactorial]
  norm_num [qBracket]
  field_simp
  ring

/-- **Molien / fake-degree q-analogue at `n = 4`** (5 partitions).

    `f^lam` is the kernel-computed `numSYTenum`, not a typed literal. -/
theorem molien_qanalogue_n4 (q : ℝ) (hq : q ≠ 0) (h2 : q ^ 2 - 1 ≠ (0:ℝ)) (h4 : q ^ 4 - 1 ≠ (0:ℝ)) (h6 : q ^ 6 - 1 ≠ (0:ℝ)) (h8 : q ^ 8 - 1 ≠ (0:ℝ)) :

      (numSYTenum [4] : ℝ) * (q⁻¹ ^ 6) * qDim q [4] +
      (numSYTenum [3, 1] : ℝ) * (q⁻¹ ^ 2) * qDim q [3, 1] +
      (numSYTenum [2, 2] : ℝ) * (1) * qDim q [2, 2] +
      (numSYTenum [2, 1, 1] : ℝ) * (q ^ 2) * qDim q [2, 1, 1] +
      (numSYTenum [1, 1, 1, 1] : ℝ) * (q ^ 6) * qDim q [1, 1, 1, 1]
      = qFactorial q 4 := by
  simp only [qDim_4, qDim_3_1, qDim_2_2, qDim_2_1_1, qDim_1_1_1_1, numSYT_4, numSYT_3_1, numSYT_2_2, numSYT_2_1_1, numSYT_1_1_1_1, qFactorial]
  norm_num [qBracket]
  field_simp
  ring


/-! ### The contrast: the corpus's `Σ qDim²` is NOT the q-factorial -/

/-- **The `Z(n) ≠ 1` defect, in its smallest exact form.** At `n = 3`, `q = 2`:

      Σ_λ qDim q λ ²  =  33/4        while        qFactorial q 3  =  105/8.

    Together with `molien_qanalogue_n3` — same `n`, same convention, same hook data —
    this shows the two sums are genuinely different objects, so the identities above
    are not vacuous. -/
theorem sum_qDim_sq_ne_qFactorial_n3_at_two :
    qDim (2:ℝ) [3] ^ 2 + qDim (2:ℝ) [2, 1] ^ 2 + qDim (2:ℝ) [1, 1, 1] ^ 2
      ≠ qFactorial (2:ℝ) 3 := by
  simp only [qDim_3, qDim_2_1, qDim_1_1_1, qFactorial]
  norm_num [qBracket]

end QOU.MathlibExt.MolienFakeDegree
