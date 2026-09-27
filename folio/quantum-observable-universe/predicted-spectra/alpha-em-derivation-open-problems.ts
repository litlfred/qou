import { remark } from "../../schema/builders";

export default remark({
  label: "rem:alpha-em-derivation-open-problems",
  title:
    "Open problems: deriving the $1.55 \\times 10^{-3}$ correction to the bare $1/\\alpha_{EM} = q[9]_q[10]_q$",
  interprets: "prop:em-coupling-projection",
  uses: [
    "rem:em-coupling-chern-simons",
    "prop:em-coupling-bring-zero-mode",
    "rem:gram-kappa-spectral-interpretation",
  ],
  tags: [
    "alpha-em",
    "fine-structure",
    "open-problem",
    "derivation-roadmap",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "Items 1–2 of the earlier checklist are **resolved** by\n[`prop:photon-ir-zero-mode-bring`](#prop:photon-ir-zero-mode-bring): the\n\"3-manifold\" is the $2$-surface $M_{\\text{Bring}}$, and the photon zero-mode\ncoefficient $b_1/\\operatorname{Area} = 2g/(4\\pi(g-1)) = 2/(3\\pi)$ is proven\n(Lean `photonZeroModeShift_at_g4`, sorry-free). What remains:\n\n1. **Verify UV finiteness.** Reshetikhin–Turaev shadow-world regularisation\n should produce a finite answer (force-carrier complexity $[9]_q[10]_q$\n regularises the categorical sum, replacing the continuum momentum integral).\n2. **Compute the next-order self-energy** $\\alpha/(4\\pi)$ as a 2-loop graph\n (the $n=2$ jet order); the simplest closed forms $1/(4\\pi)$, $1/(2\\pi[2]_q)$\n are near-misses at $\\sim 0.4\\%$.\n\nThe numerical match at $5.7 \\times 10^{-8}$ is no coincidence; the leading\nmechanism is derived, with UV finiteness and the next-order term the open\nremainder.",
    },
  ],
});
