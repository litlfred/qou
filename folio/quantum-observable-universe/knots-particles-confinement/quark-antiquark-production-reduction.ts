import { remark } from "../../schema/builders";

export default remark({
  label: "rem:quark-antiquark-production-reduction",
  interprets: "def:quark-antiquark-production",
  title: "Quark--antiquark production: step-by-step Hecke reduction",
  tags: [
    "quark",
    "antiquark",
    "pair-production",
    "hopf-link",
    "meson",
    "hecke-algebra",
    "colored-photon",
  ],
  uses: [
    "def:quark-antiquark-production",
    "def:breit-wheeler-pair-production",
    "def:up-quark",
    "def:down-quark",
    "def:categorical-meson",
    "conj:four-term-pair-nucleon",
    "prop:confinement-operator-selection",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict):  ([photon](#def:photon))" },
  ],
});
