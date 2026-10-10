import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:ugb-generator-choice",
  title: "Generator choice in division",
  lean: { ref: "ugb:UGB.UnitalGroebner.lemma_generator_choice", validation: "not_checked" },
  tags: ["groebner-basis", "division"],
  uses: ["def:unital-groebner-basis", "def:admissible-system"],
});
