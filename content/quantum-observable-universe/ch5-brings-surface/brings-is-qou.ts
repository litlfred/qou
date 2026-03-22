import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:brings-is-qou",
  title: "Bring's surface is a quantum observable universe",
  uses: [
    "def:brings-surface",
    "prop:yekutieli-lifting",
    "thm:qu-to-qou",
  ],
  proofs: ["prf:brings-is-qou"],
});
