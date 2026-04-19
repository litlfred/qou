import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-phase-stratification",
  title:
    "Confinement phases are open strata of the generic $q$-locus",
  lean: {
    decl: "QOU.BraidKnot.ConfinementPhaseStratification",
    validation: "not_checked",
  },
  uses: [
    "def:confined-particle",
    "def:confinement-category",
    "prop:confinement-sdp",
    "prop:confinement-topological",
    "prop:level-sufficiency",
    "prop:shell-closure-stability",
    "prop:parity-regime-selection",
    "def:deconfinement-golden-threshold",
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
