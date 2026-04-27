import { proposition } from "../../schema/builders";

/**
 * The Bethe-Weizsäcker coefficients are not fitted parameters:
 * they are shadow prices (LP dual variables) of the Frobenius
 * positivity constraints in the nuclear operator selection LP.
 *
 * This closes the derivation loop:
 *   operator-selection-lp → shadow prices → BW coefficients
 *   bw-categorical-descent → partition structure → scaling functions
 *   wedderburn-trace-identity → normalization → trace budget
 *
 * At each Hecke level k, the BW coefficient for partition λ ⊢ k
 * is c_λ = y_λ^* · m_e, where y_λ^* is the optimal dual variable
 * of the Frobenius constraint ⟨Φ, π_λ⟩_F ≥ 0.
 */
export default proposition({
  label: "prop:bw-coefficient-shadow-price",
  title:
    "BW coefficients as shadow prices of the Frobenius positivity constraints",
  lean: { ref: "qou:QOU.BraidKnot.BWCoefficientShadowPrice",
    validation: "not_checked",
  },
  uses: [
    "prop:bw-categorical-descent",
    "prop:wigner-coefficient-derivation",
  ],
  tags: [
    "bethe-weizsaecker",
    "shadow-price",
    "lp-duality",
    "frobenius-positivity",
    "wedderburn",
    "derived-coefficient",
  ],
});
