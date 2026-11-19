import { proof } from "../../schema/builders";

export default proof({
  label: "prf:per-nucleon-shift-additive-linearity",
  title: "Proof of per nucleon shift additive linearity",
  uses: ["prop:per-nucleon-shift-additive-linearity"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witnesses: computations/per-irrep-pole-proton-h3.witness.json, per-irrep-pole-deuteron-h6.witness.json, y-lambda-wenzl-bridge-symbolic-witness.json, chi-deuteron-h6.witness.json.",
    },
  ],
});
