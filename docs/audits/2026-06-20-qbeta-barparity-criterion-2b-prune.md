# Q_β fibre-kernel — criterion 2(b) prune (bar-odd `b(q)`)

**Date.** 2026-06-20.
**Bean.** qkhc (Q_β kernel hunt, Stage C) — the fibre-level Habiro kernel `R(q,ξ)`.
**Type.** **Constraint / pruning** of the open-axis search criteria — *not* a
real-q closed-form value-hunt (forbidden) and *not* a refuted mechanism. This is
the sanctioned step-3 "narrow before you scan" of
[`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`](2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md).
**Probe.** [`computations/qbeta/qbeta_barparity_kernel_criterion_prune.py`](../../computations/qbeta/qbeta_barparity_kernel_criterion_prune.py)
→ `qbeta-barparity-kernel-criterion-prune.witness.json` (exact symbolic, sympy).

## What was assumed

The open-axis doc lists, as a hard invariant the surviving kernel `F(q)` must
satisfy (criterion **2(b)**):

> *"bar-evenness / `q↦q⁻¹` symmetry of any `F(q)` (the `c₂ = −1` rung is bar-even)."*

## What the symbolic check shows

Using the substrate forms (`qbeta_c3_jhopf_q0_vs_q1_comparison.py`):

| quantity | form | bar-parity (`q↦q⁻¹`) |
|---|---|---|
| Hoefsmit base `b` | `(q−q⁻¹)/(q+q⁻¹)` | **bar-ODD** (`b(q⁻¹)=−b(q)`; odd/even) |
| `ℏ_q²` | `(1−q⁻¹)²` | bar-covariant (`↦ q²ℏ_q²`) |
| **expansion variable `u`** | `b·ℏ_q²` | **bar-ODD-covariant** (`u ↦ −q²u`, verified) |
| `J_Hopf` | `−(q²+q⁻²)` | bar-EVEN |

A bar-**even** kernel `F(q)=Σ c_k u^k` in this `u` forces, term by term,

$$\boxed{\,c_k(q^{-1}) = (-1)^k\,q^{-2k}\,c_k(q)\,}.$$

**None of the documented coefficients satisfy it:**

| `k` | candidate | residual `c_k(q⁻¹) − (−1)^k q^{−2k}c_k(q)` | satisfies? |
|---|---|---|---|
| 2 | `c₂ = −1` (proved-exact) | `q⁻⁴ − 1` | ❌ |
| 3 | `c₃ = −2 − ℏ_q²` (near-match) | `≠ 0` | ❌ |
| 3 | `c₃ = J_Hopf(q)` (near-match) | `(−q¹⁰−q⁶−q⁴−1)/q⁸` | ❌ |

## Verdict

**Criterion 2(b) cannot be imposed on the `c_k` ladder in the variable `u`.** Its
justification — *"`c₂ = −1` is bar-even"* — conflates the bar-**invariance** of a
constant (`c₂(q⁻¹)=c₂(q)`, trivially true) with the **covariance law** a bar-even
`F` actually needs in the bar-odd-covariant `u`. Because `b(q)` is bar-ODD, that
law is `c_k(q⁻¹)=(−1)^k q^{−2k}c_k(q)`, which the proved-exact `c₂=−1` already
violates.

**Consistent picture (no contradiction with the framework):** the bar-symmetry
lives in the **full `Q_β`** — the bar-**odd** `sinh` partner of the bar-even
`cosh` meson scale (per the canonical framing) — not in `F(q)` over `u`. `Q_β =
Q_A · cos(α_eff) · Π(1+c_k u^k)`; the bar-parity must be tracked across all
factors, with `b(q)` bar-odd, not by demanding a bar-even `F` in `u`.

## Strengthening — the bar-oddness is *irreducible* (no reparametrization rescue)

One might hope a different expansion variable restores a bar-even `F`. It cannot.
A candidate monomial variable `v = b^a · ℏ_q^{2c}` transforms as

$$v(q^{-1}) = (-1)^a\,q^{2c}\,v(q)\qquad(\text{$b$ bar-odd, $ℏ_q^2$ bar-covariant}),$$

so `v` is bar-**invariant** only when `a` is even **and** `c = 0` — i.e. a variable
with **no `ℏ`**. But the `c_k` ladder is intrinsically an `ℏ`-expansion (`c ≠ 0`).
Hence **every `ℏ`-containing expansion variable is bar-covariant**, and a bar-even
kernel `F` in such a variable is impossible while the `c_k` are the documented
forms. Criterion 2(b) is therefore **definitively dropped**, not merely weakened:
the bar-symmetry *necessarily* lives in the full `Q_β` (bar-odd), never in `F`.

## Narrowing for the kernel hunt (the deliverable)

The next fibre-kernel search should **not** carry "`F` bar-even in `u`" as a
filter. Instead:

1. **Use a bar-definite variable explicitly.** Either find a bar-**invariant**
   small parameter `v` (replacing `u`) in which the `c_k` *do* become bar-definite,
   or carry the bar-ODD-covariance of `u` through `R(q,ξ)` directly.
2. **Anchor the parity on `Q_β` (bar-odd), not `F`.** The overall sinh parity is
   the real constraint; `F`'s parity is derived from it given the bar-odd `b(q)`
   and the `cos(α_eff)`/`Q_A` factors.

A constraint on `R(q,ξ)`, not a value — within the qkhc discipline (nothing
wired; `c_k` stay cal-anchored).

## Follow-up — the closed-form `Q_β` is bar-mixed too (parity is a *fibre* statement)

Testing the natural next step ("anchor the parity on `Q_β`") symbolically: the
closed-form `Q_β` core `(q²−2q−1)(q+1)/q³ = 1 − q⁻¹ − 3q⁻² − q⁻³` is **bar-MIXED**
(neither bar-odd nor bar-even; the `|·|` variant likewise). So the *literal*
archimedean closed form is **not** bar-definite — the "`Q_β` = bar-odd `sinh`
partner" statement is about its **structural origin** (`sinh` vs the `cosh` meson
scale), not a bar-parity of the evaluated closed form.

**Net:** bar-parity is **not a clean archimedean filter at any level** — neither on
`F(q)` in `u` (criterion 2b, refuted above) nor on the closed-form `Q_β`. If the
bar-involution constrains the kernel, it does so at the **fibre level** (formal-`q`,
pre-archimedean), consistent with CLAUDE.md's *"c_k live in the FIBRE … Im(q)
unconstrained at the fibre, Im(q₀)=0 only at the archimedean evaluation"* framing.
This is the disciplined place to mount any future bar-symmetry argument — on the
formal-`q` Habiro element, not the archimedean `Q_β(q₀)` or the real-`u` ladder.

*Caveat.* This isolates the `Π(1+c_k u^k)` factor; the `cos(α_eff)` and `Q_A`
factors carry their own bar-parity and a full accounting must include them.
