import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:bring-brane",
  title: "Bring surface ($\\chi = -6$ brane) — substrate constants",
  uses: [
    "def:brings-surface",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/bring_chiral_fibre_figure.py",
    witness: "computations/bring-chiral-fibre-figure.witness.json",
    status: "verified",
  },
  tags: [
    "mba",
    "step-4",
    "bring-surface",
    "brane",
    "constants",
    "canonical-chain",
  ],
});
