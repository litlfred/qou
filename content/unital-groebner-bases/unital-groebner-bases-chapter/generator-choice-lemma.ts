import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:generator-choice",
  title: "Generator choice in the division algorithm",
  lean: { ref: "ugb:UGB.UnitalGroebner.generator_choice", validation: "not_checked" },
  tags: ["groebner-basis", "division", "generator"],
  uses: ["def:groebner-basis", "def:division-algorithm"],
  proofs: ["prf:generator-choice"],
});
