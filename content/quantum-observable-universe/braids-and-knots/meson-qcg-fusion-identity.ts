import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "The q-Clebsch-Gordan fusion $[3]_q[4]_q=[2]_q+[4]_q+[6]_q$ is standard q-representation theory. The novel, framework-specific mathematical insight is its application to the 2-body meson $m_K^2/m_\\pi^2$ squared-ratio (as opposed to a 1-body character)." },
  ],
  label: "prop:meson-qcg-fusion-identity",
  title:
    "q-Clebsch–Gordan fusion identity $[3]_q\\cdot[4]_q = [2]_q + [4]_q + [6]_q$",
  lean: {
    ref: "qou:QOU.BraidKnot.meson_qCG_3x4",
  },
  uses: [],
  cites: [
    "kassel1995",
    "jones1987",
  ],
  tags: [
    "hecke-algebra",
    "clebsch-gordan",
    "meson",
    "fusion-product",
    "categorical-derivation",
  ],
});
