import { definition, proposition, remark } from "../../schema/builders";

/**
 * Atomic braid definition: electrons in the nuclear braid.
 */
export const atomicBraid = definition({
  label: "def:atomic-braid",
  title: "Atomic braid $H_{A+Z}(q)$",
  lean: {
    decl: "QOU.AtomicBraid.NeutralAtom",
    validation: "not_checked",
  },
  uses: ["def:transfer-matrix-operator", "def:derived-atom"],
});

/**
 * LP stability criterion for atoms.
 */
export const lpStability = proposition({
  label: "prop:atomic-lp-stability",
  title: "LP stability of the atomic braid",
  uses: ["def:atomic-braid", "def:borromean-baryon"],
});

/**
 * Complete Wedderburn mass formula.
 */
export const wederburnMass = proposition({
  label: "prop:wedderburn-mass-formula",
  title: "Three-invariant mass formula",
  uses: ["def:atomic-braid", "prop:atomic-lp-stability"],
});

/**
 * Neutron-proton mass splitting from quark crossing change.
 */
export const neutronProtonSplitting = proposition({
  label: "prop:neutron-proton-splitting",
  title: "Neutron--proton mass splitting",
  uses: ["def:atomic-braid", "prop:wedderburn-mass-formula"],
});

/**
 * Photon color content and degree-2 binding.
 */
export const colorPairing = remark({
  label: "rem:color-pairing-binding",
  title: "Degree-2 color pairing as binding energy",
  interprets: "prop:wedderburn-mass-formula",
  uses: ["def:color-tube-coordinates"],
});

/**
 * Mass comparison table Z = 1–20.
 */
export const massTable = remark({
  label: "rem:mass-table-z1-20",
  title: "Predicted vs observed masses, $Z = 1$--$20$",
  interprets: "prop:wedderburn-mass-formula",
});
