//! Atom-level Hecke computations: the NF-vector multiplication
//! kernel [`hm`], the Markov trace [`nf_tr`], and the full
//! atom / per-generator construction used by the nuclear-mass and
//! molecular-binding binaries.
//!
//! Everything here operates on **6-element NF coefficient vectors**
//! (the normal form on the H_3(q) basis), not on free-algebra
//! polynomials — the `reduce_nf` machinery lives in the sibling
//! [`crate::nf`] module.

use crate::nf::markov_z;

/// Multiply an NF element by `(c · σ_gen + d · 1)`.
///
/// Mirrors `pyhecke.gram.hm` (which closes over `h = q − q⁻¹`).
/// `gen` must be 0 or 1. `nf[0..6]` is the coefficient vector on the
/// NF basis `[γ, σ₀, σ₁, L₊, L₋, e⁻]`.
///
/// `#[inline]`: `hm` is the inner micro-op of [`build_atom_nf`] (~40
/// calls per nucleon), so we ask the compiler to inline across the
/// module boundary even without LTO.
#[inline]
pub fn hm(nf: &[f64; 6], c: f64, d: f64, gen: u8, h: f64) -> [f64; 6] {
    let mut r = [0.0f64; 6];
    let tables: [(usize, &[(usize, f64)]); 6] = if gen == 0 {
        [
            (0, &[(1, c), (0, d)]),
            (1, &[(1, c * h), (0, c), (1, d)]),
            (2, &[(3, c), (2, d)]),
            (3, &[(3, c * h), (2, c), (3, d)]),
            (4, &[(5, c), (4, d)]),
            (5, &[(5, c * h), (4, c), (5, d)]),
        ]
    } else {
        [
            (0, &[(2, c), (0, d)]),
            (1, &[(4, c), (1, d)]),
            (2, &[(2, c * h), (0, c), (2, d)]),
            (3, &[(5, c), (3, d)]),
            (4, &[(4, c * h), (1, c), (4, d)]),
            (5, &[(5, c * h), (3, c), (5, d)]),
        ]
    };
    for (si, tgts) in tables.iter() {
        if nf[*si].abs() < 1e-15 {
            continue;
        }
        for (ti, co) in tgts.iter() {
            r[*ti] += nf[*si] * co;
        }
    }
    r
}

/// Markov trace of an NF vector at a given `q`.
pub fn nf_tr(nf: &[f64; 6], q: f64) -> f64 {
    let tr = crate::nf::trace_weights(q);
    (0..6).map(|i| nf[i] * tr[i]).sum()
}

/// Sum of NF coefficients (the augmentation / net of the element).
pub fn nf_net(nf: &[f64; 6]) -> f64 {
    nf.iter().sum()
}

