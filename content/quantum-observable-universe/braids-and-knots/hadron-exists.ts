import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hadron-exists",
  title: "Existence of hadrons",
  lean: {
    decl: "QOU.Hadron.exists",
    validation: "not_checked",
  },
  uses: [
    "def:hadron",
    "def:crossing-energy",
    "def:categorical-proton",
  ],
  proofs: ["prf:hadron-exists"],
  tags: ["existence", "hadron"],
});
