# Q_β fibre-kernel — criterion 2(b) prune (bar-even `b(q)`)

**Date.** 2026-06-20 (corrected 2026-06-21).
**Bean.** qkhc (Q_β kernel hunt, Stage C) — the fibre-level Habiro kernel `R(q,ξ)`.
**Type.** **Constraint / pruning** of the open-axis search criteria — *not* a
real-q closed-form value-hunt (forbidden) and *not* a refuted mechanism. This is
the sanctioned step-3 "narrow before you scan" of
[`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`](2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md).
**Probe.** [`computations/qbeta/qbeta_barparity_kernel_criterion_prune.py`](../../computations/qbeta/qbeta_barparity_kernel_criterion_prune.py)
→ `qbeta-barparity-kernel-criterion-prune.witness.json` (exact symbolic, sympy).

> **⮕ CORRECTION (2026-06-21).** An earlier version of this doc used a
> **non-canonical** `b(q)=(q−q⁻¹)/(q+q⁻¹)` (bar-ODD), which gives the **wrong**
> substrate step-size `u≈0.00102` — off by ~8× from the documented `u≈0.00852`.
> The canonical Hoefsmit base (matching `u≈0.00852`, the mainstream `c_k`
> probes, and `SilverAnchorGrounding.lean`, `b²=(q⁴+q²+1)/(q²+1)²`) is
> `b(q)=√((h²+3)/(h²+4))=√(q⁴+q²+1)/(q²+1)` with `h=q−q⁻¹`, which is **bar-EVEN**
> (`QOU.QBeta.hoefsmitBSq_bar_even`). The **verdict is unchanged** — criterion
> 2(b) is still refuted — but **there is no "parity-split"**: `u` is uniformly
> bar-even-covariant (`u↦+q²u`, no per-rung sign). See
> [`2026-06-20-hoefsmit-b-bar-parity-correction.md`](2026-06-20-hoefsmit-b-bar-parity-correction.md)
> (sibling fix `3f95b1ea`).

## What was assumed

The open-axis doc lists, as a hard invariant the surviving kernel `F(q)` must
satisfy (criterion **2(b)**):

> *"bar-evenness / `q↦q⁻¹` symmetry of any `F(q)` (the `c₂ = −1` rung is bar-even)."*

## What the symbolic check shows

| quantity | form | bar-parity (`q↦q⁻¹`) |
|---|---|---|
| Hoefsmit base `b` | `√(q⁴+q²+1)/(q²+1)` | **bar-EVEN** (`b²` is a function of `h²`, `h` bar-odd) |
| `ℏ_q²` | `(1−q⁻¹)²` | bar-covariant (`↦ q²ℏ_q²`) |
| **expansion variable `u`** | `b·ℏ_q²` | **bar-EVEN-covariant** (`u ↦ +q²u`, verified) |
| `J_Hopf` | `−(q²+q⁻²)` | bar-EVEN |

A bar-**even** kernel `F(q)=Σ c_k u^k` in this `u` forces, term by term (no
`(−1)^k` — `u` carries no per-rung sign):

$$\boxed{\,c_k(q^{-1}) = q^{-2k}\,c_k(q)\,}.$$

**None of the documented coefficients satisfy it:**

| `k` | candidate | residual `c_k(q⁻¹) − q^{−2k}c_k(q)` | satisfies? |
|---|---|---|---|
| 2 | `c₂ = −1` (proved-exact) | `q⁻⁴ − 1` | ❌ |
| 3 | `c₃ = −2 − ℏ_q²` (near-match) | `−(q−1)²−2+2/q⁶+(q−1)²/q⁸` | ❌ |
| 3 | `c₃ = J_Hopf(q)` (near-match) | `(−q¹⁰−q⁶+q⁴+1)/q⁸` | ❌ |

## Verdict

**Criterion 2(b) cannot be imposed on the `c_k` ladder in the variable `u`.** Its
justification — *"`c₂ = −1` is bar-even"* — conflates the bar-**invariance** of a
constant (`c₂(q⁻¹)=c₂(q)`, trivially true) with the **covariance law** a bar-even
`F` actually needs in the bar-even-covariant `u`. That law is
`c_k(q⁻¹)=q^{−2k}c_k(q)`, which the proved-exact `c₂=−1` already violates
(`q⁻⁴ ≠ 1`), as do both `c₃` candidates.

**No parity-split.** Because the canonical `b(q)` is bar-EVEN, `u` is uniformly
bar-even-covariant — there is **no** per-rung `(−1)^k` sign and **no**
"parity-split ladder". The prune stands purely on the documented `c_k` *values*
failing the (unsigned) covariance law, independent of any bar-oddness of `u`.

## Narrowing for the kernel hunt (the deliverable)

The next fibre-kernel search should **not** carry "`F` bar-even in `u`" as a
filter (the documented `c_k` violate the covariance it would require). The
bar-symmetry, if it constrains the kernel, must be reckoned at the level of the
full `Q_β` or the fibre object — see the follow-up below — not by demanding a
bar-even `F` in the real-`u` ladder.

A constraint on `R(q,ξ)`, not a value — within the qkhc discipline (nothing
wired; `c_k` stay cal-anchored).

## Follow-up — the closed-form `Q_β` is bar-mixed too (parity is a *fibre* statement)

The closed-form `Q_β` core `(q²−2q−1)(q+1)/q³ = 1 − q⁻¹ − 3q⁻² − q⁻³` is
**bar-MIXED** (neither bar-odd nor bar-even; the `|·|` variant likewise). So the
*literal* archimedean closed form is **not** bar-definite — the "`Q_β` = bar-odd
`sinh` partner" statement is about its **structural origin** (`sinh` vs the
`cosh` meson scale), not a bar-parity of the evaluated closed form.

**Net:** bar-parity is **not a clean archimedean filter at any level** — neither on
`F(q)` in `u` (criterion 2b, refuted above) nor on the closed-form `Q_β`. If the
bar-involution constrains the kernel, it does so at the **fibre level** (formal-`q`,
pre-archimedean), consistent with CLAUDE.md's *"c_k live in the FIBRE … Im(q)
unconstrained at the fibre, Im(q₀)=0 only at the archimedean evaluation"* framing.
This is the disciplined place to mount any future bar-symmetry argument — on the
formal-`q` Habiro element, not the archimedean `Q_β(q₀)` or the real-`u` ladder.

*Caveat.* This isolates the `Π(1+c_k u^k)` factor; the `cos(α_eff)` and `Q_A`
factors carry their own bar-parity and a full accounting must include them.
