//! H_A(q) 3-channel Wedderburn binding energy —
//! [prop:tower-binding-energy](https://github.com/litlfred/qou/blob/claude/continue-hamdover-QGLMZ/content/quantum-observable-universe/particle-interactions/tower-binding-energy.md).
//!
//! Parity port of `folio-assistant/computations/full-tower-mass.py`
//! (the correct content-block mass framework per the 2026-04-19
//! domain audit).  The H_{3A} Plancherel variant already ported at
//! `atom.rs` is under the deprecated single-vortex formula.
//!
//!   B(Z, N) = Σ_{λ ∈ {sym, std, alt}} w_λ · m_e · Σ_{i=0}^{A-2} ln|Φ_q(V̂_i^λ)|
//!
//! with
//!   w_sym = w_alt = 1 / ([2]_q² + 2)
//!   w_std = [2]_q² / ([2]_q² + 2)
//!   V̂_i^sym = ∏_j (c_j·q + d_j)                       (symmetric channel)
//!   V̂_i^std = z·a_i + b_i                              (std transfer)
//!   V̂_i^alt = ∏_j (-c_j/q + d_j)                      (alternating)
//!
//! where the per-generator product runs over this-nucleon's gluon
//! crossings plus inter-nucleon crossings to later nucleons.
//!
//! Python: folio-assistant/computations/full-tower-mass.py — the
//! symbolic (sympy) version used for content block numerics.  This
//! Rust port is purely numerical at a given q.

/// Per-pair (c, d) for the inter-particle crossing.
///
/// Particle codes:  0 = neutron (n), 1 = proton (p), 2 = electron (e).
/// `h = q − q⁻¹`.
///
/// Strong-channel crossings: pp = σ₀, nn = σ₀⁻¹, pn = symmetric mix.
/// EM-channel crossings: pe = σ₀⁻¹ (strong Coulomb binding),
///                        ne = identity-like (neutral), ee = σ_0.
/// The (c, d) form follows the per prop:tower-binding-energy general
/// Hecke relation — small-d on strongly attractive pairs.
#[inline]
fn crossing_coeffs(ti: u8, tj: u8, h: f64) -> (f64, f64) {
    match (ti, tj) {
        (1, 1) => (1.0, 0.0),          // pp
        (0, 0) => (1.0, -h),            // nn
        (1, 0) | (0, 1) => (1.0, -h / 2.0),   // pn
        // Electron couplings (EM channel):
        (1, 2) | (2, 1) => (1.0, -h / 2.0),   // pe (Coulomb attractive)
        (0, 2) | (2, 0) => (1.0, 0.0),        // ne (no direct EM)
        (2, 2) => (1.0, -h),                   // ee (Pauli mix)
        _ => (1.0, 0.0),
    }
}

/// Ground-state nucleon ordering: interleave protons (1) and neutrons (0).
fn ground_state_ordering(z: u32, n: u32) -> Vec<u8> {
    let mut out = Vec::with_capacity((z + n) as usize);
    let (mut pi, mut ni) = (0u32, 0u32);
    for _ in 0..(z + n) {
        let prefer_p = pi < z
            && (ni >= n
                || (pi as f64) / (z.max(1) as f64)
                    <= (ni as f64) / (n.max(1) as f64));
        if prefer_p {
            out.push(1);
            pi += 1;
        } else {
            out.push(0);
            ni += 1;
        }
    }
    out
}

/// ln|Φ_q(V)| = Σ_{k≥1} -ln|1 − q^{-k} V|  (analytic continuation).
fn ln_phi_q(v: f64, qi: f64, max_k: usize) -> f64 {
    if v == 0.0 {
        return 0.0;
    }
    let mut s = 0.0_f64;
    let mut qik = qi;
    for _ in 0..max_k {
        let f = 1.0 - qik * v;
        if f.abs() < 1e-300 {
            return f64::INFINITY;
        }
        s -= f.abs().ln();
        if (qik * v).abs() < 1e-15 {
            break;
        }
        qik *= qi;
    }
    s
}

