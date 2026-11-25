import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:borromean-photon-factorisations",
  title: "Linking neutrality selects the photon factorisation of the Borromean core",
  lean: { ref: "qou:QOU.StandardModel.PhotonNeutralSelection.neutral_selects_corpus" },
  uses: ["def:photon", "prop:borromean-two-photon-factorisation"],
  cites: ["iwahori1964", "kassel2008"],
  tags: ["photon", "borromean", "gamma-gamma", "linking-neutrality", "hecke-algebra"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-25",
      body: "Lean: `QOU.PhotonNeutralSelection.neutral_selects_corpus` (sorry-free) in the concrete model of $H_3(q)$ (`QOU.HeckeH3Model`). Without the neutrality hypotheses the factorisation is not unique: over $\\mathbb{Q}(q)$ the solution set of $\\gamma(\\varphi)\\gamma(\\psi) = V^3$ has 8 points, the corpus pair plus the roots of a sextic that is irreducible over $\\mathbb{Q}(q)$ with Galois group $S_6$; 2 of the 6 are real at the proton $q_0$ (Singular, `computations/probes/photon_jet_spectral/singular/`, measured, not Lean). Owner ruling 2026-11-25 (`docs/coordination/owner-rulings.md`): linking neutrality is imposed term by term, with the scope of the 2026-11-21 ruling, so this proposition is the derivation of the photon weights. The ruling was made with the result already known; the corpus precedent `QEDHigherOrderCovariance` §P applies the colouring to the whole braid, under which the factorisations are not separated. Audit §11.2, §13.",
    },
  ],
});
