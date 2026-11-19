import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:cpt-orbit-closure-density",
  title:
    "CPT-saturation as Type-B fold-orbit closure: deriving $\\rho_F \\in \\{m_e, 2m_e\\}$ from crystal structure",
  lean: {
    ref: "qou:QOU.ParticleInteractions.cpt_orbit_closure_density",
    validation: "not_checked",
  },
  uses: [
    "rem:frobenius-packing-density",
    "conj:symmetric-crystal-pair-production",
  ],
  cites: [
    "kashiwara1991",
    "lecouvey2007",
    "brundankleshchev2009",
    "khovanovlauda2009",
    "kassel1995",
  ],
  tags: [
    "cpt",
    "type-b-fold",
    "orbit-closure",
    "frobenius-packing",
    "chirality",
    "wedderburn",
    "crystal-basis-shortcut",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
