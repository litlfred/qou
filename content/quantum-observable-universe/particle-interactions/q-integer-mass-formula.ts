import { proposition } from "../../schema/builders";

/**
 * The Bethe-Weizsäcker coefficients are q-integer products.
 *
 * All seven extended BW coefficients are derivable from the substrate
 * parameter q₀ alone as products of quantum integers
 * [n]_q = (q^n - q^{-n})/(q - q^{-1}) times m_e.  The two additional
 * terms (exchange Coulomb and shell correction) are derived from Hecke
 * representation theory and the shell closure / palindromicity
 * conjectures.
 */
export default proposition({
  label: "prop:q-integer-mass-formula",
  title: "Atomic mass formula with $q$-integer Bethe--Weizs\\\"acker coefficients",
  uses: [
    "prop:wedderburn-mass-formula",
    "prop:operator-selection-lp",
    "conj:palindromicity-orbital-type",
  ],
  tags: [
    "mass-formula",
    "q-integer",
    "Bethe-Weizsacker",
    "zero-parameters",
    "Wedderburn",
    "exchange-coulomb",
    "shell-correction",
    "exceptional-divisor",
  ],
});
