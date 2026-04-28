import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:brings-is-qou",
  lean: { ref: "qou:QOU.Brings.brings_is_qou",
    validation: "not_checked",
  },
  title: "Bring's surface is a quantum observable universe",
  uses: [
    "def:brings-surface",
    "thm:qu-to-qou",
  ],
  proofs: ["prf:brings-is-qou"],
});
