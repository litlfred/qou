import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pentagon-ascension-bound",
  lean: {
    decl: "QOU.BraidsAndKnots.Stubs.pentagon_ascension_bound",
    file: "QOU/BraidsAndKnots/Stubs.lean",
    validation: "not_checked",
  },
  title:
    "Pentagon-factored $\\Phi_q$ product has $R$-factor bounded by $1 + O(\\hbar_q^2)$",
  uses: [
    "def:quantum-bloch-group",
    "prop:single-vortex-to-log-form-reduction",
    "def:recursive-brane-tower",
  ],
  tags: [
    "pentagon-identity",
    "quantum-dilogarithm",
    "r-factor",
    "jet-ascension",
    "brane-tower",
  ],
});
