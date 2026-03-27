import { example } from "../../schema/builders";

export default example({
  label: "ex:nitrogen-14-threading",
  title:
    "The ${}^{14}\\mathrm{N}$ maximal braid shortcut vs ${}^{14}\\mathrm{C}$ broken alternation",
  tags: [
    "nitrogen-14",
    "carbon-14",
    "braid-word",
    "threading",
    "alternation",
    "pauli-cost",
    "coulomb",
    "beta-decay",
  ],
  uses: [
    "prop:nuclear-groebner-reduction",
    "thm:markov-trace-factorization",
    "prop:generator-volume-decomposition",
    "def:stable-nucleus",
    "prop:hadron-half-life",
    "prop:beta-stability",
  ],
});
