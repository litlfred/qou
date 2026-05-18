import { proposition } from "../../schema/builders";

/**
 * The Schur-Weyl 3-root product λ_{SW}^(1)(z) appearing in the
 * categorical action integral A(a) is an EXACT rational function
 * of z with palindromic-coefficient discriminant.
 *
 * Specifically:
 *   λ_{SW}^(1)(z) = ∏_k dc_k/dz = -P(z)/D(z)
 *
 * where the cubic roots c_k(z) satisfy the color-tube cubic
 * F(z, c) = c³ + (4z+1)c² + (6z²+3z+1)c + (4z³+3z²+2z+1), and:
 *
 *   P(z) = res_c(F, F_z) = 64z⁶+96z⁵+120z⁴+160z³+105z²+66z+39
 *   D(z) = disc_c(F)     = 16z⁶+24z⁵+35z⁴+50z³+35z²+24z+16
 *
 * D(z) has palindromic coefficients (z ↔ 1/z symmetry).
 *
 * Proof: implicit function theorem + classical Vieta-resultant
 * identity. Verified numerically at z=0.1 to machine precision
 * against production `picard_lefschetz_thimble.sw_3root_product_degree1`.
 *
 * Status: PROVED. The rational form makes ∫_{-a}^{a} λ_{SW}^(1)
 * computable in closed form via partial fractions, providing the
 * algebraic foundation for the substrate-m_p categorical action.
 */
export default proposition({
  label: "prop:sw-3root-rational-integrand",
  title:
    "Schur-Weyl 3-root product is an exact rational function with palindromic discriminant",
  lean: {
    ref: "qou:QOU.BraidKnot.SW3RootRationalIntegrand",
    validation: "not_checked",
  },
  uses: [],
  cites: [
    "lang2002algebra",
  ],
  tags: [
    "schur-weyl",
    "categorical-action",
    "rational-function",
    "resultant",
    "discriminant",
    "palindromic",
    "color-tube-cubic",
    "picard-lefschetz",
    "structural-derivation",
  ],
});
