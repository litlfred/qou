import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:q-heat-kernel-peter-weyl",
  label: "rem:q-heat-kernel-peter-weyl-interpretation",
  title:
    "Convergence, the $q$-Gaussian equilibrium mode, and the place in the $q$-heat story",
  uses: [
    "prop:q-heat-kernel-peter-weyl",
    "prop:q-gaussian-solves-q-heat",
    "def:categorical-laplace",
    "def:q-dilogarithm",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): is the convergence conjecture `qHeatKernelPeterWeyl`; it is not proved." },
  ],
});
