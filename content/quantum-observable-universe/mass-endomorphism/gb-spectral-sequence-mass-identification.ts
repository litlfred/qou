import { remark } from "../../schema/builders";

export default remark({
  label: "rem:gb-spectral-sequence-mass-identification",
  title: "Identification of the six mass terms with spectral-sequence pages",
  interprets: "prop:gb-spectral-sequence",
  uses: ["thm:knot-mass-formula-unified"],
  tags: ["spectral-sequence", "mass-terms", "markov-trace"],
});
