# P-C15 — the 4₁ order-2 qZeilberger Casoratian ratio clears the bar-parity gate (Q_β fibre kernel, achievable arm)

**Date:** 2026-07-03 · **Axis:** Q_β 1ppQ achievable arm — fibre kernel `F(q)`/`R(q,ξ)`
· **Tier:** structural-exact (symbolic bar-parity identity; no fit, no anchor sweep)
· **Verdict:** **PASS (survivor)** — not excluded; advance gated on the H₄ c₄^even build.

## Scope note (read first)

This is a **scope-(a) positive**: the 4₁ order-2 operator is *not excluded* by the
bar-parity invariant tested here. It is **NOT a closure, NOT a c_k value, and nothing
is wired.** Per the c_k flip-flop discipline (AGENTS.md §Q_β `c_k` truncation framing)
a passed structural gate motivates the next (gated) build; it never itself becomes a
production coefficient.

## What was tested

The open axis for the Q_β achievable arm is a fibre-level Habiro element `F(q)` whose
kernel `R(q,ξ)` drives the c_k recursion. The engine is proved sorry-free
([`RationalCoeffRecurrence.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/RationalCoeffRecurrence.lean));
the kernel constraints are proved
([`QBetaCKRecursionKernelConstraints.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/QBetaCKRecursionKernelConstraints.lean):
non-constant, `a₂ = c₂ = −1`, `a₁` bar-**odd**, constant depth-2 refuted); the kernel
itself is the missing object.

The newly-landed 4₁ colored-Jones **order-2 qZeilberger operator**
([`aj_figure_eight_certificate.py`](../../computations/aj_figure_eight_certificate.py),
exact certificate verified N=1..12) is a candidate for `R(q,ξ)`:

```
a₂ J_{N+2} + a₁ J_{N+1} + a₀ J_N = b ,   x := q^N
a₀ = (x−1)(x²q³−1)/x⁶ ,   a₂ = (xq²−1)(x²q−1)/x⁶ ,   a₁ bar-odd.
```

**This is a different object from every refuted class C1–C14** (see
[refuted-class map](2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md)):
- **C14** tested the 4₁ *Ohtsuki loop-series rationals* as candidate **c₃ scalars** —
  numerology on scalars, refuted. P-C15 tests the **operator/Casoratian structure**.
- **cp4i / `HabiroNewtonLadder`** tested only the **degenerate first-order Newton
  restriction** (Casoratian ≡ 0, supplies no sign). P-C15 uses the **full second-order**
  operator, whose Casoratian is genuinely nonzero.
- Not real-q (C1–C4), not constant-kernel (C5), not mass-side (C8/C12), not the linear
  bridge (C13).

## The decidable gate (on paper, no numerics)

For `a₂ f_{N+2} + a₁ f_{N+1} + a₀ f_N = 0`, the Casoratian of two independent solutions
obeys (Abel–Heine, derived — no sign flip)

```
W_{N+1}/W_N = a₀/a₂ = (q³x³ − q³x² − x + 1)/(q³x³ − q²x − qx² + 1).
```

