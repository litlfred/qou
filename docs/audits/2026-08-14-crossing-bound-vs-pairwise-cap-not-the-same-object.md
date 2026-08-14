# The two `C(n,2)`s are not the same object

Bean `qou-81gl`. Probe:
[`crossing_bound_vs_pairwise_cap_probe.py`](scripts/crossing_bound_vs_pairwise_cap_probe.py),
witness [`…witness.json`](scripts/crossing_bound_vs_pairwise_cap_probe.witness.json).

Two results in the corpus carry the binomial `C(n,2)`:

| result | statement | shape |
|---|---|---|
| `QOU.Braiding.card_allPairs_le_length` (Ch 9, PR #5021) | a braid word whose net permutation reverses all `C(n,2)` strand pairs has length `≥ C(n,2)` | **lower** bound on a **count** |
| `QOU.MassTheory.exchangeDet_pow_two_le_four` | `ρ_A(m) := b_A(m)/b_2(m) ≤ C(A,2)`, where `b_A(m) = −ln det(I + m(J−I)_A)` | **upper** bound on a **ratio** |

The second is the proved exclusion behind *"the missing extensive binding term
must be super-pairwise."* If the first were the same fact seen from the braid
side, the two could be unified and the braid side would inherit a constraint on
binding. This audit tests that and reports the negative.

## The shared binomial is real, and it is `|E(K_n)|` in both places

Expanding `b_A(m) = −ln[(1 + (A−1)m)(1−m)^{A−1}]` at small `m` gives
`b_A(m) = m²·A(A−1)/2 + O(m³)`, so `ρ_A(m) → C(A,2)` as `m → 0`. Measured at
50 dps:

| A | `C(A,2)` | `ρ_A(10⁻¹²)` | abs err |
|---|---|---|---|
| 3 | 3 | 2.999999999998 | 2.0e-12 |
| 4 | 6 | 5.999999999992 | 8.0e-12 |
| 6 | 15 | 14.99999999996 | 4.0e-11 |
| 8 | 28 | 27.999999999888 | 1.12e-10 |

So this is **not** a bare numerical coincidence: `C(A,2)` in the cap is
genuinely the edge count of the complete graph `K_A`, exactly as `C(n,2)` in the
crossing bound is the number of strand pairs. The vocabulary is shared.

That is also the whole of what is shared. Counting the edges of `K_n` is what
the word *pairwise* means; two results that both count pairs have the same
subject matter, not the same content.

## Incidental finding: the cap is approached, never attained

Sweeping `m` over `(0,1)`, the supremum of `ρ_A` sits at the `m → 0` endpoint
and the cap is never reached at finite coupling:

| A | `C(A,2)` | max `ρ_A` on the grid | at | exceeds cap |
|---|---|---|---|---|
| 4 | 6 | 5.99201795611071342 | m = 0.001 | no |
| 6 | 15 | 14.9601493985142026 | m = 0.001 | no |
| 8 | 28 | 27.8885847151907477 | m = 0.001 | no |

The name *saturation cap* suggests a value the ratio attains. It does not: it is
the weak-coupling limit and an upper envelope everywhere else. This strengthens
rather than weakens the existing exclusion — the pairwise cumulant falls *short*
of `C(A,2)` at every physical `m`, so it falls further short of
`ρ_strong(4) ≈ 13` than the cap alone states.

## Why no bridge exists

The decisive point is not the direction of the inequalities, though they do run
opposite ways on different quantities. It is that **word length does not control
any magnitude the binding reads.**

Binding enters through the Markov trace `tr_M(β)`, and `tr_M` is not monotone in
the length of `β`. The witness is immediate: `σ₁σ₁⁻¹` has length 2, net
permutation the identity, and zero crossed pairs — the same trace as the empty
word. A *lower* bound on the number of letters therefore induces no lower bound
on a trace-derived magnitude, which is the only direction that could interact
with an *upper* cap on `ρ_A`.

The two results never meet. **Verdict: not the same object. Scope-(a)** — this
says the crossing bound supplies no constraint on the extensive term, not that
no relation between braid combinatorics and binding magnitude exists.

## The trap, recorded

There is a second, more tempting inference here, and it is wrong:

> `prop:pairwise-interaction-decomposition` says there is no `n`-ary braiding
> generator. The missing extensive term must be super-pairwise. Therefore the
> missing term cannot exist.

This is the category error AGENTS.md names under
§"Before declaring refuted": *a compositional / additive / trace object is
already many-body*. The proposition forbids a super-pairwise **generator**. It
says nothing about a super-pairwise **value**, and a Markov trace of a word
built from 2-strand letters is already a many-body object — that is what a trace
does. The saturation cap's conclusion is untouched by the pairwise principle,
and the search for the extensive term is not narrowed by it.

Recording this because the inference is one step from the material and reads as
a result.

## What was not checked

- Whether any *other* braid-side quantity — writhe, exponent sum, Seifert genus,
  reduced word length in a fixed normal form — does control `tr_M` well enough
  to interact with the cap. Only length was tested, because length is what the
  crossing bound bounds.
- The `A ≠ 4` cases of the cap in Lean. `exchangeDet_pow_two_le_four` is proved
  for `A = 4`; the small-`m` limit above is consistent with the general
  `ρ_A ≤ C(A,2)` but this probe does not prove it.
