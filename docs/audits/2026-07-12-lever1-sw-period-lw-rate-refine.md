# Lever-1: the SW-period↔lw fork is resolved; the naive single-branch rate overshoots (z2bn)

**Date:** 2026-07-12
**Branch:** `claude/lever1-sw-period-lw-rate-refine-2026-07-12`
**Compute:** [`computations/lever1_sw_period_lw_rate_refine.py`](../../computations/lever1_sw_period_lw_rate_refine.py)
**Witness:** [`computations/lever1-sw-period-lw-rate-refine.witness.json`](../../computations/lever1-sw-period-lw-rate-refine.witness.json)
**Bean:** `z2bn` (lever-1 fibre q-difference kernel). **Refines:** `sw_period_growth_probe.py`
(audit-only), `prop:sw-period-residue-sum` (Lean `sw_period_eq_residue_sum`),
`Lever1Depth2Exclusion.lean`.

## Context — the frontier is more resolved than the `z2bn` headline

The `z2bn` bean's headline ("frontier = derive τ = tr B geometrically, owner-gated, not
started") is **stale**. The SW-period prolongation fork is already resolved:

- `a_D^(n) = ∮_γ λ_SW^(n)` on the color cubic `P = X³+(z+1)X²+(z²+z+1)X+(z³+z²+z+1)`, with the
  **explicit** higher-jet rule `λ_SW^(n)=X^(n)(z)dz` (operator `D=∂_z+X'∂_X` — the "abstract
  jets" gap is filled in `sw_period_growth_probe.py`).
- Two corpus claims: (i) depth-2/SL2 `a_{n+2}=τ·a_{n+1}−a_n`, ratio → λ₊≈2.184; (ii) #1765/lw
  `a_D^(n)=lw(n−1)=(1/n)Σ_{λ⊢n}dim_q`, ratio grows. They agree n≤4 (τ fit to those anchors) then split.
- **Resolved:** the branch-point Puiseux estimate + `prop:sw-period-residue-sum` (residues =
  per-block Wedderburn dim_q = lw, Lean-proved) ⇒ super-exponential ⇒ **lw/#1765 is the true
  prolongation; the depth-2 τ is an n≤4 effective fit** (also Lean (b)-excluded, `Lever1Depth2Exclusion`).

## This probe — reproduce in-container + quantitative rate check

Two things the audit-only argument did not pin numerically (mpmath-only, sympy firewalled here):

**1. Fork reproduced in-container.** lw ratio grows `1.34→3.10` (super-exp) while the depth-2
ratio → `λ₊≈2.184` (constant); they split at n≥5.

| n | lw(n−1) | lw ratio | (n−½)/R | √n | depth-2 ratio |
|---|--:|--:|--:|--:|--:|
| 3 |   1.337 | 1.337 | 2.651 | 1.732 | 1.337 |
| 5 |   5.376 | 2.123 | 4.772 | 2.236 | 2.115 |
| 6 |  13.560 | 2.522 | 5.832 | 2.449 | 2.169 |
| 8 | 115.826 | 3.100 | 7.953 | 2.828 | 2.184 |

**2. Quantitative rate check (new).** The **naive single-branch** estimate `(n−½)/R` (R = nearest
of the branch points) **overshoots** the true lw ratio **~2.6×** at n=8 (7.95 vs 3.10). The color
cubic has **6 branch points in 3 pairs** (`|z| ≈ 0.943, 1.0, 1.061`); the exact geometric rate is
the **full multi-branch residue sum**, not the nearest point. The true lw ratio tracks the
**involution-class ~√n** growth (`√8 = 2.83`), consistent with the q→1 telephone/involution-number
limit of lw.

## Verdict (scope-(a))

The fork resolution **stands** — the SW period grows super-exponentially (= lw), not at the
constant λ₊ of the depth-2 τ-recurrence. But the geometric rate is **quantitatively** the
multi-branch-point residue sum, **not** the single-point falling factorial (which overshoots ~2.6×).
So the open geometric piece is sharper than "derive τ": it is the **exact super-exponential `a_D^(n)`
kernel** — the q-Bessel-class / multi-branch residue sum whose q→1 limit is the involution numbers —
with the τ-recurrence being only its n≤4 shadow. This refines the `z2bn` "τ = tr B derivation"
framing: τ is settled (n≤4 fit); the live object is the super-exp kernel.

## Derivation — the exact classical (q=1) kernel (answering "τ is a fit?")

τ is **not** a fit: `τ = (a_D²+a_D⁴)/a_D³` is an exact q-rational combination of the *derived*
categorical anchors `a_D^(n)=lw(n−1)` (Lean `tauAnchor_closed_form`). What is only n≤4-effective
is the *fixed-τ depth-2 recurrence as a model of all-n growth*. The **exact** kernel is derivable
at the classical limit, and it is derived — not fitted:

- **q→1:** `S(n) = Σ_{λ⊢n} dim_q(λ) → Σ_{λ⊢n} f^λ = I(n)` (RSK/Burnside = the keystone **Identity
  I**; `I` = involution/telephone numbers, A000085). Verified exact: `S(n)|_{q=1} = 1,2,4,10,26,76,
  232,764`.
- **Exact classical kernel (derived + Lean-proved sorry-free):** `a_D^(n)=I(n)/n` satisfies the
  **variable-coefficient** depth-2 recurrence
  `a_D^(n) = ((n−1)/n)·a_D^(n−1) + ((n−1)(n−2)/n)·a_D^(n−2)` (matches to 1e-12 for all n). Its
  coefficients grow with n ⇒ super-exponential; the fixed-τ (constant-coefficient) depth-2 is its
  **n≤4 shadow**. Lean:
  [`QOU/Mass/BindingClassicalKernel.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/BindingClassicalKernel.lean)
  (`aDClassical_variable_coeff`, `aDClassical_coeff_unbounded`) — lean-direct exit 0, sorry-free,
  proved from the corpus `involutionNumber` telephone recurrence.
- **q-deformation (measured):** `S(n)=S(n−1)+[n−1]_q·S(n−2)+D(n)` — `c_2=[1]_q`, `c_3=[2]_q`
  **exact** (D=0), cyclotomic Habiro tail `D(n)` growing from n≥4 (q→1 ⇒ `[n−1]_q→(n−1)`, `D→0`,
  recovering the exact telephone recurrence).

So the exact kernel is **derived**: the q-deformed telephone recurrence, whose q=1 limit is the
*proved* involution recurrence. This closes the classical-kernel gap **modulo the same Identity I**
(`Σ f^λ = I(n)`, `YoungTableauStandard.sum_dimSYT_eq_involution`) the keystone P1–P5 program
discharges — so the classical binding kernel and the keystone share **one** open input; everything
else is proved. Compute:
[`computations/lever1_binding_classical_kernel_derive.py`](../../computations/lever1_binding_classical_kernel_derive.py).

## Discipline

mpmath-only (reproducible where sympy is firewalled); the classical-kernel Lean is verified
lean-direct exit 0, sorry-free. `lw` categorical (q-hook dim_q, no fit); branch points are the
cubic's geometry; τ is the wired closed form; the classical kernel is derived from a proved
theorem. The overshoot is a **reported quantitative mismatch**, not a tuned match. No production
wiring. Scope-(a).
