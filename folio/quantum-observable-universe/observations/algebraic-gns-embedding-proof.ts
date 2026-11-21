import { proof } from "../../schema/builders";

export default proof({
  label: "prf:algebraic-gns-embedding",
  title: "Proof of the Markov-trace GNS embedding",
  uses: ["prop:algebraic-gns-embedding"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean lemma `QOU.SchurWeyl.ocneanuWeight_conventionD_pos_of_two_rows` proves that the closed-form convention-D Ocneanu weight is strictly positive on every shape with at most two rows, for $q > 0$, $q \\neq 1$. The companion `ocneanuWeight_conventionD_eq_zero_of_three_rows` proves it is zero on the rest. That this closed form is the Markov weight at general $n$ is the classical Ocneanu–Wenzl formula; in the corpus it is proved in Lean at $n = 3$ and checked numerically through $n = 6$, so the Lean lemma supports the cited result and does not replace it." },
  ],
});
