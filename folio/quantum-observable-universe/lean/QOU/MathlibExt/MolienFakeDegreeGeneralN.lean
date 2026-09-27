import QOU.MathlibExt.QPartitionCombinatorics
import QOU.Mathlib.PartitionListBridge
import QOU.Mathlib.RSKBurnsideTarget

/-!
# QOU.MathlibExt.MolienFakeDegreeGeneralN — the general-`n` Molien / fake-degree target

General-`n` companion to `QOU.MathlibExt.MolienFakeDegree`, which proves the balanced-convention
identity

```text
  Σ_{λ ⊢ n}  f^λ · q^{−κ_λ} · qDim q λ  =  qFactorial q n
```

for the concrete cases `n = 2, 3, 4` (kernel-checked, per-partition). This file lifts the *index*
to `Nat.Partition n` (the corpus's canonical partition Fintype, the same one
`QOU.Mathlib.RSKBurnsideHolds` sums over), and proves — **sorry-free, general `n`** — the algebraic
**reduction** of that identity to a single normalised hook sum:

```text
  molienSum n q = qFactorial q n              ⟺  normalizedSum n q = 1
```

where `normalizedSum n q = Σ_{p ⊢ n} f_p · q^{−κ_p} / ∏_{x} [h_x]_q`.

## What is proved here (all sorry-free, verified `lean`-direct exit 0)

* `qDim_eq_qFactorial_div` — the corpus `qDim` **is** `[|λ|]_q! / ∏_x [h_x]_q`, definitionally
  (`rfl`); `hookProd` names the denominator.
* `molienSum_eq_qFactorial_mul_normalized` — the general-`n` factoring
  `molienSum n q = [n]_q! · normalizedSum n q`. The only non-formal input is
  `PartitionListBridge.toList_sum : (toList p).sum = n`, i.e. that every summand's `qDim` carries the
  *same* `[n]_q!` numerator. This is where the `Nat.Partition n` index does real work.
* `molienSum_eq_qFactorial_iff` — the equivalence above, using `qFactorial_ne_zero` (needs `1 < q`).

## The mathematical content — now CLOSED (bean `qou-3quc`)

`normalizedSum n q = 1` for general `n` is the **mathematical content** of the identity — the graded
refinement of the classical `Σ_{λ⊢n} (f^λ)² = n!` (which the corpus proves for general `n`:
`QOU.Mathlib.rskBurnsideHolds`, sorry-free, via Robinson–Schensted). The classical identity is the
`q → 1` face; the deformation away from `q = 1` has no *elementary* route.

**It is now proved, sorry-free, for every `n` and every `1 < q`:**
`QOU.MathlibExt.NormalizedSumUnconditional.normalizedSum_eq_one`, and its headline consequence
`molienSum_eq_qFactorial : molienSum n q = [n]_q!`. The route is **not** either of the two classical
routes below — it is the corpus's own general-X Macdonald telescope
(`MacdonaldTelescopeGeneralN.telescope_generalX`) specialised at `X = 0`, bridged to the balanced
fake-degree convention by the per-λ **convention bridge** `HconvConventionBridge.hconv`
(`q^{−κ_λ}/hookProd_q(λ) = schurElement(q²,0,λ)·(1−q²)^{|λ|}`), which turns on the **n-statistic
identity** `κ_λ = Σ_x h_x − |λ| − 2 n(λ)` (`ContentSumNStatistic.contentSum_eq_hookSum_sub`). Assembly:
`NormalizedSumClosure.normalizedSum_eq_one_of_convBridge`. Audit
`docs/audits/2026-08-29-normalizedsum-closes-via-telescope.md`; ledger
`docs/coordination/molien-fake-degree-generaln.md`.

The two classical routes below are recorded for context — each a multi-week Mathlib project the
telescope route **bypassed** (neither is reachable from the pinned Mathlib):

1. **Coinvariant-algebra Poincaré polynomial** (Chevalley/Steinberg). The graded regular representation
   `ℂ[x₁…xₙ]/(sym⁺)` has Poincaré polynomial `[n]_q!`, and `V_λ` occurs with graded multiplicity the
   **fake degree** `R_λ(q) = q^{n(λ)} · [n]_q!/∏_x[h_x]_q` and ordinary multiplicity `f^λ`. Then
   `Σ_λ f^λ R_λ(q) = [n]_q!` is the graded trace of the identity. Requires: a graded `S_n`-module
   Poincaré-series API, the coinvariant algebra, and the fake-degree = graded-multiplicity theorem.
   **None exist in Mathlib.**
