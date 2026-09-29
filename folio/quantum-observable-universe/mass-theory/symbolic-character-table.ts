import { proposition } from "../../schema/builders";
export default proposition({
  label: "prop:symbolic-character-table",
  title: "Symbolic character table $\\chi_\\lambda(\\sigma)$ for all partitions $H_2$--$H_7$",
  lean: { ref: "qou:QOU.BraidKnot.symbolic_character_table", validation: "not_checked" },
  uses: ["prop:wedderburn-trace-identity"],
  tags: ["character", "seminormal", "symbolic", "partition", "self-conjugate"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-07-19",
      body:
        "The self-conjugate column $c_\\lambda \\in \\{1,3,8,10\\}$ " +
        "($\\lambda \\in \\{[2,1],[3,1,1],[3,2,1],[4,1,1,1]\\}$) is Lean-proved " +
        "sorry-free in `QOU.BraidKnot.ClambdaColumn` " +
        "(`clambda_21` / `clambda_311` / `clambda_321` / `clambda_4111`), as " +
        "$c_\\lambda = \\#\\mathrm{SYT}(\\lambda)/2$: the single-generator count " +
        "$2c_\\lambda = \\#\\mathrm{SYT}$ (`two_mul_card_rowClass_eq_card`) together " +
        "with the machine-checked Frame–Robinson–Thrall hook-length formula " +
        "(`QOU.Mathlib.numStandardYoungTableaux_mul_hookLengthProduct`), which pins " +
        "$\\#\\mathrm{SYT} \\in \\{2,6,16,20\\}$. The general $n\\le 7$ table and the " +
        "pair characters remain compute-verified (probe), not yet Lean-proved.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/symbolic_character_table_probe.py",
    witness: "computations/probes/symbolic-character-table-probe.witness.json",
    status: "verified",
  },
});
