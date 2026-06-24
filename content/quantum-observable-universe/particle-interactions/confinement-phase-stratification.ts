import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-phase-stratification",
  proofs: ["prf:confinement-phase-stratification"],
  title:
    "Confinement phases are open strata of the generic $q$-locus",
  lean: { ref: "qou:QOU.BraidKnot.ConfinementPhaseStratification",
    validation: "not_checked",
  },
  uses: [
    "prop:level-sufficiency",
    "prop:shell-closure-stability",
    "thm:parity-regime-selection",
    "rem:deconfinement-golden-threshold",
  ],
  tags: [
    "phase",
    "phase-boundary",
    "stratification",
    "open-set",
    "regime-switch",
    "deconfinement",
    "sdp-feasibility",
    "local-constancy",
  ],
});
