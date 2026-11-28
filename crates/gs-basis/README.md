# `gs-basis`

A standalone, publication-grade pure-Rust (`#![forbid(unsafe_code)]`, zero C-FFI, `wasm32`-compatible) scientific computer-algebra library for **non-commutative Gröbner–Shirshov bases**, **matrix-free Iwahori–Hecke / Temperley–Lieb layer-peeling traces**, and **oriented toric binomial reductions**.

## Capabilities

1. **Exact Coefficient Rings (`scalar`, `dyadic`)**
   - `RingScalar` (`CoeffRing`) trait with exact arithmetic, unit inversion (`try_inv`), and exact division (`try_div_exact`).
   - Built-in rings: `i64`, `num_bigint::BigInt`, `num_rational::BigRational`, GCD-free dyadic rationals `DyadicScalar` ($\mathbb{Z}[\frac{1}{2}]$) and dense-window dyadic Laurent polynomials `DyadicLaurent` ($\mathbb{Z}[\frac{1}{2}][q, q^{-1}]$), sparse Laurent polynomials `LaurentPoly<R>` in $R[q, q^{-1}]$ (with $h = q - q^{-1}$ and quantum integers $[n]_q$), and truncated $h$-jet rings `TruncatedJet<R, K>` representing $R[h]/(h^{K+1})$.
   - Standalone `gs-peel` JSON CLI (`src/bin/gs-peel.rs`) exposing batch dyadic Hecke normal-form walks, Temperley–Lieb dyadic loop-closure trace walks, homogeneous division-free Markov tower peeling, and monotone two-row Bratteli sweeps.

2. **Free Associative Algebras & Admissible Monomial Orders (`order`, `free_alg`)**
   - `FreeAlg<G, R>` over any ordered generator alphabet `G: Ord + Clone + Hash`.
   - Two-sided multiplication-compatible well-orders (`MonomialOrder<G>`): `DegLex`, `DegRevLex`, `DegRightLex`, and `WeightedDegLex`.

3. **Dynamic Buchberger–Shirshov Engine (`shirshov`)**
   - Overlap ($ab$ vs $bc$) and inclusion ($abc$ vs $b$) S-polynomial compositions (Diamond Lemma).
   - Interreduction (`autoreduce`), leftmost-innermost normal-form reduction (`reduce`), and configurable `CompletionConfig` (`max_degree`, `max_filtration_order`, `max_iterations`) producing an auditable `CompletionCertificate`.

4. **Specialized Combinatorial Normal-Form Backends (`hecke`, `temperley_lieb`)**
   - `BokutShiaoHecke<R>`: exact type-$A$ Iwahori–Hecke algebra $H_n(q)$ normal forms via Coxeter permutation multiplication and lexicographically minimal reduced words, matching the Bokut–Shiao / Kang–Lee–Lee–Oh Gröbner–Shirshov completion.
   - `TemperleyLiebBasis<R>`: planar non-crossing diagram algebra $TL_n(\delta)$ of Catalan dimension $C_n = \frac{1}{n+1}\binom{2n}{n}$, exact loop-counting composition, Markov loop closure trace, and skein projection $\sigma_i \mapsto q\,\mathbf{1} - e_i$.

5. **Matrix-Free Hecke Layer-Peeling & Transfer Sweeps (`peel`)**
   - `peel::markov_tower`: streaming GS multiplication + inductive Ocneanu–Markov generator peeling down $H_n(q) \to H_{n-1}(q) \to \dots \to H_1(q)$ without constructing representation matrices.
   - `peel::chain_transfer`: Hecke-only $2\times 2$ transfer-matrix reduction of block-ordered chain elements $\Xi_n = \prod_{i=0}^{n-2}\prod_k (c_{i,k}\sigma_i + d_{i,k})$ in $\binom{n-1}{2}$ block multiplications.
   - `peel::bratteli_two_row`: multiplicity-free Young–Hoefsmit Gelfand–Tsetlin edge transfer sweep computing exact characters $\chi^\lambda(\beta)$ and Catalan-scaled two-row ($\ell(\lambda) \le 2$) traces.

6. **Oriented Toric Binomials & Stratum Column Promotion (`binomial`)**
   - `BinomialBasis` & `pottier_graver_basis`: Conti–Traverso / Graver vector rewriting over $\mathbb{N}^m$ preserving $A u = b$ for any integer matrix $A \in \mathbb{Z}^{d \times m}$, LP reduced-cost certificates $\bar{c}_j(y)$, and functorial column promotion $A_{k+1} = A_k M_{k\to k+1}$.

## Quick Example

```rust
use gs_basis::{
    CompletionConfig, DegLex, FreeAlg, LaurentPoly, NormalFormBasis, ShirshovEngine,
};

type Laur = LaurentPoly<i64>;

let h = Laur::h(); // q - q^{-1}
let s0 = FreeAlg::<usize, Laur>::generator(0);
let s1 = FreeAlg::<usize, Laur>::generator(1);
let one = FreeAlg::<usize, Laur>::one();

// Presentation of H_3(q): sigma_i^2 = h*sigma_i + 1 and sigma_0*sigma_1*sigma_0 = sigma_1*sigma_0*sigma_1
let rels = vec![
    &(&s0 * &s0) - &(&s0.scale(&h) + &one),
    &(&s1 * &s1) - &(&s1.scale(&h) + &one),
    &(&(&s1 * &s0) * &s1) - &(&(&s0 * &s1) * &s0),
];

let mut engine = ShirshovEngine::from_relations(rels, DegLex).unwrap();
let cert = engine.complete(&CompletionConfig::default()).unwrap();
assert!(cert.is_complete);

let lhs = engine.reduce(&(&(&s1 * &s0) * &s1));
let rhs = engine.reduce(&(&(&s0 * &s1) * &s0));
assert_eq!(lhs, rhs);
```
