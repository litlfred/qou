# Interface-operator pairwise-assembly ceiling (2026-06-30)

**Branch:** `claude/interface-operator-pairwise-ceiling-2026-06-30`
**Probe:** `computations/probes/interface_operator_pairwise_ceiling_probe.py` (+ witness)
**Extends:** the two term-side ℓ¹ prunes
(`delta_lambda_l1_ceiling_sign_prune`, `binding_qgaussian_ell1_ceiling_measurement`)
to the **assembly side**, and refines the 4-body assembly audit
(`2026-06-23-interface-operator-derivation-and-4body-assembly.md`).

## Question

The term-side ℓ¹ prunes showed the single `Σ_λ y_λ χ^λ Δ_λ` term cannot close
the binding deficit — an **interface / many-body operator (PROBE 2)** must
supply the rest. The 4-body audit found the *multiplicative* deficit form
`1−∏f` too weak (its chain/tetrahedron A-scaling far below AME). But that is
only one pairwise-assembly model. **What is the ceiling over the whole
pairwise class, and how much must the interface operator add beyond it?**

## Method — zero-fit, scale-free

Measure the binding A-scaling ratio `R(X) = B(X)/B(D)` reachable by **every**
2-body bond assembly: `{multiplicative 1−∏f, additive Σ(−log f)} × {linear
chain (A−1 bonds), complete graph (C(A,2) bonds)}`, using the
categorically-forced **zero-fit** per-bond factors

    p-p → z,   n-n → z − h,   p-n → z − h·(½ − δ/4),

`z = 1/(√q+1/√q) ≈ 0.499`, `h = q−q⁻¹ ≈ 0.209`, `δ = flavor_split_leading(q)`
(the PROVEN leading split, de-wired 2026-06-29). Ratios cancel the per-atom
scale `E₀·τ_vac`, so there is **no free parameter** (anti-flip-flop). The
**pairwise ceiling** = max over the four models; the **super-pairwise
enhancement** = `R_AME / ceiling`.

## Result

| iso | A | B_AME | R_AME | mult-chain | mult-cplt | add-chain | **add-cplt** | ceiling | **super×** |
|-----|---|------:|------:|---:|---:|---:|---:|---:|---:|
| D   | 2 | 2.225 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| T   | 3 | 8.482 | 3.81 | 1.46 | 1.58 | 2.33 | 3.33 | 3.33 | 1.14 |
| ³He | 3 | 7.718 | 3.47 | 1.33 | 1.52 | 1.75 | 2.75 | 2.75 | 1.26 |
| ⁴He | 4 | 28.296 | 12.72 | 1.56 | 1.65 | 3.08 | **6.08** | 6.08 | **2.09** |
| ⁶Li | 6 | 31.995 | 14.38 | 1.64 | 1.65 | 5.16 | **15.24** | 15.24 | **0.94** |

Three structural findings:

1. **The additive complete-graph form is far stronger than the
   multiplicative one.** `add-complete` reaches 6.08× the deuteron at ⁴He vs
   the multiplicative ≤1.65×. The 4-body audit's "topology is not the missing
   scale" conclusion was drawn from the *multiplicative* form only; the
   additive linked-cluster on the complete graph closes most of the gap, so
   the deficit is **not a general A-scaling failure**.

2. **⁴He needs a 2.09× super-pairwise enhancement.** Even the best 2-body
   assembly tops at 6.08×D; AME is 12.72×D. The residual factor of ~2.1 is a
   genuine **≥3-body cooperative term** — the α-particle shell-closure /
   supermultiplet spike — that no pairwise bond model (either form, either
   topology) can supply.

3. **The spike is ⁴He-LOCAL, not a monotone many-body trend.** ⁶Li
   *overshoots* the best pairwise model (super× = 0.94 < 1): the complete-graph
   `C(A,2)` bond count grows too fast by A=6. So the interface operator is
   **not** simply "sum over all pairs" — it carries a localized ⁴He
   enhancement that does not persist to ⁶Li. This cross-validates the sibling
   probe `su4-occupancy-binding-mass-probe` ("occupancy reading is ⁴He-LOCAL,
   breaks by ²⁴Mg").

## Scope — (a) scope-limited, points the interface operator

This is a **(a) scope-limited** measurement: it shows the *pairwise* class —
with the current categorical factors and these two assembly forms — tops out
at 6.08×D at ⁴He, 2.09× short. It does **not** exclude the interface operator;
it **specifies its target**: a localized, ⁴He-centred, ≥3-body cooperative
term contributing the residual ~2.1× at A=4 and *vanishing* by A=6. Nothing is
fitted; the ceiling is read off the categorical factors.

## Why useful for PROBE 2

PROBE 2's full closure is double-gated — Rust infrastructure (MPFR seminormal
matrices at H₉/H₁₂ for the ρ_F operator extraction) and owner-gated absolute
scale (the s5-so3 keystone W_λ). This probe narrows what that gated machinery
must deliver **before** it is built: not a better pairwise bond sum (the
ceiling is fixed at 6.08×D), but a genuine 3-/4-body cluster operator (Ursell
connected term) that is sharply peaked at the α-particle and decays by ⁶Li.
Formalize-first: a one-script scale-free ratio bound tells the keystone build
exactly which structure to target.

## Reproduce
```bash
python3 computations/probes/interface_operator_pairwise_ceiling_probe.py
```
