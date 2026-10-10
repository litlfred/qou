import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:dilog-pentagon-is-associator",
  title: "The pentagon coherence is equivalent to being a $q$-dilogarithm",
  lean: {
    ref: "qou:QOU.QuantumObservableUniverses.DilogPentagonAssociator.pentagon_iff_isDilog",
    validation: "not_checked",
  },
  uses: ["def:q-dilogarithm", "prop:q-dilogarithm-exists"],
  cites: ["faddeev_kashaev1994"],
  tags: ["dilogarithm", "pentagon-identity", "associator", "monoidal"],
});
