import { proof } from "../../schema/builders";

export default proof({
  label: "prf:qu-to-qou",
  title: "Proof of QU with observability and categorical lifting is a QOU",
  uses: ["thm:qu-to-qou"],
});
