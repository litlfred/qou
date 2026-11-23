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
    "conj:four-term-pair-nucleon",
    "def:photon",
    "prop:borromean-two-photon-factorisation",
    "prop:gamma-gamma-generates-particles",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Moved out of the prose by the voice-leak drain (qou-d4kh, W14b, 2026-11-21): coefficients recomputed exactly over Q(q) in `computations/probes/photon_chiral/photon_chiral_ports_probe.py`; witness `computations/probes/photon_chiral/photon-chiral-ports.witness.json`. The earlier citation `breit-wheeler-nucleon-nf.witness.json` does not exist in the repository." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Witness:** `breit-wheeler-nucleon-nf.witness.json`" },
    {
      kind: "refined-framing",
      date: "2026-11-20",
      body:
        "**Photon restated on def:photon (owner ruling, bean `qou-99qc`, 2026-11-18, confirmed 2026-11-20).** " +
        "The photon's fourth term is the chiral vertex σ₀σ₁⁻¹. The bare photon is 𝟏, so the bare pair is 𝟏, not " +
        "σ₀² (photon-usage audit 2026-11-17, C2). The three-term specialisation and its fitted weights are " +
        "unchanged, because φ₀₁ = 0 gives the same element in both forms. Exact recomputation: " +
        "computations/probes/photon_chiral (PR #8595).",
    },
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
