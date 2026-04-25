import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-dilogarithm-exists",
  title: "Existence of the $q$-dilogarithm",
  lean: { ref: "qou:QOU.QDilogarithm.exists",
    validation: "not_checked",
  },
  uses: [
    "def:q-dilogarithm",
    "prop:q-logarithm-exists",
  ],
  proofs: ["prf:q-dilogarithm-exists"],
  tags: ["existence", "q-dilogarithm", "pentagon-identity"],
});
