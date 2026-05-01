import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:algebraic-volume-specialization",
  title: "Specialisation of the algebraic quantum volume",
  uses: [
    "rem:kashaev-as-archimedean-realization",
    "def:algebraic-quantum-volume",
    "def:q-pochhammer-partial-product",
    "conj:shared-denominator-cusp-holonomy",
    "conj:algebraic-geometric-dilog-equivalence",
    "prop:sw-period-thimble-equivalence",
  ],
});
