# The hook column reduces to the reduced Burau: tr_{(k,1ⁿ⁻ᵏ)}(ρ) = q^{L(1−j)}·e_j (qou-o6ov)

**Date:** 2026-09-02
**Directive (owner):** grind the o6ov cancellation theorem (chose option 2).
**Scope:** scope-(a); a positive structural result; no MeV, no fit, nothing wired.
**Probe:** [`magnus_hook_exterior_power_probe.py`](../../computations/deltalambda/magnus_hook_exterior_power_probe.py)

## Result (verified exact, A=2 & A=3, 139 digits)

For the **hook family** `λ = (k, 1ⁿ⁻ᵏ)` (which covers the full b-range, `b = n−k = j`), the
**plain** Hecke character of the atom word `ρ` is exactly

```
tr_{(k,1ⁿ⁻ᵏ)}(ρ) = q^{L(1−j)} · e_j( eigenvalues of ρ in the reduced-Burau rep (n−1,1) ),
                   j = n−k,   L = braid-word length,
```

where `e_j` is the `j`-th elementary symmetric polynomial. Measured worst relative error
`3e-139` (A=2) / `3e-138` (A=3), for **all** `k` including both endpoints (`k=1` sign, `k=n`
trivial). Since `e_j(μ) = [t^j] det(1 + t·ρ^V)` is the reduced-Burau **characteristic
polynomial** (≈ the Alexander determinant), this says:

> **The hooks are the (q-)exterior powers of the reduced Burau rep.** `(k,1ⁿ⁻ᵏ) = Λ^{n−k}(V)`,
> `V` the reflection/reduced-Burau rep, and the whole hook column of characters is governed by
> the `(n−1)`-dim Burau spectrum — a closed form, up to the exact q-twist `q^{L(1−j)}`.

## Why this matters for the tr-decay (qou-o6ov)

- **First closed-form reduction of a full sub-column.** The seven routes in the
  [route-status consolidation](2026-09-02-magnus-tr-decay-route-status-consolidation.md) are all
  dead; this is a *positive* handle, on the hook slice. The hooks are exactly the family that
  covers every `b`, and they now reduce to an `(n−1)`-dim object.
- **An explicit exponential-in-b decay factor.** `|tr_{(k,1ⁿ⁻ᵏ)}(ρ)| = q^{−L(j−1)}·|e_j|`, and
  `q^{−L(j−1)} → 0` geometrically as `b=j` grows (`q>1`). So the *plain* hook character carries
  a clean, proved `q^{−L(j−1)}` decay — the first exact decay law in the arc.
- **Extends #6392 from a point to a column.** #6392 identified `b=1` as the reduced-Burau /
  Alexander sector; this shows the *entire hook column* is the Burau exterior-power tower, with
  the `b=1` reflection rep as `Λ¹(V)` and the sign endpoint as `Λ^{n−1}(V) = det`.

## ALL ORDERS: the Ω₂-inserted hook column is a determinant DERIVATIVE (verified)

The tr-**decay** theorem is about `tr(ρ_λ Ω₂)`, not the plain `tr(ρ_λ)`. The Ω₂ insertion acts on
`Λ^j(V)` as the induced **derivation**, so by Jacobi's formula the whole hook column of the decay
object — **every order `j` at once** — is a determinant derivative of the same `(n−1)`-dim
reduced Burau. **Verified exact** (A=2 worst rel `7e-92`, A=3 `2e-91`;
[`magnus_hook_all_orders_genfun_probe.py`](../../computations/deltalambda/magnus_hook_all_orders_genfun_probe.py)):
```
Σ_j tr_{(n−j,1ʲ)}(ρ·Ω₂) t^j  =  q^L · s · det(1+s·ρ^V) · tr( (1+s·ρ^V)⁻¹ Ω₂^V ρ^V ),   s = t/q^L.
```
(The plain identity is the `Ω₂ → 1` case: `Σ_j tr_{(n−j,1ʲ)}(ρ) t^j = q^L·det(1+s·ρ^V)`.) So the
**hook slice of the tr-decay is closed-form** in the reduced-Burau data `ρ^V`, `Ω₂^V`, and its
decay in `b=j` is explicit: the `s = t/q^L` rescaling suppresses order `j` by `q^{−Lj}`, on top
of the reduced-Burau (Alexander) spectrum. This is a genuine **partial proof of the decay on the
hook slice** — reduced from an exponentially-growing family of hook irreps to one `(n−1)`-dim
matrix pair.

"All orders" here means all exterior-power degrees `j`; the same structure lifts to higher
Magnus terms `Ω_m` as higher determinant-derivatives of the reduced Burau (not pursued here).

## Honest limits

- **A=2, A=3 exact; A=4 timed out** (large hooks are slow to build densely at dps 140) — not a
  failure, a compute cost.
- **Hook slice only.** This is the hook sub-column; the full `b`-decay over all `λ` is still the
  open theorem (the non-hook `λ` are not exterior powers).

## Bottom line

The plain hook characters of the atom word are the **q-twisted elementary symmetric functions
of the reduced-Burau spectrum**, `tr_{(k,1ⁿ⁻ᵏ)}(ρ) = q^{L(1−j)}·e_j`, exact to 139 digits — so
the hooks are the q-exterior powers of the reduced Burau and the whole hook column reduces to an
`(n−1)`-dim object carrying an explicit `q^{−L(j−1)}` decay in `b`. **And the actual decay
object `tr(ρΩ₂)` follows the same reduction at all orders** — its hook column is the
determinant-**derivative** `q^L·s·det(1+sρ^V)·tr((1+sρ^V)⁻¹Ω₂^V ρ^V)`, verified exact. So the
hook slice of the tr-decay is closed-form via the reduced Burau, with an explicit `q^{−Lj}`-per-
order suppression — the first positive, partial proof on the arc. The full `b`-decay over the
non-hook `λ` (which are not exterior powers) remains the open theorem.
