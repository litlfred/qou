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
      body: "The $\\mathrm{tr}_{\\mathrm{full}}$ column now uses the canonical $q$-deformed Jones-Markov weights $\\hat y_\\lambda$ (`prop:y-lambda-closed-form-wenzl-bridge`), recomputed by `computations/atom_mass_full_hecke_qdeformed.py` → `atom-mass-full-hecke.witness.json` (the previously-cited witness never existed). This replaced the classical $\\{1/6,2/3,1/6\\}$ weighting, which differs by up to $\\sim7\\times$ per channel and had flipped the signs of $^7$Li/$^{11}$B/$^{19}$F and faked the $^{14}$N cancellation. $B/A$/$\\Delta$ are weight-independent (Bethe-Weizsäcker). Historical producer `computations/atom_mass_derived.py` carries a 'DO NOT TRUST OUTPUT' banner.",
    },
    {
      kind: "caveat",
      date: "2026-06-22",
      body: "Model scope (residual open item). The per-atom three-channel traces $\\mathrm{tr}_{\\mathrm{sym/std/alt}}$ are inherited and are a per-atom **H_3 projection model** — exact only at $A=1$. For $A>1$ this is distinct from the full $H_{3A}$ Markov trace: an independent canonical $^4$He computation (`atomic-tr-m-helium4.witness.json`, $|\\mathrm{tr}_M|=0.967$) does not coincide with the three-channel value here ($0.516$ $q$-deformed), and corpus $^4$He trace conventions (disjoint-product $0.967$, all-nuclides-v2 $\\sim1.12$, 3-channel $0.516$) do not agree. A trustworthy per-atom recompute is therefore blocked by both the GS-reducer wall ($A\\ge5$) and convention reconciliation ($A\\ge2$); the columns should be read as a specific three-channel projection, not the canonical $H_{3A}$ trace. General-n three-row Ocneanu weight vanishing: `QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows`.",
    },
  ],
});
