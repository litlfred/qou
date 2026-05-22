import { remark } from "../../schema/builders";

export default remark({
  label: "rem:mass-endomorphism-jet-tower",
  title: "Jet-brane reformulation of the mass tower",
  interprets: "prop:mass-tower-operator-valued",
  uses: ["prop:mass-tower-operator-valued"],
  tags: ["mass-tower", "jet-stratification", "audit"],
});
