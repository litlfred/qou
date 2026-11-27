import { table } from "../../schema/builders";

export default table({
  label: "tbl:lean-community-libraries-dag",
  title:
    "Dependency graph and module inventory of the six standalone Lean 4 Reservoir community libraries",
  uses: ["prose:formalisation-coverage"],
  tags: ["lean-infrastructure", "reservoir", "community-libraries", "dag", "appendix"],
});