/// Build the atom NF for (Z, N) via Hecke multiplication.
///
/// Mirrors `hecke_core.build_atom_nf` byte-for-byte. Construction:
///
/// 1. Build each nucleon via B_3 confinement + quark crossings +
///    gluon self-coupling.
/// 2. Compose in ground-state interleaved order (p, n, p, n, …).
/// 3. Apply inter-nucleon crossings between each pair:
///    pp = σ₀, nn = σ₀⁻¹, pn = ½(σ₀ + σ₀⁻¹).
/// 4. Apply pe crossings for Z electrons (σ₁⁻¹).
///
/// `h` is `hecke_h(q)` for the target q; pass `hecke_h(Q_0)` to match
/// the Python default.
pub fn build_atom_nf(z_count: u32, n_count: u32, h: f64) -> [f64; 6] {
    let a = z_count + n_count;
    if a == 0 {
        return [1.0, 0.0, 0.0, 0.0, 0.0, 0.0];
    }

    // Ground-state interleaved ordering.
    let mut ordering: Vec<u8> = Vec::with_capacity(a as usize);
    let (mut pc, mut nc) = (0u32, 0u32);
    for k in 0..a {
        if (k % 2 == 0 && pc < z_count) || nc >= n_count {
            ordering.push(b'p');
            pc += 1;
        } else {
            ordering.push(b'n');
            nc += 1;
        }
    }

    let mut nf = [1.0f64, 0.0, 0.0, 0.0, 0.0, 0.0];
    let half_h = 0.5 * h;

    for k in 0..a as usize {
        // B_3 confinement: 3x (σ₀ σ₁⁻¹)
        for _ in 0..3 {
            nf = hm(&nf, 1.0, 0.0, 0, h);
            nf = hm(&nf, 1.0, -h, 1, h);
        }

        if ordering[k] == b'p' {
            // Proton: uud
            nf = hm(&nf, 1.0, 0.0, 0, h);        // (0,1) uu → σ₀
            nf = hm(&nf, 1.0, -half_h, 0, h);    // (0,2) ud → mixed
            nf = hm(&nf, 1.0, -half_h, 1, h);    // (1,2) ud → mixed (gen 1)
        } else {
            // Neutron: udd
            nf = hm(&nf, 1.0, -half_h, 0, h);    // (0,1) ud → mixed
            nf = hm(&nf, 1.0, -half_h, 0, h);    // (0,2) ud → mixed
            nf = hm(&nf, 1.0, -h, 1, h);         // (1,2) dd → σ₁⁻¹
        }

        // Gluon self-coupling: 1 × σ₀ per nucleon. Patched from
        // 2×σ₀ → 1×σ₀ to match Python `hecke_core.build_atom_nf`
        // (commit b607e3e): atom-level SDP gluon search identified
        // ['s0'] × A as the universal LP-dual optimum, beating the
        // pre-existing ['s0 s0'] × A default by ~0.04% in
        // Plancherel-trace binding error across D / T / ³He.
        nf = hm(&nf, 1.0, 0.0, 0, h);

        // Inter-nucleon crossings with all previous nucleons
        for prev in 0..k {
            let (ti, tj) = (ordering[prev], ordering[k]);
            if ti == b'p' && tj == b'p' {
                nf = hm(&nf, 1.0, 0.0, 0, h);         // pp: σ₀
            } else if ti == b'n' && tj == b'n' {
                nf = hm(&nf, 1.0, -h, 0, h);          // nn: σ₀⁻¹
            } else {
                nf = hm(&nf, 1.0, -half_h, 0, h);     // pn/np: mixed
            }
        }
    }

    // Electrons: pe crossing (EM channel, gen=1)
    for _ in 0..z_count {
        nf = hm(&nf, 1.0, -h, 1, h);
    }

    nf
}

// ─── Per-generator Wedderburn volumes ────────────────────────────────

/// Per-generator Wedderburn-channel state.
///
/// `(a, b)` tracks the 2-dim standard irrep accumulator, `sp` the
/// 1-dim symmetric channel, `ap` the 1-dim alternating channel.
#[derive(Debug, Clone, Copy)]
struct ChannelState {
    a: f64,
    b: f64,
    sp: f64,
    ap: f64,
}

impl ChannelState {
    fn new() -> Self {
        Self { a: 0.0, b: 1.0, sp: 1.0, ap: 1.0 }
    }

    fn apply(&mut self, c: f64, d: f64, h: f64, q: f64, qi: f64) {
        let a_new = self.a * c * h + self.a * d + self.b * c;
        let b_new = self.a * c + self.b * d;
        self.a = a_new;
        self.b = b_new;
        self.sp *= c * q + d;
        self.ap *= -c * qi + d;
    }
}

/// Volume entry: `(sym, std, alt, full)` for one generator.
#[derive(Debug, Clone, Copy)]
pub struct VolumeEntry {
    pub sym: f64,
    pub std: f64,
    pub alt: f64,
    pub full: f64,
}

fn _proton_g0_full(h: f64) -> Vec<(f64, f64)> {
    vec![
        (1.0, 0.0), (1.0, 0.0), (1.0, 0.0),  // B_3
        (1.0, 0.0),                           // uu
        (1.0, -0.5 * h),                      // ud
        (1.0, 0.0),                           // 1 gluon (was 2 — see build_atom_nf note)
    ]
}

fn _proton_g1(h: f64) -> Vec<(f64, f64)> {
    vec![
        (1.0, -h), (1.0, -h), (1.0, -h),      // B_3
        (1.0, -0.5 * h),                       // ud (gen 1)
    ]
}

fn _neutron_g0(h: f64) -> Vec<(f64, f64)> {
    vec![
        (1.0, 0.0), (1.0, 0.0), (1.0, 0.0),  // B_3
        (1.0, -0.5 * h),                      // ud
        (1.0, -0.5 * h),                      // ud
        (1.0, 0.0),                           // 1 gluon (was 2 — see build_atom_nf note)
    ]
}

