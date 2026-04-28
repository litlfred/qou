import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:huckel-from-T2N-invariant",
  title:
    "Hückel $4n+2$ rule from $T(2,N)$ component count and weight parity",
  tags: [
    "huckel",
    "4n+2",
    "aromaticity",
    "T2N",
    "alexander-polynomial",
    "conjecture",
    "topology-to-chemistry",
  ],
  lean: { ref: "qou:QOU.Organic.huckelFromT2NInvariant",
    validation: "not_checked",
  },
  uses: [
    "lem:T2N-components",
    "lem:alexander-T2N-closed-form",
    "def:torus-knot-T2-odd-alexander",
  ],
  cites: [],
});
