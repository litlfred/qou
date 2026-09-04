# A derivative-only mixed-shift `D_q` cannot have the C1 kernel as its symbol

**Date:** 2026-09-04 · **Bean:** `qou-33hb` · follows `qou-o2n6` (#6523), `qou-60ew` (#6498), `qou-4g01` (#6474)
**Lean:** `QOU.Mass.C1KernelAsShiftSum` (sorry-free; generic `CommRing` for the invariant, `Field` for the kernel)
**Probe:** [`derivative_only_dq_vs_c1_kernel_probe.py`](../../computations/probes/derivative_only_dq_vs_c1_kernel_probe.py) (exact sympy, symbolic `q` and `u`)

## What was asked

The owner asked for *the derivative-only mixed-shift `D_q`* — the class the three
prunes left alive at the low body orders: a sum of shift-1 and shift-2 terms whose
multipliers all vanish at `e = −k` (Jackson `[e+1]_q σ` + q-`d/dz` `[e+2]_q σ²` is the
model case). It reaches the residue slot (#6498) and is not excluded by the residual
below the window (#6523). The constructive question is whether it can be the
prolongation operator of `conj:qdifference-kernel-prolongation-symbol`, whose symbol
the conjecture says is the C1 kernel

  `L_K = (q²x − 1)σ² − (q − 1)σ − (q − 1)`,   `x = q^m`, `σ : x ↦ qx`.

## Answer: no — in either dictionary, and the reason is one line

Reading `L_K` in the shift calculus needs a dictionary between `σ` and the `t`-shift
(that dictionary *is* wall W2). Two are natural:

| dictionary | `x` | `σ` | `L_K` as a shift-sum |
|---|---|---|---|
| (a) unit shift | `q^e` | `e ↦ e+1` | `(q^{e+2} − 1)·S₂ − (q−1)·S₁ − (q−1)·S₀` |
| (b) double cover (`binding-genfun-qdifference` scope note: adjoin `x^{1/2}`) | `u^{2e}`, `q = u²` | `e ↦ e+2` | `(u^{2e+4} − 1)·S₄ − (u²−1)·S₂ − (u²−1)·S₀` |

Under (a), `c1KernelOp_eq_recurrence` checks that this is literally the corpus's
recurrence `[m+2]_q b_{m+2} = b_{m+1} + b_m` in the geometric q-integer `qint` of
`qlift_normalized_kernel_exists`, times `(q − 1)`.

**The invariant.** A derivative-only sum kills the constant seed `t⁰`
(`sumOp_derivativeOnly_const`: every term reads `t⁰` from slot `−k` with weight
`c_k(−k) = 0`). The kernel does not: its zeroth-order term evaluates `t⁰` at `e = 0` to
`−(q − 1)` under (a) and `−(u² − 1)` under (b) (`c1KernelOp_const_ne_zero`,
`c1KernelOpCover_const_ne_zero`). Hence

> `derivativeOnly_ne_c1KernelOp` / `derivativeOnly_ne_c1KernelOpCover`:
> **no derivative-only shift-sum equals the kernel**, for any `q ≠ 1`.

Probe (2) checks both derivative-only candidates kill `t⁰` (balanced and geometric
conventions), that `L(t⁰)` is supported on exactly `{−1, 0}` — both slots fed by the
non-derivative terms — and that the only way `L`'s shift-1 multiplier could annihilate
constants is `q = 1`.

**Consequence.** If the conjecture holds, `D_q` has a **non-derivative component**. That is
the #6474 clause ("odd shift *and* non-derivative component") reached by a **third
route** — from the kernel's own shape — independent of the residue argument (#6498
showed a mixed derivative sum *can* have a residue) and of the residual argument (#6523
showed the residual only bites above the window). The derivative-only class survives the
target properties and fails the target *symbol*.

## Where the kernel sits, and what the two dictionaries disagree on

Under (a) the kernel is exactly the #6474 admissible class: the shift-2 term is
derivative-like (`c₂(−2) = q⁰ − 1 = 0`), the shift-1 term is not (`c₁ ≡ −(q−1)`). Its
residue on a power-series seed is dead at level 1 and alive at level 2,

  `L_K² f (−2) = (q − 1)² (f 0 − f 1)`

(`c1KernelOp_residue_two`): it reads the **branch value** `a₀ = X_c` and the leading
square-root coefficient `a₁`. The derivative-only candidate's level-2 residue is `−a₁`
(#6498) — it cannot see the branch value at all.

Under (b) every shift is even: the kernel **commutes with the covering monodromy**
(`c1KernelOpCover_comm_mono`), has no odd component, and its residue is alive already at
level 1, `−(u² − 1) a₀` (`c1KernelOpCover_residue_one`). So the two dictionaries disagree
on parity — (a) puts the Door-v `(−1)^m` alternation on an odd shift, (b) has no odd
shift to put it on. **That disagreement is the open W2 question in its sharpest form**:
which `t`-shift `σ` is. Nothing here settles it.

## Honest scope

- `D_q` is **not constructed**. The result is a scope-(b) exclusion of the derivative-only
  class *as the carrier of the conjectured symbol*, with the invariant cited
  (`sumOp_derivativeOnly_const` vs the kernel's zeroth-order term). It says nothing about
  operators whose symbol is not `L_K`.
- The result is conditional on the conjecture's identification "kernel = symbol". If the
  identification is wrong, a derivative-only `D_q` is still admissible by everything else.
- The dictionary is not derived; both natural readings give the same exclusion, which is
  why it is stated for both.
- One probe over-claim of mine, corrected before commit: I first asserted `L(t⁰)` is
  supported at `e = 0` alone; it is supported at `{−1, 0}` (the shift-1 term also reads
  the constant). The invariant is unaffected — either slot witnesses it.

## Reproduce

```bash
PYTHONPATH=computations python3 -u computations/probes/derivative_only_dq_vs_c1_kernel_probe.py
```
