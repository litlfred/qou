import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:strangelet-witten-stability",
  label: "rem:strangelet-merger-signature",
  title:
    "Strangelet deconversion energy in neutron star mergers",
  tags: [
    "strangelet",
    "neutron-star",
    "merger",
    "kilonova",
    "gravitational-waves",
    "neutrino-burst",
    "phase-transition",
    "falsifiability",
  ],
  uses: [
    "rem:strangelet-witten-stability",
    "prop:eos-borromean-cfl",
    "rem:cfl-neutron-star-observables",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-21",
      body:
        "Owner rulings 2026-11-20 (option B of " +
        "`docs/audits/2026-11-20-up-quark-electron-knot-clash.md`) and " +
        "2026-11-21: a quark is an unknot strand of $\\mathcal{B}_3$; " +
        "$T_{2,5}^{\\sigma}$ and $T_{2,3}^{\\sigma}$ are the lepton partners of " +
        "$\\mathfrak{s}$ and $\\mathfrak{d}$, and their crossing counts are " +
        "generation labels. The quark identifications were reworded on " +
        "2026-11-21; the mathematics was not changed. The conversion energy " +
        "charges each quark the Jones value of its partner. That step assumes " +
        "the quark carries its partner's skein cost, which the ruling no longer " +
        "implies, so the estimate needs re-scoping in the same way as " +
        "`sec:strangelet-intro` (2026-11-20 note). The Jones values themselves " +
        "are unaffected.",
    },
  ],
});
