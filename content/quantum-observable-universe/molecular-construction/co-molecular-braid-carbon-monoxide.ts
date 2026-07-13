import { example } from "../../schema/builders";

/**
 * Worked construction of the CO molecular braid in three stages:
 * build the constituent atoms, assemble in H_42(q), reduce to NF.
 */
export default example({
  label: "ex:co-molecular-braid-carbon-monoxide",
  title: "Building the carbon monoxide braid",
  interprets: "def:co-molecular-braid",
  uses: ["def:co-molecular-braid", "def:atomic-braid"],
  tags: [
    "carbon-monoxide",
    "CO",
    "triple-bond",
    "heteronuclear",
    "molecular-braid",
  ],
});