For the operator to be a bar-covariant fibre object at all, this ratio must be bar-even
up to a single monomial twist (cf. the k-independent twist proved in
[`QBesselBarCovariance.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/QBesselBarCovariance.lean)).
Apply the fibre bar involution `q → 1/q, x → 1/x`:

| quantity | value |
|---|---|
| `R = a₀/a₂` | `(q³x³−q³x²−x+1)/(q³x³−q²x−qx²+1)` |
| `R(1/q,1/x)` | **identical to `R`** |
| **twist** `R(1/q,1/x)/R` | **`1`** (Laurent monomial — trivially bar-even) |
| q→1 classical shadow of `R` | **`1` > 0** (consistent with measured even-channel `W₂ = +102.674 > 0`) |

The numerator/denominator each carry the same coefficient bar-ratio (`a₀`, `a₂` share
parity; `a₁` is the odd one, matching the upstream proof), so the twist cancels to `1`:
**the 4₁ order-2 Casoratian ratio is exactly bar-self-reciprocal.**

Compute: [`qbeta_pc15_casoratian_bar_parity_probe.py`](../../computations/qbeta/qbeta_pc15_casoratian_bar_parity_probe.py)
→ [`qbeta-pc15-casoratian-bar-parity.witness.json`](../../computations/qbeta/qbeta-pc15-casoratian-bar-parity.witness.json)
(sympy 1.14.0, exact symbolic).

**Lean certificate (sorry-free, division-free over `CommRing`).** The bar-parity
is now a proved theorem, not only a symbolic witness:
[`QOU/QBeta/QCasoratianBarParity.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/QCasoratianBarParity.lean).
It is stated over a generic `[CommRing R]` — the reciprocity is a `ℤ[q,x]`
polynomial fact needing no field, only that `q, x` are units (`q·qi=1, x·xi=1`):
`casNum_reciprocal`/`casDen_reciprocal` (numerator and denominator each scale by the
*same* monomial `q³x³` under `q↦q⁻¹, x↦x⁻¹`) and, division-free,
`casoratian_ratio_bar_invariant` (`casNum qi xi · casDen q x = casNum q x · casDen qi xi`
— the shared factor cancels). A `Field` corollary
`casoratian_ratio_bar_self_reciprocal` gives the literal `a/b` ratio form.
lean-direct `exit 0`, sorry-free; wired into `QOU.lean`. Complements the sibling
`QCasoratianAbel` (the first-order Abel–Heine recurrence the ratio comes from).

## Kill-criterion outcome

- **Kill (→ refuted row C15)** would have required: twist not a monomial, **or** wrong
  q→1 shadow sign. **Neither holds.** No refuted row is added.
- **Advance (this outcome):** the gate is cleared; the 4₁ operator is a **live candidate**
  for `R(q,ξ)`. Per the standing gate, **do not run an anchor sweep now** — the anchor-level
  Casoratian `W₃/W₂` can only be evaluated once genuine c₄ rungs exist.

## Next step (gated) and the connection to existing infra

The one gated next move is the **H₄ Hoefsmit `c₄^even` build** (bean `8we6`), which supplies
the genuine c₄ rung. That plugs directly into the sibling's already-machine-checked
decision gate `sigma3_lift_kill_test` /
[`StageCSigma3LiftObligation.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StageCSigma3LiftObligation.lean)
(`W₂ > 0` tier-robust; any valid lift with `W₃ ≤ 0` refutes the single-AW-recurrence
identification). **P-C15 de-risks that build**: it confirms the kernel candidate is a
genuine bar-symmetric object before the expensive H₄ Hoefsmit computation is undertaken.

## Session reanalysis pointer

This probe was run as part of a full **reanalysis of the path to 1 ppQ** (2026-07-03,
main @ `746a5091`). Headline corrections recorded for siblings:
- **L2 = 3/7** (m_e, m_p anchors + m_K/m_π); the four failing genuine predictions
  (m_μ ×964, Q_β ×160, m_n ×181, Δ_pn ×159) all funnel into the **s5-so3 keystone**.
- **Identity I ≠ keystone unlock.** The RSK/SYT surge drove Identity I to **one remaining
  OV `sorry`** (unconditional for all physical n) — but it is a rigor input to a
  falsifiable *gate*, not the keystone. The keystone's geometric leg
  (`BWVacuumRowIsHecke` / `W_λ`) had its leading candidate — the genuine **Σ(2,3,5) WRT
  S-matrix on S³/2I — refuted 2026-07-02** (D=2≠4; vacuum ratio φ ∉ targets).
- **Q_β (P-C15) is the one near-term needle-mover** not below the CAL-2 floor and not
  keystone-gated. This probe is its first structural survivor.
