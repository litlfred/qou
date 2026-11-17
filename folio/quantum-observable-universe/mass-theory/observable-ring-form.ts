import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:observable-ring-form",
  title:
    "Every observable is a $q_0$-element times a monomial in the dimensional proxies $m_e$, $m_\\pi$",
  uses: ["prop:three-calibration-inputs"],
  tags: ["calibration", "predictive-content", "ring-form"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-16",
      body:
        "Split out of `prop:three-calibration-inputs` on owner ruling (decision card, 2026-11-16, \"narrow to the count of three\"). The proposition now keeps only the count of three inputs, which its proof argues. This ring-form claim was never proved there, and the ring stated there, $\\mathbb{Z}[q_0^{\\pm 1/2}]$, is contradicted by the block's own $\\mathfrak{E}_0 = m_e/(q_0(q_0-1))$, since $1/(q_0-1) \\notin \\mathbb{Z}[q^{\\pm 1/2}]$.",
    },
  ],
});
