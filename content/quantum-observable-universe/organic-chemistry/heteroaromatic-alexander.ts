import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:heteroaromatic-alexander",
  title:
    "Heteroaromatic Alexander invariance under heteroatom substitution",
  tags: [
    "heteroaromatic",
    "pyridine",
    "furan",
    "thiophene",
    "pyrrole",
    "alexander-polynomial",
    "topological-invariance",
    "conjecture",
  ],
  lean: { ref: "qou:QOU.Organic.heteroaromaticAlexander",
    validation: "not_checked",
  },
  uses: [
    "lem:alexander-T2N-closed-form",
    "def:torus-knot-T2-odd-alexander",
  ],
  cites: [],
});
