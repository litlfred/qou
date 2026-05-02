import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:algebraic-primality-equals-empirical-at-q0",
  title:
    "Proposition 7. Algebraic primality at $q_0$ equals the empirical magic ladder",
  lean: {
    ref: "qou:QOU.Interactions.AlgebraicPrimality.MagicEqualsEmpirical",
    validation: "not_checked",
  },
  uses: [
    "def:algebraic-primality",
    "prop:n-equals-1-vacuous-magic",
    "conj:homological-shell-condensation",
    "prop:magic-numbers-from-q",
  ],
  cites: [
    "mathas1999",
    "kassel1995",
  ],
  tags: [
    "magic-numbers",
    "primality",
    "empirical-match",
    "q0",
    "open-problem",
    "axiom-class",
  ],
});