/// Gluon operator token: token → list of (c, d) crossings.
///
/// Matches the Python `GLUON_CANDIDATES` from
/// `sdp_gluon_multiplicity_hA.py` but numerical in `h = q − 1/q`.
fn gluon_crossings(token: &str, h: f64) -> Vec<(f64, f64)> {
    match token {
        "none" => vec![],
        "s0" => vec![(1.0, 0.0)],
        "s0s0" => vec![(1.0, 0.0), (1.0, 0.0)],
        "s0x4" => vec![(1.0, 0.0); 4],
        "s1" => vec![(1.0, -h)],
        "Lp" => vec![(1.0, 0.0), (1.0, -h)],
        "Lm" => vec![(1.0, -h), (1.0, 0.0)],
        "trefoil" => vec![(1.0, 0.0), (1.0, 0.0), (1.0, 0.0)],  // T_{2,3} = σ³
        _ => panic!("unknown gluon token: {}", token),
    }
}

/// Per-generator per-channel vertex volumes V̂_i^{sym,std,alt} at q.
///
/// Extended form accepting per-nucleon gluon tokens and per-pair
/// crossing multiplicities.  Matches the Python symbolic version in
/// `sdp_gluon_multiplicity_hA.per_gen_volumes_gluon` at q₀.
fn per_gen_volumes_ha(
    gen_idx: usize,
    ordering: &[u8],
    gluons: &[&str],
    q: f64,
    m_pp: u32,
    m_pn: u32,
    m_nn: u32,
) -> (f64, f64, f64) {
    let h = q - 1.0 / q;
    let z = 1.0 / (q.sqrt() + 1.0 / q.sqrt());
    let (mut a, mut b) = (0.0_f64, 1.0_f64);
    let (mut sym_v, mut alt_v) = (1.0_f64, 1.0_f64);
    // Gluon self-coupling per the token for this nucleon.
    let gluon = gluon_crossings(gluons[gen_idx], h);
    for (gc, gd) in &gluon {
        let (na, nb) = (a * gc * h + a * gd + b * gc, a * gc + b * gd);
        a = na;
        b = nb;
        sym_v *= gc * q + gd;
        alt_v *= -gc / q + gd;
    }
    // Inter-nucleon crossings to later nucleons.
    let big_a = ordering.len();
    for j in (gen_idx + 1)..big_a {
        let (c, d) = crossing_coeffs(ordering[gen_idx], ordering[j], h);
        let m = match (ordering[gen_idx], ordering[j]) {
            (1, 1) => m_pp,
            (0, 0) => m_nn,
            _ => m_pn,
        };
        for _ in 0..m {
            let (na, nb) = (a * c * h + a * d + b * c, a * c + b * d);
            a = na;
            b = nb;
            sym_v *= c * q + d;
            alt_v *= -c / q + d;
        }
    }
    (sym_v, z * a + b, alt_v)
}

/// Default gluons per particle type:
///   proton (1)   → "s0s0" (2·σ₀)
///   neutron (0)  → "s0x4" (4·σ₀)
///   electron (2) → "none" (atomic binding is ~keV scale,
///                  orders of magnitude smaller than nuclear MeV;
///                  self-coupling of bound electrons is ~0 in the
///                  Hecke-tower framework).
fn default_gluons(ordering: &[u8]) -> Vec<&'static str> {
    ordering.iter().map(|&t| match t {
        1 => "s0s0",
        0 => "s0x4",
        2 => "none",
        _ => "none",
    }).collect()
}

/// Nuclear binding energy with an explicit ordering + gluons vector.
///
/// `ordering`: length A, 1 = proton, 0 = neutron (physical slot order).
/// `gluons`: length A, token per nucleon (e.g. "s0s0", "none", "Lp").
pub fn binding_ha_custom(
    ordering: &[u8],
    gluons: &[&str],
    m_pp: u32,
    m_pn: u32,
    m_nn: u32,
    q: f64,
    m_e_mev: f64,
) -> f64 {
    let big_a = ordering.len();
    if big_a < 2 {
        return 0.0;
    }
    debug_assert_eq!(gluons.len(), big_a,
        "gluons length must match ordering length");
    let q2 = q * q;
    let qi2 = 1.0 / q2;
    let qint2 = (q2 - qi2) / (q - 1.0 / q);
    let denom = qint2 * qint2 + 2.0;
    let w_sym = 1.0 / denom;
    let w_std = qint2 * qint2 / denom;
    let w_alt = w_sym;

    let qi = 1.0 / q;
    let (mut bs, mut bd, mut ba) = (0.0_f64, 0.0_f64, 0.0_f64);
    for i in 0..(big_a - 1) {
        let (vs, vd, va) = per_gen_volumes_ha(
            i, ordering, gluons, q, m_pp, m_pn, m_nn);
        bs += ln_phi_q(vs.abs(), qi, 500);
        bd += ln_phi_q(vd.abs(), qi, 500);
        ba += ln_phi_q(va.abs(), qi, 500);
    }
    w_sym * m_e_mev * bs + w_std * m_e_mev * bd + w_alt * m_e_mev * ba
}

