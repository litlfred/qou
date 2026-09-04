# The C1 kernel cannot carry the Door-v residual — in either dictionary

**Date:** 2026-09-04 · **Bean:** `qou-w0tx` · follows `qou-33hb` (#6582), `qou-o2n6` (#6523), `qou-60ew` (#6498), `qou-4g01` (#6474)
**Lean:** `QOU.Mass.C1KernelDictionaryParity` (sorry-free; generic `CommRing` + `CharZero` + `NoZeroDivisors` for the monodromy lemma, `Field` for the kernel)
**Probe:** [`c1_kernel_door_v_residual_probe.py`](../../computations/probes/c1_kernel_door_v_residual_probe.py) (exact sympy, symbolic `q` and `u`)

## What was asked

#6582 left the two `σ ↔ t`-shift dictionaries for the C1 kernel
`L_K = (q²x − 1)σ² − (q−1)σ − (q−1)` disagreeing on parity: under (a) (`σ` = unit
`t`-shift, `x = q^e`) the kernel has an odd component; under (b) (`σ` = `t`-shift 2 on
the double cover, `q = u²`) it commutes with the covering monodromy `t ↦ −t`. My own
pitch at the end of #6582 was that the Door-v `(−1)^m` residual — the target property
#6474 demanded of the prolongation operator's tower — would pick (a), because (b) has
no odd shift to put the alternation on. This tranche tested that.

## Answer: the residual does not decide; it kills both

The residual is the demand that the level-`n` jet carry monodromy character `(−1)^n ε`
from some level `n₀` on (`halt : ∀ n, n₀ ≤ n → mono (Tⁿ X) = ((−1)^n ε) • Tⁿ X`). Under
either dictionary a tower satisfying it is **zero** from that level on.

**(b) — monodromy commutation.** A monodromy-commuting homogeneous operator transports
the character of level `n` to level `n + 1` unchanged, so alternation at two consecutive
levels forces `2 · (−1)^n ε · Tⁿ⁺¹X = 0`, hence `Tⁿ⁺¹X = 0`, with **no hypothesis on the
seed** (`comm_mono_flip_kills`). Applied to the cover operator:
`c1KernelOpCover_residual_kills_tower` — the tower is zero from level `n₀ + 1` on.

**(a) — the `e`-dependence of the shift-2 weight.** #6498's
`residual_from_level_tower_is_odd_part` forces the even part `E` (shift 2 + zeroth
order) to kill both the level-`n₀` jet `Y` and `O Y`. Written out,

    E Y = 0      :  (q^{e+2} − 1) Y(e+2) = (q − 1) Y(e)
    E (O Y) = 0  :  (q^{e+1} − 1) Y(e+2) = (q − 1) Y(e)      (after re-indexing)

— the same recurrence with `q^{e+1}` in place of `q^{e+2}`. Their difference is
`q^{e+1}(q − 1) Y(e+2) = 0`, so `Y = 0` for `q ≠ 0, 1` (`c1E_zero_c1E_O_zero_imp`; the
probe checks the identity `(q−1)·E Y(e) + E(O Y)(e−1) = (q−1)² q^{e+1} Y(e+2)` that the
Lean `linear_combination` uses). Hence `c1KernelOp_residual_kills_jet`: under (a) the jet
is zero **at** the level where alternation starts, and `c1KernelOp_residual_kills_tower`:
the tower is zero from `n₀` on.

The Door-v residual in the corpus is the asymptotic sign alternation of the **growing**
GGM solution — nonzero at every level (#6523, `GGMAlternationOnset`). So **the C1
kernel, read as a shift operator on the jet tower, is not a carrier of the Door-v
residual in either dictionary.**

## Two things the probe established that the Lean does not state

- **The window is minimal: one alternating level is satisfiable, the second kills.**
  Under (a), `E Y = 0` alone has solutions — but the `e = −1` slot reads
  `E Y(−1) = (q − 1) Y(1)`, so the odd part is forced to zero and the family is the
  **q-cosh series in `t²`**, `Y(2k) = Y(0) / ([2]_q [4]_q ⋯ [2k]_q)` with the geometric
  q-integer, one free constant. On it the level-1 jet is the pure odd part and does
  flip; `E (O Y) ≠ 0`, so the level-2 flip is what kills. Under (b) any fixed-parity
  seed carries a constant character at every level — it never flips at all.
- **The kernel annihilates its own carrier.** With `b₀ = b₁ = 1` and
  `[m+2]_q b_{m+2} = b_{m+1} + b_m`, `L_a b = 0` on the whole window, residue slots
  included (`b₀ = b₁` makes the `e = −1` slot vanish). So the kernel's tower on the C1
  carrier is `(b, 0, 0, …)`: there is nothing to alternate. The Door-v alternation
  lives on the GGM growing solution, which is not the tower of anything the kernel
  iterates.

## Consequence for the conjecture

If `conj:qdifference-kernel-prolongation-symbol` holds *and* the prolongation operator
is its symbol, then the `(−1)^m` twist between `C1 ⊗ C1` and GGM is **not produced by
the prolongation's own iteration**. It must sit in the seed or in the pairing, not in
`D_q`. Combined with #6582 (the kernel is not derivative-only) this says the two target
properties #6474 used to narrow `D_q` — the residue and the residual — sit differently
against the target symbol: the residue is *consistent* with `L_K` (level-2 residue
`(q−1)²(a₀ − a₁)`, #6582), the residual is *inconsistent* with it. That is a sharper
statement of what #6474's admissible class actually constrains.

And the dictionary question W2 (`qou-xufp`) is **not** settled by the residual. Both
readings fail it the same way, so the parity disagreement between them stays open, and
my #6582 suggestion that the residual would pick (a) was wrong — recorded here so the
next agent does not re-run it.

## Honest scope

- Scope-(b) exclusion, invariants named: monodromy commutation for (b); for (a), that
  the shift-2 weight `q^{e+2} − 1` is not translation-invariant in `e` while the
  zeroth-order weight `−(q − 1)` is. Needs `q ≠ 0` and `q ≠ 1` (the zpow step).
- The result is about **the kernel itself as the operator**. An operator whose *symbol*
  is `L_K` but which differs from it by lower-order terms is not excluded; nothing here
  constructs `D_q`.
- Conditional on the conjecture's identification "symbol = `L_K`". If that is wrong the
  residual constrains nothing about `L_K`.
- One probe defect corrected before commit: the first version of section (3) imposed
  `E Y = 0` up to the window's upper edge, where the zero padding forces `Y = 0` from
  the top down — a window artifact that read as "the family is trivial". Restricting to
  `e + 2 < N` recovers the q-cosh family.

## Reproduce

```bash
PYTHONPATH=computations python3 -u computations/probes/c1_kernel_door_v_residual_probe.py
```
