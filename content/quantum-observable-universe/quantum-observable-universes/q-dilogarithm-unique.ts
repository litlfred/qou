import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-dilogarithm-unique",
  title: "Uniqueness of the $q$-dilogarithm",
  lean: { ref: "qou:QOU.QDilogarithm.unique",
    validation: "not_checked",
  },
  uses: ["prop:q-dilogarithm-exists"],
  proofs: ["prf:q-dilogarithm-unique"],
  tags: ["uniqueness", "q-dilogarithm"],
});
