import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:knot-factor-shell-closed",
  proofs: ["prf:knot-factor-shell-closed"],
  title:
    "Shell-closed $Z = N$ even-even nuclei give $a = 1$ exactly",
  lean: {
    ref: "qou:QOU.BraidKnot.knot_factor_shell_closed",
    validation: "not_checked",
  },
  uses: ["prop:knot-factor-spectral-form"],
  tags: [
    "knot-factor",
    "shell-closed",
    "even-even",
    "markov-equilibrium",
    "carbon-12",
    "calcium-40",
    "iron-56",
    "lead-208",
  ],
});
