import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:assembly-projector-exists",
  title: "Existence of the symmetric-block assembly projector",
  lean: {
    ref: "qou:QOU.Molecular.symmetric_assembly_projector_exists",
    validation: "not_checked",
  },
  uses: ["def:molecular-assembly-projector"],
  cites: ["wenzl1988", "kassel1995"],
  tags: [
    "assembly-projector",
    "existence",
    "idempotent",
    "q-young-symmetrizer",
    "delocalization",
  ],
});
