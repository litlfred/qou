//! Ruled 4-term photon $\gamma^{(s)}(\phi)$ and $k$-photon collision products ($k = 1\ldots 4$).
//!
//! Implements the ruled photon (`owner-rulings.md`, 2026-11-18/20):
//! $$\gamma^{(s)}(\phi_0, \phi_1, \phi_{01}) \;=\; \mathbf{1} + \phi_0\,\sigma_s + \phi_1\,\sigma_{s+1} + \phi_{01}\,\sigma_s\sigma_{s+1}^{-1}$$
//! at any strand offset $s \ge 0$, where $\sigma_k^{-1} = \sigma_k - h\,\mathbf{1}$ in the balanced
//! Iwahori–Hecke algebra $H_n(q)$ ($\sigma_k^2 = h\,\sigma_k + \mathbf{1}$, $h = q - q^{-1}$).

use gs_basis::peel::markov_tower::LinearFactor;
use gs_basis::{BokutShiaoHecke, FreeAlg, LaurentPoly, NormalFormBasis, RingScalar};
use serde::{Deserialize, Serialize};

use crate::u1_neutral::is_linking_neutral;

/// Single signed Artin braid generator $\sigma_{\text{gen}}^{\pm 1}$.
#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Debug, Serialize, Deserialize)]
pub struct BraidCrossing {
    /// 0-based generator index `i` swapping strand positions `i` and `i + 1`.
    pub gen: usize,
    /// Crossing sign: `+1` for $\sigma_i$, `-1` for $\sigma_i^{-1}$.
    pub sign: i8,
}

impl BraidCrossing {
    /// Positive crossing $\sigma_{\text{gen}}$.
    pub fn pos(gen: usize) -> Self {
        Self { gen, sign: 1 }
    }

    /// Negative crossing $\sigma_{\text{gen}}^{-1}$.
    pub fn neg(gen: usize) -> Self {
        Self { gen, sign: -1 }
    }

    /// Convert to a `LinearFactor<R>` in balanced Hecke normalisation ($\sigma_i^{-1} = \sigma_i - h\mathbf{1}$).
    pub fn to_linear_factor<R: RingScalar>(&self, h: &R) -> LinearFactor<R> {
        if self.sign >= 0 {
            LinearFactor::sigma(self.gen)
        } else {
            LinearFactor::sigma_inv(self.gen, h)
        }
    }
}

/// Signed Artin braid word in $B_n$.
#[derive(Clone, Default, PartialEq, Eq, PartialOrd, Ord, Hash, Debug, Serialize, Deserialize)]
pub struct BraidWord {
    crossings: Vec<BraidCrossing>,
}

impl BraidWord {
    /// Empty (identity) braid word.
    pub fn empty() -> Self {
        Self {
            crossings: Vec::new(),
        }
    }

    /// Construct from a vector of signed crossings.
    pub fn new(crossings: Vec<BraidCrossing>) -> Self {
        for c in &crossings {
            assert!(
                c.sign == 1 || c.sign == -1,
                "BraidCrossing sign must be +1 or -1, got {}",
                c.sign
            );
        }
        Self { crossings }
    }

    /// Construct from `(gen, sign)` tuples.
    pub fn from_pairs(pairs: &[(usize, i8)]) -> Self {
        Self::new(
            pairs
                .iter()
                .map(|&(gen, sign)| BraidCrossing { gen, sign })
                .collect(),
        )
    }

    /// Single positive crossing $\sigma_i$.
    pub fn sigma(i: usize) -> Self {
        Self {
            crossings: vec![BraidCrossing::pos(i)],
        }
    }

    /// Single negative crossing $\sigma_i^{-1}$.
    pub fn sigma_inv(i: usize) -> Self {
        Self {
            crossings: vec![BraidCrossing::neg(i)],
        }
    }

    /// Chiral two-photon vertex $V_s = \sigma_s \sigma_{s+1}^{-1}$ on strands `(s, s+1, s+2)`.
    pub fn vertex_v(strand_offset: usize) -> Self {
        Self {
            crossings: vec![
                BraidCrossing::pos(strand_offset),
                BraidCrossing::neg(strand_offset + 1),
            ],
        }
    }

