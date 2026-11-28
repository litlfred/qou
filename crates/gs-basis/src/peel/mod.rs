//! Layer-peeling and monotone transfer-matrix algorithms for Iwahori–Hecke algebras $H_n(q)$.
//!
//! Provides three complementary evaluation engines avoiding $(n)!$-dimensional matrix
//! materialisation:
//! - [`markov_tower`]: Streaming Gröbner–Shirshov multiplication followed by inductive
//!   Ocneanu–Markov generator peeling down the tower $H_n(q) \to H_{n-1}(q) \to \dots \to H_1(q)$.
//! - [`chain_transfer`]: Hecke-only $2\times 2$ transfer-matrix reduction of block-ordered
//!   elements $\Xi_n = \prod_{i=0}^{n-2} \prod_k (c_{i,k}\sigma_i + d_{i,k}\mathbf{1})$ into
//!   canonical chain form $\prod_{i=0}^{n-2} (a_i\sigma_i + b_i\mathbf{1})$.
//! - [`bratteli_two_row`]: Multiplicity-free Gelfand–Tsetlin / Young–Hoefsmit edge transfer sweep
//!   computing irreducible characters $\chi^\lambda(\beta)$ (both restricted to two-row Catalan
//!   shapes $\ell(\lambda) \le 2$ and unrestricted) for monotone words in a single pass.

pub mod bratteli_two_row;
pub mod chain_transfer;
pub mod markov_tower;
