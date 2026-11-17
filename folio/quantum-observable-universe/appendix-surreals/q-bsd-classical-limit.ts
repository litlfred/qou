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
        "**OPEN — trace identity.** The block writes `tr(kappa_0) = chi(A) = -6` for the Euler class `kappa_0 = e(xi)`. The integral of the Euler class is `chi_eu(M_0)`; reading it as a trace of `A` identifies two different objects. Under the owner ruling of 2026-09-15, `tr(id_A) = dim_q(A)` is a q-dependent quantum dimension, and `-6` is `chi_eu(M_0)`, the topological Euler characteristic of the base curve (`rem:three-euler-characteristics`). Flagged open on owner instruction 2026-11-17 (Bring foundations cleanup); the bare `chi(A)` here was not renamed because the step uses a trace identity, not only the genus. Bean `qou-qhcr`.",
    },
  ],
});
