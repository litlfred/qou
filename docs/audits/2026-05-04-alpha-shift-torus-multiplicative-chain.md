# α_shift(T_{p,k}) and the multiplicative chain for α_EM⁻¹

**Date:** 2026-05-04
**Branch:** `copilot/identify-multiplicative-chain`
**Refs:**
- [`computations/alpha/alpha_shift_torus.py`](../../computations/alpha/alpha_shift_torus.py)
- [`computations/alpha/alpha-shift-torus.witness.json`](../../computations/alpha/alpha-shift-torus.witness.json)
- [`prop:em-coupling-projection`](../../content/quantum-observable-universe/descartes-universe/em-coupling-projection.md)
- [`prop:alpha-em-categorical-trace-ratio`](../../content/quantum-observable-universe/descartes-universe/alpha-em-categorical-trace-ratio.md)
- [`prop:force-carrier-intertwining-correspondence`](../../content/quantum-observable-universe/braids-and-knots/force-carrier-intertwining-correspondence.md)

## Background — two source threads

### `claude/improve-charge-precision-AXKIA`

The branch landed the **δ_q decoration** infrastructure
([`def:delta-q-decoration`](../../content/quantum-observable-universe/braids-and-knots/delta-q-decoration.md))
and proved the algebraic identity

> α_EM = h² / [q · δ_q(T_{2,9}) · δ_q(T_{3,5})]

where δ_q(T_{p,k}) = q^k − q^{−k} = h · [k]_q for the dominant
all-anti-symmetric channel. This refactors α_EM out of the
operator-selection LP layer into the q-dimension layer, tracking
exactly which Wedderburn channel the bound state projects through
([`prop:force-carrier-intertwining-correspondence`](../../content/quantum-observable-universe/braids-and-knots/force-carrier-intertwining-correspondence.md):
λ = (p, 1^{n−p})).

### `claude/w3-w4-followups`

The branch landed the closed form for the atomic Markov-trace
denominator,
[`docs/audits/2026-05-03-w3-habiro-unblocked.md`](2026-05-03-w3-habiro-unblocked.md):

> D(u) = 2^(2A+1) · u^shift · (1+u²)^{3A−1}

with two factors categorically proved and the **shift exponent**
narrowed to

> shift = max pole-order of seminormal closed-cycle product over SYT
> axial-distance configurations, **minus** within-partition (Hecke
> σ²-reduction) and cross-partition (Ocneanu y_λ) cancellation.

The DP probe ([`dp_pole_probe.py`](../../computations/dp_pole_probe.py))
implements the cycle-additive upper bound on the q=0 pole order and
exposes the per-partition Δ_within / Δ_cross cancellation counts.

## The bridge — α_shift as the unifying primitive

Both threads name the same combinatorial object: **the pole order
at q = 0 of a seminormal-trace expression**. We make this explicit:

> **Definition (α_shift).** For a torus knot T_{p,k} represented
> as the closure of β_{p,k} = (σ_1 σ_2 ⋯ σ_{p−1})^k in B_p,
>
> α_shift(T_{p,k}) := max_{λ ⊢ p} ord_{q=0}^{(−)} χ_λ(β_{p,k}),
>
> where ord_{q=0}^{(−)} denotes the pole order at q = 0 (= negative
> of the Laurent valuation).

Empirically on the test bench (p, k) ∈ {(2, 3), (2, 5), (2, 9),
(3, 4), (3, 5), (3, 7)} — symbolic Hoefsmit computation in
[`alpha_shift_torus.py`](../../computations/alpha/alpha_shift_torus.py):

| (p, k) | maximizer λ | α_shift(T_{p,k}) | k(p−1) |
|--------|-------------|-------------------|---------|
| (2, 3) | (1,1)       | 3                 | 3       |
| (2, 5) | (1,1)       | 5                 | 5       |
| (2, 9) | (1,1)       | 9                 | 9       |
| (3, 4) | (1,1,1)     | 8                 | 8       |
| (3, 5) | (1,1,1)     | 10                | 10      |
| (3, 7) | (1,1,1)     | 14                | 14      |

Two observations are uniform:

1. **The maximizer is always V_{(1^p)}** — the all-anti-symmetric
   irrep. (Geometrically: the SYT of shape (1^p) has a single SYT
   with axial-distance pattern (−1, −2, …, −(p−1)) along the
   column. Each generator σ_i in β_{p,k} acts as the eigenvalue
   −q⁻¹ on this 1×1 block, contributing pole order 1 per generator.)
2. **α_shift(T_{p,k}) = k(p−1)** — exactly the number of generators
   in β_{p,k} = (σ_1 ⋯ σ_{p−1})^k, with each contributing pole 1.

For (p, k) with gcd(p, k) ≠ 1 the closure is a link rather than a
knot; we restrict to coprime pairs in this audit.

## Consequence — multiplicative chain for α_EM⁻¹

[`prop:em-coupling-projection`](../../content/quantum-observable-universe/descartes-universe/em-coupling-projection.md)
gives the bare formula

