import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-planck-constant",
  title: "Quantum Planck Constant",
  tags: ["planck", "deformation"],
  lean: { ref: "qou:QOU.quantumPlanckConstant",
    validation: "leanok",
  },
  uses: ["def:substrate-parameter"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "Two things pin this one. (1) `ℏ_q(p) = 1 - q(p)⁻¹` is proved to lie " +
        "in `[0, 1)` from the **ordering hypotheses** `field_ge_one` and " +
        "`field_pos` on the substrate field — the §7c \"ordering `0 < q` → " +
        "`ℝ`\" row. (2) Those hypotheses live on `QOU.SubstrateParameter`, " +
        "which **42 files** in the library mention; the base ring cannot be " +
        "moved for this block in isolation. The block therefore sits on the " +
        "archimedean side of the §7c wall, and any change is a " +
        "`SubstrateParameter` refactor rather than a per-block one.",
    },
  ],
});
