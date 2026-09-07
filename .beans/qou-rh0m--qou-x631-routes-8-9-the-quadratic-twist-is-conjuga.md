---
# qou-rh0m
title: 'qou-x631 routes 8-9: the quadratic twist is conjugation -- it proves the odd-class vanishing but is sign-blind'
status: done
type: task
created_at: 2026-09-07T04:29:23Z
updated_at: 2026-09-07T04:29:23Z
---


Asked directly: is there a **quadratic twist** in the self-duality / Frobenius
pairing picture? **Yes — and it is the only one `S_k` has.** This settles what it
buys and what it cannot.

## The twist

Twisting by the sign character — the unique quadratic character of `S_k` — sends
`S^λ ↦ S^λ ⊗ sgn = S^{λ'}`. So the twist involution *is* transposition of the
Young diagram, and **self-dual = self-conjugate**. On symmetric functions it is
`ω`, with `ω(s_λ) = s_{λ'}` and `ω(p_μ) = ε_μ p_μ`, `ε_μ = sgn(μ)`.

## What it gives (1): a one-line proof of the odd-class vanishing

Let `P_k := Σ_λ (f^λ)² s_λ`, so `S_μ = ⟨p_μ, P_k⟩` in the Frobenius (Hall)
pairing. Since `f^{λ'} = f^λ`, `P_k` is **ω-invariant**; `p_μ` is
**ω-anti-invariant** for odd μ; and **ω is an isometry**. Hence

    S_μ = ⟨ω p_μ, ω P_k⟩ = ε_μ S_μ   ⟹   S_μ = 0 whenever ε_μ = −1.

This is orthogonality of the two ω-eigenspaces — cleaner than the term-pairing
argument in `qou-cze8`, and the right way to state it.

## What it gives (2): two-sided bounds, from positivity

`A := Σ_λ f^λ e_λ` acts on the λ-block by `f^λ > 0`, so `A` is a **positive**
element of `ℂ[S_k]` and `σ ↦ A(σ) = T_{type(σ)}/k!` is positive-definite.
Restriction to a subgroup preserves that, so `Σ_{h∈H} A(h) ≥ 0`:

| H | constraint |
|---|---|
| `⟨3-cycle⟩ ≅ ℤ/3` | `M(k) + 2·T₃(k) ≥ 0` |
| `A₄` | `M(k) + 3·T_{(2,2,1^{k−4})}(k) + 8·T₃(k) ≥ 0` |

with `M(k) = Σ_λ (f^λ)³`. Both verified, k ≤ 13. Cauchy–Schwarz on the same
positivity gives `|S_μ| ≤ M(k)`.

## What it does NOT give — the point

**Every constraint positivity yields is a LOWER bound on `T₃`.** The conjecture
is an **upper** bound. The quadratic structure is **sign-blind in the direction
needed**, and not close: at k = 13, `T₃ ≈ −5.1×10¹¹` against a ℤ/3 bound of
`−4.4×10¹³` — two orders of magnitude of slack.

## Route 8, eliminated: splitting by the twist orbit

The refinement self-duality actually suggests is `T₃ = SC + PR` — self-dual
shapes versus 2-element twist orbits — proving each negative. **Both change
sign:**

    SC > 0  at k = 7 (+800), k = 9 (+38416)
    PR > 0  at k = 3, 4, 6 (+252), k = 10 (+3015552)

So no argument treating self-dual and paired shapes separately can work; `T₃ ≤ 0`
is a genuine cancellation *between* the twist orbits. Distinct from the epic's
earlier "sub-family sign-definiteness" elimination, which concerned shape
families (two-row, hooks) rather than the twist orbit.

## Where this leaves the search

Consistent with `qou-ujil`: the effect is an O(1) correlation at the CLT scale.
Neither the twist nor positivity sees a correlation — both are exact-algebraic
and scale-free, while the signal is asymptotic and sits at `k^{3/2}`. That is why
they give equalities (odd classes) and inequalities of the wrong sense, but never
the conjecture.
