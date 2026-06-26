import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "While the mechanical process of $q$-deforming operators is a standard procedure, the mathematical novelty is observing that applying the exact $q$-derivative $D_q$ to classical Kelvin-wave dispersion immediately generates an exact, analytically rigorous doubly-exponential UV suppression mechanism ($\\tau_k \\sim q^{-2k}$) in the fluid bulk, bypassing the need for ad-hoc phenomenological regularization or arbitrary cutoffs." },
  ],
  label: "prop:kelvin-dispersion-derivation",
  lean: { ref: "qou:QOU.FluidDynamics.kelvin_dispersion_derivation", validation: "not_checked" },
  title: "Kelvin wave dispersion from the $q$-Laplacian eigenvalue problem",
  uses: ["def:q-navier-stokes"],
  tags: ["kelvin-wave", "dispersion", "q-laplacian", "eigenvalue", "derivation"],
});
