import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:frobenius-antipode-unifies-chirality-and-tower",
  label: "rem:frobenius-antipode-neutron-tower-closure",
  title:
    "Frobenius-antipode symmetrization closes the neutron tower",
  uses: [
    "conj:frobenius-antipode-unifies-chirality-and-tower",
    "conj:six-term-mass-formula-complete",
  ],
  cites: ["kassel1995"],
  tags: [
    "frobenius",
    "antipode",
    "neutron-tower",
    "alpha-blend",
    "catalan",
    "determinant-invariant",
  ],
});
