#![forbid(unsafe_code)]
#![warn(missing_docs)]

//! # `gs-basis` — Non-Commutative Gröbner–Shirshov Bases, Dyadic Laurent Rings & Layer Peeling
//!
//! `gs-basis` is a standalone, pure-Rust library (`#![forbid(unsafe_code)]`, zero C-FFI,
//! `wasm32`-compatible) for computing exact normal forms, Gröbner–Shirshov completions,
//! dyadic Laurent reductions, inductive Markov/Bratteli layer-peeling traces, and oriented
//! binomial lattice reductions.
//!
//! ## Modules
//!
//! - [`scalar`]: Exact coefficient rings implementing [`RingScalar`] (also exported as [`CoeffRing`]),
//!   including `i64`, `BigInt`, `BigRational`, sparse Laurent polynomials [`LaurentPoly<R>`] over
//!   `R[q, q^-1]`, and truncated power-series jets [`TruncatedJet<R, K>`] over `R[h]/(h^(K+1))`.
//! - [`dyadic`]: GCD-free dyadic rationals [`DyadicScalar`] ($\mathbb{Z}\[\frac{1}{2}\]$) and
//!   dense-window dyadic Laurent polynomials [`DyadicLaurent`] ($\mathbb{Z}\[\frac{1}{2}\]\[q, q^{-1}\]$).
//! - [`order`]: Admissible monomial well-orders ([`DegLex`], [`DegRevLex`], [`DegRightLex`],
//!   [`WeightedDegLex`], [`OrderKind`]) compatible with two-sided word concatenation.
//! - [`free_alg`]: Sparse elements [`FreeAlg<G, R>`] of the free associative algebra $R\langle G \rangle$.
//! - [`shirshov`]: Dynamic Buchberger–Shirshov completion ([`ShirshovEngine`]) via overlap and
//!   inclusion S-polynomial compositions, interreduction, and [`NormalFormBasis`] reduction.
//! - [`hecke`]: Fast combinatorial Coxeter / Bokut–Shiao normal-form backend ([`BokutShiaoHecke`])
//!   for type-$A$ Iwahori–Hecke algebras $H_n(q)$.
//! - [`temperley_lieb`]: Planar non-crossing diagram backend ([`TemperleyLiebBasis`]) for
//!   Temperley–Lieb algebras $TL_n(\delta)$ with Catalan dimension $C_n$, loop closure trace,
//!   and Hecke skein quotients.
//! - [`peel`]: Matrix-free layer-peeling and transfer-matrix engines:
//!   - [`peel::markov_tower`]: Streaming GS accumulation + inductive Ocneanu–Markov tower peeling
//!     $H_n(q) \to H_{n-1}(q) \to \dots \to H_1(q)$ (both normalized and homogeneous division-free).
//!   - [`peel::chain_transfer`]: Hecke-only $2\times 2$ block-chain transfer reduction.
//!   - [`peel::bratteli_two_row`]: Multiplicity-free Gelfand–Tsetlin / Young–Hoefsmit edge transfer
//!     sweep (Catalan two-row $\ell(\lambda) \le 2$ and unrestricted).
//! - [`binomial`]: Conti–Traverso / Pottier Graver oriented binomial vector rewriting over
//!   $\mathbb{N}^m$, LP reduced-cost fiber certificates, and functorial column promotion $A_{k+1} = A_k M$.
//!
//! ## Example: Completing an Unconfluent Presentation
//!
//! ```rust
//! use gs_basis::{
//!     BokutShiaoHecke, CompletionConfig, DegLex, FreeAlg, LaurentPoly, NormalFormBasis,
//!     ShirshovEngine,
//! };
//!
//! type R = LaurentPoly<i64>;
//! let h = R::h();
//!
//! // Standard uncompleted presentation of H_5(q) on 4 generators sigma_0..sigma_3:
//! let uncompleted = BokutShiaoHecke::<R>::uncompleted_rules(5, &h);
//! let mut engine = ShirshovEngine::from_rules(uncompleted, DegLex).unwrap();
//!
//! // Before completion, Bokut-Shiao's n=4 counterexample S-polynomial does NOT reduce to 0:
//! let w1 = FreeAlg::<usize, R>::word(vec![2, 3, 2, 1]);
//! let w2 = FreeAlg::<usize, R>::word(vec![3, 2, 1, 3]);
//! let diff = &w1 - &w2;
//! assert!(!engine.reduce(&diff).is_zero());
//!
//! // Dynamic Buchberger-Shirshov completion discovers the missing Bokut-Shiao rules:
//! let cert = engine.complete(&CompletionConfig::default()).unwrap();
//! assert!(cert.is_complete);
//! assert!(engine.reduce(&diff).is_zero());
//!
//! // And agrees identically with the O(l*n) Coxeter fast-path backend:
//! let fast = BokutShiaoHecke::new(5, h);
//! assert_eq!(fast.reduce(&w2), w1);
//! ```

pub mod binomial;
pub mod dyadic;
pub mod free_alg;
pub mod hecke;
pub mod order;
pub mod peel;
pub mod scalar;
pub mod shirshov;
pub mod temperley_lieb;

pub use binomial::{
    linear_cost, pottier_graver_basis, promote_stratum_columns, reduced_costs, BinomialBasis,
    BinomialRule, IntegerMatrix,
};
pub use dyadic::{DyadicLaurent, DyadicScalar};
pub use free_alg::{FreeAlg, Word};
pub use hecke::BokutShiaoHecke;
pub use order::{DegLex, DegRevLex, DegRightLex, MonomialOrder, OrderKind, WeightedDegLex};
pub use scalar::{rat, LaurentPoly, RingScalar, RingScalar as CoeffRing, TruncatedJet};
pub use shirshov::{
    CompletionCertificate, CompletionConfig, CriticalPairKind, NormalFormBasis, RewriteRule,
    ShirshovEngine, ShirshovError,
};
pub use temperley_lieb::{
    PlanarMatching, SkeinConvention, TemperleyLiebBasis, TemperleyLiebElement,
};
