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
    "prop:jet-tower-convergence",
    "prop:markov-pair-z2",
    "prop:pentagon-uv-commutation",
    "prop:descended-level-zero",
    "prop:delta-max-uniform-bound",
  ],
  tags: ["mass-tower", "jet-stratification", "audit"],
});