    /// Power $V_s^k = (\sigma_s \sigma_{s+1}^{-1})^k$.
    pub fn vertex_v_pow(strand_offset: usize, exp: usize) -> Self {
        let mut crossings = Vec::with_capacity(2 * exp);
        for _ in 0..exp {
            crossings.push(BraidCrossing::pos(strand_offset));
            crossings.push(BraidCrossing::neg(strand_offset + 1));
        }
        Self { crossings }
    }

    /// Bare Borromean 3-strand baryon core $\beta_{\mathrm{Bor}}^{(s)} = V_s^3 = (\sigma_s\sigma_{s+1}^{-1})^3$.
    pub fn borromean_v3(strand_offset: usize) -> Self {
        Self::vertex_v_pow(strand_offset, 3)
    }

    /// Underlying slice of signed crossings.
    pub fn crossings(&self) -> &[BraidCrossing] {
        &self.crossings
    }

    /// Number of crossings in the unreduced braid word.
    pub fn len(&self) -> usize {
        self.crossings.len()
    }

    /// Returns `true` iff the braid word has zero crossings.
    pub fn is_empty(&self) -> bool {
        self.crossings.is_empty()
    }

    /// Shift all generator indices by `+offset`.
    pub fn shifted(&self, offset: usize) -> Self {
        Self {
            crossings: self
                .crossings
                .iter()
                .map(|c| BraidCrossing {
                    gen: c.gen + offset,
                    sign: c.sign,
                })
                .collect(),
        }
    }

    /// Concatenate `self` followed by `other`.
    pub fn concat(&self, other: &Self) -> Self {
        let mut crossings = Vec::with_capacity(self.crossings.len() + other.crossings.len());
        crossings.extend_from_slice(&self.crossings);
        crossings.extend_from_slice(&other.crossings);
        Self { crossings }
    }

    /// Convert to `Vec<LinearFactor<R>>` for streaming Hecke / Bratteli evaluation.
    pub fn to_linear_factors<R: RingScalar>(&self, h: &R) -> Vec<LinearFactor<R>> {
        self.crossings
            .iter()
            .map(|c| c.to_linear_factor(h))
            .collect()
    }

    /// Expand in the free associative algebra $R\langle \sigma_0, \sigma_1, \dots \rangle$ via
    /// $\sigma_i^{-1} = \sigma_i - h\,\mathbf{1}$.
    pub fn to_free_alg<R: RingScalar>(&self, h: &R) -> FreeAlg<usize, R> {
        let mut acc = FreeAlg::one();
        for c in &self.crossings {
            let factor = c.to_linear_factor(h).to_free_alg();
            acc = &acc * &factor;
        }
        acc
    }
}

/// Ruled 4-term photon element at strand offset $s$:
/// $$\gamma^{(s)}(\phi_0, \phi_1, \phi_{01}) = \mathbf{1} + \phi_0\sigma_s + \phi_1\sigma_{s+1} + \phi_{01}\sigma_s\sigma_{s+1}^{-1}.$$
#[derive(Clone, PartialEq, Eq, Debug, Serialize, Deserialize)]
pub struct Photon4Term<R> {
    /// Starting strand offset $s \ge 0$ (uses generators $\sigma_s$ and $\sigma_{s+1}$, moving strands $s, s+1, s+2$).
    pub strand_offset: usize,
    /// Coefficient $\phi_0$ of $\sigma_s$.
    pub phi_0: R,
    /// Coefficient $\phi_1$ of $\sigma_{s+1}$.
    pub phi_1: R,
    /// Coefficient $\phi_{01}$ of the chiral vertex $V_s = \sigma_s\sigma_{s+1}^{-1}$.
    pub phi_01: R,
}

impl<R: RingScalar> Photon4Term<R> {
    /// Construct $\gamma^{(s)}(\phi_0, \phi_1, \phi_{01})$ at strand offset `strand_offset`.
    pub fn new(strand_offset: usize, phi_0: R, phi_1: R, phi_01: R) -> Self {
        Self {
            strand_offset,
            phi_0,
            phi_1,
            phi_01,
        }
    }

