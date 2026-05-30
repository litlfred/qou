import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:cpt-d6-d7-d8-closure",
  title:
    "CPT closure: D6 + D7 + D8 jointly imply $C \\cdot P \\cdot T$ preserves the Markov trace",
  lean: {
    ref: "qou:QOU.ParticleInteractions.CPTD6D7D8Closure",
    validation: "not_checked",
  },
  uses: [
    "prop:cpt-orbit-closure-density",
    "def:bar-involution",
  ],
  cites: [
    "wigner1937",
    "jones1987",
    "kassel1995",
  ],
  tags: [
    "cpt-closure",
    "discrete-symmetry",
    "compound-conjecture",
    "duality-d6-d7-d8",
    "markov-trace",
    "open-problem",
  ],
});
