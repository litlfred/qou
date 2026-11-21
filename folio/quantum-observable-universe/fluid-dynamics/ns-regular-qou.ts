import { definition } from "../../schema/builders";

export default definition({
  label: "def:ns-regular-qou",
  title: "NS-regular quantum observable universe",
  // Was `qou:QOU.FluidDynamics.NSRegularQOU`. Neither that namespace nor that
  // declaration exists anywhere in the tree, and the canonical resolver returns
  // unresolved for it. `QOU.GaugeFieldFluidDynamics.BoundaryObservability`
  // carries this block's own `\label{def:ns-regular-qou}` — the label is the
  // evidence, the ref's name was not. Same repair as `thm:su2-emergence`
  // (PR #5222) and `def:mass-identity` (bean `qou-qc6s`).
  //
  // Why nothing caught this: the block has a co-located sibling
  // `ns-regular-qou.lean`, and `walkBlocks` resolves the sibling FIRST. So the
  // checkers audited the stub and passed, while the library ref sat dead and
  // the real declaration went unchecked. A sibling stub MASKS a broken library
  // ref — see bean `qou-2u26`.
  lean: {
    ref: "qou:QOU.GaugeFieldFluidDynamics.BoundaryObservability",
    validation: "not_checked",
  },
  uses: ["def:q-navier-stokes"],
  tags: [
    "definition",
    "navier-stokes",
    "obstruction",
    "euler-characteristic",
    "categorical",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The global-surface definition $\\deg e(\\xi) = \\chi(A)$ is (matching `QOU.FluidDynamics.qou_ns_in_qou`)." },
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Restated by owner decision (Q-VO9T-2 = 1, beans qou-nzyr and qou-hjl0): " +
        "NS(A) is redefined from the degenerate curve restriction $\\kappa_0|_\\Sigma \\in H^2(\\Sigma, \\mathcal{B}) = 0$ " +
        "to the global surface Euler class $e(\\xi) \\in H^2(\\mathcal{S}, \\mathbb{Z}) \\cong \\mathbb{Z}$ of degree $\\chi(A)$ " +
        "(matching `QOU.FluidDynamics.qou_ns_in_qou` and item 1 of `thm:ns-singularity-descartes`). " +
        "This restores the non-degenerate categorical dichotomy ($\\mathrm{NS}(A) = 0 \\iff \\chi(A) = 0$), " +
        "while explicitly scoping the bridge to classical 3D unforced Navier–Stokes as a framework model " +
        "correspondence rather than a deductive PDE equivalence (citing Tao's averaged-NS barrier, " +
        "J. Amer. Math. Soc. 29 (2016), 601–674, and the $q \\to 1$ Euler vs fixed-$\\hbar_q$ NS scaling distinction; " +
        "audit `docs/audits/2026-10-12-ns-v3-tao-barrier.md`).",
      see: "../../../../docs/audits/2026-10-12-ns-v3-tao-barrier.md",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Descartes theorem](#thm:ns-singularity-descartes), item 3)" },
  ],
});
