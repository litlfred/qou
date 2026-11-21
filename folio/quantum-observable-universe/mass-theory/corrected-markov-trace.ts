import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:corrected-markov-trace",
  title:
    "Markov trace of $\\sigma_0\\sigma_1\\sigma_0$",
  tags: [
    "markov-trace",
    "correction",
    "hopf-link",
    "yang-baxter",
    "adjacent-generators",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.corrected_markov_trace" },
  cites: ["jones1987"],
  uses: [
    "thm:jones-markov-trace",
  ],
});
