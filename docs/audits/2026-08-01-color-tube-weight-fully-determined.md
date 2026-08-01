# The color-tube weight tensor `W` — from 8 free parameters to 0

**Date:** 2026-08-01
**Beans:** `qou-ctkw` → `qou-63n2`
**Verdict:** **`W` is fully determined by `q`**, modulo one named weighting
assumption. No target consulted, nothing tuned, nothing wired.

## The chain

`conj:inter-nucleon-channel-color-tube` open question 1 asked for the closed form
of the 9-element weight tensor `W_{c₁c₂}(F₁,F₂)`. It came down in three forced
steps, none of them fitted:

| step | mechanism | free parameters |
|---|---|---|
| bare | arbitrary nonneg normalised 9-vector per flavor pair | **8** |
| color side (PR #4506) | `T₁ ⊗ T₁ = A ⊕ T₁ ⊕ H` — isotypic basis from the discharged fiber action | **2** |
| isospin selection (PR #4510) | `I=½ ⊗ I=½ = I=1 ⊕ I=0`; exchange antisymmetry forces `I=1 → T₁`, leaving only the `I=0` A/H mix | **1** |
| quantum dimensions (this) | `[3]_q² = [1]_q + [3]_q + [5]_q` ⇒ `W_A : W_H = [1]_q : [5]_q` | **0** |

## The final step

The color-pair space is the tensor square of the `ℓ=1` (`T₁`) irrep, and its
q-deformed Clebsch–Gordan decomposition is **exact** (verified symbolically):

```
[3]_q²  =  [1]_q + [3]_q + [5]_q
```

— the q-analogue of `A ⊕ T₁ ⊕ H`, with quantum dimensions `[1], [3], [5]` in
place of `1, 3, 5`. Weighting each isotypic summand by its quantum dimension
fixes the `I=0` (deuteron) channel's mix as `W_A : W_H = [1]_q : [5]_q` — a
function of `q` alone.

At the substrate `q₀`: `W_A = 0.160760299107`, `W_H = 0.839239700893`.

## The falsifiable check (not tuned)

At `q → 1` the quantum dimensions degenerate to classical ones, so the mix
**must** become the classical dimension ratio `1 : 5`, i.e. `1/6 : 5/6` — exactly
the classical projector-trace weights computed independently in PR #4506. It
does. The weighting was fixed before evaluation, so this is a check, not a
tuning.

## The one assumption, named

That the isotypic weighting is by **quantum** dimension (the categorical /
q-Plancherel measure) rather than classical dimension. This is the canonical
choice in a quantum-group setting and is what the corpus already uses elsewhere,
but it *is* a choice — so the result is a derivation **modulo the q-dimension
weighting**, not an unconditional one. It is not tuned: it was fixed beforehand
and its `q → 1` limit is checked independently.

Also still conditional: the isospin step rests on
`InterfaceExchangeAntisymmetry` (PR #4510), a class with **no instance** —
a physical assumption about the interface, not nucleon Fermi statistics.

## Why the order matters

The deuteron binding was **not** used anywhere in this chain. That was
deliberate: with `W` now derived, the deuteron becomes an **independent check**
rather than an input. Had the mix been fixed against it, the check would have
been circular and the result a fit. Testing `W` against the deuteron — and
against the ν_SDP positivity question (`ctkw`) — is the natural next probe, and
it is now a genuine test.

## Cross-references

- [`2026-08-01-color-pair-isotypic-decomposition.md`](2026-08-01-color-pair-isotypic-decomposition.md) — the color side.
- [`conj:inter-nucleon-channel-color-tube`](../../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md) — open question 1.
- [`2026-06-21-nu-sdp-saturation-obstruction-and-critical-distance.md`](2026-06-21-nu-sdp-saturation-obstruction-and-critical-distance.md) — the ν_SDP arc a derived `W` was meant to feed.
