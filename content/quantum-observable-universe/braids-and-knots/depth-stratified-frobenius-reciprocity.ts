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
    "prop:plancherel-term-7-formulation",
    "prop:unified-curvature-rank-mass-formula",
    "prop:free-config-chi-lr-equivalence",
    "prop:chirality-from-frobenius-self-pairing",
    "thm:jones-markov-trace",
  ],
  cites: ["frobenius1898", "macdonald1995", "lewin1981"],
  computation: {
    engine: "python",
    script:
      "folio-assistant/computations/binding_depth_stratified_knot_weighted.py",
    witness:
      "folio-assistant/computations/binding-depth-stratified-knot-weighted.witness.json",
    status: "open-research-falsification-recorded",
  },
  tags: [
    "frobenius-reciprocity",
    "curvature-rank",
    "knot-ideal",
    "chirality-channel",
    "binding-energy",
    "research-open",
    "drum-shape",
  ],
});
