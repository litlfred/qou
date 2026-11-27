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
    ref: "qou:QOU.Confinement.QIntegerMassFormula",
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
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`): `2026-08-24-qintegermassformula-vacuity-probe.lean` shows `QOU.Interactions.QIntegerMassFormula` synthesises `canonical` (`f_magic = 0`) globally and `fits_AME_conditional` projects `IsAMEValue.fits_bound` directly.",
      see: "docs/audits/2026-08-24-qintegermassformula-vacuity-probe.lean",
    },
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation refutation (`qou-x60n`): `2026-09-04-conjecture-carriers-round-two.lean` (`C5.not_inhabited`) proves the unrestricted `∀ B_AME : ℝ` `QIntegerMassFormula` class in `mass-theory/q-integer-mass-formula.lean` is uninhabitable (`¬ Nonempty QIntegerMassFormula`), making theorems conditioned on that copy vacuously true.",
      see: "docs/audits/2026-09-04-conjecture-carriers-round-two.lean",
    },
  ],
});
