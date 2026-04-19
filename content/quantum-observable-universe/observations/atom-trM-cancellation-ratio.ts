import { remark } from "../../schema/builders";

export default remark({
  label: "rem:atom-trM-cancellation-ratio",
  title:
    "Atom Markov trace is a near-cancellation with ratio $\\sim B/(A \\cdot m_n c^2)$",
  interprets: "prop:atomic-braid-mass",
  uses: [
    "prop:atomic-braid-mass",
    "prop:mass-endomorphism-tower",
    "thm:jones-markov-trace",
  ],
  cites: ["leitner2026"],
  tags: ["mass-prediction", "cancellation-ratio", "binding-energy"],
});