fn _neutron_g1(h: f64) -> Vec<(f64, f64)> {
    vec![
        (1.0, -h), (1.0, -h), (1.0, -h),      // B_3
        (1.0, -h),                             // dd (gen 1)
    ]
}

/// Per-generator Wedderburn volumes `V̂_i^full` for the atom braid.
///
/// Returns one [`VolumeEntry`] per generator:
///   * `include_inter = true`: `n_gens_total = 3A − 1` (physical atom
///     with pp/nn/pn inter-nucleon crossings)
///   * `include_inter = false`: `n_gens_total = 2A` (free baseline)
///
/// `crossings_per_pair` (or explicit `m_pp` / `m_pn` / `m_nn`)
/// controls inter-nucleon crossing multiplicity. Pass `None` for the
/// defaults.
pub fn atom_per_generator_volumes(
    z_count: u32,
    n_count: u32,
    include_inter: bool,
    crossings_per_pair: u32,
    m_pp: Option<u32>,
    m_pn: Option<u32>,
    m_nn: Option<u32>,
    q: f64,
) -> Vec<VolumeEntry> {
    let a = z_count + n_count;
    if a == 0 {
        return vec![];
    }

    let qi = 1.0 / q;
    let h = q - qi;

    let ordering: Vec<u8> = {
        let mut v = Vec::with_capacity(a as usize);
        for _ in 0..z_count { v.push(b'p'); }
        for _ in 0..n_count { v.push(b'n'); }
        v
    };

    let n_gens_total: usize = if include_inter {
        (3 * a - 1) as usize
    } else {
        (2 * a) as usize
    };
    let mut states: Vec<ChannelState> = vec![ChannelState::new(); n_gens_total];

    for k in 0..a as usize {
        let nuc = ordering[k];
        let (intra0, intra1) = if nuc == b'p' {
            (_proton_g0_full(h), _proton_g1(h))
        } else {
            (_neutron_g0(h), _neutron_g1(h))
        };
        let (base_g0, base_g1) = if include_inter {
            (3 * k, 3 * k + 1)
        } else {
            (2 * k, 2 * k + 1)
        };
        for &(c, d) in &intra0 {
            states[base_g0].apply(c, d, h, q, qi);
        }
        for &(c, d) in &intra1 {
            states[base_g1].apply(c, d, h, q, qi);
        }
        if include_inter && (k as u32) < a - 1 {
            let i = 3 * k + 2;
            let next_nuc = ordering[k + 1];
            let (c, d, m) = if nuc == b'p' && next_nuc == b'p' {
                (1.0f64, 0.0f64, m_pp.unwrap_or(crossings_per_pair))
            } else if nuc == b'n' && next_nuc == b'n' {
                (1.0, -h, m_nn.unwrap_or(crossings_per_pair))
            } else {
                (1.0, -0.5 * h, m_pn.unwrap_or(crossings_per_pair))
            };
            for _ in 0..m {
                states[i].apply(c, d, h, q, qi);
            }
        }
    }

    // Wedderburn weights for H_3(q). Match Python byte-for-byte:
    //   q_int(n) = (q^n - q^{-n}) / (q - q^{-1})
    //   nf3_val = [1]_q · [2]_q · [3]_q = [3]_q!
    //   qdim_sym = 1, qdim_std = [2]_q, qdim_alt = 1
    //   w_* = qdim_*^2 / nf3_val, then renormalise so Σ w_* = 1.
    // Graceful handling of q = 1 (classical limit, denom = 0, [n]_q → n).
    let denom = q - 1.0 / q;
    let qint = |n: i32| -> f64 {
        if denom.abs() < 1e-12 {
            n as f64
        } else {
            (q.powi(n) - q.powi(-n)) / denom
        }
    };
    let qint2 = qint(2);
    let qint3 = qint(3);
    let nf3_val = qint(1) * qint2 * qint3;
    let (qdim_sym, qdim_std, qdim_alt): (f64, f64, f64) = (1.0, qint2, 1.0);
    let (mut w_sym, mut w_std, mut w_alt): (f64, f64, f64) =
        (qdim_sym.powi(2) / nf3_val, qdim_std.powi(2) / nf3_val, qdim_alt.powi(2) / nf3_val);
    let wt = w_sym + w_std + w_alt;
    w_sym /= wt;
    w_std /= wt;
    w_alt /= wt;

    let z_mark = markov_z(q);
    let mut out = Vec::with_capacity(n_gens_total);
    for s in states.iter() {
        let v_std = z_mark * s.a + s.b;
        out.push(VolumeEntry {
            sym: s.sp,
            std: v_std,
            alt: s.ap,
            full: w_sym * s.sp + w_std * v_std + w_alt * s.ap,
        });
    }
    out
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::nf::{hecke_h, Q_0};

    #[test]
    fn hm_identity_on_gamma() {
        // hm(γ, 1, 0, 0) should give σ_0 (basis index 1)
        let nf = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0];
        let out = hm(&nf, 1.0, 0.0, 0, hecke_h(Q_0));
        assert!((out[1] - 1.0).abs() < 1e-12);
        for i in [0, 2, 3, 4, 5] {
            assert!(out[i].abs() < 1e-12);
        }
    }

    #[test]
    fn nf_tr_of_gamma_is_one() {
        let nf = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0];
        assert!((nf_tr(&nf, Q_0) - 1.0).abs() < 1e-14);
    }

    #[test]
    fn nf_net_sum() {
        let nf = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0];
        assert!((nf_net(&nf) - 21.0).abs() < 1e-14);
    }

    #[test]
    fn build_atom_nf_hydrogen() {
        let h = hecke_h(Q_0);
        let nf = build_atom_nf(1, 0, h);
        assert!(nf.iter().all(|x| x.is_finite()));
        assert!(nf.iter().any(|x| x.abs() > 1e-10));
    }

    #[test]
    fn build_atom_nf_vacuum() {
        let h = hecke_h(Q_0);
        let nf = build_atom_nf(0, 0, h);
        assert!((nf[0] - 1.0).abs() < 1e-14);
        for i in 1..6 {
            assert!(nf[i].abs() < 1e-14);
        }
    }

    /// Anchor the Rust `build_atom_nf` output for D, T, ³He, ⁴He to
    /// reference values captured from the Python `hecke_core.build_atom_nf`
    /// implementation after the gluon-count fix (PR #387 / commit e9555dc).
    ///
    /// These values would have flagged the `2·σ₀ → 1·σ₀` drift
    /// immediately. Anchor tolerance is 1e-14 — byte-identical against
    /// the Python reference.
    fn assert_nf_close(got: [f64; 6], want: [f64; 6], label: &str) {
        for i in 0..6 {
            assert!(
                (got[i] - want[i]).abs() < 1e-14,
                "{}: component {} = {} but expected {} (Δ = {:.3e})",
                label, i, got[i], want[i], (got[i] - want[i]).abs(),
            );
        }
    }

    #[test]
    fn build_atom_nf_deuterium_anchor() {
        // Deuterium (Z=1, N=1) — captured from Python reference.
        let h = hecke_h(Q_0);
        let nf = build_atom_nf(1, 1, h);
        let want = [
            0.07906980016041938,
            0.03081047272161687,
            -0.023573832439791872,
            1.0365975259780913,
            -0.07330449849547012,
            -0.09753323222314403,
        ];
        assert_nf_close(nf, want, "deuterium D");
    }

    #[test]
    fn build_atom_nf_tritium_anchor() {
        // Tritium (Z=1, N=2).
        let h = hecke_h(Q_0);
        let nf = build_atom_nf(1, 2, h);
        let want = [
            1.0499136673052372,
            -0.0919745969167634,
            0.011010789075463379,
            -0.05637357079266976,
            0.0337216048367702,
            0.08211068751035897,
        ];
        assert_nf_close(nf, want, "tritium T");
    }

    #[test]
    fn build_atom_nf_helium3_anchor() {
        // Helium-3 (Z=2, N=1).
        let h = hecke_h(Q_0);
        let nf = build_atom_nf(2, 1, h);
        let want = [
            -0.09594932576763585,
            0.05640138172644632,
            1.0462524512200269,
            0.32182313719525707,
            0.00884093610261389,
            -0.07828524176710339,
        ];
        assert_nf_close(nf, want, "helium-3");
    }

    #[test]
    fn build_atom_nf_helium4_anchor() {
        // Helium-4 (Z=2, N=2).
        let h = hecke_h(Q_0);
        let nf = build_atom_nf(2, 2, h);
        let want = [
            1.0848298163930892,
            0.01137427995641008,
            -0.07551276178296537,
            -0.08514672560596817,
            0.006870765197978325,
            0.2909333525459163,
        ];
        assert_nf_close(nf, want, "helium-4");
    }
}
