import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:single-vortex-to-log-form-reduction",
  lean: {
    decl: "QOU.BraidsAndKnots.Stubs.single_vortex_to_log_form_reduction",
    file: "QOU/BraidsAndKnots/Stubs.lean",
    validation: "not_checked",
  },
  title:
    "Single-vortex mass formula reduces to the log-$\\Phi_q$ tower form under Wedderburn projection",
  uses: [
    "prop:mass-endomorphism-tower",
    "prop:tower-binding-energy",
    "prop:categorical-mass-markov",
    "def:quantum-bloch-group",
  ],
  tags: [
    "mass-formula",
    "quantum-dilogarithm",
    "wedderburn",
    "logarithmic-reduction",
  ],
});
