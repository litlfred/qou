import { proposition } from "../../schema/builders";

/**
 * The Bethe-Weizsäcker mass formula as a categorical descent
 * decomposition: descended (central) + transient (exceptional divisor)
 * components.
 */
export default proposition({
  label: "prop:bw-categorical-descent",
  title:
    "Bethe-Weizsäcker formula as descent decomposition of the mass endomorphism",
  tags: [
    "mass",
    "bethe-weizsaecker",
    "descent-decomposition",
    "exceptional-divisor",
    "casimir",
    "wedderburn",
    "quantum-dilogarithm",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.bw_categorical_descent",
    validation: "not_checked",
  },
  uses: ["thm:wedderburn-mass-formula"],
});
