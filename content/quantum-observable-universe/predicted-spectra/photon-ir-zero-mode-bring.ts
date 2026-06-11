import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:photon-ir-zero-mode-bring",
  title:
    "Photon IR zero-mode on Bring's surface: $\\delta(1/\\alpha_{EM})_{\\mathrm{IR}} = b_1/\\mathrm{Area} = 2g/(4\\pi(g-1))$",
  lean: {
    ref: "qou:QOU.Archimedean.PhotonIRZeroMode.photonZeroModeShift_eq",
    validation: "not_checked",
  },
  computation: {
    engine: "python",
    status: "verified",
    script: "folio-assistant/computations/photon_ir_zero_mode_bring.py",
    witness: [
      "folio-assistant/computations/photon-ir-zero-mode-bring.witness.json",
    ],
  },
  uses: [
    "prop:em-coupling-bring-zero-mode",
    "prop:force-carrier-bring-uniqueness",
    "prop:jet-sw-tau-decomposition",
  ],
  tags: [
    "alpha-em",
    "bring-surface",
    "hodge",
    "gauss-bonnet",
    "photon-zero-mode",
    "harmonic-forms",
    "from-lagrangian",
  ],
});
