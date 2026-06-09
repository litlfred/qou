import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:metallic-cascade-collapse",
  title:
    "Collapse cascade across the metallic ladder and the delayed second neutrino burst",
  tags: [
    "tier:E",
    "metallic-ratio",
    "supernova",
    "core-collapse",
    "second-neutrino-burst",
    "cfl-transition",
    "neutron-star",
    "falsifiable",
  ],
  uses: [
    "conj:color-superconductivity-borromean",
    "prop:borromean-hopf-energy-crossover",
    "rem:cfl-neutron-star-observables",
  ],
  cites: [
    "sagert2009",
    "dasgupta2010",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-06-09",
      body:
        "Added on PR #2081 (owner-directed, both-branch framing). " +
        "Quantitative inputs: silver latent heat 21.5 MeV/baryon " +
        "(`metallic-cascade-collapse-energy.witness.json`), q↔ρ " +
        "placements (`metallic-q-rho-calibration.witness.json`), " +
        "hyperon-anchored chain " +
        "(`metallic-phi-rung-hyperon-onset.witness.json`).  Lean " +
        "class axiomatization (§3b pattern) deferred until a " +
        "placement is selected by data or owner direction.",
    },
  ],
});
