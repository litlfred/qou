import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:im-q-physical-role",
  label: "rem:ohtsuki-tower-bar-parity",
  title:
    "Bar-parity of the Ohtsuki tower at the imaginary substrate: even rungs are $\\mathrm{Re}\\,\\mathfrak{V}$ (mass), odd rungs are $\\mathrm{Im}\\,\\mathfrak{V}$ (the bar-odd $S$)",
  uses: ["conj:im-q-physical-role", "rem:c3-s-imq-decay-projection"],
  cites: ["andersen-mistegard2020"],
  tags: [
    "im-q",
    "ohtsuki-tower",
    "complex-volume",
    "bar-parity",
    "c3-bar-odd",
    "q-beta",
    "candidate-iii",
    "deuteron-binding",
    "wedderburn-conjugation",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Both statements are proved over $\\mathbb{C}$ in the Lean file `OhtsukiTowerBarParity.lean` ... the resummation is recorded in [`qbeta_c3_borel_pade_resummation_probe.py`](../../../computations/qbeta/qbeta_c3_borel_pade_resummation_probe.py) ... The parity backbone is proved over a generic commutative ring in [`ConjugationParitySplit.lean`](../../../folio/quantum-observable-universe/lean/QOU/MassTheory/ConjugationParitySplit.lean)" },
  ],
});