/// Nuclear binding energy B(Z, N) with default ground-state ordering
/// and default gluons (2σ₀ on proton, 4σ₀ on neutron).
pub fn binding_ha(
    z: u32,
    n: u32,
    m_pp: u32,
    m_pn: u32,
    m_nn: u32,
    q: f64,
    m_e_mev: f64,
) -> f64 {
    let ordering = ground_state_ordering(z, n);
    let gluons = default_gluons(&ordering);
    binding_ha_custom(&ordering, &gluons, m_pp, m_pn, m_nn, q, m_e_mev)
}

/// Binding energy with Z bound electrons appended to the atom braid.
///
/// Per user (2026-04-19) "B needs electrons": the proposition's
/// M(Z,N) = Z·m_p + N·m_n + Z·m_e − B(Z,N) has Z free electrons in
/// the first three terms; binding of those electrons to the nucleus
/// (Coulomb / QED) is absorbed into B(Z, N).  At the H_A tower level,
/// we extend the algebra from H_A(q) (nucleons only) to H_{A+Z}(q)
/// by appending Z "electron" strands (particle code 2) to the
/// ordering.  Each electron has the default T_{2,3} trefoil gluon;
/// inter-crossings between electrons and nucleons use the EM-channel
/// (c, d) values in `crossing_coeffs`.
///
/// Reduces to `binding_ha` when `z == 0` (no electrons).
pub fn binding_ha_with_electrons(
    z: u32,
    n: u32,
    m_pp: u32,
    m_pn: u32,
    m_nn: u32,
    q: f64,
    m_e_mev: f64,
) -> f64 {
    // Nuclear ordering + electrons appended.
    let mut ordering = ground_state_ordering(z, n);
    for _ in 0..z {
        ordering.push(2);                       // electron
    }
    let gluons = default_gluons(&ordering);
    binding_ha_custom(&ordering, &gluons, m_pp, m_pn, m_nn, q, m_e_mev)
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::nf::Q_0;

    const M_E_MEV: f64 = 0.51099895;

    /// Reproduces full-tower-mass.py's D prediction (≈ 4.92 MeV).
    #[test]
    fn d_matches_python_full_tower() {
        let b = binding_ha(1, 1, 1, 1, 1, Q_0, M_E_MEV);
        // Python reports B_pred ≈ 4.9244 for D.
        assert!((b - 4.9244).abs() < 1e-2,
                "Rust D binding {:.4} deviates from Python 4.9244", b);
    }

    /// Reproduces 4He prediction (≈ 19.41 MeV).
    #[test]
    fn he4_matches_python_full_tower() {
        let b = binding_ha(2, 2, 1, 1, 1, Q_0, M_E_MEV);
        assert!((b - 19.41).abs() < 0.1,
                "Rust 4He binding {:.4} deviates from Python 19.41", b);
    }

    /// sdp_inter_nucleon_hA: 4He at (m_pp, m_pn, m_nn) = (2, 2, 2) is
    /// Python err 0.0199% → B ≈ 27.55 MeV. Test parity.
    #[test]
    fn he4_best_triple_matches_python_sdp() {
        let b = binding_ha(2, 2, 2, 2, 2, Q_0, M_E_MEV);
        assert!((b - 27.549).abs() < 0.1,
                "Rust 4He@(2,2,2) binding {:.4} != Python 27.549", b);
    }
}