    /// Construct in the legacy unshifted basis $\mathbf{1} + \psi_0\sigma_s + \psi_1\sigma_{s+1} + \psi_{01}\sigma_s\sigma_{s+1}$
    /// using the exact chart map $\phi_0 = \psi_0 + h\psi_{01}$, $\phi_1 = \psi_1$, $\phi_{01} = \psi_{01}$.
    pub fn from_unshifted_chart(
        strand_offset: usize,
        psi_0: &R,
        psi_1: &R,
        psi_01: &R,
        h: &R,
    ) -> Self {
        let phi_0 = psi_0.add_val(&h.mul_val(psi_01));
        Self {
            strand_offset,
            phi_0,
            phi_1: psi_1.clone(),
            phi_01: psi_01.clone(),
        }
    }

    /// Return the four unreduced signed-braid summands `[([], 1), ([+s], phi_0), ([+(s+1)], phi_1), ([+s, -(s+1)], phi_01)]`.
    pub fn to_braid_terms(&self) -> [(BraidWord, R); 4] {
        let s = self.strand_offset;
        [
            (BraidWord::empty(), R::one()),
            (BraidWord::sigma(s), self.phi_0.clone()),
            (BraidWord::sigma(s + 1), self.phi_1.clone()),
            (BraidWord::vertex_v(s), self.phi_01.clone()),
        ]
    }

    /// Expand $\gamma^{(s)}(\phi)$ into `FreeAlg<usize, R>` via $\sigma_{s+1}^{-1} = \sigma_{s+1} - h\,\mathbf{1}$:
    /// $\mathbf{1} + (\phi_0 - h\phi_{01})\sigma_s + \phi_1\sigma_{s+1} + \phi_{01}\sigma_s\sigma_{s+1}$.
    pub fn to_free_alg(&self, h: &R) -> FreeAlg<usize, R> {
        let s = self.strand_offset;
        let coeff_s0 = self.phi_0.sub_val(&h.mul_val(&self.phi_01));
        FreeAlg::from_terms([
            (vec![], R::one()),
            (vec![s], coeff_s0),
            (vec![s + 1], self.phi_1.clone()),
            (vec![s, s + 1], self.phi_01.clone()),
        ])
    }
}

impl<R: RingScalar> Photon4Term<LaurentPoly<R>> {
    /// Positive-chirality eigen-photon $\gamma_+^{(s)} = \gamma^{(s)}(0, 0, qh)$ where $h = q - q^{-1}$.
    pub fn gamma_plus(strand_offset: usize) -> Self {
        let q = LaurentPoly::<R>::q();
        let h = LaurentPoly::<R>::h();
        Self::new(
            strand_offset,
            LaurentPoly::zero(),
            LaurentPoly::zero(),
            &q * &h,
        )
    }

    /// Negative-chirality eigen-photon $\gamma_-^{(s)} = \gamma^{(s)}(0, 0, -q^{-1}h)$ where $h = q - q^{-1}$.
    pub fn gamma_minus(strand_offset: usize) -> Self {
        let qi = LaurentPoly::<R>::q_inv();
        let h = LaurentPoly::<R>::h();
        Self::new(
            strand_offset,
            LaurentPoly::zero(),
            LaurentPoly::zero(),
            -(&qi * &h),
        )
    }
}

/// Expand the $k$-photon product $\gamma_1 \cdots \gamma_k$ into at most $4^k$ unreduced
/// `(BraidWord, R)` summands (retaining signed crossings before Hecke quadratic reduction so
/// whole-word linking-neutrality selection can be applied cleanly).
pub fn k_photon_braid_expansion<R: RingScalar>(photons: &[Photon4Term<R>]) -> Vec<(BraidWord, R)> {
    let mut acc: Vec<(BraidWord, R)> = vec![(BraidWord::empty(), R::one())];
    for ph in photons {
        let terms = ph.to_braid_terms();
        let mut next = Vec::with_capacity(acc.len() * 4);
        for (w_pref, c_pref) in &acc {
            if c_pref.is_zero() {
                continue;
            }
            for (w_step, c_step) in &terms {
                if c_step.is_zero() {
                    continue;
                }
                let prod = c_pref.mul_val(c_step);
                if !prod.is_zero() {
                    next.push((w_pref.concat(w_step), prod));
                }
            }
        }
        acc = next;
    }
    acc
}

