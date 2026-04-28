import { proposition } from "../../schema/builders";
export default proposition({
  label: "prop:symbolic-character-table",
  title: "Symbolic character table $\\chi_\\lambda(\\sigma)$ for all partitions $H_2$--$H_7$",
  lean: { ref: "qou:QOU.BraidKnot.symbolic_character_table", validation: "not_checked" },
  uses: ["rem:hecke-algebra-from-braiding", "prop:wedderburn-trace-identity"],
  tags: ["character", "seminormal", "symbolic", "partition", "self-conjugate"],
});
