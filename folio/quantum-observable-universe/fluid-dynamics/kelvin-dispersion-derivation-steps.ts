import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:kelvin-dispersion-derivation",
  label: "rem:kelvin-dispersion-derivation-steps",
  title: "Derivation of the Kelvin dispersion from the $q$-Laplacian eigenvalue problem",
  uses: ["prop:kelvin-dispersion-derivation", "def:q-navier-stokes"],
  tags: ["kelvin-wave", "dispersion", "q-laplacian", "eigenvalue", "derivation"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-15",
      body: "An earlier version wrote mu_k^(q) = (2*pi*[k]_q / L_q)^2 with L_q = L, disagreeing with the dimensional restoration by 4*pi^2 / hbar_q (issue #8053).",
    },
  ],
});
