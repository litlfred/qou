import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:categorical-irreducible",
  lean: { ref: "qou:QOU.categorical_irreducible",
    validation: "not_checked",
  },
  title: "Irreducibility from observability",
  tags: ["irreducibility", "instanton"],
  uses: ["def:categorical-instanton"],
  proofs: ["prf:categorical-irreducible"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-irreducible-0.svg", blockIndex: 0, hash: "2b1f63269ecd" },
  ],

});
