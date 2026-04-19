//! Hecke algebra H_3(q) engine — Gröbner normal-form kernel and
//! atom-level constructions for the quantum observable universe.
//!
//! Module layout:
//!
//! * [`nf`] — GB-NF kernel: word rewriting, `reduce_nf`, `mul_polys`,
//!   NF basis constants, and the Markov/Hecke scalar helpers
//!   (`markov_z`, `hecke_h`, `trace_weights`).
//! * [`gram`] — 6×6 Gram matrix, inverse, determinant, and the
//!   JSON certificate (`GramCertificate`).
//! * [`atom`] — NF-vector multiplication kernel (`hm`), Markov trace
//!   on NF vectors (`nf_tr`), the full `build_atom_nf` construction,
//!   and per-generator Wedderburn volumes.
//! * [`certificate`] — certificate I/O helpers.

pub mod atom;
pub mod certificate;
pub mod gram;
pub mod nf;
pub mod sdp_decision;
