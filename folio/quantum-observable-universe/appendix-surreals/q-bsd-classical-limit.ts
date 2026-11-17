import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-bsd-classical-limit",
  title:
    "$q$-BSD across $\\mathbb{P}^1$, the Kummer obstruction, and the classical limit",
  interprets: "conj:q-birch-swinnerton-dyer",
  uses: [
    "def:categorical-mordell-weil",
    "prop:root-of-unity-truncation",
    "prop:ns-kummer-specialisation",
    "rem:substrate-gm-torsion",
  ],
  tags: [
    "birch-swinnerton-dyer",
    "millennium-problem",
    "kummer",
    "gm-torsion",
    "projective-line",
    "classical-limit",
    "l-function",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-17",
      body:
        "**RESOLVED 2026-11-17 — the integer is chi_eu.** The block wrote `tr(kappa_0) = chi(A) = -6` for the Euler class. The integral of the Euler class of the unit tangent bundle is `chi_eu(M_0)` (Poincare-Hopf); it is not a trace of `A`. Now written `kappa_0[M_0] = chi_eu(M_0) = -6`, with the unit-tangent-bundle hypothesis cited from `prop:ns-kummer-specialisation`. Bean `qou-qhcr`, PR #8365.",
    },
  ],
});
