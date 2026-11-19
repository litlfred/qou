import { proof } from "../../schema/builders";

export default proof({
  label: "prf:algebraic-gns-embedding",
  title: "Proof of the Markov-trace GNS embedding",
  uses: ["prop:algebraic-gns-embedding"],
  authorNotes: [
    {
      kind: "status",
      body: "Closed-form Convention-D Ocneanu positivity and 3-row vanishing proved in `QOU.SchurWeyl.ocneanuWeight_conventionD_pos_of_two_rows` and `ocneanuWeight_conventionD_eq_zero_of_three_rows` (Markov weight identification proved in Lean at n = 3 and checked numerically through n = 6).",
    },
  ],
});
