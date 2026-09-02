---
# qou-0ri8
title: 'ROAST: the c1 arithmetic-sequence thread is weak and aimed at the wrong regime'
status: completed
type: task
priority: normal
created_at: 2026-08-31T16:52:46Z
updated_at: 2026-08-31T16:54:01Z
---


## The claim being roasted

I closed the previous turn with:

> over a common denominator the three **bond** coefficients are `pp = 38/16`,
> `pn = 37/16`, `nn = 36/16` — an exact arithmetic sequence, decreasing by
> `1/16` per proton→neutron swap. That looks derivable the way `c₀` was, and if
> `c₁(A)` has a closed form the same way, the **exact leading-order binding is
> known for every A** — which is a much bigger piece of the primary goal than
> anything else on the list.

Four things wrong with it, in increasing order of seriousness.

### 1. Three points, two parameters. One degree of freedom.

An "arithmetic sequence" through three values is fitted by (start, spacing) — two
parameters for three numbers. That is **one** degree of freedom of evidence. And
there is no fourth bond type to test against: `pp`, `pn`, `nn` exhaust the
2-nucleon flavour content, so the claim is **untestable at `A = 2` by
construction**. I presented a 1-dof observation as a pattern.

### 2. It does not generalise, and I already had the data that shows it

`T = 163/64` and `³He = 85/32 = 170/64` differ by one proton→neutron swap, same
as `pp → pn`. The increment there is **7/64**, not `1/16 = 4/64`.

So "decreasing by `1/16` per proton→neutron swap" is an `A = 2` coincidence, not
a rule, and the numbers refuting it were in the table I was reading from when I
wrote the claim. The sign is consistent (more protons → larger `c₁`); the
magnitude is not. Any closed form would have to be more than linear in `N − Z`.

### 3. "Derivable the way `c₀` was" was an analogy with nothing behind it

`c₀` is derivable because it is a **character value**: at `q = 1` the Markov
trace is `2^{c(σ)−n}` by Schur–Weyl, and the cycle count is a permutation
computation. That is a specific structural reason, not a general one.

`c₁` is the first **derivative** of the trace in `ℏ_q`. It is not a character
value of anything, and there is no corresponding representation-theoretic handle.
I asserted the analogy because both are dyadic rationals. Being dyadic is a
consequence of denominators `2^{3A}`, which every coefficient in this expansion
will share — it is not evidence of a common derivation.

### 4. The sharpest one: I proposed chasing the regime I had just shown is wrong

In the same report I established that the floor-corrected chain/atom ratios are
`1.118 / 1.020 / 1.194` at `q₀` and `1.791 / 1.765 / 3.429` at **leading order**
— i.e. the good agreement at `q₀` is higher-order terms cancelling a large
leading-order error, and pairwise additivity is *not* a controlled approximation.

Then I recommended investing in an exact closed form for the **leading-order**
coefficient. That is asking for an exact handle on the regime that demonstrably
does not describe the physics at `q₀`. The two halves of my own report do not sit
together.

### And the payoff was oversold anyway

"The exact leading-order binding is known for every `A`" would be, at best, the
exact leading-order **trace**. It is not binding, and it does not touch the
magnitude: the chain gives `6.89 MeV` for ⁴He against AME `28.30` — `4.1×` short
under convention A, `22×` under B. **I checked, and it is not scale choice**, so
knowing `c₁` exactly moves neither the `4.1×` nor the `23 MeV` α-residual.

## The near-miss that this roast actually turned up

The `c₁` values went into `QOU/MassTheory/PairwiseChainLeadingOrder.lean` as
definitions on the strength of a `limit_denominator(4096)` fit at `~1e-9`. That
is a weak identification, and I committed it before checking.

Re-checking at `η = 1e-12/1e-13` returned values **58–72 % away** from the
committed ones, which taken at face value would have falsified the Lean file. It
turned out the *re-check* was the artefact, not the commit — see `qou-v1cp`: the
trace routine is silently wrong below `η ≈ 1e-10` and returns flavour-degenerate
values. **The committed numbers are correct.**

But the process was wrong twice over: the identification was under-evidenced when
I made it, and I only verified it because a roast was asked for. The right time
to scan several decades was before writing the definitions, not after.

## What to do instead

**Drop this thread.** It is a weak pattern, refuted in its generalisation by data
already in hand, aimed at the wrong regime, with an oversold payoff.

The binding gaps that are actually load-bearing, in order:

1. **The `4.1×` magnitude shortfall at ⁴He.** Not scale choice (checked, both
   conventions fail). This is the primary gap and nothing this session has moved
   it.
2. **The `~23 MeV` 4-body α-residual**, which `derive_binding_chain_cooperative`
   already localises and which grew slightly under the floor correction. Whether
   the α-unit has a categorical representation at all is the long-standing open
   question (`t7qv`), and it is where the binding magnitude actually lives.
3. **`qou-v1cp`** — fix the silent `η` failure, because every future `ℏ_q`-limit
   measurement in this lane runs through the routine that has it.

Of those, (3) is small and certain; (1) and (2) are the real physics and neither
has a cheap attack. **Say so rather than manufacture one** — the pattern this
bean is roasting is exactly the manufacture of a cheap attack when the expensive
ones are the real work.
