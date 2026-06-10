import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:phase-transition-boundary",
  label: "rem:molecular-hbond-phase-transition",
  title:
    "Molecular phase transitions: the hydrogen-bond network as the boundary action",
  computation: {
    engine: "python",
    status: "verified",
    script: "folio-assistant/computations/hbond_categorical_action.py",
    witness: [
      "folio-assistant/computations/hbond-categorical-action.witness.json",
    ],
  },
  uses: [
    "prop:phase-transition-boundary",
    "prop:quantum-ideal-gas-law",
    "prop:symmetric-block-domain-weight",
    "def:covalent-bond-shared-trefoil",
    "prop:tetrahedral-hbond-directions",
    "prop:boltzmann-constant",
    "def:quantum-temperature",
  ],
  tags: [
    "phase-transition",
    "hydrogen-bond",
    "boiling-point",
    "latent-heat",
    "hbond-cohesion",
    "sp3-flip",
    "q-ideal-gas",
    "water",
  ],
});
