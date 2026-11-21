import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-dilogarithm",
  label: "rem:q-dilogarithm-pentagon-associator",
  title: "The $q$-dilogarithm pentagon as the monoidal associator axiom",
  tags: ["dilogarithm", "pentagon-identity", "associator", "monoidal"],
  uses: [
    "def:q-dilogarithm",
    "prop:phi-q-aj-machinery-identification",
    "prop:dilog-pentagon-is-associator",
  ],
  cites: ["faddeev_kashaev1994", "faddeev-kashaev-volkov2000", "baseilhac-benedetti-fibred", "terashima-yamazaki2013"],
  authorNotes: [
    { kind: "status", date: "2026-10-11", body: "Relocated from the block prose by the paper-voice commentary audit: the two links (categorical → scalar descent; analytic q ≠ 1 five-term) are not formalised; the Faddeev–Kashaev identification is cited rather than machine-checked, and the analytic relation is a conjecture class." },
  ],
});
