# `f₁/f₀` reduces to two per-letter weights — one derivable, and the reduction is unfalsifiable here

**Attempts** the step named as highest-value by the `L1` audit: derive
`f₁/f₀ = (21Z + 16N)/2`, the single remaining empirical input in that chain.

**Partial, with a structural negative that matters more than the partial.** The
coefficient reduces to two per-letter weights, one of which now has a candidate
derivation. But the reduction **cannot be tested by any `(Z,N)` data**, and I
came close to reporting the automatic check as confirmation.
Beans `qou-brng` / `qou-pdg9`.

## Where 21 and 16 come from

Not a mystery — the probe says so at
[`c1_leading_coefficient_derived_probe.py:554`](../../computations/probes/c1_leading_coefficient_derived_probe.py):

    # proton 6σ+3σ⁻¹ → 21, neutron 5σ+4σ⁻¹ → 16

They are the **nucleon letter census**. Solving

    6·w₊ + 3·w₋ = 21          (proton)
    5·w₊ + 4·w₋ = 16          (neutron)

gives `w₊ = 4`, `w₋ = −1`, i.e. after the overall ½,

    f₁/f₀ = 2·n₊ − n₋/2 ,   n₊ = 6Z + 5N ,  n₋ = 3Z + 4N

which reproduces all six recorded values (21, 37/2, 16, 53/2, 29, 37).

## 🛑 The six-case agreement is AUTOMATIC — it is not evidence

Two unknowns were solved from two equations. Every case then has census

    (n₊, n₋) = Z·(6,3) + N·(5,4)

so **every `(Z,N)` lies in the cone spanned by the two nucleon words that fixed
the weights.** A linear functional agreeing on two generators agrees on every
non-negative combination of them, identically.

**Consequence, and it is the main finding here: the per-letter hypothesis is
unfalsifiable within this family.** More `(Z,N)` cannot over-determine it — not
A = 5, not A = 6, not the A = 2..20 range the probe already asserts. Any effort
spent extending `(Z,N)` to "confirm" it buys exactly nothing.

This is worth stating plainly because the six-row table *looks* like
confirmation, and I nearly filed it as such.

## What the reduction is, stated at its true strength

It is a **reparameterisation**: two per-nucleon constants (21, 16) → two
per-letter constants (2, −½) plus additivity of `log tr_free` over letters. That
is a real gain in economy and it makes the next question sharper — *why these
two weights?* — but it is not new evidence, and it does not derive `f₁/f₀`.

## One weight has a candidate derivation; the other does not

With the convention-D Markov parameter `z = q³/(q²+1)`:

    d/dq log z |_{q=1} = 2          ← exactly the σ weight
    bar partner z(1/q):  −2         ← NOT the σ⁻¹ weight, which is −½

So the σ half has a plausible origin in the Markov parameter's logarithmic
derivative at `q = 1`. **The σ⁻¹ half remains unexplained** — the obvious bar
partner gives the wrong value, off by a factor of 4 and not merely in sign.

## A trap checked rather than assumed

The weights invite the reading `2 = 1/z(1)` and `−½ = −z(1)`, since `z(1) = ½`.
**That is not evidence for convention D**, because

    convention D  z = q³/(q²+1)      z(1) = 1/2
    convention C  z = √q/(q+1)       z(1) = 1/2

`z(1) = ½` in **both**. The quantity that *does* discriminate is the derivative
— `2` for D against `0` for C — and that one genuinely favours D, but only for
the σ weight.

## What would settle it

A braid word whose census lies **outside the cone** spanned by `(6,3)` and
`(5,4)`. The current probe cannot express one: `tr_M_series(Z, N, …)` is
parameterised by nucleon counts, not by a word, so every input it accepts is in
the cone by construction. Testing the per-letter hypothesis needs a
word-level trace entry point that does not currently exist.

## Scope

- **`f₁/f₀` is NOT derived.** The chain from `L1` still rests on it.
- The reduction is exact algebra on the six recorded values; no new compute was
  run for it.
- The `d/dq log z` computation is symbolic (sympy) at `q = 1`, both conventions.
- Scope-(a): about the expansion of a computational object, not the physics.