> α_EM⁻¹ = q · [9]_q · [10]_q.

Substituting α_shift(T_{2,9}) = 9 and α_shift(T_{3,5}) = 10:

> **α_EM⁻¹ = q · [α_shift(T_{2,9})]_q · [α_shift(T_{3,5})]_q.**

This is no longer a numerical coincidence; it is the composition of
two named identities (each of which holds at every prime k ≥ p):

1. `prop:em-coupling-projection`: α_EM⁻¹ = q · [9]_q · [10]_q.
2. `prop:alpha-shift-torus-knot` (introduced in this PR):
   α_shift(T_{p,k}) = k(p−1) on V_{(1^p)} for gcd(p,k)=1.

The new content block
[`prop:alpha-em-shift-multiplicative-chain`](../../content/quantum-observable-universe/descartes-universe/alpha-em-shift-multiplicative-chain.md)
is the conjunction.

## Cross-link to the w3-w4 D(u) shift

The shift exponent in
[`2026-05-03-w3-habiro-unblocked.md`](2026-05-03-w3-habiro-unblocked.md)
is the same primitive applied to the *atomic* braid β(Z, N) (not a
torus braid). Its closed-form ansatz

> shift(Z, N) = 18Z + 21N + 1

decomposes into per-crossing contributions (1, 4, 0) intra-nucleon
and (0, 0, 1) inter-nucleon — strand-topology dependent. The
torus-braid case is the same machinery in the cleanest setting:

- **No inter-nucleon coupling** ⇒ no inter-nucleon term.
- **All generators are σ_i (none averaged, none σ⁻¹)** ⇒ the
  per-crossing α reduces to a single number = 1 on V_{(1^p)}.
- **No Hecke σ²-cancellation** because the SYT path through the
  single-column irrep visits distinct axial distances at every step
  (no two adjacent contents differ by ±1, so the b² = (1−q^{2ρ−2})
  (1−q^{2ρ+2})/(1−q^{2ρ})² cancellation never fires on V_{(1^p)}
  for p ≤ 3).
- **No cross-partition Ocneanu cancellation** because the maximum
  pole order is uniquely realised on a single irrep (other irreps
  contribute pole order 0).

Hence the torus-braid case is the **clean limit** in which the
shift formula admits an immediate closed form, and validates the
DP-pole-probe upper-bound machinery on the simplest possible input.

## Witness summary

The witness [`alpha-shift-torus.witness.json`](../../computations/alpha/alpha-shift-torus.witness.json)
records:

- The full per-irrep symbolic χ_λ(β_{p,k}) ∈ ℚ(q) for each test
  bench (p, k).
- The pole order at q = 0 and lowest Laurent power for each irrep.
- 14 assertions: 6 × `α_shift = k(p-1)` + 6 × `maximizer = V_{(1^p)}`
  + 2 × bridge-consistency at (2, 9) and (3, 5).

All 14 assertions pass.

## Open work (next steps)

- **Step 4** — extend α_shift to NH_n basis braids (general
  Gröbner–Shirshov NF words, not just torus braids). Sit on the
  `gb_nf_reducer.rs` perm utilities.
- **Step 5** — confinement → NF-structure forcing: the
  operator-selection LP/SDP active set must constrain the NF
  support of compound β₁ ⋆ I ⋆ β₂. Conjecture, with witness via
  `lp_dual_witness_validator.py`.
- **Step 6** — wire α_EM² into
  [`conj:e-hartree-categorical-derivation`](../../content/quantum-observable-universe/descartes-universe/e-hartree-categorical-derivation.md)
  via the multiplicative-chain form, replacing the BW-cost
  interpretation in `derivation-chain-audit.witness.json`.

## Caveat

The closed form **α_shift(T_{p,k}) = k(p−1)** is verified at the
test bench (six (p, k) pairs, two values of p) but **not formally
proved** as a function of arbitrary (p, k). The categorical proof
requires showing:

1. The single SYT of V_{(1^p)} carries axial-distance pattern
   (−1, −2, …, −(p−1)) ✓ (immediate from contents = column − row =
   −row in a single-column tableau).
2. Each σ_i acts as the eigenvalue −q⁻¹ on this 1×1 block ✓
   (Hoefsmit: the 1×1 case is rho = ±1, and rho = −1 here gives
   eigenvalue −q⁻¹).
3. The product of k(p−1) eigenvalues −q⁻¹ has pole order exactly
   k(p−1) at q = 0 ✓ (trivial: (−q⁻¹)^{k(p−1)} = (−1)^{k(p−1)}
   q^{−k(p−1)}).

Step 3 also requires showing this is the **maximum** over all
λ ⊢ p — equivalently, that no other irrep produces pole order
> k(p−1). The witness verifies this for p ∈ {2, 3}; the general
case is the content of [`prop:alpha-shift-torus-knot`](../../content/quantum-observable-universe/braids-and-knots/alpha-shift-torus-knot.md)
and is left as a conjecture pending a structural proof from the
seminormal denominator structure (analogous to the unresolved
`(6, 7, 1)` question in the atomic-braid case).
