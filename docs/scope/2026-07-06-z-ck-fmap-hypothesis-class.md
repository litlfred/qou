# z→c_k f-map — the surviving hypothesis class (formalize-first, bean `ea56`)

**Date:** 2026-07-06 · **Branch:** `claude/z-c-k-f-map-keystone-ub5yix` (PR #3449)
· **Ledger:** [`z-ck-fmap-keystone.md`](../coordination/z-ck-fmap-keystone.md)
· **Discipline:** structural only — no c_k value, no anchor sweep, no wiring,
no tier change (registry §8 flip-flop guard respected).

## 1. New structural result — the z-alone exclusion (scope-(a))

Proved this session (sorry-free Lean, `lean`-direct exit 0:
[`QOU/QBeta/ZBarParity.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/ZBarParity.lean);
sympy-exact 7/7:
[`qbeta_z_bar_parity_fmap_class_probe.py`](../../computations/qbeta/qbeta_z_bar_parity_fmap_class_probe.py)
→ [`qbeta-z-bar-parity-fmap-class.witness.json`](../../computations/qbeta/qbeta-z-bar-parity-fmap-class.witness.json)):

| atom | bar-parity under `q ↦ q⁻¹` | twist |
|---|---|---|
| `z(q) = √q/(1+q)` (Markov parameter) | **EVEN** | `1` (exact) |
| `ℏ_q = 1 − q⁻¹` | odd | `−q` |
| `ℏ_q²` (ladder variable `u = b·ℏ_q²`) | even | `q²` |
| `κ_{(2,1)} = (q−1)³(q+1)/q²` ((2,1) heat carrier) | **ODD** | `1` (exact) |

Since the bar-fixed locus is a subring (Lean `bar_fixed_add/_mul/_pow`), every
scalar functional of `z` alone — any polynomial or rational function — is
bar-EVEN. The c_k-recursion kernel's leading coefficient `a₁ = −c₃` is proved
bar-ODD (`QBetaCKRecursionKernelConstraints.ck_a1_bar_odd_of_c3_odd`) and is empirically
nonzero (`|c₃| ≈ 2.07`). A bar-even scalar equal to a bar-odd nonzero element
forces `2a = 0` (Lean `bar_even_and_odd_two_mul_eq_zero`), impossible in
characteristic ≠ 2. **Hence no scalar rational function of `z` alone can source
`a₁`.** The z-recursion backbone supplies magnitude/recursion structure only —
never the parity.

Scope-(a) phrasing (per AGENTS.md): this excludes *scalar z-alone functionals
as the odd-channel source*; it does not exclude `z` as an ingredient.

## 2. The hypothesis-class lattice (state of the search space)

| class | shape | status |
|---|---|---|
| **Z0** | linear / bar-even seeding from `Δtr_M` | **REFUTED** — C13 (PR #2465) |
| **Z1** | pure powers `A·(Δtr_M)^m` | being pruned by [PR #3429](https://github.com/litlfred/qou/pull/3429) (odd m → half-integer rung; m=2 → forbidden c₁; m=4,6 generically killed) — cite when landed |
| **Z2** | scalar rational functionals of `z` alone | **EXCLUDED this session** (§1, parity) |
| **Z3** | (bar-even z-functional) × (bar-odd carrier: `κ_{(2,1)}`, `sinh(kη)`, odd `ℏ`-powers with twist) | **SURVIVING scalar class** — converges with the heat-route (2,1) mode-selectivity and the Stage-B parity re-mix requirement |
| **Z4** | operator-level: Hoefsmit `T_β` ladder / 4₁ order-2 qZeilberger kernel (P-C15 survivor) | **SURVIVING operator class** — the `c4qz` gated probe target |

Constraints every surviving candidate must still clear (the 7-step preflight,
[2026-06-05 gates](../audits/2026-06-05-qbeta-formalize-first-gates-consolidation.md)):
corpus-grep; refuted-class check; bar-parity (§4(b) — for the *even* overall
`F`, with the ODD `a₁` in the kernel); radius/pole at `u_substrate` (§4(a));
q=1 shadow `c₂ → −1`, `c₃ → −2` (§4(c)); direction sanity (§4(d));
cross-anchor stability. Only `c₂, c₃` are data-determined (precision floor) —
candidates are never validated against fitted `c_{k≥4}`.

## 3. Reachability note (Z3/Z4 are engine-compatible)

`z` is algebraic over `ℚ(q)` (degree 2) and satisfies the proved 3-term
recursion; `κ_{(2,1)}` is q-rational. Finite ring combinations of q-holonomic
atoms are q-holonomic, so every Z3 candidate admits a finite-depth q-difference
kernel with q-rational coefficients — exactly the class the sorry-free
[`RationalCoeffRecurrence.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/RationalCoeffRecurrence.lean)
engine consumes, and NOT the constant-kernel class refuted through depth 4.
Compatibility is necessary, not sufficient: the identification (which
z-functional, which carrier, which weights) remains the open keystone.

## 4. Next gated step

Bean `c4qz` (now unblocked): run the P-C15 4₁ order-2 operator against the
exact `Δtr_M` Taylor data through the preflight, with kill criteria pre-stated
— testing whether the qZeilberger kernel, seeded by the z-backbone, reproduces
`c₂ = −1` exactly and the `c₃ → −2` shadow with a bar-odd `a₁` in the Z3/Z4
factored form.