/// Compute the exact Bokut–Shiao Gröbner–Shirshov normal form of a $k$-photon product
/// $\gamma^{(s_1)}(\phi_1)\cdots\gamma^{(s_k)}(\phi_k)$ in $H_n(q)$, multiplying and reducing
/// one photon at a time.
pub fn k_photon_product<R: RingScalar>(
    photons: &[Photon4Term<R>],
    hecke: &BokutShiaoHecke<R>,
) -> FreeAlg<usize, R> {
    let h = hecke.h();
    let mut state = FreeAlg::one();
    for ph in photons {
        assert!(
            ph.strand_offset + 2 <= hecke.num_strands(),
            "photon at strand_offset {} requires at least {} strands, but Hecke basis has {}",
            ph.strand_offset,
            ph.strand_offset + 3,
            hecke.num_strands()
        );
        let ph_alg = ph.to_free_alg(h);
        state = hecke.multiply_reduced(&state, &ph_alg);
    }
    state
}

/// Two-photon collision product $\gamma_1 \cdot \gamma_2$ ($4^2 = 16$ monomials) reduced in $H_n(q)$.
pub fn two_photon_product<R: RingScalar>(
    p1: &Photon4Term<R>,
    p2: &Photon4Term<R>,
    hecke: &BokutShiaoHecke<R>,
) -> FreeAlg<usize, R> {
    k_photon_product(&[p1.clone(), p2.clone()], hecke)
}

/// Three-photon collision product $\gamma_1 \cdot \gamma_2 \cdot \gamma_3$ ($4^3 = 64$ monomials) reduced in $H_n(q)$.
pub fn three_photon_product<R: RingScalar>(
    p1: &Photon4Term<R>,
    p2: &Photon4Term<R>,
    p3: &Photon4Term<R>,
    hecke: &BokutShiaoHecke<R>,
) -> FreeAlg<usize, R> {
    k_photon_product(&[p1.clone(), p2.clone(), p3.clone()], hecke)
}

/// Four-photon collision product $\gamma_1 \cdot \gamma_2 \cdot \gamma_3 \cdot \gamma_4$
/// ($4^4 = 256$ monomials) reduced to Bokut–Shiao normal form in $H_n(q)$.
pub fn four_photon_product<R: RingScalar>(
    photons: &[Photon4Term<R>; 4],
    hecke: &BokutShiaoHecke<R>,
) -> FreeAlg<usize, R> {
    k_photon_product(photons.as_slice(), hecke)
}

