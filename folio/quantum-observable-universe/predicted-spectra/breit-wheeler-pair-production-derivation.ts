import { remark } from "../../schema/builders";

export default remark({
  label: "rem:breit-wheeler-pair-production-derivation",
  interprets: "def:breit-wheeler-pair-production",
  title:
    "Color-dressed photon, polarization models, and the $4$-term Breit--Wheeler normal form",
  tags: [
    "breit-wheeler",
    "pair-production",
    "photon",
    "electron",
    "positron",
    "hecke-algebra",
    "colored-photon",
    "normal-form",
  ],
  uses: [
    "def:breit-wheeler-pair-production",
    "rem:knot-basis-color-content",
    "rem:physics-names-knot-operations",
    "prop:four-term-pair-nucleon",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Witness:** `breit-wheeler-nucleon-nf.witness.json`" },
    {
      kind: "caveat",
      date: "2026-11-15",
      body:
        "**Fit labelled (owner H2, bean `qou-ccst`, PR #7825).** The values φ = 0.0487 and s = 0.0978 are " +
        "obtained by setting E_pair = 2m_e, i.e. fitted to the electron mass. The text now says so, and no " +
        "longer presents closing the 1.6 % gap as evidence.",
    },
  ],
});
