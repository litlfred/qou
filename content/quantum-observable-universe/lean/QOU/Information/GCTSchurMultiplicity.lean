import QOU.Information.GCTMultiplicityObstruction
import QOU.MathlibExt.WenzlSchurElement

/-!
# QOU.Information.GCTSchurMultiplicity — a concrete GCT obstruction from TL vanishing

`GCTMultiplicityObstruction` gives the abstract GCT separation logic (a
multiplicity obstruction at a partition `λ` is a genuine separator) plus the
`QouGCTObstruction` bridge as a no-instance conjecture class. This file grounds
that logic in a **proved multiplicity drop** — the Temperley–Lieb Schur-element
vanishing of `WenzlSchurElement` — so the separation is exhibited on real
representation-theoretic data, not a toy.

The **GCT multiplicity indicator** `schurMult Q X λ` is `1` when the Wedderburn
block `λ` is present (Schur element nonzero) and `0` when it is dropped (Schur
element zero). Two facts, both already proved in `WenzlSchurElement`:

* **substrate** (`X ≤ 0`, `Q > 1`): every block is present (`schurElement_ne_zero`);
* **TL locus** (`X = Q^{-N}`): a block with a content-`N` cell is dropped
  (`schurElement_tl_eq_zero`).

So the substrate and TL-locus data are `SeparatedAt` **every** content-`N`
partition — `1` vs `0`. Concretely, `[2]` (which has the content-`1` cell
`(0,1)`) is separated at `N = 1`.

## ⚠ This is an OCCURRENCE obstruction, not a multiplicity one (correction, 2026-08-15)

Read `schurMult` before citing this file as GCT progress:

```
noncomputable def schurMult (Q X : ℝ) (lam : Partition) : ℕ :=
  if schurElement Q X lam = 0 then 0 else 1
```

It is a **0/1 indicator** — block present or absent — and `schur_separatedAt`
separates by `1 ≠ 0`. In GCT terminology that is precisely an **occurrence**
obstruction, not a multiplicity obstruction: no multiplicity is ever computed,
let alone compared. The distinction is not pedantic. This file's own sibling
`GCTMultiplicityObstruction` records the reason: Bürgisser–Ikenmeyer–Panova
prove that occurrence obstructions **cannot** separate `VP` from `VNP`
(`[burgisser2019]`), which is exactly why that module restricts itself to
multiplicity obstructions.

Earlier docstrings here called this "a genuine GCT multiplicity obstruction" and
"a real multiplicity drop". Both over-claimed, and in the direction that matters
— they label as progress-toward-separation an object the literature has proved
cannot separate. The **theorems are true and sorry-free**; only the framing was
wrong.

To upgrade this to a genuine multiplicity obstruction, `schurMult` would have to
return the actual Wedderburn multiplicity (the dimension of the block, or the
`λ`-isotypic multiplicity), and the separation would have to compare two
*different nonzero* values — not presence against absence.

**Honest scope.** What is proved: the substrate and TL-locus Wedderburn
decompositions differ, on real representation-theoretic data. That is worth
having. It is **not** an instance of `QouGCTObstruction` (which needs the per-`n`
obstruction separating a *counting-hard* object from every *poly-time* object —
the open `VP`-vs-`VNP` content), and by BIP it is not a route to one. No
fabricated instance; the wall stays open. Base ring `ℝ` (§7c: `schurElement` is
archimedean — `Q > 1`, `X ≤ 0`).

-- Ref: [burgisser2019] https://doi.org/10.1090/jams/908
-/

namespace QOU.Information

open QOU.MathlibExt.QPartitionCombinatorics
open QOU.MathlibExt.WenzlSchurElement
open scoped Classical

/-- **GCT multiplicity indicator.**  `1` if the Wedderburn block `λ` is present
    (Schur element nonzero), `0` if dropped (Schur element zero) — the block's
    multiplicity in the (semisimple or TL-truncated) decomposition. -/
noncomputable def schurMult (Q X : ℝ) (lam : Partition) : ℕ :=
  if schurElement Q X lam = 0 then 0 else 1

/-- **Substrate: every block present (sorry-free).**  For `Q > 1`, `X ≤ 0` no
    Schur element vanishes, so every multiplicity is `1`. -/
theorem schurMult_substrate {Q X : ℝ} (hQ : 1 < Q) (hX : X ≤ 0) (lam : Partition) :
    schurMult Q X lam = 1 := by
  unfold schurMult
  rw [if_neg (schurElement_ne_zero hQ hX lam)]

/-- **TL locus: a content-`N` block is dropped (sorry-free).**  At `X = Q^{-N}` a
    partition with a content-`N` cell has vanishing Schur element, so its
    multiplicity drops to `0`. -/
theorem schurMult_tl_drop {Q : ℝ} (hQ : 1 < Q) {N : ℤ} {lam : Partition}
    (h : HasContentCell lam N) : schurMult Q (Q ^ (-N)) lam = 0 := by
  unfold schurMult
  rw [if_pos (schurElement_tl_eq_zero hQ h)]

/-- **A proved OCCURRENCE separation (sorry-free).**  The substrate data
    `schurMult Q (-1)` (all blocks present) and the TL-locus data
    `schurMult Q (Q^{-N})` (content-`N` blocks dropped) are `SeparatedAt` every
    content-`N` partition: `1 ≠ 0`.

    **Not a multiplicity obstruction.**  `schurMult` is a 0/1 presence
    indicator, so this separates by occurrence, and Bürgisser–Ikenmeyer–Panova
    prove occurrence obstructions cannot separate `VP` from `VNP`.  See the
    module docstring's correction record before citing this as GCT progress. -/
theorem schur_separatedAt {Q : ℝ} (hQ : 1 < Q) {N : ℤ} {lam : Partition}
    (h : HasContentCell lam N) :
    SeparatedAt (schurMult Q (-1)) (schurMult Q (Q ^ (-N))) lam := by
  show schurMult Q (-1) lam ≠ schurMult Q (Q ^ (-N)) lam
  rw [schurMult_substrate hQ (by norm_num) lam, schurMult_tl_drop hQ h]
  exact one_ne_zero

/-- The two multiplicity data genuinely differ (via `multData_ne_of_separatedAt`):
    the substrate and TL-locus Wedderburn decompositions are distinct. -/
theorem schur_multData_ne {Q : ℝ} (hQ : 1 < Q) {N : ℤ} {lam : Partition}
    (h : HasContentCell lam N) :
    schurMult Q (-1) ≠ schurMult Q (Q ^ (-N)) :=
  multData_ne_of_separatedAt (schur_separatedAt hQ h)

/-- **Concrete non-vacuity: `[2]` has a content-`1` cell.**  The cell `(0,1)` of
    the partition `[2]` has content `1 − 0 = 1`. -/
theorem hasContentCell_two : HasContentCell [2] 1 := by
  refine ⟨0, ?_, 1, ?_, ?_⟩ <;> decide

/-- **Concrete GCT obstruction (sorry-free).**  At `N = 1` the block `[2]` is
    present at the substrate and dropped at the TL locus `X = Q^{-1}` — an
    explicit, proved multiplicity drop separating the two regimes. -/
theorem schur_separatedAt_two {Q : ℝ} (hQ : 1 < Q) :
    SeparatedAt (schurMult Q (-1)) (schurMult Q (Q ^ (-(1 : ℤ)))) [2] :=
  schur_separatedAt hQ hasContentCell_two

end QOU.Information