/// Project a $k$-photon expansion onto its whole-word linking-neutral braid summands on
/// `num_strands` strands (`PhotonU1NeutralCut`), then reduce the neutral sum to GS normal form.
pub fn k_photon_linking_neutral_projection<R: RingScalar>(
    photons: &[Photon4Term<R>],
    hecke: &BokutShiaoHecke<R>,
) -> FreeAlg<usize, R> {
    let n = hecke.num_strands();
    let h = hecke.h();
    let mut neutral_sum = FreeAlg::zero();
    for (bw, coeff) in k_photon_braid_expansion(photons) {
        if is_linking_neutral(&bw, n) {
            let elem = bw.to_free_alg(h);
            let red = hecke.reduce(&elem);
            neutral_sum.add_scaled_assign(&red, &coeff);
        }
    }
    neutral_sum
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn chiral_eigen_photon_pair_equals_borromean_v3_with_zero_hopf_electron_term() {
        type L = LaurentPoly<i64>;
        let h = L::h();
        let hecke3 = BokutShiaoHecke::new(3, h.clone());

        let gp = Photon4Term::<L>::gamma_plus(0);
        let gm = Photon4Term::<L>::gamma_minus(0);
        let pair_nf = two_photon_product(&gp, &gm, &hecke3);
        let v3_nf = hecke3.reduce(&BraidWord::borromean_v3(0).to_free_alg(&h));

        // Exact identity in Z[q, q^{-1}][H_3(q)]: gamma_+ * gamma_- == V^3 = beta_Bor!
        assert_eq!(pair_nf, v3_nf);
        // Zero coefficient on longest word sigma_0 sigma_1 sigma_0 (Hopf electron):
        assert_eq!(pair_nf.coeff(&[0, 1, 0]), L::zero());
    }

    #[test]
    fn shifted_chart_matches_unshifted_photon_expression() {
        type L = LaurentPoly<i64>;
        let h = L::h();
        let q = L::q();
        let phi0 = L::from_i64(3);
        let phi1 = L::from_i64(-2);
        let phi01 = q.clone();

        let ruled = Photon4Term::new(0, phi0.clone(), phi1.clone(), phi01.clone());
        let psi0 = &phi0 - &(&h * &phi01);
        let from_old = Photon4Term::from_unshifted_chart(0, &psi0, &phi1, &phi01, &h);
        assert_eq!(ruled, from_old);

        let unshifted_manual = FreeAlg::from_terms([
            (vec![], L::one()),
            (vec![0], psi0),
            (vec![1], phi1),
            (vec![0, 1], phi01),
        ]);
        assert_eq!(ruled.to_free_alg(&h), unshifted_manual);
    }

    #[test]
    fn four_photon_product_256_terms_and_two_baryon_factorisation() {
        type L = LaurentPoly<i64>;
        let h = L::h();

        // 1. Verify full 4^4 = 256 term expansion when all 4 coefficients are non-zero:
        let generic = Photon4Term::new(0, L::from_i64(2), L::from_i64(3), L::from_i64(5));
        let p4_3 = [
            generic.clone(),
            Photon4Term::new(0, L::from_i64(7), L::from_i64(11), L::from_i64(13)),
            generic.clone(),
            generic.clone(),
        ];
        let raw_256 = k_photon_braid_expansion(&p4_3);
        assert_eq!(raw_256.len(), 256);

        // Reduces cleanly on 3, 4, 6, and 8 strands:
        for n_strands in [3usize, 4, 6, 8] {
            let hn = BokutShiaoHecke::new(n_strands, h.clone());
            let nf = four_photon_product(&p4_3, &hn);
            assert!(!nf.is_zero());
            // On 3 strands, H_3(q) has dimension 3! = 6, so 256 terms collapse to <= 6 basis words!
            if n_strands == 3 {
                assert!(nf.num_terms() <= 6);
            }
        }

        // 2. Two-baryon 4-photon state on 6 strands:
        // gamma_+^(0) * gamma_-^(0) * gamma_+^(3) * gamma_-^(3) == V_0^3 * V_3^3!
        let hecke6 = BokutShiaoHecke::new(6, h.clone());
        let two_baryon_photons = [
            Photon4Term::<L>::gamma_plus(0),
            Photon4Term::<L>::gamma_minus(0),
            Photon4Term::<L>::gamma_plus(3),
            Photon4Term::<L>::gamma_minus(3),
        ];
        let prod_nf = four_photon_product(&two_baryon_photons, &hecke6);
        let v0_3 = BraidWord::borromean_v3(0);
        let v3_3 = BraidWord::borromean_v3(3);
        let expected_two_baryon = hecke6.reduce(&v0_3.concat(&v3_3).to_free_alg(&h));
        assert_eq!(prod_nf, expected_two_baryon);

        // And because every term of gamma_+^(s) gamma_-^(s) uses only 1 and V_s (whose powers
        // are linking-neutral!), the linking-neutral projection equals the full product!
        let neutral_proj = k_photon_linking_neutral_projection(&two_baryon_photons, &hecke6);
        assert_eq!(neutral_proj, expected_two_baryon);
    }
}
