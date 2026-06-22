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
      body: "The $\\mathrm{tr}_{\\mathrm{full}}$ column now uses the canonical $q$-deformed Jones-Markov weights $\\hat y_\\lambda$ (`prop:y-lambda-closed-form-wenzl-bridge`), recomputed by `computations/atom_mass_full_hecke_qdeformed.py` → `atom-mass-full-hecke.witness.json` (the previously-cited witness never existed). This replaced the classical $\\{1/6,2/3,1/6\\}$ weighting, which differs by up to $\\sim7\\times$ per channel and had flipped the signs of $^7$Li/$^{11}$B/$^{19}$F and faked the $^{14}$N cancellation. Residual open item: the per-channel traces are inherited from the published table — the high-$A$ $\\chi^\\lambda$ are not independently witnessed (GS reducer infeasible past light nuclei; e.g. $^{20}$Ne = H_60). $B/A$/$\\Delta$ are weight-independent (Bethe-Weizsäcker). Historical producer `computations/atom_mass_derived.py` carries a 'DO NOT TRUST OUTPUT' banner.",
    },
  ],
});