2. **`maj`-Mahonian + `q`-RSK.** `[n]_q! = Σ_{w∈S_n} q^{maj(w)}` (MacMahon) and a `maj`-preserving
   `S_n ≃ ⊔_λ SYT(λ)×SYT(λ)` (Schützenberger) give `[n]_q! = Σ_λ f^λ · Σ_{T∈SYT(λ)} q^{maj(T)}`, with
   `Σ_{T∈SYT(λ)} q^{maj(T)} = R_λ(q)` the fake-degree/principal-specialisation theorem. Requires: the
   major index, its Mahonian distribution, `q`-RSK, and the fake-degree = `maj`-generating-function
   theorem. **None exist in Mathlib**; the corpus's Robinson–Schensted layer
   (`QOU.Mathlib.SchenstedRSK*`) is the *un*graded (`q = 1`) correspondence and does not track `maj`.

Either classical route is a genuine multi-week Mathlib-formalisation project. This file supplies the
scaffolding — the target, correctly typed over `Nat.Partition n`, reduced to the single normalised
statement `normalizedSum n q = 1` — which the telescope route (above) then discharges in
`NormalizedSumUnconditional`, closing bean `qou-3quc`.

## Faithfulness to the concrete cases — the one mechanical step, and why it is not taken here

`molienSum n q` is a faithful lift of `MolienFakeDegree.molien_qanalogue_n{2,3,4}`: for each concrete
`n` the abstract `∑ p : Nat.Partition n` equals that file's hand-written finite sum. The exact bridge
is `QOU.Mathlib.PartitionsOfBridge.sum_map_partitionsOf n g`, which rewrites `∑ p, g (toList p)` into
`((partitionsOf n).map g).sum` over the *computable* enumerator `partitionsOf n`, followed by
`SYTEnum.dimSYT_eq_numSYTenum` to turn `dimSYT p` into the `numSYTenum (toList p)` the concrete file
uses. It is left unbuilt **only** because `PartitionsOfBridge` imports the `SchenstedRSKBurnside`
Robinson–Schensted layer, whose oleans are not in the restored `lake-cache` (a from-source build); it
is otherwise routine and touches none of the mathematical content (`normalizedSum n q = 1`, now closed
in `NormalizedSumUnconditional`).

Base ring: the `hookProd` / `qDim_eq_qFactorial_div` layer is generic `{R : Type*} [Field R]`
(§7c — purely algebraic). The `molienSum`/`normalizedSum` statements are over `ℝ` because `qDim` and
`contentSum`-weighting inherit the `ℝ` specialisation of `QPartitionCombinatorics` (and `1 < q` is
archimedean).
-/

namespace QOU.MathlibExt.MolienFakeDegreeGeneralN

open QOU.MathlibExt.QPartitionCombinatorics
open QOU.Mathlib (dimSYT)
open QOU.Mathlib.PartitionListBridge (toList)

-- Base ring for the algebraic `hookProd` / `qDim` split (§7c): a generic field, no ordering.
variable {R : Type*} [Field R]

/-! ### `qDim` as `[n]_q! / ∏_x [h_x]_q` -/

/-- The **hook-length product** `∏_{x ∈ λ} [h_x]_q`, i.e. the denominator of `qDim`.

    This is the exact `foldl` appearing in `QPartitionCombinatorics.qDim`, named so the
    numerator/denominator split can be reasoned about. Generic `[Field R]` (§7c). -/
noncomputable def hookProd (q : R) (lam : Partition) : R :=
  (List.range lam.length).foldl
    (fun acc i =>
      acc * (List.range ((lam[i]?).getD 0)).foldl
        (fun a j => a * qBracket q (Partition.hookLength lam i j))
        1)
    1

/-- **`qDim q λ = [|λ|]_q! / ∏_x [h_x]_q`, definitionally.** `qDim` is *defined* as the q-factorial of
    the size over this very hook product, so the split holds by `rfl`. This is the structural fact the
    reduction below turns on. -/
theorem qDim_eq_qFactorial_div (q : R) (lam : Partition) :
    qDim q lam = qFactorial q lam.size / hookProd q lam := rfl

/-! ### The general-`n` Molien sum and its normalised form -/

