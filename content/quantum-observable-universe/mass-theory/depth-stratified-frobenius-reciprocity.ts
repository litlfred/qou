import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:depth-stratified-frobenius-reciprocity",
  title:
    "Frobenius-reciprocity ideal restriction at low curvature-rank",
  lean: {
    ref: "qou:QOU.BraidKnot.DepthStratifiedFrobeniusReciprocity",
    validation: "not_checked",
  },
  uses: [
    "cor:lr-tensor-character-bridge",
    "prop:chirality-from-frobenius-self-pairing",
  ],
  cites: ["frobenius1898", "macdonald1995", "lewin1981"],
  computation: {
    engine: "python",
    script:
      "computations/binding_depth_stratified_knot_weighted.py",
    witness:
      "computations/binding-depth-stratified-knot-weighted.witness.json",
    status: "experimental",
  },
  tags: [
    "tier:S",
    "frobenius-reciprocity",
    "curvature-rank",
    "knot-ideal",
    "chirality-channel",
    "binding-energy",
    "research-open",
    "drum-shape",
  ],
});
