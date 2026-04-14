import { proposition } from "../../schema/builders";

/**
 * The Bethe-Weizsäcker coefficients are q-integer products.
 *
 * All five semi-empirical mass formula coefficients are derivable
 * from the substrate parameter q₀ alone as products of quantum
 * integers [n]_q = (q^n - q^{-n})/(q - q^{-1}) times m_e.
 */
export default proposition({
  label: "prop:q-integer-mass-formula",
  title: "Atomic mass formula with $q$-integer Bethe--Weizs\\\"acker coefficients",
  uses: [
    "def:atomic-braid",
    "prop:wedderburn-mass-formula",
    "prop:operator-selection-lp",
  ],
  tags: [
    "mass-formula",
    "q-integer",
    "Bethe-Weizsacker",
    "zero-parameters",
    "Wedderburn",
  ],
});
