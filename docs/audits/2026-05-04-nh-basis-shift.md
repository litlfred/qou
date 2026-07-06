# Step 4 audit — NH_n basis braids: per-letter shift accounting

**Date.** 2026-05-04
**Branch.** `copilot/identify-multiplicative-chain`
**Witness.** [`computations/nh-basis-shift.witness.json`](../../computations/nh-basis-shift.witness.json)
**Script.** [`computations/nh_basis_shift.py`](../../computations/nh_basis_shift.py)
**Upstream.** [`docs/audits/2026-05-04-alpha-shift-torus-multiplicative-chain.md`](2026-05-04-alpha-shift-torus-multiplicative-chain.md)

## Question

The atomic-braid shift framework
([`docs/audits/2026-05-03-w3-habiro-unblocked.md`](2026-05-03-w3-habiro-unblocked.md))
splits

> shift = (max seminormal pole order over SYT axial-distance configs)
>           − Δ_within (Hecke σ²-reduction)
>           − Δ_cross  (Ocneanu y_λ cancellation)

Step 4 of the multiplicative-chain plan asks: in the **knot-by-knot
NH_n basis** (the GS / Coxeter normal-form basis of H_n(q)), can
we expose the same decomposition as a **per-letter** identity:

> shift_NF(b) = (one σ_i pole per NF letter) − (GB-reduction count)

with the GB-reduction count equal to the number of σ²-cancellations
the GS rewriting consumes?

## Method

For every w ∈ S_n with n ∈ {2, 3, 4, 5} (a total of
1 + 2 + 6 + 24 + 120 = 153 basis braids):

1. Pick the Matsumoto / right-greedy reduced word for w (canonical;
   independent of choice by braid relations within H_n(q)).
2. Build the seminormal Hoefsmit matrices σ_i ∈ ρ_λ(H_n(q))
   symbolically in q (sympy) for every λ ⊢ n. Compute χ_λ(T_w) = tr
   ρ_λ(T_w) ∈ ℚ(q) and `pole_order_at_zero(χ_λ)`.
3. `shift_full(w) := max_λ pole_order(χ_λ)` and
   `gb_reduction_count(w) := ℓ(w) − shift_full(w)`.
4. Cross-check against the cyclic Coxeter element
   (s_1 ⋯ s_{n-1})^k, which is the torus-knot generator from
   [`prop:alpha-shift-torus-knot`](../../content/quantum-observable-universe/braids-and-knots/alpha-shift-torus-knot.md).

## Result — empirical "no cancellation" theorem on the entire NH_n basis

For **every** w ∈ S_n at n ≤ 5, the witness records:

| n | # basis braids | max pole order | maximizer λ           | `gb_reduction_count` |
|---|---------------:|---------------:|-----------------------|----------------------:|
| 2 | 2              | 1              | (1,1)                 | 0 (always)           |
| 3 | 6              | 3              | (1,1,1)               | 0 (always)           |
| 4 | 24             | 6              | (1,1,1,1)             | 0 (always)           |
| 5 | 120            | 10             | (1,1,1,1,1)           | 0 (always)           |

That is: **for every basis braid b ∈ NH_n with n ≤ 5, the seminormal
pole order at q = 0 saturates the per-letter upper bound exactly:**

> shift_NF(b) = ℓ(b),
> gb_reduction_count(b) = ℓ(b) − ℓ(b) = 0.

The maximizer is always the all-anti-symmetric channel V_{(1^n)}.
The longest element w_0 ∈ S_n (the n-cell column reversal) achieves
the global max ℓ(w_0) = n(n − 1)/2 = pole order.

### Cross-check with `alpha_shift_torus.py`

| (p, k) | reduced word length | computed pole | k(p − 1) | match |
|--------|--------------------:|--------------:|---------:|:------|
| (2, 3) | 3                   | 3             | 3        | ✓     |
| (2, 5) | 5                   | 5             | 5        | ✓     |
| (3, 4) | 8                   | 8             | 8        | ✓     |

For the cyclic Coxeter element (s_1 ⋯ s_{n-1}), n ∈ {2, 3, 4, 5}
the witness records pole order = n − 1, matching the closed form
`alpha_shift(T_{n,1}) = 1 · (n − 1)` from
[`prop:alpha-shift-torus-knot`](../../content/quantum-observable-universe/braids-and-knots/alpha-shift-torus-knot.md).

