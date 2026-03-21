import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:categorical-irreducible",
  title: "Irreducibility from observability",
  tags: ["irreducibility", "instanton"],
  lean: {
    decl: "QOU.categorical_irreducible",
    validation: "leanok",
  },
  status: "not_started",
  hasProof: true,
  uses: [
    "def:quantum-observable-universe",
    "def:categorical-instanton",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-irreducible-0.svg", blockIndex: 0, hash: "2b1f63269ecd" },
  ],

});
