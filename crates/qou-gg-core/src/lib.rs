#![forbid(unsafe_code)]
#![warn(missing_docs)]

//! # `qou-gg-core` — Pure-Rust Zero-FFI $\gamma\gamma$, 4-Photon & Atomic-Chart Core
//!
//! Lightweight foundational algebra crate built exclusively on [`gs_basis`], `num-*`, and `serde`
//! (`wasm32`-compatible, zero C-FFI dependencies).
//!
//! ## Modules
//!
//! - [`photon`]: Signed Artin [`BraidWord`]s, ruled 4-term [`Photon4Term<R>`]
//!   $\gamma^{(s)}(\phi) = \mathbf{1} + \phi_0\sigma_s + \phi_1\sigma_{s+1} + \phi_{01}\sigma_s\sigma_{s+1}^{-1}$,
//!   chiral eigen-photons $\gamma_\pm$, and general $k$-photon products through 4-photon
//!   ([`four_photon_product`], $4^4 = 256$ monomials).
//! - [`u1_neutral`]: Whole-word linking-neutrality cut (`QOU/StandardModel/PhotonU1NeutralCut.lean`)
//!   on arbitrary strand counts $n \ge 2$.
//! - [`hadron`]: Bare Borromean baryon $\beta_{\mathrm{Bor}} = V^3$, typed `uud`/`udd` flavours,
//!   $\pi^\pm$ ($\sigma_0^2 \in H_2(q)$), electron Hopf word ($\sigma_0\sigma_1\sigma_0$), and
//!   crossing-local quark-charge-dressed $3\times 3$ matrices $L_p, L_n, M_p, M_n$
//!   (`QOU/Nuclear/NucleonChargeDressedWords.lean`).
//! - [`atomic_chart`]: Deterministic $O(A)$ `T3` proper 3-edge-coloured inter-nucleon bond graph
//!   (`QOU/MassTheory/NucleusBondValence.lean`) and canonical $(Z, N)$ [`AtomicDatum`] generator
//!   across $Z = 0\ldots 118$.
//!
//! ## Example: Exact Borromean Pair Identity $\gamma_+ \gamma_- = V^3$ in $H_3(q)$
//!
//! ```rust
//! use gs_basis::{BokutShiaoHecke, LaurentPoly, NormalFormBasis, RingScalar};
//! use qou_gg_core::{BraidWord, Photon4Term, two_photon_product};
//!
//! type L = LaurentPoly<i64>;
//! let h = L::h();
//! let hecke3 = BokutShiaoHecke::new(3, h.clone());
//!
//! let gp = Photon4Term::<L>::gamma_plus(0);
//! let gm = Photon4Term::<L>::gamma_minus(0);
//! let pair_nf = two_photon_product(&gp, &gm, &hecke3);
//!
//! let v3_nf = hecke3.reduce(&BraidWord::borromean_v3(0).to_free_alg(&h));
//! assert_eq!(pair_nf, v3_nf);
//! // Zero electron Hopf-word (sigma_0 sigma_1 sigma_0) coefficient:
//! assert_eq!(pair_nf.coeff(&[0, 1, 0]), L::zero());
//! ```

pub mod atomic_chart;
pub mod hadron;
pub mod photon;
pub mod u1_neutral;

pub use atomic_chart::{
    build_atomic_datum, canonical_atomic_chart_0_to_118, construct_t3_bond_graph, element_symbol,
    max_t3_bonds, verify_t3_bond_graph, AtomicDatum, ColourChannel, ElectronShellPlacement,
    NucleonBondEdge, NucleonPlacement, T3BondGraph, ELEMENT_SYMBOLS, MADELUNG_SHELL_CAPACITIES,
};
pub use hadron::{
    borromean_baryon_word, charged_pion_word, electron_hopf_word, g_cofactor_poly, ln_matrix,
    lp_matrix, mat3_mul, mat3_sub, mat3_trace, mn_matrix, mp_matrix, photon_pair_matrix, Mat3,
    NucleonKind, QuarkFlavour,
};
pub use photon::{
    four_photon_product, k_photon_braid_expansion, k_photon_linking_neutral_projection,
    k_photon_product, three_photon_product, two_photon_product, BraidCrossing, BraidWord,
    Photon4Term,
};
pub use u1_neutral::{
    closure_components, component_pair_count, is_linking_neutral, is_u1_neutral,
    pairwise_linkings_twice, self_writhes, writhe,
};
