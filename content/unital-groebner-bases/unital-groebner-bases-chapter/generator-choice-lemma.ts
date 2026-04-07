import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:generator-choice",
  title: "Generator choice in the division algorithm",
  tags: ["groebner-basis", "division", "generator"],
  uses: ["def:groebner-basis", "def:division-algorithm"],
  proofs: ["prf:generator-choice"],
});
