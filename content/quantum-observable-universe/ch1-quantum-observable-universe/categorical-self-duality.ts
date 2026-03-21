import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-self-duality",
  title: "Categorical self-duality",
  tags: ["self-duality", "yang-mills"],
  lean: {
    decl: "QOU.categorical_self_duality",
    validation: "leanok",
  },
  status: "not_started",
  uses: [
    "def:categorical-instanton",
    "def:q-hodge-star",
  ],
  proofs: ["prf:categorical-self-duality"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-self-duality-0.svg", blockIndex: 0, hash: "68a5ca708cf5" },
  ],

});
