import { example } from "../../schema/builders";

export default example({
  interprets: "def:chern-character",
  label: "ex:su2-characters-and-quantum-dimension",
  title: "$\\mathrm{SU}(2)$ characters, and the quantum dimension as one evaluation of them",
  lean: { ref: "qou:QOU.Examples.su2Character", validation: "not_checked" },
  tags: ["su2", "character", "quantum-dimension", "chern-character", "grothendieck-group"],
  uses: [
    "def:chern-character",
    "def:grothendieck-group-of-a-qou",
    "ex:quantum-universe-su2",
  ],
  foreshadows: ["rem:euler-characteristic-of-the-regular-representation"],
  cites: ["fulton-harris1991", "kassel1995"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "Lean names moved out of the prose (voice drain, epic `qou-d4kh`): the three identities are `su2Character_one`, `su2Character_mul_q_sub` and `su2Character_fundamental`.",
    },
  ],
});
