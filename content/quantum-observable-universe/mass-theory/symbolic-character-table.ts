import { proposition } from "../../schema/builders";
export default proposition({
  label: "prop:symbolic-character-table",
  title: "Symbolic character table $\\chi_\\lambda(\\sigma)$ for all partitions $H_2$--$H_7$",
  lean: { ref: "qou:QOU.BraidKnot.symbolic_character_table", validation: "not_checked" },
  uses: ["prop:wedderburn-trace-identity"],
  tags: ["character", "seminormal", "symbolic", "partition", "self-conjugate"],
  computation: {
    engine: "mpmath",
    script: "computations/probes/symbolic_character_table_probe.py",
    witness: "computations/probes/symbolic-character-table-probe.witness.json",
    status: "verified",
  },
});
