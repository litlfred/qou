# Ramified shift-operator calculus: derivative-like `D_q` of shift 1 or 2 cannot produce a residue

**Date:** 2026-09-03 · **Bean:** `qou-4g01` · continues `qou-qx7j` (#6462) and the
2026-07-20 scoping audit's walls **W1–W3**
**Lean:** `QOU.Mathlib.RamifiedShiftCalculus` (sorry-free, generic `CommRing`) ·
**Probe:** [`ramified_shift_calculus_prune_probe.py`](../../computations/probes/ramified_shift_calculus_prune_probe.py) (exact, exit 0, 26 checks)

## What was asked

Walls W1–W2 of
[`2026-07-20-zgeometric-prolongation-symbol-scoping.md`](2026-07-20-zgeometric-prolongation-symbol-scoping.md):
construct the q-difference prolongation `D_q` from the colour curve `Σ` and
extract its symbol at a ramified pole — "q-jet-bundle / q-D-module symbol
calculus absent from Mathlib and the corpus".

This does **not** construct `D_q`. It builds the symbol calculus at the ramified
pole and uses it, per the formalize-first probe discipline, to **prune the class
of candidate `D_q` exactly before anything is constructed**.

## What existed (corpus-grep)

| module | has | lacks |
|---|---|---|
| `QOU.Mass.QDiffProlongationBaseOperator` | the q-dilation and Jackson operator **in `z`** on monomials | the ramified chart |
| `QOU.Brings.RamificationParityMonodromy` | the coefficient model `f : ℤ → R` at `z = z_c + t²`, the classical `ddz` as a shift-2 operator, the covering monodromy `mono` | any operator other than `ddz`; composition; the residue slot |
| `QOU.QInteger` (`QIntegerCanonical`) | canonical `[k]_q` on `ℤ`, with `[0]_q = 0` | — |

The gap is exactly the calculus: operators as symbols, their composition, and
what they do to the residue slot. That is what is added.

## The calculus

A **shift operator** is `shiftOp k c f = fun e => c e * f (e + k)` — the
coefficient at `tᵉ` read from `t^{e+k}` with weight `c e`. The pair `(k, c)` is
the operator's symbol on the punctured `t`-disk.

| result | statement |
|---|---|
| `shift2_eq_shiftOp`, `ddz_eq_shiftOp` | the corpus's operators are members (`ddz` = shift 2, multiplier `e+2`) |
| `shiftOp_comp` | **symbols compose**: `shiftOp k c ∘ shiftOp l d = shiftOp (k+l) (c · d(·+k))` |
| `shiftOp_iterate` | `n`-fold: `∏_{i<n} c(e + ik) · f(e + nk)` |
| `shiftOp_residue_slot` | the residue slot `t^{−2}` is read from `t^{k−2}` with weight `c(−2)` |
| `annihilatesConstants_iff` | `c(−k) = 0` ⟺ the operator kills the constant term `t⁰` |

Every derivative on the chart is a shift operator that annihilates constants:

| operator | `k` | `c e` | `c(−k)` |
|---|---|---|---|
| classical `d/dz` | 2 | `e + 2` | `0` |
| naive q-deformation of `d/dz` | 2 | `[e+2]_q` | `[0]_q = 0` |
| Jackson `D_{q,t}` in the local coordinate | 1 | `[e+1]_q` | `[0]_q = 0` |

Both q-integer conventions give `[0]_q = 0` (probe checks both; the Lean
instantiates the canonical balanced one), so the prune below does not depend on
the convention choice.

## The W1 prune — two exact necessary conditions

**1. Residue.** On a power-series seed (support in `t`-degrees `≥ 0` — the
colour-cubic branch is one):

- shift 2 with `c(−2) = 0` ⟹ residue slot dead at every `n ≥ 1`, for every seed
  (`residue_slot_zero_shift_two`; the `i = 0` factor of the iterate is `c(−2)`);
- shift 1 with `c(−1) = 0` ⟹ dead at every `n` (`residue_slot_zero_shift_one`;
  `n ≤ 1` by the seed's support, `n ≥ 2` by the `i = 1` factor `c(−1)`).

**No derivative-like prolongation of shift 1 or 2 can produce the binding
period.** Instantiated: `qddz_residue_slot_zero`, `jacksonT_residue_slot_zero`.
A residue needs a component with `c(−k) ≠ 0` — a genuine zeroth-order term,
which in rank 2 is the connection-matrix datum the conjecture block's 2026-08-26
note already places the symbol in.

**2. Parity.** An even shift commutes with the covering monodromy `t ↦ −t`
(`shiftOp_comm_mono_of_even`, generalising `shift2_comm_mono`); an **odd** shift
anti-commutes (`shiftOp_anticomm_mono_of_odd`), so an odd-shift jet tower from a
fixed-parity seed has monodromy eigenvalue `(−1)^n ε`
(`odd_shift_jet_monodromy_alternates`) — the Door-v residual, and the positive
counterpart to `classical_jet_monodromy_constant`. Carrying that residual needs
an **odd** shift.

**Together:** any single-shift `D_q` carrying both measured target properties has
an **odd shift** and a **non-derivative component**. Both derived from the local
geometry of `Σ` (square-root branch ⇒ the coefficient model) and the two target
properties. **No C1 kernel coefficient enters** — the W3 anti-fit obligation is
respected by construction.

## Non-vacuity, checked

- `constant_weight_shift_one_residue`: a shift-1 operator with `c ≡ 1` reaches
  the residue slot from the constant term in two steps with weight `1`. The
  prune is about *derivative-like* operators, not all operators.
- Probe (5): a shift-1 operator with `c(−1) = λ` and `[e+1]_q` elsewhere has
  residue a nonzero multiple of `λ`, vanishing exactly at `λ = 0`.
- The scratch axiom check includes a deliberate `sorry` on the prune *without*
  its hypothesis, confirming the hypothesis is load-bearing.

## Honest scope

- `D_q` is **not constructed**; W1 stays a wall. The class is narrowed.
- The prune is for **single-shift** operators. A general q-D-module element is a
  finite sum `Σ_k c_k σ^k`; its residue slot is the sum of the slots and could in
  principle cancel or survive. The composition law is the tool for that case;
  the sum case is not claimed here.
- Shift `k ≥ 3` (a triple pole per jet) is not pruned by the residue argument;
  it is geometrically unnatural but not excluded here.
- The keystone `a_D^(n) = lw(n−1)` is neither weakened nor strengthened.

## Reproduce

```bash
PYTHONPATH=computations python3 -u computations/probes/ramified_shift_calculus_prune_probe.py
```
