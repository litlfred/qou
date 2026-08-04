import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hadron-exists",
  title: "Existence of hadrons",
  lean: { ref: "qou:QOU.Hadron.exists",
    validation: "not_checked",
  },
  proofs: ["prf:hadron-exists"],
  tags: ["existence", "hadron"],
});
