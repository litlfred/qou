//! Hadron braid words and crossing-local quark-charge-dressed $3\times 3$ weight-space matrices
//! (`QOU/Nuclear/NucleonChargeDressedWords.lean`).

use gs_basis::RingScalar;
use serde::{Deserialize, Serialize};

use crate::photon::BraidWord;

/// Valence quark flavour label (`Up` = $u$, `Down` = $d$).
#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Debug, Serialize, Deserialize)]
pub enum QuarkFlavour {
    /// Up-type strand ($u$).
    Up,
    /// Down-type strand ($d$).
    Down,
}

/// Nucleon isospin species (`Proton` = $uud$, `Neutron` = $udd$).
#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Debug, Serialize, Deserialize)]
pub enum NucleonKind {
    /// Proton $\mathfrak{p}$ with valence flavours `[Up, Up, Down]`.
    Proton,
    /// Neutron $\mathfrak{n}$ with valence flavours `[Up, Down, Down]`.
    Neutron,
}

impl NucleonKind {
    /// Canonical 3-strand valence quark assignment (`uud` for `Proton`, `udd` for `Neutron`).
    pub fn valence_flavours(self) -> [QuarkFlavour; 3] {
        match self {
            NucleonKind::Proton => [QuarkFlavour::Up, QuarkFlavour::Up, QuarkFlavour::Down],
            NucleonKind::Neutron => [QuarkFlavour::Up, QuarkFlavour::Down, QuarkFlavour::Down],
        }
    }
}

/// Bare 3-strand Borromean baryon braid word $\beta_{\mathrm{Bor}}^{(s)} = V_s^3 = (\sigma_s\sigma_{s+1}^{-1})^3$.
pub fn borromean_baryon_word(strand_offset: usize) -> BraidWord {
    BraidWord::borromean_v3(strand_offset)
}

/// Charged pion 2-strand Hopf braid word $\pi^\pm = \sigma_s^2 \in B_2$.
pub fn charged_pion_word(strand_offset: usize) -> BraidWord {
    BraidWord::from_pairs(&[(strand_offset, 1), (strand_offset, 1)])
}

/// Ruled electron 3-strand braid word $\sigma_s \sigma_{s+1} \sigma_s \in B_3$ (closing to the Hopf link;
/// 2026-11-21 owner ruling).
pub fn electron_hopf_word(strand_offset: usize) -> BraidWord {
    BraidWord::from_pairs(&[
        (strand_offset, 1),
        (strand_offset + 1, 1),
        (strand_offset, 1),
    ])
}

/// Exact $3 \times 3$ matrix over a commutative ring `R`.
pub type Mat3<R> = [[R; 3]; 3];

/// $3 \times 3$ identity matrix over `R`.
pub fn mat3_identity<R: RingScalar>() -> Mat3<R> {
    let z = R::zero();
    let o = R::one();
    [
        [o.clone(), z.clone(), z.clone()],
        [z.clone(), o.clone(), z.clone()],
        [z.clone(), z, o],
    ]
}

/// Exact $3 \times 3$ matrix multiplication over `R`.
pub fn mat3_mul<R: RingScalar>(a: &Mat3<R>, b: &Mat3<R>) -> Mat3<R> {
    std::array::from_fn(|i| {
        std::array::from_fn(|j| {
            let mut acc = R::zero();
            for k in 0..3 {
                acc = acc.add_val(&a[i][k].mul_val(&b[k][j]));
            }
            acc
        })
    })
}

/// Exact $3 \times 3$ matrix subtraction `a - b`.
pub fn mat3_sub<R: RingScalar>(a: &Mat3<R>, b: &Mat3<R>) -> Mat3<R> {
    std::array::from_fn(|i| std::array::from_fn(|j| a[i][j].sub_val(&b[i][j])))
}

/// Matrix trace $\sum_{i=0}^2 m_{i,i}$.
pub fn mat3_trace<R: RingScalar>(m: &Mat3<R>) -> R {
    m[0][0].add_val(&m[1][1]).add_val(&m[2][2])
}

/// One period $L_p(q, c, a, b) = \sigma_1(1 + c Q_1 Q_2)\sigma_2^{-1}(1 + c Q_2 Q_3)$ on the
/// 3-dimensional `uud` weight space $W_p$ (`NucleonChargeDressedWords.Lp_eq`), taking explicit
/// `(q, q_inv, c, a, b)` so no field division is required.
pub fn lp_matrix<R: RingScalar>(q: &R, q_inv: &R, c: &R, a: &R, b: &R) -> Mat3<R> {
    let one = R::one();
    let zero = R::zero();
    let h = q.sub_val(q_inv);
    // f_aa = 1 + a^2 * c,  f_ab = 1 + a * b * c
    let f_aa = one.add_val(&a.mul_val(a).mul_val(c));
    let f_ab = one.add_val(&a.mul_val(b).mul_val(c));
    let prod = f_aa.mul_val(&f_ab);
    let f_ab_sq = f_ab.mul_val(&f_ab);

    [
        [
            h.neg_val().mul_val(q).mul_val(&prod),
            q.mul_val(&prod),
            zero.clone(),
        ],
        [zero.clone(), zero.clone(), q_inv.mul_val(&prod)],
        [f_ab_sq, zero, h.mul_val(q_inv).mul_val(&prod)],
    ]
}

