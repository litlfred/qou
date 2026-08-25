# C1's `∞` has no *local isoformal* Stokes data — but `qou-wgnx`'s Stokes multipliers are a different object and remain open

**Date:** 2026-08-08 · **Axis:** C1 `∞`-residual (`qou-vkg5`) · **Tier:** correction
of my own claim + one Lean instance. **No fit, nothing wired.**

> ## 🛑 READ THIS FIRST — two different objects share the name "Stokes multiplier"
>
> An earlier draft of this audit was titled *"There is no Stokes multiplier at
> C1's `∞`"* full stop. That phrasing is **wrong and actively harmful**: it reads
> as voiding bean `qou-wgnx`'s open item #1, which is a real, live, meaningful
> target.
>
> | object | where | status |
> |---|---|---|
> | **local isoformal moduli at `∞`** — RSZ `F(P₁,…,P_k)`, the analytic moduli *within* one formal class at a single point | this audit | **dimension 0. Does not exist.** C1 is pure isoclinic at `∞` |
> | **the connection-matrix Stokes multipliers** — the data in `P = Y₀⁻¹Y_∞` between the theta-normalised solutions at `0` and at `∞` | [`qou-wgnx`](../../.beans/) | **OPEN, and the connection matrix + its invariant `χ` are already built** |
>
> This audit retracts a claim about the **first** object only. It says nothing
> against the second, which is global rather than local and is not constrained by
> any dimension count at a single point.

## The claim being retracted

Across PRs #4771 and #4783 I repeatedly wrote that the remaining open item was
*"compute C1's Stokes multiplier at `∞`"*, most recently as a scoreboard row:

> | **Stokes multiplier** | **OPEN — the only remaining item** |

**That item does not exist.** C1 at `∞` is **pure isoclinic**, and a pure
isoclinic module has no local q-Stokes phenomenon. Not "hard to compute" —
*nonexistent*.

## Why, from RSZ

Two independent statements, both already in the corpus:

