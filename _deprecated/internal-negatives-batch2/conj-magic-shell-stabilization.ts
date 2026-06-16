import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:magic-shell-stabilization",
  title: "Magic-shell stabilization term $\\Delta_{\\mathrm{shell}}(Z, N)$ in the brane-tower binding formula",
  lean: { ref: "qou:QOU.BraidKnot.MagicShellStabilization" },
  uses: [
    "conj:brane-tower-z-habiro",
    "prop:spin-involution-lp-dual-invariance",
    "def:confined-particle",
    "prop:operator-selection-lp",
  ],
  tags: [
    "brane-tower",
    "magic-numbers",
    "shell-stabilization",
    "isospin",
    "z-n-symmetry",
    "open-problem",
    "post-n-star-closure",
  ],
  computation: {
    engine: "python",
    script: "computations/probe_phiq_pair_knot_magic_shell.py",
    witness: [
      "computations/probe-phiq-pair-knot-magic-shell.witness.json",
      "computations/probe-phiq-pair-knot-markov-trace.witness.json",
      "computations/tr-m-he4-canonical.witness.json",
    ],
    status: "experimental",
  },
});
