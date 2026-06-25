# z2bn lever-1 τ-derivation — first non-fitted geometric probe

**Date:** 2026-06-25
**Branch:** `claude/z2bn-tau-derivation-2026-06-25`
**Probe:** [`computations/substrate/z2bn_tau_derivation_probe.py`](../../computations/substrate/z2bn_tau_derivation_probe.py)
· **Witness:** [`computations/substrate/z2bn-tau-derivation-probe.witness.json`](../../computations/substrate/z2bn-tau-derivation-probe.witness.json)
· **Lean:** [`QOU/Mass/Lever1TauClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/Lever1TauClosedForm.lean)

## Context

The owner **authorized** (2026-06-25) the previously gated derivation of the lever-1 binding-kernel
trace `τ = tr B = 2.6424` as the abelianised `λ_SW` Gauss–Manin holonomy on the coral elliptic curve
`E_q` (a Subgoal-2 step distinct from the s5-so3 reversal; see
[`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) and the `z2bn` bean). This
is the **first non-fitted probe**: establish the clean geometric anchors and test principled holonomy
candidates **once** (no tuning), reporting honestly where the geometry lands. `q₀` is never tuned; the
target value `2.6424` is never fed into any fit.

The corpus setup (`descartes-elliptic-curve.{md,lean}`, `mi-sw-abelianisation-cartan.md`,
`sl2-prolongation-recurrence.md`, `lever1_lambda_sw_no_shortcut.py`):

- **Curve** `E_q : y² = x³ + p(q)x + r(q)`, `p(q)=2(q²−q+1)/(3q)+(q−1)/(3√q)`, `r(q)=…+20/27`.
- **Spectral (coral) cubic** `X³+(z+1)X²+(z²+z+1)X+(z³+z²+z+1)=0`, `z=√q−1/√q`, color coordinate `X`.
- **SW differential** `λ_SW = X dz`; prolonged periods `a_D^(n) = ∮ λ_SW^(n)`; depth-2 recurrence
  `a_D^(n+2)=τ·a_D^(n+1)−a_D^(n)`, `det B = 1`.
- **Anchors** `a_D^(2)=1`, `a_D^(3)=(q+1)²/(3q)`, `a_D^(4)=(3q²+4+3q⁻²)/4`;
  `τ=(a_D^(2)+a_D^(4))/a_D^(3)`.

## Results

### (A) The τ closed form is exact — and now Lean-proved

`τ = (a_D^(2)+a_D^(4))/a_D^(3)` simplifies **exactly** (sympy + Lean `field_simp; ring`) to

$$\tau(q) = \frac{3(3q^4+8q^2+3)}{4q(q+1)^2}.$$

At `q₀ = 1.1099785955573347199`: `τ = 2.6423863133…`, `θ_binding = acosh(τ/2) = 0.7814539460…`,
`λ = eᶿ = 2.1846463153…` (50 dps). Formalized sorry-free as
[`tau_kernel_closed_form`](../../content/quantum-observable-universe/lean/QOU/Mass/Lever1TauClosedForm.lean)
(`ℝ`, `q≠0`, `q+1≠0`).

### (B) The coral curve `E_q` is confirmed — `j(q₀) = 129.86`

Computing the periods of `y²=x³+p(q₀)x+r(q₀)` (roots + complete elliptic integrals) and the Klein
invariant `1728·kleinj(ω₂/ω₁)` gives **`j(q₀) = 129.860`** (corpus 129.86) and **`j(1) = 128`**, with
`p(1)=2/3`, `r(1)=20/27` exact — the descartes/coral `E_q` is the right curve.

> **Side finding (corpus bug, low-priority):** `descartes-elliptic-curve.lean`'s `j_invariant p r`
> def is `-1728(4p)³/(4p³+27r²)` — it **omits the `−16`** of `Δ = −16(4p³+27r²)`, so it returns
> `−16·j` (`j(1) = −2048`, not `128`). The curve and the compute are correct (compute uses the proper
> formula); only that one Lean def is off. It is annotated "NOT part of the formal proof chain", so
> this is a flag for a follow-up, not a blocker.

### (C) The coral-cubic color-root power sums

By Newton's identities on `X³+(z+1)X²+(z²+z+1)X+(z³+z²+z+1)`:

`p₁=−(z+1)`, `p₂=−(z²+1)`, `p₃=−(z³+1)` (the clean `−(zⁿ+1)` law for `n≤3`), then
`p₄=3z⁴+4z³+4z²+4z+3`, `p₅=−(z⁵+5z⁴+5z³+5z²+5z+1)`, `p₆=−(z⁶+1)`. The anchors are **not** these bare
power sums (`a_D^(3)=(z²+4)/3 ≠ p₂`), so the prolongation `λ_SW^(n) ↦ a_D^(n)` is a non-trivial
operator — not a naive `∮ Xⁿ dz`.

### (E) Honest verdict on the holonomy — (a)-NEGATIVE, not closed

No bare-period quantity of `E_q` reproduces `τ = 2.6424` without tuning. The closest near-coincidence
is the modular period ratio's imaginary part `Im(ω₂/ω₁) = 0.734` vs `θ_binding = 0.781` (**~6 % off**) —
a near-miss, **not** a derivation (numerology guard: near-but-not-exact does not close). `2cosh(|z(q₀)|)
= 2.011 ≠ 2.642`, etc.

**Conclusion.** This probe **confirms the two clean pieces** (the exact τ closed form, now Lean-proved;
the curve via `j(q₀)=129.86`) and **bounds the residual precisely**: the geometric closure needs the
explicit prolongation operator `λ_SW^(n)` (equivalently the q-family Gauss–Manin monodromy on the
Hodge multiplicity space), which the anchors show is non-trivial. That operator — not a bare period —
is the owner-gated keystone residual. No fit anywhere; `q₀` and `2.6424` never tuned.

## Scope ((a)/(b) discipline)

- **(a)-positive:** τ closed form exact (Lean-proved); curve `E_q` confirmed (`j(q₀)=129.86`).
- **(a)-negative (scope-limited):** bare `E_q` periods, *alone*, do not reproduce `τ` — this constrains
  the *holonomy normalisation/candidate*, it does **not** exclude the `λ_SW`-prolongation mechanism
  (which this probe does not compute). The prolongation operator stays the open object.

## Cross-references

- [`computations/substrate/lever1_lambda_sw_no_shortcut.py`](../../computations/substrate/lever1_lambda_sw_no_shortcut.py) — anchors; no algebraic shortcut to τ.
- [`computations/substrate/lever1_binding_monodromy_hyperbolicity.py`](../../computations/substrate/lever1_binding_monodromy_hyperbolicity.py) — `τ>2 ⇒ B` hyperbolic `SL₂(ℝ)`.
- [`docs/audits/2026-06-24-lever1-coral-eq-monodromy-integrality.md`](2026-06-24-lever1-coral-eq-monodromy-integrality.md) — coral `E_q` = descartes `E_q`; `tr B ∉ ℤ`.
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — keystone ledger; PR #2722 holds the geometric `tr B` side.
