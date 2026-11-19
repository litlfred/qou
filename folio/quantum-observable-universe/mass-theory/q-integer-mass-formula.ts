import { conjecture } from "../../schema/builders";

/**
 * The seven-term atomic mass-formula coefficients are q-integer products.
 *
 * All seven coefficients are derivable from the substrate parameter q₀
 * alone as products of quantum integers
 * [n]_q = (q^n - q^{-n})/(q - q^{-1}) times m_e.  The two additional
 * terms (exchange Coulomb and shell correction) are derived from Hecke
 * representation theory and the shell closure / palindromicity
 * conjectures.
 */
export default conjecture({
  label: "conj:q-integer-mass-formula",
  title: "Seven-term atomic mass formula with $q$-integer coefficients",
  lean: {
    ref: "qou:QOU.Interactions.QIntegerMassFormula",
    validation: "not_checked",
  },
  uses: [
    "thm:wedderburn-mass-formula",
    "prop:operator-selection-lp",
    "conj:palindromicity-orbital-type",
  ],
  tags: [
    "mass-formula",
    "q-integer",
    "zero-parameters",
    "Wedderburn",
    "exchange-coulomb",
    "shell-correction",
    "exceptional-divisor",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
