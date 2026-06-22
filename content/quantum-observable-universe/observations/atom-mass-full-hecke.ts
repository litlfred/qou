import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:mass-comparison-table",
  label: "rem:atom-mass-full-hecke",
  title: "Atomic mass of $Z = 1$--$10$ via full three-channel Hecke algebra",
  tags: [
    "mass",
    "hecke-engine",
    "three-channel",
    "symmetric",
    "alternating",
    "standard",
    "wedderburn",
    "binding-energy",
    "skein-lagrangian",
  ],
  uses: [
    "rem:mass-comparison-table",
    "rem:hecke-charge-mass-duality",
    "prop:y-lambda-closed-form-wenzl-bridge",
  ],
  cites: [
    "jones1985",
    "kock2004",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-06-22",
      body: "The $\\mathrm{tr}_{\\mathrm{full}}$ / $B/A$ / $\\Delta$ columns of the data table are still computed with the $q\\to1$ classical Wedderburn weights $\\{1/6,2/3,1/6\\}$, not the canonical $q$-deformed Jones-Markov weights $\\hat y_\\lambda$ (`prop:y-lambda-closed-form-wenzl-bridge`, witness `y-lambda-at-q0.witness.json`), which differ by up to $\\sim7\\times$ per channel at the substrate. The prose now states the canonical convention and flags the table as the classical limit; a $q$-deformed regeneration of the per-atom table (channel traces + $\\mathrm{tr}_{\\mathrm{full}}$ + Skein binding) plus its own witness is the outstanding production step. The previously-cited `atom-mass-full-hecke.witness.json` never existed; the historical producer `computations/atom_mass_derived.py` carries a 'DO NOT TRUST OUTPUT' structural-bug banner.",
    },
  ],
});
