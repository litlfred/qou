import QOU.MathlibExt.QPartitionCombinatorics

/-!
# QOU.MathlibExt.AddableBoxHookOneRow — the one-row case of the addable-box hook identity (B)

The general-`n` fake-degree gap (`MolienFakeDegreeInduction`, bean `qou-x4zl`) reduces to the
**addable-box hook identity (B)**

```text
  Σ_{b addable to μ} q^{−c(b)} · hookProd(μ) / hookProd(μ+b)  =  1        (B')
```

(equivalently `Σ_b q^{−c(b)} qDim(μ+b)/qDim(μ) = [|μ|+1]_q`). This file records the **one-row**
case `μ = (n)` in closed form, which is the honest base of an induction on row count.

## The one-row case IS the balanced q-integer recurrence

For `μ = (n)` there are exactly two addable boxes:
`(0,n)` (content `n`, giving `(n+1)`) and `(1,0)` (content `−1`, giving `(n,1)`). Using
`hookProd((n)) = [n]_q!`, `hookProd((n+1)) = [n+1]_q!` and `hookProd((n,1)) = [n+1]_q·[n−1]_q!`,
`(B')` collapses to

```text
  q^{−n} · [n]_q!/[n+1]_q!  +  q^{1} · [n]_q!/([n+1]_q·[n−1]_q!)  =  1
  ⇔  q^{−n}/[n+1]_q + q·[n]_q/[n+1]_q = 1
  ⇔  [n+1]_q  =  q·[n]_q + q^{−n}.
```

That last line is exactly `QPartitionCombinatorics.qBracket_add` at `(a,b) = (n,1)` (`[1]_q = 1`).
So the one-row (B) is already corpus infrastructure; `oneRow_addable_hook_recurrence` below is the
direct proof, recorded as the base case and as documentation that the small-row cases are not the
open content.

**What is NOT here (honest scope, bean `qou-ognw`).** The `≥2`-row cases of (B) do **not** reduce to
`qBracket_add`: adding the *new-row* box to a two-row `μ=(a,b)` produces a **three-row** `(a,b,1)`
shape, so even two-row (B) needs a three-row hook product. The general (B) is a q-hook-length-formula
identity; the clean route is the **content / partial-fraction** expansion (the addable- and
removable-box contents of `μ` interlace, and (B) is the residue identity over the content variable —
`QOU.SchurWeyl.QJucysMurphyEigen` gives the contents as q-JM eigenvalues). That is a genuine
multi-lemma formalisation, tracked in `qou-ognw`; this file lands only the one-row brick.

Base ring: generic `[Field R]` with the standard non-degeneracy `q ≠ 0`, `q − q⁻¹ ≠ 0` (§7c —
purely algebraic, no ordering).

-- Ref: content/.../QOU/MathlibExt/MolienFakeDegreeInduction.lean (the induction this feeds)
-- Ref: computations/qbeta/fake_degree_addable_box_recursion_probe.py (identity (B), exact n ≤ 6)
-/

namespace QOU.MathlibExt.AddableBoxHookOneRow

open QOU.MathlibExt.QPartitionCombinatorics

variable {R : Type*} [Field R]

/-- **The one-row addable-box hook recurrence** `[n+1]_q = q·[n]_q + q^{−n}`, the content of the
identity (B) at `μ = (n)`. Direct proof from the balanced formula; equivalently
`qBracket_add q hq n 1` with `[1]_q = 1`. -/
theorem oneRow_addable_hook_recurrence (q : R) (hq : q ≠ 0) (hden : q - q⁻¹ ≠ 0) (n : ℕ) :
    qBracket q (n + 1) = q * qBracket q n + q ^ (-(n : ℤ)) := by
  have h := qBracket_add q hq n 1
  rw [qBracket_one hden] at h
  simpa using h
