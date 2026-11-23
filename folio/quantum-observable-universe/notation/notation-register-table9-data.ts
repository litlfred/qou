import { table } from "../../schema/builders";
export default table({
  label: "tbl:notation-register-table9-data",
  title: "Data table 9 from ",
  tags: ["extracted-table"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Lean conventions moved out of the table by the voice-leak drain (qou-d4kh, W14b): the generic base ring is a type variable `{R : Type*}` with the weakest typeclass that admits the construction (`[CommRing R]`, `[Field R]`, `[GroupWithZero R]`); `ℝ` is used only for declarations that need `Real.sqrt`, `Real.rpow`, `Real.cos`, `Real.exp`, `Real.log`, an ordering predicate, `linarith`, or a CODATA value (AGENTS.md §7c)." },
  ],
});
