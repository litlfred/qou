import { remark } from "../../schema/builders";

export default remark({
  label: "rem:wedderburn-vs-schur-natural",
  title:
    "Both Wedderburn and Schur appear naturally — they have different roles in the tower formula",
  interprets: "prop:tower-binding-energy",
  uses: [
    "prop:tower-binding-energy",
    "prop:mass-endomorphism-tower",
    "prop:categorical-mass-markov",
    "def:categorical-action",
  ],
  tags: [
    "wedderburn",
    "markov-schur",
    "derivation",
    "tower-formula",
    "small-a-anomaly",
  ],
});
