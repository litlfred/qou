import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:dilogarithm-archimedean-limit",
  title:
    "$(1{-}q)\\,\\log\\Phi_n(x; q) \\to \\mathrm{Li}_2(x)$ under $\\tau_{\\mathrm{arch}}$",
  lean: {
    ref: "qou:QOU.QPochhammer.ArchimedeanLimit",
    validation: "not_checked",
  },
  uses: [
    "def:q-pochhammer-partial-product",
    "cor:quantum-dilogarithm",
    "def:archimedean-realization-functor",
    "rem:kashaev-as-archimedean-realization",
  ],
  cites: ["faddeev1994", "kashaev1997", "zagier1986"],
  tags: [
    "tier:keystone",
    "q-pochhammer",
    "dilogarithm",
    "bloch-wigner",
    "archimedean",
    "saddle-point",
    "open-problem",
  ],
});
