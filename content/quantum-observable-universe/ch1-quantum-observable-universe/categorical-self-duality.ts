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
  hasProof: true,
  uses: [
    "def:categorical-instanton",
    "def:q-hodge-star",
  ],
});
