import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:sigma-shell-from-beta-chain-derivation",
  title:
    "Closed-form derivation of $\\sigma_{\\mathrm{shell}}$ magnitude from compound $\\beta$-decay chain Q-values",
  lean: {
    ref: "qou:QOU.BraidKnot.sigma_shell_from_beta_chain",
    validation: "not_checked",
  },
  uses: [
    "prop:compound-beta-shell-calibration",
    "prop:rho-k-h3a-refinement",
  ],
  cites: ["wenzl1988", "kassel1995"],
  tags: [
    "sigma-shell",
    "beta-decay",
    "AME",
    "shell-magnitude",
    "y-target",
    "magic-numbers",
    "1ppb",
    "derivation",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/sigma_shell_from_beta_chain.py",
    witness: "computations/sigma-shell-from-beta-chain.witness.json",
    status: "experimental",
  },
});
