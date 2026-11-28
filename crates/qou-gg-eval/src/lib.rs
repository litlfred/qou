//! `qou-gg-eval` — 80+ dps proton-pinned MPFR evaluator for proper `γγ` hadrons,
//! 4-photon states, 4-strand flavoured `γγ` nucleons, 6-strand neutral lepton-pair
//! words, and full-strand `A = 1..4` `T3`-bonded nuclear braids (`qou-ggtb`).
//!
//! Zero `f64` arithmetic enters any evaluation path: every scalar, normal form,
//! Hoefsmit/Gelfand–Tsetlin matrix entry, Markov trace, and Specht character is
//! computed in `rug::Float` at `>= 266` bits (default `320` bits ≈ 96 dps) pinned
//! strictly to the experimental proton anchor `q_0^(p)`.

pub mod h3;
pub mod h4_flavoured;
pub mod lepton_pair_6s;
pub mod light_nuclei_t3;
pub mod scalars;
pub mod tower_gt;
