import { proposition } from "../../schema/builders";

/**
 * The QOU mass formula as a categorical descent decomposition:
 * descended (central) + transient (exceptional divisor)
 * components.
 *
 * History: renamed from `prop:mass-categorical-descent` on 2026-05-18
 * to align with the QOU six-term-mass-formula production framework
 * (the BW naming framed the same descent decomposition around the
 * empirical Bethe-Weizsäcker formula; the structural content is
 * mass-formula-agnostic and recovers BW as one phenomenology).
 */
export default proposition({
  label: "prop:mass-categorical-descent",
  proofs: ["prf:mass-categorical-descent"],
  title:
    "QOU mass formula as descent decomposition of the mass endomorphism",
  tags: [
    "mass",
    "mass-formula",
    "descent-decomposition",
    "exceptional-divisor",
    "casimir",
    "wedderburn",
    "quantum-dilogarithm",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.mass_categorical_descent",
    validation: "not_checked",
  },
  uses: ["thm:wedderburn-mass-formula"],
});
