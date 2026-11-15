import { definition } from "../../schema/builders";

export default definition({
  label: "def:molecular-assembly-projector",
  title: "Molecular assembly projector $e_{\\lambda,\\mu}$",
  lean: {
    ref: "qou:QOU.Molecular.AssemblyProjector",
    validation: "not_checked",
  },
  uses: ["def:parabolic-hecke-subalgebra", "rem:h3-hecke-idempotents"],
  tags: [
    "assembly-projector",
    "idempotent",
    "jones-wenzl",
    "wedderburn",
    "delocalization",
    "q-young-symmetrizer",
  ],
});
