import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-zero-stokes-region-identification",
  title:
    "Aether $q_0$ identification via Stokes region of the generating function (over $\\mathbb{Z}[q, q^{-1}]$)",
  lean: {
    ref: "qou:QOU.BraidKnot.QZeroStokesRegionIdentification.QZeroStokesIdentification",
    validation: "not_checked",
  },
  uses: ["prop:phi-q-aj-machinery-identification", "rem:dilog-saddle-regime"],
  cites: [
    "mostow1968",
    "prasad1973",
    "reid1990",
    "garoufalidis2004",
    "faddeev1995",
    "kashaev1997",
    "murakami-murakami2001",
    "champanerkar2003",
  ],
  tags: [
    "tier:S",
    "q-zero-identification",
    "stokes-region",
    "generating-function",
    "z-q-q-inverse-universal",
    "minimal-archimedean",
    "100-percent-proved-track",
    "conditional-class-3b-cond",
  ],
});
