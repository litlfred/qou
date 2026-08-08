---
# qou-vkg5
title: 'GAP: the Ecalle bridge equation (AlienDerivation §4) is unproved'
status: todo
type: task
created_at: 2026-08-08T13:55:07Z
updated_at: 2026-08-08T13:55:07Z
---


`QOU/Mathlib/AlienDerivation.lean`.

Its header used to list four things the file formalizes. Items 3 and 4 were
never in it — a plan read as an inventory. The header now says so (PR #4771).

**§3 is closed**, and the reason it was stuck is worth recording: the obstacle
was a single lemma missing from *Mathlib*, not from this corpus. `Derivation`
has `leibniz`, `leibniz_pow`, `leibniz_inv`, `leibniz_div` but no iterate —
`Nat.choose` appears nowhere under `Mathlib/RingTheory/Derivation/`. Supplied
as `QOU/MathlibExt/DerivationIterateLeibniz.iterate_leibniz`:

    Dⁿ(f·g) = Σ_{k≤n} C(n,k) · Dᵏf · D^{n−k}g

That binomial convolution *is* the Cauchy product of two exponential series,
which is why it is exactly what makes `exp(D)` multiplicative. Also landed:
`exp_leibniz_iff_cross_vanishes` — at `D² = 0`, `(1+D)` is multiplicative **iff**
`Df·Dg = 0`, i.e. at one-instanton order the automorphism property is
*equivalent* to the vanishing of the two-instanton cross-term.

**§4 — the bridge equation — is what remains open.** Écalle's statement relates
the alien derivatives to the ordinary derivative,

    Δ_ω ∘ ∂  −  ∂ ∘ Δ_ω  =  −ω · Δ_ω ,

so that the `Δ_ω` assemble into the "bridge" between the formal and analytic
sides. Nothing in the corpus asserts it and nothing depends on it.

## What a first honest attempt would need

1. **The commutator relation as a structure field, not a theorem.** `Δ_ω` is
   currently a bare `Derivation R A A` with no relation to a distinguished `∂`.
   The bridge equation is a *hypothesis* on the system, so it belongs as a field
   on `AlienDerivationSystem` (or a §3b conditional class) carrying the `−ω·Δ_ω`
   commutator — not as something to be derived from the present data, which
   cannot support it.
2. **Then the consequences are provable.** With the commutator as a hypothesis,
   the standard corollaries (the `Δ_ω` span a graded Lie algebra; `exp` of the
   sum factorises when the `Δ_ω` commute) become algebra, and `iterate_leibniz`
   is already in hand for the `exp` half.

## Do not

Do **not** add the bridge equation as an `axiom`, and do **not** state it as an
unconditional theorem about the existing `AlienDerivationSystem` — per
AGENTS.md §"Axiomatization is NOT a Proof", axiomatising it would not prove it,
and per §3b-cond a hypothesis-carrying class is the honest encoding.

Also unresolved and prior to all of this: the q-native question. C1 **cannot**
be confluenced to the classical setting (`L1 → (x−1)σ²`, not rank 2 —
[`2026-08-08-rsz-c1-infinity-route-closed.md`](../docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md)),
so a classical bridge equation would not transfer to it even once proved.
