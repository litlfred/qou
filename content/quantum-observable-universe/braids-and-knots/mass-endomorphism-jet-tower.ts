import { remark } from "../../schema/builders";

export default remark({
  label: "rem:mass-endomorphism-jet-tower",
  title: "Jet-brane reformulation of the mass tower",
  interprets: "prop:mass-endomorphism-tower",
  uses: ["prop:mass-endomorphism-tower"],
  tags: ["mass-tower", "jet-stratification", "audit"],
});