**11 / 11** witness assertions pass.

## Interpretation

### Why does GB reduction = 0 on the entire S_n basis at low rank?

Each σ_i in the Matsumoto-reduced word is *already* in normal form:
no σ_i² substring appears (otherwise the word would not be reduced),
so the Hecke rewriting σ_i² = (q − q⁻¹)σ_i + 1 never fires. Every
σ_i contributes its full eigenvalue spectrum {q, −q⁻¹} to the
seminormal matrix product, and the all-anti-symmetric channel
V_{(1^n)} consistently picks up the full −q⁻¹ pole at every step
because:

- Every irreducible λ ⊢ n with at least two rows has at least one
  row of length ≥ 2; on the row, two consecutive entries (i, i+1)
  give axial distance +1, and the corresponding σ_i acts in a
  Hoefsmit 2 × 2 block that is *not* purely diagonal in (−q⁻¹).
- Only the column shape λ = (1^n) forces every consecutive pair
  (i, i + 1) into a column with axial distance −1, where σ_i acts
  as the scalar −q⁻¹.

So the column SYT path always wins, and the per-letter upper bound
is *tight* on V_{(1^n)} — for any reduced word, not just the
cyclic Coxeter element.

### Cross-link to the atomic-braid framework

The per-letter additive decomposition
([`docs/audits/2026-05-03-w3-habiro-unblocked.md`](2026-05-03-w3-habiro-unblocked.md))

> shift = max pole order − Δ_within − Δ_cross

reduces in the NH_n basis to

> shift_NF(b) = ℓ(b) − 0 − 0 (n ≤ 5)

i.e. the basis braids individually have **no within-partition
σ²-cancellation** (they are reduced) and **no cross-partition
Ocneanu cancellation** (because the maximizer is unique:
V_{(1^n)}). The cancellations Δ_within, Δ_cross only switch on for
**products of basis braids** (compounds β₁ ⋆ I ⋆ β₂) where the
unreduced concatenation forces σ²-rewriting and the Ocneanu trace
mixes channels — which is precisely the regime addressed by Step 5.

### Why this strengthens
[`prop:alpha-shift-torus-knot`](../../content/quantum-observable-universe/braids-and-knots/alpha-shift-torus-knot.md)

The torus-knot proposition states `α_shift(T_{p,k}) = k(p − 1)` on
V_{(1^p)} for the *cyclic* Coxeter element. Step 4 shows the same
mechanism — single column, all axial distances −1, no
cancellation — is responsible for **every** basis braid's pole
order at low rank. The closed form is the n = p restriction of a
strictly more general identity on NH_n, namely

> shift_NF(T_w) = ℓ(w) for all w ∈ S_n, n ≤ 5,

which is the *clean* (no-cancellation) regime of the GS-NF basis.

## Limitations

- n ≤ 5 only; full S_5 = 120 basis braids takes ≈ 30 s with sympy
  symbolic Hoefsmit. n = 6 (720 braids) and n = 7 (5040) would
  require a numerical / interval-arithmetic switch.
- The "GB reduction count" is defined here as ℓ(w) − shift_full(w);
  it equals the *gap* but does not provide an explicit GS rewriting
  trace. A future step could thread the gap to specific
  σ_i² → (q − q⁻¹)σ_i + 1 rewrites in the GS reduction sequence.
- The empirical "no cancellation on the entire NH_n basis" result
  is a strong claim that we have not yet attempted to prove
  categorically; that proof would observe that the column SYT path
  is the unique pole-saturating path on V_{(1^n)} *and* that this
  channel always achieves the global max — both elementary
  Hoefsmit-axial-distance facts.

## Where it lands

- **Witness:** [`computations/nh-basis-shift.witness.json`](../../computations/nh-basis-shift.witness.json)
- **Script:** [`computations/nh_basis_shift.py`](../../computations/nh_basis_shift.py)
- **Strengthens:** [`prop:alpha-shift-torus-knot`](../../content/quantum-observable-universe/braids-and-knots/alpha-shift-torus-knot.md)
- **Feeds:** Step 5 audit (`docs/audits/2026-05-04-nh-knots-confinement-shift.md`) — provides the baseline shift_NF(b) table that the LP/SDP confinement comparison post-projects against.
