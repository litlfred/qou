import { remark } from "../../schema/builders";

export default remark({
  label: "rem:isospin-mass-split-em-localisation",
  title: "Mirror-isobar mass split lives outside the spin-/sign-invariant sector",
  interprets: "prop:crystal-isospin-degeneracy",
  uses: ["prop:crystal-isospin-degeneracy"],
  tags: [
    "isospin",
    "tritium",
    "helium-3",
    "mass-split",
    "coulomb",
    "electromagnetic",
    "localisation",
    "structural-impossibility",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): (see the scope note in [Neutron--proton mass splitting from quark crossing change](#prop:neutron-proton-mass-splitting))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): (see the scope note in [Neutron--proton mass splitting from quark crossing change](#prop:neutron-proton-mass-splitting))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ([`frobenius-s-classification`](frobenius-s-classification.md), `mass_S_difference`); the Lean files above carry explicit, sorry-free operators for both non-invariant pieces. ... (see the scope note in `prop:neutron-proton-mass-splitting`); (`BextGPMT q 3 = -dMod111 q > 0`, ...; `gpmt_threeRow_cumulant_signs`)" },
  ],
});
