import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pre-archimedean-mass-gap",
  title: "Algebraic Witnesses for Faddeev Moments and the Pre-Archimedean Mass Gap",
  computation: {
    engine: "hecke-engine",
    script: "tools/hecke-engine/src/bin/faddeev_ck.rs",
    witness: "computations/qbeta/faddeev_ck_witness.lean",
    status: "verified",
  },
  tags: [
    "mass-gap",
    "pre-archimedean",
    "faddeev",
    "modular-double",
    "algebraic-witness",
    "q-beta",
  ],
  uses: [
    "prop:atom-knot-mass-derivation",
    "conj:mass-endomorphism",
  ],
  cites: [
    "faddeev1994",
    "kashaev1997",
  ],
  lean: {
    ref: "qou:QOU.QBeta.faddeev_ck_witness",
    validation: "checked",
  },
});
