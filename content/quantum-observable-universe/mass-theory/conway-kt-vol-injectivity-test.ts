import { remark } from "../../schema/builders";

export default remark({
  label: "rem:conway-kt-vol-injectivity-test",
  title:
    "Conway--Kinoshita--Terasaka mutant pair: B1 Vol-injectivity sanity check",
  interprets: "rem:transcendental-accounting",
  uses: [
    "rem:transcendental-accounting",
    "conj:gb-depth-period-correspondence",
    "rem:knot-exhaustiveness",
    "rem:bring-embeddable-knots",
    "prop:knot-indexed-convolution-grid",
  ],
  cites: ["thurston1978"],
  tags: [
    "mutant-pair",
    "conway-knot",
    "kinoshita-terasaka",
    "vol-injectivity",
    "ruberman-theorem",
    "sanity-check",
    "graded-mikusinski",
  ],
});
