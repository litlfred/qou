import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:categorical-proton",
  label: "rem:meson-to-proton-via-borromean",
  title:
    "Proton formation: three pair productions and the energy scale $\\mathbf{E}_0$",
  tags: [
    "proton",
    "baryon-number",
    "borromean",
    "energy-scale",
    "typed-crossings",
    "beta-decay",
    "formation-chain",
    "hecke-algebra",
    "computational-witness",
    "pair-production",
  ],
  uses: ["rem:energy-scale-planck"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Witness: `meson-nucleon-nf.witness.json`,\n`beta-decay-energy-scale.witness.json`,\n`confinement-operator-selection.witness.json`." },
  ],
});