**1. The dimension formula.** RSZ Thm 3.3.5,
`dim F(P₁,…,P_k) = Σ_{i<j} rᵢrⱼ(μⱼ − μᵢ)`. At `k = 1` the index set `{i < j}` is
empty, so the isoformal space is a point. Formalized in
[`RSZIsoformalInterface.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/RSZIsoformalInterface.lean)
as `rszIsoformalDim_one`, whose docstring I wrote in #4721 and which says, verbatim:

> *"A pure isoclinic module has no isoformal moduli, hence no Stokes data to
> extract."*

**2. The Stokes sheaf.** Per
[`2026-07-20-qlift-doorI-analytic-summation.md` §1](2026-07-20-qlift-doorI-analytic-summation.md)
reading RSZ §5.5.2 / Thm 5.5.7 / §4.4 directly: the q-Stokes matrices
`St_{λ₀}(λ;A)` are **upper-triangular unipotent** automorphisms inducing the
**identity on `gr M₀`**, and the phenomenon *is* the ambiguity between generic
divisor partitions among the slope pieces. With one slope there is no
strictly-upper-triangular part and nothing to partition: the Stokes group is
trivial.

Both say the same thing by different routes.

## That C1 is pure isoclinic at `∞` was settled three weeks before I started

[`2026-07-20-qlift-routeA-rsz-invariants.md` §2](2026-07-20-qlift-routeA-rsz-invariants.md):
the `∞` Newton polygon of `L1` has the single edge `(r,d) = (2,1)`, slope **½
with multiplicity 2** — *pure isoclinic, non-integral*, the irreducible rank-2
`E(2,1,·)` of RSZ §2.2.2.2 (restriction of scalars of a rank-1 slope-1 line on
the 2-cover). Machine-cross-checked there by an mpmath lower-hull script.

So the premise was in the corpus on 2026-07-20, I re-derived the same single edge
independently in #4721, wrote the dim-0 consequence into a Lean docstring in that
same PR — and then stated the opposite three times.

## How it happened

Not a computation error; a **framing** error, and the same shape as the one #4721
was written to fix. The 2026-08-01 chain said "slope ½ ⇒ two Stokes multipliers
`U ∈ ℂ²`". #4721 killed the *derivation* of that number, showing §3.3 does not
apply and `dim = 0` at `k = 1`. But I kept the *noun* — "the Stokes multiplier" —
as the name of the residual, and never re-asked whether the object survived its
own refutation. The corpus-grep checklist would have caught it: I grepped for
`{0,1,∞}`, for existing beans, for overlapping declaration names, but never for
`pure isoclinic`, which is the phrase that decides it and which returns six hits
across three prior audits.

## What is actually true about C1's `∞`

| item | status |
|---|---|
| formal class at `∞` | pure isoclinic, `E(2,1,c)`, slope ½ mult 2 |
| the class parameter `c` | determined: edge equation `q²t² = q−1`, product fixed by `det A`, residual freedom exactly the deck sign |
| weight lattice | `q^{½ℤ}`, up to deck sign |
| **analytic moduli within that formal class** | **a point — `dim = 0`. No Stokes data.** |

The local story at `∞` is therefore **closed**, not open. The "residual freedom"
I characterised in #4771/#4783 as constraining an unknown multiplier is in fact
the *whole* local invariant, and it is computed.

## What remains — and it was already being worked, under `qou-wgnx`

I originally listed "global connection data between `0` and `∞`" here as an
untouched successor target. **It is not untouched.** Bean `qou-wgnx`
("theta-normalised canonical solutions for C1") has been on it since 2026-08-07:

| result | status there |
|---|---|
| `∞`-side theta-normalised canonical solutions | built, substitution residual `1e-62` |
| connection matrix `P = Y₀⁻¹Y_∞` | obtained, `[[c₊,c₋],[c̄₊,c̄₋]]`, elliptic per entry |
| pole divisor, module exponents | symbolic, residue theorem confirms completeness |
| basis-**invariant** cross-ratio `χ = P₀₀P₁₁/(P₀₁P₁₀)` | order 2, closed form verified to `5.3e-63`, shape confirmed against Lin–Ma–Xu arXiv:2412.02281 Thm 1.2 |
| `QOU/QBeta/C1ConnectionPoles.lean`, `C1ZeroSideExponents.lean` | sorry-free |

Its open item #1 is the **Stokes multipliers proper** — functions of `χ`, the
remaining step being convention-dependent. That is a live target and nothing in
this audit touches it.

## A second correction: my `∞`-exponent value carried a silent `q^{1/4}`

In #4783 I wrote *"C1's `∞` exponent data is fully determined: the pair is
`±√(q−1)/q`"*. `computations/qbeta/c3_w2_c1_theta_canonical.py` has a section
headed, verbatim, **"The convention finding — read this before citing
`B = ±sqrt(q-1)/q`"**, recorded 2026-08-07 — the day before I started:

- `T_edge = ±√(q−1)/q` — root of the Newton **edge polynomial**. Correct as
  arithmetic about that polynomial.
- `T_theta = ±√(q−1)/q^{3/4}` — the parameter that indexes the theta-normalised
  canonical solutions, **hence indexes the Stokes sectors**.
- They differ by exactly `q^{1/4}`, and **the edge root provably does not satisfy
  the indicial equation**.

That script's verdict classifies the confusion as scope-(b) and names the failure
mode: *"an object computed correctly, then given a name whose meaning it does not
have."* I then did precisely that, and the warning was addressed to the exact
string I used.

**Consequence for #4771's weight lattice.** I proved there that the dilation lift
`c² = q` generates `q^{½ℤ}`. The *algebra* stands. But the sector-indexing
parameter is `T_theta ∼ q^{3/4} ∉ q^{½ℤ}`, so the gloss "C1's `∞` weight lies in
`q^{½ℤ}`" does not follow — it inherits the same silent `q^{1/4}`. The lattice
result should be read as a statement about the **dilation lift**, which is what
it proves, and not about the sector parameter.

## Process note

Three corrections in this arc, all the same shape: an object computed correctly,
then named as something it is not. The corpus had already diagnosed that pattern
and written a warning against the specific string I used. What failed was not
the mathematics but the search — I grepped for names I had invented rather than
for the concepts, and so never reached `qou-wgnx`, `c3_w2_c1_*`, or
`C1ZeroSideExponents.lean`.

## Landed with this correction

`c1_infinity_isoformalDim_eq_zero` in
[`RSZIsoformalInterface.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/RSZIsoformalInterface.lean):
the *instance*, not just the general lemma — C1's own `∞` data after the forced
ramified pullback (`k = 1`, `r = 2`, slope `1`) has isoformal dimension `0`. The
general fact was already there and got restated wrongly anyway; a named instance
mentioning C1 is harder to walk past.

-- Ref: [ramis-sauloy-zhang2013] https://arxiv.org/abs/0903.0853 (Thm 3.3.5, §4.4, Thm 5.5.7, §2.2.2.2)
-- Ref: [manuscript] docs/audits/2026-07-20-qlift-routeA-rsz-invariants.md
-- Ref: [manuscript] docs/audits/2026-07-20-qlift-doorI-analytic-summation.md
-- Ref: [manuscript] docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md
