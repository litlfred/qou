import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:centered-hecke-variance-positive",
  title:
    "Centred Hecke transfer matrix has strictly positive variance in the Wenzl regime",
  lean: { ref: "qou:QOU.Observations.centered_hecke_variance_positive", validation: "not_checked" },
  uses: [
    "thm:jones-markov-trace",
    "rem:non-commutative-probability-dictionary",
  ],
  tags: [
    "q-clt",
    "variance",
    "wenzl-positivity",
    "established",
  ],
  proofs: ["prf:centered-hecke-variance-positive"],
  authorNotes: [
    {
      kind: "status",
      body: "**Provable arithmetic.** The proof in `prf:centered-hecke-variance-positive` is direct algebra plus the inequality $(q^{1/2}+q^{-1/2})^2 > 4$ ⟹ Wenzl regime ⟹ variance positive.",
    },
  ],
});
