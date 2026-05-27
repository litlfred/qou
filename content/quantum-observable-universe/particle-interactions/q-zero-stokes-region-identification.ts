import { conjecture } from "../../schema/builders";

export default proposition({
  label: "prop:q-zero-stokes-region-identification",
  title:
    "Substrate $q_0$ identification via Stokes region of the generating function (over $\\mathbb{Z}[q, q^{-1}]$)",
  lean: {
    ref: "qou:QOU.BraidKnot.QZeroStokesRegionIdentification",
    validation: "not_checked",
  },
  uses: [
    "def:borromean-baryon",
    "def:quantum-planck-constant",
    "prop:phi-q-aj-machinery-identification",
    // broken-ref removed (Phase 7): conj:q-zero-complex-extension
    "prop:quantum-langlands-dual",
  ],
  cites: [
    "mostow1968",
    "prasad1973",
    "reid1990",
    "garoufalidis2004",
    "faddeev1995",
    "kashaev1997",
    "murakami-murakami2001",
    "champanerkar-kofman-mullen2008",
  ],
  tags: [
    "q-zero-identification",
    "stokes-region",
    "generating-function",
    "z-q-q-inverse-universal",
    "minimal-archimedean",
    "100-percent-proved-track",
    "conditional-class-3b-cond",
  ],
});
