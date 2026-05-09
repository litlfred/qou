import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:rho-k-h3a-refinement",
  title:
    "$H_{3A}$ Wedderburn refinement of the categorical density $\\rho_K$ beyond leading-order",
  lean: {
    ref: "qou:QOU.BraidKnot.rho_k_h3a_refinement",
    validation: "not_checked",
  },
  uses: [
    "prop:atomic-mass-gb-nf",
    "prop:hoefsmit-scattering-pipeline",
    "prop:y-lambda-closed-form-wenzl-bridge",
    "prop:wedderburn-as-noncomm-fourier",
    "prop:schur-weyl-mass-decomposition",
    "prop:six-term-mass-formula-complete",
  ],
  cites: ["wenzl1988", "hoefsmit1974", "kassel1995"],
  tags: [
    "rho-k",
    "wedderburn",
    "H_3A",
    "plancherel",
    "wenzl-bridge",
    "hoefsmit",
    "1ppb",
    "derivation",
  ],
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/rho_k_h3a_refinement.py",
    witness: "folio-assistant/computations/rho-k-h3a-refinement.witness.json",
    status: "stub",
  },
});
