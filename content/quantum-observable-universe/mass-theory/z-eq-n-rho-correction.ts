import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:z-eq-n-rho-correction",
  title:
    "Z=N substrate-q correction to the Kashaev law: $B = m_e \\cdot \\mathrm{Vol}_{\\rm hyp}(K_A) \\cdot (\\rho_{\\rm struct} + A - [A]_q)$",
  lean: {
    ref: "qou:QOU.BraidKnot.ZeqNRhoCorrection",
    validation: "not_checked",
  },
  uses: [
    "prop:kashaev-volume-conjecture",
    "def:substrate-parameter",
  ],
  cites: [],
  tags: [
    "binding-energy",
    "kashaev",
    "z-equals-n",
    "q-deformation",
    "rho-substrate",
    "1ppb",
    "open-problem",
  ],
});
