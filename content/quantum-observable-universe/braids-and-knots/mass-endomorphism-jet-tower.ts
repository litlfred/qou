import { remark } from "../../schema/builders";

export const massEndomorphismJetTower = remark({
  label: "rem:mass-endomorphism-jet-tower",
  title: "Jet-brane reformulation of the mass tower",
  interprets: "prop:mass-endomorphism-tower",
  uses: [
    "prop:mass-endomorphism-tower",
    "def:recursive-brane-tower",
    "def:descent-involution",
    "def:quantum-bloch-group",
    "thm:jones-markov-trace",
  ],
  tags: ["mass-tower", "jet-stratification", "audit"],
});
