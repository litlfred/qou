import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:algebraic-volume-specialization",
  title: "Specialisation of the algebraic quantum volume",
  // The previous `uses[]` listing of
  // `conj:shared-denominator-cusp-holonomy` and
  // `conj:algebraic-geometric-dilog-equivalence` was wrong-direction:
  // the proposition's algebraic content (routes 1–4 of
  // specialisation) is a routine derivation from
  // `def:algebraic-quantum-volume`; the conjectures *interpret* the
  // resulting denominator structure / Kashaev limit downstream of
  // the proposition. See `docs/audits/conjecture-cones.md`
  // "Methodology" footnote (case (2) cleanup). The conjecture
  // references remain as prose citations in the .md.
  uses: [
    "rem:kashaev-as-archimedean-realization",
    "def:algebraic-quantum-volume",
    "def:q-pochhammer-partial-product",
    "prop:sw-period-thimble-equivalence",
  ],
});