/// One period $L_n(q, c, a, b)$ on the 3-dimensional `udd` weight space $W_n$
/// (`NucleonChargeDressedWords.Ln_eq`).
pub fn ln_matrix<R: RingScalar>(q: &R, q_inv: &R, c: &R, a: &R, b: &R) -> Mat3<R> {
    let one = R::one();
    let zero = R::zero();
    let h = q.sub_val(q_inv);
    let h_sq = h.mul_val(&h);
    // f_bb = 1 + b^2 * c,  f_ab = 1 + a * b * c
    let f_bb = one.add_val(&b.mul_val(b).mul_val(c));
    let f_ab = one.add_val(&a.mul_val(b).mul_val(c));
    let prod = f_bb.mul_val(&f_ab);
    let f_ab_sq = f_ab.mul_val(&f_ab);

    [
        [
            zero.clone(),
            h.neg_val().mul_val(&f_ab_sq),
            f_ab_sq.clone(),
        ],
        [
            q_inv.mul_val(&prod),
            h_sq.neg_val().mul_val(&f_ab_sq),
            h.mul_val(&f_ab_sq),
        ],
        [zero.clone(), q.mul_val(&prod), zero],
    ]
}

/// Dressed proton operator $M_p(q, c, a, b) = L_p(q, c, a, b)^3$.
pub fn mp_matrix<R: RingScalar>(q: &R, q_inv: &R, c: &R, a: &R, b: &R) -> Mat3<R> {
    let lp = lp_matrix(q, q_inv, c, a, b);
    let lp2 = mat3_mul(&lp, &lp);
    mat3_mul(&lp2, &lp)
}

/// Dressed neutron operator $M_n(q, c, a, b) = L_n(q, c, a, b)^3$.
pub fn mn_matrix<R: RingScalar>(q: &R, q_inv: &R, c: &R, a: &R, b: &R) -> Mat3<R> {
    let ln = ln_matrix(q, q_inv, c, a, b);
    let ln2 = mat3_mul(&ln, &ln);
    mat3_mul(&ln2, &ln)
}

/// Exact cofactor polynomial $G(q, a, b, c) = G_{c0}(q,a,b) + c\,G_{c1}(q,a,b) + c^2\,G_{c2}(q,a,b)$
/// satisfying $q^6(\operatorname{tr}(M_n) - \operatorname{tr}(M_p)) = c(a - b)(1 + abc)^3 G(q, a, b, c)$
/// (`NucleonChargeDressedWords.G`).
pub fn g_cofactor_poly<R: RingScalar>(q: &R, a: &R, b: &R, c: &R) -> R {
    let p = |k: u32| q.pow_u32(k);
    let s = |n: i64| R::from_i64(n);

    let q2 = p(2);
    let q4 = p(4);
    let q6 = p(6);
    let q8 = p(8);
    let q10 = p(10);
    let q12 = p(12);

    // Common symmetric base S0 = q^12 - 3 q^10 + 3 q^8 + 3 q^4 - 3 q^2 + 1
    let base_even = q12
        .sub_val(&s(3).mul_val(&q10))
        .add_val(&s(3).mul_val(&q8))
        .add_val(&s(3).mul_val(&q4))
        .sub_val(&s(3).mul_val(&q2))
        .add_val(&R::one());

    let p_a_c0 = base_even.sub_val(&s(4).mul_val(&q6));
    let p_b_c0 = q10
        .sub_val(&s(4).mul_val(&q8))
        .add_val(&s(4).mul_val(&q6))
        .sub_val(&s(4).mul_val(&q4))
        .add_val(&q2);
    let gc0 = s(3).mul_val(&a.mul_val(&p_a_c0).add_val(&b.mul_val(&p_b_c0)));

    let p_a3_c1 = base_even.sub_val(&s(3).mul_val(&q6));
    let p_a2b_c1 = base_even.sub_val(&s(5).mul_val(&q6));
    let p_ab2_c1 = s(2)
        .mul_val(&q10)
        .sub_val(&s(8).mul_val(&q8))
        .add_val(&s(9).mul_val(&q6))
        .sub_val(&s(8).mul_val(&q4))
        .add_val(&s(2).mul_val(&q2));
    let gc1 = s(3).mul_val(
        &a.pow_u32(3)
            .mul_val(&p_a3_c1)
            .add_val(&a.pow_u32(2).mul_val(b).mul_val(&p_a2b_c1))
            .add_val(&a.mul_val(&b.pow_u32(2)).mul_val(&p_ab2_c1))
            .sub_val(&b.pow_u32(3).mul_val(&q6)),
    );

    let p_a4_c2 = base_even.sub_val(&s(2).mul_val(&q6));
    let p_ab3_c2 = s(3)
        .mul_val(&q10)
        .sub_val(&s(12).mul_val(&q8))
        .add_val(&s(15).mul_val(&q6))
        .sub_val(&s(12).mul_val(&q4))
        .add_val(&s(3).mul_val(&q2));
    let gc2 = a.mul_val(
        &a.pow_u32(4)
            .mul_val(&p_a4_c2)
            .add_val(&a.pow_u32(3).mul_val(b).mul_val(&p_a2b_c1))
            .add_val(&a.pow_u32(2).mul_val(&b.pow_u32(2)).mul_val(&p_a2b_c1))
            .add_val(&a.mul_val(&b.pow_u32(3)).mul_val(&p_ab3_c2))
            .sub_val(&s(3).mul_val(&b.pow_u32(4)).mul_val(&q6)),
    );

    gc0.add_val(&c.mul_val(&gc1))
        .add_val(&c.pow_u32(2).mul_val(&gc2))
}