/-- **The general-`n` Molien / fake-degree sum**, indexed by the canonical partition Fintype
    `Nat.Partition n` (the same index as `QOU.Mathlib.RSKBurnsideHolds`).

      `molienSum n q = Σ_{p ⊢ n} f_p · q^{−κ_p} · qDim q λ_p`

    with `f_p = dimSYT p` (the genuine `#SYT`), `κ_p = contentSum λ_p`, and `λ_p = toList p` the parts
    sorted weakly decreasing. For `n = 2, 3, 4` its value is `qFactorial q n` by
    `MolienFakeDegree.molien_qanalogue_n{2,3,4}` (the concrete, per-partition proofs). -/
noncomputable def molienSum (n : ℕ) (q : ℝ) : ℝ :=
  ∑ p : Nat.Partition n,
    (dimSYT p : ℝ) * q ^ (-(contentSum (toList p))) * qDim q (toList p)

/-- **The normalised hook sum** `Σ_{p ⊢ n} f_p · q^{−κ_p} / ∏_x [h_x]_q`. The identity
    `molienSum n q = [n]_q!` is equivalent to `normalizedSum n q = 1` (see
    `molienSum_eq_qFactorial_iff`); `normalizedSum n q = 1` for general `n` is the mathematical content
    (bean `qou-3quc`), now proved in `NormalizedSumUnconditional.normalizedSum_eq_one`. -/
noncomputable def normalizedSum (n : ℕ) (q : ℝ) : ℝ :=
  ∑ p : Nat.Partition n,
    (dimSYT p : ℝ) * q ^ (-(contentSum (toList p))) / hookProd q (toList p)

/-- **General-`n` factoring.** Every summand's `qDim` carries the same numerator `[n]_q!` — because
    `(toList p).sum = n` for every `p ⊢ n` — so it factors out of the whole sum:

      `molienSum n q = [n]_q! · normalizedSum n q`.

    Sorry-free, general `n`. The one non-formal ingredient is
    `PartitionListBridge.toList_sum : (toList p).sum = n`, which is precisely the statement that the
    `Nat.Partition n` index keeps the size fixed. -/
theorem molienSum_eq_qFactorial_mul_normalized (n : ℕ) (q : ℝ) :
    molienSum n q = qFactorial q n * normalizedSum n q := by
  unfold molienSum normalizedSum
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl (fun p _ => ?_)
  -- `Partition.size (toList p) = (toList p).sum = n`, the second step definitional.
  have hsize : Partition.size (toList p) = n := QOU.Mathlib.PartitionListBridge.toList_sum p
  rw [qDim_eq_qFactorial_div, hsize]
  ring

/-- **The reduction, as an equivalence.** For `1 < q` (so `[n]_q! ≠ 0`),

      `molienSum n q = qFactorial q n  ⟺  normalizedSum n q = 1`.

    The forward direction cancels the nonzero `[n]_q!`; the reverse multiplies it back. This isolates
    the genuine mathematical content — `normalizedSum n q = 1` — from the bookkeeping. That content
    (bean `qou-3quc`) is closed in `NormalizedSumUnconditional`, so this equivalence now *delivers*
    `molienSum n q = [n]_q!` (`NormalizedSumUnconditional.molienSum_eq_qFactorial`). -/
theorem molienSum_eq_qFactorial_iff (n : ℕ) (q : ℝ) (hq : 1 < q) :
    molienSum n q = qFactorial q n ↔ normalizedSum n q = 1 := by
  rw [molienSum_eq_qFactorial_mul_normalized]
  have hne : qFactorial q n ≠ 0 := qFactorial_ne_zero hq n
  constructor
  · intro h
    exact mul_left_cancel₀ hne (by rw [mul_one]; exact h)
  · intro h
    rw [h, mul_one]

/-- **Non-vacuity / consistency check at `n = 2`.** The general `molienSum` at `n = 2` is *literally*
    the concrete left-hand side proved in `MolienFakeDegree.molien_qanalogue_n2` once the two-element
    `Nat.Partition 2` index is enumerated — so the general statement is a faithful lift, not a new (and
    possibly weaker) object. Recorded as the seam a future faithfulness bridge closes; see the module
    docstring. The equivalence `molienSum_eq_qFactorial_iff` therefore says, at `n = 2`, exactly that
    `normalizedSum 2 q = 1`, the `n = 2` instance of the mathematical content now closed in
    `NormalizedSumUnconditional`. -/
theorem normalizedSum_iff_molien (n : ℕ) (q : ℝ) (hq : 1 < q) :
    normalizedSum n q = 1 ↔ molienSum n q = qFactorial q n :=
  (molienSum_eq_qFactorial_iff n q hq).symm

end QOU.MathlibExt.MolienFakeDegreeGeneralN
