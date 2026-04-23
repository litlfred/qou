import { remark } from "../../schema/builders";

export default remark({
  label: "rem:residual-conjecture-probe",
  title: "Probe of the residual conjecture: can (i) or (ii) be further reduced?",
  tags: ["ansatz", "hyperelliptic", "z5-residual", "probe", "reduction"],
  uses: [
    "conj:genus-2-ansatz",
    "thm:hyperelliptic-z5-classification",
    "def:commutative-qou",
    "prop:fiber-adjoint-involution",
    "def:brings-surface",
  ],
  interprets: "conj:genus-2-ansatz",
});