/// Ruled photon-pair polynomial $\Gamma_q(L) = \mathbf{I} + h^2 L - h^2 L^2$ evaluated on $3\times 3$ matrix `l`
/// (`NucleonChargeDressedWords.photonPair`).
pub fn photon_pair_matrix<R: RingScalar>(q: &R, q_inv: &R, l: &Mat3<R>) -> Mat3<R> {
    let h = q.sub_val(q_inv);
    let h2 = h.mul_val(&h);
    let id = mat3_identity::<R>();
    let l2 = mat3_mul(l, l);
    std::array::from_fn(|i| {
        std::array::from_fn(|j| {
            id[i][j]
                .add_val(&h2.mul_val(&l[i][j]))
                .sub_val(&h2.mul_val(&l2[i][j]))
        })
    })
}

#[cfg(test)]
mod tests {
    use super::*;
    use gs_basis::{rat, LaurentPoly};
    use num_rational::BigRational;

    #[test]
    fn nucleon_charge_dressed_trace_split_and_photon_factorisation_defect() {
        type L = LaurentPoly<BigRational>;
        let q = L::q();
        let qi = L::q_inv();

        // 1. Undressed (c = 0) and equal-charge (a = b) vanish identically in Q[q, q^{-1}]:
        let a = L::constant(rat(2, 3));
        let b = L::constant(rat(-1, 3));
        let c0 = L::zero();
        assert_eq!(
            mat3_trace(&mn_matrix(&q, &qi, &c0, &a, &b)),
            mat3_trace(&mp_matrix(&q, &qi, &c0, &a, &b))
        );

        let c_nz = L::constant(rat(3, 7));
        assert_eq!(
            mat3_trace(&mn_matrix(&q, &qi, &c_nz, &a, &a)),
            mat3_trace(&mp_matrix(&q, &qi, &c_nz, &a, &a))
        );

        // 2. Exact polynomial identity `trace_dressed_split`:
        // q^6 * (tr(Mn) - tr(Mp)) == c * (a - b) * (1 + a*b*c)^3 * G(q, a, b, c)
        let tr_mn = mat3_trace(&mn_matrix(&q, &qi, &c_nz, &a, &b));
        let tr_mp = mat3_trace(&mp_matrix(&q, &qi, &c_nz, &a, &b));
        let lhs = q.pow_u32(6).mul_val(&tr_mn.sub_val(&tr_mp));

        let one = L::one();
        let one_plus_abc = one.add_val(&a.mul_val(&b).mul_val(&c_nz));
        let g_val = g_cofactor_poly(&q, &a, &b, &c_nz);
        let rhs = c_nz
            .mul_val(&a.sub_val(&b))
            .mul_val(&one_plus_abc.pow_u32(3))
            .mul_val(&g_val);
        assert_eq!(lhs, rhs);
        assert!(!lhs.is_zero());

        // 3. Exact `photonFactorisationDefect_one_zero`:
        // q^3 * (Mp - photonPair(q, Lp))[1][0] == -a*c*(q^2 - 1)^2*(1 + a^2*c)*(1 + a*b*c)^3*(a^2*b*c + a + b)
        let lp = lp_matrix(&q, &qi, &c_nz, &a, &b);
        let mp = mp_matrix(&q, &qi, &c_nz, &a, &b);
        let pp = photon_pair_matrix(&q, &qi, &lp);
        let defect = mat3_sub(&mp, &pp);
        let defect_10_scaled = q.pow_u32(3).mul_val(&defect[1][0]);

        let q2_minus_1_sq = q.pow_u32(2).sub_val(&one).pow_u32(2);
        let one_plus_a2c = one.add_val(&a.pow_u32(2).mul_val(&c_nz));
        let tail = a
            .pow_u32(2)
            .mul_val(&b)
            .mul_val(&c_nz)
            .add_val(&a)
            .add_val(&b);
        let expected_defect = a
            .mul_val(&c_nz)
            .neg_val()
            .mul_val(&q2_minus_1_sq)
            .mul_val(&one_plus_a2c)
            .mul_val(&one_plus_abc.pow_u32(3))
            .mul_val(&tail);
        assert_eq!(defect_10_scaled, expected_defect);
        assert!(!defect_10_scaled.is_zero());
    }
}
