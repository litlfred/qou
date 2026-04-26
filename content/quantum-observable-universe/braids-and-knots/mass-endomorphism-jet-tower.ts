import { remark } from "../../schema/builders";

export default remark({
  label: "rem:mass-endomorphism-jet-tower",
  title: "Jet-brane reformulation of the mass tower",
  interprets: "prop:mass-endomorphism-tower",
  uses: [
    "prop:mass-endomorphism-tower",
    "def:recursive-brane-tower",
    "def:descent-involution",
    "prop:descent-eigenspaces",
    "thm:topological-mass",
    "rem:quantum-bloch-group",
    "thm:jones-markov-trace",
    "thm:markov-trace-factorization",
  ],
  tags: ["mass-tower", "jet-stratification", "audit"],
});
