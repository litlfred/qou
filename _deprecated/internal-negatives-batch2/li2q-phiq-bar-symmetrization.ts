import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:li2q-phiq-bar-symmetrization",
  title:
    "Symmetric q-dilogarithm as bar-symmetrization of Faddeev",
  lean: {
    ref: "qou:QOU.BraidKnot.Li2qPhiqBarSymmetrization",
    validation: "not_checked",
  },
  uses: [
    "def:q-dilogarithm",
    "def:archimedean-realization-functor",
    "rem:pre-tau-vs-post-tau",
    "prop:full-pole-structure-mass-trace",
  ],
  cites: ["faddeev1995", "kashaev1997", "andersenKashaev2014"],
  computation: {
    engine: "python",
    script:
      "computations/m_p_m_e_li2q.py",
    witness:
      "computations/m-p-m-e-li2q.witness.json",
    status: "verified",
  },
  tags: [
    "q-dilogarithm",
    "faddeev",
    "bar-involution",
    "archimedean-wall",
    "volume-conjecture",
    "non-perturbative",
  ],
});
